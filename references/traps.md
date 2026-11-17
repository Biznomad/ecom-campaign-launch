# Platform traps

Each of these cost a retry in real runs. APIs change; check current docs when a call fails.

## Shopify

- Automatic discounts: use a fixed amount off each item for "deal price" offers. Check `appliesOnSubscription` and what the discount combines with.
- Automatic discounts can't be limited to a customer group. For early access, announce to a group first rather than gating.
- A store has a theme limit. `themeDuplicate` can return nothing when the limit is hit; delete an unused theme with the owner's OK first.
- Preview a theme with a cookie jar and `?preview_theme_id=`; the first request can return the live theme. Confirm the theme ID on the page.
- Bundle variants often carry no unit cost. Take cost from the single unit.
- Subscription plans may be owned by the subscription app and not editable through the store API.
- Don't rely on theme scripts for quantity or price; test what actually lands in the cart.
- Time zones: use the right UTC offset for the date (daylight saving changes it).

## Meta

- Account status must be active before writes. After a payment, read the status again before retrying.
- Writes are rate limited. After a burst, wait a minute or more and retry; make build scripts resumable with a state file.
- Opt out of automatic creative enhancements field by field if you need the image and text unchanged.
- Engagement counts on a page post need the page's token, not the ad account's.
- Some old posts (dynamic creative) can't be mounted in a new ad. Skip them.

## Google Ads

- Some campaign types have no end date. Schedule a pause.
- Text limits are strict: headlines 30 characters, descriptions 90, promotion targets short.
- Shopping needs an approved merchant account; without it, run Search only.

## Email platform

- API versions differ in what they can read. If a campaign returns "not found", try the version it was created with.
- A status change can return success and do nothing under a billing hold. Always read back.
- Back off and retry on rate limits.

## General

- Scheduled one-shot jobs (publish a theme, pause a campaign) need a guard: check the current state matches what you expect, and support a dry run.
- Keep a rollback for every publish: the previous theme ID, the previous budget, the previous status.
- Long shell one-liners with quotes break. Write a script file and run it.
