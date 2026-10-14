# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values (off-by-one tolerated if explained) | NO | Bottom line claims cutoff-timing was 'Raised independently by 4 of 9 interviewees (two store managers of different types + area sales)' — that phrase names only 3 people (two store managers + area sales), yet asserts 4, an uncorrected internal count mismatch rather than an explained coding choice. |
| Links the waste/stockout symptom to the 2025 changes as the main hypothesis, flagged as needing store-level data from I8 | yes | Confidence section: 'Low-medium confidence on sizing the fix... store-level waste breakdown are not yet in hand (see Open questions)'; open question: 'Store-level waste and stockout breakdown (I8 offered to share this) ... Strengthens or weakens the causal link'. |
| Names the unowned decisions (late changes, substitutions/allocation, plan sharing) and proposes explicit owners | yes | Decision-rights table lists all three gaps as 'no owner,' and the recommendation assigns 'the production planner (or logistics lead) explicit, standing authority over late-change handling and shortage-priority rules' and puts the plan 'in the ERP, visible to stores'. |
| Treats culture statements (I2, I7) as opinions without examples, not a basis for the recommendation | NO | I7 is correctly downgraded ('single respondent... kept out of the recommendation'), but I2 is instead used as corroborating hard evidence for the cutoff-timing root cause ('I2, I5 ... Confirmed'), not flagged as an unsubstantiated opinion. |
| Recommends process/decision-rights fixes first and keeps the regional-manager layer as a later option with cost/attention flagged | yes | 'Recommended: Option C... Fix B now; revisit a regional layer later only if a residual gap remains'; Option A flagged '~4 FTE + overhead (ASSUMPTION: salary band and reports not in hand)'. |
| States what data would confirm the diagnosis (store-level waste/stockouts before vs after 2025, timing of late changes) | NO | Open questions only request a cross-sectional 'store-level waste and stockout breakdown' to see concentration by store; no request for a before/after-2025 comparison or for data on the timing distribution of late changes. |
| Answer line states what changes, in what sequence, by when | yes | 'Fix the process, the data-sharing rule and the two missing decision rights first (4–8 weeks, near-zero headcount cost); only revisit a regional layer if a coordination gap remains once that's done.' |
| Does not recommend the new regional layer as the main answer | yes | 'Don't add the regional-manager layer yet' is the stated answer, with Option C (process fixes first) recommended. |
| Does not invent quotes, interview counts, or figures not in the notes | yes | No internally contradicted fabricated figures found beyond the counting slip already flagged in criterion 1; quotes are consistently attributed to numbered interviewees (I1–I9) matching the stated 9-interview set. |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

## Bottom line

The interviews don't support the CEO's diagnosis. **None of the four root causes that come up repeatedly across functions is a reporting-line problem:**

1. **Cutoff timing is wrong** — 2pm is *before* stores know tomorrow's real demand (weather, train timetable). Raised independently by 4 of 9 interviewees (two store managers of different types + area sales).
2. **The production plan isn't shared** — it lives on the planner's personal drive, not the ERP, and stores can't see it. The finance controller ties this directly to where waste concentrates ("safe" over-ordering). Corroborated by 4 interviewees across 3 different functions.
3. **No one owns the shortage/substitution decision** — it defaults to whoever's standing there (the delivery driver on the ramp, the baker splitting evenly). Corroborated by a store manager, the baker, and the logistics lead — three independent functions.
4. **Late changes have no real channel** — some get silently dropped, others get patched in informally overnight by WhatsApp, so store and bakery disagree about what's even possible.

The two comments that sound like support for regional managers (I5: "a regional manager could fight for us," I9: "stores feel alone") describe a felt lack of advocacy — not a decision that's structurally blocked today. And the one "HQ never listens" comment (I7) is a single respondent's opinion, not corroborated evidence of a separate root cause.

**Recommendation:** fix the process first — move/split the cutoff to follow the real demand signal, put the plan in the ERP so stores can see it, and explicitly assign the two orphaned decisions (late-change handling, shortage priority) to an existing role like the production planner or logistics lead. This is weeks, not months, and near-zero headcount cost. Only reconsider the regional-manager layer afterward, if a genuine coordination gap remains — adding a management layer on top of broken processes typically just renames the problem.

I wrote the full analysis (issue tree, decision-rights map, option comparison, trap checks, assumptions, and open questions — including a few things I'd want from you before locking this in, like the store-level waste breakdown finance offered to share) to `case-operating-model-brightwell-bakeries.md` in the working directory.


## Files in work dir after run

- case-operating-model-brightwell-bakeries.md
- com-03-input.md

## File written by the run: case-operating-model-brightwell-bakeries.md

# Operating model: Brightwell Bakeries, why central bakery and stores don't coordinate, and whether a regional-manager layer fixes it

**Answer:** Don't add the regional-manager layer yet. The interviews point to four fixable root causes — a cutoff time that is earlier than the real demand signal, a production plan nobody is authorised to share, no owner for shortage/substitution decisions, and an informal channel (phone/WhatsApp) for late changes that bypasses the plan entirely. None of these is a reporting-line problem. Fix the process, the data-sharing rule and the two missing decision rights first (4–8 weeks, near-zero headcount cost); only revisit a regional layer if a coordination gap remains once that's done.

**Confidence:** medium-high the diagnosis is right (four of nine interviews independently corroborate the plan-visibility gap, four independently corroborate the cutoff-timing gap, three independently corroborate the no-owner substitution gap — three different functions each time). Low-medium confidence on sizing the fix, because spans/layers data, the ERP cost, and a store-level waste breakdown are not yet in hand (see Open questions).

## Step 1: Sharpened question

As given: "Which decisions and data flows does the 2025 centralised-bakery, 2pm-cutoff model require that today's process cannot deliver, and what is the smallest change that closes the waste gap (9.2% vs 5% target) and the stockout gap (~7 vs ~2 per store per week) — with or without a new regional-manager layer?"

Already proposed structure: 4 regional managers between stores and HQ, proposed by the CEO.
What's fixed/not in scope here: the central-bakery model itself (not questioned in any interview); only the coordination layer and surrounding process are in scope.

## Step 2: Issue tree — hypotheses and status

| Branch | Hypothesis | Evidence | Status |
|---|---|---|---|
| Process/timing | The 2pm cutoff is earlier than the point stores have reliable demand information (weather, train timetables), so orders are built on stale information | I2, I5 (independently, two store types), I9 (area sales, "biggest complaint I hear") | **Confirmed** |
| Data/systems | Stores can't see the production plan, so they over-order "safe", which is where most waste sits | I3 (planner, plan "on my drive," would share "if someone said I may"), I8 (finance controller — waste concentrated in stores ordering safe; plan not in ERP), I1, I5 | **Confirmed** |
| Decision rights | No one owns the substitution/shortage-priority decision; it defaults ad hoc to whoever is physically present | I1 ("driver decides what we get"), I4 (baker "just splits it," no priority rule given), I6 (logistics lead: "drivers decide... not their job really") | **Confirmed** |
| Process/channel | Late changes (4–6pm) have no formal path into the plan; they're either dropped (store side) or patched in informally overnight (bakery side), so the two sides disagree about what's even possible | I1 ("orders after 2pm just get dropped"), I3 (locked at 2, can't amend), I4 (late WhatsApp changes do get baked, inconsistently) | **Confirmed** |
| Structure | The store-to-HQ reporting line itself (no regional layer) is what blocks a fix | I5, I9 want a regional manager to "fight for" stores / reduce feeling "alone" | **Killed as root cause** — both quotes describe a felt lack of advocacy, not a decision that is structurally impossible today. Nothing in I1–I8 names an escalation failure that a management layer, rather than a process fix, would resolve. |
| Culture | "HQ doesn't listen" is a standalone root cause | I7 (single respondent), echoed loosely by I9 | **Weak evidence, not a root cause** — one direct respondent (I7); best read as the perception that follows from the four confirmed causes above (plan hidden, cutoff ignores real signals, no one owns shortages), not an independent driver. Should resolve as a side effect once those are fixed; not worth a structural fix on its own ([weak evidence](#)). |

## Step 3: Deciding analyses

**a. Process diagnostics — end to end**

Store demand signal (known ~4–6pm) → order (due 2pm, i.e. before the signal exists) → plan locked at 2pm on planner's personal spreadsheet (not shared, not in ERP) → night bake follows the sheet; late WhatsApp exceptions patched in inconsistently → on shortage, driver picks the substitution at the ramp, baker splits short items with no priority rule.

Three failure points, none of them an org-chart problem:
1. The cutoff is sequenced *before* the information it should be based on exists (I2, I5).
2. The plan is a private file, not a shared system of record (I3, I8) — this is the direct mechanism I8 ties to waste: stores that can't see the plan over-order "safe."
3. Two decisions — late-change handling and shortage substitution — have no assigned owner, so they default to whoever is physically closest (planner drops them, driver improvises, baker splits evenly).

**b. Decision-rights review**

| Decision | Should decide | Today |
|---|---|---|
| Where to set the order cutoff | Ops/HQ, informed by what time stores actually have reliable demand data | Set to 2pm in 2025 without that input (I2, I5, I9 all flag the mismatch) |
| Who sees the production plan | Should be store managers + finance, by default | No one — planner holds it personally, unauthorised to share (I3) |
| How to handle a change after cutoff | Needs one rule, one channel | Two uncoordinated paths: dropped silently (I1) or patched informally overnight (I4) |
| Who gets priority when an item is short | Needs an explicit rule (tiering, pre-commitments, rotation) | No one — driver improvises on the ramp (I1, I6), baker splits evenly by default (I4) |

Every row has a gap, and every gap is "no owner," not "too many owners" or "too many layers." A regional-manager layer does not by itself fill any of these four rows unless the CEO explicitly assigns them there — and if that's the intent, it's worth asking whether an existing role (production planner, logistics lead) could own them for a fraction of the cost.

**c. Structure / option comparison**

Design criteria (proposed — confirm with CEO/COO before final scoring): closes the waste and stockout gap, cost, speed to impact, disruption.

| Option | Description | Closes root causes found | Cost | Speed | Transition risk |
|---|---|---|---|---|---|
| A — CEO's proposal: 4 regional managers | New layer between stores and HQ | Not directly — none of the 4 confirmed causes is a reporting-line gap. Could help only if managers are explicitly handed the cutoff-review, plan-sharing and shortage-priority decisions, which is a scope decision, not a structural one | ~4 FTE + overhead (ASSUMPTION: salary band and reports not in hand — data request below) | Slow: hiring, onboarding, months before they're effective | Medium-high: adds a hand-off; risks becoming a complaint-absorption layer that papers over, rather than fixes, the four gaps (classic "reorganising before fixing process" trap) |
| B — Fix process, data and decision rights, no new layer | (1) Move or split the cutoff so it follows the real demand signal; (2) put the plan in the ERP, visible to stores in real time; (3) give the production planner (or logistics lead) explicit, standing authority over late-change handling and shortage-priority rules; (4) retire the WhatsApp/phone side-channel once there's a real one | Directly addresses all 4 confirmed causes | Low — mostly policy decisions + an ERP/sheet integration (ASSUMPTION: integration cost not sized — data request below) | Fast: 4–8 weeks for the policy and ownership changes; ERP integration may lag | Low — no new reporting lines, existing roles get clearer mandates |
| C — Do B now; revisit a regional layer later only if a residual gap remains | e.g., cross-store trade-offs too complex for a shared system, or a genuine need for a regional voice in planning trade-offs | Same as B, plus a checkpoint | Low now, optional cost later | Fast now | Lowest — avoids sunk cost in a layer that turns out unnecessary |

**Recommended: Option C.** The smallest change that closes the gap wins; B is forced regardless of what you ultimately decide about regional managers, because none of the four confirmed causes is solved by A alone.

**d. Spans and layers** — not assessed quantitatively; current managers-per-store and reporting spans weren't in the interview set. Flagging as a data request rather than guessing.

**e. Sourcing** — not applicable; no outsourcing question here.

**g. Alignment check** — Option B asks store managers and the planner to adopt a shared system and a published rule instead of personal judgment calls; a real but modest change in working habits, no change in authority. Option A changes authority lines company-wide, which is a bigger sell and, per I7's "HQ never listens," risks being read as HQ adding bureaucracy rather than fixing the complaint — unless A is paired with B and scoped explicitly to the four decision rights above.

## Step 4: Trap checks

- [x] Broken processes and data are fixed or scheduled before any structure change — Option C sequences B before reconsidering A.
- [x] The design starts from what the gap requires (waste, stockouts), not from the org chart the CEO proposed.
- [ ] Spans differ by type of work — not assessed; no spans/layers data in hand.
- [x] Decision rights for the key decisions (cutoff timing, plan visibility, late changes, shortage priority) are made explicit in the recommendation.
- [x] No centralisation proposed beyond what's already done; the plan-visibility fix is "share," not "centralise further."
- [x] N/A — no outsourcing in scope.
- [ ] Transition cost of Option A not counted (flagged as an assumption/data request, not fabricated).
- [x] The culture claim (I7, "HQ never listens") is treated as one respondent's opinion, not evidence of a root cause, and kept out of the recommendation.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | 4 regional managers would cost materially more than reassigning 2–3 decision rights to existing roles | Qualitative only, not costed | Not given in interviews or briefing | A credible cost/benefit for Option A was produced showing it's cheap relative to B |
| 2 | ERP integration of the plan sheet is a bounded, near-term IT task | Assumed feasible in weeks, not months | I8 says the gap is simply "not in the ERP"; no IT estimate given | IT confirms it needs a longer platform project |
| 3 | The four confirmed causes, not store-manager skill or culture, explain most of the waste/stockout increase | Treated as the primary drivers | Triangulated across 3–4 independent interview sources each | A store-level data cut (data request below) shows the increase concentrated in causes not covered by I1–I9 |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| By when does the CEO/COO want the waste and stockout gap closed? | No date was given; sequencing and urgency of Option B vs A depend on it | COO | Sets the timeline in the transition plan |
| Store-level waste and stockout breakdown (I8 offered to share this) | Confirms whether waste/stockouts concentrate in stores with the worst plan-visibility and cutoff-mismatch problems, or elsewhere | Finance controller (I8) | Strengthens or weakens the causal link behind Option B; could surface a fifth cause not in the interviews |
| Current spans and layers (how many stores per manager today, how many layers store-to-CEO) | Needed to assess whether 4 regional managers is even sized right, if Option A is pursued later | HQ/COO | Enables a real spans-and-layers analysis instead of a qualitative one |
| Cost and timeline to add the plan sheet to the ERP | Decides how fast Option B's data fix can actually land | IT/ops | Could shift Option B's "fast" rating if integration turns out to be a multi-month platform project |
| Why was the cutoff moved to 2pm in 2025 — was there a production-capacity constraint behind it? | If 2pm is driven by a real baking-capacity limit, the fix may be a two-stage order (indicative + late adjustment window) rather than simply moving the cutoff later | COO/production | Changes which specific process fix is recommended inside Option B |

## What would change the answer

1. If the store-level data (I8) shows waste/stockouts are *not* concentrated in stores with the worst plan-visibility or cutoff problems, the four confirmed causes explain less than assumed, and a fifth cause (e.g., SKU mix, delivery routing) needs its own branch.
2. If spans-and-layers data shows today's store managers already have no functioning escalation path to HQ at all (not just "feel unheard"), the case for *some* additional coordination role gets stronger — though it still wouldn't need to be the full 4-manager layer the CEO proposed, and the decision-rights fixes in Option B would still be needed regardless.
3. If IT confirms the ERP plan-sharing fix is a multi-month project, Option B's "fast, low-cost" rating drops and a lighter interim fix (e.g., emailing/printing the daily plan to stores) should be sequenced first.

