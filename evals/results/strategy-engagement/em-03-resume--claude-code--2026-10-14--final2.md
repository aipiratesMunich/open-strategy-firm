# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md (gate status and hypothesis statuses), not only the workplan | yes | "Catering (H1) is confirmed at EUR 2.5–3.3m by 2031. Franchising (H3) was killed 2026-10-01... Delivery (H2...) and suburban stores (H4) are still open" plus gate 2 verdict details — matches 02-hypotheses.md and 00-status.md, not just workplan rows |
| Reports current answer, hypothesis statuses (confirmed/killed/open), and that H3 (franchising) was killed | yes | "Fund corporate catering and online delivery; no franchising. Catering (H1) is confirmed... Franchising (H3) was killed 2026-10-01 — royalties would breach the 14% margin floor" |
| Notices ghost deck still contains a franchising page and says it must be removed/rewritten | yes | "the ghost deck (v2) still had a page pitching franchising as a live 'hypothesis'... a direct contradiction a board member would catch immediately"; gate2-v2.md: "Rewrite page 4 as the ruled-out alternative" |
| Identifies next open workplan row with highest impact (H2 delivery order growth) as next step | yes | "workplan row 3 (delivery order growth, H2 — high impact, high uncertainty, due 2026-10-20) is the next open item by impact" |
| Notices gate 2 partner review marked open and either runs it or says it must run before more analysis | yes | "I ran the gate 2 partner review properly (it had only ever been passed on v1, never re-run on v2 — the workplan file said as much). Verdict: Release with fixes." |
| Does not restart the engagement from the beginning or re-ask problem statement questions | yes | Reply proceeds directly from existing status without re-asking framing/problem-statement questions |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

**Where things stand on Brightwell:**

**Current answer (v2):** Fund corporate catering and online delivery; no franchising. Catering (H1) is confirmed at EUR 2.5–3.3m by 2031. Franchising (H3) was killed 2026-10-01 — royalties would breach the 14% margin floor. Delivery (H2, the biggest open risk) and suburban stores (H4) are still open.

**Found and fixed on resume:** the ghost deck (v2) still had a page pitching franchising as a live "hypothesis" ("Franchising adds EUR 4m...") even though H3 had already been killed and the current answer already excludes it — a direct contradiction a board member would catch immediately. I ran the gate 2 partner review properly (it had only ever been passed on v1, never re-run on v2 — the workplan file said as much). Verdict: **Release with fixes**. Fixed the ghost deck page to state the franchising finding and why it was killed, and recorded the review in `reviews/gate2-v2.md`. Gate 2 is now cleared on v2.

**Moved the top analysis forward:** workplan row 3 (delivery order growth, H2 — high impact, high uncertainty, due 2026-10-20) is the next open item by impact. I couldn't find any pilot-store data or comparable-chain benchmarks in the working directory, and I don't have web access in this session to pull outside-view comparables — so rather than inventing numbers, I wrote up the research plan in `research/h2-delivery-order-growth.md`: the triangulation approach (pilot-store trend + comparable-chain outside view), counter-evidence checks to run (adoption-curve flattening, promo-driven growth, footfall cannibalisation), and a concrete data request list.

**What's needed from you to unblock H2:** Brightwell's pilot-store delivery order counts/revenue by month (or, failing that, three store-manager interviews as a weaker fallback), the pilot-store selection basis, and delivery cost-per-order — all itemized in the data-requests table. Workplan row 5 (combined business case) depends on this, so it's the critical path to the 2026-10-30 deadline and the 12 November board date.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/research/h2-delivery-order-growth.md
- engagement/brightwell/reviews/gate2-v2.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v2 | EM | passed (gate 2 on v2, 2026-10-14, release with fixes — ghost deck franchising page fixed) |
| Plan | Workplan | v2 | EM | passed (gate 2 on v2, 2026-10-14) |
| Analyse | Analyses per branch | 2 of 5 done; #3 (delivery) in progress | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v2):** Fund corporate catering and online delivery; no franchising.
**Biggest open risk:** delivery order growth may be far below plan.
**Next decision needed from the client:** provide pilot-store delivery order data (see `research/h2-delivery-order-growth.md` data requests) so H2 can move from open to confirmed/killed.


## File written by the run: engagement/brightwell/02-hypotheses.md

# Hypotheses

**Current answer (v2, 2026-10-02):** Fund corporate catering and online delivery; no franchising.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Catering can reach at least EUR 2.5m revenue by 2031 | high | medium | order data + 12 office interviews | below EUR 1.5m in both estimates | confirmed (EUR 2.5-3.3m) |
| H2 | Delivery orders can grow at least 15% a year for five years | high | high | pilot-store order data, comparable chains | below 8% a year | open |
| H3 | Franchising adds at least EUR 4m by 2031 within the margin floor | medium | high | 3 franchise-operator interviews | royalties push store margin below 14% | killed 2026-10-01 |
| H4 | Suburban stores can be lifted above 14% margin | low | medium | store P&L | no store above 14% after rent reset | open |

**Change log:** v1 → v2: franchising killed after operator interviews. 2026-10-14: gate 2 re-run on v2 (release with fixes — ghost deck franchising page corrected); H2 research opened, see `research/h2-delivery-order-growth.md` — blocked on pilot-store data request to Brightwell ops.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck v2

| # | Section | Action title | Status |
|---|---|---|---|
| 1 | Executive summary | Catering and delivery can add EUR 6m+ by 2031 within the margin floor | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 3m by 2031 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business | hypothesis |
| 4 | 3. Franchising | Franchising is ruled out: operator royalties would push store margin below the 14% floor | killed |
| 5 | 4. Stores | Suburban expansion does not pay back under current rents | partly |


## File written by the run: engagement/brightwell/04-workplan.md

# Workplan v2

| # | Analysis | Tests | Effort (days) | Due | Status |
|---|---|---|---|---|---|
| 1 | Catering bottom-up and top-down sizing | H1 | 3 | 2026-09-26 | done |
| 2 | Franchise operator interviews | H3 | 2 | 2026-10-01 | done |
| 3 | Delivery order growth: pilot-store data and comparable chains | H2 | 4 | 2026-10-20 | in progress — data requested, see `research/h2-delivery-order-growth.md` |
| 4 | Suburban store rent-reset scenario | H4 | 2 | 2026-10-24 | open |
| 5 | Combined business case | all | 3 | 2026-10-30 | open |


## File written by the run: engagement/brightwell/research/h2-delivery-order-growth.md

# Research: H2, delivery order growth, 2026-10-14

**Hypothesis:** Online delivery orders from existing high-street stores can grow at least 15% a year, compounded, for the five years 2027–2031.
**Kill criterion:** Growth comes in below 8% a year in both the pilot-store trend and the comparable-chain outside view.
**Verdict:** open; strength: weak (no decisive evidence collected yet — this branch has not been run, only planned)
**So what:** Cannot yet say whether delivery clears the bar that the EUR 6m+ exec-summary number needs it to clear; the two data sources below are what would decide it, and neither is in hand.

## Findings
| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| — | No findings yet. | — | — | — | — | — | — |

No client pilot-store order data and no comparable-chain benchmark have been supplied in the working directory, and this session has no web access to pull external comparables. Nothing below is a result — it is the plan for getting one.

## Triangulation of decisive claims
| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Delivery order growth, existing stores, 2027–2031 | Pilot-store order data (client) — not yet supplied | Comparable bakery/café/QSR chain delivery growth (desk research) — not yet pulled | Yes, once both exist | ASSUMPTION: 8–20%/year, placeholder only | weak |

## Outside view
| Forecast | Reference class | Range achieved | Where this case sits and why |
|---|---|---|---|
| 15%/year compounded delivery growth, 5 years | Comparable bakery/café chains' delivery or click-and-collect programmes | Not yet researched — do not state a figure from memory | To be filled once desk research or an interview source is available; flag any figure found as needing a source, date and URL before it goes in the model |

## Counter-evidence
Not yet searched. When the pilot data arrives, explicitly check for: order growth concentrated in the first 2–3 pilot months then flattening (adoption curve, not a trend); growth driven by discount promotions that will not continue; cannibalisation of in-store footfall rather than incremental revenue.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Pilot-store delivery order volumes, monthly, since pilot launch | missing | n/a | Client order-management export, by store, by month | Brightwell ops |
| Number and selection basis of pilot stores (representative of the high-street estate or not) | missing | n/a | Store list with footfall/catchment comparison to full estate | Brightwell ops / EM |
| Comparable chain delivery growth rates | missing | 8–20%/year used as a placeholder bracket only, not a finding | Desk research (trade press, operator annual reports) once web access is available, or a named comparable the client can point to | EM |
| Capex/opex per store to run delivery (packaging, platform fees, extra staffing) | missing | n/a | Needed for workplan row 5 (combined business case) and the EUR 3m capital constraint — request alongside order data | Brightwell finance |

## Data requests
| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Pilot-store delivery order counts and revenue, monthly, from pilot start to today | CSV/export, one row per store per month | Primary trend data for H2; the only way to confirm or kill the 15%/year threshold from client-side evidence | If unavailable, run the 3 store-manager interviews below as a weaker single-source substitute and mark the verdict strength "weak" | Brightwell ops |
| List of pilot stores with footfall tier (high-street/suburban) and launch date | Table | Needed to check whether pilot stores are representative before extrapolating to the full estate | Treat extrapolation as a wide range if store selection is unknown or biased | Brightwell ops |
| Platform/delivery cost per order (own-fleet or third-party platform commission) | Table or rate card | Feeds the margin-floor check (14%) and the combined business case, not just the growth-rate question | Use the industry commission range once sourced via desk research, flagged as an assumption | Brightwell finance |
| 3 store-manager interviews on observed demand drivers, repeat-order behaviour, and capacity limits | Interview notes | Qualitative read on whether growth is structural (new customer segment) or one-off (promotion-driven) — needed for the counter-evidence check | None; this is already the fallback | EM |

## Next step
This branch cannot move past "open" without at least one of: the pilot-store export, or the three store-manager interviews. Both are now data requests — see `00-status.md`. Once either lands, rerun this file's Findings, Triangulation and Counter-evidence sections and reach a verdict (confirmed / killed / reshaped) before starting workplan row 5 (combined business case), which depends on it.


## File written by the run: engagement/brightwell/reviews/gate2-v2.md

# Partner review: hypotheses v2, ghost deck v2, workplan v2, 2026-10-14, gate 2

**Verdict:** Release with fixes

**One-line reason:** Structure and workplan correctly reflect the franchising kill, except the ghost deck still pitches franchising as a live hypothesis page — that one page must be rewritten before the team works from this deck.

## Findings
| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Blocker | Logician | 6, 8 | 03-ghost-deck.md, page 4 (Franchising) | Page 4 is titled "Franchising adds EUR 4m with no capital from Brightwell", status "hypothesis" — but H3 was killed 2026-10-01 (royalties breach the 14% margin floor) and the exec summary / current answer already say "no franchising". The deck contradicts itself. | Rewrite page 4 as the ruled-out alternative: state the finding and the reason it was killed, status "killed". |
| 2 | Minor | Decision Maker | 1 | 00-status.md | Structure row says "passed (gate 2 on v1)" while Plan row says "open (v2 not reviewed)" for the same v2 change set (the franchising kill). Reads as if structure is cleared but plan isn't, when both need the same re-review. | Record this gate 2 v2 review for both rows once fixes land. |

## Premortem
1. Board asks "I thought franchising was ruled out — why is it still a page in this deck?" — covered by finding 1 once fixed.
2. Delivery (H2) comes in below 8%/year and no fallback move is costed — not yet addressed; this is why workplan row 3 is the next step, not a finding against v2 itself.
3. Catering's EUR 2.5–3.3m confirmed range gets rounded up to EUR 3m+ in later pages without the range — watch for this at synthesis, not a blocker now.

## What is good and must survive the rewrite
- Kill criteria are numeric and were applied correctly (H3 killed on a clear, stated threshold).
- Workplan row order (delivery before suburban stores) matches impact and uncertainty ranking.
- Current answer was updated the same day the hypothesis died, not left stale.

