# Operating Model

## Typical questions

Operating-model requests usually arrive as a structure request ("draw us a new org chart"). The structure is the last thing to decide. First establish what the strategy needs the organisation to do differently.

- "We need a new organisation." → "Which capabilities and decisions does <strategy> require that today's set-up cannot deliver, and what is the smallest change that fixes that?"
- "Should we centralise <function>?" → "Which activities in <function> gain from scale or consistency, which need local speed or customer proximity, and who should decide what?"
- "We are too slow / too bureaucratic." → "Which decisions take too long, who is involved, and where do layers or unclear rights cause the delay?"
- "Should we outsource <activity>?" → "Is <activity> a source of advantage or a commodity, and can a partner do it better or cheaper at acceptable risk?"

An operating-model question is sharp when it names the strategy it serves, the capabilities in question and the measurable symptom (speed, cost, quality, missed targets).

## Issue tree skeleton

A MECE starting tree. Adapt, never use unchanged. Work from strategy to structure, never the reverse.

- **What must the organisation be able to do?**
  - Strategy-critical capabilities and the performance level each needs. *H: the strategy needs a guaranteed 48-hour service response that no unit owns today.*
  - Gap today: where performance falls short, and why
- **Are processes and systems the cause?**
  - Core processes end to end: hand-offs, delays, rework
  - Data and systems that support them. *H: delays come from dispatch and spare-part availability, not from reporting lines.*
- **Are decision rights clear?**
  - Who decides, who is consulted, who executes, for the ten to fifteen decisions that matter most
  - Escalation paths and committees
- **Is the structure fit for purpose?**
  - Primary axis: function, region, product, customer segment
  - Spans of control and number of layers
  - Centre versus business units: what is shared, what is local
- **What should we do ourselves?** (sourcing)
  - Activities that create advantage stay in-house; commodity activities can be bought or partnered
- **Do people, skills and culture support it?**
  - Roles, skills, incentives, leadership behaviours

The [Seven-S Framework](seven-s.md) model is a useful completeness check: strategy, structure and systems are easy to change on paper; shared values, style, staff and skills decide whether the change holds.

## Key analyses

- **Strategy-to-capability map.** For each strategic priority, the capabilities it needs and their current maturity ([Seven-S Framework](seven-s.md), [Value Chain](value-chain.md)).
- **Process diagnostics.** End-to-end walk of the critical processes with lead times and failure points; fix the process before redrawing boxes.
- **Decision-rights review.** Map key decisions to roles; find decisions with no owner or too many vetoes.
- **Spans and layers.** Count managers, direct reports and layers from the top to the front line; compare with what the work needs and with peers ([Cost Benchmarking](cost-benchmarking.md)).
- **Sourcing assessment.** Per activity: strategic importance, internal performance against market options, switching risk ([Value Chain](value-chain.md)).
- **Option comparison.** Two or three design options scored against design criteria agreed upfront; cost and transition plan per option ([Business Case](business-case.md)).

## Traps

- **Reorganising before fixing processes.** New boxes on old processes give the same results with new names. Fix the broken process and data first, then decide what structure it needs.
- **Starting from the org chart.** Designing structure without a statement of what the strategy requires leads to designs that reflect politics and personalities.
- **One-size spans.** A single target span for all managers ignores that a field-service lead and a research lead do different work.
- **Decision rights left implicit.** A new structure without a decision map recreates the old escalation habits.
- **Centralising by default.** Shared services save money only where activities are standardised; otherwise they add hand-offs.
- **Outsourcing advantage.** Handing a partner the activity customers choose you for. Sourcing decisions follow the value chain, not the cost line alone.
- **Ignoring transition cost and disruption.** Reorganisations absorb management attention for months. Count that against the benefit and sequence the changes.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps decided to launch service contracts with a 48-hour response guarantee on its installed base (base case EUR 12.5m revenue by 2030, EUR 6m investment). Its 85 service technicians sit in six regions and report to the regional sales heads; dispatch is done region by region; contract pricing decisions are not assigned. Management proposed a new central service division. Sharpened question: "What set-up lets Alder meet a 48-hour response on contracted pumps from 2027, at the lowest change cost?"

Process diagnosis: response within 48 hours is met in about 60% of calls. Most misses trace to two causes: spare parts not in the regional van stock, and technicians tied up in one region while another is overloaded. Neither is fixed by a new division alone. Recommendation in sequence: (1) central dispatch across regions and a stocked-parts list for the 200 most-failed parts, from early 2027; (2) a service head with P&L for contracts and clear rights over contract pricing within a price corridor set by the board; (3) partner technicians for the two remote regions where demand is too thin for own staff; (4) revisit a full service division once contract volume justifies it.

## Output template

```markdown
# Operating model: <client>, <decision question in one line>

**Answer:** <what changes, in what sequence, by when, to reach <the strategy requirement and its target>; a proposed structure is judged only against that>

## What the strategy requires
| Strategic priority | Capability needed | Performance needed | Today | Gap |
|---|---|---|---|---|

## Root causes of the gap
| Gap | Process / system cause | Decision-rights cause | Structure cause | People / skills cause |
|---|---|---|---|---|

## Decision rights (key decisions)
| Decision | Decides | Consulted | Executes | Today |
|---|---|---|---|---|

## Structure options
| Option | Description | Meets capability needs | Cost | Transition risk | Score |
|---|---|---|---|---|---|

## Spans, layers, sourcing
- Spans and layers: <current vs proposed>
- Sourcing: <activity> keep / partner / outsource, reason

## Transition plan
| Step | What changes | Owner | Date | Success measure |
|---|---|---|---|---|

## What would change the answer
1. If <fact>, then <consequence>.
```

## Playbook

How to run this case step by step. Steps 1 to 4 are specific to this case type; the shared engagement procedure covers the rest.

### Step 1: Sharpen the question

Requests usually arrive as "draw us a new org chart". First establish what the strategy needs the organisation to do differently. Ask, in small groups:
- Which strategy or priority must the organisation deliver, and what performance level (response time, cost, quality, growth)?
- What is the measurable symptom: which decisions are slow, which targets are missed, by how much?
- Which structure is already proposed, by whom, and why?
- Which ten to fifteen decisions matter most, and who takes them today?
- For outsourcing: do customers choose you for this activity?
- What must not change (sites, works council agreements, key people, timing constraints)?

Write the decision question in this form: "Which capabilities and decisions does <strategy> require that today's set-up cannot deliver, and what is the smallest change that fixes that by <date>?" It is sharp when it names the strategy, the capabilities in question and the measurable symptom. Keep a proposed structure as one option, not as the frame.

### Step 2: Instantiate the issue tree

Work from strategy to structure. Adapt the skeleton in the case note; set each threshold with the client.

| Branch | Hypothesis (example form) | Kill criterion |
|---|---|---|
| Capability | The strategy needs <capability at level x> that no unit owns today | Capability already owned and performing at the needed level |
| Process and systems | Most misses trace to process hand-offs, data or systems, not reporting lines | Process runs to standard; misses start where reporting lines split the work |
| Decision rights | Key decisions have no clear owner or too many vetoes | Decision map shows clear owners and fast decisions |
| Structure | The primary axis or the centre-unit split blocks the capability | Gaps close with process and decision fixes alone |
| Spans and layers | Layers or spans slow decisions or add cost against what the work needs | Spans and layers fit the work type; no delay traced to them |
| Sourcing | <activity> is a commodity a partner can do better or cheaper at acceptable risk | Customers choose us for it, or switching risk is too high |
| People and culture | Incentives and skills support the change | Incentives reward the old behaviour and cannot change in time |

### Step 3: Run the deciding analyses, in order

Each analysis ends by marking its hypothesis confirmed, killed or reshaped. If your agent can run sub-tasks in parallel, run 3b to 3d in parallel; otherwise in order.

a. **Strategy-to-capability map.** Per strategic priority, the capability, the performance needed and the gap today ([Seven-S Framework](seven-s.md), [Value Chain](value-chain.md)).
b. **Process diagnostics.** End-to-end walk of the critical processes with lead times and failure points, from data and interviews with the people who run them ([Interview Guide](interview-guide.md)). Fix the process before redrawing boxes.
c. **Decision-rights review.** Map key decisions to who decides, who is consulted, who executes; find decisions with no owner or too many vetoes.
d. **Spans and layers.** Managers, direct reports and layers from top to front line, against what the work needs and, where comparable data exists, peers ([Cost Benchmarking](cost-benchmarking.md)).
e. **Sourcing assessment.** Per activity: strategic importance, internal performance against market options, switching risk ([Value Chain](value-chain.md)).
f. **Option comparison.** Two or three design options scored against design criteria agreed with the client before scoring; if they were not agreed (quick case), list them above the table marked "proposed, to agree with <decider> before final scoring". Per option: running cost, one-off transition cost (EUR, or a range marked as assumption), management attention (who, for how many months), transition risk and plan ([Business Case](business-case.md)).
g. **Alignment check.** Run the recommended option through [Seven-S Framework](seven-s.md): which soft elements (incentives, style, skills) must change for it to hold?

### Step 4: Run the trap checks

Answer each with yes or no and fix every no before writing:
- [ ] Broken processes and data are fixed or scheduled before any structure change.
- [ ] The design starts from a written statement of what the strategy requires, not from the org chart.
- [ ] Spans differ by type of work; no single target span for everyone.
- [ ] Decision rights for the key decisions are explicit in the recommendation.
- [ ] Centralisation is proposed only where activities are standardised.
- [ ] No activity customers choose the client for is outsourced.
- [ ] Transition cost and management attention are counted against the benefit, and changes are sequenced.
- [ ] Claims about culture or behaviour rest on examples, not opinions ([Weak Evidence](weak-evidence.md)).

### Step 5: Answer page

Use the output template in [Operating Model](operating-model.md) for the body, wrapped in the shared format below. Lead with what changes, in what sequence, by when; the structure option comes after the root causes that justify it.

### Case rules

- The smallest change that closes the gap wins over the most complete redesign.

### Answer page format

```markdown
# Operating model: <client>, <decision question in one line>

**Answer:** <what changes, in what sequence, by when>
**Confidence:** high / medium / low, because <one reason>

<body sections from the case note output template>

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
```

### Limits

Labour law, works council consultation, individual staffing decisions and job grading need HR and legal specialists; flag them. The skill designs roles and rights, not who fills them.

## Related

- [Growth Strategy](growth-strategy.md), [Profitability Turnaround](profitability-turnaround.md), [Seven-S Framework](seven-s.md), [Value Chain](value-chain.md), [Cost Benchmarking](cost-benchmarking.md), [Problem Definition](problem-definition.md), [Synthesis](synthesis.md)
