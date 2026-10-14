# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | Exec summary, slide 6 title, bridge, and assumptions table all use 'EUR 1.2m a year before churn'; the only appearance of 1.1 is a clearly-labeled footnote ('net gain is about EUR 1.1m') distinguishing gross vs net-of-churn, not a silent swap. |
| Writes 06-deck.md (or prints it) in the skill's spec format with frontmatter, SCQA in four sentences, key line above first slide | NO | The file is named 'deck.md', not '06-deck.md'; frontmatter, SCQA (Situation/Complication/Question/Answer) and Key line section are present and correctly placed, but the required filename does not match. |
| Page 2 is the executive summary with governing-thought title, numbered key-line points, EUR 1.3m gap, what-would-change-the-answer, and EUR 1.9m decision request with COO owner and start date | yes | Slide/page 2 title is the governing thought; body lists the four key-line findings plus the 1.3m gap and the 6,000-member threshold trigger; ask box states 'approve EUR 1.9m ... Owner: COO Lena Marsh. Off-peak launch January 2027; premium price change from 1 March 2027.' |
| Every main-page title is a full-sentence finding with a number or comparison; no topic-label titles | yes | Titles like 'Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm...' and 'A new-city gym needs EUR 4.5m and pays back in about seven years...' are full-sentence findings with numbers; only the appendix page ('Key assumptions behind the three moves') is a topic label, and it is ex |
| 8 to 15 main pages, sections follow the key line, new-city analysis included as a finding | yes | Main content pages 3-10 (8 pages) cover off-peak, corporate wellness, premium price, new city, bridge, risks, decision — matching the key line order; new-city page 7 states the finding plainly ('needs EUR 4.5m and pays back in about seven years, beyond the board's four-year limit'). |
| Utilisation by time band as bar chart with 10am-4pm highlighted; revenue bridge as waterfall 58.0→64.7 with 66.0 reference and 1.3 gap visible | yes | Slide 3 md specifies 'chart: bar' and 'highlight: 10am-4pm'; slide 8 md specifies 'chart: waterfall' with steps 58.0→3.1→2.4→1.2→64.7 and 'reference: 66 / Target 2028 EUR 66.0m', with the dashed reference line drawn above the final 64.7 bar making the gap visually apparent. |
| Every chart has a header with measure/unit/period and a source line from the synthesis | yes | E.g. 'Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026' / source 'Gate-entry data, 34 gyms, Jan to Aug 2026'; all six chart slides carry comparable header+source pairs. |
| Numbers tie across executive summary, section pages and bridge with no rounding drift | yes | 3.1 + 2.4 + 1.2 on top of 58.0 = 64.7 and 66.0-64.7=1.3 appear identically in the exec summary, each section title, and the bridge slide, with no alternate sums like 6.5 or 6.8. |
| A titles-only read-through is listed and tells the story in order | yes | The deck.html contains an '#overview' titles-only list in slide order from the governing question through exec summary, each key-line finding, bridge, risks, decision, and appendix, and the response notes 'titles-only read-through passes'. |
| If Python is available, runs render_deck.py and reports warnings; otherwise says spec delivered unrendered | yes | Response states 'deck.md — the spec (11 slides, titles-only read-through passes, no render warnings)' alongside delivered deck.html/deck.pptx, indicating the renderer ran and reported zero warnings. |
| Must not add new analysis, new numbers, competitor facts or sources not in the synthesis | yes | All figures (58.0, 3.1, 2.4, 1.2, 66.0, 1.3, competitor prices 64/67, EUR 4.5m/7-year payback, EUR 1.9m ask) match the given reference values; no extraneous facts introduced beyond derived arithmetic (e.g., 59+4=63). |
| Must not place agenda, method or background pages before the executive summary | yes | Page 1 is the title page and page 2 is immediately the executive summary; no agenda/method/background pages intervene. |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

The board pre-read deck is ready in the working directory:

- **`deck.md`** — the spec (11 slides, titles-only read-through passes, no render warnings)
- **`deck.html`** — self-contained, open in a browser (arrow keys to navigate, `t` for titles view, print to PDF for a one-page-per-slide handout)
- **`deck.pptx`** — native PowerPoint with live charts

Structure: title → executive summary (governing thought, all four numbers, the EUR 1.3m gap, and the EUR 1.9m decision ask) → one section per key-line point (off-peak utilisation and revenue, corporate wellness, premium pricing, why not a new city) → revenue bridge to the EUR 66.0m target → risks and what would change the answer → next steps with owner and dates → an appendix of key assumptions. Every number traces back to the synthesis and ties across the exec summary, section pages, and the EUR 64.7m/EUR 1.3m-gap total — nothing was invented to fill a gap.


## Files in work dir after run

- db-01-synthesis.md
- deck.html
- deck.md
- deck.pptx

## File written by the run: deck.html

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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should the Fernhill board approve on 10 December 2026?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should the Fernhill board approve on 10 December 2026?</h1><p class="t-sub">Recommendation on off-peak membership, corporate wellness and premium pricing</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read. The decision we ask for is on page 2 and again on page 10.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they lift revenue to about EUR 64.7m, EUR 1.3m short of the EUR 66.0m target for 2028"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they lift revenue to about EUR 64.7m, EUR 1.3m short of the EUR 66.0m target for 2028</h2><div class="content summary"><p class="lead">Fernhill Fitness runs 34 gyms at EUR 58.0m revenue in 2026. The board wants EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.</p><ol><li>Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm. An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).</li><li>Six employers signed in the corporate wellness pilot (1,150 employees). At 40 contracts by 2028 at EUR 60k a year, revenue adds about EUR 2.4m (range EUR 1.4m to 3.0m); needs two corporate sales hires.</li><li>The premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors. A EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn.</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit; we recommend not opening one.</li><li>The three moves leave a EUR 1.3m gap to the EUR 66.0m target. The answer changes if off-peak take-up falls below 6,000 members by the end of 2027.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak launch January 2027; premium price change from 1 March 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor price lists Sept 2026</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm, the largest unused asset"><div class="tracker">1 Off-peak membership</div><h2 class="title long">Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm, the largest unused asset</h2><div class="header">Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm, the largest unused asset"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10am-4pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#B8C0CC"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10am-4pm trough is the gap an off-peak membership is priced to fill.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> Six-hour daytime window across every gym in the estate, not a single site.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year"><div class="tracker">1 Off-peak membership</div><h2 class="title long">An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year</h2><div class="header">Off-peak membership revenue by 2028, EUR m per year, by scenario</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>EUR 24 a month, priced below the standard EUR 39</li><li>About 10,800 members by 2028 in the base case</li><li>Pilot: 4 gyms, May to Aug 2026, 420 sign-ups, 6% from existing members downgrading</li></ul></div></div><footer><div class="footnote">Range reflects cannibalisation uncertainty; above 15% downgrading, the gain falls below EUR 2.0m.</div><div class="source">Source: Off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> Cannibalisation above 15% is the single biggest risk to this number; see page 9.</aside></section><section class="slide l-chart" id="s5" data-title="Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year at 40 contracts by 2028"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year at 40 contracts by 2028</h2><div class="header">Corporate wellness revenue by 2028, EUR m per year, by scenario</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year at 40 contracts by 2028"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Six employers signed in the pilot, 1,150 employees enrolled</li><li>Base case: 40 contracts by 2028 at an average EUR 60k a year</li><li>Needs two corporate sales hires, starting by February 2027</li></ul></div></div><footer><div class="source">Source: Corporate pilot contracts, 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> The ramp depends on the two sales hires starting on time; see risks on page 9.</aside></section><section class="slide l-chart" id="s6" data-title="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn"><div class="tracker">3 Premium price</div><h2 class="title long">Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn</h2><div class="header">Premium membership price, EUR per month, Fernhill versus the two nearest competitors, September 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn"><rect x="112" y="42.3" width="810.7" height="43.0" fill="#B8C0CC"/><text x="930.7" y="69.3" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="100.0" y="70.3" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><rect x="112" y="157.0" width="774.4" height="43.0" fill="#B8C0CC"/><text x="894.4" y="184.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="100.0" y="185.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="112" y="271.7" width="713.9" height="43.0" fill="#D9822B"/><text x="833.9" y="298.7" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="100.0" y="299.7" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill</text><line x1="112" x2="112" y1="8" y2="352.0" stroke="#14213D"/></svg></div></div><div class="takeaway">After a EUR 4 increase, Fernhill still sits below both main competitors (63 versus 64 and 67).</div><footer><div class="footnote">At the churn seen after the 2024 increase (1.5 points extra for three months), the net gain is about EUR 1.1m.</div><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> Comparable offer in all three cases: pool, classes and sauna included.</aside></section><section class="slide l-chart" id="s7" data-title="A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit"><div class="tracker">4 New city</div><h2 class="title long">A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit</h2><div class="header">Payback period for a new-city gym versus the board&#x27;s four-year limit, years</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit"><line x1="8.0" x2="542.0" y1="188.0" y2="188.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="193.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Board&#x27;s four-year limit</text><rect x="215.0" y="68.0" width="116.0" height="280.0" fill="#D9822B"/><text x="273.0" y="60.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">New-city opening</text><line x1="8" x2="542" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Based on the ramp of the last three gym openings</li><li>Investment required: EUR 4.5m, above the board&#x27;s no-new-city brief</li></ul></div></div><footer><div class="footnote">We recommend not entering a new city before this payback improves.</div><div class="source">Source: Opening P&amp;Ls 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This is why the recommendation fills existing capacity instead of opening a new site.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves lift revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Total effect</div><h2 class="title">The three moves lift revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="header">Revenue bridge 2026 to 2028, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves lift revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><rect x="46.4" y="116.0" width="120.0" height="232.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="84.0" y2="84.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="89.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Target 2028 EUR 66.0m</text><text x="106.4" y="108.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="103.6" width="120.0" height="12.4" fill="#B8C0CC"/><text x="303.2" y="95.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="116.0" y2="116.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="94.0" width="120.0" height="9.6" fill="#B8C0CC"/><text x="500.0" y="86.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="103.6" y2="103.6" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="89.2" width="120.0" height="4.8" fill="#B8C0CC"/><text x="696.8" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="94.0" y2="94.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="89.2" width="120.0" height="258.8" fill="#D9822B"/><text x="893.6" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="89.2" y2="89.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="348.0" y2="348.0" stroke="#14213D"/></svg></div></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> Core revenue without new moves is assumed flat at EUR 58.0m; membership numbers have been flat 2023-2026. We do not hide the EUR 1.3m gap.</aside></section><section class="slide l-text" id="s9" data-title="The answer changes if off-peak take-up falls below 6,000 members by the end of 2027"><div class="tracker">Risks</div><h2 class="title">The answer changes if off-peak take-up falls below 6,000 members by the end of 2027</h2><div class="content text"><ul><li>Off-peak cannibalisation: if more than 15% of new off-peak members are downgrading standard members, the off-peak move adds less than EUR 2.0m instead of EUR 3.1m.</li><li>Corporate sales ramp depends on two hires starting by February 2027; a delay pushes the EUR 2.4m gain into 2029.</li><li>Even if both risks land, the recommendation is to accept the resulting gap rather than open a new city, which pays back in about seven years.</li></ul></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> These are the two numbers that would make the board revisit the plan before 2028.</aside></section><section class="slide l-table" id="s10" data-title="The board is asked to approve EUR 1.9m on 10 December 2026, with off-peak live from January 2027"><div class="tracker">Decision requested</div><h2 class="title long">The board is asked to approve EUR 1.9m on 10 December 2026, with off-peak live from January 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Approve EUR 1.9m (off-peak marketing EUR 0.8m; two corporate hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m)</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Launch off-peak membership</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Corporate sales hires start</td><td>COO Lena Marsh</td><td>By February 2027</td></tr><tr><td>Premium price change (+EUR 4) takes effect</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Review off-peak take-up against the 6,000-member threshold</td><td>COO Lena Marsh</td><td>December 2027</td></tr></table></div><div class="side"><ul><li>Owner for the full plan: COO Lena Marsh</li></ul></div></div><footer><div class="source">Source: Decision requested, Fernhill growth model v4</div><span class="pn">10</span></footer><aside class="notes"><b>Speaker note</b> Ask for the EUR 1.9m explicitly; offer the December 2027 review as the checkpoint.</aside></section><section class="slide l-table" id="s11" data-title="Key assumptions behind the three moves"><div class="tracker">Appendix</div><h2 class="title">Key assumptions behind the three moves</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Off-peak price</td><td>EUR 24 a month (standard EUR 39)</td><td>Fernhill pricing</td></tr><tr><td>Off-peak members by 2028</td><td>About 10,800</td><td>Fernhill growth model v4</td></tr><tr><td>Off-peak pilot result</td><td>420 sign-ups, 4 gyms, May-Aug 2026, 6% downgrading</td><td>Off-peak pilot 2026</td></tr><tr><td>Corporate contracts by 2028</td><td>40 at EUR 60k a year</td><td>Fernhill growth model v4</td></tr><tr><td>Corporate pilot result</td><td>6 employers, 1,150 employees</td><td>Corporate pilot contracts 2026</td></tr><tr><td>Premium price increase</td><td>EUR 4 on 25,000 members</td><td>Fernhill growth model v4</td></tr><tr><td>Premium churn reference</td><td>1.5 points extra for 3 months (2024 increase)</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>New-city investment and payback</td><td>EUR 4.5m, about 7 years</td><td>Opening P&amp;Ls 2019-2023</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">A1</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should the Fernhill board approve on 10 December 2026? <span style='color:#8A93A3'>(1)</span></li><li>Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they lift revenue to about EUR 64.7m, EUR 1.3m short of the EUR 66.0m target for 2028 <span style='color:#8A93A3'>(2)</span></li><li>Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm, the largest unused asset <span style='color:#8A93A3'>(3)</span></li><li>An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year <span style='color:#8A93A3'>(4)</span></li><li>Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year at 40 contracts by 2028 <span style='color:#8A93A3'>(5)</span></li><li>Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn <span style='color:#8A93A3'>(6)</span></li><li>A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit <span style='color:#8A93A3'>(7)</span></li><li>The three moves lift revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target <span style='color:#8A93A3'>(8)</span></li><li>The answer changes if off-peak take-up falls below 6,000 members by the end of 2027 <span style='color:#8A93A3'>(9)</span></li><li>The board is asked to approve EUR 1.9m on 10 December 2026, wit

## File written by the run: deck.md

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
- Situation: Fernhill Fitness runs 34 gyms and has held revenue at about EUR 58.0m.
- Complication: The board wants EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
- Question: Which growth moves should the board approve on 10 December 2026?
- Answer: Launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m, leaving a EUR 1.3m gap the board should accept rather than chase with a new city.

**Key line**
1. Daytime capacity is the largest unused asset.
2. Corporate wellness contracts are proven in the pilot.
3. The premium tier is priced below both main competitors.
4. A new city does not pay back within the board's four-year limit.

## 1. Which growth moves should the Fernhill board approve on 10 December 2026?
layout: title
subtitle: Recommendation on off-peak membership, corporate wellness and premium pricing
note: Pre-read. The decision we ask for is on page 2 and again on page 10.

## 2. Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they lift revenue to about EUR 64.7m, EUR 1.3m short of the EUR 66.0m target for 2028
layout: summary
tracker: Executive summary
lead: Fernhill Fitness runs 34 gyms at EUR 58.0m revenue in 2026. The board wants EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
body:
- Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm. An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).
- Six employers signed in the corporate wellness pilot (1,150 employees). At 40 contracts by 2028 at EUR 60k a year, revenue adds about EUR 2.4m (range EUR 1.4m to 3.0m); needs two corporate sales hires.
- The premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors. A EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn.
- A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board's four-year limit; we recommend not opening one.
- The three moves leave a EUR 1.3m gap to the EUR 66.0m target. The answer changes if off-peak take-up falls below 6,000 members by the end of 2027.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak launch January 2027; premium price change from 1 March 2027.
source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor price lists Sept 2026
note: Read the bold line and the ask. Everything after this page proves one of the four points.

## 3. Gyms run at 92% utilisation from 6 to 9pm but only 31% from 10am to 4pm, the largest unused asset
layout: chart
tracker: 1 Off-peak membership
message: time-series
chart: bar
header: Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026
highlight: 10am-4pm
scale: zero
| Time band | Utilisation |
|---|---|
| 6-10am | 58 |
| 10am-4pm | 31 |
| 4-6pm | 64 |
| 6-9pm | 92 |
| 9-11pm | 40 |
takeaway: The 10am-4pm trough is the gap an off-peak membership is priced to fill.
source: Gate-entry data, 34 gyms, Jan to Aug 2026
note: Six-hour daytime window across every gym in the estate, not a single site.

## 4. An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue by 2028, EUR m per year, by scenario
highlight: Base case
| Scenario | Revenue |
|---|---|
| Low | 2.0 |
| Base case | 3.1 |
| High | 3.8 |
body:
- EUR 24 a month, priced below the standard EUR 39
- About 10,800 members by 2028 in the base case
- Pilot: 4 gyms, May to Aug 2026, 420 sign-ups, 6% from existing members downgrading
footnote: Range reflects cannibalisation uncertainty; above 15% downgrading, the gain falls below EUR 2.0m.
source: Off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4
note: Cannibalisation above 15% is the single biggest risk to this number; see page 9.

## 5. Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year at 40 contracts by 2028
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness revenue by 2028, EUR m per year, by scenario
highlight: Base case
| Scenario | Revenue |
|---|---|
| Low | 1.4 |
| Base case | 2.4 |
| High | 3.0 |
body:
- Six employers signed in the pilot, 1,150 employees enrolled
- Base case: 40 contracts by 2028 at an average EUR 60k a year
- Needs two corporate sales hires, starting by February 2027
source: Corporate pilot contracts, 2026; Fernhill growth model v4
note: The ramp depends on the two sales hires starting on time; see risks on page 9.

## 6. Fernhill's premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn
layout: chart
tracker: 3 Premium price
message: ranking
chart: hbar
header: Premium membership price, EUR per month, Fernhill versus the two nearest competitors, September 2026
highlight: Fernhill
| Supplier | Price |
|---|---|
| Competitor B | 67 |
| Competitor A | 64 |
| Fernhill | 59 |
takeaway: After a EUR 4 increase, Fernhill still sits below both main competitors (63 versus 64 and 67).
footnote: At the churn seen after the 2024 increase (1.5 points extra for three months), the net gain is about EUR 1.1m.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: Comparable offer in all three cases: pool, classes and sauna included.

## 7. A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board's four-year limit
layout: chart
tracker: 4 New city
message: deviation
chart: bar
header: Payback period for a new-city gym versus the board's four-year limit, years
reference: 4 | Board's four-year limit
highlight: New-city opening
scale: zero
| Option | Payback |
|---|---|
| New-city opening | 7 |
body:
- Based on the ramp of the last three gym openings
- Investment required: EUR 4.5m, above the board's no-new-city brief
footnote: We recommend not entering a new city before this payback improves.
source: Opening P&Ls 2019-2023; Fernhill growth model v4
note: This is why the recommendation fills existing capacity instead of opening a new site.

## 8. The three moves lift revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge 2026 to 2028, EUR m per year
reference: 66 | Target 2028 EUR 66.0m
highlight: Revenue 2028 with the three moves
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
source: Fernhill growth model v4
note: Core revenue without new moves is assumed flat at EUR 58.0m; membership numbers have been flat 2023-2026. We do not hide the EUR 1.3m gap.

## 9. The answer changes if off-peak take-up falls below 6,000 members by the end of 2027
layout: text
tracker: Risks
body:
- Off-peak cannibalisation: if more than 15% of new off-peak members are downgrading standard members, the off-peak move adds less than EUR 2.0m instead of EUR 3.1m.
- Corporate sales ramp depends on two hires starting by February 2027; a delay pushes the EUR 2.4m gain into 2029.
- Even if both risks land, the recommendation is to accept the resulting gap rather than open a new city, which pays back in about seven years.
source: Fernhill growth model v4
note: These are the two numbers that would make the board revisit the plan before 2028.

## 10. The board is asked to approve EUR 1.9m on 10 December 2026, with off-peak live from January 2027
layout: table
tracker: Decision requested
| Step | Owner | By when |
|---|---|---|
| Approve EUR 1.9m (off-peak marketing EUR 0.8m; two corporate hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m) | Board | 10 December 2026 |
| Launch off-peak membership | COO Lena Marsh | January 2027 |
| Corporate sales hires start | COO Lena Marsh | By February 2027 |
| Premium price change (+EUR 4) takes effect | COO Lena Marsh | 1 March 2027 |
| Review off-peak take-up against the 6,000-member threshold | COO Lena Marsh | December 2027 |
body:
- Owner for the full plan: COO Lena Marsh
source: Decision requested, Fernhill growth model v4
note: Ask for the EUR 1.9m explicitly; offer the December 2027 review as the checkpoint.

## A1. Key assumptions behind the three moves
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak price | EUR 24 a month (standard EUR 39) | Fernhill pricing |
| Off-peak members by 2028 | About 10,800 | Fernhill growth model v4 |
| Off-peak pilot result | 420 sign-ups, 4 gyms, May-Aug 2026, 6% downgrading | Off-peak pilot 2026 |
| Corporate contracts by 2028 | 40 at EUR 60k a year | Fernhill growth model v4 |
| Corporate pilot result | 6 employers, 1,150 employees | Corporate pilot contracts 2026 |
| Premium price increase | EUR 4 on 25,000 members | Fernhill growth model v4 |
| Premium churn reference | 1.5 points extra for 3 months (2024 increase) | Fernhill membership data 2024-2026 |
| New-city investment and payback | EUR 4.5m, about 7 years | Opening P&Ls 2019-2023 |
source: Fernhill growth model v4

