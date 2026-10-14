# com-01-quote-speed on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Opens from the strategy requirement before any structure discussion | yes | Step 1 states 'Strategy: win mid-size/large shippers via fast, reliable quotes — standard quotes answered in ≤1 working day, win rate 22%→30% by end of 2027' before the 'Structure proposed' line merely restates the proposal and before any analysis of it. |
| Shows waiting dominates (~5/6 days) concentrated in approvals and pricing queue | yes | Step 3b table: 'total elapsed 6.0 days, hands-on work 1.0 day' with queue(2.0)+MD(1.5)+Finance(1.0)+Legal(0.5)=5.0 days waiting. |
| Identifies approvals happen on every quote despite written >250k/non-standard limits | yes | 'MD approval is written for >EUR 250k, but "Regional MDs approve every quote..."' and similarly for Finance and Legal in Step 3c. |
| Recommends explicit decision rights for key decisions | yes | Decision rights table: pricing team approves standard quotes within corridor, MD only >250k, Finance only >30 days, Legal only for deviations, and 'Own the customer after signing — To be assigned explicitly'. |
| Shows fix reaches ~1 day without division, keeps division as costed option | yes | Option C: 'removing the 3.0 approval-wait days... leaves elapsed time ≈ 1.0 day'; Option B retains 'EUR 3.2m/year running cost... High transition risk'. |
| Options scored against criteria agreed before scoring | yes | 'Design criteria proposed here, to agree with the CEO before final scoring' precedes the A–D option table; D is explicitly left unscored ('To revisit, not score now'). |
| Treats win-rate link as association, not proof | yes | 'speed and win rate move together in the client's own data' and open question notes value of a win-rate point still needed, avoiding causal claims. |
| Names soft elements (MD/Finance habits, pricing capacity) with dated sequence | yes | Step 3g: 'Regional MDs, Finance and Legal must actually stop reviewing every standard quote — this is a behaviour change'; transition plan lists dates 'Within 4 weeks', 'Within 6 weeks', 'End Q1 2027', 'Q3 2027 review'. |
| Answer line states what changes, in what sequence, by when | yes | 'Have the CEO mandate, within the next 4 weeks, that standard quotes...stop triggering...sign-off...Revisit a smaller, scoped key-account pricing/solutions cell...only after this fix is embedded.' |
| Does not recommend Key Account division as first move | yes | 'Fix decision rights and pricing capacity before building a new division.' |
| Does not invent peer spans/quote times/industry win rates | yes | 'No peer benchmark available' stated explicitly rather than fabricating comparison figures. |

## Transcript

## Turn 1

**User:** Kestrel wants faster quotes to win key accounts. The sales director proposes a new Key Account division. Work the operating model case from the diagnostic pack; answer page for the CEO. (Attached in the working directory: com-01-input.md.)

I've worked this as an operating-model quick case and saved the full answer page to `case-operating-model-kestrel.md`. Here's the core of it:

**The numbers kill the division as the first move.** Of the 6.0-day median quote cycle, only 1.0 day is actual hands-on work — the other 5.0 days are pure waiting. Of that, 3.0 days (MD 1.5 + Finance 1.0 + Legal 0.5) are approvals that, per the written rules, shouldn't even apply to the 70% of quotes that are standard (<€250k, standard terms) — but the decision-map interviews show MDs, Finance and Legal review *every* quote regardless. The other 2.0 days are a central-pricing queue with zero hands-on work attached, pointing to a capacity/prioritization issue, not a missing team.

**Recommendation:** enforce the thresholds already on paper (standard quotes skip MD/Finance/Legal sign-off), give the central pricing team a fast lane for standard quotes, and explicitly assign post-signing customer ownership. That collapses elapsed time to roughly the 1.0 day of real work already in the process — hitting the board's target — for near-zero incremental cost, versus €3.2m/year and 40 FTE for a division that (as proposed) doesn't actually change any decision rights and so inherits the same bottleneck. A scoped, smaller key-account cell for the genuinely complex 30% of quotes is worth revisiting later, sized to real data.

Biggest open gaps flagged in the doc: quote volume (to confirm the queue is prioritization, not a capacity shortfall) and whether "key accounts" actually overlaps with the 70% standard population the target applies to.


## Files in work dir after run

- case-operating-model-kestrel.md
- com-01-input.md

## File written by the run: case-operating-model-kestrel.md

# Operating model: Kestrel Logistics, key-account quoting speed

*Quick case, run from the diagnostic pack (com-01-input.md). Fictional company and figures.*

## Step 1: Sharpen the question

Strategy: win mid-size/large shippers via fast, reliable quotes — standard quotes answered in ≤1 working day, win rate 22%→30% by end of 2027.
Symptom: median quote cycle is 6.0 working days against a 1-day target; quotes answered in ≤2 days win at 34%, quotes answered in ≥5 days win at 17% — speed and win rate move together in the client's own data.
Structure proposed: a new Key Account division (~40 FTE, EUR 3.2m/year, own pricing/solutions/contract team, reporting to CEO), proposed by the sales director.

**Decision question:** Which capabilities and decisions does the 1-day standard-quote target require that today's set-up cannot deliver, and what is the smallest change that closes the gap — before committing to a new 40-FTE division?

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Capability | Standard quotes need ≤1-day turnaround; no unit is accountable for that cycle time today | A unit already hits ≤1 day for standard quotes | **Confirmed** — median is 6.0 days, a 5-day gap |
| Process & systems | Most of the 6 days is waiting, not work | Hands-on time ≈ elapsed time | **Confirmed** — hands-on work is 1.0 of 6.0 days (83% is pure wait) |
| Decision rights | Key approval decisions have no real owner — written thresholds exist but are not applied | Decision map shows clear owners and fast decisions | **Confirmed** — MD, Finance and Legal each review 100% of quotes despite written rules limiting review to above-threshold/non-standard cases |
| Structure | The current division of work (not decision rights) blocks the 1-day target, so a new division is required | Gap closes with process + decision-rights fixes alone | **Killed as stated / reshaped** — the 5 waiting days are fully explained by H2+H3; a new division is not the lever that closes them |
| Spans & layers | Layers or spans are slowing decisions | No delay traced to layers/spans; data insufficient to benchmark | **Open** — no peer data; current layering doesn't look extreme, but no quote-volume data to check pricing-team capacity |
| Sourcing | N/A — no outsourcing question in this case | — | **Not applicable** |
| People & culture | Ownership of decisions (and of the customer post-signing) is contested, not just the written rule | Roles already clear in practice | **Confirmed as a second, separate gap** — "who owns the customer after signing" has no written rule and both sales and regional operations claim it |

## Step 3: Deciding analyses

**a. Strategy-to-capability map.** Strategy needs a reliable ≤1-working-day quote for the 70% of volume that is standard (<EUR 250k, standard lanes/terms). Today's capability: 6.0-day median, with win rate falling from 34% (≤2 days) to 17% (≥5 days) — a 17pp swing on speed alone, which is roughly the size of the whole 22%→30% target. The capability gap is real and strategy-relevant.

**b. Process diagnostics.** Walking the 120-quote trace: total elapsed 6.0 days, hands-on work 1.0 day.

| Step | Elapsed | Hands-on | Pure wait |
|---|---|---|---|
| Sales intake | 0.5 | 0.1 | 0.4 |
| Central pricing queue | 2.0 | 0 | 2.0 |
| Pricing calculation | 0.5 | 0.5 | 0 |
| Regional MD approval | 1.5 | 0.1 | 1.4 |
| Finance approval | 1.0 | 0.1 | 0.9 |
| Legal check | 0.5 | 0.2 | 0.3 |
| **Total** | **6.0** | **1.0** | **5.0** |

Pricing calculation is the only step where elapsed ≈ hands-on — i.e. the only step that is genuinely work-bound. Every other step is dominated by waiting. **5 of the 6 days are queueing or waiting for a sign-off, not work.**

**c. Decision-rights review.** The written rules already carve out standard quotes:
- MD approval is written for >EUR 250k, but "Regional MDs approve every quote; pricing team will not release without it."
- Finance approval is written for terms beyond 30 days, but "Finance reviews every quote."
- Legal approval is written for deviations from standard terms, but "Legal checks every quote, including standard terms."

For the 70% of quotes that are standard (below EUR 250k, standard lanes and terms), none of these three gates should trigger at all under the written policy — in practice all three run every time, accounting for 3.0 of the 5.0 waiting days (MD 1.5 + Finance 1.0 + Legal 0.5). This is the single largest lever in the case. Separately, "who owns the customer after signing" has no written rule at all and is actively contested between sales and regional operations — not on the quoting critical path, but directly relevant to any contract-team design, including the proposed division.

**d. Spans and layers.** Sales: 6 regional sales managers × 4–5 KAMs (two layers). Central pricing: 1 head + 7 analysts (one layer). Neither looks unusually deep from the data given, and no peer benchmark exists to compare against. The 2.0-day central-pricing queue (0 hands-on work attached to it) looks like a capacity/prioritisation issue inside the 7-analyst team rather than a layering problem — but this needs quote-volume data to confirm (see Open questions).

**e. Sourcing assessment.** Not applicable — no activity in this case is a candidate for outsourcing.

**f. Option comparison.** *Design criteria proposed here, to agree with the CEO before final scoring: meets the 1-day target for the 70% standard segment; cost and time to stand up; disruption/management attention; coverage of the full standard-quote population (not just "key accounts").*

| Option | Description | Meets 1-day target (standard) | Cost | Transition risk/time | Coverage of 70% standard volume | Score |
|---|---|---|---|---|---|---|
| A. Status quo | No change | No — 6.0 days | EUR 0 direct, but ~13pp of win rate left on the table (34% vs 17% cohort gap) | None | — | Low |
| B. Sales director's Key Account division | New 40-FTE division, own pricing/solutions/contract team, reports to CEO | Uncertain — proposal is silent on decision rights; if MD/Finance/Legal still review every quote, the new division inherits the same 3.0-day habit | EUR 3.2m/year running cost, plus hiring/stand-up | High — recruiting and building a 40-person unit typically takes 2–4 quarters; absorbs management attention | Unclear — "key accounts" is not defined against the <EUR250k standard-quote population (see Open questions) | Medium |
| C. Enforce decision rights + fast lane (recommended) | Apply the written thresholds as written (standard quotes skip MD/Finance/Legal sign-off); dedicate fast-lane capacity inside the existing 7-analyst pricing team for standard quotes; assign customer ownership explicitly | Yes, modelled — removing the 3.0 approval-wait days and collapsing the queue leaves elapsed time ≈ 1.0 day, which is exactly today's hands-on work total | Near-zero incremental — a CEO mandate, a reissued policy, and reallocating 1–2 of the existing 7 analysts; no new headcount assumed | Low — weeks, behavioural not structural | Full — applies to all standard quotes system-wide, whichever sales channel books them | High |
| D. Scoped key-account cell, sequenced after C | Once C is embedded, add a small senior pricing/solutions pod for the genuinely complex, non-standard 30% (large/non-standard terms), sized to real volume, not a 40-FTE division from day one | N/A — targets the other 30%, not the 1-day standard target | Materially less than EUR 3.2m/year; size to be set from post-C data | Low–medium | Addresses the segment the sales director is really worried about, without duplicating the fixed central functions | To revisit, not score now |

**g. Alignment check (7S) on Option C.** Style: Regional MDs, Finance and Legal must actually stop reviewing every standard quote — this is a behaviour change that needs a visible CEO mandate, not just a memo, since the habit is long-standing ("pricing team will not release without it"). Skills: the pricing team's fast lane needs a simple standard/non-standard triage rule the sales intake step can apply consistently. Incentives: regional MDs and Finance currently carry informal risk-aversion incentives to review everything; the policy reissue should state explicitly that they are not accountable for standard-quote terms within the agreed thresholds.

## Step 4: Trap checks

- [x] Broken processes and data are fixed or scheduled before any structure change. — Option C (process/decision-rights) is sequenced before any structure decision; the division (Option D) is deferred.
- [x] The design starts from a written statement of what the strategy requires, not from the org chart. — Started from the 1-day/30%-win-rate target and the process trace, not from the proposed division.
- [ ] Spans differ by type of work; no single target span for everyone. — **Open**: no peer benchmark data available to set differentiated spans; not blocking this recommendation, but flagged under Open questions.
- [x] Decision rights for the key decisions are explicit in the recommendation. — Option C explicitly reassigns standard-quote approval authority away from blanket MD/Finance/Legal review, and assigns post-signing customer ownership.
- [x] Centralisation is proposed only where activities are standardised. — Pricing stays centralised but differentiates a fast lane for the standardised 70%, rather than carving out a new unit.
- [x] No activity customers choose the client for is outsourced. — No outsourcing proposed.
- [x] Transition cost and management attention are counted against the benefit, and changes are sequenced. — EUR 3.2m/year and 2–4 quarters of build-out (Option B) weighed explicitly against a near-zero-cost, weeks-long policy fix (Option C); transition plan below sequences both.
- [x] Claims about culture or behaviour rest on examples, not opinions. — Based on the decision-map interview quotes (9 people across sales, pricing, finance, two regional MDs), not inference.

## Step 5: Answer page

**Answer:** Fix decision rights and pricing capacity before building a new division. Have the CEO mandate, within the next 4 weeks, that standard quotes (70% of volume, below EUR 250k, standard lanes and terms) stop triggering Regional MD, Finance and Legal sign-off — enforcing the thresholds already written — and give the central pricing team a dedicated fast lane for these quotes. Removing those three approval waits (3.0 of the 5.0 waiting days) and collapsing the queue brings elapsed time down to roughly the 1.0 day of actual hands-on work already in the process — meeting the board's target — at near-zero incremental cost, instead of committing EUR 3.2m/year and 40 FTE to a new division before the process is fixed. Revisit a smaller, scoped key-account pricing/solutions cell for the complex 30% only after this fix is embedded and real volume data justifies it.

**Confidence:** Medium — the process and decision-rights diagnosis is strong (120-quote trace plus 9 interviews, and the arithmetic is internally consistent: 1.0 day hands-on + 5.0 days of wait that decompose cleanly into named causes). It is held to medium, not high, because quote-volume data to confirm the pricing-queue root cause, and a clear mapping of "key accounts" onto the 70% standard-quote population, are both still missing.

**Specialists and review:** None of this requires legal/tax/works-council input as framed (it reassigns internal sign-off authority, not employment terms). If headcount is later reduced or roles reassigned under Option D, HR should review job-grading and consultation requirements at that point.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win mid-size/large shippers on speed and reliability | Standard-quote turnaround | ≤1 working day | 6.0 days median | 5.0 days |
| Win rate 22%→30% by end-2027 | Quotes answered fast enough to convert | ≥30% win rate | 34% when ≤2 days, 17% when ≥5 days, most quotes land in the slow cohort | Speed is the lever; no separate pricing/product gap evidenced |

## Root causes of the gap

| Gap | Process/system cause | Decision-rights cause | Structure cause | People/skills cause |
|---|---|---|---|---|
| 5.0-day wait on standard quotes | Central pricing queue (2.0 days, 0 hands-on) likely a capacity/prioritisation issue | MD, Finance, Legal each review 100% of quotes despite written thresholds limiting this to above-threshold/non-standard cases (3.0 days) | Not evidenced as a structural cause — gap explained by process + decision rights | Review habit entrenched ("pricing team will not release without it"); no incentive change needed to fix the rule, but the behaviour needs an explicit mandate to stop |
| Ambiguous post-sale ownership | — | No written rule; sales and regional operations both claim ownership | Relevant to any contract-team design (including a future division) | — |

## Decision rights (key decisions)

| Decision | Decides (proposed) | Consulted | Executes | Today |
|---|---|---|---|---|
| Approve price on a standard quote (<EUR 250k, standard lanes/terms) | Central pricing analyst, within corridor | — | Pricing team | Regional MD approves every quote regardless of value |
| Approve price above EUR 250k or non-standard lanes | Regional MD | Pricing | Pricing team | Same as written rule — unchanged |
| Approve payment terms ≤30 days | Pricing/sales, no separate sign-off | — | Pricing team | Finance reviews every quote |
| Approve payment terms >30 days | Finance | Pricing | Finance | Same as written rule — unchanged |
| Approve standard contract terms | Sales, no separate sign-off | — | Sales | Legal checks every quote, including standard terms |
| Approve deviation from standard terms | Legal | Sales | Legal | Same as written rule — unchanged |
| Own the customer after signing | To be assigned explicitly (sales or regional operations) | Both | Whoever is assigned | Not written; both claim it |

## Structure options

See Step 3f table above (Options A–D).

## Spans, layers, sourcing

- Spans and layers: Sales — 6 regional sales managers × 4–5 KAMs; central pricing — 1 head + 7 analysts. No peer benchmark available; not identified as the primary driver of delay from the data given. Quote volume vs. 7-analyst capacity is unverified (Open questions).
- Sourcing: Not applicable — no activity in this case is a candidate for outsourcing.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | CEO mandate + reissue the written approval thresholds; confirm with Regional MDs, Finance and Legal that standard quotes bypass their sign-off | CEO + Regional MDs/Finance/Legal leads | Within 4 weeks | Policy reissued; sampled audit shows MDs/Finance/Legal are not reviewing standard quotes |
| 2 | Stand up a fast lane in the central pricing team for standard quotes (reallocate 1–2 of the 7 analysts or set an SLA-priority queue) | Head of central pricing | Within 6 weeks | Standard-quote queue wait ≤0.5 day |
| 3 | Assign post-signing customer ownership explicitly | CEO/COO | Within 4 weeks | Decision map updated; no dual claims in next interview round |
| 4 | Re-trace a fresh sample of quotes | Operations excellence team | End Q1 2027 | Median elapsed ≤1 day for standard quotes; win rate trending toward 30% |
| 5 | Revisit a scoped key-account pricing/solutions cell (Option D) for the complex 30%, sized to real volume/capacity data from steps 1–4 | Sales director + CEO | Q3 2027 review | Cost-benefit case built on actuals, not the current EUR 3.2m/40-FTE estimate |

## What would change the answer

1. If quote-volume data shows the 7-analyst pricing team is capacity-constrained overall (not just mis-prioritised), a fast lane alone won't close the queue — some additional pricing headcount (far short of 40 FTE) would be needed alongside the decision-rights fix.
2. If "key accounts" turns out to be essentially the same population as the 70% standard-quote volume, a dedicated, correctly-resourced key-account team could be a valid way to implement the same fix — the problem would be the division's design (unchanged decision rights, 40 FTE sized without volume data), not the idea of a dedicated team.
3. If MDs, Finance and Legal review every quote because of a past loss event or genuine risk — not habit — then removing the gates needs a compensating control (exception reporting, sampled audit) rather than straight removal.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | "Key accounts" (the sales director's proposed scope) is a different population from "standard quotes" (<EUR 250k, standard lanes/terms, 70% of volume) | Treated as distinct segments | Standard-quote threshold is defined by deal economics, not account tier; no data maps key accounts to deal-size buckets | Client confirms key accounts ≈ the 70% standard population — the division's target scope would then match the strategy's target scope |
| 2 | The 2.0-day central pricing queue is a prioritisation/triage problem inside the existing team, not an overall capacity shortfall | Recommended fix = fast lane, no new hires | Pricing calculation itself takes only 0.5 day hands-on, so the team can clearly work fast; the queue sits before that step | Volume data shows the team is short of total capacity, not just mis-sequencing work |
| 3 | The written approval thresholds (MD >EUR250k, Finance >30 days, Legal on deviations) still reflect the risk the business is willing to accept | Recommended enforcing them as written, at zero new governance cost | Decision-map "written rule" column, unchanged since presumably set deliberately | The thresholds are outdated or were overridden after a specific loss/compliance event — then they need resetting, not just enforcing |
| 4 | EUR 3.2m/year and 40 FTE is the full run-rate cost of the sales director's proposal (not including one-off stand-up cost) | Used as given | As stated in the proposal | Total cost of ownership (recruiting, systems, management attention) is materially higher or lower |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Monthly/annual quote volume, standard vs. non-standard | Needed to confirm whether the pricing queue is a prioritisation issue (fixable for free) or a capacity shortfall (needs headcount) | Head of central pricing | Determines whether Option C needs added pricing FTEs on top of the fast lane |
| How "key accounts" is defined, and its overlap with the 70% standard-quote population | Determines whether the proposed division's scope actually matches where the speed problem lives | Sales director / CEO | If high overlap, a correctly-resourced key-account team could be the right vehicle for the same fix, not a competing idea |
| Why MDs, Finance and Legal review every quote despite the written thresholds (habit, past incident, lack of trust in pricing) | Determines whether removing the gates is safe as-is or needs a compensating control | Regional MDs, Finance lead, Legal lead | Changes Step 1 of the transition plan from "enforce" to "reset, then enforce" |
| Revenue/margin value of one win-rate point | Needed to build a full cost-benefit case if a scoped key-account cell (Option D) is pursued later | CFO/Finance | Sizes the eventual Option D investment against real returns, rather than the current uncosted 40-FTE estimate |
| Who should own the customer after signing — sales or regional operations | Unresolved in both the current state and the proposed division's "contract team" | CEO/COO | Must be settled regardless of which structure option is chosen |

## Trap checks

See Step 4 above — all ticked except spans/layers differentiation, which is open pending peer benchmark data (not blocking).

