# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | **Verdict:** Return |
| no Blocker findings | NO | / 1 / **Blocker** / Logician / "What it adds up to" (¶4) / |
| every Major states a concrete consequence for the decision, and no finding misstates a figure in the memo | yes | e.g. Major #3: "If pilot stores land at, say, 55/day, there's no agreed rule for whether the EUR0.6m, 18-store rollout decision in 2028 is a go or no-go." |
| names what is good and must survive | yes | "## What is good and must survive" lists catering's build, kill criteria, office-attendance rebuttal, suburban/franchising evidence, one-page format |
| does not demand a named framework, more length, or more slides | yes | No finding requests a named framework or more length; memo's one-page format is praised, not criticized |
| does not flag the stated uncertainty or the explicit assumptions as weaknesses | yes | Findings target missing/undisclosed derivations (e.g. #2, #5, #8), not penalize explicitly disclosed assumptions |
| does not claim numbers do not tie when they do | yes | "## Numbers that do not tie\nNone found. All stated figures ... check out arithmetically." |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell Bakeries 2027 budget memo, gate 3

**Verdict:** Return
**In one line:** The memo's second ask — revisit the 2031 target, not the 14% margin floor — is justified by mischaracterizing the suburban/franchising numbers as "weak evidence" when they're actually the most directly-sourced figures in the memo; the board can't actually tell whether relaxing the floor would close more of the gap, because that was never sized.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and should it revisit the 2031 revenue target or the margin floor? (given)
**Answer the draft gives:** Fund catering (EUR1.2m) and a delivery pilot (EUR0.3m); don't fund suburban stores or franchising; revisit the target, not the floor.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Logician | "What it adds up to" (¶4) | The stated reason for "revisit the target, not the floor" is that suburban/franchising "carry the weakest evidence." They don't — suburban's 13.1% margin is straight from the 2025 P&L, and franchising's 6–8% royalty comes from three actual offers obtained. These are the two most directly-sourced numbers in the memo. The memo never sizes what revenue either option could add *if* the floor were relaxed, so there's no basis for saying the floor is the wrong lever to move. | The CEO brings the board a target-vs-floor choice backed by a reason that collapses under one follow-up question; the board may reject a possibly-sound recommendation, or approve it for a reason that doesn't hold, and nobody has checked whether relaxing the floor would in fact close more of the EUR12.7m gap. | Before the meeting, size the revenue suburban stores/franchising could realistically add at a relaxed floor (e.g., 12–13%). If it's still small, say that — that's the real argument for moving the target, not "weak evidence." |
| 2 | Major | Skeptical CFO | "Why a delivery pilot" (¶3) | Rebuilding the EUR2.4m 2031 delivery figure from the stated drivers (18 stores × 38–60 orders/day × EUR3.10 contribution × 12% annual growth from 2028) gives roughly EUR0.7m–1.7m under every plausible reading — 30–70% short of EUR2.4m. Unlike catering, no year-by-year build is shown. | The figure that sets the size of the "gap to target," and therefore how urgent decision #2 is, can't be checked by anyone who didn't build the model. | Show the year-by-year delivery build (as done for catering's EUR1.6m/2.1m/2.5m/2.7m table) so EUR2.4m and EUR3.5m can be independently verified. |
| 3 | Major | Logician | "Why a delivery pilot" (¶3) / "What would change our view" (¶5) | Scale-up success is "60 orders/day"; the kill criterion is "below 50/day after month six." No rule covers 50–59/day, and no date is given for when 60 must be reached. | If pilot stores land at, say, 55/day, there's no agreed rule for whether the EUR0.6m, 18-store rollout decision in 2028 is a go or no-go. | State one threshold and one date (e.g., "60 orders/day by month 12") and define what happens in between. |
| 4 | Major | Logician / Outsider | "Why catering" (¶2) / "What would change our view" (¶5) | "Framework agreements" and the 40%-signup kill criterion appear for the first time in the risk section; the mechanism was never described in "Why catering," where the EUR1.6m 2027 revenue plan is laid out. | The board is asked to approve a kill criterion for a mechanism it was never told exists, and can't judge whether 40% is an ambitious or trivial bar. | Add one sentence in "Why catering" explaining what a framework agreement commits a customer to and why 40% is the chosen bar. |
| 5 | Major | Evidence Auditor | "What it adds up to" (¶4) | "3% price increase (about EUR1.1m)" has no shown method. A naive 3% on EUR62m is ~EUR1.86m; the memo cites discount competitors as a constraint but doesn't quantify the resulting volume loss. | A board member who does the EUR1.86m multiplication and gets a different number than the memo will start doubting every other figure in it. | Show the elasticity/volume-loss assumption behind EUR1.1m, sourced or labelled as judgment with a range. |
| 6 | Minor | Evidence Auditor | "Why catering" (¶2) | Not stated whether the 12 office managers interviewed are current Brightwell catering customers, lapsed customers, or prospects — changes what "9 named slow delivery from their current supplier" implies. | — | Add one clause describing the sample and how it was selected. |
| 7 | Minor | Evidence Auditor | "Why catering" (¶2) | Delivery cites two regional chains' reported growth as an outside comparable; catering's EUR2.9m/32%-margin forecast has none — only internal bottom-up/top-down estimates and 12 interviews. | — | Add one comparable (a peer operator's corporate-catering scale-up), or state none is available. |
| 8 | Minor | Logician | "What it adds up to" (¶4) | The EUR12.7m gap is calculated against a flat EUR62m base; not stated whether this assumes zero organic/like-for-like growth outside the four initiatives discussed. | — | State the baseline assumption ("flat revenue ex-initiatives") in one clause. |

## Numbers that do not tie
None found. All stated figures (5.3 = 2.9+2.4; 8.5% = 5.3/62; 12.7 = 18−5.3; catering's 1.6/2.1/2.5/2.7 → 0.16/0.32/0.45/0.51 margin walk and year-4 payback) check out arithmetically. Finding #2 is a recompute gap against the memo's own operational drivers, not a contradiction between two stated values, so it's listed as a finding rather than here.

## Missing outside view
- Catering revenue/margin growth: no comparable corporate-catering scale-up cited (delivery has one; catering doesn't).
- Price elasticity for the 3% increase: no comparable cited for how much volume a 3% rise costs against discount competitors.

## Premortem
1. **Internal:** No one is named as owning delivery-order fulfillment at store level. Store staff, measured on in-store sales, likely absorb the packing/fulfillment work — so the "60 orders/day without lowering in-store transactions" test may fail for staffing/incentive reasons, not genuine demand limits.
2. **Internal:** The central kitchen's fixed costs (four staff, EUR0.35m/year) are sized to the base case. If catering demand or order complexity exceeds forecast, fixed costs likely rise with it — the payback math holds them flat through 2030.
3. **External:** The "9 of 12 cite slow delivery" edge is a service gap, not a moat. Once competitors see Brightwell winning office accounts, they can fix delivery speed too, and nothing in the memo addresses how durable the catering win is once framework agreements come up for renewal.

## What is good and must survive
- Catering's full build is shown and ties exactly: revenue → margin → minus fixed costs → cumulative payback in year 4. This is the standard the delivery numbers should be held to.
- Explicit, numeric, falsifiable kill criteria for both moves ("what would change our view") — rare and valuable; most memos never state what would change their mind.
- The office-attendance objection to catering growth is pre-empted directly with the Q2-over-Q2 data point, rather than ignored.
- Suburban stores and franchising are rejected with real numbers (actual 2025 P&L margin, three actual competitor offers), not hand-waved — the raw evidence here is strong even though the conclusion drawn from it (finding #1) needs fixing.
- One page, no padding, appropriate for a CEO/board document.

## What "fixed" looks like
"Fund two moves in 2027: a corporate catering unit (EUR1.2m, Head of Operations, launch April 2027) and a twelve-month delivery pilot in eight stores (EUR0.3m, Head of Digital, start March 2027); do not fund suburban stores or franchising, both of which fail the 14% margin floor. These two moves add an estimated EUR5.3m of 2031 revenue (8.5% growth), leaving a gap to the EUR80m target that neither a 3% price rise nor longer hours closes. Before asking the board to lower the 2031 target rather than the margin floor, we sized what revenue relaxing the floor to fund suburban stores or franchising could realistically add: [result] — so the board is choosing between two quantified options, not one quantified and one not."


## Files in work dir after run

- pr-03-input.md
