#!/usr/bin/env python3
"""
HubSpot API Integration for Cowork Daily Orchestrator
Handles task retrieval with theme day prefix parsing (Option A)
"""

import os
import httpx
from typing import List, Dict, Optional, Any
from enum import Enum

class HubSpotAPI:
    """Wrapper for HubSpot CRM API."""
    
    def __init__(self, api_key: str, portal_id: str):
        self.api_key = api_key
        self.portal_id = portal_id
        self.base_url = "https://api.hubapi.com"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    async def search_tasks(self, owner_id: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Search for tasks owned by a specific user."""
        url = f"{self.base_url}/crm/v3/objects/tasks/search"
        
        payload = {
            "filterGroups": [
                {
                    "filters": [
                        {
                            "propertyName": "hubspot_owner_id",
                            "operator": "EQ",
                            "value": owner_id
                        },
                        {
                            "propertyName": "hs_task_status",
                            "operator": "IN",
                            "values": ["NOT_STARTED", "IN_PROGRESS"]
                        }
                    ]
                }
            ],
            "limit": limit,
            "properties": [
                "hs_task_body",
                "hs_task_priority",
                "hs_task_status",
                "hs_task_subject",
                "hubspot_owner_id",
                "hs_due_date"
            ]
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=self.headers, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                return data.get("results", [])
            except Exception as e:
                print(f"[HubSpot] Task search failed: {e}")
                return []
    
    async def update_task(self, task_id: str, properties: Dict[str, Any]) -> bool:
        """Update task properties."""
        url = f"{self.base_url}/crm/v3/objects/tasks/{task_id}"
        payload = {"properties": properties}
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.patch(url, json=payload, headers=self.headers, timeout=10.0)
                response.raise_for_status()
                return True
            except Exception as e:
                print(f"[HubSpot] Failed to update task {task_id}: {e}")
                return False

class HubSpotTaskManager:
    """Manages fetching and filtering HubSpot tasks."""
    
    THEME_DAY_PREFIXES = {
        "Monday": "[MON]",
        "Tuesday": "[TUE]",
        "Wednesday": "[WED]",
        "Thursday": "[THU]",
        "Friday": "[FRI]",
        "Saturday": "[SAT]"
    }
    
    def __init__(self, hubspot_api: HubSpotAPI, owner_id: str):
        self.hubspot = hubspot_api
        self.owner_id = owner_id
    
    async def fetch_todays_tasks(self, theme_day: str = "Monday") -> List[Dict[str, Any]]:
        """
        SCHEMA DECISION (Option A — LOCKED 2026-06-15):
        Theme day is encoded as a prefix in hs_task_subject: [MON], [TUE], [WED], [THU], [FRI]
        This honors Zap 2 governance: no custom properties, theme logic in task subject.
        
        Example: "[MON] Lauren Woolsey - Follow up on deal"
        """
        print(f"[HubSpotTasks] Fetching tasks for {theme_day}...")
        
        all_tasks = await self.hubspot.search_tasks(self.owner_id, limit=100)
        print(f"[HubSpotTasks] Total open tasks: {len(all_tasks)}")
        
        theme_prefix = self._get_theme_prefix(theme_day)
        filtered_tasks = []
        
        for task in all_tasks:
            props = task.get("properties", {})
            task_subject = props.get("hs_task_subject", "")
            task_prefix = self._extract_theme_from_subject(task_subject)
            
            if task_prefix == theme_prefix:
                filtered_tasks.append(self._parse_task(task))
        
        print(f"[HubSpotTasks] Tasks matching {theme_day} (prefix: {theme_prefix}): {len(filtered_tasks)}")
        filtered_tasks.sort(key=lambda t: (t.get("priority_order", 999), t.get("due_date", "")))
        
        return filtered_tasks
    
    def _parse_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Parse HubSpot task object into clean dict."""
        props = task.get("properties", {})
        
        priority_str = props.get("hs_task_priority", "medium")
        priority_order = {"high": 1, "medium": 2, "low": 3}.get(priority_str.lower(), 2)
        
        return {
            "id": task.get("id"),
            "name": props.get("hs_task_subject", props.get("hs_task_body", "Untitled Task")[:50]),
            "body": props.get("hs_task_body", ""),
            "status": props.get("hs_task_status", "NOT_STARTED"),
            "priority": priority_str,
            "priority_order": priority_order,
            "due_date": props.get("hs_due_date", "No due date"),
            "owner_id": props.get("hubspot_owner_id", "")
        }
    
    def _get_mock_tasks(self, theme_day: str = "Monday") -> List[Dict[str, Any]]:
        """Return mock tasks for testing."""
        mock_data = {
            "Monday": [
                {
                    "id": "mock_task_1",
                    "name": "[MON] Lauren Woolsey - Follow up on deal",
                    "body": "Discuss loan options for new property",
                    "status": "NOT_STARTED",
                    "priority": "high",
                    "priority_order": 1,
                    "due_date": "2026-06-16",
                    "owner_id": "66124405"
                },
                {
                    "id": "mock_task_2",
                    "name": "[MON] Realtor partnership call",
                    "body": "Discuss Q3 pipeline and referral strategy",
                    "status": "NOT_STARTED",
                    "priority": "medium",
                    "priority_order": 2,
                    "due_date": "2026-06-16",
                    "owner_id": "66124405"
                }
            ]
        }
        return mock_data.get(theme_day, [])
    
    def _get_theme_prefix(self, theme_day: str) -> str:
        """Get the expected prefix for a theme day."""
        return self.THEME_DAY_PREFIXES.get(theme_day, "[MON]")
    
    def _extract_theme_from_subject(self, subject: str) -> str:
        """Extract theme day prefix from task subject."""
        if not subject:
            return ""
        
        for prefix in self.THEME_DAY_PREFIXES.values():
            if subject.strip().startswith(prefix):
                return prefix
        
        return ""

if __name__ == "__main__":
    import asyncio
    
    async def test():
        api_key = os.environ.get("HUBSPOT_API_KEY", "test_key_missing")
        hubspot = HubSpotAPI(api_key if api_key != "test_key_missing" else "dummy", "242239760")
        manager = HubSpotTaskManager(hubspot, "66124405")
        
        tasks = manager._get_mock_tasks("Monday")
        print(f"[Test] Mock tasks: {len(tasks)}")
        for task in tasks:
            print(f"  [{task['priority'].upper()}] {task['name']}")
    
    asyncio.run(test())