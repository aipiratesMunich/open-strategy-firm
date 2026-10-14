# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States question, outputs, and decision threshold before building | yes | spec.json 'question' field and README.md lead with 'Question answered: ... Decision rule (CFO): approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life'; deck slide 1 poses the question and executive summary states NPV/payback/IRR up front |
| Separates inputs, calculations, outputs; no numbers typed inside formulas other than 0/1 or documented unit conversion | yes | spec.json formulas e.g. 'pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1)', '-fixed_cost * min(1, t)', '(1 + hurdle_rate) ** -t' use only 0/1 literals; inputs.csv, calc.csv, outputs.csv are separate files |
| Base NPV within EUR 3.1m-3.4m and payback in 2030 or year 4 | yes | outputs.csv: npv base = 3.2302410504; payback_period base = 2030 |
| Tornado ranking with saving per parcel first and parcels routed second | yes | sensitivity.csv: rank 1 saving_per_parcel, rank 2 parcels_full_runrate; deck slide 5 table lists same order |
| Break-even values for saving per parcel (~0.42-0.43) and parcels (~3.8-3.9m), both inside range | yes | sensitivity.csv: saving_per_parcel break_even=0.4249869616 (yes); parcels_full_runrate break_even=3.8635178329 (yes) |
| Break-even placed in headline/decided-by line, not only appendix | yes | Executive summary slide 2 body: 'Two drivers decide the answer: saving per parcel (break-even EUR 0.425...) and full run-rate volume (break-even 3.86m parcels...)'; also in chat 'What decides the answer' table |
| Down case as coherent story (competitor hub), not uniform cut, NPV negative | yes | scenario_stories.down: 'a competitor opens its own south hub: fewer parcels route through ours, the price response compresses the saving per parcel, and we accelerate fit-out at higher cost'; outputs.csv npv down = -4.626210314 |
| Checks block and two outputs recomputed by hand with both numbers recorded | yes | README 'Checks' table (3 checks, all OK) and 'Spot test' section: 'NPV by hand: ... Sum = 3.23, matches model' and 'Payback by hand: ... consistent with the model's "2030"' |
| Lists the 60% ramp as a flagged assumption | yes | README 'Flags' section: 'Drivers flagged as assumptions (no source or source starts with "assumption"): ramp_2027'; also chat answer flags it explicitly |
| 'What the deck should say' sentences carrying the model version | yes | README section '## What the deck should say' with 4 numbered sentences each ending '(model v01)' |
| Must not: present NPV without range or scenarios | yes | NPV always accompanied by scenario table (down/base/up) and break-even range table throughout deck and chat answer |
| Must not: add terminal value or tax without flagging departure | yes | Deck footnote: 'EUR m, no tax, no terminal value, per the agreed screening conventions.' — no terminal value/tax added, consistent with stated conventions |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

Everything's built and checked. Here's the business case for the board.

## Answer

**Approve the EUR 6.0m south hub.** Base case NPV is **EUR 3.2m** at the 9% hurdle (IRR 20.9%), and the investment pays back in cash by **2030** (about 3.8 years in), well inside the hub's 8-year life.

## What decides the answer

Not cost, not financing — **saving per parcel** and **parcel volume**:

| Driver | Break-even | Quoted range | Inside range? |
|---|---|---|---|
| Saving per parcel | EUR 0.425/parcel | 0.40 – 0.65 | Yes — barely above the low case |
| Parcels at full run-rate | 3.86m/year | 3.8 – 5.6m | Yes — barely above the low case |
| Hub fixed cost | EUR 1.48m/year | 0.7 – 1.2 | No |
| Investment | EUR 9.23m | 5.5 – 7.5 | No |
| Hurdle rate | 20.9% | 7% – 11% | No |

Fixed cost, the investment itself, and the hurdle rate would each have to blow through their quoted ranges to flip the case alone. Saving per parcel and volume don't have that cushion — their break-evens sit just above the low end of each range.

That matters because the planning team's own risk note — a competitor opening a rival hub — pushes exactly those two drivers down together (plus a costlier, accelerated fit-out). Modeled as one coherent scenario: NPV falls to **-EUR 4.6m**. Without that competitor response, NPV rises to **EUR 8.3m**.

## Deliverables written to the working folder

- `model/` — CSV-driven model (`inputs.csv`, `spec.json`, `calc.csv`, `sensitivity.csv`, `checks.csv`, `model.xlsx` with live formulas, `README.md` with full build/check/spot-test detail)
- `deck.md` / `deck.html` / `deck.pptx` — 7-page board deck (NPV waterfall, payback chart, sensitivity, competitor scenario, decision request) plus a 2-page appendix

All checks pass, two key outputs were hand-verified against the model, and the deck's titles-only read-through tells the full story without the body text.

One flag worth the board's attention: the 60% 2027 ramp assumption has no quoted range (it's based on the 2023 north hub's experience) — it isn't in the sensitivity table because of that, but it's worth tracking against actuals through 2027.


## Files in work dir after run

- deck.html
- deck.md
- deck.pptx
- fm-01-input.md
- model/README.md
- model/calc.csv
- model/checks.csv
- model/inputs.csv
- model/model.xlsx
- model/outputs.csv
- model/sensitivity.csv
- model/spec.json

## File written by the run: deck.html

<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kestrel south hub cross-dock business case</title><style>
:root{--text:#14213D;--accent:#D9822B;--muted:#B8C0CC;--light:#E8EBF0;--bg:#FFFFFF}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#2B2F36;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;color:var(--text)}
#stage{position:absolute;left:0;top:0;width:1280px;height:720px;transform-origin:0 0}
.slide{display:none;position:absolute;inset:0;width:1280px;height:720px;background:var(--bg);padding:44px 64px 30px;flex-direction:column}
.slide.active{display:flex}
.tracker{font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:700;min-height:18px;margin-bottom:10px}
.title{font-size:30px;line-height:1.22;font-weight:700;max-width:1120px}
.title.long{font-size:26px}
.header{font-size:16px;color:#5B6475;margin-top:12px}
.content{flex:1;display:flex;gap:40px;margin-top:22px;min-height:0}
.exhibit{flex:1;min-width:0;display:flex;align-items:center;justify-content:center}
.exhibit.tbl{align-items:flex-start}
.chart{width:100%;height:100%}
.side{width:380px;font-size:19px;line-height:1.45;padding-top:8px}
.side li,.text li{margin:0 0 14px 20px}
.text{flex-direction:column;font-size:22px;line-height:1.45;max-width:1040px}
.lead{font-size:20px;line-height:1.5;color:#3B4458;margin-bottom:18px;max-width:1080px}
.summary{flex-direction:column;gap:0}
.summary ol{font-size:19px;line-height:1.45;margin-left:24px}
.summary li{margin-bottom:10px;padding-left:6px}
.ask{margin-top:auto;border-left:5px solid var(--accent);background:var(--light);padding:14px 18px;font-size:18px;line-height:1.4}
.takeaway{margin-top:14px;padding:10px 16px;border-top:2px solid var(--text);font-size:18px;font-weight:600}
footer{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-top:14px;font-size:13px;color:#5B6475;line-height:1.35}
footer .pn{font-weight:700;color:var(--text)}
.footnote{margin-bottom:2px}
table.data{border-collapse:collapse;font-size:17px;width:100%}
table.data th{text-align:left;border-bottom:2px solid var(--text);padding:8px 12px;font-weight:700}
table.data td{border-bottom:1px solid var(--light);padding:8px 12px;vertical-align:top}
table.data th.num{text-align:right}
table.data td.num{text-align:right;font-variant-numeric:tabular-nums}
table.data tr.hl td{background:var(--light);font-weight:700}
.slide.l-title{justify-content:center;padding-left:96px}
.t-client{font-size:18px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:24px}
.t-title{font-size:48px;line-height:1.15;max-width:980px;font-weight:700}
.t-sub{font-size:22px;margin-top:24px;color:#3B4458;max-width:900px}
.t-meta{font-size:16px;margin-top:40px;color:#5B6475}
.slide.l-title footer,.slide.l-section footer{margin-top:auto}
.slide.l-section{justify-content:center;padding-left:96px}
.s-title{font-size:40px;line-height:1.2;max-width:1000px;margin-top:12px}
.notes{display:none;position:absolute;left:0;right:0;bottom:0;background:#FFF8E8;border-top:2px solid var(--accent);padding:12px 64px;font-size:16px;line-height:1.4}
body.shownotes .slide.active .notes{display:block}
#overview{display:none;position:fixed;inset:0;overflow:auto;background:var(--bg);padding:40px 56px;font-size:18px;line-height:1.5}
body.overview #overview{display:block}
#overview h1{font-size:22px;margin-bottom:16px}
#overview li{margin:0 0 8px 28px;cursor:pointer}
#hint{position:fixed;right:12px;bottom:8px;font-size:12px;color:#C9CED8}
.warn{color:#B00020}
@media print{
  @page{size:1280px 720px;margin:0}
  html,body{background:#fff}
  #stage{position:static;transform:none!important;width:auto;height:auto}
  .slide{display:flex!important;position:relative;page-break-after:always;break-after:page}
  .notes,#hint,#overview{display:none!important}
}
</style></head>
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Should Kestrel invest in the south cross-dock hub?"><div class="t-client">Kestrel Logistics (fictional)</div><h1 class="t-title">Should Kestrel invest in the south cross-dock hub?</h1><p class="t-sub">Business case for the EUR 6.0m investment, board decision pre-read</p><p class="t-meta">Board, investment decision pre-read | October 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Decision requested on page 7. NPV, payback and the deciding drivers are on pages 3 to 6.</aside></section><section class="slide l-summary" id="s2" data-title="Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, payback by 2030 — the case turns negative only if a rival hub cuts volume and savings together"><div class="tracker">Executive summary</div><h2 class="title long">Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, payback by 2030 — the case turns negative only if a rival hub cuts volume and savings together</h2><div class="content summary"><p class="lead">The south region routes parcels without a cross-dock hub. The planning team sized a hub that shortens line-haul and cuts handling per parcel; the CFO&#x27;s rule is to approve if NPV at the 9% hurdle rate is above zero over the hub&#x27;s eight-year life, 2027 to 2034.</p><ol><li>At the base case (5.0m parcels/year full run-rate, EUR 0.55 saved per parcel, 60% ramp in 2027), the hub returns NPV of EUR 3.2m at 9% (IRR 20.9%) against the EUR 6.0m investment.</li><li>The EUR 6.0m is recovered in cash by 2030, about 3.8 years after the investment, well inside the eight-year horizon.</li><li>Two drivers decide the answer: saving per parcel (break-even EUR 0.425, against a EUR 0.40 to 0.65 range) and full run-rate volume (break-even 3.86m parcels, against a 3.8m to 5.6m range). Hub fixed cost, the investment itself and the hurdle rate would each have to move past their quoted range to flip the case alone.</li><li>If a competitor opens its own south hub, those two drivers move together: volume falls, the saving per parcel is squeezed by a price response, and the accelerated fit-out costs more. Together they take NPV to -EUR 4.6m. Without a competitor response, NPV rises to EUR 8.3m.</li></ol><div class="ask">&quot;Decision requested (owner and date proposed; not given in the input): board approves EUR 6.0m capex for the south hub at its next meeting. Before the lease is signed, confirm no competing hub is planned in the south region and secure shipper volume toward the 3.86m-parcel break-even. The answer changes if either signal fails.&quot;</div></div><footer><div class="source">Source: Kestrel planning team inputs (fm-01-input.md); model v01.</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Pages 3 to 6 prove each of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life"><div class="tracker">1 NPV</div><h2 class="title">Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life</h2><div class="header">NPV bridge at 9%, EUR m, 2027 to 2034, base case v01</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life"><rect x="33.4" y="228.0" width="82.8" height="120.0" fill="#B8C0CC"/><line x1="8.0" x2="542.0" y1="228.0" y2="228.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="233.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">CFO rule: approve if NPV &gt; 0</text><text x="74.8" y="220.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6.00</text><text x="74.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Investment</text><text x="74.8" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">(start 2027)</text><rect x="166.9" y="63.8" width="82.8" height="284.2" fill="#B8C0CC"/><text x="208.2" y="55.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+14.21</text><line x1="116.1" x2="166.9" y1="348.0" y2="348.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="208.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">PV of parcel</text><text x="208.2" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">savings,</text><text x="208.2" y="404.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2027-2034</text><rect x="300.4" y="63.8" width="82.8" height="99.6" fill="#B8C0CC"/><text x="341.8" y="55.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.98</text><line x1="249.6" x2="300.4" y1="63.8" y2="63.8" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="341.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">PV of hub fixed</text><text x="341.8" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">cost, 2027-2034</text><rect x="433.9" y="163.4" width="82.8" height="64.6" fill="#D9822B"/><text x="475.2" y="155.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.23</text><line x1="383.1" x2="433.9" y1="163.4" y2="163.4" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="475.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">NPV at 9%</text><line x1="8" x2="542" y1="228.0" y2="228.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>Full run-rate of 5.0m parcels/year at EUR 0.55 saved per parcel from 2028; 2027 carries the 60% ramp</li><li>Hub fixed cost of EUR 0.9m/year, discounted at 9% over the 8-year life</li><li>IRR 20.9%, well above the 9% hurdle</li></ul></div></div><footer><div class="footnote">EUR m, no tax, no terminal value, per the agreed screening conventions.</div><div class="source">Source: Kestrel planning team inputs; model v01 (spec.json, calc.csv).</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> Numbers tie to the executive summary and to model/README.md.</aside></section><section class="slide l-chart" id="s4" data-title="The EUR 6.0m investment is recovered in cash by 2030, three years into operation"><div class="tracker">2 Payback</div><h2 class="title">The EUR 6.0m investment is recovered in cash by 2030, three years into operation</h2><div class="header">Cumulative cash flow (undiscounted), EUR m, 2027 to 2034, base case v01</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The EUR 6.0m investment is recovered in cash by 2030, three years into operation"><text x="46.0" y="365.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6</text><text x="46.0" y="200.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1</text><text x="46.0" y="35.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8</text><line x1="56" x2="510" y1="360.0" y2="360.0" stroke="#B8C0CC"/><text x="56.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Start 2027 (investment)</text><text x="112.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2027</text><text x="169.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2028</text><text x="226.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2029</text><text x="283.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2030</text><text x="339.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2031</text><text x="396.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2032</text><text x="453.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2033</text><text x="510.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2034</text><line x1="56.0" x2="510.0" y1="218.6" y2="218.6" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="518.0" y="223.6" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">cash break-even</text><polyline points="56.0,360.0 112.8,342.3 169.5,298.7 226.2,255.1 283.0,211.5 339.8,167.9 396.5,124.3 453.2,80.7 510.0,37.1" fill="none" stroke="#B8C0CC" stroke-width="2.5"/><circle cx="56.0" cy="360.0" r="4" fill="#B8C0CC"/><circle cx="112.8" cy="342.3" r="4" fill="#B8C0CC"/><circle cx="169.5" cy="298.7" r="4" fill="#B8C0CC"/><circle cx="226.2" cy="255.1" r="4" fill="#B8C0CC"/><circle cx="283.0" cy="211.5" r="4" fill="#B8C0CC"/><circle cx="339.8" cy="167.9" r="4" fill="#B8C0CC"/><circle cx="396.5" cy="124.3" r="4" fill="#B8C0CC"/><circle cx="453.2" cy="80.7" r="4" fill="#B8C0CC"/><circle cx="510.0" cy="37.1" r="4" fill="#B8C0CC"/><text x="510.0" y="25.1" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7.70</text></svg></div><div class="side"><ul><li>Simple (undiscounted) payback falls during 2030, about 3.8 years after the investment</li><li>The hub reaches full run-rate (5.0m parcels) from 2028; the 2027 result reflects the 60% ramp</li></ul></div></div><footer><div class="footnote">Payback is a liquidity check on undiscounted cash; the discounted NPV on page 3 is the CFO&#x27;s approval test.</div><div class="source">Source: Model v01 (calc.csv).</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> In the down case (page 6) cumulative cash never turns positive inside the 8-year horizon.</aside></section><section class="slide l-chart" id="s5" data-title="Saving per parcel swings NPV by EUR 6.5m low to high — more than cost or financing assumptions"><div class="tracker">3 What decides the answer</div><h2 class="title">Saving per parcel swings NPV by EUR 6.5m low to high — more than cost or financing assumptions</h2><div class="header">NPV swing from low to high value, EUR m, one driver at a time, others at base, v01</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Saving per parcel swings NPV by EUR 6.5m low to high — more than cost or financing assumptions"><rect x="280" y="23.4" width="282.6" height="43.0" fill="#B8C0CC"/><text x="570.6" y="50.4" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6.46</text><text x="268.0" y="51.4" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Saving per parcel (EUR/parcel)</text><rect x="280" y="100.2" width="224.0" height="43.0" fill="#B8C0CC"/><text x="512.0" y="127.2" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">5.12</text><text x="268.0" y="128.2" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Parcels at full run-rate (m/year)</text><rect x="280" y="177.0" width="121.2" height="43.0" fill="#B8C0CC"/><text x="409.2" y="204.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.77</text><text x="268.0" y="205.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hub fixed cost (EUR m/year)</text><rect x="280" y="253.8" width="87.5" height="43.0" fill="#B8C0CC"/><text x="375.5" y="280.8" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.00</text><text x="268.0" y="281.8" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Investment (EUR m)</text><rect x="280" y="330.6" width="65.2" height="43.0" fill="#B8C0CC"/><text x="353.2" y="357.6" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.49</text><text x="268.0" y="358.6" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hurdle rate (% per year)</text><line x1="280" x2="280" y1="8" y2="392.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>Saving per parcel: break-even EUR 0.425, inside the quoted EUR 0.40 to 0.65 range — a EUR 0.13 fall from base (24%) turns NPV negative on its own</li><li>Parcel volume: break-even 3.86m parcels/year, inside the quoted 3.8m to 5.6m range — barely above the low case</li><li>Hub fixed cost, the investment and the hurdle rate would each have to move past their quoted high end (to EUR 1.48m/year, EUR 9.23m, or 20.9%) to flip the case alone — none is plausible within its range</li></ul></div></div><footer><div class="footnote">One-way sensitivity, others held at base; break-even values from model v01 (sensitivity.csv).</div><div class="source">Source: Kestrel planning team ranges (fm-01-input.md); model v01.</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> The cheapest check before committing capital: confirm current-year fuel prices behind the saving-per-parcel range, and anchor volume with signed shipper commitments.</aside></section><section class="slide l-chart" id="s6" data-title="A rival hub in the south region would flip the case to NPV -EUR 4.6m; its absence lifts NPV to EUR 8.3m"><div class="tracker">4 Competitor risk</div><h2 class="title long">A rival hub in the south region would flip the case to NPV -EUR 4.6m; its absence lifts NPV to EUR 8.3m</h2><div class="header">NPV at 9% by scenario, EUR m, v01</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A rival hub in the south region would flip the case to NPV -EUR 4.6m; its absence lifts NPV to EUR 8.3m"><line x1="8.0" x2="542.0" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="246.3" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">CFO rule: approve if NPV &gt; 0</text><rect x="41.8" y="241.3" width="106.4" height="98.8" fill="#D9822B"/><text x="95.0" y="358.1" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.63</text><text x="97.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Down: rival hub opens</text><rect x="219.8" y="172.4" width="106.4" height="68.9" fill="#B8C0CC"/><text x="273.0" y="164.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.23</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base</text><rect x="397.8" y="63.6" width="106.4" height="177.7" fill="#B8C0CC"/><text x="451.0" y="55.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8.33</text><text x="453.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Up: no rival hub</text><line x1="8" x2="542" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Down case (one coherent story, not independent moves): volume falls to the low 3.8m parcels, the price response compresses saving per parcel to EUR 0.40, and the accelerated fit-out costs the high EUR 7.5m</li><li>Up case: no competitor response; volume holds at the high 5.6m parcels, saving stays at EUR 0.65 (2023 fuel-price regime), and the fit-out lands on the low EUR 5.5m quote</li><li>In the down case, cumulative cash never turns positive inside the 8-year horizon (page 4)</li></ul></div></div><footer><div class="footnote">Scenarios move the planning team&#x27;s named drivers together for one reason each; hub fixed cost and the hurdle rate are held at base in both.</div><div class="source">Source: Planning team note on competitor response (fm-01-input.md); model v01 scenarios.</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> This is the one risk that moves two of the three deciding drivers at once.</aside></section><section class="slide l-table" id="s7" data-title="Approve EUR 6.0m for the south hub now, with volume and competitor checks before the lease is signed"><div class="tracker">Next steps</div><h2 class="title long">Approve EUR 6.0m for the south hub now, with volume and competitor checks before the lease is signed</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner (proposed)</th><th>By when (proposed)</th></tr><tr><td>Board approves EUR 6.0m capex for the south hub</td><td>Board</td><td>Next board meeting</td></tr><tr><td>Confirm no competing south-region hub is planned</td><td>Network planning lead</td><td>Before lease signature</td></tr><tr><td>Secure anchor shipper volume toward the 3.86m-parcel break-even</td><td>Commercial lead</td><td>Before capex release</td></tr><tr><td>Re-test saving per parcel against current fuel prices</td><td>Finance</td><td>Before capex release</td></tr></table></div><div class="side"><ul><li>Risk: a rival hub turns the case negative (NPV -EUR 4.6m, page 6)</li><li>Risk: saving per parcel or volume alone falling below its break-even (page 5) also turns NPV negative</li><li>Risk: the 60% 2027 ramp is an unproven assumption with no quoted range; track actuals against it through 2027</li></ul></div></div><footer><div class="source">Source: Kestrel planning team inputs (fm-01-input.md); model v01.</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> Owner and date are placeholders pending the board calendar; everything else ties to pages 2 to 6.</aside></section><section class="slide l-table" id="s8" data-title="Model inputs and ranges"><div class="tracker">Appendix</div><h2 class="title">Model inputs and ranges</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th class="num">Base</th><th>Low</th><th>High</th><th>Unit</th><th>Source</th></tr><tr><td>Parcels at full run-rate</td><td class="num">5.0</td><td>3.8</td><td>5.6</td><td>m parcels/year</td><td>2025 network flow data, south region (Kestrel planning team)</td></tr><tr><td>Ramp in 2027</td><td class="num">60%</td><td>n/a</td><td>n/a</td><td>share of full run-rate</td><td>ASSUMPTION: planning team, based on the 2023 north hub opening</td></tr><tr><td>Saving per parcel</td><td class="num">0.55</td><td>0.40</td><td>0.65</td><td>EUR/parcel</td><td>Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices</td></tr><tr><td>Hub fixed cost</td><td class="num">0.9</td><td>0.7</td><td>1.2</td><td>EUR m/year</td><td>Site lease offer plus 14 FTE staffing plan</td></tr><tr><td>Investment</td><td class="num">6.0</td><td>5.5</td><td>7.5</td><td>EUR m</td><td>Two supplier quotes, September 2026</td></tr><tr><td>Hurdle rate</td><td class="num">9%</td><td>7%</td><td>11%</td><td>per year</td><td>Group finance</td></tr></table></div></div><footer><div class="source">Source: fm-01-input.md; model v01 (model/inputs.csv).</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s9" data-title="Full annual cash flow, base case"><div class="tracker">Appendix</div><h2 class="title">Full annual cash flow, base case</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Line item</th><th class="num">2027</th><th class="num">2028</th><th class="num">2029</th><th class="num">2030</th><th class="num">2031</th><th class="num">2032</th><th class="num">2033</th><th class="num">2034</th></tr><tr><td>Parcels routed, m/year</td><td class="num">3.00</td><td class="num">5.00</td><td class="num">5.00</td><td class="num">5.00</td><td class="num">5.00</td><td class="num">5.00</td><td class="num">5.00</td><td class="num">5.00</td></tr><tr><td>Savings, EUR m</td><td class="num">1.65</td><td class="num">2.75</td><td class="num">2.75</td><td class="num">2.75</td><td class="num">2.75</td><td class="num">2.75</td><td class="num">2.75</td><td class="num">2.75</td></tr><tr><td>Hub fixed cost, EUR m</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td><td class="num">-0.90</td></tr><tr><td>Net cash flow, EUR m</td><td class="num">0.75</td><td class="num">1.85</td><td class="num">1.85</td><td class="num">1.85</td><td class="num">1.85</td><td class="num">1.85</td><td class="num">1.85</td><td class="num">1.85</td></tr><tr><td>Discounted cash flow, EUR m</td><td class="num">0.69</td><td class="num">1.56</td><td class="num">1.43</td><td class="num">1.31</td><td class="num">1.20</td><td class="num">1.10</td><td class="num">1.01</td><td class="num">0.93</td></tr></table></div></div><footer><div class="source">Source: Model v01 (model/calc.csv). Investment of EUR 6.0m at start of 2027 (t=0) is not a row in this table; see page 3.</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Should Kestrel invest in the south cross-dock hub? <span style='color:#8A93A3'>(1)</span></li><li>Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, payback by 2030 — the case turns negative only if a rival hub cuts volume and savings together <span style='color:#8A93A3'>(2)</span></li><li>Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life <span style='color:#8A93A3'>(3)</span></li><li>The EUR 6.0m investment is recovered in cash by 2030, three years into operation <span style='color:#8A93A3'>(4)</span></li><li>Saving per parcel swings NPV by EUR 6.5m low to high — more than cost or financing assumptions <span style='color:#8A93A3'>(5)</span></li><li>A rival hub in the south region would flip the case to NPV -EUR 4.6m; its absence lifts NPV to EUR 8.3m <span style='color:#8A93A3'>(6)</span></li><li>Approve EUR 6.0m for the south hub now, with volume and competitor checks before the lease is signed <span style='color:#8A93A3'>(7)</span></li><li>Model inputs and ranges <span style='color:#8A93A3'>(A1)</span></li><li>Full annual cash flow, base case <span style='color:#8A93A3'>(A2)</span></li></ol></div>
<div id="hint">arrows: navigate | t: titles | n: notes | print: PDF</div>
<script>
(function(){
var slides=[].slice.call(document.querySelectorAll('.slide')),i=0,stage=document.getElementById('stage');
function fit(){var s=Math.min(innerWidth/1280,innerHeight/720);stage.style.transform='translate

## File written by the run: deck.md

---
title: Kestrel south hub cross-dock business case
client: Kestrel Logistics (fictional)
audience: Board, investment decision pre-read
date: October 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
---

# Deck: Should Kestrel invest in the south cross-dock hub?

*Fictional company. All figures, people and documents invented for evaluation (fm-01-input.md). Model version v01.*

**Opening (SCQA)**
- Situation: Kestrel's south region routes parcels without a cross-dock hub; the planning team has sized a hub that would cut line-haul and handling cost per parcel.
- Complication: the EUR 6.0m investment and its savings depend on volume, fuel-linked savings and ramp assumptions that are only partly ranged, and a competitor could open a rival hub.
- Question: should Kestrel invest, and what decides whether the case holds?
- Answer: approve; base case NPV is EUR 3.2m at the 9% hurdle (IRR 20.9%), payback inside four years, but the case is decided by parcel volume and saving per parcel, and a rival hub flips it negative.

**Key line**
1. Discounted at 9%, the hub returns NPV of EUR 3.2m over its eight-year life.
2. The EUR 6.0m investment is recovered in cash by 2030, three years into operation.
3. Saving per parcel and parcel volume decide the answer; cost and financing assumptions do not.
4. A rival hub in the south region would flip the case negative; its absence lifts NPV to EUR 8.3m.

## 1. Should Kestrel invest in the south cross-dock hub?
layout: title
subtitle: Business case for the EUR 6.0m investment, board decision pre-read
note: Decision requested on page 7. NPV, payback and the deciding drivers are on pages 3 to 6.

## 2. Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, payback by 2030 — the case turns negative only if a rival hub cuts volume and savings together
layout: summary
tracker: Executive summary
lead: The south region routes parcels without a cross-dock hub. The planning team sized a hub that shortens line-haul and cuts handling per parcel; the CFO's rule is to approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life, 2027 to 2034.
body:
- At the base case (5.0m parcels/year full run-rate, EUR 0.55 saved per parcel, 60% ramp in 2027), the hub returns NPV of EUR 3.2m at 9% (IRR 20.9%) against the EUR 6.0m investment.
- The EUR 6.0m is recovered in cash by 2030, about 3.8 years after the investment, well inside the eight-year horizon.
- Two drivers decide the answer: saving per parcel (break-even EUR 0.425, against a EUR 0.40 to 0.65 range) and full run-rate volume (break-even 3.86m parcels, against a 3.8m to 5.6m range). Hub fixed cost, the investment itself and the hurdle rate would each have to move past their quoted range to flip the case alone.
- If a competitor opens its own south hub, those two drivers move together: volume falls, the saving per parcel is squeezed by a price response, and the accelerated fit-out costs more. Together they take NPV to -EUR 4.6m. Without a competitor response, NPV rises to EUR 8.3m.
ask: "Decision requested (owner and date proposed; not given in the input): board approves EUR 6.0m capex for the south hub at its next meeting. Before the lease is signed, confirm no competing hub is planned in the south region and secure shipper volume toward the 3.86m-parcel break-even. The answer changes if either signal fails."
source: Kestrel planning team inputs (fm-01-input.md); model v01.
note: Read the bold line and the ask. Pages 3 to 6 prove each of the four points.

## 3. Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life
layout: chart
tracker: 1 NPV
message: flow
chart: waterfall
header: NPV bridge at 9%, EUR m, 2027 to 2034, base case v01
reference: 0 | CFO rule: approve if NPV > 0
highlight: NPV at 9%
| Step | EUR m | Type |
|---|---|---|
| Investment (start 2027) | -6.00 | delta |
| PV of parcel savings, 2027-2034 | 14.21 | delta |
| PV of hub fixed cost, 2027-2034 | -4.98 | delta |
| NPV at 9% | 3.23 | total |
body:
- Full run-rate of 5.0m parcels/year at EUR 0.55 saved per parcel from 2028; 2027 carries the 60% ramp
- Hub fixed cost of EUR 0.9m/year, discounted at 9% over the 8-year life
- IRR 20.9%, well above the 9% hurdle
footnote: EUR m, no tax, no terminal value, per the agreed screening conventions.
source: Kestrel planning team inputs; model v01 (spec.json, calc.csv).
note: Numbers tie to the executive summary and to model/README.md.

## 4. The EUR 6.0m investment is recovered in cash by 2030, three years into operation
layout: chart
tracker: 2 Payback
message: time-series
chart: line
header: Cumulative cash flow (undiscounted), EUR m, 2027 to 2034, base case v01
reference: 0 | cash break-even
highlight: End 2030
| Year | Cumulative cash flow |
|---|---|
| Start 2027 (investment) | -6.00 |
| End 2027 | -5.25 |
| End 2028 | -3.40 |
| End 2029 | -1.55 |
| End 2030 | 0.30 |
| End 2031 | 2.15 |
| End 2032 | 4.00 |
| End 2033 | 5.85 |
| End 2034 | 7.70 |
body:
- Simple (undiscounted) payback falls during 2030, about 3.8 years after the investment
- The hub reaches full run-rate (5.0m parcels) from 2028; the 2027 result reflects the 60% ramp
footnote: Payback is a liquidity check on undiscounted cash; the discounted NPV on page 3 is the CFO's approval test.
source: Model v01 (calc.csv).
note: In the down case (page 6) cumulative cash never turns positive inside the 8-year horizon.

## 5. Saving per parcel swings NPV by EUR 6.5m low to high — more than cost or financing assumptions
layout: chart
tracker: 3 What decides the answer
message: ranking
chart: hbar
header: NPV swing from low to high value, EUR m, one driver at a time, others at base, v01
highlight: Saving per parcel (EUR/parcel)
| Driver | NPV swing |
|---|---|
| Saving per parcel (EUR/parcel) | 6.46 |
| Parcels at full run-rate (m/year) | 5.12 |
| Hub fixed cost (EUR m/year) | 2.77 |
| Investment (EUR m) | 2.00 |
| Hurdle rate (% per year) | 1.49 |
body:
- Saving per parcel: break-even EUR 0.425, inside the quoted EUR 0.40 to 0.65 range — a EUR 0.13 fall from base (24%) turns NPV negative on its own
- Parcel volume: break-even 3.86m parcels/year, inside the quoted 3.8m to 5.6m range — barely above the low case
- Hub fixed cost, the investment and the hurdle rate would each have to move past their quoted high end (to EUR 1.48m/year, EUR 9.23m, or 20.9%) to flip the case alone — none is plausible within its range
footnote: One-way sensitivity, others held at base; break-even values from model v01 (sensitivity.csv).
source: Kestrel planning team ranges (fm-01-input.md); model v01.
note: The cheapest check before committing capital: confirm current-year fuel prices behind the saving-per-parcel range, and anchor volume with signed shipper commitments.

## 6. A rival hub in the south region would flip the case to NPV -EUR 4.6m; its absence lifts NPV to EUR 8.3m
layout: chart
tracker: 4 Competitor risk
message: deviation
chart: bar
header: NPV at 9% by scenario, EUR m, v01
reference: 0 | CFO rule: approve if NPV > 0
highlight: Down: rival hub opens
| Scenario | NPV |
|---|---|
| Down: rival hub opens | -4.63 |
| Base | 3.23 |
| Up: no rival hub | 8.33 |
body:
- Down case (one coherent story, not independent moves): volume falls to the low 3.8m parcels, the price response compresses saving per parcel to EUR 0.40, and the accelerated fit-out costs the high EUR 7.5m
- Up case: no competitor response; volume holds at the high 5.6m parcels, saving stays at EUR 0.65 (2023 fuel-price regime), and the fit-out lands on the low EUR 5.5m quote
- In the down case, cumulative cash never turns positive inside the 8-year horizon (page 4)
footnote: Scenarios move the planning team's named drivers together for one reason each; hub fixed cost and the hurdle rate are held at base in both.
source: Planning team note on competitor response (fm-01-input.md); model v01 scenarios.
note: This is the one risk that moves two of the three deciding drivers at once.

## 7. Approve EUR 6.0m for the south hub now, with volume and competitor checks before the lease is signed
layout: table
tracker: Next steps
| Step | Owner (proposed) | By when (proposed) |
|---|---|---|
| Board approves EUR 6.0m capex for the south hub | Board | Next board meeting |
| Confirm no competing south-region hub is planned | Network planning lead | Before lease signature |
| Secure anchor shipper volume toward the 3.86m-parcel break-even | Commercial lead | Before capex release |
| Re-test saving per parcel against current fuel prices | Finance | Before capex release |
body:
- Risk: a rival hub turns the case negative (NPV -EUR 4.6m, page 6)
- Risk: saving per parcel or volume alone falling below its break-even (page 5) also turns NPV negative
- Risk: the 60% 2027 ramp is an unproven assumption with no quoted range; track actuals against it through 2027
ask: "Decision requested: approve EUR 6.0m for the south hub. Owner and date are proposed, since the input named neither. The answer changes if a rival hub is confirmed, or if committed volume or the saving per parcel falls to its break-even level."
source: Kestrel planning team inputs (fm-01-input.md); model v01.
note: Owner and date are placeholders pending the board calendar; everything else ties to pages 2 to 6.

## A1. Model inputs and ranges
layout: table
tracker: Appendix
| Driver | Base | Low | High | Unit | Source |
|---|---|---|---|---|---|
| Parcels at full run-rate | 5.0 | 3.8 | 5.6 | m parcels/year | 2025 network flow data, south region (Kestrel planning team) |
| Ramp in 2027 | 60% | n/a | n/a | share of full run-rate | ASSUMPTION: planning team, based on the 2023 north hub opening |
| Saving per parcel | 0.55 | 0.40 | 0.65 | EUR/parcel | Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices |
| Hub fixed cost | 0.9 | 0.7 | 1.2 | EUR m/year | Site lease offer plus 14 FTE staffing plan |
| Investment | 6.0 | 5.5 | 7.5 | EUR m | Two supplier quotes, September 2026 |
| Hurdle rate | 9% | 7% | 11% | per year | Group finance |
source: fm-01-input.md; model v01 (model/inputs.csv).

## A2. Full annual cash flow, base case
layout: table
tracker: Appendix
| Line item | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 |
|---|---|---|---|---|---|---|---|---|
| Parcels routed, m/year | 3.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 |
| Savings, EUR m | 1.65 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 | 2.75 |
| Hub fixed cost, EUR m | -0.90 | -0.90 | -0.90 | -0.90 | -0.90 | -0.90 | -0.90 | -0.90 |
| Net cash flow, EUR m | 0.75 | 1.85 | 1.85 | 1.85 | 1.85 | 1.85 | 1.85 | 1.85 |
| Discounted cash flow, EUR m | 0.69 | 1.56 | 1.43 | 1.31 | 1.20 | 1.10 | 1.01 | 0.93 |
source: Model v01 (model/calc.csv). Investment of EUR 6.0m at start of 2027 (t=0) is not a row in this table; see page 3.

# Titles-only read-through

Passes: the seven main titles alone tell the board the NPV, the payback, what decides the answer, the competitor risk and the decision requested.


## File written by the run: model/README.md

# Model: Kestrel south hub cross-dock business case (fictional), v01

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? Decision rule (CFO): approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life, 2027 to 2034.

**Master check:** OK

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -4.626 | 8.33 |
| IRR | per year | 0.2091 | -0.09939 | 0.388 |
| Payback (first period cumulative cash >= 0) | year | 2030 | none | 2029 |
| Parcels routed at full run-rate (2028) | m parcels | 5 | 3.8 | 5.6 |
| Net cash flow at full run-rate (2028) | EUR m | 1.85 | 0.62 | 2.74 |

Scenarios (coherent sets, drivers changed from base):
- **down**: parcels_full_runrate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (a competitor opens its own south hub: fewer parcels route through ours, the price response compresses the saving per parcel, and we accelerate fit-out at higher cost)
- **up**: parcels_full_runrate = 5.6, saving_per_parcel = 0.65, investment = 5.5 (no competitor entry: full network volume and 2023-level fuel prices hold the saving per parcel up, and the fit-out lands on the lower supplier quote)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | parcels_full_runrate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | fixed_cost | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | hurdle_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |

Drivers without low/high range (not tested): ramp_2027

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| parcels_full_runrate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate |  |  | ASSUMPTION: planning team based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = 2025 fuel prices high = 2023 fuel prices |
| fixed_cost | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes September 2026 |
| hurdle_rate | 0.09 | per year | 0.07 | 0.11 | Group finance |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1)` |
| parcels_routed | m parcels per year | `parcels_full_runrate * ramp` |
| savings | EUR m | `parcels_routed * saving_per_parcel` |
| fixed_cost_flow | EUR m | `-fixed_cost * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0)` |
| net_cash_flow | EUR m | `savings + fixed_cost_flow + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + hurdle_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |
| parcels_routed_within_runrate | base | >=0 | 0 | OK |
| parcels_routed_within_runrate | down | >=0 | 0 | OK |
| parcels_routed_within_runrate | up | >=0 | 0 | OK |
| ramp_not_above_one | base | >=0 | 0 | OK |
| ramp_not_above_one | down | >=0 | 0 | OK |
| ramp_not_above_one | up | >=0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027
- No range for: ramp_2027

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)

## Spot test

- NPV by hand: PV of savings (EUR 1.65m in 2027, EUR 2.75m/year 2028-2034) = 14.21; PV of fixed cost (EUR 0.9m/year, 2027-2034) = -4.98; investment at t=0 = -6.00. Sum = 3.23, matches model.
- Payback by hand: cumulative undiscounted cash is -1.55 at end 2029 and +0.30 at end 2030 (net cash flow EUR 1.85m/year from 2028); crosses zero about 0.84 of the way through 2030, consistent with the model's "2030".

## What the deck should say

1. Discounted at the 9% hurdle rate, the hub returns NPV of EUR 3.2m over its eight-year life (model v01).
2. The EUR 6.0m investment is recovered in cash by 2030, about 3.8 years after the investment (model v01).
3. Saving per parcel (break-even EUR 0.425/parcel) and parcel volume (break-even 3.86m parcels/year) decide the answer; both break-evens sit inside their quoted ranges, while fixed cost, investment and the hurdle rate would each have to move outside their ranges to flip the case alone (model v01).
4. A rival south hub moves both deciding drivers together and turns NPV negative (-EUR 4.6m); its absence lifts NPV to EUR 8.3m (model v01).


## File written by the run: model/calc.csv

line_item,unit,start,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
parcels_routed,m parcels per year,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
savings,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost_flow,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK
parcels_routed_within_runrate,base,>=0,0.0,OK
parcels_routed_within_runrate,down,>=0,0.0,OK
parcels_routed_within_runrate,up,>=0,0.0,OK
ramp_not_above_one,base,>=0,0.0,OK
ramp_not_above_one,down,>=0,0.0,OK
ramp_not_above_one,up,>=0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
parcels_full_runrate,5.0,m parcels per year,2025 network flow data south region (Kestrel planning team),3.8,5.6,full run-rate volume once ramp complete
ramp_2027,0.60,share of full run-rate,ASSUMPTION: planning team based on the 2023 north hub opening,,,full run-rate assumed reached from 2028
saving_per_parcel,0.55,EUR per parcel,Network simulation v4; low = 2025 fuel prices high = 2023 fuel prices,0.40,0.65,
fixed_cost,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,
investment,6.0,EUR m,Two supplier quotes September 2026,5.5,7.5,paid at start of 2027 (t=0)
hurdle_rate,0.09,per year,Group finance,0.07,0.11,


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,8.3296245579,v01
irr,per year,0.2091368125,-0.0993929701,0.3880178751,v01
payback_period,year,2030,,2029,v01
parcels_routed_2028,m parcels,5.0,3.8,5.6,v01
net_cash_flow_2028,EUR m,1.85,0.62,2.74,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,parcels_full_runrate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,fixed_cost,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,hurdle_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub cross-dock business case (fictional)",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? Decision rule (CFO): approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life, 2027 to 2034.",
  "periods": ["start", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1)"},
    {"name": "parcels_routed", "unit": "m parcels per year", "expr": "parcels_full_runrate * ramp"},
    {"name": "savings", "unit": "EUR m", "expr": "parcels_routed * saving_per_parcel"},
    {"name": "fixed_cost_flow", "unit": "EUR m", "expr": "-fixed_cost * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "savings + fixed_cost_flow + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + hurdle_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first period cumulative cash >= 0)", "unit": "year", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "parcels_routed_2028", "label": "Parcels routed at full run-rate (2028)", "unit": "m parcels", "fn": "value", "row": "parcels_routed", "period": "2028"},
    {"name": "net_cash_flow_2028", "label": "Net cash flow at full run-rate (2028)", "unit": "EUR m", "fn": "value", "row": "net_cash_flow", "period": "2028"}
  ],
  "checks": [
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - savings - fixed_cost_flow - capex", "rule": "==0"},
    {"name": "parcels_routed_within_runrate", "expr": "parcels_full_runrate - parcels_routed", "rule": ">=0"},
    {"name": "ramp_not_above_one", "expr": "1 - ramp", "rule": ">=0"}
  ],
  "scenarios": {
    "down": {"parcels_full_runrate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"parcels_full_runrate": 5.6, "saving_per_parcel": 0.65, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "a competitor opens its own south hub: fewer parcels route through ours, the price response compresses the saving per parcel, and we accelerate fit-out at higher cost",
    "up": "no competitor entry: full network volume and 2023-level fuel prices hold the saving per parcel up, and the fit-out lands on the lower supplier quote"
  },
  "break_even": {"output": "npv", "target": 0}
}

