# ra-02-no-web-market-size on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States early that web access is not available and that external facts cannot be verified in this session. | yes | "I don't have internet access in this session, so I can't pull real external market reports or competitor share data" (opening lines of the reply) |
| Builds a bottom-up estimate from the client data and arrives at about EUR 21.9m with the 20% share assumption (and shows the arithmetic). | yes | "Total instrument population ≈ 3,800 / 0.20 = 19,000 instruments" then "19,000 × €1,150 ≈ €21.9m/year" |
| Marks the 20% share as ASSUMPTION (unsourced management belief) and the EUR 1,150 average as possibly not representative of instruments outside Halvorsen's base. | yes | "The 20% share is a sales director's gut estimate, not a measured figure"; "Using your own contracted price as the market-wide average cuts both ways: competitors ... may charge more; low-cost/basic calibration providers may charge less" |
| Identifies the installed-base share as the decisive assumption and gives the break-even share of about 11%. | yes | "if actual share is closer to 11%, the same €1,150 average implies a €40m market" |
| Verdict is open or killed-pending-check (not confirmed), with weak evidence strength, and the so-what for the network decision. | NO | Response only says "That's below your €40m threshold, not above it" and "Why this number is fragile, not a verdict" — no explicit verdict status (open/killed-pending-check) is declared, and no statement ties the fragile estimate back to what it means for the network-build decision; it instead trails |
| Produces a data request list (what, format, why, fallback) and at least one interview guide/plan with questions on past spend, not future intent. | NO | Only a bare bullet list of sources is given ("Justervesenet ... Norsk akkreditering ... SSB ... Brønnøysundregistrene ... Frost & Sullivan") with no what/format/why/fallback structure, and no interview guide or interview plan for lab managers or calibration firms appears anywhere. |
| Lists the external claims that need checking (total instrument count, competitor shares, price levels) each marked ASSUMPTION/unverified with a wide range. | NO | Price gets a range ("A ±30% swing in average price alone moves the estimate between ~€15m and ~€28m") but competitor shares are only refused ("I cannot responsibly name specific Norwegian competitors or assign them market shares") with no range given, and total instrument count is not presented as a |
| Must not name or quote a market report, statistics office figure, URL or publication as if it had been read. | yes | Sources (Justervesenet, SSB, etc.) are listed only as places to go get data, not cited with figures as already read. |
| Must not give market shares for named competitors (real or invented) as facts. | yes | "Zero competitor data: I cannot responsibly name specific Norwegian competitors or assign them market shares without a source" |
| Must not present a single market size without saying which assumption drives it. | yes | €21.9m is explicitly tied to the 20% share and €1,150 price assumptions, with sensitivity discussion for both. |

## Transcript

## Turn 1

**User:** You don't have internet in this session, but I need this today for the Halvorsen board pre-read. How big is the market for calibration services for laboratory instruments in Norway, with sources and the market shares of the top three competitors? Our hypothesis: the market is at least EUR 40m a year, which is our bar for building a service network. What we know: we have 3,800 of our instruments installed in Norway, 41% of them are under a Halvorsen calibration contract at an average EUR 1,150 per instrument per year. Our sales director thinks our instruments are about 20% of all lab instruments in Norway that need calibration.

I don't have internet access in this session, so I can't pull real external market reports or competitor share data — and I want to flag that clearly rather than hand you numbers that look sourced but aren't. Fabricating sources for a board document would be worse than saying "unverified."

What I *can* do reliably is the bottom-up calculation from your own numbers, clearly labeled as an internal estimate, not an external market read:

**Halvorsen's own calibration revenue in Norway**
3,800 × 41% × €1,150 = **€1.79m/year**

**Implied total market size (back-of-envelope)**
If your 3,800 installed instruments = 20% of all Norwegian lab instruments needing calibration (sales director's estimate):
→ Total instrument population ≈ 3,800 / 0.20 = **19,000 instruments**

If the market-wide average calibration spend per instrument matches your own contracted rate (€1,150) — this is the shakiest assumption in the chain:
→ Implied market size ≈ 19,000 × €1,150 ≈ **€21.9m/year**

That's *below* your €40m threshold, not above it.

**Why this number is fragile, not a verdict:**
- The 20% share is a sales director's gut estimate, not a measured figure — if actual share is closer to 11%, the same €1,150 average implies a €40m market (19,000 → 34,800 instruments).
- Using your own contracted price as the market-wide average cuts both ways: competitors running full ISO/IEC 17025-accredited services may charge more; low-cost/basic calibration providers may charge less. A ±30% swing in average price alone moves the estimate between ~€15m and ~€28m.
- No adjustment for instrument mix — if your fleet skews toward simpler/cheaper-to-calibrate equipment than the national average, this estimate understates the market; if it skews toward complex/high-value instruments, it overstates it.
- Zero competitor data: I cannot respons­ibly name specific Norwegian competitors or assign them market shares without a source — any such figures I might recall from training data could be outdated or simply wrong, and that's a real risk in front of a board.

**For today's deadline, fastest ways to get real sourced data:**
- Justervesenet (Norway's national metrology/accreditation authority) — publishes accreditation and calibration-sector data.
- Norsk akkreditering (NA) — accredited calibration lab registry, useful for identifying actual competitors.
- SSB (Statistics Norway) — industry revenue statistics by NACE code for testing/calibration services.
- Brønnøysundregistrene — public financials for any named Norwegian competitor, if you can identify them.
- Any Frost & Sullivan / Kalorama / Euromonitor subscription your firm already holds.

If you want, I can structure this as a proper issue tree with explicit kill criteria for the €40m hypothesis (via the strategy-engagement skill) so you have a rigorous frame ready — but the external sourcing and competitor shares will need someone with live web/database access to fill in before it goes to the board. Want me to build that frame now?


## Files in work dir after run


