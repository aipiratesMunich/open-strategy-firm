# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how" in a way that respects the CEO's request | NO | The day-one answer is unconditional entry: "Day-one answer: Proceed, but phase it ... Nov 3 approve this phased plan." Kill criteria (H1, H5) only trigger 're-scope' or 'lower target, slower spend', never 'do not enter' — whether to enter at all is never actually reopened, only the mode/sequencing i |
| States the EUR 60k study and hire already made are sunk and don't justify entry; CM's future cost counts against budget | yes | "the hire and the study are spent either way; they don't make a distributor-vs-own-sales choice correct on its own forward economics" and the capital waterfall subtracts Tomasz's ongoing salary run-rate through Dec 2028 from the EUR1.5m cap to get ~EUR1.24m remaining. |
| Flags EUR48m vs 80m+ conflict, uses study as documented base, asks for missing study attachment | yes | "EUR 48m (Ines's paid study) vs. EUR 80m+ (Tomasz, unsourced, \"read it somewhere last year\")" and "Get and read \"PL_study_final_v3.pdf\"; reconcile it against Tomasz's EUR 80m figure." |
| Puts EUR3m bar in proportion (~6% of segment) and calls for bottom-up ramp, not a share assumption | yes | "~6% of Ines's EUR 48m study" and trap-check item "Share built bottom-up from named distributor/customer types and win rates — not done, only '4 met, 2 keen' exists." |
| Compares distributors and own sales on cost, speed, control and exit cost using only input/flagged assumptions | NO | The comparison is only promised as a future slide: slide 4 "Body sketch: entry-mode comparison table (cost, speed, control, exit cost)" — this is an outline for later work, not an actual comparison performed in the delivered files; H4 only addresses cost/capex, not control or exit cost. |
| Flags German 31% margin as not tested for Poland | yes | "Poland contribution margin is unknown; Germany's 31% is used only as a directional sanity check, not a Poland forecast (home-market transfer risk)." |
| Answer is enter under named conditions / enter later / do not enter, with exit criteria — not an unconditional go | NO | "Day-one answer: Proceed, but phase it" — entry itself is decided unconditionally; none of the listed kill criteria (H1, H4, H5) actually resolve to 'do not enter Poland', only to re-scoping or mode changes. |
| Open-questions table naming who can answer (e.g. CFO for study, Tomasz for distributor terms) | NO | Next steps are a bullet list ("Next steps / what's needed from Marc, Ines, Tomasz") not a table consistently mapping each question to a named owner; only the hypotheses 'Status' column occasionally names Tomasz, with no systematic owner column. |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | "'Move fast before the Italians' is an unverified competitor claim — no name, share or capacity data"; margins and market size are consistently flagged as unverified/hypotheses, not asserted as fact. |
| Does not treat "we have already hired and paid" as a reason in the recommendation | yes | "Sunk costs justify deciding quickly, not entering, and especially not a specific capital-intensive mode" — explicitly separates urgency from the sunk-cost-as-justification trap. |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

Worked this as a market-entry case. One thing up front: Marc's framing ("we've already got Tomasz and the study, so we're going — just tell us how") is sunk-cost logic. The hire and the study are spent either way; they don't make a distributor-vs-own-sales choice correct on its own forward economics, and the two market-size numbers in the thread haven't even been reconciled yet. I didn't just pick a number and move on — both go into the Nov 3 material as open risks. Full files are in `engagement/corvina-poland/`.

**The gap in numbers:** Board wants EUR 3m revenue by end-2028 within a EUR 1.5m total cap. Tomasz's salary alone (EUR 110k/yr since Sept 2026, through Dec 2028) is ~EUR 257k — already ~17% of the entire cap before a single sample or sales call is funded. What share of the market EUR 3m represents depends on which size number you believe: ~6% of Ines's EUR 48m study, or ~4% of Tomasz's EUR 80m+ (unsourced, "read it somewhere last year"). That's a big swing to be leaving unresolved three weeks before a leadership meeting.

**Day-one answer:** Proceed, but phase it — run a distributor-led pilot in Warsaw using the two leads Tomasz says are already keen, hold off on own-sales capex (van, reps, warehousing), and have Nov 3 approve *that* phased plan with named kill/scale triggers, not a permanent distributor-vs-direct decision.

**Ranked hypotheses (full table in `02-hypotheses.md`):**
| # | Hypothesis | Kill criterion |
|---|---|---|
| H1 Size | Segment is ~EUR 48m, not EUR 80m+ | True 3-city segment reconciles below ~EUR 20-25m → re-scope target |
| H4 Mode | Distributor-led fits inside the ~EUR 1.24m remaining capital; full own-sales doesn't | No distributor commits volume, or direct capex exceeds ~EUR 1.24m |
| H5 Pays | Base case hits EUR 3m within EUR 1.5m cumulative spend | Modelled burn exceeds cap under a realistic (non-instant) ramp |
| H6 Sunk-cost check | Forward case (ignoring past spend) stands on its own | It's negative/marginal and only "we already committed" is carrying it — **this is live now** |
| H2/H3/H7 | Competitor concentration, pipeline quality, alternative use of capital | All currently untested — no data in the thread |

**Ghost deck (SCQA + slide titles, full version in `03-ghost-deck.md`):**
Situation → hire + study already in motion under a 1.5m/3m mandate. Complication → the two size estimates disagree by 67%, margin is unverified, Tomasz's salary already eats 17% of the cap. Question → enter, and how, inside the cap and deadline. Answer → phased distributor-first pilot, not a permanent mode lock.

**What would have to be true / what to test first:** the real segment is closer to EUR 40-50m than 25m; at least one "keen" distributor will commit volume; Poland margin isn't far below Germany's 31% reference; EUR 1.24m covers a 6-9 month pilot plus a scale tranche. Fastest, cheapest next moves: get the actual study PDF, get Tomasz's source for EUR 80m, get Marc/Ines to confirm what counts inside the EUR 1.5m cap, and turn "4 met, 2 keen" into a real pipeline.

Want me to turn this into the actual Nov 3 slide draft, or run the capital/ramp model for H5 once you can get me the study and a cap-scope answer from Ines?


## Files in work dir after run

- cme-03-input.md
- engagement/corvina-poland/00-status.md
- engagement/corvina-poland/01-problem-statement.md
- engagement/corvina-poland/02-hypotheses.md
- engagement/corvina-poland/03-ghost-deck.md

## File written by the run: engagement/corvina-poland/00-status.md

# Status: Corvina — Poland office-coffee entry

**Mode:** Day-one answer (phases 1-2 condensed; no further input available from the user beyond the forwarded thread). Full engagement (phases 3-7) not started — see workplan below for what it would cover.

**Current answer:** Proceed, but phase it. Distributor-led pilot in Warsaw first (using the two already-keen leads), own-sales capex held back until the pilot validates Polish margin and conversion and the EUR 48m/EUR 80m market-size gap is reconciled. Nov 3 should approve this phased plan and its kill/scale triggers, not a permanent distributor-vs-direct choice.

**Key open risks:**
1. Market size unreconciled: EUR 48m (Ines's paid study) vs. EUR 80m+ (Tomasz, unsourced).
2. Study PDF ("PL_study_final_v3.pdf") referenced but not available — scope/methodology unknown.
3. Poland contribution margin unverified; Germany's 31% is a reference only.
4. Tomasz's salary (EUR 110k/yr since Sept 2026) already consumes ~17% of the EUR 1.5m cap before any sales spend; unclear if the EUR 60k study also counts against the cap.
5. "Move fast before the Italians" is an unverified competitor claim — no name, share or capacity data.
6. Marc's framing treats the Tomasz hire and the study as reasons to proceed (sunk-cost logic) rather than testing the forward case on its own; this needs to be named explicitly in the Nov 3 material, not smoothed over.
7. No exit/kill criteria exist yet for Poland.

**Partner gate:** Not run (day-one mode). Recommend a quick partner-review pass (checklist A/B) before this goes into the Nov 3 deck, specifically on: (a) whether the sunk-cost framing has been fully stripped from the recommendation logic, (b) whether the two market-size figures are presented as reconciled or honestly flagged as open.

**Next steps / what's needed from Marc, Ines, Tomasz:**
- The actual study PDF, or at minimum its market-size methodology and geographic/channel scope.
- The source and scope behind Tomasz's EUR 80m figure.
- Confirmation of what counts inside the EUR 1.5m cap (study? Tomasz's salary? both?).
- A structured pipeline from Tomasz beyond "4 met, 2 keen."
- Any indicative volume/placement interest from the two keen distributor leads.

See `01-problem-statement.md`, `02-hypotheses.md`, `03-ghost-deck.md`.


## File written by the run: engagement/corvina-poland/01-problem-statement.md

# Problem statement: Corvina — Poland office-coffee entry

**Question:** Should Corvina enter the Polish office-coffee wholesale market (Warsaw, Kraków, Wrocław), and if so by which mode and sequencing, to reach EUR 3m revenue by end-2028 within a EUR 1.5m total capital cap, given that Tomasz is already hired and the market study already paid for?

| Element | Content |
|---|---|
| Decision | Enter now vs. pause for reconciliation; if enter, mode: distributor-led, own sales force, or phased hybrid; and sequencing (which city/segment first) |
| Decision maker | Marc (CEO); can block/delay: Board (set the EUR 1.5m cap and EUR 3m/2028 target), Ines/CFO (budget release) |
| Success criteria | EUR 3m revenue by end of 2028; total capital spend ≤ EUR 1.5m (scope of this cap vs. sunk costs unconfirmed — see assumptions) |
| Guardrails | Must not breach the EUR 1.5m cap; margin floor not yet set by the board — proposed to test against Germany's 31% contribution margin as a directional reference only, pending Poland-specific data |
| In scope | Office-coffee wholesale channel in Warsaw, Kraków, Wrocław (the study's scope); entry-mode choice; phasing/sequencing; a pilot-and-scale structure for the Nov 3 decision |
| Out of scope | Other Polish cities beyond the three named; other channels (retail, vending, e-commerce); M&A/JV entry; detailed pricing policy (separate case if needed) — flagged as assumptions, not confirmed with Marc |
| Constraints | ~3 weeks to the 3 Nov 2026 leadership meeting; EUR 60k already spent on the study (June 2026, sunk); Tomasz already under contract at EUR 110k/yr since Sept 2026 (sunk/committed independent of mode choice); competitor urgency claim ("the Italians") is unverified, no name or share data; the underlying study PDF is referenced but not yet in hand |
| Decision date | 3 November 2026 — unclear whether this is the final mode-lock or a go/no-go checkpoint; flagged for Marc to clarify |

**Why this matters now:** Tomasz is already operating in-market and his salary is already consuming budget regardless of which mode is chosen, so delay has a real cost. But Marc's framing — "we've already got Tomasz and the study, so we're going" — treats two sunk costs as reasons to lock an entry *mode* now. Sunk costs justify *deciding quickly*, not *entering*, and especially not a specific capital-intensive mode. The two market-size estimates in hand differ by ~67% (EUR 48m vs. EUR 80m+) and have not been reconciled, and Tomasz's salary alone already claims ~17% of the total capital cap before a single sample or sales call is funded. Locking a mode on Nov 3 without resolving these would let past commitments, not forward economics, pick the plan.

**Flagged assumptions to verify:**
1. The EUR 60k study (EUR 48m) and Tomasz's figure (EUR 80m+) may differ in scope (three cities vs. all Poland; wholesale-only vs. all office-coffee spend including retail/vending) — currently unreconciled, treated here as two competing estimates rather than resolved to one number.
2. Whether the EUR 1.5m board cap is inclusive of the EUR 60k study and Tomasz's ongoing EUR 110k/yr salary, or incremental on top of them — assumed here, conservatively, that both count against the cap.
3. Poland contribution margin is unknown; Germany's 31% is used only as a directional sanity check, not a Poland forecast (home-market transfer risk).
4. "Move fast before the Italians" has no named competitor, share or capacity evidence — treated as unverified momentum/urgency claim.
5. No exit, pilot, or kill criteria currently exist for Poland — proposed as part of the Nov 3 answer rather than assumed absent forever.
6. Out-of-scope items (other cities/channels/M&A/pricing) are this analyst's working scope cut, not something Marc has confirmed.

**Agreed by:** Not yet confirmed by Marc — presented as the working frame given no further input is available; flagged for his sign-off before the Nov 3 material is finalised.


## File written by the run: engagement/corvina-poland/02-hypotheses.md

# Hypotheses: Corvina — Poland office-coffee entry

Day-one answer: **Proceed, but phase it** — distributor-led pilot in Warsaw first, own-sales capex held back until a pilot validates Polish margin, conversion and the true market size; Nov 3 approves the phased plan and its kill/scale triggers, not a permanent distributor-vs-direct choice.

Ranked by impact and uncertainty; each kill criterion is written before further data arrives.

| # | Branch | Hypothesis | Number/threshold | Kill criterion | Status |
|---|---|---|---|---|---|
| H1 | Attractive: size | The serviceable Warsaw/Kraków/Wrocław wholesale segment is at least ~EUR 48m, not EUR 80m+ | EUR 48m (Ines's study) vs. EUR 80m+ (Tomasz, unsourced, "read it somewhere last year") — gap unreconciled | If the true 3-city wholesale segment reconciles below ~EUR 20-25m (e.g. Tomasz's figure is nationwide/all-channel and not comparable), the 3m/2028 target implies a share no new entrant takes in two years — forces a re-scope, not necessarily a full kill | Open — need the study PDF and Tomasz's source |
| H2 | Attractive: structure | No single distributor/competitor controls enough of the segment to block entry | Unknown — no competitor names, shares or capacity in the thread | If 2-3 incumbents hold >60-70% with entrenched office-account relationships, distributor-led entry needs a differentiated angle or the plan is killed | Open — no data yet |
| H3 | Can win: early signal | Tomasz's "4 met, 2 keen" is too small a sample to confirm demand | n=4, i.e. a 50% "keen" rate on 4 conversations | If a larger pipeline (e.g. 20+ qualified conversations) shows conversion well below that 50%, the momentum claim driving urgency is overstated | Open — ask Tomasz to log a structured pipeline |
| H4 | How: mode | Distributor-led entry reaches EUR 3m by 2028 within EUR 1.5m faster and at lower capital risk than own sales from day one | Tomasz's salary (EUR 110k/yr, Sept 2026–Dec 2028 ≈ EUR 257k) already consumes ~17% of the EUR 1.5m cap, leaving ~EUR 1.24m for everything else | If no distributor will commit to volume/placement that could plausibly reach meaningful revenue in the window, OR a direct build's required capex (reps, van, warehousing) exceeds ~EUR 1.24m, the corresponding mode is killed | Reshaping: own-sales-only looks capital-constrained on these numbers; distributor-led or hybrid is the live option |
| H5 | Pays | Base case reaches EUR 3m revenue with cumulative spend ≤ EUR 1.5m and a contribution margin that justifies continuing past 2028 | Margin unverified for Poland; Germany reference is 31% (directional only) | If modelled cumulative burn to reach a EUR 3m run-rate exceeds EUR 1.5m under a realistic (non-instant) ramp, or margin comes in well under the Germany reference, the plan needs re-scoping (lower target, slower spend, or a capital ask to the board) | Open — needs a simple ramp/capital model, see workplan |
| H6 | Sunk-cost trap check | The case for entry stands on its own forward economics, not on the fact that Tomasz and the study are already paid for | Test: strip Tomasz's past salary and the EUR 60k study from the calculus — does investing the *remaining* ~EUR 1.24m to reach EUR 3m by 2028 still look positive? | If the forward-only case is negative or marginal and is only being carried by "we already committed," the current plan is sunk-cost reasoning and needs re-justifying on its own merits before Nov 3 | **Live risk** — Marc's own framing ("we've already got Tomasz and the study, so we're going") is exactly this trap; must be addressed explicitly in the Nov 3 material |
| H7 | Beats alternatives | The Poland capital is better spent here than on the next-best use of the same ~EUR 1.5m (e.g. growing the Germany book at a known 31% margin) | Not yet compared | If the Germany (or another core) alternative returns more per euro of capital for the same management attention, Poland needs a non-financial justification (strategic option value) stated explicitly, not assumed | Not yet tested — lowest-effort branch to add if time allows before Nov 3 |

## Trap checks (market-entry playbook)
- [ ] Share built bottom-up from named distributor/customer types and win rates — **not done**, only "4 met, 2 keen" exists.
- [ ] Customers/channel/price tested in Poland, not copied from Germany — **not done**, Germany's 31% margin is a reference only.
- [ ] At least one aggressive incumbent-reaction case modelled — **not done**, no competitor data exists.
- [x] Sunk costs (study, hire) explicitly excluded from the recommendation logic — **flagged as H6**, must stay excluded in the Nov 3 deck.
- [ ] Ramp compared against comparable entries — **not done**; widen range and name the gap in the deck.
- [ ] Exit/kill criteria and exit cost written down before entry — **not done**; proposed as part of the Nov 3 answer.
- [ ] Entry compared with the best alternative use of the same capital — **H7, not yet run**.


## File written by the run: engagement/corvina-poland/03-ghost-deck.md

# Ghost deck: Corvina — Poland office-coffee entry (for 3 Nov 2026 leadership meeting)

**Situation:** Corvina hired a Poland country manager in September 2026 and commissioned a EUR 60k market study, under a board mandate capped at EUR 1.5m total investment and a EUR 3m revenue target by end-2028.

**Complication:** The country manager's own market estimate (EUR 80m+) is roughly 67% higher than the commissioned study's figure (EUR 48m); the two have never been reconciled; Poland's margin is unverified; and the country manager's salary alone already claims ~17% of the entire capital cap before any sales spend. Deciding the entry *mode* now, on the logic that "we're already committed," risks locking in the wrong plan before these are resolved.

**Question:** Should Corvina enter, and if so which mode and sequencing gets to EUR 3m by end-2028 inside the EUR 1.5m cap?

**Answer (day-one, to be tested):** Proceed with a distributor-led pilot in Warsaw, hold own-sales investment back until the pilot proves Polish margin and conversion, and use Nov 3 to approve the phased plan and its kill/scale triggers — not a one-time distributor-vs-direct choice.

## Slide titles (full sentence, each marked "hypothesis")

1. **"Corvina should enter Poland, but the all-or-nothing mode decision Marc wants on Nov 3 can't yet be made responsibly."** [hypothesis]
   - Body sketch: lay out what's missing (reconciled market size, competitor map, Poland margin) vs. what's known (two keen distributor leads, a hired CM).

2. **"The EUR 48m and EUR 80m market estimates describe different things, and resolving which applies changes the required 2028 share from ~6% to ~4%."** [hypothesis]
   - Body sketch: side-by-side of the two figures, likely scope differences (3 cities vs. national; wholesale vs. all channels), and the resulting share-of-market math under each.

3. **"Tomasz's salary alone already consumes ~17% of the EUR 1.5m cap, leaving about EUR 1.24m to fund everything else through 2028."** [hypothesis]
   - Body sketch: capital waterfall — cap, minus study (if in-scope), minus salary run-rate to Dec 2028, = remaining investable capital.

4. **"A distributor-led pilot in Warsaw is the only mode that fits inside the remaining capital and the 2028 deadline; a full own-sales build does not."** [hypothesis]
   - Body sketch: entry-mode comparison table (cost, speed, control, exit cost) against the ~EUR 1.24m remaining budget and the ~26-month runway to Dec 2028.

5. **"Treating the Tomasz hire and the study as reasons to commit, rather than as sunk costs, is inflating confidence in a plan that hasn't been pressure-tested."** [hypothesis]
   - Body sketch: name the sunk-cost logic in Marc's own words, show the forward-only case (capital remaining vs. target) stands or falls on its own, independent of past spend.

6. **"Nov 3 should approve a phased, distributor-first plan with a named pilot, proof point, and kill/scale trigger — not a permanent distributor-vs-direct choice."** [hypothesis]
   - Body sketch: the recommended decision, the 90-day pilot definition, what "scale" and "kill" look like numerically, and what's needed from the board/CFO to release the next capital tranche.

## What would have to be true
- The serviceable 3-city segment is really at least ~EUR 40-50m (closer to the study than to Tomasz's figure).
- At least one of the two "keen" distributor leads will commit to placement/volume that could plausibly build toward EUR 3m by 2028.
- Poland contribution margin, once measured, isn't dramatically below the Germany 31% reference.
- The remaining ~EUR 1.24m is enough to fund a 6-9 month distributor pilot plus a later scale-up tranche, without needing a board top-up.

## What the full engagement would test first (highest impact, fastest kill tests)
1. Get and read "PL_study_final_v3.pdf"; reconcile it against Tomasz's EUR 80m figure and resolve the scope difference.
2. Ask Tomasz to turn "4 met, 2 keen" into a structured pipeline (names, stage, indicative volume) — cheap, fast, already in motion.
3. Get indicative volume/placement commitments (even non-binding) from the two keen distributor leads.
4. Build a simple capital-burn/ramp model for distributor-led vs. own-sales vs. hybrid against the EUR 1.5m cap and the Dec 2028 date.
5. Ask Marc/Ines directly: does the EUR 1.5m cap include the EUR 60k study and Tomasz's salary, or is it incremental on top of both?

