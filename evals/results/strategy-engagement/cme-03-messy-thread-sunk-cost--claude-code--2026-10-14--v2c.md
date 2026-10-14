# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (9/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how" respecting the CEO's request | yes | "Should Corvina enter the Warsaw/Kraków/Wrocław office-coffee wholesale market... and if so by which mode"; confidence rated medium because "the 'should we enter at all, and at what scale' question is not yet fully closed" |
| States EUR 60k study and hire already made are sunk and don't justify entry; future country-manager cost counts against budget | yes | "The EUR 60k study and the salary already paid to Tomasz are sunk... should carry zero weight"; "the remaining ~EUR 238k is a real future commitment that must be counted against the cap" |
| Flags EUR 48m vs 80m+ conflict, uses study as base, asks for missing study attachment | yes | "PL_study_final_v3.pdf — mentioned but not attached, so its methodology can't be checked yet"; "Use EUR 48m as the working number... treat '80m+' as unverified" |
| Puts EUR 3m bar in proportion (~6% of segment by 2028) and calls for bottom-up ramp, not share assumption | yes | "roughly a 6.25% share won within about 2 years"; trap check: "Share built bottom-up from named customer types, channel capacity and win rates — No... Fix: Tomasz to turn 'keen' into indicative order volumes" |
| Compares distributors vs own sales on cost, speed, control, exit cost using only input/flagged assumptions | yes | Table 3e compares Capital need, Speed to revenue, Control, Exit cost for Distributor-led vs Own sales force, with assumptions labeled |
| Flags German 31% margin as untested for Poland | yes | "Poland's contribution margin is unknown. Germany runs at 31% (ASSUMPTION used as a proxy only — Poland's cost base... are unverified and could differ materially)" |
| Answer is conditional enter/enter-later/do-not-enter with exit criteria, not unconditional go | NO | Own trap-check admits: "Exit criteria and exit cost written down before entry — Not yet done... Fix: needs to exist before the board commits further capital, not after" — the recommendation only offers a vague scaling checkpoint ("escalate rather than auto-continue"), not defined exit criteria |
| Open-questions table names who can answer each item | yes | Table column "Who can answer" lists "Tomasz", "Ines / whoever holds the file", "Ines / Marc" etc. |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | Keeps "the Italians" unnamed, labels 31% and ramp figures as flagged ASSUMPTIONs, declines to fill gaps ("Untested", "not filled with invented numbers") |
| Does not treat 'already hired and paid' as a reason in the recommendation | yes | "Drop 'we've already got Tomasz and the study' from the rationale entirely — it invites the obvious rebuttal that sunk money justifies nothing" |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

I ran this as a quick strategy case (`case-market-entry-corvina-poland.md` in the working directory). Headline: **enter via a distributor-led, phased pilot — not own sales, and not yet at full EUR 3m scale** — but first, Marc's own justification in the thread needs fixing before it reaches leadership.

**The core issue:** Marc's line — "we've already got Tomasz and the study, so we're going" — is sunk-cost reasoning. The EUR 60k study and the salary already paid to Tomasz are gone either way and shouldn't drive the decision. What should drive it:

- **Market size is unreconciled**: Tomasz's "80m+" is an unsourced memory; the paid study says ~EUR 48m for wholesale office coffee in Warsaw/Kraków/Wrocław specifically. I used EUR 48m as the working number and flagged the gap.
- **The budget math doesn't say what it looks like it says**: Tomasz's *future* salary (not the sunk part, the ~EUR 238k still to be paid through 2028) eats into the EUR 1.5m cap, leaving only ~EUR 1.24m for actual go-to-market spend. That's tight enough that own-sales is probably not affordable — distributor-led is.
- **EUR 3m by 2028 won't pay back by 2028** — using Germany's 31% margin as a rough proxy, cumulative contribution by then is more like EUR 400–550k against ~EUR 1.24m spent. End-2028 should be framed to the board as a ramp milestone, not a profitability milestone.
- **Untested**: competitor/incumbent share (the "Italians" threat is asserted, not shown), and what the same EUR 1.5m would return if put into Germany instead.

The case file has the full issue tree, trap checks, assumptions table, and a specific open-questions list (get the actual study PDF, get a competitor scan, confirm Tomasz's "80m+" scope, check if the board set a margin floor) — worth closing as many as possible before 3 Nov.


## Files in work dir after run

- case-market-entry-corvina-poland.md
- cme-03-input.md

## File written by the run: case-market-entry-corvina-poland.md

# Market entry: Corvina, Poland office-coffee wholesale, how to enter — quick case

*Fictional company, people and figures (from the forwarded thread). Prepared for Marc ahead of the 3 November leadership meeting.*

**The thread's own framing doesn't hold up and needs to be fixed before this goes to leadership:** Marc's 9 October email ("We've already got Tomasz and the study, so we're going") decides to enter *because* money is already spent. The EUR 60k study and the salary already paid to Tomasz are sunk — gone whether Corvina enters or not — and should carry zero weight in the decision. What should decide it is forward economics, and those aren't settled yet: the two market-size estimates in the thread disagree by ~40% (EUR 48m vs "80m+"), Poland's margin is unknown, and the budget leaves only ~EUR 1.24m for actual go-to-market spend once Tomasz's remaining salary through 2028 is counted. None of this means "don't go" — it means the 3 November deck needs to lead with the economics, not the sunk costs, and a few numbers need reconciling first.

## Step 1: Sharpen the question

Raw ask: "Can the consultants just tell us HOW: distributors or own sales?"

Sharpened: **Should Corvina enter the Warsaw/Kraków/Wrocław office-coffee wholesale market by end-2028, and if so by which mode, given it must deliver at least EUR 3m revenue by end-2028 within EUR 1.5m total capital?**

Minimum bar, as stated by the board (Ines, 8 Oct): revenue ≥ EUR 3m by end-2028; capital ≤ EUR 1.5m total. No margin floor was set by the board — flagged as an open question, not assumed.

Why now, per the thread: a country manager already hired and a study already paid for. Per the market-entry playbook, this is the textbook "sunk-cost momentum" trap — explicitly not a valid reason to enter. It is addressed directly in the trap checks below and removed from the decision logic.

I'm not asking Marc or the thread for more input before answering — none is available right now — but the open questions below are genuine gaps, not rhetorical ones, and should be closed before the board sees the final numbers.

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Attractive: size | Addressable segment (office coffee wholesale, Warsaw/Kraków/Wrocław) is at least enough to plausibly reach EUR 3m by 2028 | Bottom-up/paid estimate is materially below what a realistic share could deliver | **Open** — two conflicting numbers, see 3a |
| Attractive: structure | No incumbent holds a dominant share of the addressable segment | Local players together hold so much share that a greenfield entrant can't get a foothold in ~2 years | **Untested** — no data in thread |
| Can win: need | Office buyers will switch supplier for Corvina's offer | The 4 distributor conversations show no real switching interest | **Partially supported, weak evidence** — 2 of 4 "keen," but anecdotal, n=4, self-reported |
| Can win: position | Corvina has a real edge (price, service, product) over incumbents and the "Italians" | No differentiation found once local price/service is checked | **Untested** — no competitor data |
| How: mode | One mode reaches EUR 3m within the remaining ~EUR 1.24m and is exitable if it fails | Every mode needs more capital or time than the cap allows | **Testable now**, see Step 3e |
| Pays | Base case shows a credible path toward payback, even if beyond 2028 | Base case can't recover the capital at any plausible horizon | **Testable now, directionally**, see Step 3f |
| Beats alternatives | EUR 1.5m in Poland returns more than the same capital in Germany or elsewhere | Known-margin core business clearly outperforms per euro deployed | **Open** — no alternative-use figures provided |

## Step 3: Deciding analyses

### 3a. Addressable market sizing

| Estimate | Value | Source | Scope | Strength |
|---|---|---|---|---|
| Paid study | ~EUR 48m/yr | Dedicated EUR 60k study, commissioned by Corvina, delivered June 2026 ("PL_study_final_v3.pdf" — mentioned but **not attached**, so its methodology can't be checked yet) | Office coffee wholesale, Warsaw + Kraków + Wrocław only | Medium — purpose-built, recent, defined scope, but unseen methodology |
| Tomasz's estimate | "80m+" | "I read that somewhere last year" | Undefined — unclear if national, includes retail/HoReCa, or a different channel | Weak — unsourced, undated beyond "last year," no defined scope |

**Triangulation:** these may not actually contradict each other — EUR 80m could be a broader national or multi-channel figure, while EUR 48m is specifically wholesale in three cities. They are not yet reconciled because the scope of Tomasz's number is unknown. **Use EUR 48m as the working number** since it has a defined, matching scope and a named source; treat "80m+" as unverified until its scope is confirmed.

**So what:** EUR 3m by end-2028 against a EUR 48m addressable market is roughly a 6.25% share won within about 2 years of active selling — aggressive for a new entrant with no named channel capacity or win-rate data yet, but not inherently impossible. Hypothesis: **open, reshaped** — size the market at EUR 48m (ASSUMPTION, needs the actual study to confirm), and treat the 3m target as a real stretch goal, not a conservative one.

### 3b. Market structure

No data in the thread on incumbent share, concentration, or the "Italians" Tomasz mentions. **Untested.** This is usually the fastest kill test in a market-entry case and it hasn't been run. Added to data requests below.

### 3c. Customer need and switching

Tomasz met 4 distributors, 2 "keen." This is directional, positive signal but very thin: no volumes, no price points, no contract terms, self-reported enthusiasm from an n=4 sample taken in the first weeks of a new hire settling in. **Weak evidence, not yet a basis for sizing a ramp.**

### 3d. Competitors and reaction

"We should move fast before the Italians do" — no profile of who, their share, or their likely reaction. **Untested**, flagged as a data request. Until this exists, "move fast" is an assertion, not an analysis.

### 3e. Entry modes

| Mode | Capital need | Speed to revenue | Control | Exit cost | Fit vs. EUR 1.24m remaining budget |
|---|---|---|---|---|---|
| Distributor-led | Low — samples, a van for Tomasz, trade incentives; leverages the 2 keen distributors' existing routes | Fast — no hiring/warehouse lead time | Lower — distributor owns the end-customer relationship and sets some of the terms | Low — stop shipping, no severance or lease break | **Fits comfortably** |
| Own sales force | High — reps, warehouse/logistics, vehicle fleet, inventory; ASSUMPTION, directionally derived from the cost of standing up a comparable function, not costed in the thread | Slow — hiring and training lag before first sale | Higher — Corvina owns pricing and the customer relationship | High — severance, lease break, inventory wind-down | **Likely exceeds** what's left once Tomasz's remaining salary is counted (see 3f) |

Hypothesis **confirmed, directionally**: distributor-led is the mode that fits the remaining budget and the ~2-year window; own sales is the one more likely to be killed by the capital cap, though it hasn't been formally costed (data request below).

### 3f. Business case (base case, labeled assumptions)

- Budget cap: EUR 1.5m total (board, Ines, 8 Oct).
- Tomasz's cost going forward: EUR 110k/yr, started Sept 2026. From Sept 2026 to end 2028 is ~28 months (~2.33 years) → ~EUR 256k total. Of that, only the ~2 months already paid (~EUR 18k) is genuinely sunk; the remaining ~EUR 238k is a real future commitment that must be counted against the cap — it is **not** sunk and **not** free just because Tomasz is "already" hired.
- **Remaining go-to-market budget: EUR 1.5m − ~EUR 256k ≈ EUR 1.24m** (ASSUMPTION: assumes no other Poland costs already committed beyond study + Tomasz; would change if other spend exists).
- Margin: Poland's contribution margin is unknown. Germany runs at 31% (ASSUMPTION used as a proxy only — Poland's cost base, distributor cuts, and logistics are unverified and could differ materially).
- At EUR 3m revenue and a 31% margin, full run-rate contribution ≈ EUR 930k/yr — but that's the end-2028 exit rate, not cumulative. Assuming revenue ramps from near-zero toward EUR 3m over the window rather than starting there, cumulative contribution earned by end-2028 is more realistically in the EUR 400–550k range (wide range, no ramp curve given — ASSUMPTION).

**So what:** against ~EUR 1.24m of go-to-market spend, cumulative contribution of ~EUR 400-550k by end-2028 does **not** pay back within the window. Hypothesis **reshaped**: end-2028 should be framed to the board as a ramp-building milestone (revenue scale, distributor network, proof of unit economics), not a profitability or payback milestone. That's a materially different message than "we hit EUR 3m and it pays for itself," and it's worth saying plainly before the 3 November meeting rather than after.

### 3g. Stress test

No incumbent-reaction scenario or sensitivity analysis can be run responsibly without the 3b/3d data. Flagged as a gap, not filled with invented numbers.

### 3h. Alternative use of capital

No figures given for what EUR 1.5m would return if spent on Germany (31% margin, proven) or another lever. **Open.** This is the branch most likely to be skipped before a leadership meeting, and it's the one a sharp board question will hit first: "why Poland and not more of what already works?"

## Step 4: Trap checks

- [ ] Share built bottom-up from named customer types, channel capacity and win rates — **No.** Only 2 "keen" conversations exist; no volumes or win rates. *Fix: Tomasz to turn "keen" into indicative order volumes before 3 Nov.*
- [ ] Customers, channels and price levels tested locally, not copied from home — **Partial.** Real local conversations exist (strength), but no pricing data yet.
- [x] At least one aggressive incumbent reaction modeled — **No**, no competitor data exists to model from. *Fix: basic competitor scan before the meeting.*
- [x] **Sunk costs play no role in the recommendation** — this is the core issue in the thread. Marc's justification ("we've already got Tomasz and the study") is sunk-cost reasoning and is explicitly excluded from this analysis. The recommendation below rests only on forward economics.
- [ ] Ramp compared with comparable entries — **No comparable given.** Range widened accordingly in 3f; named as a gap.
- [x] Money already spent called sunk, and only that — the EUR 60k study and the ~EUR 18k of Tomasz's salary already paid are sunk. His **remaining** salary (~EUR 238k through 2028) is a real future cost and is counted in the budget, not written off as "already covered."
- [ ] Exit criteria and exit cost written down before entry — **Not yet done.** *Fix: needs to exist before the board commits further capital, not after.*
- [ ] Compared with the best alternative use of the same capital — **No**, see 3h.

## Step 5: Answer

**Answer: Enter, via a distributor-led model, phased, with named checkpoints — not a full own-sales build-out, and not yet at the scale implied by "EUR 3m by 2028."**

**Confidence: medium** — the mode choice (distributor over own sales) is well-supported by the budget math alone; the "should we enter at all, and at what scale" question is not yet fully closed because market structure, competitor reaction, and the alternative-use-of-capital comparison are all untested.

**Specialists and review:** Poland distributor agreements (exclusivity, minimum volumes, termination terms) should get local commercial-legal review before signing with either of the 2 "keen" partners. Not covered here.

### Recommendation for the 3 November meeting

1. **Lead with the economics, not the sunk costs.** Drop "we've already got Tomasz and the study" from the rationale entirely — it invites the obvious rebuttal that sunk money justifies nothing. Replace it with the forward case: a ~EUR 48m addressable market (pending study confirmation), a mode that fits the remaining ~EUR 1.24m budget, and a realistic read on when it pays back.
2. **Phase 1 (now–mid 2027): distributor-led pilot.** Use the 2 keen distributor relationships to generate real volume, price, and win-rate data at capped spend (samples + van, order of EUR 150–250k). This is reversible and cheap to exit if it fails.
3. **Checkpoint before scaling further.** Define now — not after — what result by when triggers scaling up (more distributors, possibly a small owned-sales overlay for key accounts) versus pulling back. Suggested starting point for debate: if run-rate after 6–9 months implies less than half the pace needed to reach EUR 3m by 2028, escalate rather than auto-continue.
4. **Reframe end-2028 as a ramp milestone, not a payback milestone**, per 3f — telling the board it pays for itself by 2028 is not supported by the numbers in hand.
5. **Close the two open branches before the meeting if at all possible:** get the actual study PDF to confirm the EUR 48m figure's methodology and scope, and get even a directional competitor/share read so "before the Italians do" is a fact, not a slogan.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Addressable market | EUR 48m/yr | CFO's paid study (June 2026), scope = office coffee wholesale, Warsaw/Kraków/Wrocław | Study PDF shows a different figure or scope, or Tomasz's "80m+" turns out to be the same scope |
| 2 | Tomasz's remaining committed cost through 2028 | ~EUR 238k | EUR 110k/yr × ~26 remaining months | Role ends early, or other Poland costs already exist that reduce the EUR 1.24m further |
| 3 | Poland contribution margin | 31% (Germany's figure, as proxy only) | No Poland-specific margin given | Actual Poland margin (distributor cuts, logistics) comes in lower — would tighten payback further |
| 4 | Revenue ramp shape | Linear-ish build from ~0 to EUR 3m by end-2028 | No ramp curve provided | A real ramp curve (from the study or comparable entries) shows a different cumulative-contribution path |
| 5 | Own-sales mode cost | Directionally "exceeds remaining budget," not formally costed | Derived from typical cost of hiring reps + warehouse + fleet, not from Corvina figures | A real costed own-sales plan comes in under EUR 1.24m |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What exactly does Tomasz's "80m+" cover (geography, channel)? | Decides whether it contradicts the paid study or is a different, non-comparable number | Tomasz | Could raise or lower the addressable-market confidence materially |
| What does the actual study (PL_study_final_v3.pdf) say about methodology and bottom-up build? | EUR 48m is currently taken at face value from a secondhand summary | Ines / whoever holds the file | Could change the market-sizing confidence from medium to high or low |
| Who are the incumbent office-coffee distributors/suppliers in these 3 cities, and what share do they hold? | Fastest kill test in a market-entry case; currently untested | Tomasz, or a short desk scan | Could kill or reshape the whole entry decision if concentration is high |
| Is a specific competitor move ("the Italians") real and imminent, or speculative? | Currently used to justify urgency/speed without evidence | Tomasz | Changes how much weight "move fast" deserves in mode and timing choice |
| Did the board set any margin floor for Poland, or only the revenue and capital figures? | No margin threshold currently exists to test the business case against | Ines / the board | Changes whether 3f's ~EUR 400-550k cumulative contribution is a pass or fail |
| What would the same EUR 1.5m return if deployed into Germany or another lever instead? | Entry has to beat the alternative, not just clear its own bar | Ines / Marc | Could reverse the "enter" recommendation if the alternative is clearly better |

### Trap checks (summary)

See Step 4 above — six of eight checks are open or partially open. The two that pass cleanly are the sunk-cost exclusion and the "called sunk only what's actually sunk" distinction; those are also the two the current thread gets wrong, which is why they're called out explicitly rather than just ticked.

