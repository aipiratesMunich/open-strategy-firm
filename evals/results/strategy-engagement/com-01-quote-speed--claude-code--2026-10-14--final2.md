# com-01-quote-speed on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Opens from the strategy requirement (1 day / 22%→30%) before any structure discussion | NO | Both the chat summary and the file's Answer line open with structural judgment first — "Do not approve the Key Account division as proposed" / "The sales director's proposal doesn't match the evidence" — before the targets are substantively restated; the explicit '1 working day' and '22%→30%' requir |
| Shows waiting dominates (~5 of 6 days) concentrated in approvals and pricing queue | yes | "6.0 days median elapsed (1.0 day of actual work)" and "5.0 days of pure waiting to remove"; root-cause table attributes it to the pricing queue (2.0 days) and MD/Finance/Legal approvals (1.4+0.9+0.3 days). |
| Identifies approvals happen on every quote despite written EUR 250k / non-standard-terms thresholds | yes | "Written rule: MD approves only >EUR 250k; practice: MD approves every quote, and pricing won't release without it" (and same pattern noted for Finance and Legal). |
| Recommends explicit decision rights for key decisions | yes | Decision-rights table assigns: pricing team decides standard quotes within rate card; MD only >EUR250k; Finance only for terms >30 days; Legal only for deviations; and "Customer ownership after signing ... Sales owns the commercial relationship; Regional Operations owns delivery execution". |
| Shows fix reaches ~1 day without new division; division kept as one option with cost and transition risk | yes | "close to the 0.6–1.0 day of actual hands-on work — i.e., to the board's 1-day target — for a fraction of EUR 3.2m/year"; Option A lists "EUR 3.2m/year running... High transition risk." |
| 2-3 options scored against agreed/flagged criteria | yes | "Design criteria proposed below, to agree with the CEO before final scoring: (1) closes the gap... (5) transition risk" followed by a 3-option (A/B/C) scored table. |
| Treats win-rate link as association, not proof | yes | "Confidence: medium, because... the win-rate-by-speed link (34% vs 17%) is correlational" and open question "Does win speed actually drive win rate, or do easier/more attractive deals get fast-tracked..." |
| Names soft elements to change plus a dated sequence | yes | "Risk aversion / habit overriding the written delegation — to be confirmed with MDs" plus transition plan steps with explicit dates ("Within 1 month", "Within 3 months"). |
| Answer line states what changes, in what sequence, by when | yes | "First (0–3 months) enforce the existing written approval thresholds... in parallel, fix the 2.0-day central-pricing queue with a small dedicated fast lane..." |
| Does not recommend the Key Account division as the first move | yes | "Do not approve the Key Account division as proposed" with Option B (no new division) recommended first and Option C pod deferred to step 5 "At 3–4 months". |
| Does not invent peer spans, peer quote times, or industry win rates | yes | Spans discussion only references Kestrel's own org ("6 regional sales managers with 4–5 KAMs each... a normal span") without citing any specific peer-company data or industry win-rate figures. |

## Transcript

## Turn 1

**User:** Kestrel wants faster quotes to win key accounts. The sales director proposes a new Key Account division. Work the operating model case from the diagnostic pack; answer page for the CEO. (Attached in the working directory: com-01-input.md.)

**The sales director's proposal doesn't match the evidence.** The 120-quote trace shows the 6-day median quote has only 1.0 day of actual work — the other 5.0 days are waiting, and 2.6 of those days come from Regional MD, Finance and Legal reviewing *every* quote even though their own written rules only require that above €250k, for terms beyond 30 days, or for non-standard terms. A new 40-FTE, €3.2m/year division doesn't fix an unenforced approval rule — it risks recreating the same override behavior inside a new box.

**Recommendation written up as a CEO answer page** (saved to `case-operating-model-kestrel.md`):
1. **Don't approve the division as proposed.**
2. **First, enforce the existing delegation**: standard quotes (70% of volume) skip MD/Finance/Legal sign-off entirely, replaced by monthly sampling — removes ~2.6 waiting days at near-zero cost.
3. **Fix the central pricing queue** (2.0 days, pure capacity bottleneck) with a small fast lane, not 40 new heads.
4. Together, this can plausibly hit the 1-day target for standard quotes for a fraction of €3.2m/year.
5. A **lean pod** for the genuinely non-standard, large key-account deals may still be worth piloting — but sized to that ~30% volume with explicit decision rights, not a full division reporting to the CEO.

Flagged as open: deal volume/value data to size the financial case, whether the win-rate/speed link is causal or confounded by deal complexity, and a legal review of whether any standard-terms quotes genuinely need case-by-case checking.


## Files in work dir after run

- case-operating-model-kestrel.md
- com-01-input.md

## File written by the run: case-operating-model-kestrel.md

# Operating model: Kestrel Logistics, how to hit the 1-working-day standard quote / 30% win-rate target by end-2027

**Answer:** Do not approve the Key Account division as proposed. First (0–3 months) enforce the existing written approval thresholds so the 70% of quotes that are "standard" (<EUR 250k, standard lanes and terms) skip Regional MD, Finance and Legal sign-off entirely, cutting ~2.6 of the 5.0 waiting days out of the process; in parallel, fix the 2.0-day central-pricing queue with a small dedicated fast lane for standard quotes, not 40 new heads. That combination can plausibly take standard quotes from a 6.0-day median to close to the 0.6–1.0 day of actual hands-on work — i.e., to the board's 1-day target — for a fraction of EUR 3.2m/year. A lean, purpose-built pod for the genuinely non-standard, large "key account" deals (the other 30%) may still be justified, but sized to that volume and given explicit decision rights, not stood up as a 40-FTE division reporting to the CEO.

**Confidence:** medium, because the process trace and decision map (120 quotes, 9 interviews) give strong, specific evidence for the root cause, but the win-rate-by-speed link (34% vs 17%) is correlational and quote volume/value data needed to size the financial case is not in the pack.

**Specialists and review:** Legal should confirm whether any standard-terms quotes genuinely need case-by-case review (e.g., liability, data-protection clauses) before "standard = no legal check" is finalised. HR should review any change to Regional MD / Finance / Legal sign-off authority, since it changes their formal decision rights even though no roles are cut.

## What the strategy requires

| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|
| Win mid/large shippers with fast, reliable quotes | Turn around a standard quote without unnecessary review loops | Answered within 1 working day | 6.0 days median elapsed (1.0 day of actual work) | 5.0 days of pure waiting to remove |
| Win rate 22% → 30% by end-2027 | Speed as a driver of win rate | Quotes answered ≤2 days: 34% win rate | Quotes answered ≥5 days: 17% win rate | 2x win-rate gap tracks directly with the speed gap we are trying to close |

## Root causes of the gap

| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|
| 2.0 days waiting in central pricing queue, 0 hands-on | Single central team (1 head + 7 analysts) queues all quotes with no fast lane for standard cases | — | Pricing centralised with no segmentation by complexity | Possibly workload/prioritisation habits, not skill |
| 1.4 days waiting for Regional MD approval, only 0.1 day of actual review | — | Written rule: MD approves only >EUR 250k; practice: MD approves every quote, and pricing won't release without it | — | Risk aversion / habit overriding the written delegation — to be confirmed with MDs |
| 0.9 days waiting for Finance approval, only 0.1 day of actual review | — | Written rule: Finance approves only terms >30 days; practice: Finance reviews every quote | — | Same pattern as above |
| 0.3 days waiting for Legal, only 0.2 day of actual review | — | Written rule: Legal approves only deviations; practice: Legal checks every quote, including standard terms | — | Same pattern; may also reflect genuine residual legal risk — to verify |
| Post-sale friction / unclear accountability | — | "Who owns the customer after signing" is not written down; Sales and Regional Operations both claim it | — | — |

**So-what:** of the 5.0 waiting days, 2.6 days (52%) are the three approval steps applying full review to quotes that, by the company's own written rule, should not need it. Another 2.0 days (40%) is queue capacity, not reporting lines. Together these explain essentially all of the gap — not a missing division. This matches the operating-model trap of reorganising before fixing the process: a new division on top of the same unenforced approval habits would very likely keep producing a 100%-review pattern inside the new structure too.

## Decision rights (key decisions)

| Decision | Decides (recommended) | Consulted | Executes | Today (practice) |
|---|---|---|---|---|
| Approve price, standard quote (<EUR 250k, standard lanes/terms) | Central pricing team, within rate card | — | Pricing team | Regional MD approves every quote; pricing won't release without it |
| Approve price, >EUR 250k or non-standard | Regional MD | Pricing lead | Pricing team | Same — correctly escalated, but indistinguishable today from the standard case above |
| Approve payment terms ≤30 days | Sales / pricing, standard template | — | Sales | Finance reviews every quote |
| Approve payment terms >30 days | Finance | — | Sales | Same — correctly escalated |
| Standard contract terms, no deviation | Sales / pricing, approved template | — | Sales | Legal checks every quote, including standard terms |
| Deviation from standard terms | Legal | — | Sales | Same — correctly escalated |
| Customer ownership after signing | To be decided and written down: Sales owns the commercial relationship; Regional Operations owns delivery execution | Both | Both | Not written; both claim it |

## Structure options

*Design criteria proposed below, to agree with the CEO before final scoring: (1) closes the gap to a 1-day standard quote, (2) fixes the root cause rather than the symptom, (3) running cost and one-off transition cost, (4) share of quote volume addressed, (5) transition risk / speed to implement.*

| Option | Description | Meets capability need | Cost | Transition risk | Score |
|---|---|---|---|---|---|
| A — Key Account division (sales director's proposal) | New division, ~40 FTE, EUR 3.2m/year, own pricing/solutions/contract team, reports to CEO | Partial at best — doesn't touch the written-vs-practice approval gap; same override behaviour likely recurs inside the new division unless decision rights are explicitly redefined | EUR 3.2m/year running, large one-off stand-up and transition cost (hiring, onboarding, new processes) | High — months of management attention, risk of a second "customer ownership" turf fight between the new division and existing sales/regional ops | Low |
| B — Delegate and declutter (recommended, no new division) | (1) Enforce written thresholds: standard quotes bypass MD/Finance/Legal entirely, replaced by monthly compliance sampling; (2) small dedicated fast-lane pricing capacity (a few analysts, reallocated or added) for standard quotes to kill the 2.0-day queue; (3) write down post-sale account ownership | High — attacks both root causes (2.6 days of unenforced escalation + 2.0 days of queue) directly | Low running cost (a few FTE at most, not 40); low one-off cost (policy + light tooling, no new division) | Low-medium — mainly a governance and capacity change, not a reorg | High |
| C — Lean key-account pod for genuinely non-standard deals | Small pod (order of magnitude fewer than 40 FTE), sized to the ~30% non-standard/large deal volume, with an explicit price corridor it can decide within; escalations only for genuine exceptions | Addresses the minority of volume where Key Account division logic has merit; complements B | Moderate, scaled to actual non-standard volume (needs sizing — see Open questions) | Medium — new team, but small and scoped | Medium — worth piloting after B, not instead of it |

## Spans, layers, sourcing

- Spans and layers: Sales has 6 regional sales managers with 4–5 KAMs each (~24–30 KAMs) — a normal span, not a source of delay on the data given. Central pricing is 1 head + 7 analysts serving all quote volume — thin relative to the 2.0-day queue it produces, consistent with a capacity/queueing cause rather than a reporting-layer cause. No evidence in this pack that adding a layer (a division reporting to the CEO) would shorten any approval step; the approval steps are slow because of how they are used, not how many layers separate them from the top.
- Sourcing: not in scope here — pricing, approval and legal review are core to quote quality and are not candidates for outsourcing on this evidence.

## Transition plan

| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|
| 1 | Publish and enforce the existing approval thresholds: standard quotes (<EUR 250k, standard lanes/terms) release without MD/Finance/Legal sign-off; monthly sample audit replaces case-by-case review | CEO + Regional MDs + Finance + Legal leads | Within 1 month | % of standard quotes released without the three sign-offs; target 100% within 2 months |
| 2 | Stand up a fast lane in central pricing for standard quotes (reallocate or add a few analysts; consider simple rate-card automation) | Head of central pricing | Within 3 months | Queue wait for standard quotes falls from 2.0 days toward <0.5 day |
| 3 | Write down post-sale customer ownership (Sales: relationship; Regional Operations: delivery) | CEO + Sales + Regional Ops leads | Within 1 month | Decision documented and communicated; no open disputes in next quarterly review |
| 4 | Remeasure the 120-quote-style trace for standard quotes | Operations excellence team | At 3 months | Median elapsed time for standard quotes ≤1–1.5 days |
| 5 | Decide on Option C (lean key-account pod) once sized | CEO, informed by Step 4 results and sizing data | At 3–4 months | Pod scoped to actual non-standard deal volume, with explicit decision rights from day one |

## What would change the answer

1. If Legal determines that standard-terms quotes carry real, undisclosed risk that needs case-by-case review (not just habit), then the achievable floor for standard quotes rises above the 0.6–1.0 day hands-on estimate, and the 1-day target may need to shift or the legal step needs its own fix (e.g., a narrower legal-risk checklist) rather than full exemption.
2. If the win-rate-by-speed relationship (34% vs 17%) turns out to be driven mainly by deal complexity rather than speed itself, the financial case for urgency weakens and the investment in Option B should still proceed (it's low-cost) but the case for any paid-for Option C pod weakens further.
3. If "key accounts" turn out to place a large share of standard-sized/standard-lane quotes (not just the non-standard 30%), then Option B alone — not a separate pod — already serves most of the sales director's actual complaint, and Option C should be deferred or dropped.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The 2.0-day central pricing queue wait is a capacity/batching issue, not a need for added review | 2.0 days, 0 hands-on | Zero hands-on time recorded during that wait in the 120-quote trace | The wait is actually caused by incomplete data from sales requiring rework, which isn't visible in this table |
| 2 | "Standard" quotes (<EUR 250k, standard lanes/terms, 70% of volume) map closely to the cases exempt from MD/Finance/Legal sign-off under the written rules | 70% of volume | Definition of "standard" matches the written approval thresholds (EUR 250k; terms ≤30 days; no term deviation) | The written thresholds and the "standard" classification diverge in practice (e.g., many standard-value quotes still have non-standard terms) |
| 3 | The win-rate gain from faster quotes (34% at ≤2 days vs 17% at ≥5 days) extrapolates toward a 1-day target | Directional, not precisely sized | Only two speed buckets from the 120-quote trace are given | The relationship saturates below 2 days (no further win-rate gain from 2 days to 1 day) |
| 4 | "Key accounts" targeted by the sales director's proposal overlap mostly with the 30% non-standard, higher-value quotes | 30% of volume | Standard is defined as <EUR 250k annual value; key accounts are typically larger | Many key accounts also place standard-sized/lane quotes, in which case Option B alone covers most of the sales director's concern |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Total annual quote volume and average deal value, split standard vs non-standard | Needed to size the revenue upside of the win-rate move (22%→30%) and the cost-benefit of Option B vs A vs C | Finance / sales ops | Firms up the business case magnitude; doesn't change the directional recommendation |
| Why do Regional MDs, Finance and Legal review every quote instead of only the excepted cases — risk aversion, past losses, distrust of the pricing team, incentive design? | The delegation fix in Step 1 only holds if the underlying reason is addressed; otherwise the override behaviour recurs | Interviews with the 2 Regional MDs, Finance and Legal leads (extend the 9-person interview round) | Could add a people/incentive workstream alongside Step 1; doesn't change the root-cause diagnosis |
| Does win speed actually drive win rate, or do easier/more attractive deals get fast-tracked and also win more regardless of speed (reverse causality / confounding by deal complexity)? | Determines how much of the 22%→30% target is actually achievable through speed alone | Operations excellence team, re-cutting the 120-quote data by deal complexity | If confounded, the urgency case weakens but the low-cost Option B fix still stands on its own merits |
| How large (volume, revenue) is the genuinely non-standard "key account" segment, and what decision rights would a lean pod need? | Needed before sizing or approving Option C | Sales director + Finance | Determines whether Option C is built at all, and at what size |
| Does any standard-terms quote carry residual legal risk that still needs individual review? | Determines whether Step 1's legal exemption is fully safe | Legal lead | Could narrow the exemption to a legal-risk checklist rather than a blanket exemption |

