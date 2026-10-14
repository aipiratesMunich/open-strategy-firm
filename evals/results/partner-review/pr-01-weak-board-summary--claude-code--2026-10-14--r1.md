# pr-01-weak-board-summary on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Return | yes | "Verdict:** Return" |
| Finds D1, D2 and D3, each rated Blocker | yes | Finding 1 (Blocker): "'Exploring' and 'considering' are not fundable decisions; no euro budget, owner, or date"; Finding 2 (Blocker): "Exec summary claims catering 'can add EUR 9m'... the table shows 2031 catering potential of EUR 6.4m" |
| Finds at least two of D4, D5, D6 | yes | Finding 7 (Major, D4): "Both customer stats come from one survey of 40 loyalty-club members"; Finding 8 (Major, D5): "No comparable company or market benchmark is cited... for the 5-year, 35%/year online growth rate"; Finding 6 (Major, D6): "Franchising... is never mentioned or ruled out" — all thre |
| States the question the draft must answer and notes the draft does not answer it | yes | "Question the draft must answer:" ... "Answer the draft gives:** 'Explore' catering further and 'consider' an accelerated online roadmap" |
| Gives a concrete fix for every finding | yes | e.g. "Name the two moves, the 2027 euro budget for each, the owner, and the specific approval requested"; "Correct the exec-summary figure to match the table..." |
| Includes a premortem with three reasons | yes | Premortem section lists three numbered items (online growth stalls, catering shortfall, suburban margin breach) |
| Lists at least one thing good that should survive (store-level margin data solid) | yes | "The store-margin-by-format table is genuinely useful granular data; it just needs to be used to actually inform the new-stores decision" |
| Shows what 'fixed' looks like in two to four sentences | yes | "What "fixed" looks like" paragraph contains 4 sentences starting "We recommend the board fund two moves..." |
| Must not invent benchmark figures without a source | yes | States "no comparable regional caterer or bakery-to-office benchmark cited" rather than inventing a figure |
| Must not rewrite the whole document instead of reviewing it | yes | Output is a structured review (findings table, premortem, missing outside view) with only a short illustrative 4-sentence 'fixed' excerpt, not a full rewrite |

## Transcript

## Turn 1

**User:** Review this executive summary before it goes to the Brightwell board next week. Is it ready? (Attached in the working directory: pr-01-input.md.)

# Partner review: Brightwell Bakeries — Growth Strategy 2027-2031 exec summary, gate 3

**Verdict:** Return
**In one line:** The two recommended moves are not actually funded decisions, their headline numbers don't tie to the document's own tables, and together they fall short of the board's EUR 80m target without anyone flagging it.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store margin above 14%? (given)
**Answer the draft gives:** "Explore" catering further and "consider" an accelerated online roadmap; next steps to be defined with management.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Decision Maker | Exec summary, para 3 | "Exploring" and "considering" are not fundable decisions; no euro budget, owner, or date; ends with "next steps will be defined with management" instead of a board ask | The board has nothing concrete to approve — the document fails its own stated purpose | Name the two moves, the 2027 euro budget for each, the owner, and the specific approval requested |
| 2 | Blocker | CFO / Evidence Auditor | Exec summary line 13 vs. Market overview table | Exec summary claims catering "can add EUR 9m in revenue by 2031"; the table shows 2031 catering potential of EUR 6.4m (4.1 + 2.3), i.e. EUR 5.2m above the EUR 1.2m 2026 base | Board approves a budget sized to a number that is ~40-70% too high depending on reading | Correct the exec-summary figure to match the table; state whether it is total or incremental revenue |
| 3 | Blocker | Logician | Exec summary vs. problem statement | Catering (+5.2m) and online (+8.7m) sum to EUR 13.9m, short of the EUR 18m needed to go from EUR 62m to EUR 80m — no bridge is shown and the gap is never acknowledged | Board thinks two moves are sufficient when, even on the document's own optimistic figures, they are not | Build and show the full revenue bridge from EUR 62m to EUR 80m; name what closes the remaining ~EUR 4m+ |
| 4 | Blocker | Logician | Exec summary line 13 vs. Store economics table | "New stores remain an option in suburban locations" is left open, but suburban stores already run at 13.1% margin, below the board's 14% floor — this contradiction is never flagged | Board could approve new suburban stores believing margin is fine, breaching its own guardrail | Either drop suburban new stores as an option and say why, or show a specific change that gets the format above 14% before presenting it as live |
| 5 | Blocker | Evidence Auditor | Exec summary line 13 / Market overview sourcing, line 25 | The EUR 9m catering figure and the 35%/year online growth behind EUR 11m are sourced only to "management estimate" / "management plan" — the client's own forecast returned to the board as analysis | Board is asked to fund numbers that have never been independently tested | Triangulate: bottom-up account pipeline and win rates for catering; comparable bakery/food-delivery growth rates for online |
| 6 | Major | Logician | Whole document | Franchising, one of the four options explicitly in scope per the problem statement, is never mentioned or ruled out | A board member who set the scope will ask why a quarter of the options vanished with no reason given | Add at least one line ruling franchising in or out, with the reason |
| 7 | Major | Evidence Auditor | Customer view, line 39 | Both customer stats come from one survey of 40 loyalty-club members (small, self-selected, already loyal); the 61% online-delivery figure is stated intent, not revealed behavior, yet supports an EUR 8.7m growth plan | A sharp board member discounts the online case as unproven on first question | Triangulate with actual order/pilot conversion data or a broader, representative sample; flag the limitation if kept |
| 8 | Major | CFO | Exec summary, line 13 | No comparable company or market benchmark is cited for either the catering ramp or the 5-year, 35%/year online growth rate | Base case may be a hoped-for case rather than a likely one, and nobody can tell | Cite achieved growth/take-up at comparable regional bakery, food-service, or delivery operators; bound the base case accordingly |
| 9 | Major | Outsider | Section titles ("Market overview," "Store economics," "Customer view") | Titles are descriptive labels, not conclusions | A board member skimming titles learns nothing about the recommendation | Rewrite each title as the finding it proves |
| 10 | Major | Premortem | Whole document | No downside case or stated triggers that would flip the recommendation | Board has no early-warning signal if online or catering underperform | Add a downside case and name the thresholds that would change the recommendation |

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Catering 2031 revenue | Exec summary: "EUR 9m" | Market overview table: EUR 6.4m (4.1 + 2.3) | EUR 2.6m overstated (~40%) |
| Combined growth vs. target | Catering + online uplift from table: EUR 13.9m | Problem statement requires +EUR 18m (62m → 80m) | EUR 4.1m unexplained gap, never addressed |

Online delivery (EUR 11.2m table vs. "EUR 11m" exec summary) ties within rounding — not a finding.

## Missing outside view

- **Corporate catering growth:** no comparable regional caterer or bakery-to-office benchmark cited; number rests solely on management's own estimate.
- **Online delivery, 35%/year for 5 consecutive years:** no comparable food-delivery or grocery-delivery operator's actual sustained growth rate cited to check whether 35%/year for five years is realistic for Brightwell's scale.

## Premortem

1. Online growth stalls well below the assumed 35%/year sustained for five years — the loyalty-club survey sample isn't representative of the broader customer base that would need to convert — and this risk is never addressed.
2. Corporate catering revenue falls far short of management's estimate because no sales capacity, account-acquisition plan, or win-rate evidence backs the number — unaddressed.
3. The board reads "new stores remain an option in suburban locations" as approval and funds suburban stores, pushing blended store margin further below the 14% covenant since suburban already runs at 13.1% — unaddressed.

## What is good and must survive

- The problem statement itself is sharp: named metric, date range, explicit margin constraint, and a closed option set — a good anchor for the rewrite.
- The store-margin-by-format table is genuinely useful granular data; it just needs to be used to actually inform the new-stores decision instead of sitting unconnected to the recommendation.
- Separating 2026 baseline from 2031 potential with a sourcing line underneath each table is the right habit — it only needs the underlying numbers corrected and triangulated.
- The 45-minute delivery threshold (61%) is a genuinely useful operational input for designing an online rollout — keep it there, just stop using it to size the growth case.

## What "fixed" looks like

"We recommend the board fund two moves in the 2027 budget: corporate catering (EUR [X–Y]m by 2031, built from a named account pipeline and benchmarked against comparable regional caterers, not management's own estimate) and online delivery (EUR [X–Y]m by 2031, with the growth rate bounded by what comparable delivery operators have actually achieved). Together with [specified third lever], these close the EUR 62m-to-EUR 80m gap in full. New suburban stores are not recommended until store economics clear the 14% margin floor — they currently sit at 13.1% — and franchising is ruled out because [reason]. We ask the board to approve a 2027 budget of EUR [Z]m for catering and EUR [W]m for online delivery, owned by [name], with a go/no-go review in [date] if growth tracks below [stated threshold]."


## Files in work dir after run

- pr-01-input.md
