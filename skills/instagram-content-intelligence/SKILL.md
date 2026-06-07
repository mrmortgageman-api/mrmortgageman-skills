---
name: instagram-content-intelligence
description: Scrapes and analyzes Instagram content across MrMortgageMan's channel and up to 5 competitor loan officer channels using Apify. Scores every post using a weighted engagement formula, identifies top-performing content patterns, and generates ready-to-post video scripts in Scott's brand voice.
---

# Instagram Content Intelligence

Scrapes 6 Instagram channels, scores every post, surfaces patterns, generates ready-to-post scripts in MrMortgageMan brand voice.

## Channels

| Lane | Handle | Role |
|------|--------|------|
| Your Channel | @mr_mortgageman | Primary |
| Competitor 1 | @theshawnkaplan | Benchmark |
| Competitor 2 | @thinkbeforeyoubuyhomes | Benchmark |
| Competitor 3 | @scottpeckloanofficer | Benchmark |
| Competitor 4 | @themortgagenerdbyjustin | Benchmark |
| Competitor 5 | @neelhome | Benchmark |

## Engagement Scoring Formula

```
Score = (Views x 0.5) + (Saves x 0.3) + (Comments x 0.2)
```

## Execution Steps

1. Run `instagram_scraper.py` from mini-PC
2. Load `instagram_data.json`
3. Score and rank all posts
4. Extract hook patterns, content structure, topic categories, format performance
5. Gap analysis vs competitors
6. Generate 3 ready-to-post scripts in MrMortgageMan voice
7. Build HTML dashboard

## Script Format

```
SCRIPT [#]
Topic:
Pattern Used:
Inspired By:
Estimated Length:

HOOK (0-3 sec):
BODY (3-45 sec):
CTA (last 5 sec):
Caption:
```

## Brand Voice

Coach energy. Direct. Zero hype. Sentences under 20 words. No em dashes.
Sign-off: "Mortgage Made Simple, Scott"
