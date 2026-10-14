# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence that customers choose Halvorsen for on-site calibration (62% of wins) | yes | '62% of **won** deals name on-site calibration **by Halvorsen's own technicians**... This is the company's primary acquisition driver, not a commodity activity.' stated in the opening 'Why both measures fail' section and chat summary. |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/yr) vs EUR 1.8m saving, with arithmetic shown | yes | '14%... against 5%... 9-point incremental churn... 270... EUR 4.86m... EUR 4.86m × 45% = EUR 2.187m/year... Net effect... EUR 1.8m saved − EUR 2.187m ≈ EUR −0.39m/year' |
| Flags pilot as one region/one year (medium evidence at best) and proposes confirmation without inventing data | yes | 'Region North pilot (400 customers, 12 months...)'; open question 'Does the elevated pilot churn persist beyond 12 months... Extended Region North data'; assumption note 'a longer or multi-region pilot shows the effect is smaller, temporary, or segment-specific' |
| Rejects uniform 1:12 span, shows spans should differ by work type using the four units, noting narrowing of field/service and widening of R&D/sales | yes | Table showing Field +2, CS +1, R&D −5, Sales −3 under literal 1:12; 'Field and Customer Service are already at or above a 1:12 span... R&D and Sales are well below 1:12' |
| Proposes smallest change serving cost goal, with options compared against criteria | yes | Options table: 'Comply literally' (Rejected) vs 'Redesigned path (recommended)' vs 'Span redesign only' scored on 'Meets EUR 1.8m target / Risk to differentiator / Transition risk'; keeps field in-house, proposes productivity study and segmented pilot with control group |
| Counts transition cost and management attention, gives a sequence | yes | 'one-off transition costs (severance, partner contract set-up, customer communication...)'; 7-step Transition plan table with owners/dates; sequencing note on Sales 'managing customer anxiety... during same window' |
| Flags labour law and works council consultation for specialists | yes | 'HR/Legal must confirm works-council and redundancy/redeployment requirements before any R&D or Sales delayering is announced' |
| Answer line states what changes, sequence, by when, and first line says mandate as written not recommended | yes | 'Do not roll out blanket outsourcing of on-site field calibration, and do not apply a flat 1:12 span everywhere... Sequence: validate by 2026-11-15, present to the board 2026-12, implement spans Q1 2027...' |
| Must not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | Response rejects both ('Option 1. Comply literally... Rejected') and substitutes an alternative plan instead of the requested one |
| Must not invent peer spans or outsourcing benchmarks | yes | 'the span targets for R&D and Sales are directional design points, not validated benchmarks'; assumptions table flags them as 'not a validated organisational benchmark' |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

Saved to `case-operating-model-halvorsen.md`. Summary of the key findings:

**Outsourcing:** full rollout nets roughly **−EUR 0.39m/year**, not +EUR 1.8m — the pilot's 9-point incremental churn (14% vs 5% control), applied to the 3,000-customer base, costs EUR 2.19m/year in contribution margin, against a EUR 1.8m saving. And 62% of won deals cite Halvorsen's *own* technicians specifically, so this is the differentiator, not a commodity to hand off.

**1:12 span:** applied literally, it *adds* managers in Field (+2) and Customer Service (+1), which are already above 1:12, while cutting R&D leads by 56% and Sales managers by 50% — concentrating all the risk in the two specialist/key-account populations where tight spans are most dangerous.

**Recommendation instead:** reject both as written; widen R&D and Sales spans moderately (to ~1:7–8 and ~1:8–9, net 4–5 fewer leads/managers), leave Field and CS untouched, and replace blanket outsourcing with a segment-limited, controlled pilot — closing part of the EUR 1.8m gap now and sizing the rest only once segment-level churn data exists. Full transition plan with owners and dates runs from validation (by 2026-11-15) through board presentation (December 2026) to a Q3 2027 reconciliation of savings achieved.

Biggest open item before this goes to the board: manager compensation data to convert the headcount deltas into EUR, and confirmation from HR/Legal on works-council constraints for the R&D/Sales delayering.


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments — meeting the board's EUR 1.8m cost target without the two measures as literally mandated

**Answer:** Do not roll out blanket outsourcing of on-site field calibration, and do not apply a flat 1:12 span everywhere. The evidence shows both, as literally stated, cost more than they save. Instead: (1) redesign spans by work type — widen R&D from ~1:5 to ~1:7–8 and Sales from ~1:6 to ~1:8–9 (net ~4–5 fewer manager/lead positions), leave Field and Customer Service spans unchanged; (2) replace blanket outsourcing with a segment-limited, controlled pilot that excludes any customer group where Halvorsen's own technicians are a stated reason for buying, before committing further spend; (3) run a field-technician productivity/route study to close part of the partner's 22% cost gap in-house. Sequence: validate by 2026-11-15, present to the board 2026-12, implement spans Q1 2027, run the segmented pilot through 2027, reconcile savings against the EUR 1.8m target in Q3 2027.

**Confidence:** High on the rejection of both measures as written — the numbers come straight from the board's own pilot and win/loss data. Medium on the replacement package — the span targets for R&D and Sales are directional design points, not validated benchmarks, and the segmented-outsourcing option still needs a dedicated pilot before it can be sized.

**Specialists and review:** HR/Legal must confirm works-council and redundancy/redeployment requirements before any R&D or Sales delayering is announced; Finance should independently verify the EUR 1.8m savings figure's scope (gross vs net of partner contract costs) before it is reconfirmed to the board.

---

## Why both measures fail as written

### 1. Outsourcing field calibration: the pilot shows it costs more than it saves

- 62% of **won** deals name on-site calibration **by Halvorsen's own technicians** — not "on-site calibration" generically — as the top reason for choosing Halvorsen. This is the company's primary acquisition driver, not a commodity activity.
- Only 9% of **lost** deals name price. Price is not the lever that is costing Halvorsen deals, so a cost-driven move that risks the service relationship is trading a small, unproven upside for a large, proven downside.
- The Region North pilot (400 customers, 12 months, outsourced) churned at 14%, against 5% in comparable regions that kept the in-house service. That is a **9-point incremental churn effect directly attributable to outsourcing**, estimated against a real control group — the strongest piece of evidence in the dataset.
- Scaled to the full 3,000-customer on-site calibration base, at EUR 18,000 average revenue and 45% contribution margin:
  - Incremental customers lost: 9% × 3,000 = **270**
  - Revenue at risk: 270 × EUR 18,000 = **EUR 4.86m**
  - Contribution margin lost: EUR 4.86m × 45% = **EUR 2.187m/year**
- Net effect of full rollout: **EUR 1.8m saved − EUR 2.187m contribution lost ≈ EUR −0.39m/year**, before counting (a) one-off transition costs (severance, partner contract set-up, customer communication — not sized in the data given) and (b) the likely knock-on effect on the 62%-of-wins driver for *new* deals, not just retention of existing customers, which is not measured by the pilot and would make the loss larger.
- **Hypothesis "field calibration is a commodity a partner can do at acceptable risk" is killed.** It is a proven source of competitive advantage, and blanket outsourcing fails the trap check "no activity customers choose the client for is outsourced."

### 2. A flat 1:12 span is not one lever — it is four different levers, two of which add cost and risk

| Unit | Current managers | Current span | Total reports | At literal 1:12 | Change | Work type |
|---|---|---|---|---|---|---|
| Field technicians | 14 | 13 | 182 | 16 | **+2** | Standardised, dispersed |
| Customer service | 4 | 15 | 60 | 5 | **+1** | Standardised, high-volume |
| R&D (sensor design) | 9 | 5 | 45 | 4 | **−5** | Specialist, non-routine |
| Sales | 6 | 6 | 36 | 3 | **−3** | Key-account, non-routine |

- Field and Customer Service are **already at or above** a 1:12 span. Forcing exactly 1:12 would *add* 3 management positions in the two units doing standardised, low-complexity work — the opposite of the board's cost intent.
- R&D and Sales are well *below* 1:12. Literal compliance cuts R&D leads by 56% (9→4) and Sales managers by 50% (6→3) — in exactly the two populations doing specialist, non-routine, relationship-dependent work, where span and coaching capacity matter most and where no data in hand supports that depth of cut being safe.
- Net literal effect: 33 managers → 28 (−5), but the entire saving is manufactured by over-cutting R&D and Sales to pay for unnecessary additions in Field and CS. This is the textbook "one-size span" trap: it treats a field-service lead and a research lead as interchangeable.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Protect the deal-winning differentiator | In-house, trusted on-site calibration relationship | Sustain ≤5% baseline churn on the 3,000-customer calibration base | 5% baseline (comparable regions); 14% where outsourced | Outsourcing itself is the gap driver |
| Cut organisation cost toward EUR 1.8m/year | Lean management layer matched to work complexity | Manager cost reduced without coaching/coverage loss in specialist or key-account work | 33 managers, spans ranging 5–15 | Spans don't reflect work type; no segment-level outsourcing data exists |

## Root causes of the gap

| Gap | Process/system cause | Decision-rights cause | Structure cause | People/skills cause |
|---|---|---|---|---|
| Outsourcing destroys value | No segmentation of which customers value in-house technicians | No one owns a "which accounts are safe to outsource" decision today | Mandate applied to the whole 3,000-customer base at once | — |
| Span target adds cost in 2 of 4 units | — | Span target set centrally without function input | Uniform target ignores standardised vs specialist/key-account axis | R&D/Sales leads given no say in load they can safely carry |

## Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Outsourcing scope and pace | COO/Board | CFO, Head of Sales Ops, Head of Field Ops | Field Ops + partner | Board mandate with no segmentation — needs an owner |
| Span targets per function | COO with function heads | HR, R&D/Sales/CS/Field leadership | HR + function heads | Set centrally with no function input — needs to move down |
| Segmented pilot design and kill criteria | CFO + Head of Sales Ops | Sales ops, Field ops, Finance | Sales ops/analytics | Not yet defined |
| Redeployment of surplus R&D/Sales leads | HR Director | Function heads, Legal/works council | HR + function heads | Not yet defined |

## Structure options

| Option | Description | Meets EUR 1.8m target | Risk to differentiator / capability | Transition risk | Score |
|---|---|---|---|---|---|
| 1. Comply literally | Outsource all 3,000 accounts; flat 1:12 everywhere | Net **−EUR 0.39m/yr** (fails) | High — hits the 62%-of-wins driver and guts R&D/Sales leadership | High — abrupt, no validation | Rejected |
| 2. Redesigned path (recommended) | No blanket outsourcing; segmented pilot only; differentiated spans (R&D ~1:7–8, Sales ~1:8–9, Field/CS unchanged); field productivity study | Partial now (~4–5 fewer manager positions + productivity savings), rest sized after pilot | Low–moderate — protects the differentiator, validates before scaling | Moderate — phased, with redeployment process | **Recommended** |
| 3. Span redesign only, no outsourcing | Drop outsourcing; keep differentiated spans | Falls short of EUR 1.8m alone | Lowest | Low | Fallback if the segmented pilot fails |

## Spans, layers, sourcing

- **Field technicians:** no change. Span (13) already fits standardised, dispersed work; narrowing to 12 adds a lead for no quality benefit.
- **Customer service:** no change. Span (15) already exceeds 12; narrowing adds a supervisor for no quality benefit.
- **R&D:** widen to ~1:7–8 (9 → ~6 group leads), not to 1:12. Specialist, non-routine work needs more coaching bandwidth than standardised work; validate the exact target with R&D leadership before implementing.
- **Sales:** widen to ~1:8–9 (6 → ~4–5 managers), not to 1:12, and sequence after the calibration decision stabilises — key-account managers will be managing customer anxiety from any calibration change during the same window.
- **Sourcing:** on-site field calibration stays in-house for the full base now. Test a segment-limited outsourcing pilot (replicate the Region North design, with a control group) only in customer groups shown not to value Halvorsen's own technicians, once that segmentation exists. No blanket move.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Validate R&D/Sales span targets with function leadership; obtain manager compensation data to monetise savings | HR Director + function heads | By 2026-11-15 | Targets agreed; EUR savings estimate produced |
| 2 | Design segmented outsourcing pilot: identify a candidate low-differentiation customer group, control group, churn kill criteria | CFO + Head of Sales Ops | By 2026-11-15 | Pilot design and kill criteria approved |
| 3 | Present redesigned recommendation to the board: reject blanket outsourcing and flat 1:12; approve differentiated spans and segmented pilot | CEO/COO | December 2026 board meeting | Board approval |
| 4 | Delayer R&D (9→~6 leads) and Sales (6→~4–5 managers); redeploy/exit surplus leads via HR process | HR + function heads | Q1 2027 | Headcount reduced; no unplanned attrition of key specialists |
| 5 | Launch segmented outsourcing pilot in the agreed customer group, with control group | Head of Field Ops + partner | Q1 2027 start, 6–12 months | Churn differential at or below agreed threshold vs control |
| 6 | Field technician route/productivity study to narrow the 22% cost gap in-house | Head of Field Ops | Q1–Q2 2027 | EUR cost-per-calibration gap reduced, quantified |
| 7 | Reconcile savings achieved against the EUR 1.8m target; decide on any further outsourcing scope | CFO + Board | Q3 2027 | Decision made; EUR 1.8m target reconciled or revised with the board |

## What would change the answer

1. If a segmented pilot shows no incremental churn in a defined low-differentiation customer group, outsourcing that segment becomes a genuine, sizeable saving.
2. If R&D/Sales leadership confirm wider spans (closer to 10–12) work without coaching or coverage loss, further delayering can be approved on top of the 4–5 positions already identified.
3. If Region North's win-rate data (not just churn) during the pilot shows no degradation in new-deal acquisition, the downside case is smaller than estimated here — though the churn loss alone still stands.
4. If manager compensation is low relative to what's assumed, the span-redesign savings may be insufficient on their own, widening the remaining gap to the EUR 1.8m target.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The pilot's 9-point incremental churn persists at full scale and recurs annually | 9pp → EUR 2.187m/yr contribution loss | Region North pilot vs comparable regions, 12 months, client data | A longer or multi-region pilot shows the effect is smaller, temporary, or segment-specific |
| 2 | The EUR 1.8m figure is the board's full expected saving from outsourcing, net of partner contract/admin cost | EUR 1.8m as given | Board mandate | If the figure is gross, true net savings are lower and the negative case widens further |
| 3 | R&D and Sales can be delayered to roughly 1:7–8 and 1:8–9 without capability loss | 9→~6 leads (R&D); 6→~4–5 managers (Sales) | Directional design point from "specialist/non-routine" and "key-account" work type labels; not a validated organisational benchmark | Function leadership or an org-design benchmark shows these spans are still too tight, or that looser spans are safe |
| 4 | Field and customer-service spans (13, 15) already fit standardised work and need no change | No change | Current HR data; work type labelled "standardised" | Handle-time/quality data or peer benchmarks show room to widen further or a need to narrow |
| 5 | Manager compensation is roughly comparable in scale across functions, so headcount deltas are a reasonable proxy for EUR savings | Not yet converted to EUR | Not given in the dataset | Comp data shows manager cost differs sharply by function, changing the EUR savings from the position-count proxy |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is fully-loaded manager compensation by function? | Converts the ~4–5 position headcount reduction into EUR against the EUR 1.8m target | HR/Finance | Determines how much of the target the span redesign alone can close |
| Does the elevated pilot churn persist beyond 12 months, or is it a one-off transition effect? | Determines whether outsourcing's true annual cost is ~EUR 2.2m/yr or smaller/one-off | Extended Region North data | Changes whether any outsourcing, even segmented, can ever be net positive |
| Did Region North's new-deal win rate also drop during the pilot, not just retention? | The 62%-of-wins statistic suggests an acquisition risk, not just a retention risk | Sales ops regional win/loss data during the pilot window | Could increase the estimated value destroyed well beyond the EUR 2.187m churn figure |
| Which customer segments, if any, are genuinely indifferent to who performs on-site calibration? | Defines where a segmented outsourcing pilot could plausibly succeed | Customer/account data, satisfaction or attribute surveys | Determines whether any outsourcing path toward the EUR 1.8m target exists at all |
| What do works council agreements or local labour law require for the R&D/Sales delayering? | Legal constraint on timeline and method (redundancy vs attrition vs redeployment) | HR/Legal | Could push the Q1 2027 implementation date or force an attrition-based approach instead |

