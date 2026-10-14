# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md (not only workplan) | yes | Reply cites gate status ('passed 2026-10-14... see reviews/gate2-structure.md'), hypothesis statuses ('Catering (H1) is confirmed... franchising (H3) was killed... delivery growth (H2) and suburban margins (H4) are still open'), going beyond workplan rows. |
| Reports current answer and hypothesis statuses, including H3 killed | yes | "current answer is 'fund corporate catering and online delivery, no franchising.' Catering (H1) is confirmed at EUR 2.5–3.3m; franchising (H3) was killed on the margin test; delivery growth (H2) and suburban margins (H4) are still open" |
| Notices ghost deck still had a franchising page and says it must be removed/rewritten | yes | "The ghost deck (v2) was stale — it still carried franchising as an open 'hypothesis' page eight days after it was killed. Rewritten as v3 with that section marked 'killed'..." |
| Identifies next open workplan row with highest impact (H2 delivery order growth) as next step | yes | "Next step is workplan row 3, delivery order growth (H2), due 2026-10-20" and status.md: "Next open workplan row (highest impact): row 3, delivery order growth (H2)" |
| Notices gate 2 partner review open and runs it or flags it must run | yes | "Gate 2 (hypotheses/ghost deck/workplan) had been sitting open since v2 — ran it now (reviews/gate2-structure.md): verdict release with fixes." |
| Does not restart the engagement from the beginning or re-ask problem statement questions | yes | Reply proceeds directly from current state (status, fixes, next step) with no re-derivation of the problem statement or framing questions. |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

**Where we are:** current answer is "fund corporate catering and online delivery, no franchising." Catering (H1) is confirmed at EUR 2.5–3.3m; franchising (H3) was killed on the margin test; delivery growth (H2) and suburban margins (H4) are still open, due 2026-10-20 and 2026-10-24.

**What I found and fixed on resume:**
- The ghost deck (v2) was stale — it still carried franchising as an open "hypothesis" page eight days after it was killed. Rewritten as v3 with that section marked "killed" and retitled to state the actual finding (royalties breach the 14% margin floor).
- No page anywhere tested whether catering + delivery actually close the full EUR 18m gap from EUR 62m to EUR 80m — I added that as a new ghost-deck section and widened workplan row 5 to compute it explicitly, with any residual gap named.
- Gate 2 (hypotheses/ghost deck/workplan) had been sitting open since v2 — ran it now (`reviews/gate2-structure.md`): verdict **release with fixes**. One minor finding still open: H1 and H3 have no `research/<branch>.md` backing file, just a one-line summary — write those before synthesis.

**Next step** is workplan row 3, delivery order growth (H2), due 2026-10-20 — six days out. I can't run that analysis without real data, so I need from you: pilot-store delivery order counts for the pilot period, and any comparable-chain delivery benchmarks you can point to or share (not something I can source from memory). For row 4 (suburban rent-reset, due 10-24) I'll need store-level P&L, and whether the rent reset is landlord-agreed or only modelled — the premortem flagged lease-renewal timing as a risk to hitting the 2027 budget date.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/reviews/gate2-structure.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | hypotheses v2, ghost deck v3 | EM | passed 2026-10-14 (release with fixes, see reviews/gate2-structure.md) |
| Plan | Workplan | v3 | EM | passed 2026-10-14 (same gate 2 review) |
| Analyse | Analyses per branch | 2 of 5 done | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | gate 2 done; gate 3 not started | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v3):** Fund corporate catering and online delivery; no franchising. Open: whether catering + delivery + base growth close the full EUR 62m -> EUR 80m gap, or leave a residual (new workplan row 5 scope).
**Biggest open risk:** delivery order growth may be far below plan (H2, untested).
**Next decision needed from the client:** none yet to decide; data needed to proceed (see below).

**Fixed this pass (2026-10-14):**
- Ghost deck was stale: section 4 (franchising) was still marked "hypothesis" eight days after H3 was killed. Rewritten in ghost deck v3 as "killed" with the margin-breach finding as the title.
- No page tested whether the plan closes the full EUR 18m revenue gap. Added as ghost deck v3 section 6 and widened workplan row 5 to compute it.
- Gate 2 (hypotheses, ghost deck, workplan) had never been reviewed on v2; run now, verdict release with fixes — see `reviews/gate2-structure.md`. Minor finding still open: H1 and H3 have no research backing file, only a one-line summary in the hypotheses table; write those before synthesis.

**Next open workplan row (highest impact): row 3, delivery order growth (H2), due 2026-10-20.**
Needed from you to run it:
1. Pilot-store delivery order data (daily or weekly order counts, by store, for the pilot period) — to test the 15%/year growth hypothesis against the 8%/year kill threshold.
2. Any comparable-chain delivery benchmarks you have access to or can name (we cannot source market benchmarks from memory; they need a named source).
3. For row 4 (suburban rent-reset, due 2026-10-24): store-level P&L for the suburban stores, and whether rent reset is something landlords have actually agreed to or only modelled — the gate 2 premortem flagged lease-renewal timing as a risk to the 2027 budget date.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck: Brightwell Bakeries, v3, 2026-10-14

**Opening (SCQA)**
- Situation: Brightwell operates EUR 62m of in-store bakery revenue across its home region.
- Complication: The board wants EUR 80m by 2031 with store-level margin held above 14%, and about EUR 3m of capital to deploy.
- Question: Which two growth moves should the board fund in the 2027 budget?
- Answer (governing thought): Fund corporate catering and online delivery; franchising is ruled out.

| # | Section (key line) | Action title (full sentence) | Body sketch (chart/table) | Data source | Workplan row | Status |
|---|---|---|---|---|---|---|
| 1 | Executive summary | Catering and delivery can add EUR 6m+ by 2031 within the margin floor; franchising does not clear the margin floor and is not recommended | Bridge chart: EUR 62m to EUR 80m by source (base growth, catering, delivery, residual gap) | Combined business case | 5 | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 2.5-3.3m by 2031 | Bar chart: catering revenue by year, order data; table: bottom-up vs top-down sizing | Order data + 12 office interviews | 1 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business if order growth holds at 15%+ a year | Line chart: pilot-store delivery orders vs comparable-chain benchmarks | Pilot-store order data, comparable chains | 3 | hypothesis |
| 4 | 3. Franchising (ruled out) | Franchising would add about EUR 4m but pushes store-level margin below the 14% floor once royalties are paid, so is not recommended | Table: modelled margin with and without royalty, by store band | 3 franchise-operator interviews | 2 | killed |
| 5 | 4. Suburban stores (risk check) | Suburban stores do not clear 14% margin even after a rent reset, so are not a growth lever for this plan | Table: store P&L before/after modelled rent reset | Store P&L | 4 | partly |
| 6 | Bridge to target | Catering and delivery combined with base organic growth close most but not all of the EUR 18m gap to EUR 80m; the residual is the board's open question | Waterfall: EUR 62m -> base growth -> catering -> delivery -> EUR 80m, with residual labelled | Combined business case | 5 | hypothesis |

**Titles-only read-through passes:** partial — titles 1 to 5 tell the catering/delivery/no-franchising/no-suburban story; title 6 is new and still needs the actual bridge numbers from workplan row 5 before it can be read as proof rather than placeholder.

**Changes since last version (v2 -> v3):**
- Section 3 (Franchising) rewritten from "hypothesis" to "killed" and retitled to state the actual finding (margin breach), per H3 kill on 2026-10-01. v2 still carried it as an open hypothesis, which was stale.
- Section 5 retitled "risk check" rather than a growth lever, since H4 tests whether existing suburban stores clear the margin floor, not a new revenue source.
- Added section 6, "Bridge to target": no existing page showed whether catering + delivery actually close the full EUR 18m gap (EUR 62m to EUR 80m) implied by the problem statement. This is carried as a placeholder until workplan row 5 produces the number.


## File written by the run: engagement/brightwell/04-workplan.md

# Workplan v3

| # | Analysis | Tests | Effort (days) | Due | Status |
|---|---|---|---|---|---|
| 1 | Catering bottom-up and top-down sizing | H1 | 3 | 2026-09-26 | done |
| 2 | Franchise operator interviews | H3 | 2 | 2026-10-01 | done |
| 3 | Delivery order growth: pilot-store data and comparable chains | H2 | 4 | 2026-10-20 | open |
| 4 | Suburban store rent-reset scenario | H4 | 2 | 2026-10-24 | open |
| 5 | Combined business case: size catering + delivery, add the base organic-growth assumption, and bridge EUR 62m to the EUR 80m target explicitly, naming any residual gap and what would close it | all | 3 | 2026-10-30 | open |

**Changes since v2:** row 5 scope widened — gate 2 review found no existing analysis states whether catering and delivery (plus base growth) actually close the full EUR 18m gap to the EUR 80m target, or leaves a residual the board needs to see.


## File written by the run: engagement/brightwell/reviews/gate2-structure.md

# Partner review: hypotheses v2, ghost deck v3, workplan v3, 2026-10-14, gate 2

**Verdict:** Release with fixes

**One-line reason:** The plan will answer the problem statement if it adds one missing analysis (the full revenue bridge to EUR 80m); the stale franchising page is now fixed.

## Findings
| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Decision Maker (4) | 4 | Ghost deck, exec summary / new section 6 | No page sizes whether catering (EUR 2.5-3.3m) + delivery (unsized) + base organic growth actually close the EUR 18m gap from EUR 62m to EUR 80m; the board will ask this directly | Widened workplan row 5 to compute the bridge explicitly and name any residual gap (done this pass) |
| 2 | Minor | Evidence Auditor (9) | 9 | Hypotheses v2, H1 and H3 | H1 (confirmed) and H3 (killed) have no `research/<branch>.md` backing file — the source, interview count and date live only as a one-line summary in the hypotheses table | Before synthesis, write `research/catering-sizing.md` and `research/franchise-interviews.md` recording sources, dates and the interview sample, even retroactively |
| 3 | Minor | Logician (6) | 6 | Ghost deck v2 (fixed in v3) | Section 4 (franchising) was still marked "hypothesis" eight days after H3 was killed, and the status line still called it open | Rewritten in v3 as "killed" with the actual finding (margin breach) as the title |

## Premortem
1. The board approves catering + delivery, the combined business case later shows a residual gap against EUR 80m that was never surfaced, and the board feels misled at the November meeting. (Addressed by finding 1.)
2. Delivery order growth (H2) comes in below the 8% kill threshold after the budget is already committed, because the pilot-store sample is small or unrepresentative of the stores slated for rollout. Not yet addressed — flag as a question for the workplan row 3 data request below.
3. Suburban rent-reset assumptions (H4) turn out to require landlord agreement that takes longer than the 2027 budget cycle, so the "risk check" page cannot close out before the board meeting. Not yet addressed — worth asking the client about lease renewal timing when requesting store P&L data.

## What is good and must survive the rewrite
- The kill criteria are numeric and were actually applied (H3 killed on a clear margin-breach test, not a soft judgment call).
- The ghost deck already writes titles as findings, not topic labels, and the day-one answer updates each time a hypothesis dies.

