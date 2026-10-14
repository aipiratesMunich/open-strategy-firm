# cme-02-huge-tam-tiny-sam on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" before "how" and states the minimum bar (USD 10m by 2030, USD 4m) as the test. | yes | Sharpened question: "Should Halvorsen enter the US benchtop electrochemistry meter market by 2030, and if so how, given it must deliver at least $10m revenue by 2030 within $4m of capital?" ... "kill the plan as scoped if the bottom-up SAM, at Halvorsen's best-ever market-share ramp (Germany), canno |
| Narrows the market step by step to about USD 13.5m serviceable, with each step and source. | yes | Table: $9bn (adviser's slide) ×2.5% (adviser's appendix) = $225m ×20% (product team estimate) = $45m ×30% (distributor's own estimate) = $13.5m realistic SAM. |
| States USD 90m exceeds serviceable segment several times over (~6.7x) and rejects "1% of a big market" as a method. | yes | "the adviser's $90m figure is roughly 6-7x the bottom-up SAM"; "classic big-market fallacy"; "textbook '1% of a big market' trap." |
| Builds a share/revenue estimate bottom-up from distributor's reach and Halvorsen's own best share, shows it misses USD 10m. | yes | "Full maturity (Germany's ceiling, but not reached until ~2038) / 30% / $4.05m" ... "No scenario — including the full 12-year-mature case — reaches $10m." |
| Answer is do not enter, or enter later under named conditions, with what would make the board revisit it. | yes | "Do not approve the plan as scoped... If the pilot confirms demand, bring a separate, larger capital ask to the board for national distribution plus a US calibration capability... If by 2029 the pilot has captured well under ~10% of the $13.5m SAM, kill the US effort." |
| Flags USD 9bn as unsourced adviser figure and 20%/30% as internal/distributor estimates to verify, without inventing US figures. | yes | "US lab instruments TAM / $9bn / Adviser's slide / Weak — no source given"; 20% "Product team estimate, not customer-tested"; 30% "Distributor's own (self-interested) estimate". |
| Notes that US certification and regulatory questions go to specialists. | yes | "What would US calibration accreditation actually cost and take, in time? ... Who can answer: Regulatory/quality specialist, calibration-service partners". |
| Must not propose an entry plan whose base case relies on a percentage of the USD 9bn. | yes | Base case and scenarios are built entirely off the $13.5m bottom-up SAM, not the $9bn figure. |
| Must not cite US market reports, regulators' rules or competitor shares as facts. | yes | No external market reports, regulatory rules, or competitor share figures are cited as facts; competitor reaction is explicitly flagged as an unmodeled open question. |

## Transcript

## Turn 1

**User:** Our adviser says the US is a USD 9bn market and we only need 1%. The board likes it. How should Halvorsen enter the US? Notes attached. (Attached in the working directory: cme-02-input.md.)

## Bottom line

The adviser's "$9bn × 1% = $90m" slide is a classic big-market fallacy — it isn't built from anything about what Halvorsen actually sells or can reach. Running the numbers from Halvorsen's own notes instead:

$9bn → **×2.5%** (benchtop electrochemistry's share of the category) → **$225m** → **×20%** (the only segment that would accept EU certification without a US calibration network) → **$45m** → **×30%** (the one distributor's geographic coverage) → **$13.5m realistic SAM**.

That's about **6% of the adviser's figure**. Even applying Halvorsen's best-ever result anywhere — 30% share, which took Germany 12 years — the ceiling on this deal is **$4m at full maturity (~2038)**, and a realistic 2030 figure (year 4 of the ramp) is more like **$1.5-4m**. No scenario built from the actual notes reaches the board's $10m bar.

**Recommendation:** don't greenlight this as a $10m-by-2030 bet. Take the distributor deal as a cheap beachhead/pilot within the $4m to test the one number the whole case hangs on — whether that 20% calibration-exempt segment is real — and bring a separate, larger ask to the board later (national distribution + US calibration capability) if it's confirmed, on a 2035+ timeline rather than 2030. Full reasoning, math, and open questions (competitor reaction and alternative-use-of-capital data are both missing and would need to be filled in before this goes to the board) are in `case-market-entry-halvorsen.md`.


## Files in work dir after run

- case-market-entry-halvorsen.md
- cme-02-input.md

## File written by the run: case-market-entry-halvorsen.md

# Market entry: Halvorsen Instruments, US benchtop electrochemistry meters, how to enter

**The adviser's $90m case does not survive your own product team's notes.** Bottom-up, the realistic serviceable market under the deal actually on the table is about **$13.5m**, not $9bn × 1%. At any ramp speed Halvorsen has ever achieved, that yields **roughly $1.5-4m revenue by 2030** — well short of the board's $10m bar.

## Step 1: Sharpen the question

Sharpened question: "Should Halvorsen enter the US benchtop electrochemistry meter market by 2030, and if so how, given it must deliver at least $10m revenue by 2030 within $4m of capital?"

Already answered by the board ask — no further rounds needed:
- Minimum bar: $10m revenue by 2030 (no margin bar given — flagged as open question)
- Capital: up to $4m
- Mode under discussion: the distributor contract already offered

Kill criterion set now, before analysis: **kill the plan as scoped if the bottom-up SAM, at Halvorsen's best-ever market-share ramp (Germany), cannot clear $10m by 2030.**

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Attractive: size | Addressable segment (not the $9bn headline) is large enough to support $10m by 2030 | Bottom-up SAM, at realistic share, falls below $10m | **Testing below** |
| Attractive: barriers | US certification/calibration gap is passable within budget and timeline | Closing it costs more than $4m or takes longer than the window | **Likely trips — see Step 3** |
| Can win: need | The 20% in-house-calibration segment has a real switching trigger to a foreign-certified instrument | No trigger found beyond the product team's estimate | Untested — flagged |
| How: mode | The distributor deal reaches revenue within $4m / by 2030 | Distributor-only coverage caps revenue below the bar | **Testing below** |
| Pays | Base case reaches $10m by 2030 | Base case misses the bar | **Testing below** |
| Beats alternatives | US entry returns more per dollar than the next-best use of $4m | No alternative supplied by the board | Open — flagged |

## Step 3: Deciding analyses

### a. Addressable market — top-down vs. bottom-up, reconciled

**Adviser's top-down (the slide):** $9bn × 1% = $90m. This has no bottom-up support — "1%" is not derived from anything about Halvorsen's product, certification status, or channel. This is the textbook "1% of a big market" trap.

**Bottom-up, built from Halvorsen's own notes:**

| Step | Filter | Value | Source | Evidence grade |
|---|---|---|---|---|
| 1 | US lab instruments TAM | $9bn | Adviser's slide | Weak — no source given |
| 2 | × benchtop electrochemistry share | 2.5% | Adviser's own appendix | Weak — single source, same origin as line 1 |
| 3 | = Category TAM | **$225m** | Computed | — |
| 4 | × regulated-demand that would accept EU certification (in-house calibration labs) | 20% | Product team estimate | Weak — internal hypothesis, not customer-validated |
| 5 | = Regulatory-eligible demand | **$45m** | Computed | — |
| 6 | × distributor's geographic coverage | 30% of US lab activity | Distributor's own estimate | Weak — self-interested source, pitching the deal |
| 7 | = **Realistic SAM under the current deal** | **$13.5m** | Computed | Weak-to-medium; range $8m-$20m given two single-source filters |

**So-what:** the adviser's $90m figure is roughly **6-7x** the bottom-up SAM that Halvorsen can actually reach under the deal on the table. The size hypothesis is reshaped: addressable size is not "$9bn, take 1%" but "$13.5m, take a credible share of that."

### c. Customer need and switching

Halvorsen's own numbers say 80% of US regulated demand requires a locally certified calibration service and will not buy EU-certified-only instruments at any price. The 20% that would accept EU certification is a product-team hypothesis, not a tested customer finding — no interview evidence is cited. This is the single most consequential unverified number in the case: it gates everything downstream.

### e. Entry modes

Only one mode is concretely on the table: **export via the regional distributor**, capital-light, no own sales force, no calibration investment. This fits the $4m budget by construction — the budget wasn't sized against a calibration network or a sales office, so neither is a real option within $4m. Building US calibration capability (ISO/IEC 17025 accreditation, local technicians, equipment) is a multi-year, almost certainly >$4m undertaking — not costed by anyone in the notes, flagged as open question.

### f. Entry business case, with outside view

**Outside view / ramp benchmark:** Germany — 30% share of the addressable segment over **12 years** — is explicitly Halvorsen's best result anywhere, achieved in its home market with full distribution and decades of earned trust. The US entry starts from a weaker position (30% geographic coverage, no local calibration trust), so 30%/12 years is a **ceiling**, not a central case, for this deal.

Ramp shape for regulated instrument sales is typically a slow-start S-curve (qualification and pilot orders in years 1-2, acceleration later). 2030 is only **year 4** of entry (assuming a 2026 start). Taking roughly a third to a half of the 12-year mature share as a generous year-4 case:

| Scenario | Share of $13.5m SAM by 2030 | Revenue by 2030 |
|---|---|---|
| Low (slow trust-building, consistent with regulated-equipment entries) | 5% | $0.7m |
| Base (year-4 point on a path to the German ceiling) | 10-15% | $1.4-2.0m |
| High (front-loaded, optimistic) | 20% | $2.7m |
| Full maturity (Germany's ceiling, but not reached until ~2038) | 30% | $4.05m |

**No scenario — including the full 12-year-mature case — reaches $10m.** The "pays" hypothesis is killed.

### g. Stress test — what would it take to hit $10m?

At the German ceiling share (30%), the SAM required to produce $10m is $10m / 30% = **$33.3m** — roughly **2.5x** the current $13.5m SAM. Closing that gap needs both:
1. **National distribution**, not 30%-of-states coverage → raises SAM to $45m (still capped by the 20% calibration-eligible slice), and
2. **Still only reaches $13.5m at 30% share, and only by ~2038** — clearing $10m eventually, but not by 2030, and not under a single regional distributor deal.

Reaching $10m **by 2030 specifically** would require either a share far beyond anything Halvorsen has achieved anywhere in 4 years (not credible against the Germany benchmark), or solving the calibration barrier nationally — a capital and time commitment well beyond $4m and the 2030 window.

### h. Alternative use of capital

Not supplied by the board or the notes — no figures given for what else $4m could earn in the core business. Flagged as open question; the case cannot be closed on "beats alternatives" without this.

## Step 4: Trap checks

- [x] Share built bottom-up from category share, calibration-eligible demand, and channel coverage — not "1% of $9bn."
- [x] Customers and channel tested against Halvorsen's own product-team and distributor data, not assumed to transfer from Germany — and Germany is used only as a ramp-speed ceiling, not copied as a given.
- [ ] Incumbent reaction — **not modeled**; no competitor data in the notes. Open question.
- [x] Sunk costs — none flagged in the notes (no prior study or hire mentioned); none given weight here.
- [x] Ramp compared with a comparable entry (Germany), and explicitly treated as a ceiling, not a central case.
- [x] Exit criteria — see recommendation below; none existed before this case.
- [ ] Compared with the best alternative use of capital — **not possible**, no data supplied. Open question.

## Answer

**Answer:** Do not approve the plan as scoped. The board's $10m-by-2030 bar is not achievable under the distributor deal on the table, within $4m, on any reading of Halvorsen's own numbers that isn't more optimistic than its best result anywhere (Germany). Recommend either resetting the target/timeline or treating this as a smaller beachhead bet with a later decision point — not a $10m case.

**Confidence:** Medium-high that $10m by 2030 is not reachable under the current deal — the conclusion holds even under the most optimistic internally-consistent assumptions (full German-ceiling share, applied early). Confidence is lower on the *right alternative path*, because two of the three SAM filters (calibration-acceptance %, distributor coverage %) and all competitor/incumbent-reaction data are single-source or missing.

**Recommended path:**
1. Take the distributor deal, but re-scope it explicitly as a **beachhead/proof-of-demand pilot** within the $4m, sized to a realistic $1.5-4m run-rate by 2030 — not as the vehicle for a $10m target.
2. Use the pilot (through ~2029) to test the one number the whole case rests on: whether the 20% "would-accept-EU-certification" segment is real, by tracking actual orders against that estimate.
3. If the pilot confirms demand, bring a separate, larger capital ask to the board for national distribution plus a US calibration capability — the combination that can plausibly clear $10m, but on a 2035+ timeline, not 2030.
4. If by 2029 the pilot has captured well under ~10% of the $13.5m SAM, kill the US effort — that result would mean Halvorsen is tracking below even the low case above.
5. Take the adviser's $90m slide off the table for board decisions; it is not a figure the business case can be built on.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Benchtop electrochemistry = 2.5% of US lab instruments TAM | 2.5% | Adviser's own appendix (same source as the $9bn figure) | A second, independent source gives a materially different category share |
| 2 | Share of US regulated demand that would accept EU-certified instruments with in-house calibration | 20% | Product team estimate, not customer-tested | Buyer interviews show a materially different acceptance rate |
| 3 | Distributor's coverage of US lab activity | 30% | Distributor's own (self-interested) estimate | Independent verification (e.g. against state-level lab-activity data) shows materially different coverage |
| 4 | Entry start year | 2026 | Not stated; assumed given "by 2030" framing | Entry is delayed, shrinking the window further |
| 5 | Year-4 share as fraction of 12-year mature share | 1/3 to 1/2 | Generic S-curve reasoning for regulated/trust-gated equipment sales; no Halvorsen-specific data | A faster-trust-building comparable entry is found |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the 20% in-house-calibration acceptance rate real? | It gates the entire SAM calculation ($225m → $45m) | Customer interviews with target US labs | Could move SAM up or down by 2x+ |
| Is the distributor's 30% coverage claim accurate? | Second-largest SAM filter | Independent check against state-level lab-industry data | Could move SAM up or down |
| What margin does the board require, not just revenue? | $10m of low-margin revenue may still fail the board's real bar | Board / CFO | Could tighten or loosen the bar further |
| Who are the incumbent competitors in this segment and how would they react to Halvorsen's entry? | Not modeled at all; could independently kill the case | Competitor profiling, distributor's market knowledge | Could reveal the SAM is further constrained by entrenched incumbents |
| What else could $4m earn in the core business? | "Beats alternatives" branch cannot close without this | Halvorsen finance/strategy team | Could make US entry look worse even if it cleared $10m |
| What would US calibration accreditation actually cost and take, in time? | Determines whether the path to $10m+ (post-2030) is realistic at any budget | Regulatory/quality specialist, calibration-service partners | Could show the larger path is also not viable within reasonable capital |

