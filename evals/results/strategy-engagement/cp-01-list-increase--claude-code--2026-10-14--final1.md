# cp-01-list-increase on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the price waterfall first and states list increase only reaches pocket price if discounts don't widen, naming uncapped 22% small-direct-account discount as the leak | yes | Waterfall table shows pocket price 81→85.2 'assuming discounts and rebates stay the same percentage of list price'; Execution risk table flags small direct accounts '22% (already the highest in the range)... Any sales rep, no cap... High – nothing stops a rep from quietly raising the discount to off |
| Break-even volume loss ~11% computed with contribution margin, formula/arithmetic shown | yes | 'Break-even volume loss for a 5% increase at a 40% contribution margin: 1 − m/(m+p) = 1 − 0.40/0.45 = 11.1%' |
| Uses 2023 change (-2% for +3%) as revealed behaviour and compares expected loss (~3-4%) with break-even | yes | 'a 3% list increase in January 2023 was followed by a 2% volume fall... scaled to 5%, about 3% expected volume loss... 3% expected loss sits far inside the 11.1% break-even threshold' |
| EBIT effect as a range across volume reactions, with arithmetic shown | yes | Table gives +EUR1.20m (0% loss), +EUR0.88m (-3%), EUR0 (-11.1%), -EUR0.42m (-15%), with 'Arithmetic: new contribution = (1 − L) × [24.0m × 1.05 − 24.0m × 0.60]...' shown |
| Differentiates by segment (OEM January renewal, distributor 60-day notice, discount cap/approval for small direct accounts) | yes | Timing table: OEM 'January 2027 renewal cycle', Distributors 'Must go out by 31 December 2026... Conflict: this is before the board decides', Small direct accounts 'the discount cap must land on or before the same date' |
| Anchors recommendation on customer value and like-for-like competitor gap, not cost | yes | '7–9% below both main competitors... The gap is not covering a service shortfall' (on-time delivery 96% vs 90%); decision text leads with price-level gap, not cost/margin |
| Names competitor reaction as a scenario (follow/hold/undercut) and what would trigger a different answer | yes | 'hold, follow, or use spare capacity to undercut... A "follow" scenario strengthens the case; an "undercut" scenario in OEM (55% of volume) would need the stress case' |
| Answer line states decision type (price level plus execution), amount, segments, date, EBIT range | yes | 'Yes, go ahead on price *level* — but 1 March is not achievable for distributors (30% of volume)... small direct accounts (15% of volume) unless discount approval is capped... Net effect... roughly +EUR 0.8m to +1.2m a year' |
| Names source of 2023 market comparison (industry association data) and treats 2023 as one data point, states dependency | yes | 'market volume from the industry association's member-reported shipment statistics'; 'rests on a single historical episode (2023)'; 'even a downside revision is unlikely to approach the 11.1% break-even' |
| Must not compute break-even with gross margin or without showing formula | yes | Used 40% contribution margin explicitly with formula '1 − 0.40/0.45', not gross margin |
| Must not suggest sharing price intentions with competitors or using competitor contract data | yes | 'no competitor contact at any point'; 'Competitive intelligence from public price lists and win/loss data only — no competitor contact' |

## Transcript

## Turn 1

**User:** Work the Ravensworth pricing case from the data pack. Quick case, I need the answer page for the January board. (Attached in the working directory: cp-01-input.md.)

I've worked the case and saved the answer page to `case-pricing-ravensworth.md`.

**Bottom line:** Go ahead on the price level — but not as cleanly as framed. Two catches the data pack sets up:

1. **Timing conflict:** a 1 March 2027 effective date needs distributor notice by 31 December 2026 (60-day clause) — *before* the January board even meets. Either the board pre-clears sign-off before year-end, or distributors start a few weeks later than OEM/small accounts.
2. **Execution leak:** small direct accounts (15% of volume) have no discount cap and already run the widest discount (22%) — any rep can quietly offset the increase unless a cap goes in at the same time.

The math itself is comfortable: break-even volume loss is 11.1%, expected loss (scaled from the one historical price move you have, 2023) is ~3%, giving an EBIT gain of roughly **+EUR 0.8m–1.2m/year** — but that only lands if the two issues above are fixed alongside the list change.

Full assumptions, open questions, and the arithmetic finance can check in a minute are all in the file.


## Files in work dir after run

- case-pricing-ravensworth.md
- cp-01-input.md

## File written by the run: case-pricing-ravensworth.md

# Pricing: Ravensworth Industrial Seals, can list prices on the standard seal range rise 5% from 1 March 2027?

**Answer:** Yes, go ahead on price *level* — but 1 March is not achievable for distributors (30% of volume) given the 60-day notice clause, and the increase will leak away on small direct accounts (15% of volume) unless discount approval is capped at the same time. Net effect if executed properly: roughly **+EUR 0.8m to +1.2m a year in contribution/EBIT** (+8% to +13% on today's EUR 9.6m), well inside an 11.1% break-even volume-loss threshold.

**Confidence:** Medium — the price-benchmark and break-even math are solid, but the volume-loss estimate rests on a single historical episode (2023) and there is no competitor-reaction or customer-value evidence. Would drop to low if actual volume loss after launch runs above ~8%, or if a competitor undercuts in the OEM segment.

**Specialists and review:** Legal/competition counsel to confirm the distributor notice mechanics and that a public price-list change carries no price-signalling risk (no competitor contact at any point). Sales operations to fix the small-direct-account discount process before go-live.

## Price position

| Offer | Our list price | Competitors | Gap | Gap explained? |
|---|---|---|---|---|
| 40 comparable part numbers (same material, size, pressure rating), Sept 2026 | Index 100 | Index 108–110 | 7–9% below both main competitors | No — lead times comparable, and Ravensworth's on-time delivery is *better* (96% vs. customers' stated 90% average, 2025 audits). The gap is not covering a service shortfall. |

→ **Hypothesis "list prices sit below comparable competitors without a spec or service reason" — confirmed.** A 5% increase would still leave Ravensworth roughly 2–4% below the current competitor band (before any competitor move of their own — see Open questions).

No customer value-to-alternative (willingness-to-pay) data exists yet; the case rests on the price benchmark and on revealed past behaviour (below), not on stated value. That is a gap worth closing in a fuller review, not a reason to hold the increase given the size of the break-even cushion.

## Price waterfall (standard range, average per EUR 100 of list price, 2025)

| Step | Today | At +5% list | % of list today |
|---|---|---|---|
| List price | 100 | 105 | 100% |
| On-invoice discount | -12 | -12.6 | 12% |
| Invoice price | 88 | 92.4 | 88% |
| Annual volume rebates | -4 | -4.2 | 4% |
| Free freight | -3 | -3 | 3% |
| **Pocket price** | **81** | **85.2** | **81%** |

Pocket price rises from 81 to 85.2, i.e. **+5.2%**, assuming discounts and rebates stay the same percentage of list (they are quoted that way in the data) and free freight stays a fixed per-shipment cost rather than a percentage (an assumption — see Assumptions; the difference is under 0.2 points of list price either way, immaterial to the decision).

## Execution risk by segment

| Segment | Share of volume | On-invoice discount | Who approves | Leakage risk for this increase |
|---|---|---|---|---|
| OEM key accounts | 55% | 8% | Key account director | Low — controlled approval, and contracts renew in January 2027: the increase can be written straight into the renewal terms. |
| Distributors | 30% | 12% | Sales director | Low on execution (controlled approval); **high on timing** — see Timing below. |
| Small direct accounts | 15% | 22% (already the highest in the range) | **Any sales rep, no cap** | High — nothing stops a rep from quietly raising the discount to offset the list increase. This segment already carries the widest discount; it is the one most likely to swallow the 5% unless the approval rule changes now. |

→ **Trap check — "list price only":** fixing the level without fixing execution would let roughly 15% of volume absorb the increase through discounting. Recommend a discount cap (or sales-director sign-off above a threshold, e.g. above today's 22% average) for small direct accounts effective the same date as the list change.

## Volume reaction and break-even

- Break-even volume loss for a 5% increase at a 40% contribution margin: **1 − m/(m+p) = 1 − 0.40/0.45 = 11.1%**. Variable cost per unit is held fixed in euro terms (not re-based to 40% of the new price) — this is the correct, conservative way to run the formula.
- Revealed evidence: a 3% list increase in January 2023 was followed by a 2% volume fall over the next 12 months, against flat market volume (Ravensworth sales data; market volume from the industry association's member-reported shipment statistics). Read naively, that is roughly 0.67 points of volume loss per point of price — scaled to 5%, about **3% expected volume loss**.
- 3% expected loss sits far inside the 11.1% break-even threshold — a comfortable cushion even allowing for the weak evidence behind the 3% estimate (one episode, self-reported market data, no check for other causes — see Open questions).

→ **Hypothesis "expected volume loss stays well below break-even" — confirmed**, with the evidence graded weak-to-medium.

## Profit effect

Base: 2025 pocket revenue EUR 24.0m; contribution margin 40% (EUR 9.6m); variable cost held fixed in euro terms.

| Volume reaction | Pocket revenue | Contribution (≈ EBIT effect of this move) | EBIT effect vs. today |
|---|---|---|---|
| 0% (full pass-through) | EUR 25.20m | EUR 10.80m | **+EUR 1.20m** |
| -3% (scaled from the 2023 episode) | EUR 24.44m | EUR 10.48m | **+EUR 0.88m** |
| -11.1% (break-even) | EUR 22.40m | EUR 9.60m | EUR 0 |
| -15% (stress: competitor undercut + small-account leakage combined) | EUR 21.42m | EUR 9.18m | **-EUR 0.42m** |

Arithmetic: new contribution = (1 − L) × [24.0m × 1.05 − 24.0m × 0.60], where 24.0m × 0.60 = EUR 14.4m is the unchanged variable cost base and 24.0m × 1.05 = EUR 25.2m is pocket revenue at full volume. At L = 0, contribution = 25.2m − 14.4m = 10.8m, a gain of EUR 1.2m on last year's EUR 9.6m.

## Timing and implementation

| Step | Segment | Date | Owner | Rule |
|---|---|---|---|---|
| Build into 2027 contract renewals | OEM key accounts (55%) | January 2027 renewal cycle | Key account director | No notice-period conflict — renewal and board decision land in the same month. |
| Issue 60-day price-list notice | Distributors (30%) | **Must go out by 31 December 2026** for a 1 March 2027 effective date | Sales director | **Conflict: this is before the board decides in January.** Either (a) the board needs to approve (or pre-clear) before 31 Dec 2026, or (b) the distributor effective date slips to roughly mid-to-late March 2027, about 60 days after the January decision. |
| Cap discount approval, then raise list price | Small direct accounts (15%) | 1 March 2027 | Sales director | No notice constraint, but the discount cap must land on or before the same date, or the increase leaks. |

This is the sharpest operational catch in the pack: **as framed, "board decides in January, effective 1 March" cannot be honoured for the distributor segment.** That doesn't kill the price increase — it means the board needs to either move its sign-off earlier or accept a later distributor start date.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Discounts and volume rebates stay the same percentage of list price after the increase; free freight stays a fixed per-shipment cost | Pocket price rises 5.2% (85.2 vs. 81) | Waterfall is quoted as % of list for discount/rebate; freight is a shipping cost, not price-linked | Freight were instead a %-of-list allowance — effect is under 0.2 points of list price, immaterial |
| 2 | Variable cost per unit is unchanged in euro terms when price rises | Contribution margin moves from 40% to ~42.9% of the new pocket price | Standard unit-economics convention — never re-apply the old margin % to a higher price | Material or labour costs are contractually indexed to the sale price, which would shrink the EBIT gain |
| 3 | Expected volume loss from a 5% increase ≈ 3%, scaled linearly from the 2023 episode (3% price → 2% loss) | 3% used as the central volume-loss case | Only revealed price/volume data point available | The 2023 drop had causes other than price (e.g. an account loss), which would make the true price elasticity — and the expected loss from this increase — smaller than assumed |
| 4 | "The board decides in January" means January 2027, the January immediately before the 1 March 2027 effective date | Used to flag the 60-day distributor notice conflict | Closest reading given the stated effective date | It means January 2026 — the notice conflict disappears entirely and the timing is comfortable |
| 5 | The 5% applies uniformly across all three segments, as the sales director asked | One flat 5% increase, no segment differentiation | This is the question as posed | Segment-level value/sensitivity data (not in this pack) showed OEM and distributors could bear more than small direct accounts, or vice versa |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What volume loss would the board treat as a failure of this increase? | Defines the real kill criterion against the computed 11.1% break-even and the 3% central estimate | Sales director / board | Sets how much headroom the board believes it has, independent of our math |
| Is 1 March 2027 a hard commercial commitment, or can it move by a few weeks for distributors? | Resolves the notice-period conflict identified above | Sales director | If flexible, no further action needed beyond informing distributors on time; if fixed, the board sign-off must move to before 31 Dec 2026 |
| Was the 2% volume drop after the 2023 increase caused by price alone, or partly by other factors (account losses, product mix, one-off)? | The entire expected-loss estimate rests on this one data point | Sales finance | Could tighten the estimate well below 3%, or raise it — though even a downside revision is unlikely to approach the 11.1% break-even |
| How are the two main competitors likely to react — hold, follow, or use spare capacity to undercut, especially in the OEM segment? | Changes which volume-loss scenario is realistic and whether the price gap closes or re-opens | Competitive intelligence from public price lists and win/loss data only — no competitor contact | A "follow" scenario strengthens the case; an "undercut" scenario in OEM (55% of volume) would need the stress case, not the central case |
| Is free freight a fixed shipping cost or a percentage-of-price allowance? | Minor refinement of how much of the 5% reaches pocket price | Logistics / finance | Immaterial either way (<0.2 points of list price) |
| Will the discount-approval cap for small direct accounts be in place by 1 March 2027? | Without it, 15% of volume is likely to leak the increase away through discounting | Sales director | Determines whether the EBIT effect in this pack is actually captured or quietly discounted away |

