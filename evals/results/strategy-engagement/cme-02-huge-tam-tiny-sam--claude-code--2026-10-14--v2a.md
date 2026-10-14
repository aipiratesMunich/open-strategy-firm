# cme-02-huge-tam-tiny-sam on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" before "how" and states the minimum bar (USD 10m by 2030, USD 4m) as the test. | yes | "Minimum bar agreed with client (from board ask): Revenue at least USD 10m by 2030; capital at most USD 4m... Kill criterion set here, before analysis: if the realistic SOM ceiling under a mode is below USD 10m even at 100% share, that mode cannot meet the bar on its own." |
| Narrows the market step by step to about USD 13.5m serviceable. | yes | "Benchtop electrochemistry ≈2.5%... USD 225m" → "20% of the USD 225m segment... USD 45m" → "distributor covers states = 30%... USD 45m × 30% = USD 13.5m" |
| States that USD 90m exceeds the serviceable segment several times over (about 6.7x) and rejects "1% of a big market" as a method. | NO | The document only computes 90/225=40% of the broader product segment ("requires Halvorsen to capture 40% of the entire US benchtop electrochemistry segment (90/225)") and never states the ratio of 90m to the 13.5m serviceable segment or frames it as 'several times over'; it rejects the 1% method but |
| Builds a share or revenue estimate bottom-up from the distributor's reach and Halvorsen's own best share, and shows it misses USD 10m. | yes | "Low (5% of SOM) / Base (12%) / High (25%) ... Mode A — status quo: USD 0.7m / 1.6m / 3.4m ... No, even at high case", derived from the 13.5m SOM using Germany's 30% share as the outside-view ceiling. |
| Answer is do not enter, or enter later under named conditions, with what would make the board revisit it. | NO | The headline recommendation is "Enter, but not on the plan implied by the adviser's slide" and recommends executing Mode B now ("sign additional US distributors") even though its own base case (USD 5.4m) misses the USD 10m bar — this is a present-tense go decision on an under-the-bar base case, not  |
| Flags the USD 9bn as an unsourced adviser figure and the 20% and 30% as internal or distributor estimates to verify, without replacing them with invented US figures. | yes | "Headline market size / USD 9bn... Adviser's slide, no source given / unverified — flag"; "Distributor's state coverage / 30%... Distributor's own estimate (self-interested, unverified)" |
| Notes that US certification and regulatory questions go to specialists. | yes | "US certification/calibration requirements for lab instruments (e.g., ISO/IEC 17025, state-level lab regulations) need a regulatory specialist before costing Mode C/D below." |
| Must not propose an entry plan whose base case relies on a percentage of the USD 9bn. | yes | All base-case figures are expressed as a percentage of the derived SOM (13.5m/45m), e.g. "Base (12% of SOM)", not a percentage of the USD 9bn. |
| Must not cite US market reports, regulators' rules or competitor shares as facts. | yes | Regulatory standards (ISO/IEC 17025) are mentioned only as an example of what a specialist should check, not asserted as settled fact; no competitor shares are cited as fact (explicitly flagged as a data gap). |

## Transcript

## Turn 1

**User:** Our adviser says the US is a USD 9bn market and we only need 1%. The board likes it. How should Halvorsen enter the US? Notes attached. (Attached in the working directory: cme-02-input.md.)

## Headline answer

**The adviser's "9bn × 1% = 90m" is wrong, and it's not a rounding error — it's off by an order of magnitude.** Reject it as the planning basis. Full case saved to `case-market-entry-halvorsen.md`; key logic:

**Why the adviser's number is fiction:** 1% of USD 9bn = USD 90m. But Halvorsen only sells benchtop electrochemistry meters, which the adviser's own appendix puts at 2.5% of that market — USD 225m. So USD 90m isn't "1% of the market," it's **40% of Halvorsen's actual product segment** — more than Germany's all-time-best result (30% share, 12 years, home market, full certification) — and that's before applying the two real-world constraints in your notes:

- **Certification:** Halvorsen has no US calibration network; only the ~20% of US demand that calibrates in-house will buy without one → true ceiling **USD 45m**, not USD 225m.
- **Channel:** the distributor on the table covers states worth ~30% of US lab activity → realistic reachable pocket under *this* deal is **USD 13.5m**, not USD 45m.

**So the plan as currently scoped (sign this one distributor, do nothing about calibration) tops out at USD 13.5m even at 100% share.** Using Germany's ramp as an outside-view ceiling, heavily derated for a new, distributor-only, ~4-year entry, base case is **~USD 1.6m by 2030** — nowhere near the board's USD 10m bar.

**The better move within the USD 4m/2030 constraints:** sign *additional* US distributors to broaden state coverage within the 20% of demand you can already legally serve — skip trying to fix calibration/certification, which is unsized and likely too slow and expensive for this window. That widens the ceiling to USD 45m: base case ≈ **USD 5.4m**, high case ≈ **USD 11.3m** by 2030. The board's USD 10m bar is reachable only in the high case — it should be treated as a stretch goal, not a committed plan, unless you extend the deadline or find the money/time to also fix calibration.

**Biggest gaps in the notes that could move this:** no competitor/incumbent data at all, no cost estimate for a US calibration build-out, no margin target from the board, and no comparison against what else that USD 4m could earn inside Halvorsen. Full assumptions, open-questions table, and trap checks are in the saved file.


## Files in work dir after run

- case-market-entry-halvorsen.md
- cme-02-input.md

## File written by the run: case-market-entry-halvorsen.md

# Market entry: Halvorsen Instruments, US benchtop electrochemistry meters, should Halvorsen enter and how?

**Answer:** Enter, but not on the plan implied by the adviser's slide. Reject "1% of USD 9bn" — the real serviceable pocket today is USD 13.5m, not USD 90m, and the single-distributor plan tops out around USD 1.6m (base case) by 2030. The viable path within the board's USD 4m cap and 2030 deadline is to sign additional US distributors to broaden state coverage *within* the 20% of demand Halvorsen can already legally serve (in-house-calibrating labs) — not to chase the other 80% by building US calibration/certification capability, which is unsized, likely slow and likely expensive. On that path, base case ≈ USD 5.4m, high case ≈ USD 11.3m by 2030.
**Confidence:** Medium — the direction (adviser's framing is wrong; the current plan fails the board's bar) is high-confidence; the size of the achievable upside rests on two unverified, self-interested estimates (adviser's USD 9bn/2.5%, distributor's 30% coverage) and no competitor or unit-level data.
**Specialists and review:** US certification/calibration requirements for lab instruments (e.g., ISO/IEC 17025, state-level lab regulations) need a regulatory specialist before costing Mode C/D below. Distributor contract terms (exclusivity, termination/wind-down cost) need legal review before signing.

## Minimum bar agreed with client (from board ask)
- Revenue at least USD 10m by 2030; capital at most USD 4m.
- Margin target and management-time budget: **not stated** — see Open questions.
- Kill criterion set here, before analysis: if the realistic SOM ceiling under a mode is below USD 10m even at 100% share, that mode cannot meet the bar on its own.

## Is the market attractive?

| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Headline market size | USD 9bn, US lab instruments | Adviser's slide, no source given | **unverified** — flag |
| Addressable product segment | Benchtop electrochemistry ≈ 2.5% of the USD 9bn → **USD 225m** | Adviser's own appendix (same unverified origin as the USD 9bn figure) | pass as upper bound, fail as a planning number |
| True SAM given current capability | Only labs that calibrate in-house will buy EU-only-certified meters ≈ 20% of the USD 225m segment → **USD 45m** | Product team estimate | **this is the real ceiling today**, not USD 225m or USD 9bn |
| SOM ceiling under the mode on the table | Current distributor covers states = 30% of US lab activity → USD 45m × 30% = **USD 13.5m** | Distributor's own estimate (self-interested, unverified) | **fails the USD 10m bar even at 100% share** |
| Concentration / incumbents | No data given on competitors, their share or likely reaction | — | **gap — flag, see Open questions** |
| Regulation / certification | Regulated US labs will not buy without a certified local calibration service; Halvorsen has none | Product team | real barrier, costed as the 80%-exclusion filter above |

## The "1% of a big market" check (adviser's framing)

The adviser's slide implies USD 90m (1% of USD 9bn). That number requires Halvorsen to capture **40% of the entire US benchtop electrochemistry segment** (90 / 225) — more than Germany's all-time best result (30% share, achieved over **12 years** in Halvorsen's home market with full certification) — through a single regional distributor, with 80% of US demand structurally excluded by the calibration gap, inside roughly four years. The headline market size is not the constraint; the reachable pocket is. **This kills the adviser's number as a planning basis**, independent of anything else below.

## Entry modes compared

| Mode | What it requires | SAM ceiling | Investment | Time to unlock | Exit cost if abandoned |
|---|---|---|---|---|---|
| A — Status quo: sign the offered distributor only, no calibration investment | Contract already offered | USD 13.5m | Low (sales/marketing support only — **ASSUMPTION**, no figure given) | Fast (~months) | Low — distributor termination terms unknown (**ASSUMPTION/missing**) |
| B — Broaden distribution: add distributors/reps to cover more states, still only the in-house-calibration slice | Business-development effort, no new certification | USD 45m | Likely within USD 4m cap (**ASSUMPTION** — no per-distributor cost given) | Moderate (signing + ramp, 1-2 years) | Moderate — multiple contracts to unwind |
| C — Build US calibration network, keep single distributor | Accredited US calibration capability (certification body, technicians, likely multi-year build) | USD 67.5m | **Unknown — likely exceeds USD 4m; unsized** | Likely multi-year — **may not fit the 2030 window** | High — sunk infrastructure, hard to exit cleanly |
| D — Both B and C | Combines above | USD 225m | **Unknown, likely well over USD 4m** | Likely exceeds 2030 window | High |

**Mode B is the best fit for the stated constraints**: it does not depend on solving the calibration/certification problem — the part of this plan that is slow, capital-heavy and unsized — it only requires signing more of the same kind of distributor relationship already on offer.

## Business case (base / low / high), by mode

Share-of-SOM assumptions use Germany's 30%-over-12-years as an outside-view ceiling, heavily derated for a new, distributor-only, ~4-year entry (**ASSUMPTION — no comparable distributor-led export entry was available to triangulate this; treat the range as wide for that reason**).

| Mode | Low (5% of SOM) | Base (12% of SOM) | High (25% of SOM) | Meets USD 10m bar? |
|---|---|---|---|---|
| A — status quo | USD 0.7m | USD 1.6m | USD 3.4m | No, even at high case |
| B — broaden distribution | USD 2.3m | USD 5.4m | USD 11.3m | **Base: no. High: yes.** |
| C — + calibration network | USD 3.4m | USD 8.1m | USD 16.9m | Base: close. High: yes. **But investment unsized and plausibly infeasible within USD 4m/by 2030.** |
| D — both | USD 11.3m | USD 27m | USD 56m | Yes, easily — if achievable at all within the cap |

Payback and margin cannot be computed — no price, unit cost or distributor margin given. **Flag as missing for the next pass.**

## Can we win?

| Factor | Halvorsen | US incumbents |
|---|---|---|
| Certification | EU only | Presumed US-certified (not verified) |
| Local calibration service | None | Presumed yes for regulated-lab segment |
| Track record | 30% share of addressable segment in Germany over 12 years (best result anywhere) — real evidence of ability to win share, but over a much longer horizon and in the home market | **No data — competitor names, shares, pricing and likely reaction are a gap.** Run competitor profiling before committing capital. |

## Compared with the alternative use of capital

Not assessable from the data given: no figures on what else Halvorsen's USD 4m and management attention could earn (core-market investment, another growth lever). **This is an open question that could override the recommendation below even if Mode B clears the board's bar** — a positive business case is not sufficient if a better alternative exists for the same money.

## What would change the answer

1. If the board's USD 9bn/2.5%/20%/30% inputs are confirmed independently (trade association or regulator data instead of adviser/distributor estimates) and come in materially higher, the SOM ceilings above rise proportionally and Mode A could become viable.
2. If building a US calibration network is costed and comes in under ~USD 2-3m (leaving room for distribution spend) with a realistic path to accreditation before 2029, Mode C/D should be re-examined — currently it is the most valuable lever and the least understood one.
3. If competitor profiling shows one or two incumbents hold most of the in-house-calibration slice already, Mode B's achievable share falls below the base case used here, and the USD 10m bar becomes unreachable under any mode within the cap.
4. If the alternative use of the USD 4m is shown to return more per dollar than the ~USD 5-11m/2030 upside from Mode B, do not enter at all — redeploy the capital.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | US lab instruments market size | USD 9bn | Adviser's slide, unsourced | Verified figure is materially lower — all SAM/SOM ceilings shrink further, strengthening "do not enter as scoped" |
| 2 | Benchtop electrochemistry share of that market | 2.5% | Adviser's own appendix | Verified figure differs by >30% — redo all downstream filters |
| 3 | Share of US benchtop electrochemistry demand from in-house-calibrating labs | 20% | Product team estimate | Verified lower — Mode B's upside shrinks; lower still argues to fix calibration instead |
| 4 | Distributor's state coverage | 30% of US lab activity | Distributor's own estimate | Independently verified coverage is much lower — Mode A's ceiling falls further |
| 5 | Achievable share of reachable pocket by 2030 | 5% / 12% / 25% (low/base/high) | Derated from Germany's 30%-in-12-years outside view; no distributor-entry comparable available | A real comparable entry is found with a faster or slower ramp — narrow the range accordingly |
| 6 | Cost to sign additional US distributors (Mode B) | Fits within USD 4m cap | No figure given | Per-distributor cost is high — Mode B may also miss the cap |
| 7 | Cost/time to build US calibration network (Mode C/D) | Unsized, assumed > USD 4m and > time available | No figure given; directional only | Credible costing comes in under cap and within timeline — re-rank modes |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What margin, not just revenue, does the board require? | USD 10m of low-margin revenue may still fail the board's real bar | Board / CFO | Could tighten or loosen the viable modes |
| How much management time is the board willing to commit, and for how long before pulling out? | Mode B/C/D need sustained BD and/or regulatory effort | Board | Determines which modes are feasible at all |
| Why this market, why now — is this driven by the adviser's study or the distributor's offer rather than strategic fit? | Sunk study/sunk distributor talks must not drive the decision | CEO / sponsor | If driven by sunk momentum, revisit the decision independently of those inputs |
| What would it cost and how long would it take to build a US calibration/certification capability? | This is the single biggest unresolved swing factor (Mode A/B vs C/D) | Ops / regulatory specialist | Could flip the recommendation toward Mode C/D if cheap and fast enough |
| Who are the US incumbents, their share and likely reaction to entry? | No competitor data in the notes at all | Market/competitor research | Could lower every share estimate above, or reveal an opening |
| What does the distributor contract say about exclusivity and termination? | Needed to cost exit and to know if signing more distributors (Mode B) is even contractually possible | Legal | If the offered contract is exclusive, Mode B may be blocked without renegotiation |
| What else could USD 4m and the same management attention earn inside Halvorsen today? | Required for the "beats alternatives" test | CFO / strategy team | A better alternative use of capital overrides a technically positive business case |

## Trap checks

- [x] Share built bottom-up from customers, channel capacity and win rates, not "1% of a big market" — built from product-segment %, calibration-acceptance %, and distributor coverage %, with share-of-SOM scenarios, not a flat 1% of USD 9bn.
- [ ] Customers, channels and price levels tested in the target market, not copied from home — **open**: Germany's ramp is used only as an outside-view ceiling, not assumed to transfer directly; US buyer behaviour needs direct verification (interviews with target labs).
- [ ] At least one aggressive incumbent reaction modelled — **open**: no competitor data was given; flagged above as the top research gap. Does not change the verdict on Mode A (fails on size alone), but could change Mode B/C/D.
- [x] Sunk costs play no role — the adviser's slide and the distributor's existing offer are treated as inputs to size, not as reasons to enter; the recommendation explicitly rejects the plan the sunk distributor offer implies.
- [x] Ramp compared with a comparable entry, or range widened and the gap named — Germany is the only comparable available; range widened (5-25%) and the missing distributor-entry comparable is named as a data request.
- [x] Money already spent (adviser's study, distributor talks) called sunk — called out explicitly, plays no role in the verdict.
- [ ] Exit criteria and exit cost written down — **open, propose now**: set a checkpoint at end-2028; if run-rate revenue is below ~USD 2m annualised or share of SOM is tracking below the low case, exit. Exit cost = capital spent to that point (up to USD 4m) + distributor wind-down cost (**unknown — contract terms not given**).
- [ ] The entry is compared with the best alternative use of the same capital — **open**: no data given; listed as the top open question that could override this recommendation even if Mode B clears the board's bar.

