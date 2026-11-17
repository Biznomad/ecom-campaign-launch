---
name: ecom-campaign-launch
description: Use when planning, staging or launching an ecommerce promo campaign of 1 week, 2 weeks or a month (weekly deal, product launch, seasonal or Black Friday sale) across store discounts, Meta and Google ads, email/SMS, app push, organic social and the storefront theme, or when asked to "run this week's campaign", "launch the sale", "audit the campaign" or "fire on all channels".
---

# Ecommerce Campaign Launch

One owner decision (offer + dates) becomes a staged, verified campaign on every channel. **Everything is built paused, draft or on a preview theme. The owner's word "launch" flips it.**

## 1. Lock the brief (ask only what's missing)

Copy `campaign.config.example.json` to the project as `campaign.config.json` and fill it. Required: store, offer, start, end, duration (`1w`, `2w` or `1m`), unit cost, shipping cost per order, daily ad budget, channels in use.

Then run `python3 scripts/plan.py campaign.config.json`. It prints money left per order, the most you can pay for a new customer, the break-even return on ad spend, and the day-by-day calendar for the chosen duration. Show that to the owner before building anything.

## 2. Rules that hold on every run

- **Writes:** confirm the account, store and theme before the first change. Stage on an unpublished theme; never write to the live theme. Back up each file before changing it and log every change with a timestamp.
- **Sends:** emails, texts and pushes stay drafts until the owner says to schedule them. Set the send time and read it back before starting the send job; a send job with no saved time sends now.
- **Spend:** ads are created paused. Read the account's billing status and today's spend before any status flip. Never raise a budget without the owner's number.
- **Credentials** stay in the environment they live in. Never print them, never copy them between clients.
- **Claims:** only the exact offer, prices and terms in the brief. No health claims, no invented reviews, no exact dates baked into images (dates go in the copy).
- **Report what happened.** A step that failed or was skipped is stated as such.

## 3. The run

1. **Audit first.** For each channel, read what is live, what is scheduled and what conflicts with the new offer (old codes that stack, an earlier promo still running, an unpaid bill pausing sends or ads). Fix blockers before building.
2. **Discounts.** Automatic discounts for the exact products and window, tested in a real cart. Check whether they apply to subscriptions and whether other codes can stack on them.
3. **Creative.** One sample for owner approval, then the set. Read `references/creative.md` for concept diversity and image checks.
4. **Paid ads.** Read `references/ads.md`. One prospecting ad set and one retargeting ad set; one post per creative reused in both.
5. **Email, SMS, push.** Read `references/messaging.md` for the cadence per duration.
6. **Organic social.** Queue as drafts behind an owner approval page; publish only approved slots.
7. **Storefront.** Hero, product page and cart on a preview theme. Walk it on a phone: tap every option, read the cart, clear the cart.
8. **Review page.** One page with every asset, copy, link, ID and the launch checklist. Send it and wait.
9. **Launch** on the owner's word: flip ads, publish the theme, schedule sends and posts. Verify each one took effect.
10. **Close.** At the end time, confirm discounts ended, ads stopped and the theme is back. Then report results against the caps from step 1.

## 4. Look up the rest

- Day-by-day calendar and what changes between 1 week, 2 weeks and a month → `references/cadence.md`
- Diagnosing a drop in add-to-cart or sales before spending more → `references/diagnose.md`
- Platform traps that cost a retry (discount, ads, email and theme APIs) → `references/traps.md`
