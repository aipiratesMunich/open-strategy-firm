# cme-02-huge-tam-tiny-sam on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" before "how" and states the minimum bar (USD 10m by 2030, USD 4m) as the test. | yes | Report title and answer frame the question as "should Halvorsen enter the US... given it must deliver at least USD 10m revenue by 2030 within USD 4m capital?" and reframe the ask as "can we get USD 10m out of a USD 13.5m reachable pool" rather than how to execute the distributor plan. |
| Narrows the market step by step to about USD 13.5m serviceable, with source and logic. | yes | Table: USD 9bn → USD 225m (2.5% benchtop electrochemistry) → USD 45m (20% buyable without US calibration) → USD 13.5m (30% distributor coverage), each with a stated basis. |
| States that USD 90m exceeds the serviceable segment several times over (about 6.7x) and rejects "1% of a big market" as a method. | NO | The write-up rejects the '1% of a big market' method ("classic trap", "1% of a market Halvorsen can't actually reach") but never computes or states that USD 90m is ~6.7x the USD 13.5m serviceable segment; it only notes '1% of USD 13.5m would be USD 135k' and frames the gap via a '74% share needed' c |
| Builds a share or revenue estimate bottom-up from the distributor's reach and Halvorsen's own best share, and shows it misses USD 10m. | yes | "Needs 74% share of reachable SAM by 2030 to hit USD 10m — exceeds Halvorsen's best-ever share (30%, and that took 12 years). **Fails.**" uses the 13.5m distributor-reach figure and Germany's 30% best share to show the shortfall. |
| Answer is do not enter, or enter later under named conditions, with what would make the board revisit it. | yes | "Enter later, under two named conditions... (a) a US calibration/certification route and (b) distribution beyond the single regional distributor" plus a dedicated 'What would change the answer' section. |
| Flags the USD 9bn as an unsourced adviser figure and the 20% and 30% as internal or distributor estimates to verify, without replacing them with invented US figures. | yes | Assumptions table: #1 'USD 9bn — Adviser slide, no source'; #3 '20% — Halvorsen product team estimate, internal, unverified'; #4 '30% — Distributor's own estimate, self-interested, unverified'. |
| Notes that US certification and regulatory questions go to specialists. | yes | Open questions table: 'Who can answer: Regulatory/quality affairs specialist, calibration-lab vendors' listed twice for calibration/certification cost and mutual-recognition questions. |
| Must not propose an entry plan whose base case relies on a percentage of the USD 9bn. | yes | Base case uses 'USD 45m SAM (calibration fixed, one distributor)' with a 2–5% share, derived bottom-up rather than as a direct percentage of USD 9bn. |
| Must not cite US market reports, regulators' rules or competitor shares as facts. | yes | Regulatory claim is sourced only to internal 'Product team notes', not to any external US regulatory report; competitor shares are explicitly listed as 'Unknown' and 'not modelled'. |

## Transcript

## Turn 1

**User:** Our adviser says the US is a USD 9bn market and we only need 1%. The board likes it. How should Halvorsen enter the US? Notes attached. (Attached in the working directory: cme-02-input.md.)

The adviser's "1% of USD 9bn" is the classic trap — a share of a market Halvorsen can't actually reach. Rebuilding bottom-up from your own notes:

**USD 9bn → USD 225m** (benchtop electrochemistry is only ~2.5% of that, per the adviser's own appendix) **→ USD 45m** (only ~20% of that demand will buy EU-certified instruments with no US calibration network) **→ USD 13.5m** (the one distributor on the table only covers ~30% of US lab activity).

So the real question isn't "can we get 1% of USD 90m" (USD 900k, trivial) — it's "can we get USD 10m out of a USD 13.5m reachable pool," which means ~74% market share by 2030. Halvorsen's best result anywhere, Germany, is 30% share — and that took 12 years, not 4.

**Bottom line: don't enter on the distributor-plus-EU-certification plan as pitched.** It structurally cannot hit the board's USD 10m bar. The case only works if Halvorsen first (1) gets a US calibration/certification route (building vs. partnering matters a lot for the USD 4m cap) and (2) adds distribution beyond this one regional distributor — which reopens the SAM to USD 45–225m, where a Germany-paced ramp could plausibly land USD 9–18m by 2030. That's a real path, not a guaranteed one, and it hinges on costs and competitor data you don't have yet (calibration partnership cost, incumbent reaction, whether the distributor's "30% of lab activity" figure is even the right proxy).

Full writeup with the business case ranges, trap checks, assumptions, and the open questions that need answers before the board commits is in `case-market-entry-halvorsen.md`.


## Files in work dir after run

- case-market-entry-halvorsen.md
- cme-02-input.md

## File written by the run: case-market-entry-halvorsen.md

# Market entry: Halvorsen Instruments, US benchtop electrochemistry, should Halvorsen enter the US by 2030 given it must deliver at least USD 10m revenue by 2030 within USD 4m capital?

**Answer:** Enter later, under two named conditions — not the adviser's "distributor + EU certification" plan as it stands. On the data given, that plan can reach at most ~USD 13.5m of *reachable* demand, not the adviser's USD 90m, and a realistic share of it falls far short of the board's USD 10m bar. Entry only clears the bar if Halvorsen first secures (a) a US calibration/certification route and (b) distribution beyond the single regional distributor — and even then the required ramp is aggressive against Halvorsen's own best-ever result (Germany).
**Confidence:** medium — the bottom-up math is solid and built from the client's own notes, but three of its five inputs are single-source, self-interested, or internal estimates with no outside check (flagged below).

## Minimum bar agreed with client (board ask)
- Revenue at least USD 10m by 2030 (~4 years from now); no margin threshold given — **open question**.
- Capital at most USD 4m.
- Kill criterion applied in this case: if the bottom-up addressable market reachable by Halvorsen's actual entry vehicle is below USD 10m even at an optimistic share, the current plan is killed (not necessarily the market).

## The adviser's number, rebuilt bottom-up

The adviser's slide: USD 9bn US lab instruments market × 1% = USD 90m. This is the "1% of a big market" trap — it assumes a share of a market Halvorsen cannot actually address, with no bottom-up path to customers. Rebuilding from Halvorsen's own notes:

| Step | Cut | Figure | Basis |
|---|---|---|---|
| 0 | Headline US lab instruments market | USD 9bn | Adviser slide, no source given |
| 1 | × benchtop electrochemistry share | USD 225m | Adviser's own appendix: ~2.5% of the headline (same unsourced study, broken down — not an independent check) |
| 2 | × demand Halvorsen can legally/practically serve today | USD 45m | Product team estimate: ~20% of US benchtop electrochemistry demand comes from labs that calibrate in‑house and would accept EU‑only certification; the rest requires a certified US calibration network Halvorsen does not have |
| 3 | × the one entry vehicle actually on the table | **USD 13.5m** | The offered distributor covers states worth ~30% of US lab activity (distributor's own estimate) |

So the real "1% of what" is USD 13.5m of reachable demand through the deal in hand, not USD 9bn, and not even the USD 225m product-line segment. 1% of USD 13.5m would be USD 135k — a figure that makes obvious how far the board's USD 10m target sits from a trivial share-grab.

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size (bottom-up, current offer) | ~USD 13.5m reachable through the single distributor deal; ~USD 45m if Halvorsen fixes calibration/certification but keeps one regional distributor; ~USD 225m ceiling for the product line if both constraints are lifted | Derived above from client notes | Fails the USD 10m bar at the current scope; passes only if both gating constraints are removed |
| Concentration / incumbents | Unknown — no competitor data supplied | — | **Open, not tested** |
| Regulatory / certification barrier | Confirmed material: regulated US labs will not buy without a certified local calibration service; Halvorsen has none today | Product team notes | Fail as-is; passable only by building or partnering for one |

## Can we win?
| Factor | Us (Halvorsen) | US incumbents |
|---|---|---|
| Product fit | pH / conductivity / dissolved oxygen benchtop meters — single product line | Unknown — not profiled |
| Certification | EU certification only | Unknown; US regulated labs require certified local calibration — this is the gating factor, not product quality |
| Channel | One distributor offer, ~30% of US lab activity by state | Unknown |
| Track record | Best result anywhere: 30% of addressable segment in Germany, achieved over **12 years** | Unknown reaction to entry — **not modelled, a trap in itself** |

Competitor behaviour and reaction are unknown. This cannot be waved away — it is listed as an open question below, not assumed benign.

## Entry modes
| Mode | Investment | Time to revenue | Reach | Fit vs. USD 4m cap / USD 10m bar |
|---|---|---|---|---|
| Distributor only, EU certification as-is (adviser's implied plan) | Low (distributor absorbs most channel cost) | Fast | USD 13.5m SAM ceiling | Needs 74% share of reachable SAM by 2030 to hit USD 10m — exceeds Halvorsen's best-ever share (30%, and that took 12 years). **Fails.** |
| Distributor + third-party US calibration/certification partnership (no owned calibration lab) | Partnership/accreditation fee, ASSUMPTION: USD 0.3–0.8m, unverified — needs a vendor quote | Medium (certification lead time unknown) | Reopens USD 45m SAM (single distributor) or USD 225m SAM (if paired with broader distribution) | Needs ~4.4% share of USD 225m by 2030 if distribution is also widened — aggressive but not absurd against the Germany ramp; depends on cost fitting inside USD 4m once sales/marketing spend is added |
| Own US calibration network + own sales office | High, likely exceeds USD 4m | Slow | Full segment | **Fails the capital cap on its face**; not costed further, ruled out |

## Business case (base / low / high) — provisional, labelled assumptions
| | Low | Base | High |
|---|---|---|---|
| SAM reachable by 2030 | USD 13.5m (distributor only, no calibration fix) | USD 45m (calibration fixed, one distributor) | USD 225m (calibration fixed + distribution widened) |
| Plausible 2030 share, given Germany took 12 yrs for 30% | n/a — mode fails outright | 2–5% (early-ramp share, outside view scaled to ~4 of 12 years) | 4–8% |
| Resulting 2030 revenue | — | **USD 0.9–2.3m** | **USD 9–18m** |
| Meets USD 10m bar? | No | No | Only at the high end of the high case |

The board's USD 10m target is only reachable in the scenario where Halvorsen (1) fixes certification/calibration, (2) widens distribution beyond the single 30%-coverage distributor, and (3) lands toward the top of a plausible, not optimistic, share range. That is a real possibility, not a certainty — and its cost is not yet known against the USD 4m cap.

## Compared with the alternative use of capital
Not assessable from the notes given: no figures were supplied for what else USD 4m could do (e.g., deepening the German share beyond 30%, a new adjacent product, or another market). This is a required comparison before the board commits — entry can clear its own bar and still be the wrong use of USD 4m. **Open question**, not answered here.

## Trap checks
- [x] Share rebuilt bottom-up from the client's own segment, calibration, and channel figures — not "1% of USD 9bn".
- [ ] Customers, channel and price levels tested in the US specifically — not done; Germany is used only as an outside-view ramp benchmark, flagged as a single-country comparable with a different regulatory regime.
- [ ] Incumbent reaction modelled — not done, no competitor data supplied. **Must be done before any commitment.**
- [x] Sunk cost flagged: the adviser's slide and the board's enthusiasm for it are not reasons to enter; the distributor's offer being "on the table" is not a reason either.
- [x] Ramp compared with a comparable (Germany, 12 years to 30%) rather than assumed.
- [ ] Exit criteria and exit cost — not yet defined. **Open question.**
- [ ] Compared with the best alternative use of the same capital — not possible with data given. **Open question.**

## What would change the answer
1. If Halvorsen can secure third-party US calibration/certification coverage for under ~USD 1m and within a timeline that leaves 3+ years to sell, the addressable SAM reopens from USD 13.5m to USD 45–225m and USD 10m by 2030 becomes plausible.
2. If the one distributor's "30% of US lab activity" estimate is independently confirmed (or found optimistic — it is self-reported), the SAM ceiling moves accordingly.
3. If a second distributor or direct channel can be added within the USD 4m cap, the USD 225m ceiling becomes reachable without an owned sales office.
4. If competitor profiling finds one or two incumbents hold most of the ~20% in-house-calibration segment already, the kill criterion on concentration should be re-applied and may kill the case outright even in the best scenario.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | US lab instruments market size | USD 9bn | Adviser slide, no source | Verified materially lower or higher |
| 2 | Benchtop electrochemistry share of that market | 2.5% | Adviser's own appendix (same unsourced study) | Independent market study shows a different figure |
| 3 | Share of US benchtop electrochemistry demand buyable without US calibration network | 20% | Halvorsen product team estimate, internal, unverified | Customer interviews show materially more or less in-house-calibration demand |
| 4 | Distributor's state coverage equals share of demand reachable | 30% | Distributor's own estimate, self-interested, unverified | Independent check (e.g. against actual electrochemistry-lab density, not general "lab activity") shows a different figure |
| 5 | Calibration/certification partnership cost | USD 0.3–0.8m | No data given — analyst range, needs a vendor quote | Actual quote falls outside this range, changing capital fit |
| 6 | Plausible 2030 share of a reopened SAM | 2–8% | Scaled down from Germany's 30%-over-12-years outside view to a ~4-year window | A faster or slower realistic ramp is evidenced from another comparable entry |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What margin, not just revenue, does the board require? | "Worth the effort" was framed only in revenue; a low-margin USD 10m could still fail the real bar | Board / CFO | Could tighten or relax the bar materially |
| Who are the incumbent US benchtop electrochemistry suppliers, and what would they do if Halvorsen entered? | Untested concentration/reaction risk could kill the case outright even in the best scenario | Competitor profiling exercise | Could kill or reshape the entry mode |
| What would third-party US calibration/certification actually cost and take to arrange? | Decides whether the USD 45–225m SAM is reachable within the USD 4m cap and the time window | Regulatory/quality affairs specialist, calibration-lab vendors | Decides whether this is "enter" or "do not enter" |
| Is the distributor's "30% of US lab activity" figure specific to electrochemistry demand, or general lab activity? | A general proxy could overstate or understate the relevant SAM | Distributor, or independent industry data | Resizes the SAM directly |
| What else could USD 4m of capital and management time do for Halvorsen (e.g., deepen Germany past 30%, a new product, another market)? | Entry can clear its own bar and still be the wrong use of the money | Board / strategy team | Could make "do not enter" the right call even if the US case is positive |
| What triggers exit, and what would exit cost (distributor wind-down, any committed spend)? | No exit criteria defined yet; board should set these before committing capital | Board, legal | Changes the downside case, not the central recommendation |
| Does Halvorsen's EU certification have any mutual-recognition or fast-track path with a US accreditation body? | Could cut both the cost and time of the calibration/certification gating factor | Regulatory/quality affairs specialist | Could move the recommendation from "later" to "now" |

