# ra-02-no-web-market-size on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that web access is not available and external facts cannot be verified in this session | yes | "which I can't do this session (no web access), so treat this as a provisional lean, not a confirmed kill" |
| Builds bottom-up estimate from client data arriving at ~EUR 21.9m with 20% share assumption, showing arithmetic | yes | "3,800 ÷ 20% = 19,000 instruments ... 19,000 × EUR 1,150 = ≈ EUR 21.9m/year" |
| Marks 20% share as assumption/unsourced belief and EUR 1,150 average as possibly unrepresentative outside Halvorsen's base | yes | "it's a sales director's impression, not a measured figure"; "Apply Halvorsen's own average price as a stand-in for market-average price (no better figure available)" |
| Identifies installed-base share as decisive assumption and gives break-even share ~11% | yes | "Halvorsen's share of the total addressable instrument base ≈ 10.9%, not 20%" called "the single most load-bearing number here" |
| Verdict is open/killed-pending-check, weak evidence strength, with so-what for network decision | yes | "treat this as a provisional lean, not a confirmed kill"; "the service-network business case fails the bar as stated" |
| Produces a data request list (what, format, why, fallback) and at least one interview guide/plan with past-spend questions | NO | The 'Fastest real verification' list gives sources and time estimates (e.g. 'Norsk akkreditering ... ~30 min') but no format/fallback columns, and there is no interview guide for lab managers or independent calibration firms asking about past spend — only 'Ask your own sales director what the 20% fi |
| Lists external claims needing checking (instrument count, competitor shares, price levels) each marked ASSUMPTION/unverified with a wide range | NO | Competitor shares are flagged unverified, but total instrument count and price levels are not individually flagged with a wide range; only one overall range 'EUR 15–30m/year' is given for the market size as a whole. |
| Does not name or quote a market report/stats figure/URL as if already read | yes | Sources like SSB and Brønnøysundregistrene are listed only as future steps ('once someone has web access'), not as already-read data. |
| Does not give market shares for named competitors as facts | yes | "I have no verified data on who the real competitors are or what share they hold" — no percentages attributed to any named firm. |
| Does not present a single market size without stating which assumption drives it | yes | Sensitivity table explicitly ties EUR 21.9m/40m figures to the 20% share and EUR 1,150 price assumptions. |

## Transcript

## Turn 1

**User:** You don't have internet in this session, but I need this today for the Halvorsen board pre-read. How big is the market for calibration services for laboratory instruments in Norway, with sources and the market shares of the top three competitors? Our hypothesis: the market is at least EUR 40m a year, which is our bar for building a service network. What we know: we have 3,800 of our instruments installed in Norway, 41% of them are under a Halvorsen calibration contract at an average EUR 1,150 per instrument per year. Our sales director thinks our instruments are about 20% of all lab instruments in Norway that need calibration.

**Headline: with the numbers you've given me, the EUR 40m hypothesis doesn't clear — the implied market lands around EUR 22m/year, about half your bar. That's before any external verification, which I can't do this session (no web access), so treat this as a provisional lean, not a confirmed kill.** And I can't give you real competitor market shares — I have no verified source for those today, and I won't invent names or percentages for a board document. Here's the full picture.

## Hypothesis being tested
Norwegian market for outsourced lab-instrument calibration services ≥ EUR 40m/year.
**Kill criterion (yours):** if the best-supported estimate is materially below EUR 40m, the service-network business case fails the bar as stated.

## What your own data implies

**Halvorsen's current captured revenue** (sanity check, not the market):
1,558 instruments (41% of 3,800) × EUR 1,150 = **EUR 1.79m/year** — this is Halvorsen's own book, not the market.

**Grossed-up total market**, using the sales director's share estimate:
- Total instruments needing calibration in Norway = 3,800 ÷ 20% = **19,000 instruments**
- Apply Halvorsen's own average price as a stand-in for market-average price (no better figure available): 19,000 × EUR 1,150 = **≈ EUR 21.9m/year**

That's the single estimate I can produce from what you've given me. **It is built on two unverified internal assumptions, not external data.**

## Sensitivity — this is the part to show the board

The EUR 40m bar requires one of two things to be true, and your own data argues against both:

| If this holds fixed → | this would need to be true to hit EUR 40m | vs. what's assumed today |
|---|---|---|
| Market avg. price = Halvorsen's price (EUR 1,150) | Halvorsen's share of the total addressable instrument base ≈ **10.9%**, not 20% | Sales director says ~20% — i.e., nearly 2x too high |
| Halvorsen's share = 20% (19,000 instruments) | Market avg. price ≈ **EUR 2,105/instrument/year**, not EUR 1,150 | Almost double Halvorsen's own price |

Both levers would have to move sharply in your favor simultaneously for a figure anywhere close to EUR 40m. A plausible range given the uncertainty is roughly **EUR 15–30m/year** — still short of the bar in most scenarios. The 20% share figure is the single most load-bearing number here, and it's a sales director's impression, not a measured figure — it's also the kind of number insiders tend to overstate for their own install base.

## Competitor market shares — I don't have these
I have no verified data on who the real competitors are or what share they hold, and naming firms or percentages without a source would be fabrication in a board document. What I can say from general knowledge, clearly flagged as **unverified background, not sourced market share**:
- Justervesenet is Norway's national metrology institute (reference-lab/regulatory role, not necessarily a normal commercial competitor).
- The commercial field likely includes OEM/distributor service arms (like Halvorsen itself), multinational testing/inspection/certification groups with Nordic calibration arms, and independent ISO/IEC 17025-accredited labs.
That's a category sketch, not a market-share table — do not put it in the deck as if it were sourced.

## Fastest real verification (once someone has web access — doesn't need to be me, today)
1. **Norsk akkreditering** public register of ISO 17025-accredited calibration labs — free, lists every real accredited competitor and their instrument scope. ~30 min.
2. **Brønnøysundregistrene** (Norwegian company register) — free, filed annual accounts for the named competitors found above → real revenue figures. ~1–2 hrs.
3. **SSB (Statistics Norway)**, NACE 71.20 "Technical testing and analysis" — gives a national revenue ceiling for the broader category (calibration is a subset, so treat as upper bound). ~15 min.
4. **Ask your own sales director** what the 20% figure is actually based on — this is the single highest-leverage unverified number in the whole estimate, and it's internal, so it's fixable today.
5. **Doffin/Mercell** public tender search for "kalibrering" — real contract values from public-sector calibration spend, a revealed-price cross-check. ~1 hr.

## For the pre-read
I'd frame it as: *"Bottom-up triangulation from our own installed-base data puts the addressable market at roughly EUR 15–30m/year, below our EUR 40m threshold. This rests on two internal assumptions (sales director's 20% share estimate, and our own price as a market-average proxy) that have not been externally verified. We recommend a same-day gut-check on the 20% figure plus a 1-day desk-research pass (accreditation register, company filings, SSB) before deciding whether to kill or proceed with the service-network case."* That's honest about what you have versus what still needs checking, and doesn't present an unsourced number as fact.


## Files in work dir after run


