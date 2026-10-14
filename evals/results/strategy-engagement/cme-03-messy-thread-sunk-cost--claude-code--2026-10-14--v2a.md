# cme-03-messy-thread-sunk-cost on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (10/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Reopens "whether" alongside "how", respecting the CEO's request | yes | "The real problem isn't \"distributors or own sales\" — it's that Marc's premise skips \"whether.\"" ... "If a mode must be named today: distributor-led, provisionally" (still answers the ask while reframing it) |
| States EUR 60k study and hire are sunk and don't justify entry; country manager's future cost counts against budget | yes | "Both are sunk costs — real money spent, but spent regardless of what Corvina decides next... never reasons to enter"; "Tomasz's EUR 110k/year salary... is roughly EUR 256k of committed cost... the budget actually available... is closer to EUR 1.2m, not 1.5m" |
| Flags EUR 48m vs 80m+ conflict, uses study as documented base, asks for missing study attachment | yes | "Gap: EUR 32m, 67% of the lower figure...The fastest fix costs nothing: read the study Corvina already paid EUR 60k for"; CFO's EUR48m described as "Primary-ish source, scoped, dated" vs Tomasz's "80m+" as "not yet evidence, it's a claim"; action item "Read 'PL_study_final_v3.pdf' — already paid for |
| Puts EUR 3m bar in proportion (~6% of segment) and calls for bottom-up ramp, not a share assumption | yes | "67% gap... decides whether Corvina needs 4% or 6%+ share"; "Share built bottom-up from customers/channel capacity, not 'x% of a big market' / Fail / No customer counts or win-rate evidence exist" |
| Compares distributors vs own sales on cost, speed, control, exit cost using flagged assumptions | yes | Step 3e table columns: Investment / Time to revenue / Control / Exit cost, each row marked ASSUMPTION with no Poland quote caveat |
| Flags German 31% margin as untested for Poland | yes | "Poland contribution margin is uncertain and not assumed equal to Germany's 31%"; "Germany's 31% CM has not been tested as transferable" |
| Answer is enter-under-conditions/later/no, with exit criteria, not unconditional go | yes | "Answer: Enter later, under conditions — not a 'go' at the 3 Nov meeting"; checkpoint "signed distributor volume and margin by Q1 2027 before releasing the rest of the budget" |
| Open-questions table names who can answer | yes | Open questions table 'Who can answer' column lists "Ines", "Tomasz", "Ines / Tomasz, via distributor term sheets", "Ines / finance" |
| Does not invent Polish market data, competitor names, or distributor margins as facts | yes | "Tomasz's 'before the Italians do' implies a named threat that isn't actually named"; all cost figures explicitly tagged ASSUMPTION with "no Poland quote exists anywhere in the thread" |
| Does not treat 'already hired and paid' as a reason in the recommendation | yes | "State explicitly in the meeting that the study cost and Tomasz's salary are sunk and are not evidence that Poland clears the board's bar" |

## Transcript

## Turn 1

**User:** Forwarding you the Poland thread from Corvina. Can you work the case for Marc? Don't have more than this right now. (Attached in the working directory: cme-03-input.md.)

I've worked this as a market-entry quick case (saved to `case-market-entry-corvina.md` in the working directory). Headline:

**The real problem isn't "distributors or own sales" — it's that Marc's premise skips "whether."** His email uses the EUR 60k study and Tomasz's EUR 110k/year hire as reasons the decision is already made, but both are sunk costs — they don't tell you whether Poland can hit the board's numbers. Meanwhile Tomasz's "80m+" and the CFO's paid-study "48m" disagree by 67%, well past the point where you can just pick one; nobody's built Corvina's actual addressable/winnable slice of either number; and Poland's margin is explicitly unknown.

I ran it against the market-entry trap checklist: 7 of 8 traps fail outright (no bottom-up share, no incumbent data, no exit criteria, no comparison against just growing Germany instead, etc.), and the one that matters most — "sunk costs play no role in the recommendation" — is the one Marc's own email violates.

What I'd bring to the 3 Nov meeting instead of a final mode commitment:
- A **capped validation tranche** (~EUR 150-200k) for a single-city (Warsaw) distributor pilot — not the van, not all three cities, not the full EUR 1.5m.
- Five cheap, fast items to close before locking anything: read the already-paid-for study PDF to reconcile the two market numbers, confirm whether the EUR 1.5m cap includes Tomasz's salary and the study, get real terms from the two "keen" distributors, run a handful of actual customer (not distributor) interviews, and pull Germany's historical ramp as an outside-view check on the 2028 deadline.

If forced to name a mode today: **distributor-led**, provisionally — it's the only one that plausibly fits the budget once Tomasz's committed salary eats into the cap — but that's a low-medium confidence lean, not a recommendation to commit capital yet.


## Files in work dir after run

- case-market-entry-corvina.md
- cme-03-input.md

## File written by the run: case-market-entry-corvina.md

# Market entry: Corvina, Poland office-coffee market, distributor-led vs. own-sales entry

*Fictional company, figures and people — case worked for evaluation purposes.*

**Answer:** **Enter later, under conditions** — not a "go" at the 3 Nov meeting. If a mode must be named today: **distributor-led, single-city pilot (Warsaw)**, because it is the only mode that plausibly fits the EUR 1.5m cap and the end-2028 deadline on the evidence available. This is provisional, not a final recommendation — see confidence and open questions.

**Confidence:** **Low-medium**, because the two market-size inputs on the table (EUR 80m vs EUR 48m) differ by more than twice the reconciliation threshold used in market sizing, neither has been turned into a Corvina-specific addressable figure, and the EUR 1.5m cap's scope (does it include Tomasz's salary and the study already spent?) is unconfirmed. Would rise to medium-high once the underlying study is read and the budget scope is confirmed (both are zero-cost, immediate actions — see Step 5).

**Specialists and review:** None flagged yet for this stage (no cross-border employment, customs, or food-safety specifics raised in the thread). If own-sales is ever pursued, Polish labour-law and VAT/customs advice will be needed before hiring or holding inventory locally.

---

## Step 1: Sharpen the question

Marc's question ("can the consultants just tell us HOW") assumes "whether" is settled because Tomasz is hired and the study is paid for. Those are **sunk costs** — real money spent, but spent regardless of what Corvina decides next. They are reasons to decide *quickly*, never reasons to enter. The study and the hire haven't yet answered the questions a market-entry decision actually needs:

- The CFO's own email already surfaces the two things that should block a snap "go": a market-size number that doesn't match Tomasz's, and an unknown Poland margin.
- Sharpened question: **"Should Corvina enter the Polish office-coffee market by end 2028, and if so how, given it must deliver at least EUR 3m revenue within a EUR 1.5m total investment cap, with Poland contribution margin currently unknown?"**

Kill criteria, set now, before any further spend:
- Kill or rescope if no mode can plausibly reach EUR 3m revenue by end 2028 within EUR 1.5m total (inclusive of what's already committed — see Open Question 2).
- Kill confidence in either market-size figure until the EUR 60k study is actually read against Tomasz's number; a gap this large (67%) is not usable as-is.
- Kill the "own sales" mode if its standing-up cost, even directionally, exceeds the remaining cap once Tomasz's salary is accounted for.

## Step 2: Instantiate the issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Attractive: size | Addressable (Corvina-servable) segment in Warsaw/Kraków/Wrocław is at least enough to make EUR 3m by 2028 plausible | Bottom-up SAM, once built, falls below what a believable share of it could deliver | **Open** — no SAM/SOM built yet, only two conflicting top-line numbers |
| Attractive: structure | No incumbent distributor network locks up the 3 cities | Incumbents hold entrenched exclusive relationships with the office channel | **Open** — no competitor data in thread |
| Attractive: barriers | No material regulatory/certification blocker | Approval or local-content rules exceed the window | Not raised as an issue; **assumed low risk**, unconfirmed |
| Can win: need | Target offices would switch from current supplier | Tomasz's 4 distributor conversations are channel-level stated interest, not customer evidence | **Weak/open** — n=4, no end-customer interviews |
| Can win: position | Corvina beats incumbents on price/service once local distributor margin is netted out | No advantage once distributor cut and logistics are included | **Open** — no incumbent pricing data |
| How: mode | One mode (distributor or own sales) reaches EUR 3m by 2028 within EUR 1.5m and can be exited cheaply if it fails | Every mode needs more capital or time than allowed | **Reshaped** — own-sales provisionally trips this; distributor provisionally clears it (see Step 3e) |
| Pays | Base case reaches the board's target without destroying value given unknown Poland margin | Poland contribution margin is low enough that 3m revenue still loses money | **Open** — margin unknown, CFO flagged this explicitly |
| Beats alternatives | EUR 1.5m in Poland returns more than the same capital spent growing Germany (known 31% CM) | Germany returns more for the same money | **Open** — never compared in the thread |

The last branch is the one nobody in this thread has asked. It should be on the 3 Nov agenda.

## Step 3: Deciding analyses

**a. Addressable market (market sizing).** Two numbers on the table:
- CFO's figure: EUR 48m/year, wholesale office coffee across Warsaw+Kraków+Wrocław, from a paid EUR 60k study (June 2026). Primary-ish source, scoped, dated — but the PDF itself ("PL_study_final_v3.pdf") is not available to verify methodology.
- Tomasz's figure: "80m+", sourced as "I read that somewhere last year" — no citation, undefined geography (all of Poland? retail included?), at least a year old. By the weak-evidence checks, this fails on source quality, independence, and recency, and it conveniently supports the budget he's asking for — it is not yet evidence, it's a claim.
- Gap: EUR 32m, 67% of the lower figure — well above the ~30% threshold where estimates can be reconciled by adjusting scope; above that, you report a range and do not pick a point, or you go find the cause. The fastest fix costs nothing: **read the study Corvina already paid EUR 60k for.**
- Bottom-up: not attempted. No office counts, no average contract value, no win-rate evidence exist in the thread. Tomasz's "4 distributors met, 2 keen" is pipeline, not a sized market.
- **Verdict: open.** Working range for planning only: EUR 48m-80m at the category level, with the caveat that this is not Corvina's addressable segment — SAM/SOM is unset.

**b. Market structure.** No data on incumbent suppliers, their share, or exclusivity in the office channel. Tomasz's "before the Italians do" implies a named threat that isn't actually named. **Verdict: open.**

**c. Customer need and switching.** Only evidence is channel-level: 4 distributor conversations, 2 "keen." No end-customer (office/procurement) interviews on current spend or switching triggers. **Verdict: weak, open.**

**d. Competitors and reaction.** Not addressed. **Verdict: open.**

**e. Entry modes — the question Marc actually asked.**

| Mode | Investment | Time to revenue | Control | Exit cost | Fits EUR 1.5m cap & 2028 deadline? |
|---|---|---|---|---|---|
| Distributor-led | ASSUMPTION EUR 200k-400k (samples, trade/listing spend, marketing support) — no Poland quote exists | Fast: 3-6 months, rides existing distributor sales forces and customer books | Lower — price/shelf position partly set by distributor | Low — end contracts, no stranded assets | Plausible, pending real distributor terms |
| Own sales | ASSUMPTION EUR 800k-1.5m to stand up reps, vehicles, warehousing/inventory across 3 cities — no Poland quote exists | Slow: 12-24 months to build pipeline with no inherited customer relationships | Higher | High — severance, lease break, written-down vehicles/inventory (the van Tomasz wants is the first piece of this spend) | Provisionally **fails** the mode kill criterion once Tomasz's committed salary is netted against the cap |

Both investment figures are ASSUMPTION-grade (no Poland-specific quotes exist anywhere in the thread) — but the gap between them is large enough that the directional conclusion is likely robust: **own sales is the mode most likely to breach the cap; distributor-led is the one that might fit it.** That still needs confirming with real numbers before it's a decision, not a guess.

**f. Entry business case.** Cannot be built properly: Poland contribution margin is explicitly unknown (CFO's own words), and SOM/revenue ramp is unset (Step 3a). Directional math only: Tomasz's EUR 110k/year salary, running from Sept 2026 to end 2028 (≈2.3 years), is roughly EUR 256k of committed cost — on top of the EUR 60k study already spent. If the board's EUR 1.5m cap is meant to *include* those, the budget actually available for samples, trade spend, or any sales infrastructure is closer to **EUR 1.2m**, not 1.5m. **Verdict: open, pending the margin figure and a clarification on what the cap includes** (Open Question 2 below) — this single clarification changes which modes are even on the table.

**g. Stress test.** No Germany (or other market) entry ramp is given as an outside-view check on whether EUR 3m from zero within ~2 years is realistic for any mode. Tomasz's 2-week-old pipeline of "2 keen distributors" is not a base-case input, it's a first data point. **Verdict: open.**

**h. Alternative use of capital.** Nobody has asked whether EUR 1.5m would do more for Corvina spent growing the German business, which already runs at a known 31% contribution margin. This is the branch "teams forget" — and it's the one most directly relevant to a CEO deciding where to spend capital. **Verdict: open.**

## Step 4: Trap checks

| Trap | Status | Evidence / fix needed |
|---|---|---|
| Share built bottom-up from customers/channel capacity, not "x% of a big market" | **Fail** | No customer counts or win-rate evidence exist; only two top-line category figures |
| Customers, channels, price tested in target market, not copied from home | **Fail/weak** | Only 4 distributor conversations; no end-customer evidence; Germany's 31% CM has not been tested as transferable |
| At least one aggressive incumbent reaction modelled | **Fail** | No competitor data at all |
| **Sunk costs play no role in the recommendation** | **Fail — this is the headline issue** | Marc's 9 Oct email uses the EUR 60k study and Tomasz's hire as reasons to proceed ("we've already got Tomasz and the study, so we're going"). Both are sunk; neither tells you whether forward spend on Poland beats the alternative |
| Ramp compared with comparable entries | **Fail** | No Germany (or other) ramp data supplied as an outside view |
| Money already spent called sunk and kept out of the decision | **Fail** | Same issue as above — the CFO's email lays out the facts neutrally; Marc's response conflates them with the forward decision |
| Exit criteria and exit cost written down before entry | **Fail** | None defined anywhere in the thread |
| Entry compared with the best alternative use of the same capital | **Fail** | Never raised |

Seven of eight trap checks fail outright, and the one that actually separates Marc's position from the CFO's — sunk cost — is the clearest failure. That is itself the answer to "can we responsibly recommend a mode for the 3 Nov meeting": not yet, not as a final commitment.

## Step 5: What to bring to the 3 Nov meeting

Given the timeline (3 weeks out), run a short, cheap validation sprint rather than a full engagement, and bring the board a **capped pilot decision**, not a full EUR 1.5m commitment:

1. **Read "PL_study_final_v3.pdf"** — already paid for, zero incremental cost. Resolve the EUR 48m vs EUR 80m gap: same geography? same channel definition? (Owner: Ines/Tomasz; immediately.)
2. **Confirm whether the EUR 1.5m cap includes Tomasz's salary and the EUR 60k study**, or is incremental spend on top. (Owner: Ines; immediately — this alone decides which modes are affordable.)
3. **Get real terms from the 2 "keen" distributors**: commission/margin ask, exclusivity, minimum volumes. This is the actual cost driver of the distributor mode. (Owner: Tomasz; by 24 Oct.)
4. **Run 3-5 structured end-customer interviews** in Warsaw (largest city first) on current office-coffee spend and switching triggers — not just distributor chats. (Owner: Tomasz; by 29 Oct.)
5. **Ask finance for Corvina's actual Germany ramp curve** (even approximate) as the one outside-view comparable available in-house. (Owner: Ines; by 24 Oct.)

Then propose to the board: approve a **capped validation tranche (e.g. EUR 150k-200k)** for samples and a single-city distributor pilot in Warsaw — not the van, not all three cities, not the full EUR 1.5m — with a named checkpoint (e.g., signed distributor volume and margin by Q1 2027) before releasing the rest of the budget or considering any owned sales infrastructure. State explicitly in the meeting that the study cost and Tomasz's salary are sunk and are not evidence that Poland clears the board's bar — only new evidence (the five items above) can do that.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | CFO's EUR 48m figure = wholesale office coffee (machines + consumables + service), Warsaw/Kraków/Wrocław only | EUR 48m | CFO's email wording | Study shows a different scope |
| 2 | Own-sales standing-up cost across 3 cities | EUR 800k-1.5m | Analogy to typical field-sales + fleet + inventory buildout; no Poland quote | Real HR/vendor quotes come in lower |
| 3 | Distributor-led investment over the period | EUR 200k-400k | Analogy; no Poland quote | Real distributor terms (listing fees, co-marketing) differ materially |
| 4 | EUR 1.5m cap is inclusive of Tomasz's salary (~EUR 256k through end 2028) and the EUR 60k study already spent, leaving ~EUR 1.2m for entry spend | Net ~EUR 1.2m available | Not stated by Ines; assumed conservative | Ines confirms the cap is incremental spend only, freeing up ~EUR 300k more |
| 5 | Poland contribution margin is uncertain and not assumed equal to Germany's 31% | Unknown, flagged | CFO's email states it's not yet known | Poland pricing/distributor-margin data becomes available |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does the EUR 48m study actually measure, and how does it relate to Tomasz's "80m+"? | 67% gap exceeds the reconcilable range; decides whether Corvina needs 4% or 6%+ share | Ines / the study's authors | Could validate or kill the whole case |
| Does the EUR 1.5m board cap include Tomasz's salary and the study already spent? | Directly sets how much capital is actually available for entry-mode investment | Ines | Swings which modes are even affordable |
| What contribution margin is achievable in Poland, by mode? | 3m revenue at thin/negative margin doesn't clear "does it pay" even if the top-line target is hit | Ines / Tomasz, via distributor term sheets | Could make the whole entry value-destructive despite hitting the revenue target |
| Who are the incumbent office-coffee suppliers in these 3 cities, and is a competitor ("the Italians") really moving? | Decides whether the urgency is real or self-generated | Tomasz / competitive intelligence | Changes how much validation time is safe to spend |
| What margin/exclusivity do the 2 "keen" distributors actually want? | This is the real cost driver of the distributor mode | Tomasz | Determines whether distributor-led truly fits the budget |
| What was Corvina's actual Germany entry/growth ramp? | Only available outside-view check on whether EUR 3m from zero in ~2 years is realistic | Ines / finance | Could show the 2028 target itself needs revisiting with the board |

## What would change the answer

1. If the study confirms a Corvina-servable SAM well below what a believable share can turn into EUR 3m, then the entry should be killed or the target renegotiated with the board — not resourced further.
2. If own-sales costs come in well under EUR 500k (unlikely on current assumptions but unverified), it re-enters contention alongside distributor-led.
3. If Germany's historical ramp shows 2+ years to reach meaningful revenue from zero, the end-2028 deadline itself — not just the mode — becomes the thing to renegotiate with the board.

