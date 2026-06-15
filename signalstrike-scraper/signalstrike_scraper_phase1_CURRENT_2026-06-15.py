#!/usr/bin/env python3
"""
🎯 SignalStrike Scraper - Phase 1
Scott W Thompson | MrMortgageMan™

Nightly automation that scrapes agent social posts and queues them for Scott's approval.

PHASE 1 SCOPE (Fri 6/13 - Fri 6/18):
- 3 test agents ONLY (Lauren Woolsey, Alka Sabherwal, Jordan Wright)
- Facebook public posts only (NOT Instagram/LinkedIn yet)
- Nightly at 11:00 PM PT
- 3-7 day gap enforcement (no touches within window)
- Template randomization (no repeats to same agent)
- Queue 8 posts/night to Notion for Scott's 6 AM approval

STATUS: ARCHITECTURE LOCKED (2026-06-12)
OWNER: Claude (Digital Chief of Staff)
CREATED: 2026-06-15
TARGET: Phase 1 QA complete by Fri 6/18
"""

import os
import asyncio
import json
import random
import httpx
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from dataclasses import dataclass

# ============================================================================
# CONFIGURATION - PHASE 1 (3 TEST AGENTS ONLY)
# ============================================================================

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
CLAUDE_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Phase 1: Hard-coded test agents (do NOT read from full watchlist)
TEST_AGENTS = [
    {
        "name": "Lauren Woolsey",
        "tier": "A",
        "facebook_url": "https://www.facebook.com/lauren.woolsey",
        "instagram_handle": "lauren_woolsey",
        "linkedin_url": "https://www.linkedin.com/in/lauren-woolsey",
        "last_touch_date": "2026-06-10",  # Example: 5 days ago
        "specialty": "High-volume residential sales in Bay Area",
        "recent_templates": []  # Track templates used for this agent
    },
    {
        "name": "Alka Sabherwal",
        "tier": "B",
        "facebook_url": "https://www.facebook.com/alka.sabherwal",
        "instagram_handle": "alka_sabherwal",
        "linkedin_url": "https://www.linkedin.com/in/alka-sabherwal",
        "last_touch_date": "2026-06-09",  # Example: 6 days ago
        "specialty": "First-time homebuyers, market insights",
        "recent_templates": []
    },
    {
        "name": "Jordan Wright",
        "tier": "A",
        "facebook_url": "https://www.facebook.com/jordan.wright",
        "instagram_handle": "jordan_wright",
        "linkedin_url": "https://www.linkedin.com/in/jordan-wright",
        "last_touch_date": "2026-06-08",  # Example: 7 days ago
        "specialty": "Investment properties, market analysis",
        "recent_templates": []
    }
]

# Response library templates (Phase 1: market insight focused)
RESPONSE_TEMPLATES = {
    "market_insight": [
        "Great insight on {detail}. You're reading the market correctly right now.",
        "Exactly right. {detail} is the real story in {market}.",
        "{detail} + inventory = the winning formula. You're ahead of the curve.",
        "You're seeing {detail} before most do. That's the competitive edge.",
        "{detail} is the insight that wins deals. Spot on."
    ],
    "congratulations": [
        "Nice close on {detail}. Volume like that doesn't happen by accident.",
        "Another win. {detail} shows the consistency. Keep it up.",
        "That's the third {detail} this month. You're running the table."
    ],
    "market_shift": [
        "Market's shifting to {detail}. Good timing on this post.",
        "{detail} is the change everyone's talking about but not acting on yet.",
        "The {detail} shift is real. Smart to be ahead of it."
    ]
}

# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class FacebookPost:
    """Represents a single Facebook post."""
    url: str
    text: str
    timestamp: datetime
    like_count: int
    comment_count: int
    extracted_detail: Optional[str] = None

@dataclass
class QueuedPost:
    """Post queued for Scott's approval."""
    agent_name: str
    post_excerpt: str
    my_comment: str
    post_url: str
    platform: str
    timestamp_scraped: datetime
    status: str = "PENDING"
    template_used: str = ""
    gap_days: int = 0

# ============================================================================
# PHASE 1: GAP ENFORCEMENT
# ============================================================================

def days_since_last_touch(agent: Dict[str, Any]) -> int:
    """
    Calculate days since last touch to agent.
    
    Returns:
        Integer number of days. If date is today, returns 0.
    """
    try:
        last_touch = datetime.strptime(agent["last_touch_date"], "%Y-%m-%d").date()
        today = datetime.now().date()
        delta = (today - last_touch).days
        return delta
    except Exception as e:
        print(f"[Gap] Error calculating gap for {agent['name']}: {e}")
        return 0

def is_within_gap_window(agent: Dict[str, Any]) -> bool:
    """
    Check if agent is within 3-7 day gap window.
    
    Returns:
        True if gap < 3 days OR gap > 7 days (skip post)
        False if gap is 3-7 days (allow post)
    """
    gap = days_since_last_touch(agent)
    
    # Skip if gap < 3 days OR gap > 7 days
    if gap < 3 or gap > 7:
        return True  # Within gap window, skip
    
    return False  # Outside gap window, allow

# ============================================================================
# PHASE 1: TEMPLATE RANDOMIZATION
# ============================================================================

def pick_random_template(agent: Dict[str, Any], context: str = "market_insight") -> tuple:
    """
    Pick a random template that hasn't been used recently for this agent.
    
    Args:
        agent: Agent dict
        context: Template category (market_insight, congratulations, market_shift)
    
    Returns:
        Tuple of (template_text, template_id)
    """
    templates = RESPONSE_TEMPLATES.get(context, RESPONSE_TEMPLATES["market_insight"])
    
    # Filter out recently used templates
    available = [t for t in templates if t not in agent.get("recent_templates", [])]
    
    # If all used recently, reset and pick from all
    if not available:
        available = templates
        agent["recent_templates"] = []
    
    picked = random.choice(available)
    template_id = f"{context}#{templates.index(picked) + 1}"
    
    # Track this template for this agent
    agent["recent_templates"].append(picked)
    if len(agent["recent_templates"]) > 3:  # Keep last 3
        agent["recent_templates"].pop(0)
    
    return picked, template_id

# ============================================================================
# PHASE 1: COMMENT DRAFTING (Claude API)
# ============================================================================

async def draft_comment_with_claude(
    agent_name: str,
    post_detail: str,
    agent_specialty: str,
    market: str = "Bay Area"
) -> str:
    """
    Draft a specific comment using Claude API.
    
    Pulls one detail from the post and creates context-specific comment.
    """
    if not CLAUDE_API_KEY:
        print(f"[Claude] API key not set. Using mock comment.")
        # Fallback to template-based mock
        templates = RESPONSE_TEMPLATES["market_insight"]
        template = random.choice(templates)
        return template.format(detail=post_detail, market=market)
    
    prompt = f"""You are Scott Thompson, a mortgage strategist. 
An agent posted on social media: "{post_detail}"
Agent specialty: {agent_specialty}
Agent name: {agent_name}

Draft a SPECIFIC (not generic) response comment that:
1. Pulls out ONE detail from their post
2. Shows you understand their market position
3. Is 1-2 sentences max
4. Sounds like a coach, not a salesman
5. Builds on their insight, doesn't repeat it

Response (comment text only, no quotes):"""
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": CLAUDE_API_KEY,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                },
                json={
                    "model": "claude-opus-4-6",
                    "max_tokens": 150,
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                comment = data["content"][0]["text"].strip()
                print(f"[Claude] Comment drafted: {comment[:50]}...")
                return comment
            else:
                print(f"[Claude] API error {response.status_code}. Using template fallback.")
                return pick_random_template({"recent_templates": []}, "market_insight")[0]
    
    except Exception as e:
        print(f"[Claude] Error: {e}. Using template fallback.")
        template, _ = pick_random_template({"recent_templates": []}, "market_insight")
        return template.format(detail=post_detail, market="Bay Area")

# ============================================================================
# PHASE 1: FACEBOOK SCRAPING (Mock for now)
# ============================================================================

async def scrape_facebook_posts(agent: Dict[str, Any], hours: int = 48) -> List[FacebookPost]:
    """
    Scrape public posts from agent's Facebook profile.
    
    Phase 1: Mock implementation (returns test posts)
    Phase 2: Implement with Playwright/BeautifulSoup
    """
    print(f"[Facebook] Scraping {agent['name']} (URL: {agent['facebook_url']})...")
    
    # MOCK DATA for Phase 1 testing
    mock_posts = {
        "Lauren Woolsey": [
            FacebookPost(
                url="https://facebook.com/lauren.woolsey/posts/12345",
                text="Just closed another 5-bed home in Danville! Market's moving fast.",
                timestamp=datetime.now() - timedelta(hours=2),
                like_count=24,
                comment_count=5,
                extracted_detail="5-bed closes in Danville"
            ),
            FacebookPost(
                url="https://facebook.com/lauren.woolsey/posts/12346",
                text="Spring market heating up. Inventory down 15% YoY.",
                timestamp=datetime.now() - timedelta(hours=18),
                like_count=31,
                comment_count=8,
                extracted_detail="Inventory down 15% YoY"
            )
        ],
        "Alka Sabherwal": [
            FacebookPost(
                url="https://facebook.com/alka.sabherwal/posts/54321",
                text="Market shifting to buyer advantage. First-time buyers have leverage again.",
                timestamp=datetime.now() - timedelta(hours=6),
                like_count=18,
                comment_count=3,
                extracted_detail="Buyer advantage in market"
            )
        ],
        "Jordan Wright": [
            FacebookPost(
                url="https://facebook.com/jordan.wright/posts/99999",
                text="Investment property appreciation + rental income = wealth building. Numbers don't lie.",
                timestamp=datetime.now() - timedelta(hours=12),
                like_count=42,
                comment_count=11,
                extracted_detail="Investment + rental income strategy"
            )
        ]
    }
    
    # Return mock posts for this agent
    posts = mock_posts.get(agent["name"], [])
    print(f"[Facebook] Found {len(posts)} posts from {agent['name']}")
    
    # Simulate request delay (respectful scraping)
    await asyncio.sleep(random.uniform(2, 4))
    
    return posts

# ============================================================================
# PHASE 1: NOTION INTEGRATION (Mock for now)
# ============================================================================

async def write_to_approval_queue(posts: List[QueuedPost]) -> bool:
    """
    Write queued posts to Notion SIGNALSTRIKE_APPROVAL_QUEUE.
    
    Phase 1: Mock implementation
    Phase 2: Implement with Notion API
    """
    print(f"[Notion] Writing {len(posts)} posts to approval queue...")
    
    for post in posts:
        print(f"  ✓ {post.agent_name}: {post.post_excerpt[:50]}...")
    
    # Mock write
    return True

async def write_to_execution_log(posts: List[QueuedPost]) -> bool:
    """
    Write execution details to Notion SIGNALSTRIKE_EXECUTION_LOG.
    
    Phase 1: Mock implementation
    Phase 2: Implement with Notion API
    """
    print(f"[Notion] Logging {len(posts)} execution entries...")
    
    for post in posts:
        print(f"  ✓ {post.agent_name} | Gap: {post.gap_days} days | Template: {post.template_used}")
    
    # Mock write
    return True

# ============================================================================
# MAIN ORCHESTRATOR - PHASE 1
# ============================================================================

class SignalStrikeScraperPhase1:
    """Main orchestrator for Phase 1 scraper (3 test agents, Facebook only)."""
    
    def __init__(self):
        self.agents = TEST_AGENTS.copy()
        self.queued_posts: List[QueuedPost] = []
        self.execution_log: List[Dict[str, Any]] = []
        self.start_time = datetime.now()
    
    async def run(self):
        """Main execution flow."""
        print("\n" + "="*80)
        print("🎯 SignalStrike Scraper - Phase 1")
        print("="*80)
        print(f"Start time: {self.start_time}")
        print(f"Test agents: {len(self.agents)}")
        print(f"Platform: Facebook only")
        print("="*80 + "\n")
        
        # Process each test agent
        for agent in self.agents:
            await self.process_agent(agent)
            
            # Rate limiting: delay between agents
            await asyncio.sleep(random.uniform(3, 7))
        
        # Write results to Notion
        await self.finalize()
        
        print("\n" + "="*80)
        print(f"✅ Phase 1 scraper complete")
        print(f"Posts queued: {len(self.queued_posts)}")
        print(f"Execution log entries: {len(self.execution_log)}")
        print("="*80 + "\n")
    
    async def process_agent(self, agent: Dict[str, Any]):
        """Process a single agent."""
        print(f"\n[Agent] Processing {agent['name']} (Tier {agent['tier']})...")
        
        # Calculate gap
        gap_days = days_since_last_touch(agent)
        print(f"  Gap since last touch: {gap_days} days")
        
        # Check gap enforcement
        if is_within_gap_window(agent):
            print(f"  ⏭️  Skipped: Within 3-7 day gap window")
            return
        
        # Scrape posts
        posts = await scrape_facebook_posts(agent)
        
        if not posts:
            print(f"  ℹ️  No new posts found")
            return
        
        # Process each post
        for post in posts:
            await self.process_post(agent, post, gap_days)
    
    async def process_post(self, agent: Dict[str, Any], post: FacebookPost, gap_days: int):
        """Process a single post."""
        print(f"\n  [Post] {post.text[:60]}...")
        
        # Draft comment
        template, template_id = pick_random_template(agent, "market_insight")
        comment = await draft_comment_with_claude(
            agent_name=agent["name"],
            post_detail=post.extracted_detail,
            agent_specialty=agent["specialty"]
        )
        
        # Check comment quality (not empty)
        if not comment or len(comment) < 10:
            print(f"  ❌ Comment too short or empty. Skipping.")
            return
        
        # Queue post
        queued = QueuedPost(
            agent_name=agent["name"],
            post_excerpt=post.text[:100],
            my_comment=comment,
            post_url=post.url,
            platform="facebook",
            timestamp_scraped=datetime.now(),
            status="PENDING",
            template_used=template_id,
            gap_days=gap_days
        )
        
        self.queued_posts.append(queued)
        print(f"  ✅ Queued: {comment[:50]}...")
        
        # Log execution
        self.execution_log.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "agent_name": agent["name"],
            "platform": "facebook",
            "post_url": post.url,
            "comment_text": comment,
            "gap_days": gap_days,
            "template_used": template_id,
            "status": "SUCCESS"
        })
        
        # Rate limiting: delay between posts
        await asyncio.sleep(random.uniform(1, 2))
    
    async def finalize(self):
        """Write results to Notion and generate report."""
        print("\n[Finalize] Writing to Notion...")
        
        # Write to approval queue
        await write_to_approval_queue(self.queued_posts)
        
        # Write to execution log
        await write_to_execution_log(self.queued_posts)
        
        # Print execution summary
        print("\n" + "-"*80)
        print("EXECUTION SUMMARY")
        print("-"*80)
        for entry in self.execution_log:
            print(f"{entry['date']} | {entry['agent_name']:15} | {entry['gap_days']:2}d gap | {entry['template_used']}")
        print("-"*80)
    
    def get_status(self) -> Dict[str, Any]:
        """Return current status."""
        return {
            "status": "complete",
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "agents_processed": len(self.agents),
            "posts_queued": len(self.queued_posts),
            "execution_log_entries": len(self.execution_log),
            "queued_posts": [
                {
                    "agent": p.agent_name,
                    "excerpt": p.post_excerpt[:50],
                    "comment": p.my_comment[:50],
                    "status": p.status
                }
                for p in self.queued_posts
            ]
        }

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    scraper = SignalStrikeScraperPhase1()
    asyncio.run(scraper.run())
    
    # Print final status
    import json
    status = scraper.get_status()
    print("\n[Status]")
    print(json.dumps(status, indent=2, default=str))
