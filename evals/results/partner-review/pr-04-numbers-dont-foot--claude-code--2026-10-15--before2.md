# pr-04-numbers-dont-foot on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: verdict is **Return**. | yes | "**Verdict:** Return" |
| Must: finds D1 and rates it Blocker. | yes | Finding 1 (Blocker): "Transport saving is EUR 1.1m in the slide that calculates it, EUR 1.3m in the slide that sums it"; Finding 2 (Blocker): "'EUR 3.4m' headline vs 'EUR 3.6m' summed total" |
| Must: the fix for D1 is an instruction, not a suggestion. | yes | "Unbundle the netted line into three visible rows... Show the net arithmetic explicitly and make slide 5's title match slide 7's table" / "Fix the title to match the table, or fix the table to match the title" |
| Must: the 'Numbers that do not tie' table lists the transport saving or the slide 7 total with both locations. | yes | Table row: "Transport saving / Slide 5 title: ...EUR 1.1m... / Slide 7 table: Transport line = EUR 1.3m" |
| Must: finds at least one of D2, D3. | yes | "slide 7's note that 'additional Leipzig operating cost (staff, energy) is netted into the transport line' with no breakout" — matches D3 (netting Leipzig opex into transport without showing it) |
| Must: premortem has three reasons and at least one internal to the client/team. | NO | The three premortem reasons are construction cost overrun (external/market), customer concentration (external/market), and savings not materializing due to hidden netted costs in the model (an analytical/disclosure issue) — none explicitly ties to owner/sponsor buy-in, incentives, execution capacity |
| Must: lists at least one thing that is good and should survive. | yes | "Options were tested, not assumed — the three-option comparison (slide 4)..." under 'What is good and must survive' |
| Must not: release the deck while any number does not tie. | yes | Verdict is Return, with explicit instruction "don't send it as-is" |
| Must not: invent benchmark figures without a source. | yes | "Capex per unit benchmark: no comparison of EUR 14.0m... against industry norms" — flags absence rather than inventing a figure |

## Transcript

## Turn 1

**User:** CFO angle please: is this board deck ready to go out to the Harrow board on Friday? (Attached in the working directory: pr-04-input.md.)

I read the deck. Here's the review, from the CFO seat — verdict first, detail below.

# Partner review: Harrow Cold Chain board deck (draft v3), gate 3

**Verdict:** Return
**In one line:** The two numbers that matter most — annual operating savings and the transport-saving component — don't tie to their own supporting tables, and the methodology hides new Leipzig operating costs inside a netted line the board can't see.

**Question the draft must answer:** Should the board approve EUR 14.0m capex for a Leipzig hub, built 2027–2028? (given, slide 1)
**Answer the draft gives:** Yes — 3.1-year payback, EUR 9.8m NPV, downside case still positive. Internally consistent-*looking*, but the savings build doesn't foot.

## Numbers that do not tie

| Number | Location A | Location B | Difference |
|---|---|---|---|
| Transport saving | Slide 5 title: "saves EUR 1.1m transport cost a year" | Slide 7 table: Transport line = EUR 1.3m | EUR 0.2m, and direction is backwards — netting *in* new Leipzig staff/energy cost should lower this line below the gross 1.1m, not raise it above |
| Total annual operating saving | Slide 7 title: "Operating savings of EUR 3.4m a year" | Slide 7 table total: 1.3 + 2.3 = EUR 3.6m | EUR 0.2m — the slide's own headline doesn't match its own table |

Both discrepancies flow from the same root cause: slide 7's note that "additional Leipzig operating cost (staff, energy) is netted into the transport line" with no breakout. Nobody outside the model can tell what the new hub actually costs to run, or verify any of the three numbers on that slide. The NPV and payback figures on slides 1, 8, and 9 are built on this unverifiable base.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Skeptical CFO | Slide 5 vs Slide 7 | Transport saving is EUR 1.1m in the slide that calculates it, EUR 1.3m in the slide that sums it — and the 1.3m supposedly already nets *out* new hub operating costs, which should make it lower, not higher | The board approves EUR 14.0m against an EUR 3.4–3.6m savings case that cannot currently be reconciled to its own source slide; if challenged in the room, management has no answer for which number is right | Unbundle the netted line into three visible rows: (a) gross transport saving, (b) new Leipzig staff cost, (c) new Leipzig energy cost. Show the net arithmetic explicitly and make slide 5's title match slide 7's table |
| 2 | Blocker | Skeptical CFO | Slide 7 title vs table | "EUR 3.4m" headline vs "EUR 3.6m" summed total — a basic footing error on the single most load-bearing slide in the deck | Any board member who adds 1.3 + 2.3 on paper catches this before the vote; it undermines confidence in every other number in the model | Fix the title to match the table, or fix the table to match the title — but find out which one is wrong first, since they can't both be right |
| 3 | Major | Evidence Auditor | Slide 4, "Capacity added 55%" | Leipzig's 55% capacity-added figure has no supporting calculation anywhere in the deck (unlike the 41% distance cut on slide 5 or the 62% volume share on slide 3, both of which tie) | The central three-option comparison table — the basis for rejecting the two cheaper alternatives — rests on an unsourced number | Add the underlying capacity figures (Kassel current capacity, Leipzig design capacity) so 55% can be checked, same treatment as slides 3 and 5 |
| 4 | Major | Skeptical CFO | Slide 6, capex table | EUR 14.0m capex has no contingency line, and the two biggest components (building, cold-storage equipment = EUR 11.5m of 14.0m) rest on two contractor quotes and one equipment quote from mid-2026, roughly a year before contractor award (slide 10: March 2027) | A construction cost overrun of even 10% (common for cold-storage builds with specialized refrigeration) erases most of the payback cushion in the downside case; the board isn't told this risk exists | Add a contingency line (typically 5–10% for this project type) and a capex-sensitivity row on slide 9 alongside the volume sensitivity, so the board sees payback/NPV under a capex overrun, not just under a volume shortfall |
| 5 | Major | Skeptical CFO | Slide 8 / model reference | NPV and payback appear to be pre-tax, pre-depreciation cash flows with no stated discount-rate justification (why 8%?) and no terminal value for a building with a useful life well beyond the 10-year horizon | The board can't tell if 9.8m NPV is conservative or optimistic without knowing the tax treatment and whether terminal value was excluded (which would understate NPV) or some other asset life assumption was used (which could overstate it) | State the discount rate's basis (WACC?), whether cash flows are pre- or post-tax, and whether terminal/residual value was included or deliberately excluded and why |
| 6 | Minor | Decision Maker | Slide 1 / Slide 7 | "Payback 3.1 years" has no stated reference date — from capex start (2027), operations start (Q3 2028), or first full savings year (2029)? | Ambiguity invites an easy clarifying question the presenter should not be fielding live | State the payback reference point explicitly, e.g. "3.1 years from first capex outlay (2027)" |

## Missing outside view

- **Overtime elimination assumption:** no comparator for how reliably a second hub actually removes 100% of overtime cost in year one of full operation versus a phased ramp-down. Harrow's own 2022–2025 trend (slide 2) shows overtime cost tripling as utilisation climbed — worth checking whether comparable dual-hub rollouts in cold-chain logistics saw a clean step-down or a multi-year taper.
- **Capex per unit benchmark:** no comparison of EUR 14.0m (or EUR per pallet position / per sqm) against industry norms for a GDP-certified cold-storage facility, to sanity-check whether the two contractor quotes are in a reasonable range.

## Premortem

1. **Construction cost overrun.** Two quotes, no contingency line, 8-month-old pricing by the time contracts are signed — cold-storage refrigeration costs have been volatile. A 10–15% overrun alone could push payback past 4 years even in the base volume case, and this isn't shown anywhere (Finding 4).
2. **Customer concentration.** Slide 9 already flags that losing 2 of the 5 largest customers drops volume below the 70% threshold where the answer flips — but the deck doesn't show how concentrated those 5 customers are as a share of eastern volume, or what Harrow is doing to de-risk that concentration before 2029.
3. **Savings don't materialize as modeled because the "transport line" already contains unknown Leipzig opex.** If new hub staffing or energy costs run higher than whatever was netted in (invisible to the board per Finding 1), the real savings could be well below EUR 3.4–3.6m with no one having seen the gross assumptions to know it's happening.

## What is good and must survive

- The problem framing is tight and well-evidenced: Kassel's utilisation/overtime trend (slide 2) and the eastern-volume growth driver (slide 3) both tie cleanly and build a genuine case for action.
- Options were tested, not assumed — the three-option comparison (slide 4) and the GDP-certification contract clause rejecting the cheaper Halle option are specific and verifiable (contract clause 7.2).
- The downside sensitivity (slide 9) and the explicit "flips below 70% of plan" threshold is exactly the right instinct — it's just incomplete (missing a capex-side sensitivity, Finding 4).
- Distance and volume-share percentages (41%, 62%) are both independently checkable from the data given and both tie correctly.

## What "fixed" looks like

Slide 7 should show three separate lines — gross transport saving, new Leipzig staff cost, new Leipzig energy cost — netting to a total that matches its own title exactly, with slide 5's headline saving restated to match. Slide 9's sensitivity table should add a capex-overrun column alongside the existing volume scenarios, and slide 6 should carry an explicit contingency line. Once those tie and the capacity-added figure on slide 4 has a shown calculation, the recommendation itself doesn't need to change — the underlying case looks genuine — but right now a CFO cannot sign off on a deck whose own headline number doesn't add up on its own slide.

**Bottom line for Friday:** don't send it as-is. The two footing errors (Findings 1–2) are a half-day fix once someone pulls the real staff/energy numbers out of the netted line; Findings 3–5 need the model owner, not just the deck owner, and could take a few days. If Friday is fixed, I'd push for Thursday's full day as fix-and-recheck buffer, or slip the board date rather than present numbers that don't tie.


## Files in work dir after run

- pr-04-input.md
