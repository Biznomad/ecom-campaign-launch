# ecom-campaign-launch

A Claude Code skill that plans, stages and launches an ecommerce promo campaign of 1 week, 2 weeks or a month across store discounts, paid ads, email, SMS, app push, organic social and the storefront theme.

Everything is built paused or as a draft. Nothing goes live until the store owner says "launch".

## Install

```
git clone https://github.com/Biznomad/ecom-campaign-launch ~/.claude/skills/ecom-campaign-launch
```

Or copy this folder to `~/.claude/skills/ecom-campaign-launch/`. Then ask Claude Code to "plan a 2-week campaign" or type `/ecom-campaign-launch`.

## Use

1. Copy `campaign.config.example.json` into your project as `campaign.config.json` and fill in your store, offer, dates, costs and channels.
2. Run `python3 scripts/plan.py campaign.config.json` to see what each order leaves you, the most you can pay for a new customer, and the day-by-day calendar.
3. Let Claude follow `SKILL.md` to audit, build, review and launch.

## What you need

Your own accounts and API access for the channels you turn on (store, ad accounts, email platform). The skill ships no credentials and no account IDs. Keep yours in environment variables, never in the config file.

## What's inside

- `SKILL.md`: the run, the safety rules and when to read each reference
- `scripts/plan.py`: unit economics and calendar, no network calls
- `references/`: cadence, creative, ads, messaging, diagnosing a drop, platform traps

## Black Friday version

[`bfcm-campaign-launch`](https://github.com/Biznomad/bfcm-campaign-launch) is the Black Friday / Cyber Monday fork of this skill. It starts the day you install it and plans every day through Cyber Monday.
