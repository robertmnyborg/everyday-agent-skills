---
name: social-research
description: Search and read Reddit and Twitter/X through OpenCLI using the user's logged-in Chrome, read-only. Use when the user asks what people say on Reddit or X about a product, operator, community, competitor, or topic; wants Reddit threads that AI search engines might cite; or wants raw customer or practitioner quotes for research. Not for posting, replying, liking, or anything on LinkedIn.
---

# Social research (Reddit + X, read-only)

`opencli` reuses the Chrome session where the user is logged in to Reddit and X.
The `opencli-readonly-guard` hook (in this repo's `hooks/`) blocks every verb outside the list below.
A blocked call is the answer. Do not route around it with `opencli browser`,
Chrome MCP clicks, or other tools.

## Commands

Reddit:
- `opencli reddit search "<query>" [--subreddit X] [--sort relevance|new|top|comments] [--time all|year|month|week] [--limit 15]`
- `opencli reddit read <post-id> [--sort best] [--limit 25] [--depth 2]`: post plus comment tree
- `opencli reddit subreddit <name> [--sort hot|top|new] [--time ...] [--limit 15]`
- `opencli reddit user-posts|user-comments <username> [--limit 15]`

X:
- `opencli twitter search "<query>" [--filter top|live] [--from user] [--limit 15] [--top-by-engagement N]`
- `opencli twitter thread <tweet-id>` / `opencli twitter article <tweet-id>`
- `opencli twitter tweets <username> [--limit 20]` / `opencli twitter profile <username>`

Health check: `opencli doctor`. If more than one Chrome profile is connected, pass
`--profile <alias>` (see `opencli profile list`).

## Procedure

1. Run `opencli doctor` once per session before the first query.
2. Run 2 to 4 query phrasings, because Reddit and X search match on exact words.
3. Open the top threads with `read` or `thread`, because snippets drop the comments that carry the opinion.
4. Quote verbatim with the permalink, author, and date for every claim.
5. Report the counts behind any theme, such as "7 of 23 threads".

## Rules
- If you use [analyst-rigor-skills](https://github.com/robertmnyborg/analyst-rigor-skills): customer or market claims built from these threads go through `trustworthy-insights`, and persona or job claims go through `job-card`.
- Keep request volume modest (tens of queries, not thousands). Scraping volume can get the account flagged.
- Never run a write. If the user wants to post, they run `! opencli ...` himself.
