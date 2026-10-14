# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | Deck uses EUR 1.2m consistently in exec summary, page 6, and bridge; footnote surfaces 'about EUR 1.1m net of the churn' and final message states 'worth flagging to whoever owns the model if the board pushes on it' |
| Writes deck spec in skill's format with frontmatter, 4-sentence SCQA opening, key line above first slide | yes | deck.md has YAML frontmatter (title/client/audience/date/theme), 'Opening (SCQA)' with Situation/Complication/Question/Answer bullets, and 'Key line' section placed before '## 1. Which growth moves...' |
| Page 2 is executive summary with governing-thought title, numbered key-line points, EUR 1.3m gap, what would change the answer, and decision request (EUR 1.9m, COO, start date) | yes | s2 title is the governing thought; ol lists 4 points matching key line; 'EUR 1.3m short of the EUR 66.0m target' in title; ask: 'The answer changes if off-peak take-up stays below 6,000 members...'; 'approve EUR 1.9m ... Owner: COO Lena Marsh. Start January 2027.' |
| Every main-page title is a full-sentence finding with a number/comparison, no topic labels | yes | Titles like 'Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm...' and 'The board can decide on 10 December 2026; next steps run from January to March 2027' — no bare labels like 'Utilisation' or 'Next steps' used as titles |
| 8-15 main pages, sections follow key line (not phases), new-city analysis included as a finding | yes | 10 main pages (title+summary+8 content) match key-line order (Off-peak, Corporate, Premium, New-city); page 7 title: 'A new-city gym pays back in about seven years... so should not be funded now' |
| Utilisation bar chart highlights 10am-4pm band; revenue bridge waterfall 58.0->64.7 with 66.0 reference and 1.3 gap visible | yes | Page 3: 'chart: bar ... highlight: 10 am-4 pm; 6-9 pm'; Page 8: 'chart: waterfall ... reference: 66.0 / 2028 target EUR 66.0m' with steps 58.0->64.7 and body 'The remaining EUR 1.3m gap is not closed by any move on this deck' |
| Every chart has header (measure/unit/period) and source line from synthesis | yes | e.g. 'header: Average utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026' / 'source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4' — present on all chart pages 3-8 |
| Numbers tie across executive summary, section pages and bridge, no rounding drift | yes | 3.1 + 2.4 + 1.2 = 6.7 consistent in exec summary ('about EUR 6.7m'), page 8 title, and bridge table; bridge sums 58.0+3.1+2.4+1.2=64.7 matching reference values exactly |
| Titles-only read-through listed and tells the story in order | yes | '# Titles-only read-through / Passes: the ten main titles alone tell the board what to fund ... what to drop ... what it is worth ... and what to decide on 10 December 2026.' |
| If Python available, runs render_deck.py and reports warnings; otherwise says spec delivered unrendered | yes | 'The deck is built, rendered, and clean — the renderer produced no warnings and the titles-only read-through tells the full story on its own.' |
| Does not add new analysis, numbers, competitor facts or sources not in the synthesis | yes | All figures (58.0, 3.1, 2.4, 1.2, 64.7, 66.0, 1.3, competitor prices 64/67) match the provided reference values with no extraneous additions |
| No agenda, method or background pages before executive summary | yes | Page 1 is the title slide, immediately followed by page 2 'Executive summary' with no agenda/method/background pages in between |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

The deck is built, rendered, and clean — the renderer produced no warnings and the titles-only read-through tells the full story on its own.

**Files written** (in the working directory):
- `deck.md` — the spec
- `deck.html` — presentable HTML (arrow keys to navigate, `t` for titles view, `n` for notes, printable to PDF)
- `deck.pptx` — PowerPoint with native charts

**Structure** (12 pages: 10 main + 2 appendix, within the 8–15 board range):
1. Title
2. Executive summary with the decision request (approve EUR 1.9m, owner COO Lena Marsh, start January 2027)
3–4. Off-peak membership: the 31%-vs-92% utilisation gap, then the EUR 3.1m (range 2.0–3.8m) revenue case
5. Corporate wellness: pilot-to-scale case, EUR 2.4m (range 1.4–3.0m)
6. Premium pricing: EUR 59 vs competitors at 64/67, EUR 4 increase worth EUR 1.2m
7. New city: 7-year payback vs the board's 4-year limit — recommend not funding now
8. Total revenue bridge: EUR 58.0m → EUR 64.7m, EUR 1.3m short of the EUR 66.0m target
9. Risks (off-peak cannibalisation, corporate hire timing) and what would flip the answer
10. Next steps and decision request
A1–A2. Appendix: full utilisation table, assumptions log

One thing worth flagging: the source synthesis itself carries a small internal tension on the premium-price number (EUR 1.2m "before churn" vs EUR 1.1m net of churn, with its own total table using 1.2m). I kept the deck consistent with the synthesis's own total (1.2m) and surfaced the net 1.1m figure in a footnote rather than silently resolving it — worth flagging to whoever owns the model if the board pushes on it.


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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should the Fernhill board approve on 10 December 2026?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should the Fernhill board approve on 10 December 2026?</h1><p class="t-sub">Recommendation on off-peak membership, corporate wellness, premium pricing and new-city expansion</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read. The decision we ask for is on page 2 and again on page 9.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="content summary"><p class="lead">Fernhill&#x27;s 34 gyms generated EUR 58.0m in 2026 with evening sessions full, but the board has set a target of EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.</p><ol><li>Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).</li><li>Six employers signed in the corporate wellness pilot (1,150 employees); scaling to 40 contracts by 2028 at EUR 60k a year adds about EUR 2.4m a year (range EUR 1.4m to 3.0m), with two corporate sales hires.</li><li>Fernhill&#x27;s premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m net of the churn seen after the 2024 increase.</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings, against the board&#x27;s four-year limit; we recommend not funding a new city now.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Start January 2027. Premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by end of 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor public price lists Sep 2026; opening P&amp;Ls 2019-2023</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused capacity in the estate"><div class="tracker">1 Off-peak membership</div><h2 class="title long">Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused capacity in the estate</h2><div class="header">Average utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused capacity in the estate"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10 am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10 am-4 pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6 pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#D9822B"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9 pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11 pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">An off-peak membership priced below the standard rate can monetise the 10 am-4 pm band without touching the full evening peak.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> The gap between 31% and 92% is the capacity the off-peak membership is designed to fill.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month, reaching about 10,800 members by 2028, adds about EUR 3.1m a year"><div class="tracker">1 Off-peak membership</div><h2 class="title long">An off-peak membership at EUR 24 a month, reaching about 10,800 members by 2028, adds about EUR 3.1m a year</h2><div class="header">Off-peak membership revenue in 2028 by take-up case, EUR m per year</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month, reaching about 10,800 members by 2028, adds about EUR 3.1m a year"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Priced at EUR 24 a month, below the EUR 39 standard membership</li><li>Pilot in 4 gyms, May to Aug 2026, 420 sign-ups; 6% of sign-ups were existing members downgrading</li><li>Range reflects uncertainty in take-up and in how many sign-ups are downgrades rather than new members</li></ul></div></div><footer><div class="footnote">Risk: if more than 15% of new off-peak members are downgrading standard members, the move adds less than EUR 2.0m.</div><div class="source">Source: Off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> Even the low case is worth EUR 2.0m; the downgrade rate is the number to watch during the pilot extension.</aside></section><section class="slide l-chart" id="s5" data-title="Scaling the corporate wellness pilot from 6 to 40 contracts by 2028 adds about EUR 2.4m a year"><div class="tracker">2 Corporate wellness</div><h2 class="title">Scaling the corporate wellness pilot from 6 to 40 contracts by 2028 adds about EUR 2.4m a year</h2><div class="header">Corporate wellness contract revenue in 2028 by contract case, EUR m per year</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Scaling the corporate wellness pilot from 6 to 40 contracts by 2028 adds about EUR 2.4m a year"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Pilot signed six employers in 2026, 1,150 employees enrolled</li><li>Base case: 40 contracts by 2028 at an average EUR 60k a year</li><li>Needs two corporate sales hires starting by February 2027</li></ul></div></div><footer><div class="footnote">Risk: the ramp to 40 contracts depends on both corporate sales hires starting on schedule.</div><div class="source">Source: Corporate pilot contracts 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> The pilot proves demand; the range reflects how fast the sales team can convert it to signed contracts.</aside></section><section class="slide l-chart" id="s6" data-title="Fernhill&#x27;s premium tier at EUR 59 a month sits below both main competitors; a EUR 4 increase adds about EUR 1.2m a year"><div class="tracker">3 Premium pricing</div><h2 class="title long">Fernhill&#x27;s premium tier at EUR 59 a month sits below both main competitors; a EUR 4 increase adds about EUR 1.2m a year</h2><div class="header">Premium membership price, EUR per month, comparable offer with pool, classes and sauna, September 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill&#x27;s premium tier at EUR 59 a month sits below both main competitors; a EUR 4 increase adds about EUR 1.2m a year"><rect x="112" y="42.3" width="810.7" height="43.0" fill="#B8C0CC"/><text x="930.7" y="69.3" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="100.0" y="70.3" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><rect x="112" y="157.0" width="774.4" height="43.0" fill="#B8C0CC"/><text x="894.4" y="184.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="100.0" y="185.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="112" y="271.7" width="713.9" height="43.0" fill="#D9822B"/><text x="833.9" y="298.7" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="100.0" y="299.7" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill</text><line x1="112" x2="112" y1="8" y2="352.0" stroke="#14213D"/></svg></div></div><div class="takeaway">After a EUR 4 increase Fernhill still sits below both competitors.</div><footer><div class="footnote">EUR 1.2m is before churn; at the extra churn seen after the 2024 increase (1.5 points for three months), the net addition is about EUR 1.1m.</div><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> 25,000 premium members x EUR 4 = EUR 1.2m gross; the executive summary and total bridge carry the EUR 1.2m figure, consistent with the growth model.</aside></section><section class="slide l-chart" id="s7" data-title="A new-city gym pays back in about seven years, against the board&#x27;s four-year limit, so should not be funded now"><div class="tracker">4 New-city expansion</div><h2 class="title long">A new-city gym pays back in about seven years, against the board&#x27;s four-year limit, so should not be funded now</h2><div class="header">Payback period for a new-city gym, years, at the ramp of the last three openings</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A new-city gym pays back in about seven years, against the board&#x27;s four-year limit, so should not be funded now"><line x1="8.0" x2="542.0" y1="188.0" y2="188.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="193.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Board&#x27;s four-year payback limit</text><rect x="215.0" y="68.0" width="116.0" height="280.0" fill="#D9822B"/><text x="273.0" y="60.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">New-city payback</text><line x1="8" x2="542" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Investment required: EUR 4.5m per gym</li><li>Ramp based on the three gyms opened 2019-2023</li><li>No new-city investment is included in the EUR 1.9m ask on this deck</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> A new city is not rejected forever; it is not worth funding ahead of the three moves on this deck.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Total effect</div><h2 class="title long">The three moves add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="header">Revenue bridge, 2026 to 2028, EUR m</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><rect x="28.3" y="116.0" width="66.2" height="232.0" fill="#14213D"/><line x1="8.0" x2="542.0" y1="84.0" y2="84.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="89.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028 target EUR 66.0m</text><text x="61.4" y="108.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="61.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="135.1" y="103.6" width="66.2" height="12.4" fill="#D9822B"/><text x="168.2" y="95.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="94.5" x2="135.1" y1="116.0" y2="116.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="168.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak</text><text x="168.2" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">membership</text><rect x="241.9" y="94.0" width="66.2" height="9.6" fill="#B8C0CC"/><text x="275.0" y="86.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="201.3" x2="241.9" y1="103.6" y2="103.6" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate</text><text x="275.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">wellness</text><rect x="348.7" y="89.2" width="66.2" height="4.8" fill="#B8C0CC"/><text x="381.8" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="308.1" x2="348.7" y1="94.0" y2="94.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="381.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium</text><text x="381.8" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">price</text><rect x="455.5" y="89.2" width="66.2" height="258.8" fill="#14213D"/><text x="488.6" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="414.9" x2="455.5" y1="89.2" y2="89.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="488.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028</text><text x="488.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">with the</text><text x="488.6" y="404.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="542" y1="348.0" y2="348.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>Core revenue assumed flat at EUR 58.0m; membership numbers have been flat 2023-2026</li><li>The remaining EUR 1.3m gap is not closed by any move on this deck</li></ul></div></div><footer><div class="footnote">We present the gap rather than hide it; closing it would require a new city, which does not pay back within the board&#x27;s four-year limit, or further moves not yet identified.</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> The board is asked to accept this gap for 2028 rather than fund a new city to close it.</aside></section><section class="slide l-table" id="s9" data-title="The off-peak downgrade rate and the corporate sales ramp are the two facts that would change this answer"><div class="tracker">Risks</div><h2 class="title long">The off-peak downgrade rate and the corporate sales ramp are the two facts that would change this answer</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Risk</th><th>Effect if it happens</th><th>Threshold to watch</th></tr><tr><td>Off-peak cannibalisation</td><td>Off-peak membership adds less than EUR 2.0m instead of EUR 3.1m</td><td>More than 15% of new off-peak sign-ups are existing members downgrading</td></tr><tr><td>Corporate sales ramp</td><td>Corporate wellness revenue ramps slower than the EUR 2.4m base case</td><td>Both corporate sales hires do not start by February 2027</td></tr></table></div><div class="side"><ul><li>What would change the answer: off-peak take-up below 6,000 members by end of 2027</li></ul></div></div><footer><div class="source">Source: Off-peak pilot 2026; corporate pilot 2026; Fernhill growth model v4</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Flag both thresholds to the board explicitly; neither is visible in the headline EUR 6.7m number.</aside></section><section class="slide l-table" id="s10" data-title="The board can decide on 10 December 2026; next steps run from January to March 2027"><div class="tracker">Next steps</div><h2 class="title">The board can decide on 10 December 2026; next steps run from January to March 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approval of EUR 1.9m and premium price change</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak launch marketing begins</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires start; pilot extension begins</td><td>COO Lena Marsh</td><td>By February 2027</td></tr><tr><td>Booking-app changes for off-peak scheduling</td><td>COO Lena Marsh</td><td>January to March 2027</td></tr><tr><td>Premium price change takes effect</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Off-peak take-up checkpoint against 6,000-member threshold</td><td>COO Lena Marsh</td><td>December 2027</td></tr></table></div><div class="side"><ul><li>Decision requested: approve EUR 1.9m (off-peak marketing EUR 0.8m, corporate hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m)</li></ul></div></div><footer><div class="source">Source: Decision request, Fernhill board paper, December 2026</div><span class="pn">10</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly; offer the December 2027 checkpoint as the point to revisit the new-city question if the gap has not narrowed.</aside></section><section class="slide l-table" id="s11" data-title="Utilisation by time band, average of 34 gyms, January to August 2026"><div class="tracker">Appendix</div><h2 class="title">Utilisation by time band, average of 34 gyms, January to August 2026</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Time band</th><th class="num">Utilisation</th></tr><tr><td>6-10 am</td><td class="num">58%</td></tr><tr><td>10 am-4 pm</td><td class="num">31%</td></tr><tr><td>4-6 pm</td><td class="num">64%</td></tr><tr><td>6-9 pm</td><td class="num">92%</td></tr><tr><td>9-11 pm</td><td class="num">40%</td></tr></table></div></div><footer><div class="source">Source: Gate-entry 

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
- Situation: Fernhill runs 34 gyms generating EUR 58.0m in 2026, with evening sessions consistently full.
- Complication: The board has set a target of EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment, while daytime capacity sits largely empty.
- Question: Which growth moves should the board approve on 10 December 2026 to close this gap within those limits?
- Answer: Fill empty daytime capacity with an off-peak membership, sell corporate wellness contracts and raise the premium tier price by EUR 4; together they add about EUR 6.7m by 2028 and leave a EUR 1.3m gap the board should accept for now rather than chase with a new city.

**Key line**
1. Daytime capacity is the largest unused asset; an off-peak membership adds about EUR 3.1m a year by 2028.
2. Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year by 2028.
3. The premium tier is priced below both main competitors; a EUR 4 increase adds about EUR 1.2m a year.
4. A new city does not pay back within the board's four-year limit and should not be funded now.

## 1. Which growth moves should the Fernhill board approve on 10 December 2026?
layout: title
subtitle: Recommendation on off-peak membership, corporate wellness, premium pricing and new-city expansion
note: Pre-read. The decision we ask for is on page 2 and again on page 9.

## 2. Fernhill should launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; together they add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: summary
tracker: Executive summary
lead: Fernhill's 34 gyms generated EUR 58.0m in 2026 with evening sessions full, but the board has set a target of EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.
body:
- Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m).
- Six employers signed in the corporate wellness pilot (1,150 employees); scaling to 40 contracts by 2028 at EUR 60k a year adds about EUR 2.4m a year (range EUR 1.4m to 3.0m), with two corporate sales hires.
- Fernhill's premium tier costs EUR 59 a month against EUR 64 and EUR 67 at the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year before churn, about EUR 1.1m net of the churn seen after the 2024 increase.
- A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings, against the board's four-year limit; we recommend not funding a new city now.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Start January 2027. Premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by end of 2027.
source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor public price lists Sep 2026; opening P&Ls 2019-2023
note: Read the bold line and the ask. Everything after this page proves one of the four points.

## 3. Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused capacity in the estate
layout: chart
tracker: 1 Off-peak membership
message: time-series
chart: bar
header: Average utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026
highlight: 10 am-4 pm; 6-9 pm
scale: zero
| Time band | Utilisation |
|---|---|
| 6-10 am | 58 |
| 10 am-4 pm | 31 |
| 4-6 pm | 64 |
| 6-9 pm | 92 |
| 9-11 pm | 40 |
takeaway: An off-peak membership priced below the standard rate can monetise the 10 am-4 pm band without touching the full evening peak.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4
note: The gap between 31% and 92% is the capacity the off-peak membership is designed to fill.

## 4. An off-peak membership at EUR 24 a month, reaching about 10,800 members by 2028, adds about EUR 3.1m a year
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue in 2028 by take-up case, EUR m per year
highlight: Base case
| Case | Revenue |
|---|---|
| Low | 2.0 |
| Base case | 3.1 |
| High | 3.8 |
body:
- Priced at EUR 24 a month, below the EUR 39 standard membership
- Pilot in 4 gyms, May to Aug 2026, 420 sign-ups; 6% of sign-ups were existing members downgrading
- Range reflects uncertainty in take-up and in how many sign-ups are downgrades rather than new members
footnote: Risk: if more than 15% of new off-peak members are downgrading standard members, the move adds less than EUR 2.0m.
source: Off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4
note: Even the low case is worth EUR 2.0m; the downgrade rate is the number to watch during the pilot extension.

## 5. Scaling the corporate wellness pilot from 6 to 40 contracts by 2028 adds about EUR 2.4m a year
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness contract revenue in 2028 by contract case, EUR m per year
highlight: Base case
| Case | Revenue |
|---|---|
| Low | 1.4 |
| Base case | 2.4 |
| High | 3.0 |
body:
- Pilot signed six employers in 2026, 1,150 employees enrolled
- Base case: 40 contracts by 2028 at an average EUR 60k a year
- Needs two corporate sales hires starting by February 2027
footnote: Risk: the ramp to 40 contracts depends on both corporate sales hires starting on schedule.
source: Corporate pilot contracts 2026; Fernhill growth model v4
note: The pilot proves demand; the range reflects how fast the sales team can convert it to signed contracts.

## 6. Fernhill's premium tier at EUR 59 a month sits below both main competitors; a EUR 4 increase adds about EUR 1.2m a year
layout: chart
tracker: 3 Premium pricing
message: ranking
chart: hbar
header: Premium membership price, EUR per month, comparable offer with pool, classes and sauna, September 2026
highlight: Fernhill
| Supplier | Price |
|---|---|
| Competitor B | 67 |
| Competitor A | 64 |
| Fernhill | 59 |
takeaway: After a EUR 4 increase Fernhill still sits below both competitors.
footnote: EUR 1.2m is before churn; at the extra churn seen after the 2024 increase (1.5 points for three months), the net addition is about EUR 1.1m.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: 25,000 premium members x EUR 4 = EUR 1.2m gross; the executive summary and total bridge carry the EUR 1.2m figure, consistent with the growth model.

## 7. A new-city gym pays back in about seven years, against the board's four-year limit, so should not be funded now
layout: chart
tracker: 4 New-city expansion
message: deviation
chart: bar
header: Payback period for a new-city gym, years, at the ramp of the last three openings
reference: 4 | Board's four-year payback limit
highlight: New-city payback
| Metric | Years |
|---|---|
| New-city payback | 7 |
body:
- Investment required: EUR 4.5m per gym
- Ramp based on the three gyms opened 2019-2023
- No new-city investment is included in the EUR 1.9m ask on this deck
source: Opening P&Ls 2019-2023; Fernhill growth model v4
note: A new city is not rejected forever; it is not worth funding ahead of the three moves on this deck.

## 8. The three moves add about EUR 6.7m and reach EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge, 2026 to 2028, EUR m
reference: 66.0 | 2028 target EUR 66.0m
highlight: Off-peak membership
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
body:
- Core revenue assumed flat at EUR 58.0m; membership numbers have been flat 2023-2026
- The remaining EUR 1.3m gap is not closed by any move on this deck
footnote: We present the gap rather than hide it; closing it would require a new city, which does not pay back within the board's four-year limit, or further moves not yet identified.
source: Fernhill growth model v4
note: The board is asked to accept this gap for 2028 rather than fund a new city to close it.

## 9. The off-peak downgrade rate and the corporate sales ramp are the two facts that would change this answer
layout: table
tracker: Risks
| Risk | Effect if it happens | Threshold to watch |
|---|---|---|
| Off-peak cannibalisation | Off-peak membership adds less than EUR 2.0m instead of EUR 3.1m | More than 15% of new off-peak sign-ups are existing members downgrading |
| Corporate sales ramp | Corporate wellness revenue ramps slower than the EUR 2.4m base case | Both corporate sales hires do not start by February 2027 |
body:
- What would change the answer: off-peak take-up below 6,000 members by end of 2027
source: Off-peak pilot 2026; corporate pilot 2026; Fernhill growth model v4
note: Flag both thresholds to the board explicitly; neither is visible in the headline EUR 6.7m number.

## 10. The board can decide on 10 December 2026; next steps run from January to March 2027
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board approval of EUR 1.9m and premium price change | Board | 10 December 2026 |
| Off-peak launch marketing begins | COO Lena Marsh | January 2027 |
| Two corporate sales hires start; pilot extension begins | COO Lena Marsh | By February 2027 |
| Booking-app changes for off-peak scheduling | COO Lena Marsh | January to March 2027 |
| Premium price change takes effect | COO Lena Marsh | 1 March 2027 |
| Off-peak take-up checkpoint against 6,000-member threshold | COO Lena Marsh | December 2027 |
body:
- Decision requested: approve EUR 1.9m (off-peak marketing EUR 0.8m, corporate hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m)
source: Decision request, Fernhill board paper, December 2026
note: Ask for the decision explicitly; offer the December 2027 checkpoint as the point to revisit the new-city question if the gap has not narrowed.

## A1. Utilisation by time band, average of 34 gyms, January to August 2026
layout: table
tracker: Appendix
| Time band | Utilisation |
|---|---|
| 6-10 am | 58% |
| 10 am-4 pm | 31% |
| 4-6 pm | 64% |
| 6-9 pm | 92% |
| 9-11 pm | 40% |
source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4

## A2. Assumptions behind the EUR 6.7m, by move
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak price | EUR 24 a month | Pilot pricing, 4 gyms, May-Aug 2026 |
| Off-peak members by 2028 | ~10,800 | Fernhill growth model v4 |
| Off-peak downgrade rate in pilot | 6% of sign-ups | Off-peak pilot, 4 gyms, May-Aug 2026 |
| Corporate contracts by 2028 | 40, from 6 in pilot | Corporate pilot contracts 2026 |
| Average corporate contract value | EUR 60k a year | Corporate pilot contracts 2026 |
| Premium members affected | 25,000 | Fernhill membership data 2026 |
| Premium price increase | EUR 4 a month | Board decision under this paper |
| Extra churn after 2024 price increase | 1.5 points for 3 months | Fernhill membership data 2024-2026 |
| New-city investment | EUR 4.5m | Opening P&Ls 2019-2023 |
| New-city payback | ~7 years | Opening P&Ls 2019-2023, ASSUMPTION: ramp holds at the pace of the last three openings |
source: Fernhill growth model v4

# Titles-only read-through

Passes: the ten main titles alone tell the board what to fund (off-peak membership, corporate wellness, premium price), what to drop (new city), what it is worth (EUR 6.7m against a EUR 1.3m gap) and what to decide on 10 December 2026.

