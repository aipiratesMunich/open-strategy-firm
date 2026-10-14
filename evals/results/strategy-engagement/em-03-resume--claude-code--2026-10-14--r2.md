# em-03-resume on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (6/6 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reply reflects content of 00-status.md and 02-hypotheses.md (not only workplan) | yes | Reply states 'Partner gate: passed (gate 2 on v2, release with fixes)' and 'Current answer: unchanged — fund corporate catering and online delivery; no franchising', matching 00-status.md, and references H3 kill / H2 open status from 02-hypotheses.md |
| Reports current answer and hypothesis statuses (confirmed/killed/open), including H3 killed | yes | 'Current answer: unchanged — fund corporate catering and online delivery; no franchising' plus 'contradicting the H3 kill from 2026-10-01' and 'H2 stays open until that data lands' |
| Notices ghost deck still had a franchising page needing removal/rewrite | yes | 'fixed a stale ghost-deck page (p.4 was still claiming franchising added €4m, contradicting the H3 kill from 2026-10-01)' |
| Identifies next open workplan row with highest impact (H2 delivery order growth) as next step | yes | 'Opened workplan row 3 (H2, delivery order growth) and wrote the evidence plan at research/delivery-orders.md.' |
| Notices gate 2 partner review was open and runs it or flags it must run first | yes | 'ran the gate-2 review that was open on the v2 package — verdict Release with fixes (not blocking)' |
| Does not restart engagement or re-ask problem statement questions | yes | Reply continues directly from prior phase state ('Current answer: unchanged...') with no re-litigation of the problem statement |

## Transcript

## Turn 1

**User:** Where are we on the Brightwell engagement? Continue. (Attached in the working directory: engagement/brightwell/.)

**Phase 4 in progress: Gather and analyse**
- **Current answer:** unchanged — fund corporate catering and online delivery; no franchising.
- **Changed since last phase:** fixed a stale ghost-deck page (p.4 was still claiming franchising added €4m, contradicting the H3 kill from 2026-10-01); ran the gate-2 review that was open on the v2 package — verdict **Release with fixes** (not blocking), two majors carried to synthesis: bridge the €6m+ catering/delivery number to the full €62m→80m target, and name H2's sample/comparable set once data arrives. Opened workplan row 3 (H2, delivery order growth) and wrote the evidence plan at `research/delivery-orders.md`.
- **Partner gate:** passed (gate 2 on v2, release with fixes).
- **Next:** workplan row 3 is blocked on client data. Need from you: pilot-store delivery order counts/revenue (weekly or monthly, since launch), delivery platform commission terms, pilot-store P&L before/after delivery launch, and any comparable-chain delivery-growth benchmarks your market team already holds — full list in `research/delivery-orders.md`. I didn't estimate a delivery growth rate from general impressions; H2 stays open until that data lands. Separately, rows 1 and 3 (H1, H3) are marked "done" in the workplan but have no backing `research/` file — worth backfilling before gate 3 so the evidence auditor has something to check.


## Files in work dir after run

- engagement/brightwell/00-status.md
- engagement/brightwell/01-problem-statement.md
- engagement/brightwell/02-hypotheses.md
- engagement/brightwell/03-ghost-deck.md
- engagement/brightwell/04-workplan.md
- engagement/brightwell/research/delivery-orders.md
- engagement/brightwell/reviews/gate2-v2.md

## File written by the run: engagement/brightwell/00-status.md

# Engagement status: Brightwell Bakeries, two growth moves for the 2027 budget

*Fictional company. All figures invented for evaluation.*

| Phase | Artefact | Status | Owner | Partner gate |
|---|---|---|---|---|
| Frame | Problem statement | approved 2026-09-12 | EM | passed |
| Structure | Issue tree, hypotheses, ghost deck | v2 | EM | passed, gate 2 on v2, 2026-10-14 (release with fixes) |
| Plan | Workplan | v2 | EM | passed, gate 2 on v2, 2026-10-14 (release with fixes) |
| Analyse | Analyses per branch | 2 of 5 done, row 3 (delivery) started 2026-10-14 | | |
| Synthesise | Storyline, executive summary | not started | | |
| Review | Partner review | | | |
| Decide | Board, 12 November 2026 | | | |
| Hand over | Implementation plan | | | |

**Current best answer (v2):** Fund corporate catering and online delivery; no franchising.
**Biggest open risk:** delivery order growth may be far below plan.
**Fixed this session:** ghost deck p.4 corrected — it contradicted killed H3 by still claiming franchising added EUR 4m; now states the ruling-out reason.
**Carried forward from gate 2 (not blocking, due by synthesis):** (1) exec summary must bridge EUR 6m+ to the full EUR 62m→80m target; (2) H2's test needs a named sample size and comparable-chain set.
**Next decision needed from the client:** none. **Data needed (blocking workplan row 3, due 2026-10-20):** pilot-store delivery order counts/revenue by week or month since launch, delivery platform commission terms, pilot-store P&L before/after delivery launch, and any comparable-chain benchmarks the client's market team already holds. Full request list in [research/delivery-orders.md](research/delivery-orders.md).


## File written by the run: engagement/brightwell/02-hypotheses.md

# Hypotheses

**Current answer (v2, 2026-10-02):** Fund corporate catering and online delivery; no franchising.

| # | Hypothesis | Impact | Uncertainty | Test | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H1 | Catering can reach at least EUR 2.5m revenue by 2031 | high | medium | order data + 12 office interviews | below EUR 1.5m in both estimates | confirmed (EUR 2.5-3.3m) |
| H2 | Delivery orders can grow at least 15% a year for five years | high | high | pilot-store order data, comparable chains | below 8% a year | open — evidence plan written, data requested, see [research/delivery-orders.md](research/delivery-orders.md) |
| H3 | Franchising adds at least EUR 4m by 2031 within the margin floor | medium | high | 3 franchise-operator interviews | royalties push store margin below 14% | killed 2026-10-01 |
| H4 | Suburban stores can be lifted above 14% margin | low | medium | store P&L | no store above 14% after rent reset | open |

**Change log:** v1 → v2: franchising killed after operator interviews.


## File written by the run: engagement/brightwell/03-ghost-deck.md

# Ghost deck v2

| # | Section | Action title | Status |
|---|---|---|---|
| 1 | Executive summary | Catering and delivery can add EUR 6m+ by 2031 within the margin floor | hypothesis |
| 2 | 1. Catering | Office catering tripled without sales effort and can reach EUR 3m by 2031 | proven |
| 3 | 2. Delivery | High-street stores can carry a profitable delivery business | hypothesis |
| 4 | 3. Franchising | Franchising is ruled out: operator royalties would push store margin below the 14% floor | proven (negative) |
| 5 | 4. Stores | Suburban expansion does not pay back under current rents | partly |

**Change log:** v1 → v2: page 4 rewritten from "franchising adds EUR 4m" (hypothesis) to the ruled-out finding, to match H3 killed 2026-10-01.


## File written by the run: engagement/brightwell/04-workplan.md

# Workplan v2

| # | Analysis | Tests | Effort (days) | Due | Status |
|---|---|---|---|---|---|
| 1 | Catering bottom-up and top-down sizing | H1 | 3 | 2026-09-26 | done |
| 2 | Franchise operator interviews | H3 | 2 | 2026-10-01 | done |
| 3 | Delivery order growth: pilot-store data and comparable chains | H2 | 4 | 2026-10-20 | data requested, see research/delivery-orders.md — blocked on client data |
| 4 | Suburban store rent-reset scenario | H4 | 2 | 2026-10-24 | open |
| 5 | Combined business case | all | 3 | 2026-10-30 | open |


## File written by the run: engagement/brightwell/research/delivery-orders.md

# Research: delivery order growth (H2), 2026-10-14

**Hypothesis:** Online delivery orders from Brightwell high-street stores can grow at least 15% a year, 2027-2031.
**Kill criterion:** Growth comes in below 8% a year (both in Brightwell's own pilot and the comparable-chain outside view).
**Verdict:** open; strength: weak (no primary data collected yet — this file is the evidence plan and data request, not a result)
**So what:** H2 cannot be confirmed or killed without the pilot-store order series and at least one outside comparable; both are requested below, due alongside the 2026-10-20 workplan date.

## Findings
*No findings yet. Do not estimate delivery growth from memory or general industry impressions — none of the rows below may be filled until the source in column 3 is in hand.*

| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| — | pending | — | — | — | — | — | — |

## Triangulation of decisive claims
Cannot be run until at least two independent sources exist (pilot data + one outside comparable). Planned pairing below.

| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Delivery order growth, Brightwell pilot stores, year-on-year | Brightwell's own pilot-store order counts (ask client, see data request 1) | Comparable bakery/QSR chain delivery ramp-up after launch (ask client's market/strategy team for any trade-body or case-study material they hold; do not source externally without web access) | to confirm once both exist | not yet available | — |

## Outside view
| Forecast | Reference class | Range achieved | Where this case sits and why |
|---|---|---|---|
| 15%/year delivery order growth for 5 years | Bakery/QSR chains launching first-party or aggregator delivery from a high-street footprint | **ASSUMPTION — not verified.** Needs a named comparable set; do not state an industry figure from memory | Cannot place Brightwell until a comparable set is named (data request 2) |

## Counter-evidence
- H4's suburban-store economics (rent resets not paying back under current terms) suggest Brightwell's margin discipline may not extend to funding delivery-platform commissions (typically 15-30% of order value) at the pilot stores either — this would cap net margin even if gross order volume hits 15%. Needs checking against pilot P&L (data request 1) before H2 can be called confirmed on revenue growth alone; growth in orders is not the same test as growth within the 14% margin floor.
- No evidence yet that contradicts the 15% figure directly, because no data has been collected. Flag: this absence is a gap, not a clean sheet.

## Assumptions and gaps
| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| Pilot-store delivery order growth to date | missing | none — do not assume a rate | Brightwell order-management system export, weekly or monthly, since pilot launch | Client (ops/digital lead) |
| Comparable-chain delivery ramp-up rate | missing | none — do not assume a rate | Named case studies or trade-body data the client's own market team holds, or a scoped desk-research pass if web access is enabled for this engagement | Client market/strategy team, or EM with web access |
| Delivery platform commission rate at pilot stores | missing | none | Pilot-store P&L or platform contract | Client (finance) |
| Capacity ceiling (kitchen throughput, rider/courier availability) before service quality or margin erodes | missing | none | Pilot-store operations data, interview with store managers | Client (ops) |
| Cannibalisation of in-store sales by delivery orders | missing | none | Pilot-store revenue by channel, same-store sales before/after delivery launch | Client (finance) |

## Data requests
| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| Pilot-store delivery order counts and revenue, by week or month, since launch | Spreadsheet export | Decisive claim: actual Brightwell order growth rate — the core test of H2 | If unavailable, interview pilot store managers for a directional estimate, labelled as unverified, wide range | Client (ops/digital lead) |
| Delivery platform contract terms (commission %, minimum order, delivery radius) | Contract or summary | Needed to test growth *within the margin floor*, not just order-count growth | Ask finance for the effective blended commission rate from the P&L | Client (finance) |
| Any case studies, trade-body benchmarks or comparable-chain data already held by Brightwell's market/strategy team | Document or interview | Outside view for the 15%/8% thresholds | If none held, EM scopes a desk-research pass (needs web access) or runs structured interviews with 2-3 comparable-chain operators (parallel to the H3 franchise-operator interview approach) | Client market/strategy team, or EM |
| Pilot-store P&L, before and after delivery launch | Spreadsheet | Tests cannibalisation and net margin impact, not just gross order growth | Store manager interview as a stopgap, labelled unverified | Client (finance) |

## Interview guide (if order data is incomplete or needs interpretation)
1. Pilot store managers (aim: 3-5, one per pilot store) — order volume trend by month, capacity constraints, customer mix (new vs. existing), anything that changed mid-pilot (menu, platform, staffing).
2. Digital/delivery operations lead (1) — platform economics, what Brightwell controls vs. the aggregator, planned changes for 2027-2031.
3. Do not conduct these until the pilot order-data export (data request 1) has been requested; the interviews interpret the data, they do not substitute for it.


## File written by the run: engagement/brightwell/reviews/gate2-v2.md

# Partner review: hypotheses v2 + ghost deck v2 + workplan v2, 2026-10-14, gate 2

**Verdict:** Release with fixes

**One-line reason:** The structure answers the question and the franchising contradiction is now fixed in the draft reviewed here, but the executive summary line and the suburban-store page still need to tie to the EUR 80m target before synthesis.

## Findings
| # | Severity | Perspective | Check | Where (page/section) | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Decision Maker | 4 | p.1 exec summary | "EUR 6m+ by 2031" does not show how it closes the EUR 62m → 80m gap (EUR 18m); the deck does not say what carries the rest (base-business growth, price, mix) | At synthesis, add one line bridging EUR 18m target to catering + delivery + base growth, so the board sees the full walk |
| 2 | Minor | Logician | 8 | p.4 franchising | Fixed in this draft (now states the ruling-out reason); keep this wording through to the final deck so the reason for dropping franchising survives | none — confirm at gate 3 that the wording is not reverted |
| 3 | Minor | Evidence Auditor | 11 | 02-hypotheses.md H2 | H2's kill criterion ("below 8% a year") is stated but the pilot-store sample size and number of comparable chains are not yet named | Name sample and comparable set when workplan row 3 is run (next step) |

## Premortem
1. Delivery order growth lands at 8-12%, below the 15% test but above the 8% kill line — an ambiguous middle that the current kill criterion does not resolve. Workplan row 3 should define what happens in that band before the data comes in.
2. Suburban rent resets get agreed with landlords on paper but take longer than 2031 to close, leaving H4 unresolved at decision time.
3. The board reads "no franchising" as leaving money on the table versus a competitor who does franchise; the deck should pre-empt this with the margin-floor arithmetic from the interviews, not just assert it.

## What is good and must survive the rewrite
- The kill criteria are numeric and were actually applied: H3 died on evidence (interviews), not on convenience.
- The day-one answer changed when H3 died (v1 → v2) and the ghost deck line 1 was rewritten to match — that is the discipline this checklist exists to protect.

