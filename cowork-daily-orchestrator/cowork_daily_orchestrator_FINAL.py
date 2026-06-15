#!/usr/bin/env python3
"""
🎯 Cowork Daily Orchestrator
Scott W Thompson | MrMortgageMan™

Production skill for Cowork that surfaces four daily rituals:
- 6:00 AM: SignalStrike Approval Queue (8 posts ready for approval)
- 8:30 AM: Pre-Work Ritual Checkpoint + Theme Day Task Queue
- 5:00 PM: Pre-Leave Ritual Checkpoint
- 7:00 PM (Sunday): Sunday Night Ritual + Week Review

Uses real Notion + HubSpot data via MCP integrations.

Status: READY FOR COWORK DEPLOYMENT
Owner: Claude (Digital Chief of Staff)
Created: 2026-06-15
"""

import os
import asyncio
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional, Any

# Import integrations
try:
    from notion_integration import NotionAPI, SignalStrikeQueueManager
    from hubspot_integration import HubSpotAPI, HubSpotTaskManager
except ImportError:
    print("[Warning] Integration modules not found. Using mock data.")
    NotionAPI = None
    HubSpotAPI = None

# ============================================================================
# CONFIGURATION
# ============================================================================

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
HUBSPOT_API_KEY = os.environ.get("HUBSPOT_API_KEY", "")

# Scott's IDs (locked)
HUBSPOT_PORTAL_ID = "242239760"
HUBSPOT_OWNER_ID = "66124405"
SCOTT_TIMEZONE = "America/Los_Angeles"  # Pacific Time

# ============================================================================
# THEME DAY ENUM (Locked)
# ============================================================================

class ThemeDay(Enum):
    MONDAY = {
        "name": "Agent Call + Signal Review Day",
        "time_block": "10 AM - 1 PM",
        "focus": "B2B Realtor/FA outreach",
        "target": "12+ conversations",
        "tag": "MONDAY"
    }
    TUESDAY = {
        "name": "First Touch / Listing Touch Day",
        "time_block": "11 AM - 2 PM",
        "focus": "Active listing agents + pipeline mgmt",
        "target": "Team meeting + calls",
        "tag": "TUESDAY"
    }
    WEDNESDAY = {
        "name": "Content + Follow-Up Day",
        "time_block": "10 AM - 1 PM",
        "focus": "Preapprovals (A/B/C urgency)",
        "target": "5+ PALs weekly",
        "tag": "WEDNESDAY"
    }
    THURSDAY = {
        "name": "Client Call / ILC Day",
        "time_block": "10 AM - 1 PM",
        "focus": "Past clients (7-day ritual cycles)",
        "target": "50 conversations",
        "tag": "THURSDAY"
    }
    FRIDAY = {
        "name": "Follow-Up Runway + Weekly Review",
        "time_block": "Flexible",
        "focus": "Clear overdue, catch-up, momentum",
        "target": "Flexible (catch-up)",
        "tag": "FRIDAY"
    }
    SATURDAY = {
        "name": "Power Hour Volume Calling",
        "time_block": "1 - 2 PM",
        "focus": "High-velocity Realtor touches",
        "target": "50+ conversations",
        "tag": "SATURDAY"
    }
    
    @staticmethod
    def get_today():
        """Get today's theme."""
        day_name = datetime.now().strftime("%A").upper()
        return ThemeDay[day_name] if day_name in ThemeDay.__members__ else ThemeDay.MONDAY

# ============================================================================
# MODULE 1: 6 AM — SIGNALSTRIKE APPROVAL QUEUE
# ============================================================================

class SignalStrikeModule:
    """6 AM - SignalStrike Approval Queue"""
    
    def __init__(self):
        self.notion = None
        self.queue_manager = None
        self.posts = []
    
    async def initialize(self):
        """Set up Notion integration."""
        if NOTION_API_KEY:
            self.notion = NotionAPI(NOTION_API_KEY)
            self.queue_manager = SignalStrikeQueueManager(self.notion)
            await self.queue_manager.find_queue_database()
    
    async def fetch_posts(self, limit: int = 8):
        """Fetch pending posts."""
        if self.queue_manager:
            self.posts = await self.queue_manager.fetch_pending_posts(limit)
        else:
            self.posts = self._get_mock_posts()[:limit]
    
    def render(self) -> str:
        """Render 6 AM queue UI."""
        output = """
╔════════════════════════════════════════════════════════════════════════════╗
║                   🎯 SIGNALSTRIKE APPROVAL QUEUE                           ║
║                        Ready for Review (6:00 AM)                          ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
        
        for i, post in enumerate(self.posts, 1):
            output += f"""
{i}. [{post['platform'].upper()}] {post['agent_name']}
   "{post['post_excerpt']}"
   
   Claude's comment:
   → {post['my_comment']}
   
   [ ✅ APPROVE ]  [ ⏭️  SKIP ]
"""
        
        output += f"""
───────────────────────────────────────────────────────────────────────────────
Queue refreshes nightly at 11:59 PM | {len(self.posts)} posts queued (target: 8)
"""
        return output
    
    def _get_mock_posts(self) -> List[Dict]:
        """Mock data for testing."""
        return [
            {
                "agent_name": "Lauren Woolsey",
                "post_excerpt": "Just closed another 5-bed in Danville!",
                "my_comment": "Great work on the volume, Lauren. Market's shifting your way.",
                "post_url": "https://facebook.com/...",
                "platform": "facebook",
                "status": "PENDING"
            },
            {
                "agent_name": "Alka Sabherwal",
                "post_excerpt": "Market shifting to buyer advantage",
                "my_comment": "Exactly right. Inventory levels tell the story.",
                "post_url": "https://linkedin.com/...",
                "platform": "linkedin",
                "status": "PENDING"
            }
        ]

# ============================================================================
# MODULE 2: 8:30 AM — PRE-WORK RITUAL + THEME DAY QUEUE
# ============================================================================

class PreWorkModule:
    """8:30 AM - Pre-Work Ritual + Theme Day Task Queue"""
    
    def __init__(self, theme_day: ThemeDay):
        self.theme_day = theme_day
        self.hubspot = None
        self.task_manager = None
        self.tasks = []
    
    async def initialize(self):
        """Set up HubSpot integration."""
        if HUBSPOT_API_KEY:
            self.hubspot = HubSpotAPI(HUBSPOT_API_KEY, HUBSPOT_PORTAL_ID)
            self.task_manager = HubSpotTaskManager(self.hubspot, HUBSPOT_OWNER_ID)
    
    async def fetch_tasks(self):
        """Fetch today's theme-filtered tasks."""
        if self.task_manager:
            self.tasks = await self.task_manager.fetch_todays_tasks(self.theme_day.name)
        else:
            self.tasks = self._get_mock_tasks()
    
    def render(self) -> str:
        """Render 8:30 AM pre-work ritual UI."""
        theme = self.theme_day.value
        
        output = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                      📋 PRE-WORK RITUAL CHECKPOINT                         ║
║                         (8:30 AM — 30 minutes)                            ║
╚════════════════════════════════════════════════════════════════════════════╝

🎯 Today's Theme: {theme['name'].upper()}
⏰ Time Block: {theme['time_block']}
📊 Target: {theme['target']}
🎯 Focus: {theme['focus']}

───────────────────────────────────────────────────────────────────────────────
CHECKLIST (Complete these before {theme['time_block'].split()[0]} start):
───────────────────────────────────────────────────────────────────────────────

☐ Opened the Boardroom (Active Batons, Open Decisions)
☐ Scanned HubSpot queue for today
☐ Confirmed prep complete (no overdue items from Friday)
☐ Ready to start at {theme['time_block'].split()[0]}?

───────────────────────────────────────────────────────────────────────────────
YOUR CALL QUEUE FOR TODAY ({theme['name']}):
───────────────────────────────────────────────────────────────────────────────
"""
        
        for i, task in enumerate(self.tasks, 1):
            priority_icon = "🔴" if task['priority'].lower() == "high" else "🟡"
            output += f"\n{i}. {priority_icon} {task['name']}"
            output += f"\n   Due: {task['due_date']}"
        
        output += """

───────────────────────────────────────────────────────────────────────────────

[ 🚀 START CALLS ]  [ ⏸️  NEED MORE TIME ]
"""
        return output
    
    def _get_mock_tasks(self) -> List[Dict]:
        """Mock data for testing."""
        return [
            {
                "id": "mock_1",
                "name": "Lauren Woolsey - Follow up on deal",
                "priority": "high",
                "due_date": "2026-06-16"
            },
            {
                "id": "mock_2",
                "name": "Realtor partnership call",
                "priority": "medium",
                "due_date": "2026-06-16"
            }
        ]

# ============================================================================
# MODULE 3: 5 PM — PRE-LEAVE RITUAL
# ============================================================================

class PreLeaveModule:
    """5 PM - Pre-Leave Ritual Checkpoint"""
    
    def __init__(self, theme_day: ThemeDay):
        self.theme_day = theme_day
    
    def render(self) -> str:
        """Render 5 PM pre-leave ritual UI."""
        theme = self.theme_day.value
        
        output = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                      📋 PRE-LEAVE RITUAL CHECKPOINT                        ║
║                        (5:00 PM — 15-30 minutes)                          ║
╚════════════════════════════════════════════════════════════════════════════╝

{theme['name'].upper()} SCORECARD:

✅ or ❌ Did you hit {theme['target']}?
✅ or ❌ Did you send your email newsletter?
✅ or ❌ Did you engage on social (3+ agents)?

───────────────────────────────────────────────────────────────────────────────
WHO STILL NEEDS TO HEAR FROM YOU TODAY?
───────────────────────────────────────────────────────────────────────────────

[Text answer here]

───────────────────────────────────────────────────────────────────────────────

[ ✅ YES, DONE FOR TODAY ]  [ ⏸️  NO, NEED 10 MORE MIN ]
"""
        return output

# ============================================================================
# MODULE 4: SUNDAY 7 PM — SUNDAY NIGHT RITUAL
# ============================================================================

class SundayNightModule:
    """Sunday 7 PM - Week Review + Preview"""
    
    def render(self) -> str:
        """Render Sunday night ritual UI."""
        output = """
╔════════════════════════════════════════════════════════════════════════════╗
║                   📋 SUNDAY NIGHT RITUAL — WEEK REVIEW                     ║
║                      (7:00 PM — 30-60 minutes)                            ║
╚════════════════════════════════════════════════════════════════════════════╝

WEEK REVIEW (This past week):
───────────────────────────────────────────────────────────────────────────────
☐ Did you hit 5+ PALs? Count: ___
☐ Did you reach 50+ past clients? Count: ___
☐ Active preapproval pipeline size: ___
☐ Top win this week: _______________
☐ One thing to improve next week: _______________

NEXT WEEK PREVIEW (Next week):
───────────────────────────────────────────────────────────────────────────────
☐ Monday targets loaded (12+ Realtors)
☐ Tuesday pipeline reviewed
☐ Wednesday preapproval queue ready
☐ Thursday past client list ready
☐ Friday flex day prepared

───────────────────────────────────────────────────────────────────────────────

[ ✅ YES, READY FOR MONDAY ]  [ ⏸️  NO, NEED TO PREPARE ]
"""
        return output

# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

class CoworkDailyOrchestrator:
    """Main orchestrator - determines which module to surface."""
    
    def __init__(self):
        self.current_theme = ThemeDay.get_today()
        self.current_time = datetime.now()
        self.modules = {}
    
    async def initialize(self):
        """Initialize all modules and integrations."""
        print("[Orchestrator] Initializing Cowork Daily Orchestrator...")
        
        self.modules['signalstrike'] = SignalStrikeModule()
        await self.modules['signalstrike'].initialize()
        
        self.modules['prework'] = PreWorkModule(self.current_theme)
        await self.modules['prework'].initialize()
        
        self.modules['preleave'] = PreLeaveModule(self.current_theme)
        self.modules['sunday'] = SundayNightModule()
        
        print("[Orchestrator] Initialization complete")
    
    async def run(self):
        """Main execution loop."""
        await self.initialize()
        
        current_hour = self.current_time.hour
        current_min = self.current_time.minute
        day_name = self.current_time.strftime("%A")
        
        print(f"\n[{current_hour:02d}:{current_min:02d}] Cowork Daily Orchestrator for {day_name}\n")
        
        if 5 <= current_hour < 7:
            print("[6:00 AM] Fetching SignalStrike queue...")
            await self.modules['signalstrike'].fetch_posts()
            print(self.modules['signalstrike'].render())
        
        elif 8 <= current_hour < 10:
            print("[8:30 AM] Fetching pre-work tasks...")
            await self.modules['prework'].fetch_tasks()
            print(self.modules['prework'].render())
        
        elif 17 <= current_hour < 18:
            print("[5:00 PM] Rendering pre-leave ritual...")
            print(self.modules['preleave'].render())
        
        elif 19 <= current_hour < 20 and day_name == "Sunday":
            print("[7:00 PM Sun] Rendering Sunday night ritual...")
            print(self.modules['sunday'].render())
        
        else:
            print(f"[No ritual scheduled for {current_hour:02d}:{current_min:02d}]")
            print("\nNext scheduled rituals:")
            print("  • 6:00 AM: SignalStrike Approval Queue")
            print("  • 8:30 AM: Pre-Work Ritual + Theme Day Queue")
            print("  • 5:00 PM: Pre-Leave Ritual")
            print("  • 7:00 PM (Sunday): Sunday Night Ritual")
    
    def get_current_status(self) -> Dict[str, Any]:
        """Return current status for Cowork dashboard."""
        return {
            "timestamp": self.current_time.isoformat(),
            "theme_day": self.current_theme.name if self.current_theme else "Unknown",
            "theme_name": self.current_theme.value['name'] if self.current_theme else "",
            "next_ritual": self._get_next_ritual(),
            "ready": True
        }
    
    def _get_next_ritual(self) -> str:
        """Determine next scheduled ritual."""
        hour = self.current_time.hour
        if hour < 6:
            return "6:00 AM - SignalStrike Queue"
        elif hour < 8:
            return "8:30 AM - Pre-Work Ritual"
        elif hour < 17:
            return "5:00 PM - Pre-Leave Ritual"
        elif self.current_time.weekday() != 6:
            return "8:30 AM (next day) - Pre-Work Ritual"
        else:
            return "7:00 PM - Sunday Night Ritual"

if __name__ == "__main__":
    orchestrator = CoworkDailyOrchestrator()
    asyncio.run(orchestrator.run())