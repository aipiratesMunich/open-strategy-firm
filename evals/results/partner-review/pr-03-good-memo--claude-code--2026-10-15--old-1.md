# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (4/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| verdict is Release or Release with fixes | NO | Verdict: Return |
| no Blocker findings | NO | Finding #1 is labeled 'Blocker' |
| every Major states a concrete consequence; no finding misstates a figure | yes | Majors #2-#5 each have a 'Consequence if unfixed' column with concrete decision impact; no figures misstated |
| names what is good and must survive | yes | 'What is good and must survive' section lists six specific strengths |
| must not demand a named framework, more length, or more slides | yes | No such demand present in findings |
| must not flag stated uncertainty or explicit assumptions as weaknesses | NO | Finding #1 flags the flat-baseline assumption as a Blocker weakness rather than accepting it as a stated assumption |
| must not claim numbers do not tie | yes | 'No outright contradictions. All headline arithmetic checks out and ties correctly: 2.9 + 2.4 = 5.3; 80 − 62 = 18, 18 − 5.3 = 12.7; 5.3/62 ≈ 8.5%' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: "Fund corporate catering and a delivery pilot in 2027", gate 3

**Verdict:** Return
**In one line:** The EUR 12.7m gap that drives the second board ask (revisit the target or the floor) assumes the EUR 62m base stays flat with no organic growth — an unstated assumption the board will ask about and the memo can't currently answer.

**Question the draft must answer:** Which 2027 growth moves should the board fund, and should it revisit the 2031 revenue target or the margin floor? (given, from the header)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the 2031 target, not the floor.
**Match:** Yes, directly — this is a well-built memo. The issues below are about what's missing or unstated, not about whether it answers the question.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Logician / CFO | "What it adds up to" | The EUR 12.7m gap (80m target − 62m base − 5.3m from the two moves) silently assumes the EUR 62m base is flat through 2031. No organic growth/decline rate is stated or sourced. | This number sizes the second board decision. If the base actually grows or shrinks organically, the true gap — and therefore whether to revisit the target or the floor — changes. A board member asking "is this against a flat baseline?" has no answer in the memo. | State the organic growth/decline assumption behind the 62m baseline explicitly, sourced (e.g., last 3–5 years' underlying CAGR), and recompute the gap net of it. |
| 2 | Major | Evidence Auditor / CFO | "Why catering" | No external benchmark for catering revenue growth or central-kitchen margins — only internal bottom-up/top-down triangulation. The delivery section has an outside-view comparable; catering, the larger (EUR 1.2m) investment, does not. | The board can't judge whether EUR 2.9m by 2031 at 32% margin is realistic versus what comparable catering launches actually achieved, or whether the team is anchored only on its own numbers. | Add a comparable (peer bakery/catering chain launch, typical ramp and margin), or state none exists and widen the stated range accordingly. |
| 3 | Major | Logician | "Why not suburban stores or franchising" | 13.1% vs. a 14% floor is the *existing* suburban stores' average margin, used to rule out *new* suburban stores. No evidence that new stores would replicate rather than improve on this (better sites, different format). | A sharp board member could argue this rejects a real option on an unexamined causal leap, which matters because it's one of only two alternatives that could close more of the revenue gap. | State whether 13.1% is stable/representative across stores and years, or explicitly flag this as the best available (imperfect) evidence. |
| 4 | Major | Skeptical CFO | "Why a delivery pilot" | Only a base case (12% growth → EUR 2.4m) and an *upside* case (18% → EUR 3.5m) are shown. No downside case is given. | The board can't see what's at stake if growth comes in below the cited 10–14% comparable range — the answer's exposure to a bad outcome is invisible. | Add a downside case (e.g., 8% growth) and the resulting revenue, consistent with the "what would flip it" discipline used elsewhere in the memo. |
| 5 | Major | Evidence Auditor / Outsider | "What would change our view" | "Framework agreements" appears as the catering kill-switch (40% of customers must sign in six months) but is never defined or connected to the plan described in "Why catering." | The board's main tripwire for killing or continuing the catering investment rests on an undefined mechanism — easy to challenge or misread in the meeting. | Define "framework agreement" where catering is introduced, and justify the 40%/six-month threshold against the P&L logic already given. |
| 6 | Minor | Outsider | "Why a delivery pilot" | "(about EUR 0.6m, a separate board decision...)" doesn't say what the EUR 0.6m is (rollout capex? opex?). | Minor confusion for a reader following the number trail. | Spell out, e.g., "rollout capex of about EUR 0.6m." |
| 7 | Minor | Evidence Auditor | "Why catering" | Trajectory is shown through 2030 (1.6/2.1/2.5/2.7m) but the cited 2031 base case (2.9m) isn't shown in that sequence — reader must extrapolate. | Minor — doesn't contradict, just requires inference. | Add the 2031 figure to the buildup. |
| 8 | Minor | Skeptical CFO | "Why catering" | EUR 1.2m kitchen payback is simple/undiscounted. | Minor given the short (4-year) payback and moderate size, but it's a capital item going to the board. | Note the discount rate used, or state simple payback is used because the horizon is short. |

## Numbers that do not tie
No outright contradictions. All headline arithmetic checks out and ties correctly: 2.9 + 2.4 = 5.3; 80 − 62 = 18, 18 − 5.3 = 12.7; 5.3/62 ≈ 8.5%; the catering contribution-minus-fixed-cost math (0.16/0.32/0.45/0.51m) and the "payback in year four" claim both verify independently. This is a real strength — see below.

## Missing outside view
- **Catering revenue/margin (EUR 2.9m, 32%):** no comparable bakery/catering launch cited — only internal triangulation.
- **Suburban store economics:** no comparable on whether a new-format or better-sited suburban store could beat the existing 13.1% average.
- **Baseline organic growth:** no historical trend for Brightwell's own base business to support treating EUR 62m as flat.
- *(Delivery growth is already well benchmarked — two regional chains' reported 10–14%. No gap here.)*

## Premortem
1. Incumbent catering suppliers fix the "slow delivery" complaint once Brightwell enters, eroding the main differentiator before the central kitchen ramps — not addressed.
2. The EUR 3.10/order delivery contribution erodes at scale (rising platform commissions, promotional discounting to hit the 60-orders/day target) even if the volume threshold is met — only volume is tested, not the economics per order. Not addressed.
3. The EUR 62m base erodes or grows independently of these two moves (cost inflation, wage pressure, footfall), so the real 2031 gap differs from EUR 12.7m regardless of how catering and delivery perform — ties directly to Finding #1. Not addressed.

## What is good and must survive
- The recommendation is fully specific: investment, owner, and start date for both moves — no "explore" or "consider" language anywhere.
- Catering revenue is triangulated two independent ways (bottom-up and top-down) to a tight, consistent range before a base case is chosen.
- The memo pre-empts the obvious objection to the catering growth story (pandemic/return-to-office recovery) with the Q2-over-Q2 data point after attendance settled.
- Alternatives (suburban stores, franchising) are explicitly considered and ruled out with reasons, not silently dropped.
- Falsifiable "what would change our view" thresholds are stated for both moves (fix the catering one's missing definition, but keep the discipline).
- The second ask — target vs. floor — is correctly left to the board rather than quietly decided by the team.

## What "fixed" looks like
"Fund two 2027 moves: a EUR 1.2m corporate catering unit (Head of Operations, launch April 2027) and a EUR 0.3m twelve-month delivery pilot in eight high-street stores (Head of Digital, start March 2027); do not fund suburban stores or franchising, whose margins sit below our 14% floor. Together these add an estimated EUR 5.3m by 2031 (8.5% growth on today's EUR 62m), assuming the rest of the store base holds flat — if it instead grows or shrinks organically, the true gap to the EUR 80m target moves accordingly, and we will confirm that baseline before the next board meeting. Because neither a price increase nor longer hours closes more than a quarter of today's estimated EUR 12.7m gap, and the only moves that could close more (suburban stores, franchising) carry the weakest evidence, we recommend the board revisit the 2031 target rather than the margin floor."


## Files in work dir after run

- pr-03-input.md
