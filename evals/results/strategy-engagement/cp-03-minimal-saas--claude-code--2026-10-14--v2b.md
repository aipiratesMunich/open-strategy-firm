# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | No clarifying questions asked up front; assistant proceeds directly with an explicit 'Assumptions' table (contribution margin, homogeneity, contract lock-in) and an 'Open questions' table at the end. |
| Computes price change ~22.5% and break-even loss via 1 - m/(m+p), arithmetic consistent with margin used | yes | 'Price change: p = (109−89)/89 = 22.5%' and 'Break-even volume loss ... 1 − 0.85/(0.85+0.225) = 1 − 0.791 = 20.9%' — matches m=0.85 reference exactly. |
| Flags gross margin is not contribution margin, states which value used and why | yes | 'using your 85% gross margin as a proxy for contribution margin — this is an assumption; it's valid here specifically because SaaS cost-to-serve ... doesn't scale with the price you charge' |
| Translates break-even into churn terms | yes | 'break-even churn = current churn / (1 − break-even loss) = 2% / 0.791 = 2.53%/month' and 'monthly churn would have to rise from 2.0% to above ~2.5%' |
| Names structure options (tiers, grandfathering, annual prepay, etc.) as questions to test rather than only a single level change | yes | 'a flat +€20 is a bigger relative hit to a one-vet practice than a five-vet hospital... segmentation by clinic size' and 'Might recommend grandfathering existing customers and raising for new signups first, as a lower-risk test' |
| Gives provisional answer with confidence low/medium and what would change it | yes | 'Confidence: medium' and 'What would change the answer: if churn ticks up past ~2.5%/month after rollout, or competitor benchmarking shows...' |
| Names revealed-behaviour data that would settle willingness to pay and treats survey as a range | NO | Only generically notes '[ ] Open — stated vs. revealed willingness to pay not checked (no interview/survey data)' — never names concrete revealed-behaviour sources (e.g. win/loss on recent deals, reactions to past price changes, churn reasons) nor discusses treating any survey result as a range. |
| Does not invent competitor prices or industry benchmarks as facts | yes | 'I don't have competitor pricing (ezyVet, Provet Cloud, Digitail, IDEXX Neo, Covetrus Pulse, etc.) and shouldn't state it from memory.' |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

No problem — I'll proceed without external benchmarking and flag that as an open item instead. Here's the quick case.

## Step 1: Sharpen the question

Decision question: **"By how much can Vetrona raise list price per clinic in the next renewal cycle without pushing monthly churn above the break-even level, and what's the margin effect?"** This is a **price level** decision (not structure or execution — single flat per-clinic fee, no tiers mentioned).

Missing info I'm assuming for a provisional answer (flagged below): whether the increase applies to new customers only or also existing ones, and whether clinics are homogeneous or split by size (solo-vet vs multi-vet practices).

## Step 2: Issue tree (instantiated)

| Branch | Hypothesis | Kill criterion |
|---|---|---|
| Value | €20/mo is small relative to a vet clinic's revenue and switching cost | Clinics are price-sensitive on this line item specifically |
| Position | No competitor benchmark in hand | — flagged, not tested here |
| Volume reaction | Expected churn increase stays well below break-even churn | Churn jumps near/above break-even on rollout |
| Execution | Increase reaches pocket price (no discount creep) | Sales/CS grants ad-hoc exceptions that erode it |
| Structure | Flat fee may not fit — large multi-vet clinics likely underpriced, solos may be at their ceiling | n/a this round |

## Step 3: Deciding analyses

**3e. Break-even volume / break-even churn** (the one piece of hard data you gave me is enough to run this):

- Price change: p = (109−89)/89 = **22.5%**
- Contribution margin: using your 85% gross margin as a proxy for contribution margin — **this is an assumption**; it's valid here specifically because SaaS cost-to-serve (hosting, support) doesn't scale with the price you charge, so it's reasonable, but worth confirming with finance that no variable cost (e.g., payment processing, usage-based infra) actually does scale with price.
- Break-even volume loss for a price increase: `1 − m/(m+p) = 1 − 0.85/(0.85+0.225) = 1 − 0.791 = 20.9%`
- Translating to churn (steady-state customer base ∝ 1/churn): `break-even churn = current churn / (1 − break-even loss) = 2% / 0.791 = 2.53%/month`

**So-what:** monthly churn would have to rise from 2.0% to above ~2.5% (a +26% relative jump, +0.5pp) before this price increase destroys more profit than it creates. That's a real margin of safety, not a knife's edge.

**3b. Price benchmark** — not run. I don't have competitor pricing (ezyVet, Provet Cloud, Digitail, IDEXX Neo, Covetrus Pulse, etc.) and shouldn't state it from memory. This matters: if €89→€109 moves you from "cheapest" to "mid-pack or above," the volume reaction could be worse than a pure churn-trend extrapolation suggests. **Open question, see below.**

**3f. Segmentation** — not run, but flagged as a trap below: a flat +€20 is a bigger relative hit to a one-vet practice than a five-vet hospital. Worth checking if your base splits that way and whether value delivered (and willingness to pay) scales with clinic size.

## Step 4: Trap checks

- [x] Cost sets the floor only — price anchored on the break-even/value logic above, not cost-plus.
- [ ] **Open** — stated vs. revealed willingness to pay not checked (no interview/survey data).
- [ ] **Open** — uniform increase trap: no segmentation by clinic size run.
- [ ] **Open** — execution: no mention of whether existing contracts allow a mid-term increase or only renewals; discount/grandfathering rules not defined.
- [x] Break-even computed with contribution margin, expected churn compared against it.
- [ ] **Open** — sales/CS messaging and objection-handling not planned.
- [x] No competitor pricing coordination involved — fine on competition-law grounds.

## Answer page

**Answer:** Raise list price to €109/month for new customers now; the break-even churn (2.53%/mo vs. your current 2.0%) gives real headroom, so this is **provisionally a good idea** — but confirm two things before applying it to the existing base: competitor price position, and whether a flat increase makes sense across clinic sizes.

**Confidence:** medium — the arithmetic is solid on the one number you gave me (churn), but I have zero data on competitor pricing or customer willingness-to-pay, and those are normally the first two things a pricing case checks (playbook steps 3a/3b before 3e).

**Specialists/review:** none needed beyond internal finance sign-off on the contribution-margin assumption; no legal/regulatory angle for a straightforward list-price change to a non-regulated B2B SaaS product.

### Profit effect
| Monthly churn | vs. break-even (2.53%) | Verdict |
|---|---|---|
| 2.0% (current, unchanged) | −0.53pp below | Price increase adds ~€20/clinic/mo profit, nearly pure margin |
| 2.53% | at break-even | Profit effect ≈ 0 |
| >2.53% | above break-even | Price increase destroys value |

### Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Contribution margin ≈ gross margin | 85% | You gave gross margin; assumed variable cost doesn't scale with price (typical SaaS) | Variable cost (e.g., payment fees, per-seat infra) scales with price charged |
| 2 | Customer base is roughly homogeneous in price sensitivity | uniform +€20 | No segmentation data given | Large/multi-vet clinics vs. solo practices react very differently |
| 3 | No existing-contract lock-in prevents a mid-cycle increase | increase applies at will | Not stated | Contracts fix price for a term, delaying realization |

### Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What do competing vet PMS products charge (ezyVet, Provet Cloud, Digitail, IDEXX Neo, etc.)? | If €109 pushes you above market, churn risk is higher than trend extrapolation suggests | You / competitor research (I can run this with web search if you grant it) | Could lower the safe price or argue for value-adds alongside the increase |
| Does churn vary by clinic size or tenure? | Determines whether a uniform increase or tiered/segmented increase is right | Your billing/CRM data | Could change from "raise for everyone" to "raise for new + large accounts first" |
| New customers only, or existing base too? | Existing-base increases usually see a short-term churn spike (even if below break-even on average) that a cohort view would catch better than a steady-state churn average | You | Might recommend grandfathering existing customers and raising for new signups first, as a lower-risk test |

**What would change the answer:** if churn ticks up past ~2.5%/month after rollout, or competitor benchmarking shows you'd be pricing above comparable products without a service/feature edge to justify it, pull back or segment the increase.


## Files in work dir after run


