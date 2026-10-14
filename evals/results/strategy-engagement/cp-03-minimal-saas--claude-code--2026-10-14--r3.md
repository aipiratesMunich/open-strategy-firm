# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | No upfront questions asked; answer proceeds directly with an 'Assumptions' table and only lists 'Open questions' at the end as non-blocking. |
| Computes price change as ~22.5% and break-even loss via 1 - m/(m+p), consistent with margin used | yes | 'Price increase: €89 → €109 = +22.5%' and 'Break-even volume loss ... = 1 − 0.85/(0.85+0.225) = ~21%' |
| Flags that gross margin is not contribution margin and states which value it uses and why | NO | Text merges the two concepts as 'Gross/contribution margin: 85%' without explicitly noting they are distinct metrics or justifying the substitution beyond an assumption footnote about variable cost. |
| Translates break-even into churn terms or explains why modeled separately | yes | 'Break-even churn = current churn / (1 − break-even loss) = 2.0% / 0.79 ≈ 2.53%/month ... room for churn to go up by ~0.5 percentage points' |
| Names structure options as a question to test rather than a single level change | yes | 'New customers only, immediately' ... 'Existing base: grandfather with notice' ... 'Segment it if you can' |
| Gives a provisional answer with confidence low/medium and what would change it | yes | 'Confidence: medium. The arithmetic is solid; what's unverified is how much churn a 22% increase actually triggers for your clinics.' |
| Names revealed-behaviour data that would settle willingness to pay, treats any survey as a range | yes | 'Any precedent — have you raised price before, what happened to churn? ... revealed behavior beats any benchmark I can quote' |
| Must not invent competitor prices or industry benchmarks as facts | NO | 'For sticky vertical SaaS, a well-communicated price increase of this size typically moves churn by a few tenths of a point, not a point or more' presented as a benchmark despite the later hedge 'that's a benchmark judgment, not your data.' |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

**Quick take: yes, likely a good move — the math gives you a wide margin of safety.**

## The math

- Price increase: €89 → €109 = **+22.5%**
- Gross/contribution margin: **85%** (assuming variable cost per customer, ~€13.35/mo, doesn't change with the price change — flagged as assumption below)
- Break-even volume loss for a price increase = 1 − m/(m+p) = 1 − 0.85/(0.85+0.225) = **~21%**

Translated into subscription terms (steady-state customer base scales with 1/churn):

**Break-even churn = current churn / (1 − break-even loss) = 2.0% / 0.79 ≈ 2.53%/month**

So the increase pays for itself in steady state as long as monthly churn doesn't rise above ~2.5% — i.e. you have room for churn to go up by **~0.5 percentage points (a 26% relative jump)** and still come out ahead on contribution profit. Below that, every tenth of a point of churn you *don't* lose is pure upside.

**Confidence: medium.** The arithmetic is solid; what's unverified is how much churn a 22% increase actually triggers for your clinics.

## Why this is likely to clear that bar

Vet practice management software is high-switching-cost: data migration, staff retraining, integrations with labs/payments. For sticky vertical SaaS, a well-communicated price increase of this size typically moves churn by a few tenths of a point, not a point or more — well inside your ~0.5pp cushion. But that's a benchmark judgment, not your data.

## What I'd actually do, not just "raise it"

1. **New customers only, immediately** — zero churn risk, pure margin.
2. **Existing base: grandfather with notice** (e.g. 60–90 days), don't force it through silently — surprise increases are what spike churn, not the increase itself.
3. **Segment it if you can** — clinics that use more features/seats likely have lower price sensitivity than single-vet practices on the base plan; don't apply +22.5% uniformly if your tiers differ.

## Assumptions

| # | Assumption | Value used | Would change the answer if |
|---|---|---|---|
| 1 | Variable cost/customer is fixed in € terms, doesn't scale with price | ~€13.35/mo (from 85% margin on €89) | Support/infra cost scales with price (e.g. usage-based) |
| 2 | 2% churn is current, pre-increase steady state | 2.0%/mo | Churn already trending up for other reasons |
| 3 | No change to CAC or sales funnel from the price change | — | Higher price materially slows new signups (different lever than churn) |

## Open questions (would sharpen this, not block it)

| Question | Why it matters | Effect on answer |
|---|---|---|
| Any precedent — have you raised price before, what happened to churn? | Best evidence you have; revealed behavior beats any benchmark I can quote | Could confirm cushion is comfortable or show it's tighter |
| Is 109 anchored to a competitor gap or value delivered, or just "feels right"? | Cost-plus/round-number increases are harder to defend to customers than value-based ones | Affects messaging and risk of pushback |
| New-business volume: is signup rate elastic to price, separate from churn? | A price rise can quietly shrink top-of-funnel, not just churn | Would need a second break-even check on acquisition, not just retention |

If you've got any data on a past price change (even a small one) or competitor pricing, that'd tighten this from medium to high confidence — happy to run the segment or competitor-benchmark cut if useful.


## Files in work dir after run


