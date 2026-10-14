# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values (difference of one acceptable if explained) | yes | Run identifies and explains 4 coded themes: 'No shared visibility... A cut-off that precedes the signal... No shortage rule... No real late-change channel' each tied to specific interviews (I1,I3,I5,I8, etc.) |
| Links symptom (waste 4.8%→9.2%, stockouts ~2→~7) to 2025 changes as main hypothesis marked for store-level testing (I8) | yes | 'the 2025 timing (centralization + cut-off change lines up exactly with when waste and stockouts both broke)' and Assumption 2: 'Causal link assumed from timing coincidence... Would change the answer if: Finance/ops data shows another driver moved at the same time,' with I8 (Finance controller) name |
| Names unowned decisions (late order changes, substitutions/allocation, sharing the plan) with explicit owners | yes | Decision rights table: 'Who may see the daily bake plan' → COO; 'Accept a late order change after 2pm' → Production planning; 'Substitution priority when a top-10 item is short' → Production planning + logistics |
| Treats culture statements (I2, I7) as opinions without examples, not basis for recommendation | yes | '*Weak evidence* — two opinions, no concrete examples; don't design the structure around this alone' and trap check: 'I2 and I7 are flagged as weak evidence and excluded from the causal story; they're listed as an open question instead' |
| Recommends process/decision-rights fixes first, keeps regional layer as option to judge later with cost/attention flagged | yes | Option A (process fix) scored 'High', Option B (4 regional managers) scored 'Low, as proposed' with cost 'High: 4 FTE, management attention for months to define the role'; Option C held for revisit 'after piloting A' |
| States what data would confirm the diagnosis (store-level waste/stockouts before/after 2025 change, timing of late changes) | NO | Only forward-looking monitoring is proposed ('Track waste and stockouts weekly by store for one quarter') and a present-day store/region breakdown question ('Does waste/stockout data break down by store or region today?') — neither asks for historical before/after-2025 store-level comparison or data |
| Answer line states what changes, in what sequence, by when | yes | 'Fix four process/decision-rights gaps first... all within 4-6 weeks and near-zero incremental headcount cost. Revisit a liaison role only if...' plus a dated transition plan (Within 2 weeks, Within 4 weeks, Within 6 weeks) |
| Does not recommend the new regional layer as the main answer | yes | 'Don't add the 4 regional managers yet' / 'Do not add the 4 regional managers now' |
| Does not invent quotes, interview counts, or figures not in the notes | yes | Uses the stated 9 interviews (I1-I9) and figures (9.2% vs 4.8%, ~7 vs ~2 stockouts) consistent with the reference figures; no fabricated direct quotes appear in the transcript |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

## Bottom line

**Don't add the 4 regional managers yet.** All 9 interviews point to the same root cause from different angles — not a missing management layer, but a broken bakery↔store process with no owner:

1. **No shared visibility** — the plan sheet lives on the planner's personal drive, not the ERP; stores are guessing (I1, I3, I5, I8).
2. **A cut-off that precedes the signal it's meant to use** — 2pm lock, but weather/demand signals land ~5pm, and the station store's numbers depend on next-day timetables (I2, I5).
3. **No shortage rule** — when a top-10 item runs short, decisions default to whoever's physically there: the driver on the ramp (I1, I6), or the night baker splitting evenly (I4).
4. **No real late-change channel** — phone calls and WhatsApp messages just get dropped because nobody has the mandate to update a locked plan (I1, I3, I4).

Finance (I8) ties the waste increase directly to #1: stores over-order "safe" because they can't see the plan. That, plus the 2025 timing (centralization + cut-off change lines up exactly with when waste and stockouts both broke), makes this a process/decision-rights problem, not a span-of-control problem. Every failure sits on the store↔bakery and store↔logistics hand-off — not the store↔HQ line a regional manager would actually occupy, unless you hand that manager explicit authority over the plan, cut-off and substitution calls, at which point you're just paying 4 salaries to do what an ERP permission and two policy decisions would do for near-zero cost.

**Recommended sequence (4-6 weeks, near-zero headcount cost):**
1. Put the plan in the ERP / shared drive — the planner is already willing, she just needs permission (I3).
2. Split the cut-off: 2pm provisional, 5-6pm final adjust — pilot on the station store first.
3. Define a substitution/priority rule owned by production planning, not the driver.
4. Replace phone/WhatsApp changes with one logged intake.
5. Track waste/stockouts weekly by store for a quarter before deciding anything about new roles.

The two interviewees who favor regional managers (I5, I9) frame it as wanting an advocate, not evidence the layer itself fixes anything — that's a symptom of the communication blackout, not an argument for new headcount.

I wrote the full analysis — root-cause table, decision-rights map, option comparison (process fix vs. regional managers vs. a narrower liaison role to revisit later), transition plan, and open questions worth checking before you commit — to `case-operating-model-brightwell.md` in the working directory.

One open question worth chasing before this goes to the CEO: does waste/stockout data break down by store or region? If problems turn out to cluster regionally for reasons beyond these four fixes, that's what would actually justify Option C (a scoped liaison role) later — not the generic layer currently on the table.


## Files in work dir after run

- case-operating-model-brightwell.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell.md

# Operating model: Brightwell Bakeries, central bakery ↔ store coordination

**Answer:** Do not add the 4 regional managers now. Fix four process/decision-rights gaps first — share the production plan, move the cut-off to match when stores actually know demand, define a shortage/substitution rule, and give late changes one real channel — all within 4-6 weeks and near-zero incremental headcount cost. Revisit a liaison role only if a defined pilot period still leaves region-specific gaps these fixes can't close.

**Confidence:** Medium-high. All 9 interviews — store managers, the planner, the night baker, logistics, finance, sales — independently point to the same mechanism (no visibility into the plan, a cut-off that precedes the store's own demand signal, no rule for shortages). That's good triangulation for a 9-interview quick case, but none of it is yet quantified by store or region, so treat the sizing below as directional.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Single central bakery, next-day ordering (set 2025) | Stores see tomorrow's bake plan | Real-time or same-day visibility | Plan sheet lives on the planner's personal drive; not in ERP (I3, I8) | No visibility — stores guess (I1, I5) |
| Accurate next-day orders | Cut-off timed to when stores know real demand | Order locked after the demand signal is known | Cut-off is 2pm; weather known ~5pm (I2); station-store commuter counts depend on next day's timetable (I5) | Cut-off precedes the information that would make the order accurate |
| Resilience to shortages | A rule for who gets priority when a top-10 item runs short | Defined, applied consistently | No rule — driver decides on the ramp (I1, I6) or night baker splits evenly (I4) | No owner, no rule |
| Waste at target | Stores order to actual need, not "safe" buffers | 5% waste | 9.2% Jan–Sep 2026, vs 4.8% in 2024 | +4.4pp, directly tied by finance to lack of plan visibility (I8) |
| Service at target | Top-10 stockouts stay low | ~2/store/week (2024 baseline) | ~7/store/week | +5/store/week, coincides with the 2025 centralization + cut-off change |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Stores can't see the plan | Plan sheet sits on one person's local drive, outside the ERP (I3, I8) | No one has told the planner she may share it — she's willing (I3) | None identified | None identified |
| Late changes get lost or can't be entered | No defined intake; changes arrive by phone (4–5pm) or WhatsApp (overnight) (I3, I4) | No one owns "accept or reject a post-cut-off change" | None identified | None identified |
| Cut-off mistimed | 2pm lock precedes the store's real demand signal (weather ~5pm, timetable for the station store) (I2, I5) | Cut-off time was set once, centrally, with no store-type variation | None identified | None identified |
| Shortages handled ad hoc | No substitution/priority protocol when a top-10 item is short (I1, I4, I6) | Decision defaults to whoever is physically present (driver on the ramp) — explicitly "not their job" (I6) | None identified | None identified |
| Waste from "safe" ordering | Follows directly from no plan visibility (I8) | — | — | — |
| "HQ doesn't listen" / "bakery people don't care" (I2, I7) | Downstream symptom of the four gaps above — stores escalate into a void because there's no shared plan or response channel | No escalation owner today | *Weak evidence* — two opinions, no concrete examples; don't design the structure around this alone | Possible, but untested — don't assume |

## Decision rights (key decisions)

| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|
| Who may see the daily bake plan | COO (one-line call) | Planner, IT/ERP owner | Planner / IT | Nobody — default is "no" |
| Accept a late order change after 2pm | Production planning | Store manager | Planner | Nobody — changes are dropped (I1) or unusable (I3, I4) |
| Substitution priority when a top-10 item is short | Production planning (pre-set rule) | Logistics | Driver / night baker apply the rule | Driver, ad hoc, on the ramp (I1, I6) |
| Cut-off time by store type | COO | Store managers, planner | Planner | Single 2pm cut-off for every store, including a station store with a materially different demand signal (I5) |

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A. Process/rights fix only (recommended) | Publish plan in ERP, split cut-off into provisional (2pm) + final adjust (5-6pm) window, set substitution rule owned by planning, define one late-change intake | Yes — closes every root cause identified in the interviews | Low: IT ticket + policy decisions, no new headcount | Low — reversible, no reporting-line change | High |
| B. Add 4 regional managers (CEO proposal), no process fix | New layer between stores and HQ to "advocate" for stores | No — doesn't touch the plan sheet, the cut-off mismatch, or the ramp substitution problem unless explicitly chartered to fix them, in which case it's option A with extra salary cost | High: 4 FTE, management attention for months to define the role | Medium — new layer can calcify today's workarounds as "how region X does it" | Low, as proposed |
| C. Regional liaison role scoped to bakery-store interface, after piloting A | A narrower role than the CEO's proposal: one person per region owns the store-side of the plan-sharing/cut-off/substitution process once it exists, and handles exceptions | Only useful once A exists; otherwise nothing to coordinate | Medium | Low if sequenced after A | Hold — revisit after a pilot quarter if region-specific gaps remain |

*Design criteria used above (impact on waste/stockout targets, cost, speed to implement, reversibility) are proposed by me for this quick case — agree them with the CEO/COO before using them to decide between B and C.*

## Spans, layers, sourcing

- Spans and layers: today, stores interact directly with the bakery/planning function and with logistics; the interviews show no evidence of a "too many stores per manager" problem. Every named failure sits on the store↔bakery and store↔logistics hand-off, not the store↔HQ line a regional manager would occupy — unless that role is explicitly given authority over the plan, cut-off and substitution decisions, in which case it only duplicates Option A with higher overhead.
- Sourcing: not applicable — production centralization is a 2025 decision already in place; this case doesn't re-litigate it, only the coordination mechanism around it.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Grant store managers and store-facing staff read access to the daily plan in the ERP (or a shared drive if ERP integration takes longer) | COO + IT | Within 2 weeks | Plan visible to all 9+ stores |
| 2 | Split the cut-off into a 2pm provisional plan and a 5-6pm final-adjust window; pilot on the station store and one other store type first | Production planning | Within 4 weeks | Station store can submit timetable-driven changes before lock |
| 3 | Set and publish a shortage/substitution priority rule; move the decision off the driver | Production planning + logistics lead | Within 4 weeks | Zero driver-decided substitutions in a 2-week sample |
| 4 | Replace phone/WhatsApp late changes with one defined intake feeding the 5-6pm window | Production planning | Within 6 weeks | All late changes logged, none silently dropped |
| 5 | Track waste and stockouts weekly by store for one quarter | Finance controller | Ongoing from step 1 | Waste trending toward 5%; stockouts trending toward ~2/store/week |
| 6 | Revisit regional/liaison role only if region-specific gaps remain after the quarter | CEO/COO | End of pilot quarter | Decision made on actual residual gap, not on today's symptom |

## What would change the answer

1. If, after steps 1-4 are running, waste and stockouts are still high in specific regions for reasons the interviews didn't surface (e.g., genuinely different regional demand patterns needing local judgment calls across many stores at once), then a scoped regional liaison (Option C) becomes justified.
2. If the planner's capacity — not information or rights — turns out to be the binding constraint (one person planning for a cut-off change, late-change intake and a substitution rule), the fix is more planning capacity, not a management layer between stores and HQ.
3. If IT confirms the plan sheet can't go into the ERP within the timeline assumed, the interim shared-drive fix should be used instead; this doesn't change the recommendation, only the mechanism.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 9 interviews are representative of the store network, not a self-selected complaining subset | Treated as representative | No store-by-store data provided | A quantitative breakdown shows the vocal stores are outliers |
| 2 | Waste and stockout increases are driven mainly by the 2025 centralization + cut-off change, not by an unrelated factor (e.g., a demand shift, a recipe change) | Causal link assumed from timing coincidence | Both metrics moved after both 2025 changes; no other change mentioned | Finance/ops data shows another driver moved at the same time |
| 3 | IT/ERP can host the plan sheet or a shared-access version within ~2-4 weeks | Used in transition plan dates | Not confirmed; not in the interviews | IT says this needs a longer system project — use a shared drive as the interim fix instead |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Does waste/stockout data break down by store or region today? | Would confirm or kill the "this is uniform, not regional" read that rules out regional managers | Finance controller (I8) | If problems cluster by region for reasons distinct from the four process gaps, Option C gets stronger |
| What is the planner's current workload/capacity? | If she's already at capacity, a cut-off/intake redesign needs more planning headcount, which changes the transition cost | Production planning lead | Could add a small headcount line to Option A, still far cheaper than 4 regional managers |
| Is the plan sheet technically ready for ERP integration, or does it need rebuilding first? | Sets a realistic date for step 1 | IT / production planner | Could push step 1 timeline out; doesn't change the sequencing logic |
| Are "HQ never listens" (I7) and "bakery people don't care" (I2) backed by specific incidents beyond what's in these notes? | These are currently weak evidence (opinion, not example) per the trap check; worth confirming before citing as a culture problem | Follow-up interviews with I2, I7 | If substantiated with examples, add a culture/incentives workstream alongside Option A |

---

## Note on method

This is a quick-case read of the operating-model playbook, run in one pass on the interview notes and figures you gave me — I did not ask further sharpening questions because the decision question, the symptom (waste, stockouts), the proposed structure (4 regional managers), and the data in hand were all already specified. The trap checks below are answered against that read.

**Trap checks**
- Broken processes fixed before structure change — yes, recommendation sequences process/rights fixes first and holds the structure decision.
- Design starts from what the strategy requires, not the org chart — yes, built from the capability gaps, not from the proposed layer.
- Spans differ by type of work — flagged: a single 2pm cut-off for every store ignores that a station store's demand signal is structurally different; recommendation splits the cut-off window and pilots by store type rather than applying one rule to all.
- Decision rights for the key decisions are explicit — yes, four decisions named with an owner each.
- Centralisation proposed only where standardized — the production centralization itself isn't re-litigated here (out of scope); cut-off timing is explicitly *not* standardized further, it's tailored by store type.
- No activity customers choose Brightwell for is outsourced — not applicable, no sourcing change proposed.
- Transition cost and management attention counted against the benefit — yes: Option A is IT-ticket-plus-policy cost; Option B (4 FTEs plus months defining the role) is costed against it explicitly and loses on that basis alone, independent of whether it would even fix anything.
- Culture claims rest on examples, not opinions — I2 and I7 are flagged as weak evidence and excluded from the causal story; they're listed as an open question instead.

