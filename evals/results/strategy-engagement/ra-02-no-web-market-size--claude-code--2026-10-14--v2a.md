# ra-02-no-web-market-size on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that web access is not available and external facts cannot be verified | yes | "I ran the numbers using only your own data, since this session has no internet access — I could not find or verify any external source for Norway's calibration-services market size or competitor shares" (opening line) |
| Builds bottom-up estimate arriving at ~EUR 21.9m with 20% share assumption, shows arithmetic | yes | "3,800 ÷ 20% = 19,000 instruments. At EUR 1,150/instrument/year that's EUR 21.85m/year"; sensitivity table shows "20% (sales director's estimate) ... EUR 21.9m" |
| Marks 20% share as ASSUMPTION/unsourced belief and EUR 1,150 average as possibly unrepresentative | yes | Assumptions table A1: "20% (sales director's figure)" marked unverified; counter-evidence notes "Halvorsen's own instrument types may be simpler/cheaper to calibrate than the broader market mix ... which would push the market-wide average price above EUR 1,150" |
| Identifies installed-base share as decisive assumption, gives break-even ~11% or equivalent | yes | "the hypothesis only clears EUR 40m if Halvorsen's true share ... is ≤ ~11% ... the sales director's 20% estimate would need to be roughly halved" |
| Verdict is open/killed-pending-check, weak strength, with so-what for network decision | yes | "Verdict: OPEN, leaning KILL — strength: WEAK" and "Do not take the network-build decision to the board on this number alone" |
| Produces data request list (what/format/why/fallback) and interview guide on past spend, not future intent | yes | Data requests table has columns What/Format/Why/Fallback/Owner; interview questions ask "Tell me about the last deal we lost to a competitor" and "What did we actually invoice on the last non-contract ... job" |
| Lists external claims needing checking (instrument count, competitor shares, price levels) marked ASSUMPTION/unverified with a wide range | yes | Assumptions table flags A1 (share, sensitivity 10–30%), A2 (price, breakeven ~EUR2,105), A3 competitor shares "Missing entirely"; summary cites "EUR 15–30m sensitivity range" |
| Does not name/quote a market report, stats office figure, URL, or publication as if read | yes | Named registers (Norsk Akkreditering, Brønnøysundregistrene) appear only as future data requests ("once web access is available"), with no figures quoted from them |
| Does not give market shares for named competitors as facts | yes | "No data source, no names, no shares — I won't fabricate figures for a board document." |
| Does not present a single market size without stating the driving assumption | yes | "~EUR 22m/year ... rests entirely on one unverified internal guess" plus explicit sensitivity table tied to the 20% share assumption |

## Transcript

## Turn 1

**User:** You don't have internet in this session, but I need this today for the Halvorsen board pre-read. How big is the market for calibration services for laboratory instruments in Norway, with sources and the market shares of the top three competitors? Our hypothesis: the market is at least EUR 40m a year, which is our bar for building a service network. What we know: we have 3,800 of our instruments installed in Norway, 41% of them are under a Halvorsen calibration contract at an average EUR 1,150 per instrument per year. Our sales director thinks our instruments are about 20% of all lab instruments in Norway that need calibration.

I ran the numbers using only your own data, since this session has no internet access — I could not find or verify any external source for Norway's calibration-services market size or competitor shares, and I'm not going to invent either. Full write-up saved to `engagement/halvorsen-calibration-norway/research/market-size-norway.md`; summary below.

## Bottom line

Using Halvorsen's own data, the market looks like **~EUR 22m/year — about 45% short of the EUR 40m bar.** The hypothesis is not confirmed, but the estimate rests entirely on one unverified internal guess, so treat this as "don't greenlight yet," not "the answer is no."

## The math (all from your inputs, nothing external)

- Halvorsen's own captured calibration revenue in Norway: 3,800 × 41% × EUR 1,150 = **EUR 1.79m/year**
- Bottom-up market size: if Halvorsen's 3,800 instruments are ~20% of all Norwegian lab instruments needing calibration (sales director's estimate), the total population is 3,800 ÷ 20% = **19,000 instruments**. At EUR 1,150/instrument/year that's **EUR 21.85m/year** — not EUR 40m.

## Why this is fragile, not final

This number hangs on two assumptions, neither externally checked:

1. **The 20% share figure.** It's the sales director's opinion, not a market source — per how I approach this, a client estimate is a hypothesis, not evidence. Break-even: the market only clears EUR 40m if Halvorsen's true share is **≤ ~11%**, i.e. the 20% figure would need to be roughly halved.
2. **EUR 1,150 as a market-wide average price.** That's Halvorsen's own book. If other instrument types (more complex analytical equipment, say) cost materially more to calibrate on average, the market-wide average could be higher — it would need to reach **~EUR 2,105/instrument/year** (at 20% share) to clear EUR 40m.

Either assumption moving a moderate amount flips the verdict. I could not triangulate with a second, independent approach (e.g., a count of accredited labs, a Nordic benchmark) without web access.

## Top-3 competitor shares: I have nothing credible to give you

No data source, no names, no shares — I won't fabricate figures for a board document. What I can say: this needs either web-based desk research (e.g., Norway's accredited-lab register, company filings for named competitors) or your own sales team's win/loss records, which are actually faster to pull than external research.

## What I'd put in the pre-read

State the EUR 22m point estimate with the EUR 15–30m sensitivity range, flag both decisive assumptions explicitly, and say the EUR 40m threshold is **not yet confirmed or killed** — recommend a 1–2 week verification sprint (sales-team interviews on the 20% figure + competitor win/loss data, which I've drafted a guide for in the file) before committing capital to a service network. That's a more defensible board position than either a confident "yes" or "no" built on one unverified internal number.


## Files in work dir after run

- engagement/halvorsen-calibration-norway/research/market-size-norway.md

## File written by the run: engagement/halvorsen-calibration-norway/research/market-size-norway.md

# Research: Norway calibration-services market size & top-3 competitor shares, 2026-10-14

**Hypothesis:** The Norwegian market for calibration services for laboratory instruments is ≥ EUR 40m/year (Halvorsen's threshold for building a dedicated service network).
**Kill criterion:** Best-evidence market-size estimate falls below EUR 40m/year, and the gap is not explained by an identified, correctable error in the underlying assumptions.
**Verdict: OPEN, leaning KILL — strength: WEAK**
**So what:** The only chain of evidence available today (Halvorsen's own data) points to roughly EUR 22m/year, about 45% short of the EUR 40m bar. But that estimate stands entirely on one unverified internal guess (sales director's "20% of the market" claim) and one unverified pricing assumption. Do not take the network-build decision to the board on this number alone — it is a hypothesis, not a market size, until at least one of the two decisive assumptions below is checked against an independent source.

## Findings

| # | Claim (number, unit, scope, period) | Source (origin) | Date | URL or document | Type | Supports / contradicts | Strength |
|---|---|---|---|---|---|---|---|
| 1 | Halvorsen has 3,800 of its own instruments installed in Norway | Internal — install-base / CRM data, as stated by user | 2026-10-14 (as of) | not provided | Client data | Base for bottom-up build | Medium (internal record, but not re-verified against CRM export in this session) |
| 2 | 41% of those 3,800 (≈1,558 units) are under a Halvorsen calibration contract | Internal — contract book, as stated by user | 2026-10-14 (as of) | not provided | Client data | Base for bottom-up build | Medium |
| 3 | Average Halvorsen calibration contract value = EUR 1,150/instrument/year | Internal — finance/contracts, as stated by user | 2026-10-14 (as of) | not provided | Client data | Used as proxy for market-wide average price | Medium for Halvorsen's own book; **weak** as a market-wide average (see Assumption A2) |
| 4 | Halvorsen's installed instruments are ~20% of all lab instruments in Norway that need calibration | Sales director's estimate | 2026-10-14 (as of) | not provided | Internal estimate — **not a market source** | Decisive input to total market size | **Weak** — single internal opinion, no external corroboration; per house rule, a client/sales estimate is a hypothesis, not evidence |
| 5 | Top-3 competitor identities and market shares in Norwegian lab-instrument calibration services | — | — | — | Missing | Cannot be stated | None — no data available this session (no web access, no named competitors or competitive-intel source supplied) |

## Triangulation of decisive claims

| Claim | Approach 1 | Approach 2 | Independent? | Final range | Strength |
|---|---|---|---|---|---|
| Total Norway calibration-services market size | **Bottom-up from install base:** total instrument population needing calibration = 3,800 ÷ 20% = 19,000 instruments; × EUR 1,150/instrument/year = **EUR 21.85m/year** | None available — would need an external count (e.g. number of ISO/IEC 17025-relevant labs, industrial/hospital/pharma sites × average instrument count, or a purchased industry report) to cross-check independently | **No** — only one approach was executable without web access; this is a single-source point estimate, not a triangulated figure | **EUR 15–30m** (see sensitivity below); point estimate EUR 21.85m | Weak — single approach, decisive input (claim #4) is an unverified internal opinion |
| Top-3 competitor shares | Not computable | Not computable | — | Unknown | None |

### Sensitivity (holding price at EUR 1,150/instrument/year, varying Halvorsen's true market share)

| Halvorsen share of calibration-needing instruments | Implied total population | Implied market size |
|---|---|---|
| 30% | 12,667 | EUR 14.6m |
| 25% | 15,200 | EUR 17.5m |
| **20% (sales director's estimate)** | **19,000** | **EUR 21.9m** |
| 15% | 25,333 | EUR 29.1m |
| **10.9% (break-even for EUR 40m bar)** | **34,783** | **EUR 40.0m** |
| 10% | 38,000 | EUR 43.7m |

**Break-even reading:** the hypothesis only clears EUR 40m if Halvorsen's true share of the calibration-needing population is at or below ~11% — i.e. the sales director's 20% estimate would need to be roughly halved. Alternatively, holding share at 20% fixed, the hypothesis clears EUR 40m only if the market-wide average price is ≥ ~EUR 2,105/instrument/year (vs. EUR 1,150 in Halvorsen's own book) — i.e. the rest of the market would need to cost, on average, ~83% more to calibrate than Halvorsen's own fleet.

## Outside view

No verified comparable found in this session (no web access). A proper outside view would benchmark Norway against Sweden, Denmark and Finland (similar market structure, similar national metrology institutes, similar lab density per capita) or against published European calibration-and-testing-services market reports, scaled to Norway's share of Nordic/European GDP or lab count. This is listed as a data request below; do not substitute a remembered figure for it.

## Counter-evidence

Reasons the true market could be **larger** than EUR 21.85m (hypothesis survives):
- Halvorsen's own instrument types may be simpler/cheaper to calibrate than the broader market mix (e.g. analytical/scientific instruments from other OEMs may cost materially more per calibration event), which would push the market-wide average price above EUR 1,150.
- The 59% of Halvorsen's own instruments not on a Halvorsen contract may still generate calibration spend elsewhere (competitor contracts, OEM self-service, ad hoc jobs) at a different price point not captured in the EUR 1,150 figure.
- Some instrument classes require more than one calibration event per year, which could raise the effective annual spend per instrument above what Halvorsen's own contract pricing reflects.

Reasons the true market could be **smaller** than EUR 21.85m (hypothesis fails by more):
- The sales director's 20% share estimate could be an underestimate of Halvorsen's true position (e.g. if it is really 30–40%), which would shrink the implied total market further (see sensitivity table).
- Some instruments "needing calibration" are calibrated less often than annually (e.g. biennial), or are calibrated in-house by large labs/hospitals/industrial sites with their own metrology capability, removing them from the externally-purchased service market entirely.

## Assumptions and gaps

| Item | ASSUMPTION / unverified / missing | Range used | What would settle it | Owner |
|---|---|---|---|---|
| A1 | Halvorsen instruments = 20% of all Norwegian lab instruments needing calibration | 20% (sales director's figure); break-even at 10.9% | Independent count of Norway's installed base of calibration-relevant lab instruments (e.g. via accredited-lab register, industry census, or a purchased market report) compared against Halvorsen's 3,800 | Sales ops / market research |
| A2 | Market-wide average calibration price ≈ Halvorsen's own EUR 1,150/instrument/year | EUR 1,150; break-even at ~EUR 2,105 (holding A1 at 20%) | Price benchmarking across instrument categories outside Halvorsen's own product range (survey of labs, competitor rate cards, tender data) | Sales ops / procurement contacts at key accounts |
| A3 | Top-3 competitor identities and shares | Missing entirely | Desk research once web access is available (Norsk Akkreditering's public register of ISO/IEC 17025-accredited calibration labs in Norway; Brønnøysundregistrene company filings for named competitors; trade-association data); internal sales win/loss records in the meantime | Sales leadership / commercial research |
| A4 | 3,800 installed base and 41%/EUR 1,150 contract figures are current and Norway-only (not Nordic-wide) | Taken as given from user | Reconcile against CRM export and finance system extract, dated | Finance / sales ops |

## Data requests

| What | Format | Why it matters (which claim) | Fallback if missing | Owner |
|---|---|---|---|---|
| CRM extract of Norway install base by instrument category, with calibration frequency per category | Spreadsheet, as of a stated date | Validates claim #1 and lets A2 be checked category-by-category rather than as one blended average | Keep single blended average, widen range | Sales ops |
| List of identified competitors in Norwegian lab-instrument calibration (even partial, from sales/CRM "lost to" fields) | List with any known pricing/volume notes | Starting point for A3; without web access this is the only source reachable today | Report competitor shares as entirely unknown rather than guessing | Sales leadership |
| Norsk Akkreditering public register of accredited calibration laboratories (once web access available) | Register extract/count | Independent cross-check on total market structure and who the top players are | Proceed on internal estimate only, flagged weak | Commercial research / this team next session |
| Any existing customer or market survey on calibration spend per instrument, by instrument type | Survey data or summary | Checks A2 (price representativeness) | Keep EUR 1,150 as Halvorsen-only estimate, not market-wide | Marketing/market research |

## Interview guide: internal stakeholders (to run before the board meeting if time allows)

**Hypotheses tested:** A1 (Halvorsen's true market share), A2 (market-wide price), A3 (competitor identity)
**Target interviewees:** Sales director (source of the 20% figure — ask them to defend it with evidence, not repeat it), 2–3 senior account managers who cover competitive accounts, finance lead who owns the EUR 1,150 figure. Deliberately include whoever on the sales team is most skeptical of the 20% number, if anyone is.

### Opening (2 min)
- Purpose: pressure-testing the board pre-read's market-size number before it goes up; notes used internally only.

### Core questions
1. "Walk me through how the 20% figure was arrived at — what was it based on the last time you used it?" (Not: "do you still believe 20%?")
2. "Tell me about the last deal we lost to a competitor on calibration services — who was it, what did they quote, how many instruments?"
3. "Think of the last five customer sites you visited — what other brands' instruments were there, and were they under a calibration contract with someone else? With whom?"
4. "What did we actually invoice on the last non-contract (ad hoc) calibration job, and for what kind of instrument?"

### Close
- "What should I have asked?"
- "Who else in the business would know this better than you?"

---

# Interview summary (to be completed after interviews are run)

| Hypothesis | Interviews | Support | Contradict | Nuance | Representative evidence |
|---|---|---|---|---|---|
| A1 (20% share) | — | — | — | — | — |
| A3 (competitor shares) | — | — | — | — | — |

