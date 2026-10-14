# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | 'adds about EUR 1.2m a year before churn, about EUR 1.1m after the churn seen following the 2024 price rise' — both figures consistently flagged together in exec summary, slide 6 title, and footnote; bridge uses 1.2 consistently for the total (58.0+3.1+2.4+1.2=64.7) |
| Writes 06-deck.md (or prints it) in the skill's spec format with frontmatter, SCQA opening in four sentences, key line above first slide | NO | File list shows 'deck.md' was written, not '06-deck.md'; content itself does have frontmatter, a 4-sentence SCQA opening, and a key line placed above slide 1, but the required filename is not used |
| Page 2 is executive summary with governing thought title, one point per key-line statement with number, EUR 1.3m gap, what would change the answer, decision request with EUR 1.9m/COO/start date | yes | Slide 2 title is the governing thought; ordered list items 1-4 mirror the key line, item 5 states 'The three moves leave a EUR 1.3m gap... answer changes if off-peak take-up falls below 6,000 members'; ask box: 'approve EUR 1.9m ... Owner: COO Lena Marsh. Start January 2027' |
| Every main-page title is a full-sentence finding with a number/comparison; no topic-label titles | yes | Titles like 'Daytime utilisation falls to 31% between 10 am and 4 pm, against 92% in the 6-9 pm peak' and 'A new-city gym needs EUR 4.5m and pays back in about seven years...' are full-sentence findings with numbers; appendix-only pages (A1/A2) use topic labels but are excluded from 'main pages' |
| 8-15 main pages, sections follow key line (not phases), new-city analysis included as a finding | yes | Trackers '1 Off-peak membership', '2 Corporate wellness', '3 Premium pricing', '4 New city (not recommended)', 'Total effect', 'Next steps' map directly to the key line; main pages 2-9 = 8 pages; new city given its own page 7 as a finding, not hidden |
| Utilisation-by-time-band bar chart with 10am-4pm highlighted; waterfall bridge 58.0→64.7 with 66.0 reference and 1.3 gap visible | yes | Slide 3 markdown 'highlight: 10 am-4 pm; 6-9 pm' with orange bars for 31 and 92; slide 8 waterfall from 58.0 to 64.7 with 'reference: 66.0 / 2028 target EUR 66.0m' and title/takeaway stating the EUR 1.3m gap |
| Every chart has a header (measure, unit, period) and a source line from the synthesis | yes | e.g. 'Gym utilisation by time band, % of capacity, average of 34 gyms, January to August 2026' with source 'Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4' — present on all six chart slides |
| Numbers tie across executive summary, section pages and bridge with no rounding drift | yes | 3.1 + 2.4 + 1.2 = 6.7m consistently used in exec summary and bridge (58.0+3.1+2.4+1.2=64.7); no alternate totals like 6.5 or 6.8 appear anywhere |
| Titles-only read-through is listed and tells the story in order | yes | HTML contains '#overview' div titled 'Titles-only read-through' with ordered list of slide titles, and the response states 'Titles-only read-through passes — read in order, they tell the full story' |
| If Python available, runs render_deck.py and reports warnings; otherwise states spec delivered unrendered | yes | Response states 'Both files rendered cleanly, no warnings' indicating the renderer was run and its (empty) warning output reported |
| Does not add new analysis, numbers, competitor facts, or sources not in the synthesis | yes | No content in the deck appears inconsistent with the stated sources (gate-entry data, pilots, competitor price lists, growth model v4); no new figures introduced beyond those cited to existing sources |
| Does not place agenda/method/background pages before the executive summary | yes | Page 1 is the title page and page 2 is immediately the executive summary; no agenda or method page intervenes |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

Both files rendered cleanly, no warnings. The board pre-read deck is ready:

- **`deck.md`** — the spec (source of truth, title + executive summary + 7 main sections + 2 appendix pages)
- **`deck.html`** — self-contained, open in a browser (arrow keys to navigate, `t` for titles-only view, `n` for speaker notes, print to PDF)
- **`deck.pptx`** — native PowerPoint with live charts

**Structure** (9 main pages + 2 appendix):
1. Title
2. Executive summary — governing thought, all four moves with numbers, the EUR 1.3m gap, and the EUR 1.9m decision ask
3. Daytime utilisation (31% vs 92% peak) — the opportunity
4. Off-peak membership: +EUR 3.1m (range 2.0–3.8)
5. Corporate wellness: +EUR 2.4m (range 1.4–3.0)
6. Premium price +EUR 4: +EUR 1.2m before churn, EUR 1.1m after
7. New city: 7-year payback, misses the 4-year limit — why it's not recommended
8. Revenue bridge waterfall: 58.0 → 64.7, EUR 1.3m short of the EUR 66.0m target
9. Next steps, risks, and the decision request
Appendix: full utilisation table, model assumptions and sources

Titles-only read-through passes — read in order, they tell the full story — and every number ties across the executive summary, sections, waterfall and appendix to the EUR 1.2m (not 1.1m) convention used in the official total, with the churn-adjusted figure flagged alongside it rather than silently dropped.


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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should the Fernhill board approve on 10 December 2026?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should the Fernhill board approve on 10 December 2026?</h1><p class="t-sub">Recommendation on off-peak membership, corporate wellness and premium pricing</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the 10 December 2026 board meeting. The decision requested is on page 2 and again on page 9.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should launch an off-peak membership, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m, reaching EUR 64.7m of the EUR 66.0m 2028 target"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should launch an off-peak membership, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m, reaching EUR 64.7m of the EUR 66.0m 2028 target</h2><div class="content summary"><p class="lead">Fernhill Fitness runs 34 gyms generating EUR 58.0m in revenue in 2026. Evening classes are full but daytime floor space is largely unused, and the board has set a target of EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.</p><ol><li>Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).</li><li>Six employers already signed in the corporate wellness pilot (1,150 employees); at 40 contracts by 2028 averaging EUR 60k a year, this adds about EUR 2.4m a year (range EUR 1.4m to 3.0m), needing two corporate sales hires.</li><li>The premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m after the churn seen following the 2024 price rise.</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings, missing the board&#x27;s four-year limit.</li><li>The three moves leave a EUR 1.3m gap to the EUR 66.0m target. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Start January 2027; premium price change from 1 March 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data and corporate pilot, 2026; competitor price lists, September 2026</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points above.</aside></section><section class="slide l-chart" id="s3" data-title="Daytime utilisation falls to 31% between 10 am and 4 pm, against 92% in the 6-9 pm peak"><div class="tracker">1 Off-peak membership</div><h2 class="title">Daytime utilisation falls to 31% between 10 am and 4 pm, against 92% in the 6-9 pm peak</h2><div class="header">Gym utilisation by time band, % of capacity, average of 34 gyms, January to August 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Daytime utilisation falls to 31% between 10 am and 4 pm, against 92% in the 6-9 pm peak"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10 am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10 am-4 pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6 pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#D9822B"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9 pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11 pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10 am-4 pm trough is unsold capacity in gyms that are already built and staffed.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> This is the asset the off-peak membership is designed to sell.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028"><div class="tracker">1 Off-peak membership</div><h2 class="title">An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028</h2><div class="header">Off-peak membership revenue by 2028, EUR m per year, scenario range</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case (EUR 3.1m)</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Priced below the EUR 39 standard tier; reaches about 10,800 off-peak members by 2028.</li><li>Pilot in 4 gyms, May to August 2026: 420 sign-ups, 6% downgrading from an existing standard membership.</li><li>Risk: if more than 15% of new off-peak members are downgrades, the move adds less than EUR 2.0m.</li></ul></div></div><footer><div class="footnote">Take-up above 10,800 members or below 6,000 by end of 2027 would move the range.</div><div class="source">Source: Gate-entry data, 34 gyms, January to August 2026; off-peak pilot, 4 gyms, May to August 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> Cannibalisation above 15% is the single biggest risk to this number.</aside></section><section class="slide l-chart" id="s5" data-title="Six employer pilots covering 1,150 employees show corporate wellness adds about EUR 2.4m a year by 2028"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Six employer pilots covering 1,150 employees show corporate wellness adds about EUR 2.4m a year by 2028</h2><div class="header">Corporate wellness contract revenue by 2028, EUR m per year, scenario range (40 contracts, average EUR 60k a year)</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Six employer pilots covering 1,150 employees show corporate wellness adds about EUR 2.4m a year by 2028"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case (EUR 2.4m)</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Six employers already signed in the 2026 pilot, with 1,150 employees enrolled.</li><li>Scaling to 40 contracts by 2028 requires two corporate sales hires, starting by February 2027.</li><li>Risk: the ramp depends on both hires starting on schedule.</li></ul></div></div><footer><div class="source">Source: Corporate pilot contracts, 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> This is the second-largest move and the one most exposed to a hiring delay.</aside></section><section class="slide l-chart" id="s6" data-title="A EUR 4 premium-price increase on 25,000 members adds about EUR 1.2m a year, EUR 1.1m after 2024-level churn"><div class="tracker">3 Premium pricing</div><h2 class="title long">A EUR 4 premium-price increase on 25,000 members adds about EUR 1.2m a year, EUR 1.1m after 2024-level churn</h2><div class="header">Monthly premium-tier price, EUR, comparable offer with pool, classes and sauna, September 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A EUR 4 premium-price increase on 25,000 members adds about EUR 1.2m a year, EUR 1.1m after 2024-level churn"><rect x="280" y="28.0" width="670.0" height="43.0" fill="#B8C0CC"/><text x="958.0" y="55.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="268.0" y="56.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="280" y="114.0" width="640.0" height="43.0" fill="#B8C0CC"/><text x="928.0" y="141.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="268.0" y="142.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><rect x="280" y="200.0" width="630.0" height="43.0" fill="#D9822B"/><text x="918.0" y="227.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">63</text><text x="268.0" y="228.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill (after +EUR 4, from March 2027)</text><rect x="280" y="286.0" width="590.0" height="43.0" fill="#B8C0CC"/><text x="878.0" y="313.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="268.0" y="314.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill (current)</text><line x1="280" x2="280" y1="8" y2="352.0" stroke="#14213D"/></svg></div></div><div class="takeaway">Even after the increase, Fernhill premium stays below both main competitors.</div><footer><div class="footnote">After the 2024 price increase, churn rose 1.5 points for three months; the same pattern would cut the EUR 1.2m pre-churn gain to about EUR 1.1m.</div><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> Priced to stay below both competitors even after the increase, which is why we see limited volume risk.</aside></section><section class="slide l-chart" id="s7" data-title="A new-city gym needs EUR 4.5m and pays back in about seven years, missing the board&#x27;s four-year limit"><div class="tracker">4 New city (not recommended)</div><h2 class="title long">A new-city gym needs EUR 4.5m and pays back in about seven years, missing the board&#x27;s four-year limit</h2><div class="header">Payback period for a new-city gym opening, years, at the ramp of the last three openings (2019-2023)</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A new-city gym needs EUR 4.5m and pays back in about seven years, missing the board&#x27;s four-year limit"><line x1="8.0" x2="542.0" y1="188.0" y2="188.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="193.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Board&#x27;s four-year payback limit</text><rect x="215.0" y="68.0" width="116.0" height="280.0" fill="#D9822B"/><text x="273.0" y="60.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">New-city gym</text><line x1="8" x2="542" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Investment required: EUR 4.5m, against the board&#x27;s EUR 2m ceiling for this round.</li><li>Ramp based on the three most recent openings, 2019 to 2023.</li><li>The EUR 1.3m gap to target (page 8) is smaller than the risk of a new city that does not pay back in time.</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls, 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This is why the recommendation is to accept the gap rather than open a new city.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Total effect</div><h2 class="title long">The three moves add EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="header">Revenue bridge, 2026 to 2028, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><rect x="46.4" y="105.0" width="120.0" height="203.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="77.0" y2="77.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="82.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028 target EUR 66.0m</text><text x="106.4" y="97.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="94.2" width="120.0" height="10.8" fill="#D9822B"/><text x="303.2" y="86.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="105.0" y2="105.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="85.8" width="120.0" height="8.4" fill="#B8C0CC"/><text x="500.0" y="77.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="94.2" y2="94.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="81.5" width="120.0" height="4.2" fill="#B8C0CC"/><text x="696.8" y="73.5" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="85.8" y2="85.8" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="81.5" width="120.0" height="226.5" fill="#14213D"/><text x="893.6" y="73.5" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="81.5" y2="81.5" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="347.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="308.0" y2="308.0" stroke="#14213D"/></svg></div></div><div class="takeaway">The EUR 1.3m gap is within the combined error range of the three estimates; we do not hide it.</div><footer><div class="footnote">Core revenue assumed flat at EUR 58.0m without the three moves (membership numbers flat 2023-2026).</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> The gap is the reason the board is asked to accept it rather than fund a new city to close it.</aside></section><section class="slide l-table" id="s9" data-title="The board decides on 10 December 2026; the answer changes below 6,000 off-peak members by end of 2027"><div class="tracker">Next steps</div><h2 class="title long">The board decides on 10 December 2026; the answer changes below 6,000 off-peak members by end of 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board decision on EUR 1.9m investment</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak launch marketing (EUR 0.8m)</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Booking-app changes (EUR 0.5m)</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires and pilot extension (EUR 0.6m)</td><td>COO Lena Marsh</td><td>By February 2027</td></tr><tr><td>Premium price increase (+EUR 4) takes effect</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Off-peak take-up checkpoint against 6,000-member threshold</td><td>COO Lena Marsh</td><td>End of 2027</td></tr></table></div><div class="side"><ul><li>Risk: off-peak cannibalisation above 15% of new sign-ups cuts that move to under EUR 2.0m.</li><li>Risk: corporate sales ramp depends on both hires starting by February 2027.</li><li>What would change the answer: off-peak take-up below 6,000 members by end of 2027.</li></ul></div></div><footer><div class="source">Source: Fernhill growth model v4; decision terms as requested for 10 December 2026</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly; offer the end-2027 checkpoint as the review point.</aside></section><section class="slide l-table" id="s10" data-title="Utilisation by time band, full data"><div class="tracker">Appendix</div><h2 class="title">Utilisation by time band, full data</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Time band</th><th class="num">Utilisation</th></tr><tr><td>6-10 am</td><td class="num">58%</td></tr><tr><td>10 am-4 pm</td><td class="num">31%</td></tr><tr><td>4-6 pm</td><td class="num">64%</td></tr><tr><td>6-9 pm</td><td class="num">92%</td></tr><tr><td>9-11 pm</td><td class="num">40%</td></tr></table></div></div><footer><div class="source">Source: Gate-entry data, 34 gyms, January to August 2026</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s11" data-title="Model assumptions and sources"><div class="tracker">Appendix</div><h2 class="title">Model assumptions and sources</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Off-peak price</td><td>EUR 24/month (vs EUR 39 standard)</td><td>Fernhill pricing, 2026</td></tr><tr><td>Off-peak members by 2028</td><td>About 10,800 (range underlying EUR 2.0m-3.8m)</td><td>Fernhill growth model v4; pilot, 4 gyms, May-Aug 2026</td></tr><tr><td>Off-peak pilot downgrade rate</td><td>6% of 420 sign-ups</td><td>Off-peak pilot, May-Aug 2026</td></tr><tr><td>Corporate contracts by 2028</td><td>40 at average EUR 60k/year</td><td>Fernhill growth model v4; pilot, 6 employers, 1,150 employees, 2026</td></tr><tr><td>Premium members</td><td>25,000</td><td>Fernhill membership data, 2024-2026</td></tr><tr><td>Premium price increase</td><td>+EUR 4/month, from 1 March 2027</td><td>Decision requested</td></tr><tr><td>Churn after 2024 price increase</td><td>+1.5 points for 3 months</td><td>Fernhill membership data, 2024-2026</td></tr><tr><td>New-city investment</td><td>EUR 4.5m</td><td>Opening P&amp;Ls, 2019-2023</td></tr><tr><td>New-city payback</td><td>About 7 years, vs board&#x27;s 4-year limit</td><td>Opening P&amp;Ls, 2019-2023</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should the Fernhill board approve on 10 December 2026? <span style='color:#8A93A3'>(1)</span></li><li>Fernhill should launch an off-peak membership, sell corporate wellness and raise the premium price by EUR 4; together they ad

## File written by the run: deck.md

---
title: Fernhill Fitness growth moves 2027-2028
client: Fernhill Fitness (fictional)
audience: Board of directors, pre-read for the 10 December 2026 meeting
date: December 2026
format: deck
---

# Deck: Which growth moves should the Fernhill board approve on 10 December 2026?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: Fernhill Fitness runs 34 gyms generating EUR 58.0m in revenue in 2026, with evening classes full but daytime floor space largely unused.
- Complication: The board has set a target of EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
- Question: Which growth moves should the board approve on 10 December 2026 to close that gap?
- Answer: Launch an off-peak membership, sell corporate wellness contracts and raise the premium tier price by EUR 4; together they add about EUR 6.7m and reach EUR 64.7m, leaving a EUR 1.3m gap the board should accept for now rather than chase with a new city.

**Key line**
1. Daytime capacity is the largest unused asset; an off-peak membership adds about EUR 3.1m a year by 2028.
2. Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year by 2028.
3. The premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year.
4. A new city does not pay back within the board's four-year limit.

## 1. Which growth moves should the Fernhill board approve on 10 December 2026?
layout: title
subtitle: Recommendation on off-peak membership, corporate wellness and premium pricing
note: Pre-read for the 10 December 2026 board meeting. The decision requested is on page 2 and again on page 9.

## 2. Fernhill should launch an off-peak membership, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m, reaching EUR 64.7m of the EUR 66.0m 2028 target
layout: summary
tracker: Executive summary
lead: Fernhill Fitness runs 34 gyms generating EUR 58.0m in revenue in 2026. Evening classes are full but daytime floor space is largely unused, and the board has set a target of EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.
body:
- Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).
- Six employers already signed in the corporate wellness pilot (1,150 employees); at 40 contracts by 2028 averaging EUR 60k a year, this adds about EUR 2.4m a year (range EUR 1.4m to 3.0m), needing two corporate sales hires.
- The premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m after the churn seen following the 2024 price rise.
- A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings, missing the board's four-year limit.
- The three moves leave a EUR 1.3m gap to the EUR 66.0m target. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Start January 2027; premium price change from 1 March 2027.
source: Fernhill growth model v4; gate-entry data and corporate pilot, 2026; competitor price lists, September 2026
note: Read the bold line and the ask. Everything after this page proves one of the four points above.

## 3. Daytime utilisation falls to 31% between 10 am and 4 pm, against 92% in the 6-9 pm peak
layout: chart
tracker: 1 Off-peak membership
message: deviation
chart: bar
header: Gym utilisation by time band, % of capacity, average of 34 gyms, January to August 2026
highlight: 10 am-4 pm; 6-9 pm
| Time band | Utilisation |
|---|---|
| 6-10 am | 58 |
| 10 am-4 pm | 31 |
| 4-6 pm | 64 |
| 6-9 pm | 92 |
| 9-11 pm | 40 |
takeaway: The 10 am-4 pm trough is unsold capacity in gyms that are already built and staffed.
source: Gate-entry data, 34 gyms, January to August 2026; Fernhill growth model v4
note: This is the asset the off-peak membership is designed to sell.

## 4. An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue by 2028, EUR m per year, scenario range
highlight: Base case (EUR 3.1m)
| Scenario | Revenue |
|---|---|
| Low | 2.0 |
| Base case (EUR 3.1m) | 3.1 |
| High | 3.8 |
body:
- Priced below the EUR 39 standard tier; reaches about 10,800 off-peak members by 2028.
- Pilot in 4 gyms, May to August 2026: 420 sign-ups, 6% downgrading from an existing standard membership.
- Risk: if more than 15% of new off-peak members are downgrades, the move adds less than EUR 2.0m.
footnote: Take-up above 10,800 members or below 6,000 by end of 2027 would move the range.
source: Gate-entry data, 34 gyms, January to August 2026; off-peak pilot, 4 gyms, May to August 2026; Fernhill growth model v4
note: Cannibalisation above 15% is the single biggest risk to this number.

## 5. Six employer pilots covering 1,150 employees show corporate wellness adds about EUR 2.4m a year by 2028
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness contract revenue by 2028, EUR m per year, scenario range (40 contracts, average EUR 60k a year)
highlight: Base case (EUR 2.4m)
| Scenario | Revenue |
|---|---|
| Low | 1.4 |
| Base case (EUR 2.4m) | 2.4 |
| High | 3.0 |
body:
- Six employers already signed in the 2026 pilot, with 1,150 employees enrolled.
- Scaling to 40 contracts by 2028 requires two corporate sales hires, starting by February 2027.
- Risk: the ramp depends on both hires starting on schedule.
source: Corporate pilot contracts, 2026; Fernhill growth model v4
note: This is the second-largest move and the one most exposed to a hiring delay.

## 6. A EUR 4 premium-price increase on 25,000 members adds about EUR 1.2m a year, EUR 1.1m after 2024-level churn
layout: chart
tracker: 3 Premium pricing
message: ranking
chart: hbar
header: Monthly premium-tier price, EUR, comparable offer with pool, classes and sauna, September 2026
highlight: Fernhill (after +EUR 4, from March 2027)
| Supplier | Price |
|---|---|
| Competitor A | 67 |
| Competitor B | 64 |
| Fernhill (after +EUR 4, from March 2027) | 63 |
| Fernhill (current) | 59 |
takeaway: Even after the increase, Fernhill premium stays below both main competitors.
footnote: After the 2024 price increase, churn rose 1.5 points for three months; the same pattern would cut the EUR 1.2m pre-churn gain to about EUR 1.1m.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: Priced to stay below both competitors even after the increase, which is why we see limited volume risk.

## 7. A new-city gym needs EUR 4.5m and pays back in about seven years, missing the board's four-year limit
layout: chart
tracker: 4 New city (not recommended)
message: deviation
chart: bar
header: Payback period for a new-city gym opening, years, at the ramp of the last three openings (2019-2023)
reference: 4 | Board's four-year payback limit
highlight: New-city gym
| Option | Payback |
|---|---|
| New-city gym | 7 |
body:
- Investment required: EUR 4.5m, against the board's EUR 2m ceiling for this round.
- Ramp based on the three most recent openings, 2019 to 2023.
- The EUR 1.3m gap to target (page 8) is smaller than the risk of a new city that does not pay back in time.
source: Opening P&Ls, 2019-2023; Fernhill growth model v4
note: This is why the recommendation is to accept the gap rather than open a new city.

## 8. The three moves add EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge, 2026 to 2028, EUR m per year
reference: 66.0 | 2028 target EUR 66.0m
highlight: Off-peak membership
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
takeaway: The EUR 1.3m gap is within the combined error range of the three estimates; we do not hide it.
footnote: Core revenue assumed flat at EUR 58.0m without the three moves (membership numbers flat 2023-2026).
source: Fernhill growth model v4
note: The gap is the reason the board is asked to accept it rather than fund a new city to close it.

## 9. The board decides on 10 December 2026; the answer changes below 6,000 off-peak members by end of 2027
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board decision on EUR 1.9m investment | Board | 10 December 2026 |
| Off-peak launch marketing (EUR 0.8m) | COO Lena Marsh | January 2027 |
| Booking-app changes (EUR 0.5m) | COO Lena Marsh | January 2027 |
| Two corporate sales hires and pilot extension (EUR 0.6m) | COO Lena Marsh | By February 2027 |
| Premium price increase (+EUR 4) takes effect | COO Lena Marsh | 1 March 2027 |
| Off-peak take-up checkpoint against 6,000-member threshold | COO Lena Marsh | End of 2027 |
body:
- Risk: off-peak cannibalisation above 15% of new sign-ups cuts that move to under EUR 2.0m.
- Risk: corporate sales ramp depends on both hires starting by February 2027.
- What would change the answer: off-peak take-up below 6,000 members by end of 2027.
source: Fernhill growth model v4; decision terms as requested for 10 December 2026
note: Ask for the decision explicitly; offer the end-2027 checkpoint as the review point.

## A1. Utilisation by time band, full data
layout: table
tracker: Appendix
| Time band | Utilisation |
|---|---|
| 6-10 am | 58% |
| 10 am-4 pm | 31% |
| 4-6 pm | 64% |
| 6-9 pm | 92% |
| 9-11 pm | 40% |
source: Gate-entry data, 34 gyms, January to August 2026

## A2. Model assumptions and sources
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak price | EUR 24/month (vs EUR 39 standard) | Fernhill pricing, 2026 |
| Off-peak members by 2028 | About 10,800 (range underlying EUR 2.0m-3.8m) | Fernhill growth model v4; pilot, 4 gyms, May-Aug 2026 |
| Off-peak pilot downgrade rate | 6% of 420 sign-ups | Off-peak pilot, May-Aug 2026 |
| Corporate contracts by 2028 | 40 at average EUR 60k/year | Fernhill growth model v4; pilot, 6 employers, 1,150 employees, 2026 |
| Premium members | 25,000 | Fernhill membership data, 2024-2026 |
| Premium price increase | +EUR 4/month, from 1 March 2027 | Decision requested |
| Churn after 2024 price increase | +1.5 points for 3 months | Fernhill membership data, 2024-2026 |
| New-city investment | EUR 4.5m | Opening P&Ls, 2019-2023 |
| New-city payback | About 7 years, vs board's 4-year limit | Opening P&Ls, 2019-2023 |
source: Fernhill growth model v4

