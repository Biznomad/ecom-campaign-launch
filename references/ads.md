# Paid ads

## Before anything

- Read the account status. An unsettled balance refuses every write and silently stops delivery.
- Read spend and results for 7 and 30 days at the account level, not one campaign.
- Pause what is wasting money before adding anything: ads over the cost cap with enough spend to judge, campaigns for offers that have ended.

## Structure

- Two campaigns: new customers and retargeting. One broad ad set in each. Splitting a small budget across many ad sets keeps each from learning.
- New customers: broad, excluding buyers, site visitors and engagers.
- Retargeting: email list, past buyers, site visitors, cart and checkout, social engagers. Exclude buyers from the last 7 days.
- Budgets at ad-set level, with a start and an end time matching the campaign window.
- Judge new-customer ads against the cost cap from `plan.py`, not against retargeting returns. Retargeting always looks better.

## Keep social proof

Every time you rebuild an ad as a new post, its likes, comments and shares reset to zero.

1. Create the ad once from an image and copy. That makes one page post.
2. Read the creative's effective post ID.
3. Create every other ad for that creative from the post ID (`object_story_id`), in the other ad set and in later weeks.
4. Keep winners running on the same post. For a new offer line, prefer a new post only when the old copy would be false.
5. Add one or two existing posts that already have engagement, if their wording is still true.

## Build order

1. Campaigns and ad sets, paused.
2. Upload images, create ads paused, mount shared posts.
3. Tracking tags on every ad: source, medium, campaign, content, plus campaign, ad set and ad IDs.
4. Verify every ad reads paused, then send the owner the list.

## Search ads

- A short Search campaign on brand plus product terms, with the price and deadline in the ad text and sitelinks to each offer.
- Schedule a pause for the end time if the platform has no end date for the campaign type.
- Update ad text when the deadline moves.

## During the campaign

Check daily: total sales, total ad spend, new customers, cost per new customer. Move money toward ads under the cap. Don't edit a learning ad set more than you must; add new ads rather than editing live ones.
