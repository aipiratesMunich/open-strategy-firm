# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values | yes | Identifies 3 corroborated causes (plan visibility I3/I8, cut-off timing I2/I5/I9, shortage priority I1/I4/I6) with accurate per-interview citations matching the source notes exactly; no interview count or figure mismatches found. |
| Links symptom to 2025 changes as main hypothesis, marked as hypothesis to test with I8 store-level data | yes | Assumption 1 explicitly frames the 2025-timing causal link as an assumption with a 'would change the answer if' falsifier, and the open-questions table ties waste confirmation to 'Finance controller (I8 already offered to share store-level numbers)'. |
| Names unowned decisions and proposes explicit owners | yes | Decision rights table assigns explicit owners for plan visibility (COO/planner), cut-off timing (COO/production planning), shortage priority (production planner), and late demand changes (production planner). |
| Treats culture statements (I2, I7) as opinions without examples and does not base recommendation on them | NO | Only I7 ('HQ never listens') is explicitly flagged as 'a single, unspecific opinion ... Flagged as weak evidence.' I2's own culture remark ('honestly the bakery people dont care about us') is never mentioned or treated as opinion anywhere in the document — I2 is cited only for the weather-timing fac |
| Recommends process/decision-rights fixes first, keeps regional layer as option to judge after, with cost/attention flagged | yes | Option A (process fixes) is recommended; Option B (CEO's regional-manager proposal) is costed as 'Material (4 salaries + management attention)' and Option C defers any coordination-role decision to after re-measurement at week 12. |
| States what data would confirm the diagnosis (store-level waste and stockouts before/after 2025, timing of late changes) | NO | Open questions request store-level waste breakdown via I8 ('Can waste be broken down by store...') but nowhere ask for store-level stockout data before/after 2025 or the timing distribution of late order changes — only post-fix 'late-change volume drops' is mentioned as a future success measure, not |
| Answer line states what changes, in what sequence, by when | yes | 'Sequence: weeks 1–2 open plan visibility and set a substitution rule; weeks 2–6 redesign the cut-off; week 12 re-measure before deciding anything about new roles.' |
| Must not recommend the new regional layer as the main answer | yes | Answer states: 'Fix three process and decision-rights breaks ... before adding any management layer,' explicitly deprioritizing the regional-manager idea as Option B scored 'Low'. |
| Must not invent quotes, interview counts, or figures not in the notes | yes | All figures (4.8%→9.2%, ~2→~7 stockouts, 2pm cut-off, 9 interviews, 4 regional managers, I8's offer to share store-level numbers) match com-03-input.md exactly with no fabricated additions. |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

Written to `case-operating-model-brightwell-bakeries.md`.

**Bottom line:** the waste and stockout trend both start exactly when the 2025 changes hit, and nine interviews converge on three concrete, fixable breaks — not a missing layer:

1. **No one can see the production plan** (it's on the planner's personal drive, not shared) — finance directly ties this to stores over-ordering "safe," which is the biggest waste driver (I3, I8).
2. **The 2pm cut-off is set before the information that drives next-day demand exists** — weather (known ~5pm) and train timetables for the station store (I2, I5), and it's the #1 complaint across the store network (I9).
3. **No rule for who gets priority when an item runs short** — drivers improvise on the ramp, confirmed independently by the store manager, the baker, and logistics itself (I1, I4, I6).

Each of those has 2–3 independent corroborating sources. The regional-manager idea rests on two people (I5, I9) proposing a structural fix to a process problem they feel but didn't diagnose — and none of the four decisions actually breaking today (plan visibility, cut-off timing, shortage priority, late-change handling) would land on a regional manager's desk unless explicitly redesigned to. The one soft finding — "HQ never listens" (I7) — is a single unspecific opinion, flagged as weak evidence rather than a real cause.

**Recommendation:** fix the three process/decision-rights breaks over the next ~6 weeks (cheap, reversible, testable), re-measure waste and stockouts at week 12, and only then revisit whether any coordination role is still needed — scoped to whatever's actually still unresolved, not a blanket 4-person layer.


## Files in work dir after run

- case-operating-model-brightwell-bakeries.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell-bakeries.md

# Operating model: Brightwell Bakeries, why don't the central bakery and stores coordinate, and would 4 regional managers fix it?

**Answer:** Fix three process and decision-rights breaks that date to the 2025 centralisation — (1) the 2pm order cut-off, (2) the invisible production plan, (3) the unowned shortage/substitution call — before adding any management layer. These explain the waste and stockout trend on their own; regional managers would not touch any of them. Sequence: weeks 1–2 open plan visibility and set a substitution rule; weeks 2–6 redesign the cut-off; week 12 re-measure before deciding anything about new roles.

**Confidence:** medium. Nine interviews triangulate well (each of the three causes below is corroborated by 2–3 independent roles — store, planner, baker, logistics, finance), and the direction matches the 2025 timing of the KPI shift. What's missing is a quantified split of the waste between "over-ordering safe" and other causes, and a clean before/after test of any fix.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Keep waste at target while running one central bakery | Stores order close to real demand | Waste ≤5% of production value | 9.2% (Jan–Sep 2026), up from 4.8% in 2024 | Large, worsening since centralisation |
| Keep shelves stocked on top-10 items | Production plan matches next-day demand; shortages allocated predictably | Stockouts near 2024 level | ~7/store/week, up from ~2 | Large, worsening since cut-off moved to 2pm |

The target (5% waste) and the "normal" stockout level (~2/week) were both roughly met before the 2025 changes. That dates the problem to the centralisation and cut-off change, not to a layer that was always missing.

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Waste up 4.8%→9.2% | Production plan kept on planner's personal drive, not in ERP or shared with stores (I3, I8) → stores order "safe" without visibility into what's actually being baked (I8, finance controller, ties this directly to the waste line) | No one has authorised the planner to share the plan — a one-line decision, not a design problem (I3) | None found | None found |
| Stockouts up 2→7/week | 2pm cut-off falls before the information that drives next-day demand is known: weather (known ~5pm, I2) and next-day train timetable for the station store (I5) — corroborated by area sales as the #1 complaint across stores (I9) | No rule for who gets priority when an item (e.g. rye) runs short — logistics lead confirms substitution is improvised on the ramp and "not their job" (I6); night baker confirms he "just splits it" with no guidance (I4); store manager confirms the driver ends up deciding (I1) | None found | "HQ never listens" (I7) is a single, unspecific opinion with no concrete example — likely a symptom of the two causes above (orders silently dropped after 2pm, no visibility into the plan) rather than an independent culture problem. Flagged as weak evidence. |

Both root causes are corroborated by 2–3 independent sources across different roles (store manager, planner, baker, logistics, finance) — that's a materially stronger basis than the "add a layer" proposal, which rests on two people (I5, I9) proposing a structural fix to a process problem they experience but didn't diagnose.

## Decision rights (key decisions)

| Decision | Decides today | Should decide | Consulted | Executes |
|---|---|---|---|---|
| Who sees the production plan | No one (planner holds it informally) | COO authorises; planner publishes in ERP daily | Finance (waste data), store managers | Production planner |
| Where the order cut-off sits | Set in 2025, owner unclear from interviews | COO / production planning, based on when demand-driving information actually arrives | Store managers (what information arrives when), production planner (how late a plan can move) | Production planner |
| Who gets priority when an item runs short | Driver, ad hoc, on the ramp (I1, I6) | Production planner, against a pre-agreed rule (e.g. top-10 items first, or by store volume) | Logistics lead | Head baker (bakes to the rule), driver (delivers per the rule, no longer decides it) |
| Late demand changes (post-cut-off phone calls, WhatsApp) | Absorbed informally by planner/baker, not systematised (I3, I4) | Define explicitly: either folded into a later cut-off, or a formal small-adjustment window | Store managers, logistics | Production planner |

None of these four decisions has anything to do with a regional layer — they're either unassigned (plan visibility, shortage priority) or assigned at the wrong moment (cut-off timing). A regional manager sitting between stores and HQ wouldn't acquire ownership of the plan sheet, the cut-off, or the shortage rule unless explicitly given it — and if that's the design, it's simpler to give those decisions to the planner and logistics lead directly, who already touch them daily.

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A. Fix process + decision rights, no new layer (recommended) | Publish plan in ERP; move/redesign cut-off to match real information timing; set a shortage-priority rule; formalise the late-change channel | Yes — addresses both root causes directly, confirmed by 5+ independent interviews | Low (mostly policy + one ERP share, no headcount) | Low — reversible, testable in weeks | High |
| B. CEO's proposal: 4 regional managers, process unchanged | Insert a regional layer between stores and HQ, leave cut-off/visibility/shortage rule as is | No — none of the interviews trace waste or stockouts to a missing layer; regional managers would advocate for stores but couldn't fix a plan that isn't in any shared system | Material (4 salaries + management attention) | High — adds a layer to an already-strained process, risk of new hand-offs and slower decisions (classic reorg trap) | Low |
| C. Fix process first, revisit a lighter coordination role later if needed | Run Option A for ~12 weeks; if store-HQ friction persists after visibility and timing are fixed (e.g., genuine cross-store prioritisation conflicts emerge), consider a narrower role — not 4 regional managers, but whoever actually needs to own the one decision still unresolved | Conditional — only relevant if Option A doesn't close the gap | Deferred | Low — decision made with evidence instead of guesswork | Fallback if A under-delivers |

## Spans, layers, sourcing

- No evidence from the interviews points to a span-of-control or layer problem today (store managers report direct frustration with HQ processes, not with managing too many people or too few). Adding 4 regional managers without a process case would be adding a layer the diagnosis doesn't support.
- Sourcing is not in question here — production is already centralised; the issue is how that centre and the stores exchange information, not who performs the baking.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | COO authorises planner to publish the daily plan; plan sheet moved into ERP (or a shared read-only view if full ERP integration takes longer) | COO + production planner | Within 2 weeks | Stores can see tomorrow's plan before ordering |
| 2 | Set and communicate a shortage/substitution priority rule (e.g., top-10 items get priority, or a fixed store ranking) | Production planner + logistics lead | Within 2 weeks | Drivers stop improvising; baker bakes to a rule, not a guess |
| 3 | Redesign the cut-off: move it later and/or split into a provisional order (early) + small adjustment window (afternoon/evening) matched to when weather and timetable data land | COO + production planner, with store manager input on actual information timing | Pilot within 6 weeks | Late-change volume drops; stockouts trend back toward ~2–3/store/week |
| 4 | Replace informal phone/WhatsApp changes with one defined channel feeding the planner's system | Ops / IT | Within 6 weeks | No late changes lost; no silent drops |
| 5 | Re-measure waste % and stockouts/store/week | COO | Week 12 | Waste trending toward 5%; stockouts trending toward ~2/week |
| 6 | Only then: revisit whether any coordination role is still missing, based on what's left unresolved | COO | Week 12+ | Decision backed by post-fix data, not pre-fix guesswork |

## What would change the answer

1. If waste and stockouts don't improve materially after steps 1–4 (by week 12), the cause is deeper than cut-off timing and visibility, and a structural fix — including a coordination layer — becomes a live option again, scoped to whatever decision is still unresolved.
2. If the finance controller's link between "safe ordering" and waste (I8) turns out to be a minority of the waste, not the majority, when broken down by store, other causes (e.g., production-side overbaking, expiry handling) need their own branch.
3. If store managers need genuine advocacy on matters beyond the plan/cut-off/shortage rule (pricing, assortment, local promotions), that is a different, legitimate case for a regional or area role — but it should be scoped to that gap specifically, not sold as the fix for waste and stockouts.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 2025 timing (centralisation + cut-off change) is the main driver of the KPI shift, not a coincident unrelated cause | Causal link assumed from timing | COO's framing + interview content all point at post-2025 process | A separate cause (e.g., a supplier change, a demand shock) is identified independently |
| 2 | "Safe ordering" (I8) is driven by lack of plan visibility, not by store managers simply preferring to over-order regardless | Visibility is the lever | I3 and I8 both point here independently | Store-level data shows waste unrelated to visibility (e.g., uniform across stores regardless of whether they already escalate informally) |
| 3 | Publishing the plan in ERP is feasible at reasonable cost within weeks | Low cost, low transition risk | Not verified — IT capacity unknown | ERP change requires a multi-month project; a manual shared-sheet interim is the fallback already noted in the transition plan |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why was the cut-off moved to 2pm in 2025 — what capacity constraint drove it? | A later cut-off is only viable if production can still run with less lead time | Production planner / COO | Determines how late the redesigned cut-off (step 3) can realistically move |
| What does ERP integration of the plan sheet actually cost and take? | Decides whether step 1 is a two-week fix or needs a manual interim | IT / production planner | If costly, swap in a shared spreadsheet/report as the near-term fix |
| Can waste be broken down by store and matched against which stores already have informal visibility (e.g., via personal contact with the planner)? | Would directly test whether visibility, not culture, explains the waste gap | Finance controller (I8 already offered to share store-level numbers) | Strengthens or weakens the central causal claim before committing budget |
| Is there a decision beyond plan/cut-off/shortage-rule that stores genuinely need an advocate for? | Separates "stores feel unheard because the process is broken" from "stores have a real unmet escalation need" | Store managers, area sales | Determines whether Option C's narrower role is ever justified |


