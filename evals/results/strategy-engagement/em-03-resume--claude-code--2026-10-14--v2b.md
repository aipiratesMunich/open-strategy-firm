# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md, not only the workplan | yes | "Current answer: unchanged — fund corporate catering and online delivery; no franchising" and "Partner gate: gate 2 passed (with fix applied). No open gates now" both pull from 00-status.md/02-hypotheses.md content, not just the workplan row. |
| Reports current answer, hypothesis statuses (confirmed/killed/open), and that H3 was killed | yes | "Current answer: unchanged — fund corporate catering and online delivery; no franchising" plus "after franchising (H3) was killed" and "so H2 stays open"; H4 flagged as next item. |
| Notices ghost deck still had a franchising page and says it must be removed/rewritten | yes | "the ghost deck still had a page claiming franchising adds EUR 4m. Fixed (ghost deck v3, reviews/gate2-v2.md, gate now passed)" |
| Identifies next open workplan row with highest impact (H2 delivery order growth) as next step | yes | "Started the next workplan row (#3, H2 — delivery order growth)" |
| Notices gate 2 was open/stale and runs it or says it must run first | yes | "caught and fixed a stale gate — gate 2 hadn't been re-run on v2..." followed by "gate 2 passed (with fix applied)" |
| Must not restart engagement from beginning or re-ask problem statement questions | yes | Response opens with "Phase 4 in progress: Gather and analyse" continuing from where work left off, with no re-asking of problem-statement questions. |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

**Phase 4 in progress: Gather and analyse**
- Current answer: unchanged — fund corporate catering and online delivery; no franchising.
- Changed since last phase: caught and fixed a stale gate — gate 2 hadn't been re-run on v2 of the hypotheses/ghost-deck/workplan after franchising (H3) was killed, and the ghost deck still had a page claiming franchising adds EUR 4m. Fixed (ghost deck v3, `reviews/gate2-v2.md`, gate now passed). Started the next workplan row (#3, H2 — delivery order growth), but WebSearch wasn't authorized this session, so I could not pull real comparable-chain benchmarks, and there's no pilot-store order data on file — so H2 stays open rather than being filled with invented numbers.
- Partner gate: gate 2 passed (with fix applied). No open gates now.
- Next: need from you — (1) pilot-store delivery order data, or confirmation none exists yet, (2) the delivery platform's commission terms, (3) whether I'm clear to use web search for comparable-chain delivery-growth benchmarks (Greggs/Pret/Costa-type rollouts). Once I have any of those, I'll finish the H2 branch, then move to H4 (suburban rent-reset, due 2026-10-24) and the combined business case.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/research/delivery-order-growth.md
- engagement/brightwell/reviews/gate2-v2.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v2 / deck v3 | EM | passed (gate 2 on v2/v3, 2026-10-14, Return → fixed: see reviews/gate2-v2.md) |
| Plan | Workplan | v2 | EM | passed (gate 2, 2026-10-14) |
| Analyse | Analyses per branch | 2 of 5 done, #3 in progress | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v2):** Fund corporate catering and online delivery; no franchising.
**Biggest open risk:** delivery order growth may be far below plan.
**Next decision needed from the client:** (1) share pilot-store delivery order data (or confirm none exists); (2) confirm delivery platform commission terms; (3) authorise web search for comparable-chain delivery-growth benchmarks. See research/delivery-order-growth.md.


## File written by the run: engagement/brightwell/02-hypotheses.md

# Hypotheses

**Current answer (v2, 2026-10-02):** Fund corporate catering and online delivery; no franchising.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Catering can reach at least EUR 2.5m revenue by 2031 | high | medium | order data + 12 office interviews | below EUR 1.5m in both estimates | confirmed (EUR 2.5-3.3m) |
| H2 | Delivery orders can grow at least 15% a year for five years | high | high | pilot-store order data, comparable chains | below 8% a year | open — no decisive data yet, see research/delivery-order-growth.md |
| H3 | Franchising adds at least EUR 4m by 2031 within the margin floor | medium | high | 3 franchise-operator interviews | royalties push store margin below 14% | killed 2026-10-01 |
| H4 | Suburban stores can be lifted above 14% margin | low | medium | store P&L | no store above 14% after rent reset | open |

**Change log:** v1 → v2: franchising killed after operator interviews.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck v3

| # | Section | Action title | Status |
|---|---|---|---|
| 1 | Executive summary | Catering and delivery can add EUR 6m+ by 2031 within the margin floor | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 3m by 2031 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business | hypothesis |
| 4 | 3. Franchising (ruled out) | Franchising is ruled out: operator royalties push store margin below the 14% floor | killed |
| 5 | 4. Stores | Suburban expansion does not pay back under current rents | partly |

**Change log:** v1 → v2: franchising killed after operator interviews (hypotheses only). v2 → v3: gate 2 review (2026-10-14) found page 4 still presented franchising as value-adding; corrected to a ruled-out page with the kill reason, matching 02-hypotheses.md and 00-status.md.


## File written by the run: engagement/brightwell/research/delivery-order-growth.md

# Research: delivery order growth (H2), 2026-10-14
**Hypothesis:** Delivery orders can grow at least 15% a year for five years (2027-2031) | **Kill criterion:** below 8% a year | **Verdict:** open; strength: weak (no decisive data in hand yet)
**So what:** This is the swing branch — at 15%/year the business case likely clears the EUR 6m target alongside catering; at 8% it likely does not, and the capital earmarked for delivery should be reconsidered. We cannot settle it without pilot-store data and external benchmarks neither of which are in hand this round.

## Findings
| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| — | No client pilot-store order data received yet | — | — | — | missing | n/a | n/a |
| — | No comparable-chain benchmark retrieved yet (web search not authorised this session) | — | — | — | missing | n/a | n/a |

Nothing here is decided yet; the table is empty because no admissible evidence has been collected, not because the branch is settled.

## Triangulation of decisive claims
| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Delivery order growth, 2027-2031 | Pilot-store order data (revealed behaviour, Brightwell's own stores) | Comparable chains that rolled out delivery from a similar base (outside view) | yes, once both are in hand | not yet computable | weak — zero of two approaches populated |

## Outside view
| Forecast | Reference class | Range achieved | Where this case sits and why |
|---|---|---|---|
| Year-on-year delivery order growth for a bakery/cafe chain in its first 3-5 years on a delivery platform | UK/EU bakery, cafe and QSR chains that added third-party delivery to an existing store estate (candidates to check: Greggs' delivery rollout via Just Eat/Uber Eats, Pret a Manger delivery, Costa Coffee delivery, Domino's as a mature high-frequency delivery comparator) | **ASSUMPTION — not verified.** I have not retrieved sourced figures for any of these; do not treat any growth rate I could state from memory as fact. | Brightwell is earlier-stage (high-street stores, no existing delivery infrastructure) than Domino's (delivery-native), so Domino's growth rates are likely a ceiling, not a central estimate. Greggs/Pret/Costa are the closer comparators by format and starting point. |

## Counter-evidence
Not yet searched. Specifically worth checking once data access is available: cases where chain delivery rollouts plateaued or reversed (e.g. third-party platform commission increases cutting store-level margin and causing chains to pull back on delivery promotion, or delivery cannibalising in-store footfall rather than adding incremental orders). If Brightwell's delivery orders substitute for walk-in purchases rather than adding net new demand, the 15% top-line order growth figure could still be real while store-level profit grows much less — relevant given the 14% margin floor is binding.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Delivery order growth rate, 2027-2031 | missing | none — do not plug a placeholder into the business case | Brightwell pilot-store order data (see data request below) | client |
| Comparable-chain delivery growth benchmarks | unverified | none | Web research with sourced, dated figures (needs search access granted) or desk research the client can supply | EM, once access is granted |
| Net-new vs cannibalised demand split | missing | none | Pilot-store data split by order channel against same-store walk-in sales pre/post delivery launch | client |
| Platform commission rate and its effect on store-level margin | unverified | none | Brightwell's current platform contract terms | client |

## Data requests
| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Pilot-store order data: weekly delivery order counts and value, by store, since delivery launch, plus same-store walk-in sales over the same period | spreadsheet/export | Only revealed-behaviour evidence for H2; also needed to separate net-new orders from cannibalisation | If unavailable for all pilot stores, request for the longest-running 3-5 stores and treat the rest as unverified | client |
| Current delivery platform contract (commission %, any minimum volume terms) | contract excerpt or summary | Determines whether order growth translates into margin-floor-compliant profit | Ask Brightwell's commercial lead for the headline commission rate only if the contract itself is confidential | client |
| Authorisation to use web search for comparable-chain benchmarks | n/a | Needed for the outside-view half of triangulation | Client-supplied desk research or analyst notes on comparable chains' delivery rollouts | client / EM |

**Data requests to the user:** could you share (a) pilot-store delivery order data (or confirm none exists yet, in which case H2 cannot be tested on revealed behaviour and we should say so in the synthesis), and (b) whether I'm clear to use web search for the comparable-chain benchmarks on this topic?


## File written by the run: engagement/brightwell/reviews/gate2-v2.md

# Partner review: hypotheses v2 / ghost deck v2 / workplan v2, 2026-10-14, gate 2

**Verdict:** Return (one fix required, mechanical)

**One-line reason:** Ghost-deck page 4 still presents franchising as a value-adding page even though H3 was killed on 2026-10-01; the deck contradicts the current best answer in 00-status.md ("no franchising").

## Findings
| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician | 5, 6, 8 (Decision Maker check 4 also fails) | 03-ghost-deck.md, row 4 "Franchising adds EUR 4m with no capital from Brightwell" | Page states franchising as a live, value-adding hypothesis. H3 (franchising) was killed 2026-10-01 in 02-hypotheses.md. Read alone, the titles tell two contradictory stories: the exec summary names only catering and delivery, but page 4 still recommends funding franchising. A board member reading the deck would not know franchising is out. | Replace the page with a one-line "ruled out" page carrying the kill reason (royalty economics breach the 14% margin floor), per check 8 (alternatives must be addressed and ruled out with reasons, not silently dropped). |

No other blockers or majors found in hypotheses v2 or workplan v2: H1's kill criterion and confirmed range tie to the stated test; H4 is correctly still open; workplan row 2 (franchise interviews, done) is the analysis that produced the kill and is correctly sequenced before row 5 (combined business case, which must now exclude franchising). Impact/uncertainty ranking and due dates in 04-workplan.md are consistent with H2 being the highest-impact open branch, flagged correctly in 00-status.md as the biggest open risk.

## Premortem
1. Board sees stale franchising language in a later deck draft and asks why it's back on the table after being ruled out — addressed by the fix above.
2. Delivery (H2) comes in between the kill criterion (8%) and the hypothesis threshold (15%) — a "grey zone" outcome the workplan doesn't yet say how to handle. Not a gate-2 blocker (no data yet), but flag for the row-3 analysis to propose a decision rule for a grey-zone result.
3. Combined business case (row 5) is costed before suburban stores (row 4, H4) resolves, understating required capital if H4 fails. Sequencing in 04-workplan.md already runs row 4 before row 5, so this is addressed as planned.

## What is good and must survive the rewrite
- Kill criteria on all four hypotheses are numeric and were set before data (H3's and H1's tests both ran clean against their pre-set thresholds).
- The exec summary title already reflects the no-franchising answer; only the supporting page is stale.
- Workplan sequencing by impact/uncertainty is sound and doesn't need to change.

