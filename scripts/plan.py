#!/usr/bin/env python3
"""Print unit economics and a day-by-day calendar for a 1-week, 2-week or 1-month campaign.

usage: python3 plan.py campaign.config.json [--json]

Reads the config (see campaign.config.example.json). Makes no network calls and changes nothing.
"""
import datetime
import json
import sys

DAYS = {"1w": 7, "2w": 14, "1m": 30}


def margin(price, units, c):
    fees = price * c.get("payment_fee_pct", 2.9) / 100 + c.get("payment_fee_fixed", 0.30)
    return round(price - units * c["unit_cost"] - c["shipping_cost_per_order"] - fees, 2)


def economics(c):
    rows = []
    for o in c["offers"]:
        m = margin(o["price"], o["units"], c)
        rows.append({"offer": o["name"], "price": o["price"], "left_per_order": m,
                     "max_cost_per_new_customer": m,
                     "break_even_return": round(o["price"] / m, 2) if m > 0 else None})
    s = c.get("subscription")
    if s:
        first = margin(s["first_order_price"], s["units"], c)
        renew = margin(s["renewal_price"], s["units"], c)
        n = max(1, int(c.get("target_payback_orders", 2)))
        rows.append({"offer": "Subscription", "price": s["first_order_price"], "left_per_order": first,
                     "left_per_renewal": renew,
                     "max_cost_per_new_customer": round(first + renew * (n - 1), 2),
                     "break_even_return": None, "payback_orders": n})
    return rows


def calendar(c):
    n = DAYS[c["duration"]]
    start = datetime.date.fromisoformat(c["start"])
    ch = c["channels"]
    plan = []
    # Email days: 1w = open, mid, last day. 2w = open, day 4, day 8, day 11, last day. 1m = one or two a week plus open/close.
    email_days = {"1w": [0, 3, 6], "2w": [0, 3, 7, 10, 13], "1m": [0, 4, 9, 13, 18, 22, 27, 29]}[c["duration"]]
    refresh_days = {"1w": [], "2w": [7], "1m": [7, 14, 21]}[c["duration"]]
    review_days = {"1w": [2, 4], "2w": [2, 6, 9, 12], "1m": [2, 6, 13, 20, 27]}[c["duration"]]
    for i in range(n):
        d = start + datetime.timedelta(days=i)
        t = []
        if i == 0:
            t.append("Launch: flip ads, publish theme, confirm discounts are live in a real cart")
        if ch.get("email") and i in email_days:
            label = "opening" if i == 0 else ("last day" if i == n - 1 else "reminder / new angle")
            t.append("Email: " + label)
        if ch.get("sms") and i in (0, n - 1):
            t.append("Text: " + ("sale is open" if i == 0 else "ends tonight"))
        if ch.get("app_push") and (i in email_days or i == n - 1):
            t.append("App push")
        if ch.get("organic_social") and i % 2 == 0:
            t.append("Organic post (approved slots only)")
        if i in refresh_days and (ch.get("meta_ads") or ch.get("google_ads")):
            t.append("Creative refresh: add new concepts, pause ads over the cost cap")
        if i in review_days:
            t.append("Review: sales, ad spend, new customers, cost per new customer vs cap")
        if i == n - 1:
            t.append("Close at %s: discounts end, ads stop, theme restored, results report" % c.get("end_time_local", "23:59"))
        plan.append({"date": d.isoformat(), "day": d.strftime("%a"), "tasks": t})
    return plan


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 else 2)
    c = json.load(open(sys.argv[1]))
    if c.get("duration") not in DAYS:
        sys.exit("duration must be one of: 1w, 2w, 1m")
    for k in ("offers", "unit_cost", "shipping_cost_per_order", "start", "channels"):
        if k not in c:
            sys.exit("missing config key: " + k)
    eco, cal = economics(c), calendar(c)
    if "--json" in sys.argv:
        print(json.dumps({"economics": eco, "calendar": cal}, indent=1))
        return
    print("%s: %s (%s, %d days from %s)" % (c.get("brand", ""), c.get("campaign_name", ""), c["duration"], DAYS[c["duration"]], c["start"]))
    print("\nMoney left per order before ads")
    for r in eco:
        line = "  %-16s price $%.2f  left $%.2f  max cost per new customer $%.2f" % (r["offer"], r["price"], r["left_per_order"], r["max_cost_per_new_customer"])
        if r.get("break_even_return"):
            line += "  break-even return %.2fx" % r["break_even_return"]
        if r.get("payback_orders"):
            line += "  (pays back by order %d; each renewal leaves $%.2f)" % (r["payback_orders"], r["left_per_renewal"])
        print(line)
    budget = c.get("ad_budget_per_day")
    if budget:
        print("\nAd budget $%s a day, $%s for the campaign" % (budget, budget * DAYS[c["duration"]]))
    print("\nCalendar")
    for d in cal:
        if d["tasks"]:
            print("  %s %s" % (d["day"], d["date"]))
            for t in d["tasks"]:
                print("     - " + t)


if __name__ == "__main__":
    main()
