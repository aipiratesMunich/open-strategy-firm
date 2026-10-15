# pr-04-numbers-dont-foot on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | **Verdict:** Return |
| Finds D1 and rates it Blocker | yes | Finding #1 / **Blocker** ... 'Transport savings and total operating savings each appear with two different values' |
| Fix for D1 is an instruction, not a suggestion | yes | 'Reconcile transport savings and the total in Slide 5, Slide 7 title, and Slide 7 table to one number; rerun payback and NPV in harrow_leipzig_v3.xlsx and update Slides 1, 8, 9' |
| Numbers-that-do-not-tie table lists transport saving or slide 7 total with both locations | yes | 'Transport savings, EUR m/yr / Slide 5: "saves EUR 1.1m transport cost a year" / Slide 7 table, "Transport" row: EUR 1.3m' |
| Finds at least one of D2, D3 | yes | Finding #3: 'Leipzig's incremental staff/energy cost is netted into the transport line instead of shown gross' |
| Premortem has three reasons, at least one internal | yes | Premortem items 2 and 3 explicitly labeled '(Internal — capacity)' and '(Internal — incentives/structure)' |
| Lists at least one good thing that should survive | yes | 'What is good and must survive' section lists Slide 1 clarity, downside scenario, Halle rule-out, sourced numbers |
| Must not release deck while any number does not tie | yes | Verdict given is Return, not Release/Release with fixes |
| Must not invent benchmark figures without a source | yes | Finding #6 only suggests adding a comparable or disclosing absence, no fabricated figures introduced |

## Transcript

## Turn 1

**User:** CFO angle please: is this board deck ready to go out to the Harrow board on Friday? (Attached in the working directory: pr-04-input.md.)

**Short answer: No — don't send it Friday as-is.** The deck has a genuine numbers-don't-tie problem on the one figure the board will anchor on (operating savings), which by itself forces a Return. Full review below, CFO lens foregrounded as asked.

# Partner review: Harrow Cold Chain — Leipzig hub board deck (draft v3), gate 3

**Verdict:** Return
**In one line:** Slide 5 says transport savings are EUR 1.1m, Slide 7's table says EUR 1.3m, and Slide 7's own title (EUR 3.4m) doesn't match its own table total (EUR 3.6m) — the number that feeds the headline 3.1-year payback and EUR 9.8m NPV is stated three different ways in the deck itself.

**Question the draft must answer:** Should the board approve EUR 14.0m capex for a second hub in Leipzig? (given)
**Answer the draft gives:** Yes — payback 3.1 years, NPV EUR 9.8m, downside still positive.

## Numbers that do not tie
| Number | Location A | Location B | Difference |
|---|---|---|---|
| Transport savings, EUR m/yr | Slide 5: "saves EUR 1.1m transport cost a year" | Slide 7 table, "Transport" row: EUR 1.3m | 0.2 |
| Total operating savings, EUR m/yr | Slide 7 title: "Operating savings of EUR 3.4m a year" | Slide 7 table, "Total" row: EUR 3.6m | 0.2 |

Per the rule the team should hold itself to: a number the document states two ways, however small, is a Blocker on its own — the board can't know whether the hub's 3.1-year payback and EUR 9.8m NPV (Slide 8) were built on EUR 3.4m or EUR 3.6m of annual savings, and every downstream figure (Slide 9's scenarios, the 70% breakeven) inherits the doubt.

## Findings
| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Skeptical CFO | Slide 5 / Slide 7 | Transport savings and total operating savings each appear with two different values (see table above) | Board approves EUR 14.0m on a payback/NPV built from a savings figure the deck can't itself confirm | Reconcile transport savings and the total in Slide 5, Slide 7 title, and Slide 7 table to one number; rerun payback and NPV in `harrow_leipzig_v3.xlsx` and update Slides 1, 8, 9 |
| 2 | Major | Skeptical CFO | Slide 8 | Payback basis undefined: not stated whether 3.1 years is simple or discounted, or measured from first capex (2027) or operations start (Q3 2028) | A board member who asks "payback from when, discounted?" exposes a gap live in the meeting | State the payback method and start date on Slide 8 |
| 3 | Major | Skeptical CFO | Slide 7 | Leipzig's incremental staff/energy cost is netted into the transport line instead of shown gross | Board can't see the real size of new Leipzig opex or stress-test it independently | Show Leipzig incremental opex as its own line; show transport savings gross |
| 4 | Major | Logician / CFO | Slide 4 vs Slide 9 | Unclear whether the "two of five" customers whose GDP requirement rules out the Halle alternative are the same "two of five largest customers" whose loss flips the investment case | If they're the same accounts, one customer event simultaneously removes the reason to build *and* the downside protection — the board isn't told this | Confirm whether these are the same accounts; disclose contract terms/renewal dates for the customers driving both the GDP constraint and the breakeven |
| 5 | Major | Logician | Slide 4 | Only three options tested; no hybrid (route GDP-sensitive volume to owned/certified capacity, rest via cheaper Halle third-party) considered before committing to a full EUR 14.0m owned hub | Board isn't shown a possibly cheaper way to satisfy the one constraint that kills the third-party option | Add a hybrid option with its capex, or state explicitly why it was excluded |
| 6 | Major | CFO / Outside view | Whole deck | No external or internal benchmark for capex-per-capacity, payback period, or overtime-removal savings against any comparable hub build | Board has no reference point for whether EUR 14.0m for 55% added capacity / 3.1-year payback is good, typical, or optimistic | Add one comparable (e.g., Kassel's own historical build cost, or a cited industry reference) or state plainly this is a greenfield estimate with no comparable |
| 7 | Minor | Evidence Auditor | Slide 6 | Two contractor quotes (Bauer, Kroll) feed one EUR 8.4m building figure; not stated which was used or how blended | — | State which quote or blend produced EUR 8.4m |
| 8 | Minor | Outsider | Slide 2 | Title says overtime "tripled since 2022" (EUR 0.7m → EUR 2.3m is 3.3x) | — | Reword to "more than tripled" |
| 9 | Minor | Evidence Auditor | Slide 4 | "Capacity added" percentages (12%/20%/55%) have no stated base | — | Footnote the base (e.g., % of current Kassel throughput) |

## Missing outside view
- Capex per unit of cold-storage capacity and typical payback for a second distribution hub: no comparable cited, internal or external.
- 41% distance cut → EUR 1.1–1.3m transport saving: no benchmark for how logistics networks of similar scale translate distance reduction into realized cost saving (vs. modeled).

## Premortem
1. **(External)** Eastern volume growth normalizes after 2027 — the 62% new-volume share since 2023 reflects a specific 2–3 year growth phase; the deck gives no outside-view check on whether that rate continues, and the case is not shown to survive if it doesn't.
2. **(Internal — capacity)** The 38-person Leipzig hiring plan (Q4 2027, presumably GDP/cold-chain certified roles) has no named recruiting lead or contingency; if hiring slips, the Q3 2028 operations start — and the savings that drive the whole payback — slip with it.
3. **(Internal — incentives/structure)** No one is named as owner of migrating eastern customer volume and routing from Kassel to Leipzig once it opens. The COO owns the capex/build; Kassel's own site management, whose overtime budget is the thing being "freed," has no stated incentive to release volume promptly. If the handoff drags, both hubs run cost while Leipzig sits underutilized.

## What is good and must survive
- Slide 1 states the decision, amount, dates and owner in one sentence — a board member knows exactly what they're approving.
- Downside scenario and explicit breakeven threshold (volume below 70% of plan) are stated on Slide 9, not hidden.
- The Halle alternative is ruled out with a specific contractual reason (GDP clause 7.2), not hand-waved.
- Most numbers are sourced with system and extraction date (Slides 2, 3, 6) — good discipline, just needs to extend to Slide 7.

## What "fixed" looks like
Slide 7 states one operating-savings figure that matches its own table and Slide 5, with Leipzig's incremental opex broken out as its own line rather than netted. Slide 8 states explicitly whether the payback is simple or discounted and from which start date. Slide 1's headline (capex, payback, NPV) is then rerun from that single reconciled savings figure before this goes back to the board.


## Files in work dir after run

- pr-04-input.md
