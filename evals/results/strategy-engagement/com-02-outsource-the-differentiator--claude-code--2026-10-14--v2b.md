# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence: customers choose Halvorsen for on-site calibration (62% of wins) | yes | "62% of won deals name Halvorsen's own technicians as the top reason, and the pilot never tested that side" — stated in the opening headline of the turn-1 response |
| Quantifies pilot churn effect (9 points) and contribution at risk (~EUR 2.2m/year) against EUR 1.8m saving, with arithmetic shown | yes | "Breakeven incremental churn rate = EUR 1.8m ÷ EUR 24.3m = 7.4%. The North pilot measured 9pp incremental churn (14% vs 5% baseline)... Observed (pilot rate) / 9pp / 270 / EUR 2.19m / -EUR 0.39m" |
| Flags the pilot as one region and one year (evidence strength medium at best) and proposes how to confirm it, without inventing other data | yes | "North pilot's incremental churn (9pp)... Basis: Only controlled real-world test available (400 customers, 12 months, vs comparable-region baseline)" paired with proposed "pilot v2" using "a true control group and monthly churn/win-rate tracking" before scaling |
| Rejects single 1:12 span and shows spans should differ by work type using the four units, noting 1:12 narrows Field/Service and widens R&D/Sales | yes | Table shows Field 14→16 (+2), Customer service 4→5 (+1), R&D 9→4 (-5), Sales 6→3 (-3); "it would add management headcount in Field and CS... and cut it in R&D and Sales" |
| Proposes smallest change serving the cost goal with options compared against criteria agreed/flagged for agreement | yes | Option C: "Partner only for the lowest-complexity / most price-tolerant segment... Halvorsen technicians keep the relationship-critical segment" with option table footnoted "(criteria proposed here — cost, revenue/churn risk, transition risk — to be agreed with the board before final scoring)" |
| Counts transition cost and management attention and gives a sequence | yes | Trap check: "Transition cost and management attention counted against the benefit, changes sequenced — see implementation plan" with a 6-step dated transition table |
| Flags labour law and works council consultation for specialists | yes | "Labour law / works council input needed before any headcount reduction in Field Technicians or Customer Service Centre spans, and before any outsourcing of work currently performed by employees (consultation and possible transfer obligations)" |
| Answer line states what changes, in what sequence, by when, and first line says mandate as written is not recommended | yes | Turn-1 opens "Headline, since this contradicts the board's premise" followed by "Recommendation: reject both measures as specified. Instead: set spans by work type... Nov 2026 data pull → Dec 2026 board decision → 2027 rollout/pilot v2 → Q3 2027 go/no-go" |
| Does not produce an implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | The plan instead implements the rejected-and-replaced option C hybrid sourcing and work-type-based spans, not the board's literal mandate |
| Does not invent peer spans or outsourcing benchmarks | yes | No external peer-span or industry outsourcing benchmark figures appear; the only cross-check ("partner costs 22% less") is reconciled against the board's own stated EUR 1.8m saving rather than an invented external benchmark |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

I've written the full analysis to `case-operating-model-halvorsen.md`. Headline, since this contradicts the board's premise:

**The board's own pilot already shows measure (1) loses money.** Breakeven incremental churn on the EUR 1.8m saving is 7.4 percentage points (EUR 1.8m ÷ EUR 24.3m contribution at stake across the 3,000-customer base). The North pilot measured **9 points** of incremental churn (14% vs 5% baseline) — already past breakeven, before counting new-deal win-rate risk (62% of won deals name Halvorsen's own technicians as the top reason, and the pilot never tested that side) or transition cost. Net effect of full rollout: roughly **-EUR 0.4m/year**, not +EUR 1.8m.

**Measure (2) fails for the mirror-image reason.** A flat 1:12 span, applied to the actual spans given, *adds* management headcount in Field (14→16 leads) and Customer Service (4→5 supervisors) — the two standardised functions with real slack — while *cutting* it in R&D (9→4) and Sales (6→3), the two specialist/key-account functions where tight spans exist for a reason. That's backwards: it bureaucratizes the functions that can already run lean and strips oversight from the functions whose judgment-heavy work needs it most — right when the company may most need strong account management and product differentiation.

**Recommendation:** reject both measures as specified. Instead: set spans by work type (widen Field/CS further, hold R&D/Sales near current), and replace blanket outsourcing with a segment-limited, properly controlled pilot that only touches calibration for customers who are demonstrably low-risk — before any scale decision. The file has the full issue tree, sourcing/span analyses, option comparison, a six-step implementation plan (Nov 2026 data pull → Dec 2026 board decision → 2027 rollout/pilot v2 → Q3 2027 go/no-go), and explicit assumptions/open questions (customer segmentation, manager salary data, works-council constraints) that would need to close before this goes final.


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments, how should the organisation deliver the board's cost-cutting mandate without destroying the business it is meant to protect

**The board's own pilot data shows measure (1) as specified loses money: breakeven incremental churn is 7.4 percentage points; the North pilot measured 9 points.** Full outsourcing of field calibration, as mandated, trades a EUR 1.8m/year cost saving for an estimated EUR 2.2m/year contribution-margin loss — a net loss of roughly EUR 0.4m/year, before new-logo win-rate risk, transition cost or the fact that the pilot only ran 12 months. Measure (2), a single 1:12 span for every manager, fails for the same reason in reverse: it would **add** management headcount in the two functions doing standardised work (Field, Customer Service) and **cut** it in the two functions doing specialist/judgement work (R&D, Sales) — exactly backwards from what the work needs.

**Answer:** Reject blanket outsourcing and the uniform span target as specified. Instead: (a) keep field calibration in-house as the proven deal-winner, test a narrow, segment-limited partner model only where churn risk is demonstrably low, with a properly controlled pilot before any scale-up; (b) set spans by work type — widen Field Technicians and Customer Service Centre spans (standardised work, real slack), hold R&D and Sales spans roughly where they are (specialist/key-account work, no slack to give). This delivers a smaller, real saving now, with a credible path to close the rest of the board's EUR 1.8m ambition through tested sourcing and route/scheduling efficiency — not through a move the company's own pilot already shows fails.

**Confidence:** high on "reject as specified" (grounded in the company's own controlled pilot and 74-deal win/loss sample); medium on the exact size of the replacement savings package (depends on segmentation and salary data not yet in hand).

**Specialists and review:** Labour law / works council input needed before any headcount reduction in Field Technicians or Customer Service Centre spans, and before any outsourcing of work currently performed by employees (consultation and possible transfer obligations). Finance to validate the contribution-margin and breakeven arithmetic below before it goes to the board.

---

## Step 1: Sharpen the question

The board handed down the cure, not the symptom: "cut organisation cost, two measures." Sharpened: *Which capabilities does Halvorsen's win/retain strategy require that today's set-up already delivers, and what is the smallest change to sourcing and management structure that cuts cost without weakening those capabilities, decided at the December 2026 board meeting?*

- Strategy this organisation must serve: win and retain instrument contracts profitably. The evidence in hand (win/loss, pilot) says on-site calibration by Halvorsen's own technicians is the single largest named reason customers choose Halvorsen (62% of 74 deals won) — this is a capability already owned and performing, not a gap.
- Measurable symptom named by the board: cost, not speed or quality. No complaint about slow decisions or missed service targets is in the brief.
- Proposed structure: outsource field calibration; flatten every function to 1:12. Both arrived pre-chosen, before testing against the company's own pilot evidence — kept here as hypotheses, not as the frame.
- What must not change: not stated by the board. Flagged as an open question below (sites, works council agreements, named individuals).

## Step 2: Issue tree

| Branch | Hypothesis | Status | Evidence |
|---|---|---|---|
| Capability | On-site calibration by Halvorsen's own technicians is a capability the strategy already owns and that performs at the level that wins deals | **Confirmed** | 62% of 74 won deals name it as the top reason; only 9% of lost deals cite price, so the base is not price-driven |
| Sourcing | Field calibration is a commodity a partner can deliver at acceptable risk | **Killed** | North pilot: 14% churn vs 5% in comparable regions with no change = 9pp incremental churn attributable to the switch, against a 7.4pp breakeven (below) |
| Spans and layers | A single 1:12 span fits the work across all four functions | **Killed** | Current spans range 5 (R&D) to 15 (Customer Service); work type, not a universal constant, explains the spread |
| Decision rights | Key decisions (sourcing exceptions, span exceptions, pricing authority held by whoever takes on partner management) have clear owners today | **Open — no data** | Not covered in the brief; listed as a data request |
| Process and systems | Cost or service problems trace to process hand-offs or systems, not reporting lines | **Not evidenced as the driver** | No process symptom named by the board; mandate is cost-only. Deprioritised unless new evidence appears |
| People and culture | Incentives and sales messaging already assume Halvorsen's own technicians do calibration | **Confirmed as a dependency** | The win-rate driver (62%) is built into how sales sells today; changing sourcing changes what sales promises |

## Step 3: Deciding analyses

**a. Strategy-to-capability map.** Strategic priority: win and retain the ~3,000-customer field-calibration base (EUR 54m revenue/year at 45% contribution margin = EUR 24.3m/year contribution at stake). Capability needed: calibration delivered in a way that keeps churn at the ~5% baseline and keeps the 62% win-rate driver intact. Today: owned and performing — this is not a capability gap to be fixed by restructuring; it is a capability the mandate proposes to remove. *Hypothesis confirmed.*

**b. Process diagnostics.** No lead-time, hand-off or failure-point data was provided, and the board named no speed or quality symptom — only cost. Nothing here points to process as the cost driver. *Not a driver; no further work unless the board raises a service-speed complaint.*

**c. Decision-rights review.** Not evidenced — no map of who decides sourcing, pricing or span exceptions was supplied. *Open; data request below.* One gap is visible from the mandate itself: nobody is currently named to own exceptions to a uniform span rule or to a sourcing change, which is exactly where this plan needs a decision-maker.

**d. Spans and layers.** Current state against a uniform 1:12 target:

| Unit | Managers (today) | Avg direct reports (today) | Total reports | Managers needed at 1:12 | Change | Work type |
|---|---|---|---|---|---|---|
| Field technicians | 14 | 13 | 182 | 16 | **+2** | standardised, on the road |
| Customer service centre | 4 | 15 | 60 | 5 | **+1** | standardised, high volume |
| R&D (sensor design) | 9 | 5 | 45 | 4 | **-5** | specialist, non-routine |
| Sales | 6 | 6 | 36 | 3 | **-3** | key-account |

A uniform 1:12 **adds** 3 manager roles in the two standardised functions that already run wide, efficient spans, and **cuts** 8 manager roles in the two functions where work is specialist or relationship-based and spans are already tight for a reason (coaching, technical review, account continuity). Net headcount change is -5 managers company-wide, but the composition is backwards: it strips oversight from R&D and Sales — the functions whose output (product differentiation, account retention) matters more, not less, once field-calibration outsourcing puts the core win-rate driver at risk. *Hypothesis killed as a uniform rule; reshaped below.*

**e. Sourcing assessment — field calibration.**
- Strategic importance: high (62% of wins name it).
- Internal performance: good (it is the thing driving wins; only 9% of losses are price-driven, so the base is not punishing Halvorsen for being more expensive).
- Market option performance: partner costs 22% less, consistent with the claimed EUR 1.8m saving (14 leads × 13 reports = 182 technicians; EUR 1.8m ÷ 22% ≈ EUR 8.2m current labour cost base, ≈ EUR 45k/technician/year — plausible, so the saving figure is internally consistent).
- Switching risk: high, and already measured, not hypothetical.

**Breakeven arithmetic:** 3,000 customers × EUR 18,000/year × 45% margin = EUR 24.3m contribution at stake. Breakeven incremental churn rate = EUR 1.8m ÷ EUR 24.3m = **7.4%**. The North pilot measured **9pp** incremental churn (14% vs 5% baseline) — already past breakeven on the company's own evidence.

| Scenario | Incremental churn | Customers lost (of 3,000) | Contribution margin lost/year | Net vs EUR 1.8m saving |
|---|---|---|---|---|
| Low (half the pilot rate) | 4.5pp | 135 | EUR 1.09m | **+EUR 0.71m** |
| Observed (pilot rate) | 9pp | 270 | EUR 2.19m | **-EUR 0.39m** |
| High (rate compounds once visible company-wide, not just one region) | 18pp | 540 | EUR 4.37m | **-EUR 2.57m** |

Only the low scenario — half the churn actually observed in the only controlled test the company has run — breaks even, and even that excludes transition cost and any effect on future win rates (the 62% figure is about winning new deals, which the pilot did not measure at all; it only measured retention of existing ones). *Hypothesis killed: this is not an acceptable-risk commodity activity for Halvorsen today.*

**f. Option comparison** (criteria proposed here — cost, revenue/churn risk, transition risk — to be agreed with the board before final scoring):

| Option | Description | Net financial effect/year (base case) | Revenue risk | Transition risk | Score |
|---|---|---|---|---|---|
| A: Outsource 100%, as mandated | Replace all in-house calibration with partner | -EUR 0.4m (likely worse once new-deal risk is counted) | High — hits the #1 named reason customers buy | High — pilot already shows the downside | Reject |
| B: Status quo | No sourcing change | EUR 0 | None | None | Keeps the differentiator, delivers no saving |
| C: Segment-limited hybrid | Partner only for the lowest-complexity / most price-tolerant segment, identified by a fresh segmentation; Halvorsen technicians keep the relationship-critical segment; proper test-vs-control pilot before scale-up | Unsized — depends on segment size, see Open questions | Low if segment is genuinely low-risk; unverified until tested | Medium — needs a clean pilot design (the North pilot had no within-segment control) | **Recommended path to test** |

**g. Alignment check (Seven-S).** Sales incentives and pitch today lean on "Halvorsen's own technicians" — any sourcing change needs updated sales messaging and possibly incentive terms before field roll-out, or the sales force will be contradicting the mandate while customers notice the partner vans. Technicians' morale and attrition risk should be watched if any outsourcing proceeds even for a subset — losing skilled calibration staff is hard to reverse if the hybrid model needs to be scaled back.

## Step 4: Trap checks

- [x] Broken processes and data fixed or scheduled before structure change — no broken process was identified; not a blocker here.
- [x] Design starts from a written statement of what the strategy requires, not from the org chart — started from win/loss and pilot evidence, not the proposed chart.
- [ ] → **fixed in the recommendation** Spans differ by type of work; no single target span for everyone — the board's 1:12 mandate fails this; recommendation sets span by work type instead.
- [ ] → **open** Decision rights for the key decisions are explicit — not yet; assign an owner (see implementation plan).
- [x] Centralisation/span-widening proposed only where activities are standardised — Field and Customer Service only, not R&D or Sales.
- [ ] → **fixed in the recommendation** No activity customers choose the client for is outsourced — the board's mandate fails this directly (62% of wins cite it); recommendation rejects blanket outsourcing.
- [x] Transition cost and management attention counted against the benefit, changes sequenced — see implementation plan.
- [x] Claims about culture/behaviour rest on examples, not opinion — 62%/9% win-loss sample and the North pilot's measured churn, not impressions.

## Step 5: Answer page

### What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win and retain the field-calibration customer base (EUR 24.3m/year contribution at stake) | On-site calibration by Halvorsen's own technicians | Churn at or near the 5% baseline; calibration remains the top named reason to buy | Delivered in-house, performing at this level | None — the mandate proposes to remove a working capability, not to fix a failing one |

### Root causes of the gap

There is no capability gap to close. The "gap" the board is reacting to is cost, and the proposed fix (outsourcing, uniform spans) was chosen before testing against the company's own pilot and win/loss evidence.

### Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Approve/reject segment-limited sourcing pilot | Board (Dec 2026) | CFO, Head of Sales, Head of Field Service | COO | Not assigned |
| Grant span exceptions by function | COO (proposed) | Function heads, HR | Function heads | Not assigned |
| Own the churn/margin tracking dashboard during any pilot | COO (proposed) | Finance, Sales Ops | Sales Ops | Not assigned |

### Structure options

See Step 3f above (Options A, B, C). Recommended: C, segment-limited hybrid sourcing, tested properly before any scale decision.

### Spans, layers, sourcing

- **Spans:** set by work type, not a single number.
  - Field technicians (standardised, on the road): has real slack above 12 already (currently 13); candidate for modest widening once route/scheduling data confirm capacity — net effect is likely 1-2 fewer lead roles, the opposite direction from the uniform-span table above.
  - Customer service centre (standardised, high volume): already above 12 (15); candidate for modest further widening if call-volume data support it — a saving, not the +1 supervisor a flat 1:12 would force.
  - R&D (specialist, non-routine): hold near current span (5); do not widen toward 12 — specialist review and coaching load does not shrink just because a target was set.
  - Sales (key-account): hold near current span (6); do not widen toward 12 — account coaching and deal support matter more, not less, while the calibration differentiator is under any scrutiny at all.
- **Sourcing:** field calibration — keep in-house for the relationship-critical segment; test partner use only for a to-be-identified low-complexity/price-tolerant segment, with a proper test-vs-control design (the North pilot compared a treated region to other regions, not a treated segment to a control segment within the same conditions — repeat it correctly before trusting a smaller number).

### Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1. Segmentation and data pull | Segment the 3,000 customers by relationship depth, complexity and price sensitivity; pull manager salary cost by level; map today's key decision rights | COO + Finance + Sales Ops | Nov 2026 | Segment sizes and candidate low-risk pool identified; span-change cost sized in EUR |
| 2. Board decision | Present this reshaped plan; reject blanket outsourcing and uniform span; approve work-type-based span redesign and a controlled hybrid-sourcing pilot v2 | Board | Dec 2026 meeting | Decision recorded |
| 3. Span redesign, Field & CS | Widen spans where workload data support it; consolidate the resulting lead/supervisor roles through attrition/redeployment first | Heads of Field Service & Customer Service, with HR/works council | Q1 2027 | Manager FTE reduced in these two units without service-level drop |
| 4. Hybrid sourcing pilot v2 | Partner handles only the identified low-risk segment, with a true control group and monthly churn/win-rate tracking against the 7.4% breakeven | COO, Head of Field Service | Q1-Q2 2027 | Incremental churn in treated segment stays below 7.4pp for two consecutive quarters before any scale-up |
| 5. R&D and Sales spans | No uniform change; revisit only via function-specific performance review | Heads of R&D & Sales | Ongoing | N/A — explicitly out of scope for the span mandate |
| 6. Review and scale decision | Board reviews pilot v2 results against breakeven; decide whether to extend sourcing to further segments | Board | Q3 2027 | Go/no-go with real, segment-level churn data instead of a single regional pilot |

### What would change the answer

1. If the segmentation in Step 1 finds a large, genuinely low-complexity/price-tolerant customer pool (not just a small tail), a bigger slice of the EUR 1.8m could be captured safely — size that pool before judging the sourcing saving as small.
2. If manager salary data show the Field/CS span-widening saving is itself close to or above EUR 1.8m, the board's cost target may be reachable without touching sourcing at all.
3. If the pilot v2 (run with a proper control group) shows incremental churn reliably below ~7.4pp in the tested segment, scaling hybrid sourcing further becomes a net-positive move, not a rejected one.
4. If competitors already outsource calibration and customers no longer treat it as a differentiator, the capability map in Step 3a would need rechecking — nothing in the current win/loss data suggests this, but it is worth re-asking in the next interview round.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | North pilot's incremental churn (9pp) is representative of what full-scale, company-wide outsourcing would produce | 9pp base case, 4.5-18pp sensitivity range | Only controlled real-world test available (400 customers, 12 months, vs comparable-region baseline) | A segment-level re-test (Step 4, pilot v2) shows materially different churn for a defined low-risk segment |
| 2 | "Field technicians" team (14 leads × 13 reports = 182) is the same population whose cost underlies the claimed EUR 1.8m outsourcing saving | Used to sanity-check the saving (≈EUR 45k/technician/year) | Internal consistency check against the 22% partner discount; not confirmed by the board's own costing | HR/Finance confirm a different population or cost base |
| 3 | Revenue and 45% contribution margin are flat per customer regardless of segment | EUR 18,000/year, 45% margin applied uniformly | Only figures given | Segmentation shows the at-risk (relationship-critical) customers are above-average revenue/margin, which would make outsourcing even more costly than modelled |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the actual customer segmentation (relationship depth, complexity, price sensitivity) within the 3,000-customer base? | Determines whether any safe pool exists for partial outsourcing, and how large | Sales Ops / CRM data | Could turn "reject outsourcing" into "outsource segment X only," sized precisely |
| What is fully loaded manager cost by level/function? | Needed to put a EUR figure on the recommended span changes and compare against the board's EUR 1.8m target | HR/Finance | Converts the FTE deltas in Step 3d into an EUR saving comparable to the mandate |
| Does outsourcing calibration affect new-deal win rates, not just existing-customer churn? | The 62% win-rate statistic is about acquisition; the pilot only measured retention — the true cost of outsourcing may be understated | Sales Ops, future win/loss interviews in regions with any partner exposure | Could make the case against outsourcing stronger still |
| What works council/labour law constraints apply to span changes and to outsourcing calibration work currently done by employees? | Transition cost, timing and legality of both measures | Legal/HR | Could lengthen the implementation timeline in Step 5 and add one-off cost not yet modelled |
| Who currently holds pricing, sourcing-exception and span-exception authority? | Decision-rights gap identified in Step 3c | COO/HR org chart | Names an owner for Steps 2-4 of the implementation plan |

