# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | footnote on page 6: 'The total on page 8 uses the EUR 1.2m before-churn figure... using the EUR 1.1m net figure instead would narrow the 2028 total to about EUR 64.6m'; also flagged explicitly in the chat reply to the user |
| Writes 06-deck.md in spec format with frontmatter, SCQA opening in four sentences, key line above first slide | yes | frontmatter block present; 'Opening (SCQA)' has exactly Situation/Complication/Question/Answer sentences; '**Key line**' section appears before '## 1. Which growth moves...' |
| Page 2 is executive summary with governing thought title, numbered key-line points, 1.3m gap, what changes the answer, decision request with 1.9m/COO/start date | yes | page 2 title is the governing thought; ordered list covers all four key-line points plus the 64.7/1.3m gap; ask box: 'approve EUR 1.9m...Owner: COO Lena Marsh, start January 2027... answer changes if off-peak take-up falls below 6,000 members' |
| Every main-page title is a full-sentence finding with a number/comparison, not a topic label | yes | titles like 'Daytime capacity is the largest unused asset: utilisation falls to 31%...' and 'A new gym in a new city needs EUR 4.5m and pays back in about seven years...'; no title is a bare label like 'Overview' |
| 8-15 main pages, sections follow key line (not phases), new-city analysis included as a finding | yes | 9 main pages (title, summary, 3,4 off-peak, 5 corporate, 6 premium, 7 new city, 8 bridge, 9 decision); page 7 title: 'A new gym in a new city needs EUR 4.5m and pays back in about seven years...' |
| Utilisation bar chart with 10am-4pm highlighted; waterfall bridge 58.0->64.7 with 66.0 reference and 1.3 gap visible | yes | page 3 spec: 'chart: bar ... highlight: 10am-4pm'; page 8 spec: 'chart: waterfall ... reference: 66.0 / 2028 target EUR 66.0m' with steps 58.0+3.1+2.4+1.2=64.7 |
| Every chart has header (measure/unit/period) and a source line from the synthesis | yes | e.g. header: 'Average gym utilisation by time band, % of capacity, 34 gyms, January to August 2026' / source: 'Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4' |
| Numbers tie across executive summary, section pages and bridge with no rounding drift | yes | 3.1+2.4+1.2=6.7 and 58.0+6.7=64.7 consistent across exec summary, pages 3-6, and page 8 bridge |
| Titles-only read-through is listed and tells the story in order | yes | '# Titles-only read-through / Passes: the nine main titles alone tell the board what to fund, what each move is worth, why a new city is excluded, and what to decide.' |
| Runs render_deck.py and reports warnings if Python available, else says spec delivered unrendered | yes | 'Titles-only read-through passes and the renderer returned no warnings.' alongside rendered 06-deck.html and 06-deck.pptx outputs |
| No new analysis, new numbers, competitor facts or sources beyond the synthesis | yes | all figures (3.1m, 2.4m, 1.2m, 4.5m, competitor prices 64/67) are reused consistently across exec summary, appendix and slides with no additional claims introduced |
| No agenda/method/background pages before the executive summary | yes | page 1 is the title page, page 2 is immediately the executive summary, no intervening agenda/method page |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

The board pre-read deck is built from the Fernhill synthesis — the argument was already finished (one governing thought, four sourced key-line statements, a total that ties, a dated decision request), so this went straight to deck build with no readiness gaps to flag.

**Files:** `06-deck.md` (spec), `06-deck.html` (open in a browser — arrow keys to navigate, `t` for titles-only view, print to PDF), `06-deck.pptx` (native PowerPoint with editable charts).

**Structure** — 9 main pages + 2 appendix:
1. Title
2. Executive summary (governing thought, decision request: approve EUR 1.9m, owner COO Lena Marsh, start Jan 2027)
3–4. Off-peak membership (utilisation gap chart, then revenue range EUR 2.0–3.8m)
5. Corporate wellness (pilot 6 contracts → 2028 target of 40, +EUR 2.4m)
6. Premium price (+EUR 4 vs. two competitors, +EUR 1.2m before churn)
7. Why not a new city (7-year payback vs. the board's 4-year limit)
8. Waterfall: EUR 58.0m → EUR 64.7m, EUR 1.3m short of the EUR 66.0m target
9. Decision request and next steps
A1–A2. Assumptions and utilisation detail

One thing worth flagging to you: the synthesis itself gives two figures for the premium price move — EUR 1.2m before churn and EUR 1.1m net of churn — and uses the 1.2m figure in its own total. I kept that convention for the headline total (consistent with the source) but called out the discrepancy explicitly on the premium slide and the waterfall slide, rather than silently picking one. Titles-only read-through passes and the renderer returned no warnings.


## Files in work dir after run

- 06-deck.html
- 06-deck.md
- 06-deck.pptx
- db-01-synthesis.md

## File written by the run: 06-deck.html

<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fernhill Fitness growth moves 2027-2028</title><style>
:root{--text:#14213D;--accent:#D9822B;--muted:#B8C0CC;--light:#E8EBF0;--bg:#FFFFFF}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#2B2F36;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;color:var(--text)}
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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should the Fernhill board approve on 10 December 2026?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should the Fernhill board approve on 10 December 2026?</h1><p class="t-sub">Closing the gap from EUR 58.0m to the EUR 66.0m 2028 target without a new city</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read. The decision we ask for is on page 2 and again on page 9.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap to accept for now"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap to accept for now</h2><div class="content summary"><p class="lead">Fernhill&#x27;s 34 gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, and the board has set a target of EUR 66.0m by 2028, up from EUR 58.0m in 2026, without new gyms in new cities and within EUR 2m of investment. Core membership revenue has been flat since 2023.</p><ol><li>Daytime capacity is the largest unused asset: an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).</li><li>Corporate wellness contracts are proven in the pilot (6 employers, 1,150 employees enrolled); 40 contracts by 2028 at an average EUR 60k a year add about EUR 2.4m a year (range EUR 1.4m to 3.0m).</li><li>The premium tier is priced below both main competitors (EUR 59 versus EUR 64 and EUR 67); a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m net of the churn seen after the 2024 increase.</li><li>A new city needs EUR 4.5m and pays back in about seven years against the board&#x27;s four-year limit; we recommend not pursuing one now.</li><li>Together the three moves reach about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target. We do not propose closing this gap with a new city.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh, start January 2027. Premium price change effective 1 March 2027. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry and pilot data 2026; competitor price lists September 2026</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Daytime capacity is the largest unused asset: utilisation falls to 31% from 10am to 4pm against 92% in the evening peak"><div class="tracker">1 Off-peak membership</div><h2 class="title long">Daytime capacity is the largest unused asset: utilisation falls to 31% from 10am to 4pm against 92% in the evening peak</h2><div class="header">Average gym utilisation by time band, % of capacity, 34 gyms, January to August 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Daytime capacity is the largest unused asset: utilisation falls to 31% from 10am to 4pm against 92% in the evening peak"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10am-4pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#B8C0CC"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10am-4pm band is both the lowest-used and the longest, six hours a day across all 34 gyms.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> This is the opportunity the off-peak membership is built to fill.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month, priced below the EUR 39 standard rate, adds about EUR 3.1m a year by 2028"><div class="tracker">1 Off-peak membership</div><h2 class="title long">An off-peak membership at EUR 24 a month, priced below the EUR 39 standard rate, adds about EUR 3.1m a year by 2028</h2><div class="header">Off-peak membership revenue in 2028 by take-up case, EUR m per year</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month, priced below the EUR 39 standard rate, adds about EUR 3.1m a year by 2028"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case (about 10,800</text><text x="350.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">members)</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Pilot in 4 gyms, May to August 2026: 420 sign-ups, 6% of them downgrades from an existing standard membership.</li><li>Systemwide target of about 10,800 off-peak members by 2028, across all 34 gyms.</li><li>Price point: EUR 24 a month off-peak versus EUR 39 standard.</li></ul></div></div><footer><div class="footnote">Risk to this range: if more than 15% of new off-peak members turn out to be downgrades from standard membership, the move adds less than EUR 2.0m.</div><div class="source">Source: Off-peak pilot, 4 gyms, May to August 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> The 6% downgrade rate seen in the pilot is well inside the 15% threshold that would cut the estimate below EUR 2.0m, but the board should track it as the pilot scales.</aside></section><section class="slide l-chart" id="s5" data-title="Corporate wellness contracts are proven in the pilot; scaling from 6 to 40 contracts by 2028 adds about EUR 2.4m a year"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Corporate wellness contracts are proven in the pilot; scaling from 6 to 40 contracts by 2028 adds about EUR 2.4m a year</h2><div class="header">Corporate wellness contracts signed, number of employers, 2026 pilot versus 2028 target</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Corporate wellness contracts are proven in the pilot; scaling from 6 to 40 contracts by 2028 adds about EUR 2.4m a year"><rect x="119.0" y="300.0" width="116.0" height="48.0" fill="#B8C0CC"/><text x="177.0" y="292.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6</text><text x="179.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2026 pilot</text><rect x="461.0" y="28.0" width="116.0" height="320.0" fill="#D9822B"/><text x="519.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="521.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028 target</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>2026 pilot: 6 employers signed, 1,150 employees enrolled.</li><li>40 contracts by 2028 at an average EUR 60k a year adds about EUR 2.4m a year (range EUR 1.4m to 3.0m).</li><li>Needs two corporate sales hires, starting by February 2027.</li></ul></div></div><footer><div class="footnote">The ramp to 40 contracts depends on the two sales hires starting on time; a later start pushes the ramp out and reduces 2028 revenue.</div><div class="source">Source: Corporate pilot contracts, 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> This is the smallest of the three moves but the one with the most direct evidence: the pilot has already closed six paying contracts.</aside></section><section class="slide l-chart" id="s6" data-title="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn"><div class="tracker">3 Premium price</div><h2 class="title long">Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn</h2><div class="header">Premium-tier monthly price for a comparable offer (pool, classes, sauna), EUR, September 2026</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn"><rect x="112" y="49.0" width="433.8" height="43.0" fill="#B8C0CC"/><text x="553.8" y="76.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="100.0" y="77.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><rect x="112" y="177.0" width="414.4" height="43.0" fill="#B8C0CC"/><text x="534.4" y="204.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="100.0" y="205.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="112" y="305.0" width="382.0" height="43.0" fill="#D9822B"/><text x="502.0" y="332.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="100.0" y="333.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill</text><line x1="112" x2="112" y1="8" y2="392.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>A EUR 4 increase on 25,000 premium members adds about EUR 1.2m a year before churn.</li><li>At the churn seen after the 2024 increase (1.5 points of extra churn for three months), the net add is about EUR 1.1m.</li><li>After the increase Fernhill premium would cost EUR 63, still below both competitors.</li></ul></div></div><footer><div class="footnote">The total on page 8 uses the EUR 1.2m before-churn figure, consistent with the growth model; using the EUR 1.1m net figure instead would narrow the 2028 total to about EUR 64.6m and widen the remaining gap to about EUR 1.4m.</div><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> Flag the churn caveat if asked; we are not hiding it, just using the model&#x27;s standard convention for the total on page 8.</aside></section><section class="slide l-table" id="s7" data-title="A new gym in a new city needs EUR 4.5m and pays back in about seven years, almost double the board&#x27;s four-year limit"><div class="tracker">4 New city</div><h2 class="title long">A new gym in a new city needs EUR 4.5m and pays back in about seven years, almost double the board&#x27;s four-year limit</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Measure</th><th>Value</th></tr><tr><td>Board&#x27;s payback limit</td><td>4 years</td></tr><tr><td>New-city gym, at the ramp of the last three openings</td><td>about 7 years</td></tr><tr><td>Investment required</td><td>EUR 4.5m</td></tr></table></div><div class="side"><ul><li>Based on the ramp of the last three gym openings, 2019 to 2023.</li><li>A new city would also need a new market entry (new city, not an existing one), which the board has excluded from this round.</li><li>We recommend not pursuing a new city now; revisit once the three approved moves are running.</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls, 2019 to 2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This is why the deck does not propose a fourth, larger lever to close the remaining EUR 1.3m gap.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add about EUR 6.7m, reaching about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Total effect</div><h2 class="title long">The three moves add about EUR 6.7m, reaching about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="header">Fernhill revenue bridge, 2026 to 2028, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add about EUR 6.7m, reaching about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><rect x="46.4" y="116.0" width="120.0" height="232.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="84.0" y2="84.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="89.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028 target EUR 66.0m</text><text x="106.4" y="108.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="103.6" width="120.0" height="12.4" fill="#B8C0CC"/><text x="303.2" y="95.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="116.0" y2="116.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="94.0" width="120.0" height="9.6" fill="#B8C0CC"/><text x="500.0" y="86.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="103.6" y2="103.6" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="89.2" width="120.0" height="4.8" fill="#B8C0CC"/><text x="696.8" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="94.0" y2="94.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="89.2" width="120.0" height="258.8" fill="#D9822B"/><text x="893.6" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="89.2" y2="89.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="348.0" y2="348.0" stroke="#14213D"/></svg></div></div><footer><div class="footnote">Core revenue without the three moves is assumed flat at EUR 58.0m; membership numbers were flat 2023-2026. Premium price shown before churn (see page 6); net of churn the total is about EUR 64.6m.</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> We are not proposing a fourth lever to close the EUR 1.3m gap this round. The board should decide whether to accept it or ask for further options at a later meeting.</aside></section><section class="slide l-table" id="s9" data-title="The board decides on 10 December 2026; the watch point is off-peak take-up against 6,000 members by end of 2027"><div class="tracker">Next steps</div><h2 class="title long">The board decides on 10 December 2026; the watch point is off-peak take-up against 6,000 members by end of 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board decision on EUR 1.9m and the premium price change</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak membership launch and marketing</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires start</td><td>COO Lena Marsh</td><td>February 2027</td></tr><tr><td>Premium price change in force</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Off-peak take-up review versus 6,000-member threshold</td><td>CFO</td><td>December 2027</td></tr></table></div><div class="side"><ul><li>Risk: off-peak cannibalisation above 15% of new sign-ups cuts the off-peak add below EUR 2.0m.</li><li>Risk: corporate sales ramp depends on both hires starting by February 2027.</li><li>Open point: the board should decide whether to accept the EUR 1.3m remaining gap or ask for a further lever at a later meeting.</li></ul></div></div><footer><div class="source">Source: Team plan; thresholds from Fernhill growth model v4</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly. Offer the December 2027 review as the checkpoint on the weakest assumption, off-peak take-up.</aside></section><section class="slide l-table" id="s10" data-title="Growth model assumptions"><div class="tracker">Appendix</div><h2 class="title">Growth model assumptions</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Off-peak members by 2028</td><td>about 10,800</td><td>Pilot (4 gyms, May-Aug 2026) scaled to 34 gyms; growth model v4</td></tr><tr><td>Off-peak price</td><td>EUR 24 a month</td><td>Fernhill pricing decision</td></tr><tr><td>Off-peak revenue 2028</td><td>EUR 3.1m (range 2.0 to 3.8)</td><td>Calculated</td></tr><tr><td>Corporate contracts by 2028</td><td>40 (pilot: 6 in 2026)</td><td>Growth model v4</td></tr><tr><td>Average corporate contract value</td><td>EUR 60k a year</td><td>Corporate pilot contracts 2026</td></tr><tr><td>Corporate revenue 2028</td><td>EUR 2.4m (range 1.4 to 3.0)</td><td>Calculated</td></tr><tr><td>Premium members</td><td>25,000</td><td>Fernhill membership data 2026</td></tr><tr><td>Premium price increase</td><td>EUR 4 a month</td><td>Pricing analysis</td></tr><tr><td>Premium revenue add</td><td>EUR 1.2m before churn, EUR 1.1m net</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>New-city investment</td><td>EUR 4.5m</td><td>Opening P&amp;Ls 2019-2023</td></tr><tr><td>New-city payback</td><td>about 7 years</td><td>Opening P&amp;Ls 2019-2023</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s11" data-title="Utilisation detail by time band"><div class="tracker">Appendix</div><h2 class="title">Utilisation detail by time band</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Time band</th><th class="num">Utilisation</th></tr><tr><td>6-10am</td><td class="num">58%</td></tr><tr><td>10am-4pm</td><td class="num">31%</td></tr><tr><td>4-6pm</td><td class="num">64%</td></tr><tr><td>6-9pm</td><td class="num">92%</td></tr><tr><td>9-11pm</td><td class="num">40%</td></tr></table></div></div><footer><div class="source">Source: Gate-entry data, 34 gyms, January to August 2026</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should the Fernhill board approve on 10 December 2026? <span style='color:#8A93A3'>(1)</span></li><li>Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap to accept for now <span style='color:#8A93A3'>(2)</span></li><li>Daytime capacity is the largest unused asset: utilisation falls to 31% from 10am to 4pm against 92% in the evening peak <span style='color:#8A93A3'>(3)</span></li><li>An off-peak membership at EUR 24 a month, priced below the EUR 39 standard rate, adds about EUR 3.1m a year by 2028 <span style='color:#8A93A3'>(4)</span></li><li>Corporate wellness contracts are proven in the pilot; scaling from 6 to 40 contracts by 2028 adds about EUR 2.4m a year <span style=

## File written by the run: 06-deck.md

---
title: Fernhill Fitness growth moves 2027-2028
client: Fernhill Fitness (fictional)
audience: Board of directors, pre-read for the 10 December 2026 meeting
date: December 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
  font: "Helvetica Neue, Helvetica, Arial, sans-serif"
---

# Deck: Which growth moves should the Fernhill board approve on 10 December 2026?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: Fernhill's 34 gyms run at 92% utilisation in the evening peak, and the board has set a target of EUR 66.0m revenue by 2028, up from EUR 58.0m in 2026, without opening gyms in new cities and within EUR 2m of investment.
- Complication: Core membership revenue has been flat since 2023, daytime capacity sits largely unused, and the obvious expansion route, a new city, does not pay back within the board's four-year limit.
- Question: Which growth moves should the board approve on 10 December 2026 to close the gap to EUR 66.0m?
- Answer: Launch an off-peak membership, sell corporate wellness contracts and raise the premium-tier price by EUR 4; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap the board should accept for now rather than chase with a new city.

**Key line**
1. Daytime capacity is the largest unused asset; an off-peak membership adds about EUR 3.1m a year by 2028.
2. Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year by 2028.
3. The premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year.
4. A new city does not pay back within the board's four-year limit.

## 1. Which growth moves should the Fernhill board approve on 10 December 2026?
layout: title
subtitle: Closing the gap from EUR 58.0m to the EUR 66.0m 2028 target without a new city
note: Pre-read. The decision we ask for is on page 2 and again on page 9.

## 2. Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap to accept for now
layout: summary
tracker: Executive summary
lead: Fernhill's 34 gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, and the board has set a target of EUR 66.0m by 2028, up from EUR 58.0m in 2026, without new gyms in new cities and within EUR 2m of investment. Core membership revenue has been flat since 2023.
body:
- Daytime capacity is the largest unused asset: an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).
- Corporate wellness contracts are proven in the pilot (6 employers, 1,150 employees enrolled); 40 contracts by 2028 at an average EUR 60k a year add about EUR 2.4m a year (range EUR 1.4m to 3.0m).
- The premium tier is priced below both main competitors (EUR 59 versus EUR 64 and EUR 67); a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m net of the churn seen after the 2024 increase.
- A new city needs EUR 4.5m and pays back in about seven years against the board's four-year limit; we recommend not pursuing one now.
- Together the three moves reach about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target. We do not propose closing this gap with a new city.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh, start January 2027. Premium price change effective 1 March 2027. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.
source: Fernhill growth model v4; gate-entry and pilot data 2026; competitor price lists September 2026
note: Read the bold line and the ask. Everything after this page proves one of the four points.

## 3. Daytime capacity is the largest unused asset: utilisation falls to 31% from 10am to 4pm against 92% in the evening peak
layout: chart
tracker: 1 Off-peak membership
message: time-series
chart: bar
header: Average gym utilisation by time band, % of capacity, 34 gyms, January to August 2026
highlight: 10am-4pm
| Time band | Utilisation |
|---|---|
| 6-10am | 58 |
| 10am-4pm | 31 |
| 4-6pm | 64 |
| 6-9pm | 92 |
| 9-11pm | 40 |
takeaway: The 10am-4pm band is both the lowest-used and the longest, six hours a day across all 34 gyms.
source: Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4
note: This is the opportunity the off-peak membership is built to fill.

## 4. An off-peak membership at EUR 24 a month, priced below the EUR 39 standard rate, adds about EUR 3.1m a year by 2028
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue in 2028 by take-up case, EUR m per year
highlight: Base case (about 10,800 members)
| Case | Revenue |
|---|---|
| Low | 2.0 |
| Base case (about 10,800 members) | 3.1 |
| High | 3.8 |
body:
- Pilot in 4 gyms, May to August 2026: 420 sign-ups, 6% of them downgrades from an existing standard membership.
- Systemwide target of about 10,800 off-peak members by 2028, across all 34 gyms.
- Price point: EUR 24 a month off-peak versus EUR 39 standard.
footnote: Risk to this range: if more than 15% of new off-peak members turn out to be downgrades from standard membership, the move adds less than EUR 2.0m.
source: Off-peak pilot, 4 gyms, May to August 2026; Fernhill growth model v4
note: The 6% downgrade rate seen in the pilot is well inside the 15% threshold that would cut the estimate below EUR 2.0m, but the board should track it as the pilot scales.

## 5. Corporate wellness contracts are proven in the pilot; scaling from 6 to 40 contracts by 2028 adds about EUR 2.4m a year
layout: chart
tracker: 2 Corporate wellness
message: time-series
chart: bar
header: Corporate wellness contracts signed, number of employers, 2026 pilot versus 2028 target
highlight: 2028 target
| Period | Contracts |
|---|---|
| 2026 pilot | 6 |
| 2028 target | 40 |
body:
- 2026 pilot: 6 employers signed, 1,150 employees enrolled.
- 40 contracts by 2028 at an average EUR 60k a year adds about EUR 2.4m a year (range EUR 1.4m to 3.0m).
- Needs two corporate sales hires, starting by February 2027.
footnote: The ramp to 40 contracts depends on the two sales hires starting on time; a later start pushes the ramp out and reduces 2028 revenue.
source: Corporate pilot contracts, 2026; Fernhill growth model v4
note: This is the smallest of the three moves but the one with the most direct evidence: the pilot has already closed six paying contracts.

## 6. Fernhill's premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn
layout: chart
tracker: 3 Premium price
message: ranking
chart: hbar
header: Premium-tier monthly price for a comparable offer (pool, classes, sauna), EUR, September 2026
highlight: Fernhill
| Provider | Price |
|---|---|
| Competitor B | 67 |
| Competitor A | 64 |
| Fernhill | 59 |
body:
- A EUR 4 increase on 25,000 premium members adds about EUR 1.2m a year before churn.
- At the churn seen after the 2024 increase (1.5 points of extra churn for three months), the net add is about EUR 1.1m.
- After the increase Fernhill premium would cost EUR 63, still below both competitors.
footnote: The total on page 8 uses the EUR 1.2m before-churn figure, consistent with the growth model; using the EUR 1.1m net figure instead would narrow the 2028 total to about EUR 64.6m and widen the remaining gap to about EUR 1.4m.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: Flag the churn caveat if asked; we are not hiding it, just using the model's standard convention for the total on page 8.

## 7. A new gym in a new city needs EUR 4.5m and pays back in about seven years, almost double the board's four-year limit
layout: table
tracker: 4 New city
| Measure | Value |
|---|---|
| Board's payback limit | 4 years |
| New-city gym, at the ramp of the last three openings | about 7 years |
| Investment required | EUR 4.5m |
body:
- Based on the ramp of the last three gym openings, 2019 to 2023.
- A new city would also need a new market entry (new city, not an existing one), which the board has excluded from this round.
- We recommend not pursuing a new city now; revisit once the three approved moves are running.
source: Opening P&Ls, 2019 to 2023; Fernhill growth model v4
note: This is why the deck does not propose a fourth, larger lever to close the remaining EUR 1.3m gap.

## 8. The three moves add about EUR 6.7m, reaching about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Fernhill revenue bridge, 2026 to 2028, EUR m per year
reference: 66.0 | 2028 target EUR 66.0m
highlight: Revenue 2028 with the three moves
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
footnote: Core revenue without the three moves is assumed flat at EUR 58.0m; membership numbers were flat 2023-2026. Premium price shown before churn (see page 6); net of churn the total is about EUR 64.6m.
source: Fernhill growth model v4
note: We are not proposing a fourth lever to close the EUR 1.3m gap this round. The board should decide whether to accept it or ask for further options at a later meeting.

## 9. The board decides on 10 December 2026; the watch point is off-peak take-up against 6,000 members by end of 2027
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board decision on EUR 1.9m and the premium price change | Board | 10 December 2026 |
| Off-peak membership launch and marketing | COO Lena Marsh | January 2027 |
| Two corporate sales hires start | COO Lena Marsh | February 2027 |
| Premium price change in force | COO Lena Marsh | 1 March 2027 |
| Off-peak take-up review versus 6,000-member threshold | CFO | December 2027 |
body:
- Risk: off-peak cannibalisation above 15% of new sign-ups cuts the off-peak add below EUR 2.0m.
- Risk: corporate sales ramp depends on both hires starting by February 2027.
- Open point: the board should decide whether to accept the EUR 1.3m remaining gap or ask for a further lever at a later meeting.
source: Team plan; thresholds from Fernhill growth model v4
note: Ask for the decision explicitly. Offer the December 2027 review as the checkpoint on the weakest assumption, off-peak take-up.

## A1. Growth model assumptions
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak members by 2028 | about 10,800 | Pilot (4 gyms, May-Aug 2026) scaled to 34 gyms; growth model v4 |
| Off-peak price | EUR 24 a month | Fernhill pricing decision |
| Off-peak revenue 2028 | EUR 3.1m (range 2.0 to 3.8) | Calculated |
| Corporate contracts by 2028 | 40 (pilot: 6 in 2026) | Growth model v4 |
| Average corporate contract value | EUR 60k a year | Corporate pilot contracts 2026 |
| Corporate revenue 2028 | EUR 2.4m (range 1.4 to 3.0) | Calculated |
| Premium members | 25,000 | Fernhill membership data 2026 |
| Premium price increase | EUR 4 a month | Pricing analysis |
| Premium revenue add | EUR 1.2m before churn, EUR 1.1m net | Fernhill membership data 2024-2026 |
| New-city investment | EUR 4.5m | Opening P&Ls 2019-2023 |
| New-city payback | about 7 years | Opening P&Ls 2019-2023 |
source: Fernhill growth model v4

## A2. Utilisation detail by time band
layout: table
tracker: Appendix
| Time band | Utilisation |
|---|---|
| 6-10am | 58% |
| 10am-4pm | 31% |
| 4-6pm | 64% |
| 6-9pm | 92% |
| 9-11pm | 40% |
source: Gate-entry data, 34 gyms, January to August 2026

# Titles-only read-through

Passes: the nine main titles alone tell the board what to fund, what each move is worth, why a new city is excluded, and what to decide.

