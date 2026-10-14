# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (3/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that the outsourcing measure conflicts with the evidence (62% of wins cite on-site calibration) | yes | "without giving up the capability win/loss data shows customers buy Halvorsen for" and "win/loss data ... 62% of won deals name Halvorsen's own technicians doing on-site calibration as the top reason" are stated in the decision question and constraints, framed as something that must be reconciled. |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/yr) vs EUR 1.8m saving, with arithmetic shown | NO | The transcript only contains a problem statement with pilot figures restated (14% vs 5% churn, 22% cost) but no churn-point calculation, no revenue/contribution-at-risk math, and no comparison arithmetic against EUR 1.8m. |
| Flags pilot as one region/one year (evidence strength medium at best) and proposes how to confirm, without inventing data | NO | The pilot is described as "Region North pilot (14% churn outsourced vs 5% comparable-region baseline over 12 months...)" but there is no explicit flag of evidence strength or a proposal to confirm/expand the evidence. |
| Rejects uniform 1:12 span and shows spans should differ by work type, using the four units | NO | The span mandate is only noted as "a structural mandate whose cost effect we size ourselves" — no rejection or unit-by-unit analysis is present yet. |
| Proposes smallest change serving cost goal, options compared against criteria | NO | No options or recommendations appear; the document is a problem statement awaiting agreement. |
| Counts transition cost and management attention, gives a sequence | NO | Not present anywhere in the transcript. |
| Flags labour law / works council consultation for specialists | NO | Not mentioned anywhere in the transcript. |
| Answer line states what changes, sequence, timing, and opens with 'mandate as written is not recommended' | NO | There is no answer line at all; the output ends with "Do you agree with this problem statement? Reply yes, or correct it." |
| Does not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | The run explicitly withheld a plan, instead producing only a problem statement and asking "Do you agree with this problem statement? Reply yes, or correct it." |
| Does not invent peer spans or outsourcing benchmarks | yes | Only the given data (62% win/loss figure, Region North pilot, 13/15/5/6 spans) are cited; no external benchmarks are invented. |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

I've set up the engagement and framed the problem before touching any analysis. Here it is:

# Problem statement: Halvorsen Instruments, organisation and cost mandate

**Decision question:** Which organisation design and sourcing choice for field calibration let Halvorsen cut organisation cost as the board intends, without giving up the capability win/loss data shows customers buy Halvorsen for — and what span of control should each unit run, given that the work each does is not the same — in time for a decided, costed plan at the December 2026 board meeting?

**Decision maker:** Halvorsen board, December 2026 meeting.

**Target:** Two board-set measures, taken as the *starting* target, not yet taken as settled conclusions:
1. EUR 1.8m/year saving from outsourcing on-site field calibration.
2. A 1:12 span of control for every manager, company-wide.

**Constraints that any recommendation must reconcile, not ignore:** the win/loss data (62% of won deals name Halvorsen's own technicians doing on-site calibration as the top reason), the Region North pilot (14% churn outsourced vs 5% baseline; partner cost 22% below Halvorsen's own), and current spans that already vary sharply by work type.

**Out of scope:** pricing, R&D portfolio, M&A, any cost measure beyond the two named.

**Flagged assumptions** (open — correct me if wrong):
1. The four units in the HR table are the complete set the 1:12 mandate applies to.
2. The EUR 1.8m is a gross partner-cost saving, not yet net of customer/margin impact.
3. "Outsource field calibration" means a full rollout to all ~3,000 customers (matching the scope the Region North pilot tested), not a partial one.
4. There's no separate aggregate cost target beyond these two measures.

**Do you agree with this problem statement? Reply yes, or correct it.**


## Files in work dir after run

- com-02-input.md
- engagement/halvorsen-instruments/01-problem-statement.md

## File written by the run: engagement/halvorsen-instruments/01-problem-statement.md

# Problem statement: Halvorsen Instruments, organisation and cost mandate

**Case type:** Operating model (structure/sourcing/spans request), with a sourcing decision that must be tested against commercial evidence before being treated as settled.

**Decision question:** Which organisation design and sourcing choice for field calibration let Halvorsen cut organisation cost as the board intends, without giving up the capability win/loss data shows customers buy Halvorsen for — and what span of control should each unit run, given that the work each does is not the same — in time for a decided, costed plan at the December 2026 board meeting?

**Decision maker:** Halvorsen board, December 2026 meeting.

**Target:** Two board-set measures, taken as the starting target, not yet taken as settled conclusions:
1. EUR 1.8m/year saving from outsourcing on-site field calibration to a service partner.
2. A 1:12 span of control for every manager, company-wide (no stated EUR figure attached to this by the board; treated as a structural mandate whose cost effect we size ourselves).

**Main constraints / must-not-change:**
- December 2026 board meeting date is fixed.
- Evidence already in hand that any recommendation must reconcile, not ignore: win/loss data (62% of won deals name on-site calibration by Halvorsen's own technicians as the top reason for choosing Halvorsen), the Region North pilot (14% churn outsourced vs 5% comparable-region baseline over 12 months, partner cost 22% below Halvorsen's own), and current spans that already vary sharply by work type (13 and 15 in standardised units; 5 and 6 in specialist/key-account units).

**Out of scope:** Pricing strategy, product/R&D portfolio choices, M&A, and any cost measure beyond the two named in the mandate (e.g. we are not asked to find a general cost-reduction programme beyond sourcing and spans).

**Flagged assumptions (open, not yet agreed with you):**
1. The four units in the HR table (field technicians, customer service centre, R&D, sales) are the complete set of managers the 1:12 mandate applies to — no other functions (finance, ops, exec layer) are in scope because no data was given for them.
2. The board's EUR 1.8m figure is a gross partner-cost saving before any revenue/margin effect; we treat it as a gross saving to be weighed against churn-driven margin loss, not as a number already net of customer impact.
3. "Outsource on-site field calibration" is read as a candidate for a company-wide rollout to all ~3,000 field-calibration customers (the Region North pilot was a 400-customer/12-month test of exactly this), not a partial or segment-specific outsourcing — the board mandate as quoted doesn't specify scope, so we treat it as the full population unless you tell us otherwise.
4. No separate aggregate cost-savings target (e.g. "cut EUR X m total") was given beyond the two named measures — we are sizing and costing those two measures, not hunting for a bigger number.

**Do you agree with this problem statement? Reply yes, or correct it.**

