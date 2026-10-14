# com-03-interview-notes on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Counts the themes in line with reference values (difference of one acceptable if explained) | yes | "Seven of nine interviews independently trace back to the same three gaps" — cites I1–I6, I8 as independent evidence, treats I7/I9 as downstream culture complaints; a defensible ~7-8 tally with some explanation given. |
| Links the waste/stockout symptom to the 2025 changes as main hypothesis, marked as a hypothesis to test with store-level data offered by I8 | NO | I8's notes state "can share the store-level numbers," but the run never surfaces this offer — Open Questions asks for 'store count and planner's current daily order-handling load' and 'cost and timeline of the 4-regional-manager proposal,' not I8's offered store-level waste/stockout breakdown. |
| Names the unowned decisions (late order changes after cut-off, substitutions/allocation when short, sharing the plan) and proposes explicit owners | yes | Decision rights table lists 'Order cutoff time/policy,' 'Production-plan visibility,' 'Late-change intake,' and 'Shortage/substitution allocation' each with a 'Should decide' owner (e.g., 'Planner, via a pre-agreed priority rule'). |
| Treats culture statements (I2, I7) as opinions without examples and does not base recommendation on them | NO | I7's "HQ never listens" is explicitly flagged as "opinion without example," but I2's parallel culture claim ("honestly the bakery people dont care about us") is never mentioned or flagged anywhere in the output — I2 is cited only for the weather-timing fact. |
| Recommends process/decision-rights fixes first and keeps regional manager layer as a later option with cost/attention flagged | yes | "Do not add the 4 regional managers now... Revisit a coordination role only after the fixes are in place"; Option A row flags "Not sized by CEO — 4 FTEs + management overhead (flag: get a number)". |
| States what data would confirm the diagnosis (store-level waste/stockouts before/after 2025 change, timing of late changes) | NO | Open Questions list covers span of control, regional-manager cost/timeline, store count/planner load, and target date — none asks for store-level waste/stockout data before vs. after the 2025 change or the timing distribution of late changes. |
| Answer line states what changes, in what sequence, by when | yes | "Fix the order-cutoff timing, production-plan visibility, and shortage-allocation rule first (weeks, near-zero cost)... Revisit a coordination role only after the fixes are in place" plus a staged transition plan with Weeks 1–2, 2–4, Week 8 milestones. |
| Must not recommend the new regional layer as the main answer | yes | "Don't add the 4 regional managers yet — the interviews don't point to a structure problem." |
| Must not invent quotes, interview counts, or figures not in the notes | yes | Quotes ("I'd share it if someone said I may", "orders after 2pm just get dropped") and figures (4.8%→9.2%, ~2→~7, target 5%) match the source notes exactly; no fabricated interview content found. |

## Transcript

## Turn 1

**User:** These are my notes from 9 interviews about why our central bakery and stores don't work together. CEO wants regional managers. Make sense of it and tell me what we should change. (Attached in the working directory: com-03-input.md.)

Saved the full analysis to `brightwell-root-cause-recommendation.md`. Here's the bottom line:

**Don't add the 4 regional managers yet — the interviews don't point to a structure problem.** Seven of nine interviews independently trace back to the same three gaps, all process/decision-rights, not layers:

1. **Cutoff timing is wrong, not just early.** The 2pm lock precedes the signals that actually drive next-day demand — weather (I2) and station timetables (I5). Stores are guessing.
2. **No plan visibility.** The production plan sits on the planner's personal drive, not the ERP — and the planner won't share it without someone explicitly authorizing it (I3: "I'd share it if someone said I may"). Starved of visibility, stores over-order "safe," which is what's driving waste up (I8 ties this directly).
3. **No shortage-allocation rule.** When an item runs short, nobody owns the call — it defaults to delivery drivers improvising on the ramp (I6, acknowledged as "not their job") or the night baker splitting arbitrarily (I4). That's a big piece of the stockout jump.

The "HQ never listens" complaint (I7, I5, I9) reads as a downstream symptom of these three gaps, not independent evidence for a missing layer — it's the only claim resting on opinion rather than a concrete example, so I've flagged it as weak evidence rather than treated it as a root cause.

**Recommended sequence (weeks, low cost):** publish the plan in the ERP, define a shortage-priority rule owned by the planner, split the cutoff into a provisional 2pm order plus a late-adjustment window for weather/timetable-sensitive stores, and replace the phone/WhatsApp late-change channel with something logged. Re-measure after one cycle. Only if the planner then becomes the bottleneck handling late changes from every store directly would I add one coordination role — not four regional managers.

Biggest open question for the CEO: what decisions would the regional managers actually own? If the answer is "exactly these three," the real fix is assigning those decision rights — the org chart is a secondary question.


## Files in work dir after run

- brightwell-root-cause-recommendation.md
- com-03-input.md

## File written by the run: brightwell-root-cause-recommendation.md

# Operating model: Brightwell Bakeries, central bakery ↔ store coordination

**Answer:** Fix the order-cutoff timing, production-plan visibility, and shortage-allocation rule first (weeks, near-zero cost) — these three process/decision-rights gaps explain the waste and stockout numbers directly. Do not add the 4 regional managers now: nothing in the interviews points to a missing layer as the cause, and adding one on top of today's broken process risks becoming a fourth hand-off rather than a fix. Revisit a coordination role only after the fixes are in place, if the planner becomes the bottleneck.

**Confidence:** Medium-high that process/decision-rights, not structure, is the primary cause — 7 of 9 interviews independently point to the same three gaps (cutoff timing, no plan visibility, no shortage rule). Low confidence on sizing (no cost/headcount data on the regional-manager proposal, no store count or current span of control) — see Open questions.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Centralized production (2025 move) stays efficient *and* reliable | Stores can see tomorrow's plan and adjust orders as late demand signals arrive | Waste ≤5%, stockouts back near ~2/store/week | Plan sheet lives on planner's personal drive, not shared; cutoff locked at 2pm before decisive signals (weather, timetables) are known | Stores order "blind" and "safe" → waste; bakery can't react to real late demand → stockouts |
| Reliable fulfillment of top-10 items | A rule for who gets priority when an ingredient/item runs short | Predictable, consistent allocation | No rule exists; drivers improvise substitutions on the ramp (I6), night baker splits arbitrarily (I4) | Top-10 stockouts tripled (~2 → ~7/store/week) |
| Store trust in HQ process | A working channel for late order changes | Changes logged and actioned before bake | Changes arrive by phone/WhatsApp at 4–5pm and at night, informally, after the 2pm lock (I1, I3, I4) | Lost/ignored changes, "orders after 2pm just get dropped" (I1) |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| Waste 4.8%→9.2% | Plan sheet not in ERP, not visible to stores → stores can't calibrate orders (I8, I3) | Planner won't share the sheet without explicit permission — no owner has authorized it (I3) | None found — centralization of baking itself isn't contested; it's the *information link* that wasn't rebuilt when production moved | Stores default to "safe" (over-)ordering because they bear stockout pain directly and have no visibility to do otherwise (I8) |
| Stockouts ~2→~7/store/week | 2pm cutoff precedes the signals that actually drive next-day demand — weather (I2), station timetables (I5) | No one owns the cutoff-time policy; no one owns shortage/substitution priority | None found | Drivers (I6) and night baker (I4) are making demand-allocation calls that aren't their job and have no criteria |
| "HQ never listens" / stores feel alone (I7, I5, I9) | Downstream symptom of the above — stores see no plan, can't get late changes in, so it reads as indifference | Same — no visible owner for store concerns in the current process | Weak evidence this is a structural/layer problem — I7's claim is opinion without an example; more consistent with the information gap than with absence of a regional layer | — |

## Decision rights (key decisions)

| Decision | Decides today | Consulted | Executes | Should decide |
|---|---|---|---|---|
| Order cutoff time / policy | Nobody explicitly — inherited from the 2025 move, enforced by planner without being its owner | — | Planner (by default) | Ops/COO sets a policy that reflects when decisive demand signals (weather, timetables) are actually known |
| Production-plan visibility to stores | Planner, informally, and only if permitted ("I'd share it if someone said I may" — I3) | — | Planner | COO/Ops authorizes; plan published automatically via ERP, not gated on one person's permission |
| Late-change intake (after cutoff) | Nobody — defaults to ad hoc phone calls / WhatsApp (I1, I3, I4) | — | Whoever picks up the phone/message | Planner, via a logged channel with a defined late window, not informal messaging |
| Shortage / substitution allocation | Nobody — defaults to delivery drivers on the ramp (I6), or night baker splitting arbitrarily (I4) | — | Driver / night baker | Planner, via a pre-agreed priority rule (e.g., by store sales tier or a swap list), set before the shortage happens |

## Structure options

| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A — CEO proposal: 4 regional managers, no process change | New layer between stores and HQ, presumably fielding store complaints and escalations | Low — doesn't touch cutoff timing, plan visibility, or shortage rule unless explicitly handed those decision rights, in which case the fix *is* the decision-rights change, not the headcount | Not sized by CEO — 4 FTEs + management overhead (flag: get a number) | High — adds a hand-off layer onto an already hand-off-heavy process; risk of becoming a complaint-forwarding layer rather than removing the cause (classic "reorganize before fixing process" trap) | Low |
| B — Fix process + decision rights, no new layer (recommended) | Publish plan in ERP; two-stage ordering (provisional at 2pm, adjustment window for weather/timetable-sensitive items later); explicit shortage-priority rule owned by planner; replace phone/WhatsApp with a logged late-change channel | High — directly closes the three gaps that 7 of 9 interviewees independently named | Low — policy change + an ERP field/shared view + a planning-capacity allowance for a second order wave | Low — builds on existing roles, nobody new to onboard | High |
| C — Single coordination role (phase 2, conditional) | If, after B, the planner is overloaded handling late changes from 9+ stores directly, add one coordination/dispatcher role to aggregate store signals before they hit the planner | Addresses a capacity problem, *if* it materializes | Medium (1 FTE vs. 4) | Medium | Hold — only pursue if B surfaces this bottleneck |

## Spans, layers, sourcing

- Spans and layers: no data in the interviews on current span of control or manager headcount — this isn't something the notes can settle (data gap, see Open questions). More importantly, none of the nine interviews describe a span/layer problem (nobody says "too many stores per manager" or "decisions stuck waiting on an overloaded manager"); every specific complaint traces to process, visibility, or an unassigned decision.
- Sourcing: not applicable — no outsourcing question here.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Publish the planner's production-plan sheet in the ERP, visible to all stores | COO authorizes; planner/IT implements | Weeks 1–2 | Stores can see tomorrow's plan before ordering |
| 2 | Define and communicate a shortage/substitution priority rule; remove the decision from drivers and the night baker | Planner, signed off by COO | Weeks 1–2 | Zero ad hoc substitution calls by drivers within 30 days |
| 3 | Move or split the cutoff: provisional order at 2pm, adjustment window for weather/timetable-sensitive stores (station, high-weather-sensitivity sites) up to ~5–6pm, feeding a small reserved-capacity buffer | Ops + production planner | Weeks 2–4 | Late-change volume handled through the logged channel, not phone/WhatsApp |
| 4 | Replace informal phone/WhatsApp late-change intake with a logged form/ERP field | Planner/IT | Weeks 2–4 | Traceable log of all late changes and their disposition |
| 5 | Re-measure waste % and stockouts/store/week after one full cycle (4–6 weeks) | COO | Week 8 | Waste trending toward 5%; stockouts trending back toward ~2–3/store/week |
| 6 (conditional) | If planner is bottlenecked by direct late-change volume from stores, add one coordination role (Option C) — not 4 regional managers | COO | After step 5 review | Planner cycle time per order day back to pre-overload baseline |

## What would change the answer

1. If the regional-manager proposal is really about giving stores political "air cover" on pricing, assortment, or local commercial decisions unrelated to the bakery-coordination problem (i.e., a different strategic question than the one in the brief), that's a separate case — don't let this waste/stockout data justify it either way.
2. If step 1–4 fixes are implemented and waste/stockouts don't improve within one full cycle, that would kill the process/decision-rights hypothesis and justify reopening the structure question.
3. If store count or planner capacity data (not available in these notes) shows the planner genuinely cannot handle 9+ stores' late changes directly even with a logged channel, that supports Option C (one coordination role) sooner rather than later — still not four regional managers.

## Trap checks

- [x] Broken processes and data fixed/scheduled before any structure change — yes, Option B precedes any new layer.
- [x] Design starts from a capability gap, not the org chart — yes, built from the plan-visibility/cutoff/shortage gaps.
- [ ] Spans differ by type of work — not applicable yet, no span redesign proposed.
- [x] Decision rights for the key decisions are explicit — cutoff policy, plan-sharing, late-change intake, and shortage allocation all given a named owner.
- [x] Centralization proposed only where activities are standardized — note: the 2025 production centralization itself already happened; this case doesn't add more centralization, it rebuilds the information link that centralization broke.
- [x] No activity customers choose the client for is outsourced — not applicable.
- [x] Transition cost and management attention counted and sequenced — yes, phased over ~8 weeks, Option C explicitly held back.
- [x] Culture claims rest on examples, not opinion — I7's "HQ never listens" is flagged as weak evidence (opinion, no example) and treated as a likely symptom of the visibility gap, not used as a standalone root cause.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 9 interviews are representative of the full population of stores/roles, not cherry-picked | Treated as representative | No sampling info given | A systematic skew (e.g., only complaining stores interviewed) is disclosed |
| 2 | Waste and stockouts share the same proximate cause (information gap) rather than two independent problems | Single root-cause framing | I8 directly links "safe ordering" to waste; I1/I2/I5 directly link cutoff/visibility to stockouts | Data shows waste concentrated in stores/items unrelated to visibility (e.g., a shelf-life or recipe issue) |
| 3 | A short adjustment window (to ~5–6pm) and small reserved-capacity buffer are operationally feasible for the central bakery | Assumed feasible at modest cost | Not tested with production/capacity data | Baking line capacity or staffing can't support a second order wave at any reasonable cost |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What decisions, specifically, would the 4 regional managers own? | The CEO's proposal is currently a headcount number, not a decision-rights design — can't be fairly scored against Option B without this | CEO / proposal author | If regional managers would *own* exactly the decisions named above (cutoff policy, plan visibility, shortage rule) and nothing else, Option A and B converge — the recommendation becomes "give those rights to someone," structure is secondary |
| Current span of control (stores per manager, layers from CEO to store) | Needed to test whether spans/layers are actually a problem, or whether it's purely process | COO / HR | Could surface a genuine span problem not visible in these 9 interviews |
| Cost and timeline of the 4-regional-manager proposal | Needed for honest cost comparison against Option B | CEO / Finance | A low-cost, fast regional-manager rollout changes the relative attractiveness, though it still doesn't address the named root causes directly |
| Store count and planner's current daily order-handling load | Determines whether Option C (one coordination role) is needed soon or much later | Production planner / Ops | High load today would move Option C from "phase 2, conditional" to "do in parallel with B" |
| Target date for the 5% waste / stockout fix | Frames how aggressive the transition plan needs to be | COO | A hard near-term deadline (e.g., tied to a board commitment) could compress the 8-week cycle |

