#!/usr/bin/env python3
"""
SignalStrike Scraper - Phase 1
Scott W Thompson | MrMortgageMan(tm)

Nightly automation that scrapes agent social posts and queues them for Scott's approval.

PHASE 1 SCOPE (6/13 - 6/18/2026):
- 3 test agents ONLY (Lauren Woolsey, Jordan Kim, Marcus Rivera)
- Facebook public posts only (NOT Instagram/LinkedIn yet)
- Nightly at 11:00 PM PT
- Gap enforcement: skip < 3 days, process 3-7 days, process overdue if > 7 days
- Template randomization (no repeats to same agent)
- Writes to Airtable: Signals Queue + Daily Command Queue

DEPLOYMENT NOTE (2026-06-15):
Phase 1 is deployed via Cowork MCP-native scheduled task (signalstrike-nightly-phase1).
That task calls Airtable MCP tools directly and does NOT require this script or API keys.
This script serves as the reference architecture for Phase 2 (real Facebook scraping).

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

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY", "")
AIRTABLE_BASE_ID = "appfcDd6KyNAnZNVH"
AIRTABLE_SIGNALS_QUEUE_TABLE = "tblkUMWXZKBUMBU7W"
AIRTABLE_COMMAND_QUEUE_TABLE = "tblEatDP2bx67PfS7"

CLAUDE_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Phase 1: Hard-coded test agents (do NOT read from full watchlist)
# Names must exactly match Airtable Agents table
TEST_AGENTS = [
    {
        "name": "Lauren Woolsey",
        "tier": "A",
        "facebook_url": "https://www.facebook.com/lauren.woolsey",
        "last_touch_date": "2026-06-07",  # 8+ days ago - overdue
        "specialty": "High-volume residential sales, Danville/Tri-Valley",
        "recent_templates": []
    },
    {
        "name": "Jordan Kim",
        "tier": "A",
        "facebook_url": "https://www.facebook.com/jordan.kim.realtor",
        "last_touch_date": "2026-06-07",  # 8+ days ago - overdue
        "specialty": "Investment properties, cap rate analysis, Walnut Creek",
        "recent_templates": []
    },
    {
        "name": "Marcus Rivera",
        "tier": "B",
        "facebook_url": "https://www.facebook.com/marcus.rivera.realtor",
        "last_touch_date": "2026-06-07",  # 8+ days ago - overdue
        "specialty": "Move-up buyers, $800K-$1.2M range, Pleasanton",
        "recent_templates": []
    }
]

# Response library templates (Phase 1: market insight focused)
RESPONSE_TEMPLATES = {
    "market_insight": [
        "Great insight on {detail}. You're reading the market correctly right now.",
        "Exactly right. {detail} is the real story in {market}.",
        "{detail} is the insight that wins deals. Spot on.",
        "You're seeing {detail} before most do. That's the competitive edge."
    ],
    "congratulations": [
        "Nice close on {detail}. Volume like that doesn't happen by accident.",
        "Another win. {detail} shows the consistency. Keep it up."
    ],
    "market_shift": [
        "Market's shifting to {detail}. Good timing on this post.",
        "{detail} is the change everyone's talking about but not acting on yet."
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
    agent_tier: str
    post_excerpt: str
    my_comment: str
    post_url: str
    platform: str
    timestamp_scraped: datetime
    status: str = "Pending Review"
    template_used: str = ""
    gap_days: int = 0
    engagement_score: int = 0

# ============================================================================
# PHASE 1: GAP ENFORCEMENT
# ============================================================================

def days_since_last_touch(agent: Dict[str, Any]) -> int:
    """Calculate days since last touch to agent."""
    try:
        last_touch = datetime.strptime(agent["last_touch_date"], "%Y-%m-%d").date()
        today = datetime.now().date()
        return (today - last_touch).days
    except Exception as e:
        print(f"[Gap] Error calculating gap for {agent['name']}: {e}")
        return 0

def should_skip_agent(agent: Dict[str, Any]) -> tuple:
    """
    Determine if agent should be skipped based on gap enforcement rules.

    Rules:
    - Gap < 3 days: SKIP (too recent)
    - Gap 3-7 days: PROCESS (normal priority)
    - Gap > 7 days: PROCESS (overdue, elevated priority)

    Returns:
        (skip: bool, reason: str)
    """
    gap = days_since_last_touch(agent)

    if gap < 3:
        return True, f"Too recent ({gap} days since last touch, minimum 3)"

    if gap > 7:
        return False, f"Overdue ({gap} days, elevated priority)"

    return False, f"In window ({gap} days)"

# ============================================================================
# PHASE 1: TEMPLATE RANDOMIZATION
# ============================================================================

def pick_random_template(agent: Dict[str, Any], context: str = "market_insight") -> tuple:
    """
    Pick a random template that has not been used recently for this agent.

    Returns:
        Tuple of (template_text, template_id)
    """
    templates = RESPONSE_TEMPLATES.get(context, RESPONSE_TEMPLATES["market_insight"])
    available = [t for t in templates if t not in agent.get("recent_templates", [])]

    if not available:
        available = templates
        agent["recent_templates"] = []

    picked = random.choice(available)
    template_id = f"{context}#{templates.index(picked) + 1}"

    agent["recent_templates"].append(picked)
    if len(agent["recent_templates"]) > 3:
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

    Brand rules (MANDATORY):
    - No em dashes (use periods or commas instead)
    - Short sentences, active voice, specific numbers only
    - Coach energy. No hype words.
    - Max 2 sentences, under 30 words total
    - Reference 1 specific detail from the post
    - Do NOT offer to help or pitch
    """
    if not CLAUDE_API_KEY:
        print(f"[Claude] API key not set. Using template fallback.")
        template, _ = pick_random_template({"recent_templates": []}, "market_insight")
        return template.format(detail=post_detail, market=market)

    prompt = f"""You are Scott Thompson, a mortgage strategist. Craft a short comment on this agent's social post.

Agent: {agent_name}
Agent specialty: {agent_specialty}
Post detail: "{post_detail}"

MANDATORY RULES:
1. Pull ONE specific detail from the post (number, location, or data point)
2. Add ONE forward-looking mortgage angle (rates, leverage, timing, qualification)
3. Max 2 sentences. Under 30 words total.
4. NO em dashes (use periods or commas instead)
5. NO hype words (no "great post", "crushing it", "game-changer")
6. Coach energy. Peer insight. Not a sales pitch.
7. Do NOT end with a question.

Good example: "Inventory down 12% plus Danville closing at that pace. You're reading the compression before it shows up in the data."
Bad example: "Great post Lauren! If you have clients looking to buy, I can help them get pre-approved today!"

Comment only, no quotes, no explanation:"""

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
                    "model": "claude-opus-4-8",
                    "max_tokens": 100,
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=10.0
            )

            if response.status_code == 200:
                data = response.json()
                comment = data["content"][0]["text"].strip()
                # Strip em dashes if Claude slips one in
                comment = comment.replace(" — ", ". ").replace("—", ".")
                print(f"[Claude] Comment drafted: {comment[:60]}...")
                return comment
            else:
                print(f"[Claude] API error {response.status_code}. Using template fallback.")
                template, _ = pick_random_template({"recent_templates": []}, "market_insight")
                return template.format(detail=post_detail, market=market)

    except Exception as e:
        print(f"[Claude] Error: {e}. Using template fallback.")
        template, _ = pick_random_template({"recent_templates": []}, "market_insight")
        return template.format(detail=post_detail, market=market)

# ============================================================================
# PHASE 1: FACEBOOK SCRAPING (Mock for Phase 1)
# ============================================================================

async def scrape_facebook_posts(agent: Dict[str, Any], hours: int = 48) -> List[FacebookPost]:
    """
    Scrape public posts from agent's Facebook profile.

    Phase 1: Mock implementation returns hardcoded test posts.
    Phase 2: Implement with Playwright/Apify scraping.
    """
    print(f"[Facebook] Scraping {agent['name']} (mock, Phase 1)...")

    mock_posts = {
        "Lauren Woolsey": [
            FacebookPost(
                url="https://facebook.com/lauren.woolsey/posts/20260615",
                text="Just closed another 5-bed home in Danville. Market's moving fast. Inventory down 12% from last month.",
                timestamp=datetime.now() - timedelta(hours=2),
                like_count=24,
                comment_count=5,
                extracted_detail="Inventory down 12%, Danville 5-bed close"
            )
        ],
        "Jordan Kim": [
            FacebookPost(
                url="https://facebook.com/jordan.kim.realtor/posts/20260615",
                text="Cap rate compression with 8% rental demand growth is the signal. Cash flow is tighter but appreciation is doing the work. That's the trade.",
                timestamp=datetime.now() - timedelta(hours=6),
                like_count=47,
                comment_count=6,
                extracted_detail="Cap rate compression with 8% rental demand growth"
            )
        ],
        "Marcus Rivera": [
            FacebookPost(
                url="https://facebook.com/marcus.rivera.realtor/posts/20260615",
                text="The $800K-$1.2M window is exactly where leverage shifted first. First-time buyers who waited are now the ones setting terms.",
                timestamp=datetime.now() - timedelta(hours=12),
                like_count=15,
                comment_count=3,
                extracted_detail="$800K-$1.2M leverage shift, first-time buyer opportunity"
            )
        ]
    }

    posts = mock_posts.get(agent["name"], [])
    print(f"[Facebook] Found {len(posts)} posts for {agent['name']}")
    await asyncio.sleep(random.uniform(1, 2))
    return posts

# ============================================================================
# PHASE 1: AIRTABLE WRITES
# ============================================================================

async def write_to_signals_queue(posts: List[QueuedPost]) -> bool:
    """
    Write queued posts to Airtable Signals Queue (tblkUMWXZKBUMBU7W).

    Phase 1: Requires AIRTABLE_API_KEY env var.
    MCP-native deployment: Cowork scheduled task writes directly via MCP tools.
    """
    if not AIRTABLE_API_KEY:
        print(f"[Airtable] No API key. Printing records that would be written:")
        for post in posts:
            print(f"  Agent: {post.agent_name} | Comment: {post.my_comment[:50]}...")
        return True

    print(f"[Airtable] Writing {len(posts)} records to Signals Queue...")

    records = []
    for post in posts:
        engagement = post.like_count + post.comment_count if hasattr(post, "like_count") else post.engagement_score
        records.append({
            "fields": {
                "fldNam3VnNPnMPIpk": post.agent_name,
                "fldp1RHVObXqLNQdR": post.timestamp_scraped.strftime("%Y-%m-%d"),
                "fldJP08eL64PJAL5m": "Facebook Post",
                "fldb7XYPdQMaXXqCf": engagement,
                "fldHGPJl17sMYzGgU": f"Tier {post.agent_tier}",
                "fld5hrSPKFPn6etQO": f"DRAFT COMMENT: {post.my_comment}",
                "fldnTpS8kfkzoxBHv": "Pending Review"
            }
        })

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_SIGNALS_QUEUE_TABLE}",
                headers={"Authorization": f"Bearer {AIRTABLE_API_KEY}", "Content-Type": "application/json"},
                json={"records": records},
                timeout=10.0
            )
            if response.status_code == 200:
                print(f"[Airtable] Signals Queue: {len(posts)} records written.")
                return True
            else:
                print(f"[Airtable] Error {response.status_code}: {response.text}")
                return False
    except Exception as e:
        print(f"[Airtable] Exception: {e}")
        return False


async def write_to_command_queue(posts: List[QueuedPost], gap_info: Dict[str, str]) -> bool:
    """
    Write queued posts to Airtable Daily Command Queue (tblEatDP2bx67PfS7).

    Phase 1: Requires AIRTABLE_API_KEY env var.
    MCP-native deployment: Cowork scheduled task writes directly via MCP tools.
    """
    if not AIRTABLE_API_KEY:
        print(f"[Airtable] No API key. Printing command queue records:")
        for post in posts:
            print(f"  Agent: {post.agent_name} | Copy: {post.my_comment[:50]}...")
        return True

    print(f"[Airtable] Writing {len(posts)} records to Daily Command Queue...")

    records = []
    for post in posts:
        gap_note = gap_info.get(post.agent_name, "8+ days overdue")
        priority = "High" if post.agent_tier == "A" else "Medium"
        records.append({
            "fields": {
                "fldfhTY9QxR2DwBDj": post.agent_name,
                "fldwAVmhBxBY3HBEV": "Comment",
                "fldYTjS7HmBX80xt9": post.my_comment,
                "fldS5JjjJ7oheHgEz": priority,
                "fldmGnekj8cPPAIE5": f"Tier {post.agent_tier}. {gap_note}.",
                "fldXs2HTVJ72sZkfO": "Pending Review"
            }
        })

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_COMMAND_QUEUE_TABLE}",
                headers={"Authorization": f"Bearer {AIRTABLE_API_KEY}", "Content-Type": "application/json"},
                json={"records": records},
                timeout=10.0
            )
            if response.status_code == 200:
                print(f"[Airtable] Command Queue: {len(posts)} records written.")
                return True
            else:
                print(f"[Airtable] Error {response.status_code}: {response.text}")
                return False
    except Exception as e:
        print(f"[Airtable] Exception: {e}")
        return False

# ============================================================================
# MAIN ORCHESTRATOR - PHASE 1
# ============================================================================

class SignalStrikeScraperPhase1:
    """Main orchestrator for Phase 1 (3 test agents, mock Facebook, Airtable writes)."""

    def __init__(self):
        self.agents = TEST_AGENTS.copy()
        self.queued_posts: List[QueuedPost] = []
        self.skipped_agents: List[Dict] = []
        self.gap_info: Dict[str, str] = {}
        self.start_time = datetime.now()

    async def run(self):
        """Main execution flow."""
        print("\n" + "="*80)
        print("SignalStrike Scraper - Phase 1")
        print("="*80)
        print(f"Start time: {self.start_time}")
        print(f"Test agents: {len(self.agents)}")
        print(f"Platform: Facebook (mock, Phase 1)")
        print("="*80 + "\n")

        for agent in self.agents:
            await self.process_agent(agent)
            await asyncio.sleep(random.uniform(2, 4))

        await self.finalize()

        print("\n" + "="*80)
        print("Phase 1 scraper complete")
        print(f"Signals queued: {len(self.queued_posts)}")
        print(f"Agents skipped: {len(self.skipped_agents)}")
        print("="*80 + "\n")

    async def process_agent(self, agent: Dict[str, Any]):
        """Process a single agent."""
        print(f"\n[Agent] Processing {agent['name']} (Tier {agent['tier']})...")

        skip, reason = should_skip_agent(agent)
        gap_days = days_since_last_touch(agent)

        print(f"  Gap: {gap_days} days | Decision: {'SKIP' if skip else 'PROCESS'} | {reason}")

        if skip:
            self.skipped_agents.append({"name": agent["name"], "reason": reason})
            return

        # Track gap info for command queue Why Now field
        if gap_days > 7:
            self.gap_info[agent["name"]] = f"No prior touch on record. {gap_days}+ days overdue"
        else:
            self.gap_info[agent["name"]] = f"{gap_days} days since last touch"

        posts = await scrape_facebook_posts(agent)
        if not posts:
            print(f"  No new posts found.")
            return

        # Process first post only (Phase 1: one comment per agent per night)
        await self.process_post(agent, posts[0], gap_days)

    async def process_post(self, agent: Dict[str, Any], post: FacebookPost, gap_days: int):
        """Process a single post and draft a comment."""
        print(f"\n  [Post] {post.text[:70]}...")

        comment = await draft_comment_with_claude(
            agent_name=agent["name"],
            post_detail=post.extracted_detail,
            agent_specialty=agent["specialty"]
        )

        if not comment or len(comment) < 10:
            print(f"  Comment too short. Skipping.")
            return

        queued = QueuedPost(
            agent_name=agent["name"],
            agent_tier=agent["tier"],
            post_excerpt=post.text[:100],
            my_comment=comment,
            post_url=post.url,
            platform="facebook",
            timestamp_scraped=datetime.now(),
            status="Pending Review",
            gap_days=gap_days,
            engagement_score=post.like_count + post.comment_count
        )

        self.queued_posts.append(queued)
        print(f"  Queued: {comment[:60]}...")

        await asyncio.sleep(random.uniform(0.5, 1.5))

    async def finalize(self):
        """Write results to Airtable and report."""
        if not self.queued_posts:
            print("\n[Finalize] No posts to write. All agents skipped or no posts found.")
            return

        print(f"\n[Finalize] Writing {len(self.queued_posts)} posts to Airtable...")
        await write_to_signals_queue(self.queued_posts)
        await write_to_command_queue(self.queued_posts, self.gap_info)

        print("\n" + "-"*80)
        print("EXECUTION SUMMARY")
        print("-"*80)
        for post in self.queued_posts:
            print(f"  {post.agent_name:18} | Tier {post.agent_tier} | {post.gap_days}d gap | {post.my_comment[:50]}...")
        if self.skipped_agents:
            print(f"\nSkipped ({len(self.skipped_agents)}):")
            for s in self.skipped_agents:
                print(f"  {s['name']}: {s['reason']}")
        print("-"*80)

    def get_status(self) -> Dict[str, Any]:
        """Return current run status."""
        return {
            "status": "complete",
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "agents_processed": len(self.agents),
            "posts_queued": len(self.queued_posts),
            "agents_skipped": len(self.skipped_agents),
            "queued_posts": [
                {
                    "agent": p.agent_name,
                    "tier": p.agent_tier,
                    "gap_days": p.gap_days,
                    "comment": p.my_comment,
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
    print("\n[Status]")
    print(json.dumps(scraper.get_status(), indent=2, default=str))
