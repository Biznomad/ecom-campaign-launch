# Email, SMS and app push

## Before building

- Check that automated flows are on: welcome, abandoned cart, abandoned checkout, browse, post-purchase. A billing hold can switch every flow off while the API still accepts "turn on" requests. Read the status back.
- Find old drafts for the same event with outdated offers or dates. Archive them so nobody sends the wrong one.
- Check old codes inside flow emails. Remove any that would stack with the new offer.

## Building

- Start from the last campaign's drafts if they fit. A campaign's email is usually a copy of a template: edit the copy attached to the campaign and read it back, not the master.
- Every email states the same offer, the end date and the terms. Subscription offers state first price, renewal price and interval.
- Audiences: most engaged first, wider later, widest on the last day.
- A resend goes to people who didn't open, set after the first send has gone out.

## Sending

Drafts only until the owner says to schedule. Then, for each message:

1. Save the send time.
2. Read the campaign back and confirm the time and audience.
3. Start the send job.

Never start a send job when step 1 failed.

## Push

One push a day at most, each with a deep link to the offer. Scheduling tools that run in a browser can log out; check the session before the launch day.

## Texts

Texts usually return the most per send and are the easiest to overuse. Open and "ends tonight" are the two that matter. Include the brand name and opt-out wording the provider requires.
