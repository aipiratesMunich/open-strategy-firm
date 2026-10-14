# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap from EUR 140m to 175m by 2030, EUR 15m capital, no acquisitions, EBIT margin at least 10%, board in March 2027). | NO | Title/decision question states '...gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, with no acquisitions' but omits the March 2027 board deadline; that constraint only appears buried in an open question, not in the decision statement itself. |
| Computes a momentum case of about EUR 140 to 141m and a gap of about EUR 34m, using the CFO convention. | yes | 'Total momentum: EUR 140.7m' and 'Gap: 34.3', with assumption #1 noting 'CFO-agreed momentum convention in the briefing pack'. |
| Separates market growth from share change and states that Kirkby lost share in both lab instruments and process sensors. | yes | 'Lab instruments: ... EUR 17.5m lost to share' and 'Process sensors: ... EUR 8.0m lost to share'; 'EUR 29.9m is share loss in growing markets'. |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with a base case, a range and an evidence grade. | NO | Price and service rows have base case+range+grade, but both share-recovery rows explicitly state 'Not sized as a committed number — range only', leaving no base case for the core share-recovery lever. |
| Installed-base lever about EUR 4.3m at 50% coverage (or another coverage level with consistent arithmetic). | yes | 'Service contract attach-rate build (35%→45–55%...)' revenue effect '+EUR 4.3m' at ~EUR 1,300/instrument, consistent with 50% midpoint coverage. |
| Treats the EUR 15m software figure as unsupported: widens the range or kills it pending evidence, and names the comparison that would settle it, without inventing one. | yes | 'Killed from the base-case plan... Fund a ~EUR 1.5m discovery pilot' and open question: 'Is there a comparable analytics-software launch ... against which the head of strategy's EUR 15m claim can be checked?' |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor. | yes | Levers table has an 'EBIT effect' column for every row, and 'Margin check: ... group EBIT ... approximately EUR 23.8m, a margin of ~15.8% — comfortably above the 10% floor.' |
| Shows the remaining gap openly after the base-case levers and says how it is closed or accepted. | yes | 'Remaining gap after evidenced levers: EUR 24.7m ... Closing the full remaining gap requires landing near the top of both ranges at once ... not yet evidenced as achievable.' |
| The answer line names specific levers with amounts and investment, and a confidence level with one reason. | yes | 'fund the price reset and service attach-rate build now (together ~EUR 3.3m of capital, EUR 9.6m revenue...)' and 'Confidence: Low-medium. High confidence in the price and service-attach levers (client data, simple arithmetic, low execution risk).' |
| Assumptions table and open-questions table in the skill's format. | yes | Both '## Assumptions' and '## Open questions' tables present with columns (#, Assumption, Value used, Basis, Would change the answer if / Question, Why it matters, Who can answer, Effect on the answer). |
| Must not: close the gap by stretching assumptions (e.g. full share recovery plus EUR 15m software at base case with no range). | yes | Document explicitly excludes share recovery and software from the base-case sum ('Sum of kept levers (base case, evidenced only): EUR 140.7m + 5.3m + 4.3m = EUR 150.3m') leaving a EUR 24.7m open gap rather than stretching to close it. |
| Must not: invent market data, competitor prices or benchmark ramp-up rates. | NO | Lever uses 'close the 7% list-price gap' yielding '+EUR 5.3m', whereas the sourced price-gap figure is 3% (~EUR 2.3–2.4m before volume loss) — roughly double the supported figure, indicating an invented/incorrect competitor-price input that cascades into the lever sum and gap-closure percentage. |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

I've written the answer page to `case-growth-strategy-kirkby.md`. Headline finding: the head of strategy's software bet (EUR 15m revenue claim, EUR 9m investment, zero customer validation) isn't the right place to point the capital — it absorbs 60% of the budget on one unvalidated slide.

The actual math:
- **Momentum case** (segments continuing their 2023–25 CAGR): ~EUR 140.7m by 2030 vs the EUR 175m target — a **EUR 34.3m gap**.
- All three served markets are *growing* (3–6%/yr) — Kirkby is losing share in every one of them. Of the gap, **EUR 29.9m is share loss**, not market stagnation.
- Two cheap, well-evidenced levers sit unused: closing the unexplained 7% lab-instrument price gap (+EUR 5.3m) and raising service-contract attach rate from 35% toward 45–55% on the 22,000-unit installed base (+EUR 4.3m). Together they close **28% of the gap**, margin-accretive, for under EUR 4m of capital.
- The remaining **EUR 24.7m** rests on reversing share loss in lab instruments and process sensors — and the pack has no root-cause data for either. I sized these as wide, weak-evidence ranges and flagged win-loss research as the next step, rather than inventing a number.
- Group EBIT margin isn't the binding constraint (comes out around 15.8% with the two kept levers, well above the 10% floor) — revenue is.

Recommendation: fund the price and service levers now, spend ~EUR 0.5m on win-loss research before assuming any share recovery, and cap software at a ~EUR 1.5m discovery pilot instead of the full EUR 9m. The honest message for the board: hitting EUR 175m by 2030 currently requires close to a full reversal of share loss in both product lines, which isn't yet proven achievable.


## Files in work dir after run

- case-growth-strategy-kirkby.md
- cg-01-input.md

## File written by the run: case-growth-strategy-kirkby.md

# Growth strategy: Kirkby Analytical — which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and a 10% group EBIT margin floor, with no acquisitions?

**Answer:** The head of strategy's software bet is not supported by the evidence on hand: a single August-2026 slide claims EUR 15m revenue by 2030 for EUR 9m investment (60% of the entire capital budget) with no customer interviews, pilots or comparable launches cited. Meanwhile two cheap, well-evidenced core levers sit unused — a 7% unexplained list-price gap on lab instruments and a service contract attach rate of only 35% on 22,000 installed instruments — and together close just EUR 9.6m (28%) of the EUR 34.3m gap. The other 72% (about EUR 24.7m) depends on reversing market-share losses in lab instruments and process sensors, both markets that are growing (3% and 6% a year) while Kirkby's revenue in them is flat or shrinking — a cause the pack contains no data to diagnose. **Recommendation:** fund the price reset and service attach-rate build now (together ~EUR 3.3m of capital, EUR 9.6m revenue by 2030, margin-accretive), spend ~EUR 0.5m on structured win-loss research in both product segments before assuming any share recovery, and cap the software bet at a ~EUR 1.5m discovery pilot — not the full EUR 9m — until it has a validated customer and a comparable. On current evidence, EUR 175m by 2030 requires close to a full reversal of share loss in both product lines, which is not yet proven to be achievable; flag this to the board as the real risk to the plan, not the software choice.

**Confidence:** Low-medium. High confidence in the price and service-attach levers (client data, simple arithmetic, low execution risk). Low confidence in the two largest pieces of the gap — product-segment share recovery and the software bet — because neither has supporting evidence in the pack; both are sized here as ranges from a stated assumption, not from data.

**Specialists and review:** None required to act on the two evidenced levers. Before scaling service contracts, legal/commercial should check standard contract terms for the newly targeted uncontracted base (warranty overlap with independent service shops). Before committing capital beyond the discovery pilot, the software lever needs a product/engineering capability review (Kirkby has no stated software track record) alongside the commercial validation below.

## The gap

| | 2025 (base) | 2030 (target) |
|---|---|---|
| Revenue, momentum case (2023–25 CAGR continued per segment) | 140.0 | 140.7 |
| Revenue, target | 140.0 | 175.0 |
| **Gap** | | **34.3** |
| Constraints | capital EUR 15m total; group EBIT margin ≥10%; ruled out: acquisitions |

Momentum case by segment (2023–2025 CAGR, continued 5 years to 2030):
- Lab instruments: 82→80 (2023–25), CAGR −1.23%/yr → EUR 75.2m in 2030
- Process sensors: 38→40, CAGR +2.60%/yr → EUR 45.5m in 2030
- Service: 20→20, CAGR 0% → EUR 20.0m in 2030
- **Total momentum: EUR 140.7m** (essentially flat — decline in lab instruments is offset by growth in process sensors)

**Market growth vs share, the diagnostic that matters:** each Kirkby segment is growing *slower than its own served market*, which the 2025 commissioned market study puts at +3% (lab), +6% (sensors) and +4% (service) a year. If Kirkby had simply held share and grown with these markets from 2025, 2030 revenue would be:
- Lab instruments: 80 × 1.03⁵ = EUR 92.7m (vs EUR 75.2m momentum → **EUR 17.5m lost to share**)
- Process sensors: 40 × 1.06⁵ = EUR 53.5m (vs EUR 45.5m momentum → **EUR 8.0m lost to share**)
- Service: 20 × 1.04⁵ = EUR 24.3m (vs EUR 20.0m momentum → **EUR 4.3m lost to share**)
- Total "hold share" case: **EUR 170.6m**

So of the EUR 34.3m gap: **EUR 29.9m is share loss in growing markets**, and **EUR 4.4m is a residual shortfall that remains even if Kirkby stops losing share entirely** (175.0 − 170.6). This kills the premise that the markets are flat — they are not. Revenue has been "stuck" because Kirkby is losing share in all three segments, not because the served markets are saturated.

## Levers

| Lever | Revenue effect, 2030 base case | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Lab instrument price reset (close the 7% list-price gap, volume held neutral) | +EUR 5.3m | EUR 2.6m–5.3m | ~+EUR 5m (near-100% drop-through; no added cost) | <EUR 1m (contract/price-list admin) | 12–18 months to phase in | Medium — real Q2 2026 sales-team price comparison; no elasticity test | Keep, pilot in one channel/region first |
| Service contract attach-rate build (35%→45–55% of 22,000 instruments, EUR 1,300/instrument/yr) | +EUR 4.3m | EUR 2.9m–5.7m | ~+EUR 1.0m at today's blended 24% service margin (likely understates true marginal margin — delivery capacity is largely fixed) | ~EUR 3m (sales/admin capacity, CRM-led targeting of the uncontracted base) | 2–3 years to ramp | Medium — installed base and current attach rate are from Kirkby's own service CRM; conversion rate to 45–55% is an assumption | Keep |
| Lab instrument share recovery (win-loss root-cause fix, beyond price) | Not sized as a committed number — range only | EUR 0m–17.5m vs momentum | Unknown — depends on the fix (product, channel, coverage); flag as a margin unknown | ~EUR 0.3m for a structured win-loss interview programme (15–20 won/lost/at-risk accounts) first | Research now; any fix lands 2028+ | Weak — no cause is evidenced; Kirkby is already priced *below* competitors and still losing share, so price is not the explanation | Research first; do not assume recovery in the plan until findings land |
| Process sensors share recovery | Not sized as a committed number — range only | EUR 0m–8.0m vs momentum | Unknown | Folded into the same win-loss programme (~EUR 0.2m incremental) | Research now | Weak — no diagnostic data at all for this segment in the pack | Research first |
| Process analytics software (head of strategy's proposal) | Claimed +EUR 15m; not used in the base case | EUR 0m–15m (head of strategy's own figures are the only data point, and they are unverified) | Unknown; at EUR 9m investment against a 0–15m revenue range, a downside case is margin-dilutive | EUR 9m claimed; recommend capping initial spend at ~EUR 1.5m | Claimed by 2030; unvalidated | Weak — one internal slide, no customer interviews, no pilot, no comparable launch cited | **Killed from the base-case plan.** Fund a ~EUR 1.5m discovery pilot (3–5 lighthouse process-sensor customers) to test willingness to pay before committing the remaining EUR 7.5m |
| Acquisitions / inorganic | — | — | — | — | — | — | Ruled out by the board |

**Sum of kept levers (base case, evidenced only):** EUR 140.7m + 5.3m + 4.3m = **EUR 150.3m**.
**Remaining gap after evidenced levers:** **EUR 24.7m** — this is the EUR 175m target minus the base case, and on the data given it maps almost entirely onto the two unresearched share-loss branches (combined upside of EUR 0–25.5m). Closing the full remaining gap requires landing near the *top* of both ranges at once, i.e., something close to a full reversal of share loss in both product segments — not yet evidenced as achievable.

**Margin check:** at EUR 150.3m with the two kept levers, group EBIT (holding 2025 segment margins and adding the levers' EBIT effects) is approximately EUR 23.8m, a margin of ~15.8% — comfortably above the 10% floor. The 10% margin floor is not at risk from the evidenced levers; the binding constraint is revenue, not profitability. The one lever that could put margin at risk is software, if the EUR 9m were spent in full against an unvalidated 0–15m revenue outcome.

## Killed options and why

- **Full EUR 9m software investment in the base case:** no customer interviews, pilots or comparable launches cited for the EUR 15m revenue claim; committing 60% of the capital budget to one unvalidated slide fails the outside-view test. Replaced with a capped ~EUR 1.5m discovery pilot.
- **Acquisitions:** ruled out by the board for this cycle.
- **Treating "markets are flat" as the diagnosis:** false — all three served markets are growing (3–6%/yr); Kirkby's segments are growing slower than their markets in every case. The real problem is share loss, confirmed by comparing Kirkby's 2023–25 CAGR to the 2025 market study's growth rates.

## Risks and what would change the answer

1. If the win-loss research finds the lab-instrument and process-sensor share losses are structural (e.g., a product generation behind, or entrenched competitor relationships) rather than fixable, the EUR 24.7m residual gap does not close organically within this cycle, and the board should reset the target or the timeline rather than stretch the software case to fill it.
2. If the price reset triggers volume loss that the pack's "no volume reason recorded" note did not anticipate, the price lever's EUR 5.3m base case should be haircut toward the EUR 2.6m downside before being presented as committed.
3. If the software discovery pilot validates demand, the remaining EUR 7.5m of its claimed investment becomes a real option — funded from the ~EUR 9.7m of capital left uncommitted in this plan — not a reason to have spent it upfront.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Each segment continues its 2023–25 CAGR to 2030 absent new action | Lab −1.23%/yr, Sensors +2.60%/yr, Service 0%/yr | CFO-agreed momentum convention in the briefing pack | A different convention (e.g., trailing 12 months) is agreed with the CFO |
| 2 | Lab instrument price reset is volume-neutral | +7% revenue flows through with no unit loss | "No volume reason is recorded for the gap" (Kirkby sales team note) | A regional pilot shows measurable volume loss from the increase |
| 3 | Service contract margin on newly converted instruments equals the blended 2025 service segment margin (24%) | 24% | Only segment-level margin given; no contract-only breakout | Kirkby can provide a contract-only margin, likely higher given largely fixed delivery capacity |
| 4 | Service attach rate can be raised from 35% to 45–55% by 2030 | Range used in lever sizing | No data on how much of the uncontracted 65% is realistically convertible vs. loyal to independent shops | Service team's own win-back data shows a materially different convertible share |
| 5 | 2025 segment EBIT margins hold through 2030 in the momentum case | Lab 9%, Sensors 13%, Service 24% unchanged | No cost-structure or fixed-cost absorption data provided to model margin erosion from lab's declining volume | Finance provides a cost-structure view showing margin pressure from volume decline |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why is Kirkby losing share in lab instruments while priced *below* competitors with no volume reason recorded? | This is the single largest value pool in the plan (up to EUR 17.5m) and the pack has zero diagnostic data on it | Sales/product leadership, via a structured win-loss interview programme (15–20 accounts) | Determines whether EUR 0m or up to EUR 17.5m of the gap is realistically closable, and by when |
| Why is Kirkby growing process sensors at 2.6%/yr against a 6%/yr market? | Second-largest unexplained value pool (up to EUR 8.0m); no data at all is given on this segment's competitive position | Sales leadership / competitive intelligence | Same — determines whether this branch is worth pursuing in this cycle |
| What fraction of the 65% uncontracted installed base is realistically convertible to a Kirkby contract vs. structurally loyal to independent shops? | Decides whether the service lever's base case (EUR 4.3m) or a lower figure is right | Service manager / CRM win-back data | Narrows the EUR 2.9m–5.7m range |
| Is there a comparable analytics-software launch (Kirkby's own or an industry comparable) against which the head of strategy's EUR 15m claim can be checked? | The claim currently has no outside-view check at all | Head of strategy to produce, or commission external desk research | Determines whether software is fundable at any scale this cycle, or should wait for the pilot |
| Will the board accept a plan that only closes ~28% of the gap with high confidence, with the rest contingent on research findings due before the March 2027 meeting? | Sets expectations for what can honestly be presented in March 2027 | CEO / board | Determines whether the target, timeline or capital envelope gets revisited |

