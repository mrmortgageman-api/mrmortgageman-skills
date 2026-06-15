#!/usr/bin/env python3
"""
Notion API Integration for Cowork Daily Orchestrator
Handles all Notion data retrieval
"""

import os
import httpx
from typing import List, Dict, Optional, Any

class NotionAPI:
    """Wrapper for Notion API calls."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
    
    async def search_database(self, query: str, type_filter: str = "database") -> Optional[str]:
        """Search for a database by name to get its ID."""
        url = f"{self.base_url}/search"
        payload = {
            "query": query,
            "filter": {"value": type_filter, "property": "object"}
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=self.headers, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                
                if data.get("results"):
                    return data["results"][0]["id"]
                return None
            except Exception as e:
                print(f"[Error] Notion search failed: {e}")
                return None
    
    async def query_database(self, database_id: str, filter_config: Optional[Dict] = None) -> List[Dict[str, Any]]:
        """Query a Notion database with optional filters."""
        url = f"{self.base_url}/databases/{database_id}/query"
        payload = {}
        
        if filter_config:
            payload["filter"] = filter_config
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, headers=self.headers, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                return data.get("results", [])
            except Exception as e:
                print(f"[Error] Database query failed: {e}")
                return []

class SignalStrikeQueueManager:
    """Manages fetching and processing SignalStrike approval queue."""
    
    def __init__(self, notion_api: NotionAPI):
        self.notion = notion_api
        self.queue_db_id = None
    
    async def find_queue_database(self) -> bool:
        """Search for SIGNALSTRIKE_APPROVAL_QUEUE database."""
        print("[SignalStrikeQueue] Searching for SIGNALSTRIKE_APPROVAL_QUEUE database...")
        self.queue_db_id = await self.notion.search_database("SIGNALSTRIKE_APPROVAL_QUEUE")
        
        if self.queue_db_id:
            print(f"[SignalStrikeQueue] Found database: {self.queue_db_id}")
            return True
        else:
            print("[SignalStrikeQueue] Database not found. Using mock data.")
            return False
    
    async def fetch_pending_posts(self, limit: int = 8) -> List[Dict[str, Any]]:
        """Fetch pending posts from SIGNALSTRIKE_APPROVAL_QUEUE."""
        if not self.queue_db_id:
            print("[SignalStrikeQueue] Using mock data (database not found)")
            return self._get_mock_data(limit)
        
        filter_config = {
            "property": "status",
            "select": {"equals": "PENDING"}
        }
        
        pages = await self.notion.query_database(self.queue_db_id, filter_config=filter_config)
        
        posts = []
        for page in pages[:limit]:
            props = page.get("properties", {})
            post = {
                "id": page["id"],
                "agent_name": self._extract_property(props, "agent_name", ""),
                "post_excerpt": self._extract_property(props, "post_excerpt", ""),
                "my_comment": self._extract_property(props, "my_comment", ""),
                "post_url": self._extract_property(props, "post_url", ""),
                "platform": self._extract_property(props, "platform", ""),
                "status": self._extract_property(props, "status", "PENDING")
            }
            posts.append(post)
        
        print(f"[SignalStrikeQueue] Fetched {len(posts)} pending posts")
        return posts
    
    def _extract_property(self, props: Dict, key: str, default: Any = None) -> Any:
        """Extract a property from Notion page properties object."""
        if key not in props:
            return default
        
        prop = props[key]
        prop_type = prop.get("type", "")
        
        if prop_type == "title":
            return "".join([t["plain_text"] for t in prop.get("title", [])])
        elif prop_type == "rich_text":
            return "".join([t["plain_text"] for t in prop.get("rich_text", [])])
        elif prop_type == "select":
            return prop.get("select", {}).get("name", default)
        elif prop_type == "url":
            return prop.get("url", default)
        else:
            return default
    
    def _get_mock_data(self, limit: int = 8) -> List[Dict[str, Any]]:
        """Return mock data for testing."""
        return [
            {
                "id": "mock_1",
                "agent_name": "Lauren Woolsey",
                "post_excerpt": "Just closed another 5-bed in Danville!",
                "my_comment": "Great work on the volume, Lauren. Market's shifting your way.",
                "post_url": "https://facebook.com/...",
                "platform": "facebook",
                "status": "PENDING"
            }
        ]

if __name__ == "__main__":
    import asyncio
    
    async def test():
        api_key = os.environ.get("NOTION_API_KEY", "test_key_missing")
        manager = SignalStrikeQueueManager(NotionAPI(api_key if api_key != "test_key_missing" else "dummy"))
        posts = await manager.fetch_pending_posts()
        print(f"[Test] Posts: {len(posts)}")
    
    asyncio.run(test())