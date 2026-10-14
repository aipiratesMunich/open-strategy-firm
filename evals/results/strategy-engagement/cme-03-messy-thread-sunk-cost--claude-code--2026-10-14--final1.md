# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how" respecting CEO's request | yes | "Reopening 'whether' — the sharpened question... Should Corvina enter Poland (office-coffee wholesale) by end 2028, and if so how" |
| States EUR 60k study and hire already made are sunk; future country manager cost counts against budget | yes | "the EUR 60k study and Tomasz's salary paid *to date* are gone either way and should carry zero weight" and "Tomasz's future salary (Sept 2026 → end 2028, not yet paid) is a real forward cost that *does* count against the 1.5m cap" |
| Flags EUR 48m vs 80m+ conflict, uses study as base, asks for missing attachment | yes | "Pass, using the 48m figure — it's the better-sourced number. The 80m claim should be treated as unverified upside" plus open question: "What does the actual study (PL_study_final_v3.pdf) say..." |
| Puts 3m bar in proportion (~6%) and calls for bottom-up ramp, not share assumption | yes | "3m / 48m = 6.25% share of the 3-city segment needed by 2028... it's a real, checkable bottom-up target once distributor capacity is known" |
| Compares distributors vs own sales on cost, speed, control, exit cost using flagged assumptions | yes | Entry modes table with columns "Investment vs. EUR 1.5m cap / Time to revenue / Control / Exit cost" |
| Flags German 31% margin as untested for Poland | yes | "Only reference point is Germany's 31% contribution margin (different market, different channel structure — not directly transferable)" |
| Answer is conditional enter/enter later/do not enter with exit criteria, not unconditional go | yes | "Enter — but via a distributor-led model... and only as a phased, conditional commitment; own sales force... should be revisited in ~12 months" plus "What would change the answer" section listing kill/reshape triggers |
| Open-questions table names who can answer | yes | Table column "Who can answer" with entries "Ines / whoever holds the study", "Tomasz", "Ines / finance", "Board / Ines" |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | "No competitor names, pricing, or incumbent reaction data in the thread" and margin marked "Unknown" throughout |
| Does not treat "already hired and paid" as a reason in the recommendation | yes | Explicitly labeled as "sunk-cost reasoning" to be excluded, and recommendation instead rests on budget math and distributor fit |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

Written to `case-market-entry-corvina-poland.md`. Headline for Marc:

**Enter Poland, but via distributor, not own sales force — and say so for the right reason, not the one in the thread.**

- Marc's stated logic ("we've already got Tomasz and the study, so we're going") is sunk-cost reasoning — the EUR 60k study and salary paid *to date* are gone regardless of the decision and shouldn't drive it. What should drive it: Tomasz's **future** salary (~EUR 257k through end 2028) already eats ~17% of the board's EUR 1.5m cap before any sales spend, which on its own rules out building an own sales force in this window — that's a budget fact, not a preference.
- The two size estimates don't actually agree because they're not measuring the same thing: Ines's EUR 48m is a paid study scoped to 3 cities; Tomasz's "80m+" is an unsourced recollection, likely broader scope. Use the 48m as the planning number for Nov 3 and flag the 80m as unverified upside.
- Biggest hole: nobody has a Poland margin number. The board's 3m revenue target could be hit and still be a loss-making channel — that's worth flagging to Marc before it becomes a line in the board deck.
- The actual study PDF ("PL_study_final_v3.pdf") is referenced but wasn't in what you forwarded — worth chasing down before Nov 3 since the whole sizing argument rests on it.

Full case file has the sourced table, the budget arithmetic, and an open-questions list sized for a 3-week runway to the leadership meeting.


## Files in work dir after run

- case-market-entry-corvina-poland.md
- cme-03-input.md

## File written by the run: case-market-entry-corvina-poland.md

# Market entry: Corvina, Poland (office coffee wholesale), should we enter and how, for the 3 Nov 2026 leadership meeting

**Answer:** Enter — but via a **distributor-led model**, not own sales force, and only as a **phased, conditional** commitment; own sales force does not fit inside the board's EUR 1.5m cap and should be revisited in ~12 months if the distributor channel is tracking to plan.
**Confidence:** Low–medium. The size numbers triangulate roughly, and the budget math rules out one of the two modes cleanly — but margin, concentration, and a real bottom-up ramp are all missing from this thread. Treat this as the structure for the Nov 3 story, not a signed-off business case.
**Specialists and review:** none flagged yet from this thread (no regulatory/tax/labour detail given) — flag to legal/tax once a distributor or entity structure is chosen.

## Reopening "whether" — the sharpened question

Marc's ask was "tell us HOW: distributors or own sales." That skips "whether," and the stated reason — "we've already got Tomasz and the study, so we're going" — is **sunk-cost reasoning**: the EUR 60k study and Tomasz's salary paid *to date* are gone either way and should carry zero weight in the decision. Re-sharpened:

> Should Corvina enter Poland (office-coffee wholesale) by end 2028, and if so how, given it must deliver at least EUR 3m revenue by end 2028 within a EUR 1.5m total capital cap?

The board already supplied the minimum bar (3m revenue / 2028) and the capital ceiling (1.5m total) — that's the hard constraint everything below is tested against. Note Tomasz's **future** salary (Sept 2026 → end 2028, not yet paid) is a real forward cost that *does* count against the 1.5m cap, unlike the money already spent.

## Minimum bar agreed (from the board, via Ines)
- Revenue at least EUR 3m by end 2028
- Capital at most EUR 1.5m total for Poland
- Margin target: not set for Poland. Only reference point is Germany's 31% contribution margin (different market, different channel structure — not directly transferable)
- Kill criteria: none written down yet by the board — proposed below, needs sign-off

## Is the market attractive?

| Criterion | Finding | Source | Verdict |
|---|---|---|---|
| Addressable size | EUR 48m/yr (Warsaw, Kraków, Wrocław wholesale office coffee) vs. Tomasz's unsourced "80m+, I read that somewhere last year" (scope and recency unclear, likely national not 3-city) | Ines: company-paid study, June 2026, EUR 60k. Tomasz: anecdotal, no source | **Pass**, using the 48m figure — it's the better-sourced number. The 80m claim should be treated as unverified upside, not planning basis |
| Concentration / incumbents | No data in thread | — | **Open** — not testable from this thread |
| Barriers / regulation | No data in thread | — | **Open** — not testable from this thread |

3m / 48m = **6.25% share of the 3-city segment needed by 2028** (~26 months out). Not trivial, but not "1% of a big market" either — it's a real, checkable bottom-up target once distributor capacity is known.

## Can we win?

Only weak signal available: Tomasz met 4 distributors in his first weeks, 2 "keen." That's a single data point from one city over one week — real but far too thin to extrapolate a national ramp from. No competitor names, pricing, or incumbent reaction data in the thread.

## Entry modes

| Mode | Investment vs. EUR 1.5m cap | Time to revenue | Control | Exit cost | Fit |
|---|---|---|---|---|---|
| Distributor-led | Tomasz's forward salary (~EUR 257k, see below) + samples/van/trade terms — fits comfortably inside remaining ~EUR 1.2m | Fast — distributor interest already exists | Low — distributor owns the customer relationship and pricing | Low — no owned logistics/fleet to unwind | **Fits budget and timeline** |
| Own sales force | Needs warehouse/logistics, delivery fleet, and reps across 3 cities — typically a multiple of what's left after Tomasz's salary | Slow — hiring, training, route-building | High | High — leases, severance, fleet, inventory | **Does not fit the cap now** |

Tomasz's forward salary alone: EUR 110k/yr × ~28 months (Sept 2026 → end 2028) ≈ **EUR 257k**, already ~17% of the entire 1.5m cap before a single sample or van is bought. That arithmetic is the main thing that rules out own sales force as a 2026–2028 mode — it's not a judgment call, it's a budget constraint.

## Business case (base / low / high) — illustrative, not costed from real data

| | Low | Base | High |
|---|---|---|---|
| Revenue 2028 | EUR 1m (distributor interest fizzles) | EUR 3m (board bar) | EUR 5m (fast distributor scale-up) |
| Cumulative investment | ~EUR 0.8m | ~EUR 1.3m | ~EUR 1.5m (full cap) |
| Payback / margin | Unknown — no Poland margin assumption given | Unknown | Unknown |

All three rows are placeholders built only to show the shape of the case — **margin is the single biggest open item**: without a Poland contribution-margin assumption, nobody can say whether 3m of distributor-channel revenue is profitable or just a vanity number for the board slide.

## Compared with the alternative use of capital

Not testable from this thread — no alternative investment was named, and the board's EUR 1.5m cap reads as Poland-specific rather than a choice against another named lever. Worth a one-line check with the board before Nov 3, but it shouldn't hold up this recommendation.

## What would change the answer
1. If the actual study ("PL_study_final_v3.pdf," mentioned but not attached) shows the 48m figure is itself soft, or that 2–3 incumbents already hold most of the 3-city segment, kill or reshape the entry.
2. If Poland contribution margin, once modelled, comes in far below Germany's 31% (plausible — distributors take a cut), the 3m revenue target may not be worth the 1.5m even though it's achievable.
3. If distributor interest doesn't convert past the first 2 "keen" contacts in the following weeks, the ramp assumption underlying the whole case breaks.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Addressable segment | EUR 48m/yr, 3 cities | Paid study (Jun 2026), better-sourced than Tomasz's figure | Actual study shows materially lower/higher, or different scope |
| 2 | Poland margin | Not estimated; Germany's 31% used only as a reference point, not a Poland number | No Poland-specific figure in thread | A real Poland margin model comes in well below 31% |
| 3 | Own-sales investment | "A multiple of what's left in budget" — directional, not costed | Typical wholesale FMCG logistics/fleet buildout cost structure, not sized from Corvina data | Corvina has existing Polish logistics/partners that lower this materially |
| 4 | Tomasz forward cost | EUR 257k (110k/yr × 28 months) | Ines's stated salary and start date | Contract terms differ from stated annual rate |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does the actual study (PL_study_final_v3.pdf) say about methodology, scope and concentration? | The 48m figure and any share/incumbent data underpin the whole sizing argument | Ines / whoever holds the study | Could pass or kill the "attractive market" branch outright |
| What's the source and scope of Tomasz's "80m+" figure? | If credible, it loosens the share-needed math; if not, it should be dropped entirely from the Nov 3 deck | Tomasz | Changes stated upside, not the base case |
| What Poland-specific contribution margin is realistic through a distributor? | Without it, "3m revenue by 2028" is a top-line target with unknown profitability | Ines / finance | Could show the board's revenue bar is hit but still loses money |
| How many distributors like the 2 "keen" ones exist across all 3 cities, and what's a realistic win rate? | This is the only real bottom-up data point available and it's not yet sized | Tomasz | Turns the 6.25%-share target into a real ramp or exposes it as unreachable |
| Is the EUR 1.5m cap Poland-specific or could it compete with another investment? | Determines whether the "beats alternatives" branch needs testing | Board / Ines | Low effect on this recommendation, but relevant to how it's framed to the board |

