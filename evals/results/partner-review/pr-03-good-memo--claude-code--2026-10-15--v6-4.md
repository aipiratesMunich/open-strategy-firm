# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (7/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | yes | "Verdict:** Release with fixes" |
| No Blocker findings | yes | All findings table entries are severity 'Major' or 'Minor'; no 'Blocker' appears |
| Every Major states a concrete consequence for the decision, and no finding misstates a figure | yes | e.g. Finding 3: "The board treats EUR 2.4m ... as consistent with the pilot's success test, when the two currently describe incompatible growth rates"; figures (32%, 1.2m, 2.5–3.3m, 38→60 orders, 3.10/order) are used consistently with the memo's own numbers confirmed in the 'Numbers that do not tie' |
| Names what is good and must survive | yes | Section "What is good and must survive" lists 7 bullet points, e.g. "Explicit, falsifiable kill criteria are given for both funded initiatives — this is the clearest strength in the memo and should not be diluted" |
| Must not demand a named framework, more length, or more slides | yes | Fixes are specific content additions ("Add a discounted payback or NPV", "Add one line pricing the cost of revisiting the target") with no request for a named framework or generic length/slide increase |
| Must not flag the stated uncertainty or explicit assumptions as weaknesses | yes | "The memo is honest about its own evidence gap on the second decision ('we know their margins, not their revenue') rather than hiding it — fix it by adding the missing symmetric cost (finding 4), don't remove the disclosure." |
| Must not claim numbers do not tie | yes | "## Numbers that do not tie\nNone found. Checked and confirmed: 2.9+2.4=5.3; 5.3/62=8.5%; ... cumulative net contribution (0.16, 0.48, 0.93, 1.44) does cross EUR 1.2m during year 4 as claimed." |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027," gate 3

**Verdict:** Release with fixes
**In one line:** The recommendation and arithmetic hold up, but two assumptions behind the money (the catering margin and the delivery growth rate) aren't yet consistent with the rest of the memo, and the second board decision (target vs. floor) is argued one-sided.

**Question the draft must answer:** Which two moves should the board fund for 2027, and should the board revisit the 2031 revenue target or the 14% margin floor? (given)
**Answer the draft gives:** Fund a EUR 1.2m catering central kitchen and a EUR 0.3m delivery pilot; don't fund suburban stores or franchising; revisit the 2031 target, not the floor.
**Match:** Yes — both decisions are answered directly, with owners, amounts and dates.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Skeptical CFO | "Why catering" | The 32% contribution margin comes from the 2025 catering P&L, which reflects in-store production, not the new central kitchen's cost structure (which adds kitchen-to-office distribution and may have different labor/scale economics). | The board approves EUR 1.2m on a "pays back in year 4" claim that assumes a margin the new operating model hasn't actually produced yet. | State whether 32% already reflects the central-kitchen model; if not, rebuild the payback on the kitchen's own expected unit economics. |
| 2 | Major | Skeptical CFO | "Why catering" | EUR 1.2m is a real capital commitment (build-out plus four hires), evaluated only with an undiscounted single-case payback — no NPV/IRR, no result at the low end of the stated EUR 2.5–3.3m range. | The board can't tell whether the investment still clears a hurdle rate, or what happens if catering lands at EUR 2.5m instead of 2.9m. | Add a discounted payback or NPV, and show the result at the low end of the range, not only the base case. |
| 3 | Major | Logician | "Why a delivery pilot" | The pilot's own scale-up bar (38 → 60 orders/day, i.e. +58%, within the pilot window) implies a growth rate several times higher than the "12% annual order growth" used to produce the EUR 2.4m base case that the pilot bar is meant to validate. | The board treats EUR 2.4m — which feeds directly into the EUR 12.7m gap used to justify revisiting the revenue target — as consistent with the pilot's success test, when the two currently describe incompatible growth rates for the same thing. | Reconcile: either explain why the pilot targets a one-off step-change the 12%/year steady-state model doesn't need to assume, or rebuild the EUR 2.4m estimate on the growth rate the pilot is actually designed to prove. |
| 4 | Major | Logician | "What it adds up to" | The case for revisiting the target instead of the floor quantifies only the cost of lowering the floor (known margin hit); it never names the cost of lowering the target (credibility, any investor or strategic commitments tied to EUR 80m). | The board adopts "revisit the target" as the safer option without ever seeing what that option costs. | Add one line pricing the cost of revisiting the target, so both sides of the board's second decision are argued with the same rigor. |
| 5 | Major | Premortem | Recommendation (whole memo) | No mention of whether the Head of Operations and Head of Digital — each already running existing operations — have the bandwidth to deliver a new central kitchen (incl. hiring four staff) and a digital pilot on a 5–6 month runway, or who owns the handoff from store-level order-taking to the new central kitchen. | The board approves two initiatives assuming execution capacity that has never been checked. | Add a line on resourcing/sponsorship for each initiative, or name a program lead distinct from the functional head. |
| 6 | Major | Premortem | "Why a delivery pilot" | The entire delivery case rests on EUR 3.10 contribution per order "after platform fees" — platform/aggregator fee increases are a known industry risk and aren't tested. | If platform economics worsen, EUR 2.4m and the EUR 12.7m gap calculation built on it both move, with no warning in the memo. | Add platform-fee risk to the delivery kill criteria or note the contribution figure's sensitivity to fee changes. |
| 7 | Minor | Outsider | "What would change our view" | "Framework agreements" appears as the catering kill criterion but is never introduced or defined earlier in the memo. | — | Define the term where catering economics are first discussed, or replace with plain language ("signed recurring-order contracts"). |
| 8 | Minor | Evidence Auditor | "What it adds up to" | The 3% price increase is sized at ~EUR 1.1m, not the ~EUR 1.86m a naive 3% × EUR 62m would give; no elasticity or base assumption is shown. Does not change the "closes less than a quarter of the gap" conclusion. | — | State the base and elasticity assumption behind EUR 1.1m. |
| 9 | Minor | Evidence Auditor | "Why catering" | The 12 office-manager interviews appear to be drawn from current customers; no detail on selection, or whether non-customers/lapsed customers were included. | — | Add one line on how the 12 were selected. |

## Numbers that do not tie
None found. Checked and confirmed: 2.9+2.4=5.3; 5.3/62=8.5%; 62+5.3=67.3, 80−67.3=12.7; 1.1+0.9=2.0, 2.0/12.7≈16%<25%; the catering payback line (1.6×32%−0.35=0.16; 2.1×32%−0.35=0.32; 2.5×32%−0.35=0.45; 2.7×32%−0.35=0.51) is arithmetically correct, and cumulative net contribution (0.16, 0.48, 0.93, 1.44) does cross EUR 1.2m during year 4 as claimed.

## Missing outside view
- **Catering 2.5–3.3m by 2031:** no comparable bakery/catering operator's growth-from-standing-start cited to sanity-check the range; the triangulation is entirely internal (sales data, interviews, top-down sizing).
- **Delivery 12% base-case growth:** the two-chain benchmark (10–14%) is a genuine outside view, but see finding 3 — it isn't reconciled with the pilot's own 60-orders-per-day bar, so right now it's an outside view attached to a number the memo's own test contradicts.
- **3% price increase, EUR 1.1m:** no external data on bakery price elasticity against discount competitors.

## Premortem
1. **External:** Delivery platform fees rise or aggregator terms worsen, eroding the EUR 3.10/order contribution the entire delivery case is built on. (Not addressed — finding 6.)
2. **External:** Office attendance trend reverses, or a competitor enters local catering at a lower price, slowing growth that to date has required "no sales effort." (Partially addressed via the 40%-framework-agreement kill criterion, but no competitive-response scenario.)
3. **Internal:** The Head of Operations and Head of Digital are each asked to deliver a new initiative on top of existing responsibilities within 5–6 months, with no named program capacity and no owner for the seam between store-level catering fulfillment today and the new central kitchen. (Not addressed — finding 5.)

## What is good and must survive
- The recommendation is specific on all four dimensions: who, what, how much, by when — for both initiatives.
- Catering is triangulated three ways (revealed sales data, bottom-up, top-down), not resting on the interviews alone.
- The memo pre-empts the obvious objection that catering growth is just COVID catch-up, using the Q2-over-Q2 data point after attendance settled.
- Suburban stores and franchising are ruled out with a specific, quantified reason (margin floor breach), not hand-waved.
- Explicit, falsifiable kill criteria are given for both funded initiatives — this is the clearest strength in the memo and should not be diluted in any rewrite.
- The memo is honest about its own evidence gap on the second decision ("we know their margins, not their revenue") rather than hiding it — fix it by adding the missing symmetric cost (finding 4), don't remove the disclosure.
- The gap arithmetic (EUR 12.7m) and the test of price/hours levers against it all tie correctly.

This can go to the CEO; flag findings 3 and 4 for the team to patch before the board meeting itself, since they bear directly on the memo's second ask.


## Files in work dir after run

- pr-03-input.md
