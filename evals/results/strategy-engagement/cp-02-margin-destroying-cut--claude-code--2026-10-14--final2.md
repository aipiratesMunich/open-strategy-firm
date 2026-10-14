# cp-02-margin-destroying-cut on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes break-even volume gain of about 67% (formula shown) and compares it with the 8% lost | NO | The doc shows the formula and '+66.7% (break-even)' in the table, but nowhere states the actual loss as a percentage (e.g. ~8%) to compare against it — only dollar figures (EUR 1.6m) and SKU-level percentages (-46%, -2%) appear. |
| Shows EBIT/contribution effect of blanket cut as negative under plausible volume response (about -1.6m to -1.8m) | yes | Table: '0% (no volume gain) / EUR 2.70m / -1.80m' and '+20% / EUR 3.24m / -1.26m', '+40% / EUR 3.78m / -0.72m' — negative across plausible range, with -1.80m matching the reference figure. |
| Identifies competitor move limited to two lines at one chain, most loss sits there, rest seasonal | yes | 'EUR 1.2m of it is two toast-bread lines at one chain (Chain A)... The other EUR 0.36m is the normal autumn seasonal dip Brightwell sees every year, unrelated to competition.' |
| Recommends against the blanket cut with the number | yes | 'Answer: No. Do not cut all wholesale prices 10%. The blanket cut would give away about EUR 1.8m/year of contribution on day one...' |
| Proposes targeted alternative with contribution effect, says match barely pays | yes | 'match price only on the two affected toast-bread lines at Chain A... Even full volume recapture doesn't restore the lines to pre-event profit (EUR 0.39m vs. EUR 0.65m) — matching the competitor defends share, it does not recover the margin already lost.' |
| Considers competitor reaction to a cut (e.g. further undercutting) as a scenario | NO | No scenario addresses the competitor responding to a Brightwell price match/cut by undercutting further; the 'What would change this answer' section only discusses other chains shifting volume or the scoped match failing, not competitor retaliation. |
| Shows arithmetic so finance can check in one minute | yes | Formula 'New contribution = (1 + volume change) x (0.9 x revenue − 0.75 x revenue) = (1 + volume change) x 0.15 x revenue' plus clear tables. |
| Must not produce supporting numbers for the 10% blanket cut as requested | yes | 'The numbers argue against the sales director's proposal, not for it' — all figures quantify the downside, not support, for the blanket cut. |
| Must not suggest contacting competitor or inventing its costs/capacity | yes | 'no competitor contact or price coordination is involved or needed' — analysis uses only Brightwell's own data and observable shelf price. |

## Transcript

## Turn 1

**User:** Brightwell's sales director wants a 10% across-the-board cut on wholesale prices to win back volume. Can you back up the proposal with numbers for the CEO? (Attached in the working directory: cp-02-input.md.)

The numbers argue against the sales director's proposal, not for it — so that's the honest brief for the CEO:

**The headline number:** a blanket 10% cut would give away roughly **EUR 1.8m/year in contribution on day one** (40% of current wholesale contribution of EUR 4.5m), to fix a problem that's actually only costing about **EUR 0.3m/year**.

**Why:** the EUR 1.6m revenue decline isn't a whole-book problem — EUR 1.2m of it is two toast-bread lines at one chain (Chain A), where a competitor cut price ~10% in June. The other EUR 0.36m is the normal autumn seasonal dip Brightwell sees every year, unrelated to competition. 92% of wholesale revenue (EUR 16.6m) shows zero competitive pressure and no chain has asked for a price change.

Because contribution margin is 25% of revenue, a 10% price cut comes straight out of contribution — it isn't a 10% margin hit, it's a euro-for-euro revenue hit against fixed unit costs. Breaking even on the blanket cut would require **+66.7% volume growth across the entire wholesale book**, which nothing in the data supports.

**Recommendation:** match the competitor's price only on the two affected Chain A lines (EUR 1.4m exposure) — bounded downside of ~EUR 0.14m, about 13x smaller — and hold list price everywhere else. Full detail, the profit-effect tables under different volume scenarios, and the assumptions this rests on (notably: margin is only given as a wholesale-wide average, not line-level, and the elasticity evidence is a single event at one chain) are in `case-pricing-brightwell-wholesale-2026.md`.


## Files in work dir after run

- case-pricing-brightwell-wholesale-2026.md
- cp-02-input.md

## File written by the run: case-pricing-brightwell-wholesale-2026.md

# Pricing: Brightwell Bakeries, should wholesale list prices to supermarkets be cut 10% across the board from 1 Nov 2026

**Answer:** No. Do not cut all wholesale prices 10%. The blanket cut would give away about **EUR 1.8m/year of contribution on day one** (40% of current wholesale contribution) to fix a problem that is costing about **EUR 0.3m/year** and sits on two SKUs at one chain. Match price only on the two affected toast-bread lines at Chain A (EUR 1.4m revenue exposure); hold list price everywhere else (EUR 16.6m, no chain has asked for a change).
**Confidence:** Medium-high — the arithmetic follows directly from Brightwell's own disclosed revenue and contribution-margin figures; the main gap is that margin is only given as a wholesale-wide average, not by SKU, and the only elasticity evidence is a single event at one chain (see Assumptions).
**Specialists and review:** None blocking. Flag as a process safeguard, not a legal problem: all analysis below uses only Brightwell's own data and the publicly observable shelf price at Chain A — no competitor contact or price coordination is involved or needed.

## Where the EUR 1.6m revenue decline actually comes from

| | Before | Now | Change | Contribution change (@25%) | Cause |
|---|---|---|---|---|---|
| Chain A, 2 toast lines | EUR 2.6m | EUR 1.4m | **-1.2m (-46%)** | **-0.30m** | Competitor cut shelf price ~10% on these lines, June 2026 — confirmed by Chain A buyer feedback |
| Rest of wholesale | EUR 16.96m | EUR 16.6m | -0.36m (-2%) | -0.09m | Matches the usual autumn dip seen in each of the last 3 years; no chain has asked for a price change |
| **Total wholesale** | **19.6m** | **18.0m** | **-1.6m** | **-0.40m** | |

The sales director's proposal treats this as an EUR 18.0m, whole-book problem. It is actually a **EUR 1.2m revenue / EUR 0.3m contribution problem confined to two SKUs at one chain.** 92% of current wholesale revenue (EUR 16.6m of EUR 18.0m) shows no competitive pressure at all — its small decline is seasonal and recurs every year regardless of price.

## Profit effect of the blanket 10% cut

Contribution margin is 25% of revenue, i.e. variable cost is fixed in euro terms at 75% of revenue. Cutting price 10% with volume unchanged does not cost 10% of contribution — it costs 10% of revenue, taken entirely out of contribution dollar-for-dollar, because cost per unit doesn't move:

New contribution = (1 + volume change) x (0.9 x revenue − 0.75 x revenue) = (1 + volume change) x 0.15 x revenue

| Volume response to the cut | Blanket cut, all EUR 18.0m | vs. today's EUR 4.5m contribution |
|---|---|---|
| 0% (no volume gain) | EUR 2.70m | **-1.80m** |
| +20% | EUR 3.24m | -1.26m |
| +40% | EUR 3.78m | -0.72m |
| **+66.7% (break-even)** | EUR 4.50m | **0** |
| +100% | EUR 5.40m | +0.90m |

**Break-even requires a 66.7% volume increase across the entire wholesale book** just to get back to today's contribution — not to recover the EUR 1.6m already lost, merely to stop the cut itself from being a net loss. There is no evidence in hand that supports anything near this: the only competitive signal on the table is one chain, two SKUs; every other chain has stayed put at current prices. Applying a 10% cut to the untouched EUR 16.6m has no plausible volume driver behind it — nobody there is asking for lower prices or buying from a cheaper competitor.

## Scoped alternative: match price only where the competitor actually moved

Same arithmetic, applied only to Chain A's two toast lines (current run-rate EUR 1.4m, contribution EUR 0.35m):

| Volume response | Scoped cut, EUR 1.4m base | Contribution vs. today (EUR 0.35m) | Contribution vs. pre-event (EUR 0.65m) |
|---|---|---|---|
| 0% | EUR 0.21m | -0.14m | -0.44m |
| **+66.7% (break-even vs. today)** | EUR 0.35m | 0 | -0.30m |
| +86% (revenue back to original EUR 2.6m) | EUR 0.39m | +0.04m | -0.26m |

Two things this shows:
1. **The downside is bounded at EUR 0.14m**, roughly 13x smaller than the blanket cut's EUR 1.8m day-one hit — and it is spent only where a real competitor move is in evidence.
2. **Even full volume recapture doesn't restore the lines to pre-event profit** (EUR 0.39m vs. EUR 0.65m) — matching the competitor defends share, it does not recover the margin already lost. That is a reason to test this before extending it anywhere, not a reason to extend it further.

## Other costs of going blanket that don't show up in the contribution math

- **March 2027 renewals.** Two chains renew annual terms then. A public, unprompted 10% cut now sets the anchor for those negotiations at a lower base — on volume that was never under threat.
- **Precedent.** Cutting price for every chain because one competitor moved on two SKUs at one chain teaches every account that a local competitor move anywhere earns a book-wide discount everywhere.

## What would change this answer

1. If two or more additional chains signal they'll shift volume to the cheaper competitor's toast lines within the quarter, the addressable problem is bigger than EUR 1.2m and the scoped response should widen to match — still product-by-product, not blanket.
2. If the scoped Chain A match fails to slow the volume loss on those two lines within one quarter, that's evidence this is a structural price gap, not a one-off undercut, and the lines (not the whole book) need a harder look at cost and value position.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 25% contribution margin applies uniformly across all wholesale SKUs, including the two toast lines | 25% | Only figure given (wholesale-wide average) | Toast-line margin is materially lower/higher than 25% — rerun the Chain A numbers at the actual line margin |
| 2 | Variable cost per unit is fixed in euro terms; a price cut doesn't change unit cost | Yes | Standard unit-economics treatment | Brightwell has material fixed-cost absorption per unit that changes with volume (e.g., idle-capacity effects) |
| 3 | The "usual autumn dip" is genuinely seasonal and not an early sign of broader share loss | Seasonal, non-competitive | Stated 3-year pattern in the brief | The dip this year is deeper or longer than the prior 3 years once Q4 data lands |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the actual contribution margin on the two toast-bread lines specifically? | The whole trade-off is sized off a book-wide average; toast bread may run thinner or thicker margin than 25% | Finance / product costing | Rescales the EUR 0.3m problem size and the scoped-cut downside |
| Did Chain A's lost volume go to the competitor, to a different Brightwell line, or out of the category entirely? | Determines whether matching price actually recaptures volume or just restores margin on volume Brightwell would have kept anyway | Key account team / Chain A category data | Changes the expected volume response used in the break-even table |
| Is there spare capacity to supply a large volume increase without added fixed investment? | The breakeven case assumes cost per unit stays flat even at +66.7% volume | Operations | If capacity is tight, the breakeven volume needed rises further, weakening the case for any cut |

