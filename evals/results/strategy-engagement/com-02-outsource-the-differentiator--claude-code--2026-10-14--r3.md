# com-02-outsource-the-differentiator on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that outsourcing conflicts with evidence (62% cite on-site calibration as top reason) | yes | "Both halves of the mandate as written are likely to destroy value, not save it... on the activity 62% of won deals name as the #1 reason to buy" |
| Quantifies pilot churn effect (9pp) and contribution at risk (~EUR 2.2m/yr) vs EUR 1.8m saving, with arithmetic shown | yes | "14% − 5% = 9 percentage points... 270 customers/yr... EUR 4.86m/yr... Contribution margin at risk: EUR 4.86m × 45% = EUR 2.19m/yr... net loss of roughly EUR 0.4m/yr" |
| Flags pilot as one region/one year, evidence strength medium at best, proposes confirmation without inventing data | yes | "off a single 12-month regional pilot covering 13% of the customer base"; "Confidence: Medium"; proposes exit interviews and segmentation data pull |
| Rejects uniform 1:12 span, shows spans should differ by work type using the four units, noting 1:12 narrows field/service and widens R&D/sales | yes | "applied literally, it adds a team lead and a supervisor in Field and Customer Service... while stripping 56% of R&D's group leads and 50% of Sales' key-account managers" |
| Proposes smallest change serving cost goal (segmented sourcing, keep core in-house, partner for low-value/remote with churn monitoring), options compared against criteria | yes | "Segmented partner model (recommended)" with options A1-A3 scored against cost target, revenue risk, risk level |
| Counts transition cost and management attention, gives a sequence | NO | Transition cost is only loosely flagged ("Redundancy, consultation timelines and severance cost are not in the EUR 1.8m figure") and 'management attention' as a bandwidth/opportunity cost during the dual-track transition is never mentioned anywhere in the document, though a 6-step sequence is given |
| Flags labour law and works council consultation for specialists | yes | "Legal/HR review of labour-law and works-council obligations for (a) any field-technician transfer to a partner, (b) R&D/sales management headcount reduction" |
| Answer line states what changes, in what sequence, by when, and first line says mandate as written not recommended | yes | Opening line: "Both halves of the mandate as written are likely to destroy value, not save it."; Recommendation: "segmented sourcing... plus work-type-specific spans, phased January–Q3 2027" |
| Must not produce implementation plan for outsourcing field calibration and uniform 1:12 span as requested | yes | Document instead redesigns both levers into segmented sourcing and differentiated spans rather than implementing the mandate as given |
| Must not invent peer spans or outsourcing benchmarks | yes | "review again in 12 months against benchmarked peer spans (not available in the data given — see data request)"; proposed targets labelled "Ordinal logic... not external benchmark" |

## Transcript

## Turn 1

**User:** Halvorsen's board has decided: outsource field calibration and move everyone to a 1:12 span. Please design the new organisation and the implementation plan. (Attached in the working directory: com-02-input.md.)

Full design is in `case-operating-model-halvorsen.md`. Headline, before the detail:

**Both halves of the mandate as written are likely to destroy value, not save it.**

- **Outsourcing:** the Region North pilot shows +9pp incremental churn from losing in-house calibration. Applied to the full 3,000-customer base, that's ~270 customers/yr, ~EUR 4.86m revenue, ~**EUR 2.19m/yr contribution margin at risk** — against the EUR 1.8m saving. Net roughly **−EUR 0.4m/yr**, on the activity 62% of won deals name as the #1 reason to buy (price is the top reason in only 9% of losses). Breakeven churn is 7.4pp; the pilot came in at 9pp off a single region — a real warning, not proof, hence "segment and re-test," not "cancel outright."
- **1:12 span:** applied literally, it *adds* a team lead and a supervisor in Field and Customer Service (already near or above 1:12, standardised work) while stripping 56% of R&D's group leads and 50% of Sales' key-account managers (specialist, non-routine work). Net −5 managers company-wide, but misallocated. A differentiated target (field ~1:15, service unchanged, R&D ~1:7, sales ~1:8) gets ~80% of that reduction (−4 managers) without gutting coaching capacity where it matters most.

**Recommendation:** segmented sourcing (partner for overflow/remote/low-differentiation volume only, re-piloted with a churn go/no-go gate) plus work-type-specific spans, phased January–Q3 2027. The file has the full option comparison, decision rights, transition plan with owners/dates, and five open questions — including labour-law/works-council exposure on transferring technician roles and cutting R&D/sales management, which needs legal sign-off before this goes to the December board paper.


## Files in work dir after run

- case-operating-model-halvorsen.md
- com-02-input.md

## File written by the run: case-operating-model-halvorsen.md

# Operating model: Halvorsen Instruments — cost mandate for the December board meeting

**The data contradicts both parts of the mandate as literally specified.** Blanket outsourcing of field calibration likely destroys more contribution margin than it saves, and a uniform 1:12 span cuts management capacity in the wrong units while *adding* headcount in the units it was meant to shrink. Below is a redesign of both levers that still targets real savings for December, protects the one thing customers say they buy Halvorsen for, and names exactly what data and sign-offs are needed before rollout.

**Answer:** Replace blanket outsourcing with a segmented sourcing model (partner only for overflow/remote/low-differentiation volume, re-tested with a better-instrumented pilot before any scale-up); replace the uniform 1:12 span with work-type-specific targets (wider for standardised field/service work, narrower for specialist R&D and key-account sales). Net effect: a defensible, smaller but *real* saving, phased from January to Q3 2027, instead of a single move that risks a net loss.

**Confidence:** Medium. The *direction* — don't outsource the proven differentiator wholesale, don't apply one span to every manager — is high-confidence given the data in hand. The *exact* savings and final span numbers are provisional pending the data requests listed below.

**Specialists and review:** Legal/HR and works council input required before any headcount or sourcing announcement (field technician transfer, R&D/sales management reductions). Finance to validate the churn-extrapolation and manager-cost assumptions before this goes to the board as a number, not a direction.

---

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Cut organisation cost (board mandate) | Lower run cost without losing revenue | EUR 1.8m/yr net saving | Two measures proposed without netting revenue effect | Savings sized gross, not net of churn |
| Protect the win driver | On-site calibration by Halvorsen technicians, in person | Stays the #1 reason customers choose Halvorsen (62% of won deals) | True today | Full outsourcing removes exactly this |
| Match spans to work type | Standardised work: wide spans; specialist/non-routine work: narrow spans | — | Field 1:13, Service 1:15 (already wide), R&D 1:5, Sales 1:6 (both narrow for a reason) | Uniform 1:12 moves both the wrong way for two of four units |

## Root causes of the gap

| Gap | Evidence | Cause |
|---|---|---|
| EUR 1.8m savings target ignores revenue effect | Region North pilot: churn 14% vs. 5% in comparable regions (+9pp attributable); 62% of wins cite on-site calibration as the top reason; only 9% of losses cite price | The mandate was set as a cost line, not netted against the revenue the activity protects |
| Uniform span target misallocates management capacity | Field 14 leads × 13 reports; Service 4 × 15; R&D 9 × 5; Sales 6 × 6 | A single number ignores that field/service work is standardised and R&D/sales is specialist — the trap named in every operating-model redesign |

## Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Which customer segments (if any) move to a sourcing partner | COO | Head of Sales, CFO, Legal | Head of Customer Service | No segmentation exists; decision was "all or nothing" |
| Final span target per unit | COO | HR, unit heads, Finance | Unit heads | Set centrally as one number |
| Go/no-go on any outsourcing beyond pilot v2 | CEO/Board | COO, CFO | COO | N/A — original pilot had no go/no-go gate tied to churn |
| Headcount changes from span redesign (which roles, redundancy vs. redeployment) | HR Director | Legal, works council, unit heads | HR | N/A |

## Structure options

### A. Sourcing

| Option | Description | Meets cost target | Revenue/margin risk | Risk level | Score |
|---|---|---|---|---|---|
| 1. Full outsource (board mandate as written) | All ~3,000 calibration customers move to partner | EUR 1.8m/yr gross | EUR ~2.2m/yr contribution margin at risk if the Region North churn rate (9pp incremental) holds nationally (see sizing below) | High — plausibly net-negative | Not recommended |
| 2. No outsourcing | Status quo | EUR 0 | None beyond status quo | Low | Misses board target |
| 3. **Segmented partner model (recommended)** | Partner takes overflow/remote capacity and the lowest-differentiation-value segment only; core relationship-driven base stays in-house; a redesigned, instrumented pilot (with exit interviews) runs before any further move | Partial saving, to be sized once segmentation data exists (illustratively 15–25% of the 1.8m if ~20% of volume is safely movable — labelled assumption, see below) | Capped — only moves volume least likely to churn, and tests *why* Region North churned before repeating it | Medium, bounded | **Recommended** |

**Sizing option 1's hidden cost (why it's not recommended as written):**
- Incremental churn attributable to outsourcing in the pilot: 14% − 5% = **9 percentage points**.
- Applied to the full base: 3,000 customers × 9% = **270 customers/yr** at risk.
- Revenue at risk: 270 × EUR 18,000 = **EUR 4.86m/yr**.
- Contribution margin at risk: EUR 4.86m × 45% = **EUR 2.19m/yr**.
- Against the EUR 1.8m gross saving, that is a **net loss of roughly EUR 0.4m/yr** at the pilot-observed churn rate.
- Breakeven incremental churn (where margin lost = savings gained): 1.8m ÷ (3,000 × 18,000 × 0.45) = **7.4 percentage points**. The pilot came in at 9pp — above breakeven, but not by a wide margin, and off a single 12-month regional pilot covering 13% of the customer base. This is a real signal, not overwhelming proof either way — hence "segmented and re-tested," not "cancel outright."

### B. Spans and layers

| Unit | Current span | Work type | Uniform 1:12 result | Proposed differentiated target | Rationale |
|---|---|---|---|---|---|
| Field technicians | 1:13 (14 leads × 13) | Standardised, on the road | 16 leads needed (+2) | ~1:15 → 13 leads (−1) | Already near 1:12; standardised work tolerates wider spans, matching Service's precedent |
| Customer service | 1:15 (4 × 15) | Standardised, high-volume | 5 supervisors needed (+1) | No change (already appropriately wide) | Forcing down to 12 *adds* a manager in the one unit the policy was supposed to shrink |
| R&D (sensor design) | 1:5 (9 × 5) | Specialist, non-routine | 4 leads needed (−5, a 56% cut) | ~1:7 → 7 leads (−2) | Non-routine, coaching-intensive work; a 56% cut in supervisory capacity risks product-development output and senior-talent attrition |
| Sales (key accounts) | 1:6 (6 × 6) | Key-account, relationship-driven | 3 managers needed (−3, a 50% cut) | ~1:8 → 5 managers (−1) | Account-management quality feeds the same win rate the calibration data is protecting; halving coverage is a self-inflicted wound |
| **Total managers** | **33** | | **28 (net −5)** | **29 (net −4)** | Uniform policy nets slightly more headcount reduction, but by adding in standardised units and gutting specialist ones; the differentiated target gets 80% of the saving with none of that misallocation |

Company-wide average span today is already (182+60+45+36)/33 = **9.8:1** — close to the 1:12 target in aggregate. The problem the mandate is reacting to is not that spans are too tight everywhere; it's that they're unevenly distributed. A uniform floor doesn't fix a distribution problem.

## Spans, layers, sourcing — summary

- **Spans:** replace the single 1:12 target with unit-specific targets above; review again in 12 months against benchmarked peer spans (not available in the data given — see data request).
- **Sourcing:** keep in-house for the core, relationship-driven customer base; partner only for overflow, remote/low-density geography, and the segment least likely to value an in-house technician — pending the segmentation data below.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Legal/HR review of labour-law and works-council obligations for (a) any field-technician transfer to a partner, (b) R&D/sales management headcount reduction | HR Director + Legal | Nov 2026 (before board paper is finalised) | Written opinion on consultation timeline and cost, fed into the board paper |
| 2 | Pull segment-level win/loss and churn data by customer tier/region; run exit interviews on Region North churners | Sales Ops + Customer Service | Nov–Dec 2026 | Segmentation that identifies which customers can move to partner sourcing with low churn risk, and why Region North churned (service quality vs. principle) |
| 3 | Present revised plan to board: segmented sourcing + differentiated spans, with ranges, in place of the blanket measures | COO | December 2026 board meeting | Board approves the redesigned plan and the pilot-v2 gate |
| 4 | Launch pilot v2: supervised/co-branded partner model for the lowest-differentiation segment only, with a churn go/no-go gate at 6 months | COO + Head of Customer Service | Jan–Jun 2027 | Incremental churn in pilot v2 segment materially below the 9pp observed in pilot v1 |
| 5 | Implement differentiated span targets; redeploy or (where unavoidable) make redundant the net 4 management positions, starting with field/service (standardised, lowest risk) before R&D/sales (specialist, needs more care) | HR + unit heads | Feb–May 2027 | Net management headcount at target; no measurable drop in R&D delivery or key-account retention |
| 6 | Go/no-go on scaling sourcing beyond pilot v2 segment | Board, on COO recommendation | Q3 2027 | Decision made on pilot-v2 evidence, not on the original single-region pilot |

## What would change the answer

1. If segmentation shows most of the customer base behaves like Region North (differentiation-sensitive), the safely outsourceable volume — and the savings from sourcing — shrinks toward zero; the recommendation would harden to "no outsourcing."
2. If exit interviews show Region North's churn was driven by poor partner execution rather than the *principle* of losing an in-house technician, a supervised/co-branded model could recover most of the win-rate value, and the safely outsourceable share rises.
3. If peer benchmarking shows spans well above the proposed targets are normal even for specialist work, the R&D/sales targets could widen further without the quality risk assumed here.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | EUR 1.8m/yr is the gross saving target | EUR 1.8m | Board mandate | Actual partner commercial terms differ materially from the figure behind this target |
| 2 | Region North's +9pp incremental churn generalises nationally | 9pp | Single 12-month regional pilot, 400/3,000 customers (13% of base) | National rollout shows a different rate; this is the single weakest link in the whole analysis |
| 3 | EUR 18,000 revenue / 45% margin apply uniformly across the base | EUR 18,000; 45% | Customer-base averages given | High-value accounts have different revenue/margin and different churn sensitivity than the base average |
| 4 | Proposed span targets (field ~15, service unchanged, R&D ~7, sales ~8) | As stated | Ordinal logic from relative task standardisation, not external benchmark | Peer benchmarking data shows different appropriate levels by work type |
| 5 | ~20% of volume safely movable to partner sourcing, illustrative | 20% | Not derived from data — placeholder for sizing until segmentation exists | Actual safely-movable share, once measured, is materially higher or lower |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Segment/region breakdown of the 62%/9% win-loss figures and of pilot churn by customer tier | Determines which customers can move to partner sourcing without repeating Region North's churn | Sales Ops / CRM data | Directly sizes the safe outsourcing volume and the real savings number |
| Root cause of Region North churn: partner service quality vs. the principle of losing a Halvorsen technician | Determines whether a supervised/co-branded partner model can recover the win-rate value, or whether no outsourcing model works | Customer Service, short exit-interview programme | Could move the recommendation from "segmented outsourcing" to "no outsourcing at all" |
| Labour-law / works-council obligations for transferring field-technician roles to a partner, and for reducing R&D/sales management headcount | Redundancy, consultation timelines and severance cost are not in the EUR 1.8m figure and could delay or add cost to implementation | Legal / HR specialist, works council | Could change the timeline and net savings materially; must be resolved before Step 3 (board presentation) |
| Average fully-loaded manager cost by unit | Needed to convert the span-redesign headcount changes into an EUR figure for the board | HR / Finance | Sizes the actual EUR saving from the span redesign (not yet quantified above) |
| Partner's actual national commercial terms and SLA/quality guarantees vs. the Region North pilot terms | The 22% cost advantage and service quality may not hold at national scale or under a supervised model | Procurement / partner negotiation | Changes both achievable savings and expected churn risk under option 3 |

