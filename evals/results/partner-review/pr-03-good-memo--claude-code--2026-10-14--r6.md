# pr-03-good-memo on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (5/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Verdict is Release or Release with fixes | NO | **Verdict:** Return |
| No Blocker findings | NO | Finding #1 is labeled 'Blocker': 'The memo frames "revisit target or floor" as a board decision in the header, then resolves it in one buried sentence...' |
| Every Major states a concrete consequence and no finding misstates a figure in the memo | yes | E.g. Finding 2: 'A board member applies the floor consistently and asks why a worse-than-suburban-margin business is being funded...'; catering margins 10/15/18/19% are consistent with the stated 32% contribution margin and revenue figures. |
| Names what is good and must survive | yes | '## What is good and must survive' lists decision 1's actionable recommendation, triangulation effort, falsifiable kill criteria, honesty about the shortfall, and pilot structuring. |
| Does not demand a named framework, more length, or more slides | yes | All fixes are specific textual edits (e.g., 'Move the recommendation...into the lead paragraph', 'Add one line distinguishing...') with no demand for a framework or added length/slides. |
| Does not flag stated uncertainty or explicit assumptions as weaknesses | yes | Finding 8 criticizes an assumption that is 'never stated or flagged' (i.e., implicit/unstated), and the memo's explicit uncertainty (the EUR 5.3m shortfall) is praised as 'Honest about the shortfall' rather than criticized. |
| Does not claim numbers do not tie when they do | yes | '## Numbers that do not tie\nNone found — EUR 2.9m + EUR 2.4m = EUR 5.3m, 5.3/62 = 8.5%... This is a well-tied memo arithmetically.' |

## Transcript

## Turn 1

**User:** Partner review please. This memo goes to the Brightwell CEO tomorrow. (Attached in the working directory: pr-03-input.md.)

# Partner review: Brightwell Bakeries board memo, gate 3

**Verdict:** Return
**In one line:** The memo answers decision 1 (fund catering + delivery) with real rigor, but ducks decision 2 — the board is explicitly asked to resolve "target or floor," and the memo's answer is one unsupported sentence with no number, owner, or process attached.

**Question the draft must answer:** Which two growth moves should the board fund in the 2027 budget, and should the board revisit the 2031 revenue target or the margin floor? (given, from the header)
**Answer the draft gives:** Fund catering (EUR 1.2m) and a delivery pilot (EUR 0.3m); don't fund suburban stores or franchising; revisit the target, not the floor — but with no revised number, owner, or timeline for the target decision.

## Findings

| # | Severity | Perspective | Where | Problem | Consequence if unfixed | Required fix |
|---|---|---|---|---|---|---|
| 1 | **Blocker** | Decision Maker / Logician | §5 "What it adds up to" | The memo frames "revisit target or floor" as a board decision in the header, then resolves it in one buried sentence ("every option that needs a lower floor also carries the weakest evidence") that doesn't hold up — suburban's 13.1% is a real P&L number and franchising rests on three actual offers, neither is "weak" relative to anything else in the memo. No revised target figure, owner, or date is proposed. | The board walks in thinking it's approving budget, then has to improvise a number for the one open strategic question the memo itself raised — exactly the failure mode of a recommendation that "jumps" rather than directs. | Move the recommendation on decision 2 into the lead paragraph. Replace "we recommend revisiting the target" with a specific proposal: e.g., "lower the 2031 target to EUR 74–76m, owned by [CFO/CEO], confirmed by [date], because lowering the floor to accommodate suburban or franchising would [state the real cost — brand/quality risk, franchisee economics, etc.], which we judge worse than a lower target." |
| 2 | Major | Logician | §3 vs §2 | Suburban stores are excluded for sitting 0.9pp below the 14% margin floor. Catering — the memo's largest ask — runs at 10%, 15%, 18%, 19% margin in years 1–4, below the same floor in year 1 and barely above it in year 2. The memo never explains why the floor applies to one and not the other. | A board member applies the floor consistently and asks why a worse-than-suburban-margin business is being funded while suburban is excluded on the same metric — undermines confidence in the floor itself as a decision rule. | Add one line distinguishing mature-store margin (the floor's intended target) from new-venture ramp-up margin, and state the year catering's margin clears 14% on its own trajectory. |
| 3 | Major | Evidence Auditor | §3 | Franchising is rejected because royalty (6–8%) "would cut store margin below the floor" — but the baseline margin of the stores being franchised is never given, so the claim can't be checked. | A sharp board member asks "below the floor from what starting margin?" and the rejection can't be defended on the spot. | State the pre-royalty margin of the candidate stores so the post-royalty math is visible (e.g., "20% margin − 8% royalty = 12%, below the 14% floor"). |
| 4 | Major | Evidence Auditor | §3 | Suburban rejection rests on a single year's average margin (13.1%, 2025 P&L) for a 0.9pp gap — no range, no view on whether some suburban sites clear the floor, no view on whether a *new* suburban store's economics differ from the existing average. | A board member asks whether this is close enough to be a modeling-error-sized gap, or whether any suburban sites already clear 14% — the rejection of an entire category rests on a razor-thin, unvalidated average. | Show the spread across existing suburban stores, not just the average, and note whether new-site economics have been separately assessed. |
| 5 | Major | Evidence Auditor | §2 | The catering size-of-prize (EUR 2.5–3.3m, base case EUR 2.9m) is triangulated bottom-up (orders × value) and top-down (office workers × spend/head) — but "catering spend per head" for the top-down leg isn't sourced, and may itself derive from the same 12 interviewed office managers used for the bottom-up EUR 190 median. If so, this is one data source counted twice, not two independent ones. | The EUR 1.2m investment's headline justification (two independent methods agreeing) collapses to one method dressed up as two — the central evidentiary claim for the biggest ask in the memo. | State the source of the "catering spend per head" top-down input explicitly and confirm it's independent of the 12-manager interview sample. |
| 6 | Major | Evidence Auditor | §2 | The 12 office managers interviewed aren't described: how chosen, whether existing customers only, whether any non-customers or dissenters are included. | A board member asks whether this is 12 happy existing accounts or a representative sample, directly affecting how much weight the EUR 190 median and the "slow delivery is the main pain" finding can bear. | Add one line on sample composition and selection method. |
| 7 | Major | Outsider / Logician | §2 | The pilot's success bar is stated twice, inconsistently: "reach 60 orders per day" (no date given) in the rationale, vs. "stay below 50 orders per day after month six" as the kill criterion. Not reconciled — unclear if 50 and 60 are a ramp (interim vs. final) or a contradiction. | At the end of the 12-month pilot, two different numbers can be cited to argue for or against the EUR 0.6m rollout — exactly the ambiguity a go/no-go gate exists to prevent. | State one explicit threshold per checkpoint (e.g., "≥50/day by month 6, ≥60/day by month 12") so the gate is unambiguous. |
| 8 | Major | Skeptical CFO | §4 | The EUR 12.7m gap to the 2031 target is computed by holding the existing EUR 62m base flat through 2031 — this assumption is never stated or flagged. | If the base business is expected to grow or shrink on its own, the EUR 12.7m gap — the number driving the "revisit target or floor" decision — is wrong in either direction, and the board is deciding on an unstated assumption. | State explicitly whether the EUR 62m base is assumed flat, and if so, why; if not, show the base-case trajectory used. |
| 9 | Minor | Evidence Auditor | §5 | The EUR 1.1m (price) and EUR 0.9m (hours) figures have no stated basis (e.g., EUR 1.1m implies the 3% increase applies to only ~60% of revenue) — doesn't change the recommendation since both are explicitly secondary and insufficient either way. | — | Add the revenue base each percentage is applied to. |

## Numbers that do not tie
None found — EUR 2.9m + EUR 2.4m = EUR 5.3m, 5.3/62 = 8.5%, 62×1.085 → gap of EUR 12.7m to EUR 80m, and "less than a quarter of the gap" (EUR 2.0m / EUR 12.7m ≈ 16%) all check out. The catering payback math (32% contribution minus EUR 0.35m fixed, against EUR 1.6m/2.1m/2.5m/2.7m revenue) also recomputes cleanly to EUR 0.16m/0.32m/0.45m/0.51m and a fourth-year payback on EUR 1.2m. This is a well-tied memo arithmetically — the problems are in unstated assumptions and unverifiable inputs, not bad math.

## Missing outside view
- **Catering growth to 2031:** delivery cites two regional chains' annual reports; catering has no equivalent external benchmark — only Brightwell's own bottom-up/top-down estimate (see finding 5).
- **Suburban store margin:** no comparison to what new bakery openings elsewhere in comparable markets achieve; only one year of Brightwell's own average.
- **40% framework-agreement conversion threshold:** no stated basis for why 40% in six months is the right bar for B2B catering contracts.

## Premortem
1. Catering demand doesn't convert to signed agreements (sub-40%), but Brightwell has already committed EUR 1.2m in capex plus EUR 0.35m/year in staff and rent with no stated exit or repurposing plan for the kitchen — not addressed.
2. The delivery rollout decision in 2028 turns on cannibalization against "comparable non-pilot stores," but the matching method for those comparables is never defined — the board approves a go/no-go rule it can't actually audit — not addressed.
3. Both launches draw on the same two functional owners (Head of Operations, Head of Digital) who also run the existing EUR 62m business day-to-day; no resourcing or contingency is mentioned if either launch slips — not addressed.

## What is good and must survive
- Decision 1's recommendation is genuinely actionable: named owner, amount, date, and scope for both catering and delivery — this is the bar the rest of the memo (and decision 2) should be held to.
- Real triangulation effort: bottom-up/top-down for catering, two named regional-chain benchmarks for delivery growth, three actual franchise offers rather than an assumed royalty rate.
- Explicit, falsifiable kill criteria ("what would change our view") — rare and valuable; keep this section, just reconcile the 50/60 orders-per-day inconsistency (finding 7).
- Honest about the shortfall: EUR 5.3m against an EUR 80m target, with the gap stated rather than papered over with optimistic pricing/hours assumptions that the memo itself shows don't close it.
- Delivery correctly structured as pilot-then-separate-decision rather than committing to the full 18-store rollout now.

## What "fixed" looks like
"Fund two moves in the 2027 budget: a corporate catering unit (EUR 1.2m, Head of Operations, April 2027) and a twelve-month delivery pilot in eight stores (EUR 0.3m, Head of Digital, March 2027). Do not fund suburban stores or franchising. We also recommend the board lower the 2031 revenue target to EUR 74–76m rather than lower the 14% margin floor: closing the remaining gap would require accepting store economics below what we hold the rest of the estate to, with no comparably strong evidence behind either alternative. [CFO] will bring a specific revised target for sign-off by [date]."


## Files in work dir after run

- pr-03-input.md
