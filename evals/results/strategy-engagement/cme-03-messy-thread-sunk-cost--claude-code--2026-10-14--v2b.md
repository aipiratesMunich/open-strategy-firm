# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how", respecting the CEO's request | yes | "Should Corvina continue to invest in Polish office-coffee wholesale ... toward EUR 3m revenue by end 2028, within a EUR 1.5m total cap — and if so, through distributors or an own sales force?" while still delivering "Provisional answer to Marc's actual question: distributor-led, not own sales" |
| States EUR 60k study and hire are sunk/don't justify entry; country manager's future cost counts against budget | yes | "EUR 60k study marked sunk; Tomasz's ongoing salary marked committed-but-forward-looking (only *future* contribution matters, not past spend)"; budget math shows ≈EUR0.257m of Tomasz's future salary subtracted from the EUR1.5m cap, leaving EUR1.18m remaining |
| Flags EUR48m vs 80m+ conflict, uses study as base, asks for missing study attachment | yes | "Use EUR 48m (the study) as the working SAM until the actual study PDF ('PL_study_final_v3.pdf', mentioned in the thread but not supplied) is read"; open question: "What does the study PDF ... actually define as 'office coffee wholesale'?" |
| Puts EUR3m bar in proportion (~6% of segment) and calls for bottom-up ramp, not share assumption | yes | "Implied share needed: EUR 3m / EUR 48m = 6.25% of the study's SAM"; trap table: "Only a top-down SAM exists (48m); no bottom-up build from named distributor types and win rates yet" |
| Compares distributors vs own sales on cost, speed, control, exit cost using only input/flagged assumptions | yes | Table in Step 3e with Investment, Time to revenue, Control, Exit cost, Fit columns, all labelled ASSUMPTION and derived from thread's EUR1.18m headroom |
| Flags German 31% margin as not tested for Poland | yes | "Germany's 31% contribution margin is a reference point only, not evidence for Poland (home-market-transfer trap)" |
| Answer is conditional entry/enter later/no, with exit criteria, not unconditional go | yes | "Answer: Enter later, under conditions — continue with a distributor-led pilot ... bring the board a go/no-go at that checkpoint rather than a committed full-scale plan"; kill criterion stated in Step 1 |
| Open-questions table names who can answer each question | yes | Open questions table rows: "Whoever holds the study (Ines/the research vendor)", "Tomasz", "HR/Legal", "Ines / the board" |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | Competitor section explicitly: "Not assessable — no competitor names, pricing or service models exist in the thread"; all cost figures labelled ASSUMPTION |
| Does not treat prior hiring/spending as a reason in the recommendation | yes | "Marc's email explicitly uses 'we've already got Tomasz and the study' as the reason to proceed... Both are treated above as committed costs, not a case for or against going forward" |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

I ran this as a quick case (market-entry playbook) and wrote the full case to `case-market-entry-corvina-poland.md`. Headline for Marc:

**The thread's framing is a sunk-cost argument, not a business case.** "We've already got Tomasz and the study, so we're going" uses past spend (EUR 60k study, EUR 110k/year hire) to justify going forward — neither cost changes by continuing or stopping. Separately, the two market-size figures on the table disagree by 67% (Tomasz's unsourced "80m+" vs. the paid study's EUR 48m for 3 cities only) and haven't been reconciled, and there's zero competitor data anywhere in the thread.

What I can still give Marc for 3 November:

- **His actual question ("how"):** go **distributor-led, not own sales**, for a first phase — it fits the ~EUR 1.18m of budget still free under the board's EUR 1.5m cap (EUR 60k study + ~EUR 0.26m of Tomasz's contracted salary through 2028 are already spoken for), and own sales plausibly busts the cap on its own once reps, logistics and fleet are added. This is directional, not vendor-quoted.
- **The number the whole case turns on:** hitting EUR 3m by end 2028 against the study's EUR 48m figure means winning **6.25% share** of a relationship-driven wholesale market within ~18-24 months, with no competitor landscape and no outside-view comparable checked yet.
- **A proposed kill checkpoint** (not yet board-approved): if signed distributor volumes 9 months in are tracking below half that pace, escalate rather than keep spending.

Biggest gaps before Marc presents this as settled: nobody has read the actual study PDF (mentioned, not supplied) to check its scope, there's no incumbent/competitor picture at all, the "2 of 4 keen" distributors are an anecdote not a signed commitment, and nobody has compared this against just putting the same money into Germany's proven 31%-margin business. All of these are listed as open questions in the file with who can answer them.


## Files in work dir after run

- case-market-entry-corvina-poland.md
- cme-03-input.md

## File written by the run: case-market-entry-corvina-poland.md

# Market entry: Corvina, Poland office coffee — quick case

*Fictional company, people and figures, per the source thread.*

**This contradicts Marc's framing up front:** the thread treats "whether to enter" as already decided because money is already spent (the EUR 60k study, Tomasz's EUR 110k/year contract) — that is a sunk-cost argument, not a business case. Neither cost changes going forward. Separately, the two market-size figures on the table disagree by 67% (EUR 48m vs EUR 80m) and haven't been reconciled, and there is no competitor data at all. This case answers Marc's "how" question (distributor-led, not own sales, for a first phase) but frames it as conditional, not a green light, because "whether" is not yet proven.

Run as a **quick case** (market-entry playbook): the deadline is the 3 November leadership meeting and the brief says no more input is available right now. Every number below is either sourced from the thread or marked ASSUMPTION with a range; nothing is invented.

---

## Step 1: Sharpen the question

Marc's question: "Can the consultants just tell us HOW: distributors or own sales?" — the market is treated as chosen.

Sharpened decision question, per the market-entry playbook's reopening of "whether":

> Should Corvina continue to invest in Polish office-coffee wholesale (Warsaw/Kraków/Wrocław to start) toward EUR 3m revenue by end 2028, within a EUR 1.5m total cap — and if so, through distributors or an own sales force?

Minimum bar, from the CFO's email: revenue ≥ EUR 3m by end 2028, total investment ≤ EUR 1.5m. No margin floor was stated for Poland — flagged as an open question below, since Germany's 31% contribution margin is not evidence for Poland's margin.

What's already committed, read from the thread (not asked, since it's in the emails):
- EUR 60k spent on the market study, June 2026 — **sunk**, spent before Tomasz's hire.
- Tomasz: EUR 110k/year, started September 2026. From Sept 2026 to end 2028 is 28 months ≈ **EUR 0.257m** contracted through the target date (ASSUMPTION: no change in contract; actual committed amount depends on notice/severance terms, a legal/HR question — see open questions).
- Together, **≈ EUR 0.32m of the EUR 1.5m cap is already spent or contracted**, leaving **≈ EUR 1.18m of headroom** against the cap through end 2028. This is the budget frame for the "how" decision below.

Kill criterion set now, before running the numbers (mine, since the thread sets a target but not a kill test): **if the realistic bottom-up obtainable share of the reconciled addressable market cannot plausibly reach EUR 3m by end 2028 within the remaining EUR 1.18m, or if a signed distributor pilot after 9 months is tracking below half that pace, escalate to the board rather than keep spending.**

---

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Attractive: size | Addressable segment (SAM) supports EUR 3m at a realistic single-digit share | SAM below ~EUR 30-50m makes 3m require a share no new entrant plausibly gets in 2 years | Open — two unreconciled figures, see Step 3a |
| Attractive: structure | No incumbent distributor/roaster holds an entrenched majority of the segment | One or two incumbents control most of the office-coffee wholesale relationships | **Unknown — no data in the thread at all** |
| Can win: need | Office managers/distributors have an unmet need Corvina's offer solves and will switch | The "keen" distributors are being polite, not actually switching supply | Thin — 2 of 4 "keen" after first meetings, no terms, no evidence of real intent to switch |
| How: mode | One mode (distributor or own sales) reaches the target within the EUR 1.18m remaining budget and is exitable cheaply | Both modes need more capital or time than remains | Provisional — see Step 3e |
| Pays | Base case reaches EUR 3m by end 2028 within budget at a margin the board would accept | Base case misses the revenue bar, or margin is materially below Germany's 31% and nobody has checked | Open — no Poland margin data exists yet |
| Beats alternatives | The remaining EUR 1.18m and Tomasz's time return more in Poland than in Germany or elsewhere | Germany's proven 31% margin business would make better use of the same capital | **Not assessed — no data given** |

---

## Step 3: Deciding analyses

### a. Addressable market (market sizing)

Two figures on the table, not yet reconciled:

| Source | Figure | Scope | Date | Evidence grade |
|---|---|---|---|---|
| Tomasz | "80m+" | Unstated — reads as all of Poland, office coffee, unclear whether wholesale-only or includes other channels | "Read somewhere last year" | **Weak** — unsourced, single person's recollection, no defined scope |
| Paid study | EUR 48m/year | Office coffee, **wholesale only**, Warsaw + Kraków + Wrocław (3 cities, not all Poland) | June 2026 | **Medium** — single commissioned study, but recent, paid for, and scope is stated |

These are not the same measurement, so the 67% gap (80m vs 48m) isn't necessarily an error — a national figure should exceed a 3-city wholesale figure. But the 80m number can't be checked against anything (no source, no scope), so it cannot be used to size the opportunity. **Use EUR 48m (the study) as the working SAM** until the actual study PDF ("PL_study_final_v3.pdf", mentioned in the thread but not supplied) is read to confirm its scope matches Corvina's actual product and that "wholesale" covers the channel the own-sales option would need too.

Important scope flag: if the study only sized the **wholesale/distributor channel**, an **own-sales** entry (selling direct to office accounts, bypassing distributors) would be reaching a different, unsized pool of demand — the 48m figure may not even apply to that mode. This needs the PDF, not a re-ask of the people who already gave their numbers.

Implied share needed: EUR 3m / EUR 48m = **6.25%** of the study's SAM by end 2028. (Against Tomasz's unverifiable 80m, it would be 3.75% — lower, but not usable as a planning number.) A new entrant reaching 6.25% of a relationship-driven B2B wholesale category in roughly 18-24 months of actual selling time (Tomasz started Sept 2026; allow a few months of setup) is an aggressive ask with no outside-view comparable yet checked.

**Status: open.** SAM taken provisionally at EUR 48m; required share (6.25%) is the single biggest unproven number in this case.

### b. Market structure

No data in the thread — not five forces, not a single named competitor, not a concentration estimate. Tomasz's 4 distributor meetings are the only market-structure signal, and they describe his own pipeline, not the competitive landscape.

**Status: unknown.** This is normally the fastest kill test in a market-entry case and it hasn't been run at all.

### c. Customer need and switching

"Met 4 office coffee distributors last week, 2 keen." That's an n of 4, after first meetings, with no terms, contracts, or stated volumes — a long way from evidence that these distributors will actually switch supply. "Keen" after one meeting is a normal, low-cost thing for a distributor to say.

**Status: thin evidence, not yet a validated demand signal.**

### d. Competitors and their reaction

Not assessed — no names, no pricing, no service model for any incumbent. Cannot be sized from the thread; flagged as a data request, not invented.

### e. Entry modes: distributor vs. own sales

No vendor quotes or HR costings exist, so the cells below are directional, built from the case's own cost structure (the EUR 1.18m remaining headroom) and labelled ASSUMPTION — not invented totals, but not costed quotes either.

| Mode | Investment (through end 2028) | Time to revenue | Control | Exit cost | Fit vs. EUR 1.18m headroom |
|---|---|---|---|---|---|
| **Distributor-led** | ASSUMPTION: EUR 0.2-0.4m (samples, van, trade terms/incentives, Tomasz's time) | ASSUMPTION: 3-6 months — distributors already have customers and logistics | Lower — price/service partly set by the distributor; limited end-customer data | Low — supply agreements can usually be unwound with notice; no fleet/warehouse beyond the one van | **Fits comfortably within headroom** |
| **Own sales** | ASSUMPTION: EUR 1.0-1.5m+ (reps, warehousing, delivery fleet, inventory working capital) | ASSUMPTION: 9-18 months — building relationships and logistics from zero | Higher — direct pricing, service and customer data | High — severance, fleet/warehouse disposal, inventory write-down | **Plausibly breaches the EUR 1.5m cap once combined with the EUR 0.32m already committed** |

**Provisional answer to Marc's actual question: distributor-led, not own sales, for a first phase.** It fits the remaining budget and the ~2-year runway to the 2028 target; own sales is the higher-control, higher-cost option a later phase could revisit once a segment is proven. This needs real vendor/HR numbers before it goes to the board as more than directional.

### f. Entry business case (directional, not a full model)

A full NPV/IRR model needs drivers that don't exist yet in the thread (distributor margin %, price per kg, win rate, customer acquisition cost). What can be stated now:

- Remaining budget to the cap: **≈ EUR 1.18m** through end 2028.
- Revenue bar: **EUR 3m by end 2028** — ASSUMPTION that this means an annual run-rate exiting 2028, not cumulative 2026-2028 revenue; this is a cheap fact to confirm with Ines/the board and it changes the required ramp materially (a cumulative-revenue reading is a much easier bar than an exit run-rate).
- No Poland margin figure exists. Germany's 31% contribution margin is a reference point only, not evidence for Poland (home-market-transfer trap) — distributor mode will likely capture less margin than own sales, since the distributor keeps a cut.

**Status: cannot be made precise from the data given.** The breakeven number to carry into the board meeting is the 6.25% share figure from 3a — that is the number the case turns on.

### g. Stress test

No incumbent-reaction case and no outside-view ramp comparable exist in the thread. Both are open; recommend naming them explicitly as unresolved in the board pack rather than presenting a single clean ramp.

### h. Alternative use of capital

Not assessed. The thread gives one comparator — Germany's office business at 31% contribution margin, a proven model — but nothing quantifies what the same EUR 1.18m and Tomasz-equivalent management time would return if spent there instead. This is the branch market-entry teams forget, and it is currently entirely unaddressed in the board-bound plan.

---

## Step 4: Trap checks

| Trap | Status | Evidence / fix |
|---|---|---|
| Share built bottom-up from customers, channel capacity, win rates, not "1% of a big market" | **Open / not yet done** | Only a top-down SAM exists (48m); no bottom-up build from named distributor types and win rates yet |
| Customers, channels and price levels tested in Poland, not copied from home | **Fail on margin** | Germany's 31% margin is being implicitly carried over; no Poland margin data |
| At least one aggressive incumbent reaction modelled | **Fail** | No competitor data exists at all |
| **Sunk costs (study, hire, talks) play no role in the recommendation** | **Fail in the thread, fixed here** | Marc's email explicitly uses "we've already got Tomasz and the study" as the reason to proceed. Both are treated above as committed costs, not a case for or against going forward. |
| Ramp compared with comparable entries, or range widened and the gap named | **Open** | No comparable entry cited; 6.25%-of-SAM-in-2-years stated as unproven, not sized against any outside view |
| Money already spent called sunk and plays no role in the decision | Same as above | EUR 60k study marked sunk; Tomasz's ongoing salary marked committed-but-forward-looking (only *future* contribution matters, not past spend) |
| Exit criteria and exit cost written down before entry | **Fail in the thread, proposed here** | See kill criterion in Step 1 and recommendation below — needs board sign-off, not yet existing |
| Entry compared with the best alternative use of the same capital | **Fail** | Germany comparison not run; flagged in 3h |

---

## Step 5: Answer page

# Market entry: Corvina, Poland office coffee, should Corvina commit beyond the study and Tomasz's hire toward EUR 3m revenue by end 2028 within a EUR 1.5m cap, and if so how

**Answer:** Enter later, under conditions — continue with a **distributor-led pilot** (not own sales) in the three cities the study covers, convert the two "keen" distributor conversations into signed volume terms as the first checkpoint, and bring the board a go/no-go at that checkpoint rather than a committed full-scale plan on 3 November.

**Confidence:** Low, because the market-size numbers are unreconciled, there is no competitor data, the required share (6.25% of the study's EUR 48m SAM by end 2028) has no outside-view comparable yet, and the "how" answer rests on directional cost assumptions, not quotes.

**Specialists and review:** HR/legal should check Tomasz's contract terms before any talk of winding the project down (notice, severance); nobody has looked at the actual study PDF yet, which should happen before the board meeting, not after.

## Minimum bar agreed with client (from the thread, not yet confirmed with Marc)
- Revenue ≥ EUR 3m by end 2028 (ASSUMPTION: annual run-rate at exit, needs confirming)
- Capital ≤ EUR 1.5m total (≈ EUR 0.32m already committed to the study and Tomasz's contract; ≈ EUR 1.18m remaining)
- No margin floor stated for Poland — open question
- Kill criterion (proposed, not yet board-approved): if signed distributor volumes 9 months in are tracking below half the pace needed for EUR 3m by end 2028, escalate rather than keep spending

## Is the market attractive?
| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size | EUR 48m/year, 3 cities, wholesale only | Paid study, June 2026 | Provisional pass — but requires 6.25% share, unproven |
| Addressable size (alternate) | "80m+", scope and source unclear | Tomasz, unsourced recollection | Not usable for planning |
| Concentration and incumbents | No data | — | **Fail — not assessed** |
| Barriers and regulation | No data | — | Not assessed |

## Can we win?
| Factor | Us | Incumbent A | Incumbent B |
|---|---|---|---|
| Not assessable — no competitor names, pricing or service models exist in the thread | — | — | — |

## Entry modes
| Mode | Investment | Time to revenue | Control | Exit cost | Fit |
|---|---|---|---|---|---|
| Distributor-led | ASSUMPTION EUR 0.2-0.4m | ASSUMPTION 3-6 months | Lower | Low | Fits remaining EUR 1.18m headroom |
| Own sales | ASSUMPTION EUR 1.0-1.5m+ | ASSUMPTION 9-18 months | Higher | High | Plausibly breaches the EUR 1.5m cap |

## Business case (base / low / high)
| | Base | Low | High |
|---|---|---|---|
| Revenue by end 2028 | Breakeven share 6.25% of EUR 48m SAM | Below breakeven if ramp or structure is worse than assumed | Only reachable with validated distributor commitments beyond the current 2 of 4 | 
| Cumulative investment | ≈ EUR 1.18m remaining of the EUR 1.5m cap | — | — |
| Payback | Not computable without distributor margin %, price and win-rate data | — | — |

## Compared with the alternative use of capital
Not run. Germany's office business is a proven 31% contribution margin model; nobody has quantified what the remaining EUR 1.18m and Tomasz's management time would return there versus in an unproven Polish market with no competitor data and an unreconciled market size. This comparison should exist before the board is asked to commit further capital.

## What would change the answer
1. If the study PDF shows the 48m figure covers a narrower product or channel than Corvina sells, the SAM — and the 6.25% breakeven — gets worse.
2. If the two "keen" distributors convert to signed volume terms within the next few weeks, that's the first real evidence of demand and would raise confidence materially.
3. If a competitor landscape review shows one or two incumbents hold most of the wholesale relationships in the 3 cities, this is a kill signal per the issue tree.
4. If HR/legal confirms Tomasz's contract has a short notice period, the real cost of pausing or exiting is much lower than it looks, which weakens the sunk-cost pressure to keep going regardless of the numbers.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | EUR 3m target is an annual run-rate at end 2028, not cumulative revenue | Run-rate reading | Standard framing for growth targets; not stated in thread | If cumulative, the required ramp is much easier and the "low confidence" flag should loosen |
| 2 | EUR 1.5m cap includes Tomasz's salary and the study cost, not just incremental new spend | Included | Most natural reading of "no more than EUR 1.5m for Poland in total" | If the cap is incremental on top of headcount, remaining headroom is larger and own sales becomes more viable |
| 3 | Distributor mode cost EUR 0.2-0.4m, own sales EUR 1.0-1.5m+ | Directional ranges | Derived from the remaining headroom and typical cost shape of each mode, no vendor/HR quotes | Real quotes could move either mode's viability |
| 4 | Study's EUR 48m figure is the right SAM (not Tomasz's 80m) | EUR 48m used | Sourced, scoped, recent; 80m is unsourced | If the study PDF reveals a narrower or wider scope than assumed |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does the study PDF ("PL_study_final_v3.pdf") actually define as "office coffee wholesale"? | Determines whether 48m is the right SAM and whether it even covers an own-sales channel | Whoever holds the study (Ines/the research vendor) | Could move the breakeven share up or down materially |
| Who are the incumbent distributors/roasters in Warsaw, Kraków, Wrocław, and how concentrated is the segment? | Fastest kill test in a market-entry case; currently entirely unanswered | Tomasz, from his own meetings and further diligence | Could kill the case outright if 1-2 players dominate |
| Are the "2 of 4 keen" distributors willing to sign volume terms, and on what terms? | Converts an anecdote into real evidence of demand | Tomasz | Confirms or kills the demand hypothesis |
| Is there a Poland margin target, or only the Germany 31% reference? | Germany's margin isn't evidence for Poland, especially under a distributor model that cedes margin | Ines / the board | Could tighten or loosen the viable mode choice |
| Does the EUR 1.5m cap include Tomasz's salary and the sunk study cost, or is it incremental? | Changes the real remaining budget from ~EUR 1.18m to a larger or smaller number | Ines | Directly changes which entry mode fits |
| What would the same capital and Tomasz's time return if redeployed into the proven German business instead? | The alternative-use-of-capital branch is currently unassessed | Ines / Marc | Could outweigh the Poland case entirely |
| What is the actual notice/severance exposure on Tomasz's contract? | Determines the real cost of pausing or exiting, relevant to whether sunk-cost pressure is justified | HR/Legal | Lowers or raises the practical cost of a "no" or "not yet" answer |

