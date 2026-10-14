# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how" in a way that respects the CEO's request | yes | "That reopens 'whether' without touching the sunk hire or study... while stopping the board from rubber-stamping 'distributor or own sales' on no evidence." |
| States EUR60k study and hire already made are sunk and don't justify entry; country manager's future cost counts against budget | NO | The file says "they only mean the information and the person are already paid for" and then treats Tomasz's cost as a flat 'EUR110k/yr... already run against the EUR1.5m cap' rather than distinguishing the sunk historical spend from his ongoing/future salary (Sept 2026–end 2028) that still consumes  |
| Flags conflict between EUR48m (study) and 80m+ (unsourced), uses study as documented base, asks for missing study attachment | yes | "Tomasz's 80m+ estimate and the study's 48m figure don't reconcile... Gap is ~67%" and open questions asks for "PL_study_final_v3.pdf," mentioned but not attached. |
| Puts EUR3m bar in proportion (~6% of three-city segment by 2028) and calls for bottom-up ramp, not a share assumption | yes | "EUR3m / EUR48m study-based SAM = 6.25% share of the three-city wholesale segment inside ~27 months" plus trap check "Share built bottom-up from customers, channel capacity, win rates — No." |
| Compares distributors vs own sales on cost, speed, control, exit cost using only input and flagged assumptions | yes | Entry modes table compares Investment, Time to revenue, Control, Exit cost for Distributor-led vs Own sales office, explicitly flagged as "a direction, not a decision." |
| Flags German 31% margin as not tested for Poland | yes | "No margin assumption for Poland — only Germany's 31% as an unvalidated stand-in" and Assumption #2 flags this as unverified. |
| Answer is enter under conditions, enter later, or do not enter, with exit criteria; not unconditional go | NO | Answer states "Enter later, under conditions" (satisfying the conditional framing) but no exit criteria are actually provided — the document only notes their absence ("No exit/kill criterion stated anywhere in the thread") and defers defining one to the Nov 3 meeting rather than stating any exit tri |
| Open-questions table names who can answer each question | yes | Table lists answerers such as "Ines (has the study)" for the study gap and "Tomasz" for "What are the actual terms the 2 'keen' distributors are offering." |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | Competitor stays unnamed: "the 'Italians' Tomasz references"; no invented Poland-specific figures or distributor margin numbers appear anywhere. |
| Does not treat "we have already hired and paid" as a reason in the recommendation | yes | Recommendation: "both stay, because they're already paid for" is framed only as a reason not to relitigate the hire/study, not as a reason to enter — consistent with the trap-check finding that sunk costs play no role in the recommendation. |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

I worked this as a market-entry case and wrote the full answer to `case-market-entry-corvina-poland.md`. Headline:

**Marc's framing has a sunk-cost problem.** "We've already got Tomasz and the study, so we're going — just tell us HOW" treats two paid-for things (the EUR60k study, Tomasz's EUR110k/yr contract) as reasons to enter. They aren't — they're already spent either way, and the real question of whether Poland clears the board's bar (EUR3m revenue by end 2028, inside EUR1.5m capital) is still open.

The case can't responsibly jump to "distributors vs. own sales" yet, because:
- **Tomasz's 80m+ estimate and the study's 48m figure don't reconcile** — different scope (nationwide anecdote vs. three-city wholesale), a 67% gap, no second source for either.
- **No bottom-up build exists** — just "2 of 4 distributors keen," no office counts, contract values, or win rates.
- **No margin assumption for Poland** — only Germany's 31% as an unvalidated stand-in.
- **No exit/kill criterion** and **no comparison to the alternative use of the same EUR1.5m** (e.g., Germany expansion) — the playbook's most-forgotten branch.

Five of seven standard trap checks fail outright (full table in the file).

**Recommendation for Nov 3:** don't bring a channel decision — bring the reconciled market size, a bottom-up revenue path from the actual distributor conversations, what that implies against the budget/target, and an exit trigger. That reopens "whether" without touching the sunk hire or study (they stay — they're paid for regardless), while stopping the board from rubber-stamping "distributor or own sales" on no evidence.

The single highest-value missing input is the actual study PDF ("PL_study_final_v3.pdf") — mentioned in the thread but not attached. Worth chasing that down before anything else.


## Files in work dir after run

- case-market-entry-corvina-poland.md
- cme-03-input.md

## File written by the run: case-market-entry-corvina-poland.md

# Market entry: Corvina, Poland office coffee — should we enter, and how, given the board's bar?

**The analysis contradicts the premise Marc's email asks us to accept.** Marc's framing — "we've already got Tomasz and the study, so we're going, just tell us HOW" — treats two sunk commitments (a EUR60k study paid in June, a EUR110k/year hire started in September) as reasons to enter. They aren't. Neither changes whether Poland clears the board's bar; they only mean the information and the person are already paid for. The decision on "whether" is still open, and right now it can't be answered responsibly with what's in this thread.

**Answer:** Enter later, under conditions — not yet decidable as a straight "enter, by distributor" on the data in hand. The decision that *can* be taken now: use the 3 November meeting to agree the bar and close the four gaps below, not to pick distributors vs. own sales.
**Confidence:** Low, because the two market-size figures are unreconciled, there is no bottom-up build, no margin assumption for Poland, and no exit criterion — four of the seven trap checks below fail outright.
**Specialists and review:** None flagged yet (no regulatory/labour question raised in the thread); revisit once an entry mode is chosen (own sales office triggers Polish employment/payroll questions; distributor triggers commercial-agency-law questions under Polish civil code — flag to legal once the mode is live).

## Minimum bar stated by the board (not yet confirmed as the operating bar)
- Revenue at least EUR 3m by end 2028 (~27 months from Tomasz's September 2026 start)
- Capital at most EUR 1.5m total for Poland
- No margin floor stated — Germany's office business runs at 31% contribution margin; Poland's is unknown and untested
- No exit/kill criterion stated anywhere in the thread

## Is the market attractive?

| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size and growth | Two figures, not reconciled: Tomasz "80m+", scope and channel undefined, sourced to "I read that somewhere last year" (unsourced, pre-dates his own role). Study (EUR60k, June 2026): EUR48m/year, specifically *wholesale* office coffee in Warsaw, Kraków, Wrocław. Gap is ~67%, above the "about a third" threshold where the two numbers must be reconciled before either is used — and the scopes look different (nationwide vs. three-city wholesale), not just noisy. | Thread | **Fail — open.** Neither number is usable alone. |
| Concentration and incumbents | Not assessed. Tomasz flags competitive urgency ("before the Italians do") but no share data, no named competitors. | Thread (anecdotal) | Open |
| Barriers and regulation | Not raised in the thread. | — | Open |

## Can we win?

| Factor | Evidence |
|---|---|
| Customer need / switching | Tomasz met 4 distributors, 2 "keen" — one week of anecdote, no conversion rate, no deal terms. Weak evidence (single source, client's own new hire, no outside comparison). |
| Competitive position | Not assessed. |
| Capabilities | Germany office-coffee business exists (31% contribution margin) as a reference point, but nothing ties Poland's cost structure, pricing, or logistics to that number yet. |

## Entry modes

| Mode | Investment | Time to revenue | Control | Exit cost | Fit (provisional) |
|---|---|---|---|---|---|
| Distributor-led | Lower fixed cost; consistent with Tomasz's early conversations and with staying inside EUR1.5m | Faster | Lower | Lower — contracts can be unwound | Better fit for the budget and the ~27-month window, **directionally, pending unit economics** |
| Own sales office | Higher fixed cost (hires, vans, logistics, training) | Slower | Higher | Higher — severance, lease, inventory | Harder to justify against EUR1.5m and the timeline as currently stated |

This is a direction, not a decision — it is not built from named customer counts, win rates, or channel capacity, which the trap checks below call out explicitly.

## Business case (illustrative only — not a business case yet)

| | What we'd need | What we have |
|---|---|---|
| Revenue ramp | Office count × contract value × win rate, by year | None given |
| Margin | Poland contribution margin | Only Germany's 31%, unvalidated for Poland (ASSUMPTION if used) |
| Investment | Cumulative capex/opex to EUR3m revenue | EUR110k/yr (Tomasz, committed since Sept 2026) + EUR60k (study, spent June 2026) = ~EUR253k already run against the EUR1.5m cap by end-2028, assuming the cap includes both (ASSUMPTION — thread doesn't say) |
| Target check | EUR3m / EUR48m study-based SAM = 6.25% share of the three-city wholesale segment inside ~27 months, cold-start, no local brand presence | Not benchmarked — no comparable entry cited for how fast a new entrant typically takes share in this channel |

**So-what:** on the one number we can anchor (the EUR48m study figure, the narrower and better-sourced of the two), hitting EUR3m by 2028 requires a 6.25% share from zero in just over two years. That is not "1% of a big market," but it is also not nothing — and nobody has tested whether 2-of-4 distributor interest scales to that. The 80m figure, if used instead, would make the same target look trivial — which is exactly why the two numbers must be reconciled before anyone plans against either.

## Trap checks

- [ ] Share built bottom-up from customers, channel capacity, win rates — **No.** Only "2 of 4 distributors keen," no office counts or contract values.
- [ ] Customers, channels, price tested in Poland, not copied from home — **No.** Germany's 31% margin is the only reference point offered, and it is not Poland data.
- [ ] At least one aggressive incumbent reaction modelled — **No.** "Before the Italians do" is the only competitive signal; no incumbent named or sized.
- [ ] Sunk costs play no role in the recommendation — **No, and this is the headline finding.** Marc's email makes the study and the hire the reason to proceed ("we've already got Tomasz and the study, so we're going"). Both are already spent; neither pays back faster or slower depending on what Corvina decides next, so neither belongs in the go/no-go logic. They are reasons to decide *quickly* (the information and the person are available now), never reasons to enter.
- [ ] Ramp compared with comparable entries — **No.** No comparable launch cited; range should stay wide until one is found.
- [ ] Exit/kill criteria and exit cost written down before entry — **No.** Nothing in the thread sets a trigger for pulling out or a cost estimate for doing so.
- [ ] Compared with the best alternative use of the same EUR1.5m — **No.** Not mentioned once in the thread; Germany expansion or another market is the natural comparison and hasn't been run.

One check passes implicitly: the board did set a capital limit (EUR1.5m) and a revenue target (EUR3m by 2028), so there is *a* bar — it's just never been tested against a reconciled market size or a real ramp.

## What would change the answer

1. If the EUR48m study figure (not the 80m anecdote) reconciles cleanly with a bottom-up build from real office/contract counts, and the resulting SOM clears EUR3m with a plausible win rate, the answer moves toward "enter, distributor-led."
2. If Poland's contribution margin, once tested, sits far below Germany's 31%, the EUR1.5m cap may not buy enough ramp to reach EUR3m profitably, and the answer moves toward "enter later, smaller scope" or "don't."
3. If the local incumbent/competitive structure (the "Italians," or others) turns out to be concentrated and entrenched, that alone could kill the case regardless of size.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The EUR1.5m board cap includes the study and Tomasz's salary already spent | ~EUR253k of EUR1.5m already committed | Not stated in thread | If the cap is *additional* to what's already spent, ~EUR1.5m is still fully available — materially more room |
| 2 | Poland contribution margin is directionally like Germany's (31%) | 31%, flagged as unverified | Only reference point in thread | If Poland's real margin is far lower (new-market logistics, distributor take, FX), the budget buys much less ramp |
| 3 | The EUR48m study figure is the more relevant anchor for SAM (wholesale, office coffee, specifically) over Tomasz's 80m | EUR48m used in the share-of-target check | Study is a paid, defined-scope source vs. an unsourced recollection | If the 80m figure is actually the correct SAM once Tomasz's scope is clarified, the required share drops sharply and the case looks much easier |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What minimum margin, not just revenue, must Poland hit by 2028, and is EUR3m revenue meant as a milestone or a payback point? | Without a margin floor, "EUR3m revenue" can't be checked against the EUR1.5m cap for payback | Ines / the board | Could tighten or loosen the bar substantially |
| What exactly does the EUR48m study measure (channel, cities, customer segment, year), and does Tomasz's 80m use the same definition? | The two numbers can't be reconciled without the actual study — this is the single highest-value missing input | Ines (has the study); request "PL_study_final_v3.pdf," mentioned but not attached | Resolves the single biggest unknown in the case |
| How much capital and time will the board actually tolerate before pulling out, and is EUR1.5m a one-time cap or annual? | No exit criterion exists; without one, the business can keep spending indefinitely before anyone calls it | Marc / the board | Sets the real downside and when "no" becomes the answer |
| What would Corvina do with the same EUR1.5m and management attention if not spent on Poland (e.g. Germany expansion)? | The playbook's last branch — entry has to beat the next-best use of the same capital, not just clear its own hurdle | Marc / Ines | Could make "don't enter now" the right call even if Poland alone looks viable |
| What are the actual terms the 2 "keen" distributors are offering (volumes, margin take, exclusivity, minimums)? | This is the only real market evidence in the thread; right now it's an anecdote, not a data point | Tomasz | Would start a genuine bottom-up SOM build |
| Who are the incumbent or competitor players (the "Italians" Tomasz references), and what share do they hold? | High local concentration is often the fastest kill criterion for market entry | Tomasz / desk research once scope is clear | Could kill or reshape the case independently of size |

## Recommendation for 3 November

Don't bring "distributors or own sales" as the question. Bring: "Here is the reconciled market size, here is a bottom-up revenue path from the distributor conversations, here is what it implies against the EUR1.5m cap and the EUR3m target, and here is the exit trigger if it's wrong — on that basis, distributor-led entry is the better fit for the budget and timeline, confirm or adjust the bar." That reopens "whether" without relitigating the hire or the study — both stay, because they're already paid for — while stopping the board from rubber-stamping a channel choice nobody has tested.

