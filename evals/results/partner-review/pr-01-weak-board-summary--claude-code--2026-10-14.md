# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return. | yes | "**Verdict:** Return" |
| Finds D1, D2 and D3, each rated Blocker. | yes | Finding 1 (Blocker): "The board asked for a decision on two funded moves; the draft offers 'exploring' and 'considering' with next steps deferred to management." Finding 2 (Blocker): catering 'EUR 9m' vs table total EUR 6.4m. Finding 3 (Blocker): EUR 18m gap bridge never shown. |
| Finds at least two of D4, D5, D6. | yes | Finding 6 (Major, 40 loyalty-club members survey = D4), Finding 7 (Major, 35%/yr growth no benchmark = D5), Finding 4 (Major, franchising dropped without analysis = D6) — all three found. |
| States the question the draft must answer and notes that the draft does not answer it. | yes | "Question the draft must answer:" ... "Answer the draft gives:" ... 'not a funding decision, not sized against the target' |
| Gives a concrete fix for every finding (not "consider improving"). | yes | e.g. "Correct the figure to EUR 5.2m growth...", "Add an explicit bridge: EUR 62m → [catering] → [online] → [gap]...", "Add margin/contribution-margin estimates for catering and online delivery..." |
| Includes a premortem with three reasons. | yes | Premortem section lists numbered items 1, 2, 3 (target missed, margin breach, franchising discovery). |
| Lists at least one thing that is good and should survive (store-level margin data solid). | yes | "The store economics table: format-level margin breakdown (not just a blended average) is the right level of granularity and should be kept and extended to the new channels." |
| Shows what "fixed" looks like in two to four sentences. | yes | "What 'fixed' looks like" section contains exactly 3 sentences starting with "Brightwell should fund two moves..." |
| Must not invent benchmark figures without a source. | yes | Review explicitly flags missing benchmarks in "Missing outside view" section rather than fabricating specific comparable figures; suggests illustrative sensitivity range 'e.g., 15-20%/yr' as a suggestion, not an asserted real benchmark. |
| Must not rewrite the whole document instead of reviewing it. | yes | Output is a structured review (findings table, numbers that don't tie, premortem, what's good) with only a short illustrative template with bracketed placeholders, not a full rewritten summary. |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready?

# Partner review: Brightwell Bakeries Growth Strategy 2027-2031 — Executive Summary, gate 3

**Verdict:** Return
**In one line:** The summary never answers the question it was given — it doesn't pick two moves, the numbers behind the ones it hints at don't add up to the board's EUR 18m target, and the binding margin constraint is ignored for the very options being pushed.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue EUR 62m → EUR 80m by 2031 while keeping store margin above 14%? (given)
**Answer the draft gives:** "Explore catering further" and "consider an accelerated online roadmap," with next steps TBD with management — not a funding decision, not sized against the target, and silent on margin and on two of the four in-scope options (new stores, franchising).

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Decision Maker | Exec summary, para 3 | The board asked for a *decision on two funded moves*; the draft offers "exploring" and "considering" with next steps deferred to management. | Board cannot approve a 2027 budget line against "exploring" and "considering" — the paper fails its one job. | Rewrite the recommendation as a decision: name the two moves, the EUR amount requested for 2027, and the expected 2031 contribution of each. |
| 2 | **Blocker** | Evidence Auditor | Exec summary ¶2 vs. Market overview table | "Corporate catering can add EUR 9m" does not tie to the table: 2026 catering revenue is EUR 1.2m (0.8+0.4), 2031 potential is EUR 6.4m (4.1+2.3) — a growth of EUR 5.2m, not EUR 9m. | A core number the board will anchor on is wrong by ~75%; if caught in the room, it discredits the whole deck. | Correct the figure to EUR 5.2m growth (or show the derivation if EUR 9m means something else — e.g., including a channel not in the table — and add that channel to the table). |
| 3 | **Blocker** | Skeptical CFO | Whole document | The paper never shows how the two recommended moves close the board's EUR 18m gap (62→80m). Using the table's own numbers, catering (+5.2m) and online (+8.7m, i.e., 11.2m−2.5m) sum to EUR 13.9m — EUR 4.1m short — even before considering execution risk. | Board approves funding believing it reaches EUR 80m; it doesn't, and no one finds out until 2031. | Add an explicit bridge: EUR 62m → [catering] → [online] → [gap] → EUR 80m, with the residual gap named and a proposed source (new stores, franchising, or base growth). |
| 4 | **Major** | Decision Maker | Problem statement vs. exec summary | Franchising, explicitly in scope per the CEO-agreed problem statement, is never mentioned. New stores are dismissed in one clause ("remain an option") with no data applied. | Board may ask why half the mandated options were silently dropped; if franchising is cheaper/faster, the recommendation could be wrong. | Either analyze franchising and new stores with the same rigor as catering/online, or state explicitly why they were screened out and on what basis. |
| 5 | **Major** | Skeptical CFO | Store economics table vs. recommendation | The board's constraint is margin >14%. Current blended margin is 14.39% — already barely above the line. Suburban stores sit at 13.1% (below threshold), yet "new stores in suburban locations" is floated, and neither catering nor online delivery margins are given at all. | The two options being pushed could be the ones that breach the board's own binding constraint, and the board has no way to check. | Add margin/contribution-margin estimates for catering and online delivery, and show pro-forma blended margin under the recommended plan. |
| 6 | **Major** | Evidence Auditor | Customer view section | Both headline customer claims (92% recommend, 61% would order online) rest on 40 self-selected loyalty-club members — a biased, tiny sample used to justify brand strength and demand for a new EUR 11m channel. | A board member who asks "who did you survey?" deflates the demand case for online delivery on the spot. | Either get a representative sample (non-loyalty customers, adequate N) or caveat the claim explicitly and reduce its weight in the recommendation. |
| 7 | **Major** | Outsider | Market overview, online delivery | 35%/year growth sustained for 5 years is the entire basis for the EUR 11m online figure, with no comparable-company or industry benchmark cited. | If 35% is unachievable (typical food-delivery scale-up growth decelerates after year 2-3), the second recommended lever underdelivers and the gap in Finding 3 widens further. | Cite a benchmark (comparable regional bakery/QSR delivery ramp) or sensitize the EUR 11m figure to a more conservative growth curve (e.g., 15-20%/yr) and show the range. |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Catering 2031 contribution | Exec summary: "EUR 9m" | Market overview table: EUR 6.4m total (EUR 5.2m growth over 2026) | EUR 2.6–3.8m overstated depending on which baseline is intended |
| Revenue bridge 62m→80m | Problem statement: EUR 18m required | Catering + online growth from table: EUR 13.9m | EUR 4.1m gap never acknowledged |

## Missing outside view
- **Online delivery 35%/year growth**: no comparable bakery/food-retail delivery ramp cited to support 5 years of sustained 35% growth.
- **Corporate catering 2031 potential**: sourced only to "management estimate," no comparable regional caterer or office-catering market growth rate cited.

## Premortem
1. The board funds catering + online on the strength of this paper; actual catering and online growth land near historical base rates rather than the unbenchmarked management estimates, and the EUR 18m target is missed by more than the EUR 4.1m gap already baked in.
2. Expansion (new suburban stores, or low-margin online delivery economics) pulls blended store margin below the board's 14% floor, because no margin data was ever produced for the two funded channels.
3. Franchising — never evaluated — turns out to be the capital-efficient way to close the gap; the board discovers two years in that a mandated option was dropped without analysis, and re-opens the whole decision.

## What is good and must survive
- The problem statement itself: specific, numeric, time-bound, agreed with the CEO up front — this is exactly the right anchor for everything else.
- The store economics table: format-level margin breakdown (not just a blended average) is the right level of granularity and should be kept and extended to the new channels.
- The customer survey's conditional insight ("61% would order online if delivery <45 minutes") is a genuinely useful, actionable data point — the problem is sample size/bias, not the question asked.

## What "fixed" looks like
"Brightwell should fund two moves in the 2027 budget: corporate catering (EUR [X]m capex, adding EUR 5.2m revenue by 2031 at an estimated store-comparable margin of [Y]%) and an accelerated online delivery roadmap (EUR [X]m capex, adding EUR 8.7m revenue at [Y]% margin, against a benchmarked growth assumption of [Z]%/year). Together these close EUR 13.9m of the required EUR 18m; we recommend closing the remaining EUR 4.1m through [new stores / franchising], detailed below, while holding blended store margin at or above 14%. We are NOT recommending franchising for [stated reason] or further suburban store expansion given its 13.1% margin versus the 14% floor."

---

**Bottom line for you:** this draft is not board-ready. The three Blockers alone (no actual decision, a catering number that's off by ~75% from its own supporting table, and a EUR 4.1m unexplained gap against the board's own target) would each independently warrant pulling it from the agenda. I'd send it back to the team with these findings before it goes anywhere near Brightwell's board next week — want me to help draft the corrected version?


## Files in work dir after run

- pr-01-input.md
