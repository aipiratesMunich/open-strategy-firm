# cme-02-huge-tam-tiny-sam on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens 'whether' before 'how' and states the minimum bar (USD 10m by 2030, USD 4m) as the test. | yes | "Recommendation: don't enter on these terms..." and "Revenue at least $10m by 2030; capital at most $4m" / "Kill criterion (applied below): if the bottom-up addressable pool... still falls short of $10m, the current entry plan is killed." |
| Narrows the market step by step to about USD 13.5m serviceable, with each step and source. | yes | Table: $9bn (adviser, unsourced) × 2.5% = $225m (adviser appendix) × 20% = $45m (product team estimate) × 30% = $13.5m (distributor estimate). |
| States that USD 90m exceeds the serviceable segment several times over (about 6.7x) and rejects '1% of a big market' as a method. | NO | Rejects the method ('The "1% of a big market" trap... is exactly what the adviser's slide falls into') but never computes or states the ~6.7x multiple of $90m over the $13.5m serviceable segment; it only contrasts $90m against the $45m SAM qualitatively, not a stated ratio against $13.5m. |
| Builds a share/revenue estimate bottom-up from distributor's reach and Halvorsen's own best share, showing it misses USD 10m. | yes | "Optimistic (hits all-time-best share instantly...) 30% ... ~$4.1m" against the $13.5m reachable pool, explicitly below the $10m floor ('60% short of the board's floor'). |
| Answer is do not enter, or enter later under named conditions, with what would make the board revisit it. | yes | "Do not enter on the terms the adviser and distributor have put on the table. Enter later, in modified form, only if a US certification + calibration investment case clears the $4m cap" plus 'What would change the answer' section. |
| Flags the USD 9bn as unsourced adviser figure and the 20%/30% as internal/distributor estimates to verify, without inventing US figures. | yes | "Adviser slide, unsourced" / "Halvorsen product team estimate... untested with buyers" / "Distributor's own estimate... self-interested source". |
| Notes that US certification and regulatory questions go to specialists. | yes | "Specialists and review: regulatory affairs (US instrument certification pathway and timeline), calibration/accreditation specialist..." |
| Must not propose an entry plan whose base case relies on a percentage of the USD 9bn. | yes | Base case uses the $13.5m/$45m bottom-up figures, not a percentage of $9bn; the $90m framing is explicitly rejected. |
| Must not cite US market reports, regulators' rules or competitor shares as facts. | yes | No external market reports, regulator rules, or competitor share figures are cited as facts; timelines like '1–2+ years' are explicitly marked ASSUMPTION. |

## Transcript

## Turn 1

**User:** Our adviser says the US is a USD 9bn market and we only need 1%. The board likes it. How should Halvorsen enter the US? Notes attached. (Attached in the working directory: cme-02-input.md.)

## Bottom line for the board conversation

The adviser's $90m is a "1% of a big market" fallacy — it assumes Halvorsen competes for the whole $9bn, when it sells one product line that's 2.5% of that ($225m), and today only 20% of that sub-segment's buyers will accept EU-certified gear with no US calibration backing it. That's a **$45m real addressable market**, not $9bn. Of that, only **$13.5m** is reachable through the distributor contract actually on offer.

Run that $13.5m through Halvorsen's own best-ever performance (30% share in Germany, over 12 years, in a market without the US certification/calibration gap) compressed into the board's 4-year window, and realistic 2030 revenue lands at **$1–4m** — even the most generous reading (hitting that all-time-best share instantly) tops out around $4m. To hit the board's $10m floor off this deal would require a 74% share nobody at Halvorsen has ever come close to.

**Recommendation: don't enter on these terms.** The only lever that changes the ceiling is removing the certification/calibration gap (unlocks the full $225m segment instead of $45m) — but that cost and timeline aren't known yet, so it's not fundable against the $4m cap without a specialist quote first. Full reasoning, the ramp math, entry-mode comparison, and the open questions (adviser's unsourced $9bn, distributor's self-reported coverage, certification cost/timeline, competitive concentration, alternative use of the $4m) are in `case-market-entry-halvorsen.md`.


## Files in work dir after run

- case-market-entry-halvorsen.md
- cme-02-input.md

## File written by the run: case-market-entry-halvorsen.md

# Market entry: Halvorsen Instruments, US benchtop electrochemistry, how to enter

**The adviser's number is wrong, and not by a small margin.** $9bn × 1% = $90m assumes Halvorsen can compete for the whole US lab instruments market. It sells one product line into one sub-segment, and today only a fifth of that sub-segment's buyers will even consider an EU-certified instrument with no US calibration network. The realistic serviceable market is **$45m**, not $9bn — and the revenue actually reachable through the distributor offer on the table is **$13.5m**. Against that, the board's $10m-by-2030 bar requires a 74% share of the reachable pool, achieved in a third of the time it took Halvorsen to win its best-ever share (30%, Germany, twelve years) in an easier market.

**Answer:** Do not enter on the terms the adviser and distributor have put on the table. Enter later, in modified form, only if a US certification + calibration investment case clears the $4m cap — see conditions below.
**Confidence:** medium — the share-of-segment figures trace to Halvorsen's own appendix/product team (reasonable, not independently verified); the $9bn headline and the distributor's coverage claim are both unsourced/self-interested and need checking; the Germany benchmark is Halvorsen's own actual result, the strongest evidence here, but it's a single comparable and the US starts with a handicap Germany didn't have.
**Specialists and review:** regulatory affairs (US instrument certification pathway and timeline), calibration/accreditation specialist (cost and time to stand up or partner for ISO/IEC 17025-type local calibration), independent market-research check on the $9bn and distributor-coverage figures.

## Minimum bar agreed with board
- Revenue at least $10m by 2030; capital at most $4m
- Kill criterion (applied below): if the bottom-up addressable pool, run through Halvorsen's own best-ever market-share performance compressed to the 2030 deadline, still falls short of $10m, the current entry plan is killed.

## Is the market attractive? — bottom-up vs. the adviser's top-down

| Step | Figure | Source | Evidence grade |
|---|---|---|---|
| Adviser's claim | $9bn × 1% = **$90m** | Adviser slide, no source | Weak — wrong unit of analysis (1% of a market Halvorsen barely touches, not 1% of its own segment) |
| Total US lab instruments market | $9bn | Adviser slide, unsourced | Weak — flag for independent check |
| × Benchtop electrochemistry share | 2.5% → **$225m** | Adviser's own appendix | Medium — same source family as above, but at least the relevant one |
| × In-house-calibration acceptance (buyers who'd take EU-certified gear with no US cal network) | 20% → **$45m = true SAM today** | Halvorsen product team estimate | Medium — internal estimate, untested with buyers |
| × Distributor's geographic coverage | 30% → **$13.5m = reachable via this contract** | Distributor's own estimate | Weak — self-interested source, and assumes its coverage overlaps proportionally with the in-house-calibration buyers specifically (unverified) |

**Verdict: hypothesis reshaped.** The addressable segment is $45m, not $9bn and not even the $225m sub-category — and only $13.5m of that $45m is reachable through the distributor deal actually on offer. The "1% of a big market" trap (market-entry playbook) is exactly what the adviser's slide falls into: no bottom-up path from the $9bn to an actual customer.

## Can we win? — the Germany benchmark under a compressed timeline

Halvorsen's own best result anywhere is 30% of its addressable segment in Germany — reached over **twelve years**, in a market where it had full local certification and calibration support from day one (no equivalent of the US 80%-exclusion gap).

2026→2030 is **four years** — a third of that timeline, in a harder starting position.

| Scenario | Share by 2030 | Basis | Revenue (vs. $13.5m reachable pool) |
|---|---|---|---|
| Outside-view pace (Germany's average ramp, ~2.5pp/yr) | ~10% | 4/12 × 30% | ~$1.4m |
| Optimistic (hits all-time-best share instantly, 3× faster than ever achieved) | 30% | Germany's ceiling, no ramp-up period | ~$4.1m |
| Required to hit board's bar | 74% | $10m / $13.5m | Not achieved anywhere by Halvorsen; implausible |
| Required to hit bar off the full $45m SAM (needs reach beyond this one distributor) | 22% | $10m / $45m | Still approaches the Germany ceiling, in 1/3 the time, against a tougher structural handicap |

**Verdict: "pays" hypothesis killed under every scenario tested.** Even the unrealistic case (best-ever share, no ramp period) lands at ~$4m — 60% short of the board's floor. The realistic range is **$1m–$4m by 2030**, not $10m and nowhere near $90m.

## Entry modes

| Mode | Investment | Time to revenue | Ceiling | Fit vs. $4m cap / 2030 date |
|---|---|---|---|---|
| Distributor only (offer on the table) | Low, likely well inside $4m (ASSUMPTION — no contract terms given) | Fast (quarters) | ~$13.5m pool → realistic $1–4m by 2030 | Fits budget and timeline; caps revenue far below the board's bar |
| Distributor + US certification/local calibration partnership | Unknown, plausibly >$4m (ASSUMPTION — needs vendor/specialist quote) | Slow — accreditation pathways typically run 1–2+ years (ASSUMPTION) | Unlocks full $225m segment, not just $45m | Likely breaches both the capital cap and the 2030 date as currently scoped |
| Own US sales/service office | High | Slow | Full segment, eventually | Not viable at $4m |

No mode reaches $10m by 2030 inside $4m. Mode B (certification + calibration) is the only path that changes the ceiling, but it needs a costed investment case before anyone can say whether it fits $4m — that case doesn't exist yet.

## Compared with the alternative use of capital

Not assessed — no data was given on what else Halvorsen could do with $4m (e.g., deepen EU share, adjacent product line). This is an open question, not a reason to default toward entry; the market-entry playbook's last branch ("beats alternatives") is the one teams forget, and it's unanswered here.

## What would change the answer

1. If a certification/calibration specialist costs Mode B at or under $4m with a credible path to market within the window, revisit — this is the only lever that moves the ceiling above $45m.
2. If the distributor's 30%-coverage claim and the product team's 20%-acceptance estimate are independently verified higher, the reachable pool grows and the gap narrows — but even doubling both still leaves the pool under $10m at Germany-pace share.
3. If the board is willing to reset the target to $1–4m by 2030 as a deliberate toehold/learning entry (not a growth bet), the distributor deal alone is a defensible low-cost move — but that is a different decision than the one the board thinks it's making.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | US lab instruments market size | $9bn | Adviser slide, unsourced | Verified materially lower or higher — moves absolute $ but not the structural conclusion (share required stays the binding constraint) |
| 2 | Distributor's coverage overlaps proportionally with in-house-calibration buyers | Applied 30% directly to the $45m SAM | Not stated in distributor's offer | If distributor's footprint skews toward regulated (not in-house-cal) labs, reachable pool is smaller than $13.5m |
| 3 | Distributor contract cost | Assumed low, within $4m | Not given | If onboarding/exclusivity terms are costly, budget for Mode B shrinks further |
| 4 | Germany ramp was roughly linear | 2.5pp share/year average | Only the 12-year endpoint given | If Germany's actual ramp was back-loaded (slow start, fast finish), the 4-year outside-view share is even lower than 10% |
| 5 | Mode B (certification + calibration) cost and timeline | >$4m, 1–2+ years | No vendor/specialist quote obtained | If a specialist quotes it under $4m with <2 year lead time, Mode B becomes viable within the board's window |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does US instrument certification + local calibration accreditation actually cost and take to stand up? | Determines whether Mode B fits the $4m cap and 2030 date — the only lever that raises the ceiling above $45m | Regulatory affairs / calibration accreditation specialist, vendor quotes | Could flip the recommendation from "do not enter" to "enter via Mode B" if costed under budget |
| Is the $9bn headline and the 2.5% segment share independently verifiable? | Adviser's own slide is unsourced; segment share comes from the same adviser's appendix | Independent market research (e.g., trade body, third-party market report) | Confirms or revises the $45m SAM base |
| Is the distributor's 30%-coverage estimate accurate, and does it overlap with in-house-calibration buyers specifically? | Self-reported by an interested party; determines the $13.5m reachable figure | Direct diligence on the distributor's customer list/territory | Could raise or lower the reachable pool materially |
| What's the competitive structure in the $45m SAM — how concentrated, who are the incumbents? | Market-entry tree's "can we win" branch is untested here; high incumbent concentration could kill the case independently of the size math | Competitor profiling / channel checks | Could surface an additional kill criterion even if the size math were fixed |
| What else could $4m and management attention earn if spent on the EU core or another lever? | The market-entry tree's last branch — entry must beat the alternative, not just clear its own bar | Internal strategy/finance | Could show the $4m is better spent elsewhere even if Mode B were costed favorably |

