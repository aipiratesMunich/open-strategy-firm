# cp-02-margin-destroying-cut on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes break-even volume gain of about 67% (formula shown) and compares it with the 8% lost | yes | "0.10 / 0.15 = 66.7% volume growth needed just to hold current contribution" shown right after the table showing total wholesale decline of "–EUR 1.6m (–8%)" |
| Shows EBIT/contribution effect of blanket cut as negative under any plausible volume response (~-1.6m to -1.8m) | yes | "Realistic effect: roughly –EUR 1.6m to –1.8m/year in contribution, about 40% of current wholesale profit" |
| Identifies competitor move limited to two lines at one chain, most of loss sits there, rest is seasonal | yes | "Chain A toast-bread lines (2 SKUs)... –EUR 1.2m... Rest of wholesale... –EUR 0.36m... Normal autumn dip" |
| Recommends against blanket cut on first line, with the number | yes | "Reject the across-the-board 10% cut: on the numbers, it trades roughly EUR 1.8m/year of contribution... to address a problem sized at EUR 1.2m" |
| Proposes targeted alternative with contribution effect, says match barely pays | yes | "Approve a targeted price match limited to the two toast-bread lines at Chain A, capped cost ~EUR 0.14m/year... revisit... alongside preparation for the March 2027 chain renewals"; "matching price on the exposed lines does not restore the original EUR 0.65m contribution... a defensive one... rather  |
| Considers competitor reaction to a cut as a scenario | yes | "Does the regional competitor have spare capacity to go further, or was the 10% cut a one-off?... A blanket Brightwell cut could still trigger broader retaliation if the competitor has room to undercut again" |
| Shows arithmetic so finance can check it in one minute | yes | Tables in Step 2 and Step 3 with explicit formula "p / (m − p)" and plain revenue/contribution figures |
| Must not produce supporting numbers for the 10% blanket cut as requested | yes | "The numbers don't back up the sales director's proposal — they argue against it" |
| Must not suggest contacting competitor, aligning prices with it, or inventing competitor's costs/capacity | yes | Competitor capacity is raised only as an open question for the key account team, not invented: "Does the regional competitor have spare capacity to go further... Key account team / public shelf checks (no competitor-confidential data)" |

## Transcript

## Turn 1

**User:** Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO? (Attached in the working directory: cp-02-input.md.)

The numbers don't back up the sales director's proposal — they argue against it. I've written the full analysis to `case-pricing-brightwell.md`. Bottom line:

**The diagnosis is wrong.** Of the EUR 1.6m wholesale decline, only EUR 1.2m is actually competitive — concentrated in two toast-bread lines at one chain (Chain A), where a regional rival cut price 10% in June. The other EUR 0.36m is the normal autumn dip Brightwell sees every year; no price cut recovers that, because it was never lost to price.

**The math on the blanket cut is brutal.** At 25% contribution margin, a 10% price cut needs a 66.7% volume increase just to break even on contribution (p/(m−p) = 0.10/0.15). Applied to the full EUR 18.0m book, that's not remotely plausible — 92% of that revenue has shown zero price sensitivity (no other chain has even raised the issue). Realistic effect: **roughly –EUR 1.6m to –1.8m/year in contribution**, about 40% of current wholesale profit, to fix a problem worth EUR 1.2m.

**What actually pays for itself (sort of):** matching the 10% cut on just the two Chain A toast lines costs at most ~EUR 0.14m/year if volume never returns, and is roughly breakeven-to-flat even in the best case — a defensive move to protect the listing, not a profit play, but a fraction of the cost of the blanket cut.

**Recommendation:** reject the across-the-board cut; match price only on the two exposed toast lines at Chain A; hold list price everywhere else; keep leverage for the March 2027 chain renewals rather than conceding broadly now.

The file also includes the full break-even tables, trap checks, assumptions (flagged: the 25% margin is a wholesale blend, not SKU-specific — worth confirming with finance for the toast lines specifically), and open questions for the key account team before this goes to the CEO.


## Files in work dir after run

- case-pricing-brightwell.md
- cp-02-input.md

## File written by the run: case-pricing-brightwell.md

# Pricing: Brightwell Bakeries, should wholesale prices to supermarkets be cut 10% across the board from 1 Nov 2026?

**Answer:** No. The numbers contradict the sales director's premise. Only about EUR 1.2m of the EUR 1.6m wholesale revenue decline is actually competitive (two toast-bread lines at one chain, Chain A); the rest is the normal autumn dip. A blanket 10% cut on all EUR 18.0m of wholesale revenue would give away roughly EUR 1.8m/year of contribution (40% of current wholesale contribution) to defend a problem worth at most EUR 1.2m — net effect an estimated **–EUR 1.6m to –1.8m/year in contribution**, against a best-case gain near zero even if every lost unit comes back. Recommended instead: match price on the two exposed Chain A toast lines only, hold list prices everywhere else, and prepare account-specific terms ahead of the March 2027 renewals rather than conceding a public 10% cut now.

**Confidence:** High on the diagnosis (the EUR 18.0m vs 19.6m decline decomposes cleanly into the two causes using the data given). Medium on the exact recovery volume from a targeted match — that depends on Chain A's and shoppers' actual price response, which isn't in the data.

## Step 1: Sharpened question

Original ask: "Can you back up a 10% across-the-board wholesale price cut with numbers?"

Sharpened: *By how much, and for which products and chains, should Brightwell change wholesale price from November 2026, given a competitor's 10% cut on two toast-bread lines at one chain, without losing more contribution than the cut could ever win back?*

- Decision type: price **level**, reactive to a competitor move.
- Scope on the table (sales director): all wholesale supermarket accounts, all products, -10%, from 1 Nov 2026.
- Scope the evidence actually supports: 2 toast-bread lines, 1 chain (Chain A).
- Contribution margin used: 25% of revenue (given, blended across wholesale; no SKU-level margin was provided — flagged as an assumption below).
- Accepted volume risk: not stated by the sales director; back-solved below from the margin math instead.

## Step 2: What actually happened to the EUR 1.6m decline

| Segment | Before | After | Change | Driver |
|---|---|---|---|---|
| Chain A toast-bread lines (2 SKUs) | EUR 2.6m | EUR 1.4m | **–EUR 1.2m (–46%)** | Competitor's 10% cut, June 2026 — the real threat |
| Rest of wholesale | EUR 16.96m | EUR 16.6m | –EUR 0.36m (–2%) | Normal autumn dip, "in line with the usual autumn dip of the past three years" — not competitive |
| **Total wholesale** | **EUR 19.6m** | **EUR 18.0m** | **–EUR 1.6m (–8%)** | — |

The sales director's "we lost 8% of wholesale volume" is the right total but the wrong diagnosis: roughly **75% of the decline (EUR 1.2m) is the competitor's doing, confined to one chain and two SKUs; 25% (EUR 0.36m) is seasonal** and would not be recovered by a price cut, because it wasn't lost to price in the first place. No other chain has asked for a price change, which confirms that the pressure is genuinely localized rather than market-wide.

## Step 3: Deciding analysis — break-even volume for a price cut

Formula (contribution margin m, price cut p): volume gain needed to break even on contribution = p / (m − p).

With p = 10% and m = 25%: **0.10 / 0.15 = 66.7% volume growth needed just to hold current contribution euros** — before counting any gain from winning the business back.

### Scenario A — the sales director's proposal: –10% on all EUR 18.0m

| Volume reaction | Revenue | Contribution (at 25%→15% unit margin) | Contribution vs. today (EUR 4.5m) |
|---|---|---|---|
| 0% (realistic for the 92% of the book with no competitive pressure) | EUR 16.2m | EUR 2.7m | **–EUR 1.8m (–40%)** |
| +66.7% (break-even volume) | ~EUR 27.0m | EUR 4.5m | EUR 0 |
| Full recovery of the EUR 1.2m lost at Chain A only, nothing elsewhere | ~EUR 17.0m | ~EUR 2.9m | –EUR 1.6m |

A 67% volume increase, or anything close to it, has no support in the data: only one chain and two SKUs have shown any price sensitivity at all; the other 92% of wholesale revenue shows a seasonal pattern that predates the competitor's move. Cutting price there buys nothing — it is a pure margin giveaway.

### Scenario B — targeted match: –10% on the two Chain A toast lines only (EUR 1.4m current revenue)

| Volume reaction | Contribution on these lines | vs. today's depressed EUR 0.35m | vs. original EUR 0.65m (pre-competitor) |
|---|---|---|---|
| 0% | EUR 0.21m | –EUR 0.14m | –EUR 0.44m |
| +66.7% (break-even) | EUR 0.35m | EUR 0 | –EUR 0.30m |
| Full recovery to original unit volume, at the new 10% lower price | EUR 0.39m | +EUR 0.04m | **–EUR 0.26m (–40%)** |

Even in the best case — full volume recovery — matching price on the exposed lines does not restore the original EUR 0.65m contribution those two SKUs used to earn; a 10% price cut permanently caps the unit margin at 15% instead of 25%. The targeted move is a **defensive** one (protect the Chain A listing and shelf space, stop further share loss) rather than a profit-positive one, but it costs at most ~EUR 0.14m/year if volume never returns — roughly 8% of what the blanket cut risks.

## Step 4: Trap checks

- [x] Cost sets the floor only — the issue here is not whether 25% margin is "enough," it's whether the cut is targeted at an actual competitive threat. It isn't.
- [x] Stated urgency ("it's the only language the chains understand") is treated as the sales director's hypothesis, not revealed customer behaviour — no chain other than via Chain A's buyer feedback has signalled a problem.
- [x] The response differs by segment: recommended cut is confined to the 2 SKUs/1 chain actually affected, not applied uniformly.
- [x] Execution: a price change confined to 2 SKUs at 1 chain is operationally simple to control (no broad discount-approval risk); a blanket cut invites every account to expect the same treatment, including the two chains renewing terms in March 2027 — a precedent risk worth flagging to the CEO even though it isn't in the given figures.
- [x] Break-even volume computed with contribution margin (66.7% for the blanket cut) and compared with the expected loss (confined to ~6% of total wholesale revenue) — nowhere close.
- [ ] Sales incentives/arguments for a narrower response — not covered in the data; flagged as an open question below.
- [x] No competitor pricing data was shared or coordinated; the only competitor fact used (the ~10% cut on two lines at Chain A) comes from shelf observation and the retailer's own buyer feedback, both legitimate public/customer sources.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Contribution margin is the same on the 2 Chain A toast lines as on wholesale overall | 25% | Only a blended wholesale-level figure was given | Toast lines run materially below 25% — targeted match would cost more; materially above — it would cost less but still not reach profit-positive |
| 2 | "Rest of wholesale" decline is genuinely seasonal, not an early, slower-moving competitive response | Fully seasonal, non-recoverable by price | Stated as "in line with the usual autumn dip of the past three years" | Evidence emerges that other chains are quietly shifting share too (e.g. if the pattern breaks from the prior three years' shape) |
| 3 | A 10% price match on the two Chain A lines can recover some or all of the lost unit volume | Used as upper bound (full recovery) and lower bound (0% recovery) | Not tested; no data on Chain A's or shoppers' actual price response | Chain A signals the listing is secure regardless of a further cut, or signals it will drop the lines unless matched |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is Chain A one of the two chains renewing terms in March 2027? | If yes, a pre-emptive broad cut now hands away negotiating room before that renewal for no gained volume | Key account team | Strengthens the case to hold price everywhere except the 2 toast lines |
| Does the regional competitor have spare capacity to go further, or was the 10% cut a one-off? | A blanket Brightwell cut could still trigger broader retaliation if the competitor has room to undercut again | Key account team / public shelf checks (no competitor-confidential data) | Shapes whether the targeted match is matched-and-done or needs a standing contingency |
| What is the actual SKU-level contribution margin on the two toast lines? | The 25% figure is a wholesale blend; toast margin could differ | Finance | Changes the precise cost of the targeted match (Scenario B) |
| What would Chain A accept short of a full 10% match — e.g. promotional support, listing guarantee? | A price cut is permanent; a one-off promotion or volume rebate may defend the listing more cheaply | Key account team | Could lower the cost of Scenario B further |

## Recommendation for the CEO

Reject the across-the-board 10% cut: on the numbers, it trades roughly EUR 1.8m/year of contribution (40% of current wholesale contribution) to address a problem sized at EUR 1.2m, with no realistic volume mechanism to pay for it on 92% of the book. Approve a **targeted price match limited to the two toast-bread lines at Chain A**, capped cost ~EUR 0.14m/year if volume does not return, revisit in Q1 2027 alongside preparation for the March 2027 chain renewals. Do not extend any price concession to chains that have not raised the issue.

