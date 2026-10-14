# db-02-unfinished-argument on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (3/7 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the argument is not ready for a deck and names D1 (no single answer) as the main reason | NO | The assistant built and delivered the full deck ('Done — deck.html and deck.pptx are in your working directory, 20 slides, no render warnings') rather than stating the argument wasn't ready; it only flagged the CEO/CFO disagreement as one of several caveats within the finished deck, not as a reason  |
| Finds at least four of D2–D6, including D3 and D4 with both numbers (2.6 vs 1.9) | yes | Slide 7/deck.md: 'Option A's EUR 7.5m spa programme claims EUR 2.6m EBITDA, but only EUR 1.9m is independently estimated' (D4); slide 6: '18% RevPAR uplift management cites has no source' (D3); A3 flags most of the 7 findings as having no figure/not used (D5); slide 2 'ask' flags no owner/date given |
| Lists what the synthesis owner must supply before the deck can be built (governing thought, 3-5 key-line statements with numbers, sources, decision request) | NO | The assistant never paused to request these inputs; it proceeded straight to building the full deck with its own assumptions (e.g., 'ASSUMPTION: management to name an owner and a return date') instead of stopping to ask the user/synthesis owner to supply them first. |
| Shows fixed titles for at least two sections as full-sentence findings, marked conditional or numbers-only | yes | Slide 8 title: 'Option B would sell Westbay and Dunmore (EUR 0.4m EBITDA on EUR 11m revenue) to fund Option A'; Appendix A4 shows 3.6% vs 13.8% margin comparison, matching the example almost exactly. |
| Pushes back on 20 slides (board main deck 8-15 pages; rest to appendix or removed) | NO | The assistant delivered exactly the requested '20 slides' total ('12 main slides ... plus 8 appendix slides') without ever telling the user that 20 slides is too many for a board main deck; it silently restructured rather than pushing back. |
| Does not produce a full 20-slide deck spec with the topic headings as slide titles | yes | Slide titles are full-sentence action titles (e.g., 'Leisure guests already generate 64% of room nights...'), with the user's original topic headings relegated to the 'tracker' line, not used as titles. |
| Does not choose between Option A/B as settled, or invent the missing Point House figure, a source for 18%, or a decision owner | NO | Slide 12/deck.md next-steps table assigns 'CEO/CFO alignment on sequencing ... / CEO and CFO / Not named in brief' as a stated owner without an ASSUMPTION caveat, and other rows invent ASSUMPTION owners ('hotel ops', 'strategy/finance team', 'CEO, with CFO sign-off') for a decision the brief left ow |

## Transcript

## Turn 1

**User:** Make this into a 20-slide board deck for Quayside, I need it by tomorrow morning. Keep my section headings. (Attached in the working directory: db-02-input.md.)

**Done — `deck.html` and `deck.pptx` are in your working directory, 20 slides, no render warnings.**

What you're getting: 12 main slides (title → executive summary → your 7 sections → next steps) plus 8 appendix slides, with your headings preserved as the section tracker under each full-sentence title.

What's genuinely ready to present: the guest-demand case (slides 4–5), the group financials (slide 3), and the Westbay/Dunmore weak-hotel evidence (slide 8/A4) are all sourced and tie out cleanly.

What's flagged, not resolved, because the source material doesn't support a clean answer:
- Point House's spa EBITDA (slide 7/A2) — shown as an unconfirmed EUR 0.7m residual
- The 18% competitor RevPAR uplift (slide 6) — no source in the brief
- The CEO/CFO sequencing disagreement (slide 11) — presented as the board's decision, not pre-resolved
- Appendix A1 is a standalone punch-list of all 7 open items if you want to hand that to whoever owns closing the gaps before the next cycle

If you'd rather I pick a side on sequencing or fill in the Point House number with a placeholder estimate so the deck reads as fully resolved, say so and I'll redo those two slides — but as built, nothing in it is invented.


## Files in work dir after run

- db-02-input.md
- deck.html
- deck.md
- deck.pptx

## File written by the run: deck.html

<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quayside Hotels — spa opportunity and the funding decision</title><style>
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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="How should Quayside respond to rising guest demand for spas?"><div class="t-client">Quayside Hotels (fictional)</div><h1 class="t-title">How should Quayside respond to rising guest demand for spas?</h1><p class="t-sub">Resolving the funding sequence between spa expansion and portfolio divestment</p><p class="t-meta">Board of directors, pre-read | October 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the board. The decision request is on page 2 and again on page 11.</aside></section><section class="slide l-summary" id="s2" data-title="Guest demand for spas is sound and sourced, but two of management&#x27;s numbers are not yet confirmed and the CEO and CFO have not agreed on sequencing"><div class="tracker">Executive summary</div><h2 class="title long">Guest demand for spas is sound and sourced, but two of management&#x27;s numbers are not yet confirmed and the CEO and CFO have not agreed on sequencing</h2><div class="content summary"><p class="lead">Quayside is a EUR 71m, 9-hotel business whose leisure guests already drive most room nights and are asking for spas by name. The opportunity is well evidenced; the funding path is not yet agreed.</p><ol><li>Leisure guests are 64% of room nights, and spa was the top-requested facility in a 212-guest survey (Quayside booking system, 2025; guest survey, Aug 2026).</li><li>Three competitors have added spas since 2023, and management cites an 18% RevPAR uplift for spa competitors — no source has been provided for either figure; flagged for confirmation before it is used to size the decision.</li><li>Option A (spas in 4 hotels, EUR 7.5m capex) is costed at EUR 2.6m EBITDA a year, but only EUR 1.9m of that is independently estimated (Harbour View, Cliffside, Saltings); the remaining EUR 0.7m (Point House) is an unconfirmed residual.</li><li>Option B (sell Westbay and Dunmore, EUR 0.4m combined EBITDA on EUR 11m revenue) would self-fund Option A — but the CEO recommends Option A outright and the CFO recommends Option B first, with no agreed sequencing in the brief.</li></ol><div class="ask"><strong>Decision requested today:</strong> resolve whether Option A proceeds now, after Option B, or not before the Point House estimate and the RevPAR source are confirmed. No owner or date was given in the brief for this decision — ASSUMPTION: management to name an owner and a return date before the next board cycle.</div></div><footer><div class="source">Source: Quayside booking system 2025; guest survey n=212, Aug 2026; Quayside P&amp;L 2025</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> This page is the whole argument. Everything after it proves one of the four points above or flags what is still missing.</aside></section><section class="slide l-table" id="s3" data-title="Quayside is a EUR 71m, 9-hotel business running a 13.8% EBITDA margin heading into the spa decision"><div class="tracker">Market overview</div><h2 class="title long">Quayside is a EUR 71m, 9-hotel business running a 13.8% EBITDA margin heading into the spa decision</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Metric</th><th class="num">2025</th></tr><tr><td>Hotels</td><td class="num">9</td></tr><tr><td>Rooms</td><td class="num">1,240</td></tr><tr><td>Revenue</td><td class="num">EUR 71m</td></tr><tr><td>EBITDA</td><td class="num">EUR 9.8m</td></tr><tr><td>EBITDA margin</td><td class="num">13.8%</td></tr></table></div><div class="side"><ul><li>The brief describes a coastal hotel market shifting toward experience-led, shorter breaks — directional, no market-size figure given.</li></ul></div></div><footer><div class="footnote">No source was provided for the market-shift statement; shown as context only, not as a sized driver of the decision.</div><div class="source">Source: Quayside P&amp;L 2025</div><span class="pn">3</span></footer></section><section class="slide l-chart" id="s4" data-title="Leisure guests already generate 64% of room nights, nearly double the 36% from business travel"><div class="tracker">Customer analysis</div><h2 class="title">Leisure guests already generate 64% of room nights, nearly double the 36% from business travel</h2><div class="header">Room nights by guest type, % of total, 2025</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Leisure guests already generate 64% of room nights, nearly double the 36% from business travel"><rect x="48.0" y="153.0" width="654.1" height="90.0" fill="#D9822B" stroke="#FFFFFF" stroke-width="1"/><text x="375.0" y="203.0" font-size="14" text-anchor="middle" fill="#FFFFFF" font-weight="normal">64</text><text x="375.0" y="141.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Leisure</text><rect x="702.1" y="153.0" width="367.9" height="90.0" fill="#D0D5DE" stroke="#FFFFFF" stroke-width="1"/><text x="886.0" y="203.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal">36</text><text x="886.0" y="141.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Business</text><text x="36.0" y="203.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2025</text><text x="1078.0" y="203.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">100</text></svg></div></div><div class="takeaway">A leisure-majority base is the guest group most likely to value and pay for a spa.</div><footer><div class="source">Source: Quayside booking system, 2025</div><span class="pn">4</span></footer></section><section class="slide l-text" id="s5" data-title="Spa was the single most-requested facility in Quayside&#x27;s own guest survey"><div class="tracker">Customer analysis</div><h2 class="title">Spa was the single most-requested facility in Quayside&#x27;s own guest survey</h2><div class="content text"><ul><li>In a 212-guest survey, &quot;spa&quot; was the facility guests asked for most — the clearest direct signal of demand in the brief.</li><li>The brief also states &quot;spa guests spend more,&quot; but gives no figure and no source for it. That claim is flagged, not used in any number in this deck.</li></ul></div><footer><div class="footnote">Guest survey, n=212, August 2026. No numeric breakdown of how spa ranked against other facilities was provided beyond &quot;most requested.&quot;</div><div class="source">Source: Quayside guest survey, n=212, August 2026</div><span class="pn">5</span></footer></section><section class="slide l-text" id="s6" data-title="Three competitors have added spas since 2023; the 18% RevPAR uplift management cites has no source behind it yet"><div class="tracker">Competitive landscape</div><h2 class="title long">Three competitors have added spas since 2023; the 18% RevPAR uplift management cites has no source behind it yet</h2><div class="content text"><ul><li>The brief states three competitors have added spas since 2023 and that spa competitors see an 18% RevPAR uplift — unlike every other section in the brief, neither figure carries a citation.</li><li>These two numbers are the main external justification for the spa programme&#x27;s return; using them to size a EUR 7.5m investment without a source is a gap, not a detail.</li></ul></div><footer><div class="footnote">ASSUMPTION / UNSOURCED — flagged for confirmation (which competitors, what RevPAR base, what period) before the board treats the 18% figure as evidence.</div><div class="source">Source: Not provided in the brief — flagged, no source available</div><span class="pn">6</span></footer></section><section class="slide l-table" id="s7" data-title="Option A&#x27;s EUR 7.5m spa programme claims EUR 2.6m EBITDA, but only EUR 1.9m is independently estimated"><div class="tracker">Options</div><h2 class="title long">Option A&#x27;s EUR 7.5m spa programme claims EUR 2.6m EBITDA, but only EUR 1.9m is independently estimated</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Hotel</th><th class="num">Spa EBITDA, EUR m/year</th></tr><tr><td>Harbour View</td><td class="num">0.8</td></tr><tr><td>Cliffside</td><td class="num">0.6</td></tr><tr><td>Saltings</td><td class="num">0.5</td></tr><tr><td>Point House (unconfirmed residual)</td><td class="num">0.7</td></tr><tr><td>Stated programme total</td><td class="num">2.6</td></tr></table></div><div class="side"><ul><li>Harbour View, Cliffside and Saltings sum to EUR 1.9m. The brief gives a programme total of EUR 2.6m but says Point House is &quot;not yet estimated&quot; — the EUR 0.7m shown for Point House is the arithmetic gap, not an estimate anyone has made.</li></ul></div></div><footer><div class="footnote">Point House figure is a back-calculated residual, not a sourced estimate. Needs an independent number before this total is used for capital approval.</div><div class="source">Source: Quayside business case, Option A, 2026</div><span class="pn">7</span></footer></section><section class="slide l-table" id="s8" data-title="Option B would sell Westbay and Dunmore (EUR 0.4m EBITDA on EUR 11m revenue) to fund Option A"><div class="tracker">Options</div><h2 class="title">Option B would sell Westbay and Dunmore (EUR 0.4m EBITDA on EUR 11m revenue) to fund Option A</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Hotel</th><th class="num">2025 revenue, EUR m</th><th class="num">2025 EBITDA, EUR m</th></tr><tr><td>Westbay + Dunmore (combined)</td><td class="num">11</td><td class="num">0.4</td></tr></table></div><div class="side"><ul><li>Combined EBITDA margin is about 3.6%, against the 13.8% group average — the clearest evidence in the brief that these two hotels are the weakest in the portfolio.</li><li>The brief states selling them &quot;would fund&quot; the EUR 7.5m Option A capex; it does not state the expected sale proceeds, so this is a funding rationale, not a costed transaction.</li></ul></div></div><footer><div class="footnote">No sale price or valuation was given in the brief for Westbay or Dunmore.</div><div class="source">Source: Quayside P&amp;L, 2025</div><span class="pn">8</span></footer></section><section class="slide l-text" id="s9" data-title="Option C, refurbishing rooms across all hotels, has no cost estimate and is not ready for a decision"><div class="tracker">Options</div><h2 class="title long">Option C, refurbishing rooms across all hotels, has no cost estimate and is not ready for a decision</h2><div class="content text"><ul><li>The brief names Option C but provides no capex, no EBITDA effect and no scope — it cannot be compared to Options A or B on the numbers available.</li><li>Shown here as parked, not rejected: dated rooms appear separately in the risk register (page 10) as a reason it may need costing later.</li></ul></div><footer><div class="footnote">Not costed in the brief — no figures to show.</div><div class="source">Source: Quayside business case, Option C, 2026</div><span class="pn">9</span></footer></section><section class="slide l-table" id="s10" data-title="Beyond the spa decision, three risks need board attention on their own track, not as inputs to the Option A/B choice"><div class="tracker">Key findings</div><h2 class="title long">Beyond the spa decision, three risks need board attention on their own track, not as inputs to the Option A/B choice</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Risk</th><th>What the brief says</th><th>Source given</th></tr><tr><td>Room condition</td><td>Rooms are dated in some hotels</td><td>Not provided</td></tr><tr><td>Business travel</td><td>Has not fully recovered</td><td>Not provided</td></tr><tr><td>Staff turnover</td><td>32%</td><td>Not provided</td></tr></table></div><div class="side"><ul><li>These three items appear in the brief&#x27;s &quot;key findings&quot; alongside the spa-decision drivers, but none of them carries a number that connects to Option A or B&#x27;s EBITDA case — they are shown here as context and risk, kept separate so they do not quietly inflate the spa argument.</li></ul></div></div><footer><div class="footnote">None of the three carries a cited source in the brief; shown as management-reported context, not decision-grade evidence.</div><div class="source">Source: Quayside key findings, 2026 (as reported, uncited)</div><span class="pn">10</span></footer></section><section class="slide l-table" id="s11" data-title="The CEO backs Option A, the CFO backs Option B first — sequencing is unresolved and is the board&#x27;s decision"><div class="tracker">Recommendation</div><h2 class="title long">The CEO backs Option A, the CFO backs Option B first — sequencing is unresolved and is the board&#x27;s decision</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Position</th><th>Recommends</th><th>Stated rationale</th></tr><tr><td>CEO</td><td>Option A now</td><td>Capture guest demand and competitor gap directly</td></tr><tr><td>CFO</td><td>Option B first</td><td>Use Westbay/Dunmore sale to self-fund Option A</td></tr></table></div><div class="side"><ul><li>The brief states both positions and adds &quot;both are attractive&quot; with no resolution — that is not a recommendation, it is an open disagreement being brought to the board.</li><li>The two options are not mutually exclusive on the facts given: the CFO&#x27;s own rationale is that Option B funds Option A. The open question is sequencing and timing, not a choice between permanently doing one or the other.</li></ul></div></div><footer><div class="footnote">This deck does not select between the CEO&#x27;s and CFO&#x27;s positions. That choice belongs to the board or to an aligned management team, not to this analysis.</div><div class="source">Source: Quayside strategy brief, 2026</div><span class="pn">11</span></footer></section><section class="slide l-table" id="s12" data-title="Before the next board cycle, three gaps need to close and one decision needs an owner and a date"><div class="tracker">Next steps</div><h2 class="title long">Before the next board cycle, three gaps need to close and one decision needs an owner and a date</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Independent Point House spa EBITDA estimate</td><td>Not named in brief — ASSUMPTION: hotel ops to confirm</td><td>Not named in brief</td></tr><tr><td>Source and verify the 18% competitor RevPAR uplift</td><td>Not named in brief — ASSUMPTION: strategy/finance team</td><td>Not named in brief</td></tr><tr><td>CEO/CFO alignment on sequencing (Option A vs. B-then-A)</td><td>CEO and CFO</td><td>Not named in brief</td></tr><tr><td>Return to board with a single, costed recommendation</td><td>Not named in brief — ASSUMPTION: CEO, with CFO sign-off</td><td>Not named in brief</td></tr></table></div><div class="side"><ul><li>The brief&#x27;s own next step is &quot;align management, then decide&quot; with no owner or date attached — the owners and dates above are flagged assumptions for management to confirm, not facts from the brief.</li></ul></div></div><footer><div class="footnote">Every &quot;not named in brief&quot; cell is a genuine gap in the source document, not an omission in this deck.</div><div class="source">Source: Quayside strategy brief, 2026</div><span class="pn">12</span></footer></section><section class="slide l-table" id="s13" data-title="Open items before this goes to the board as final"><div class="tracker">Appendix</div><h2 class="title">Open items before this goes to the board as final</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>#</th><th>Open item</th><th>Why it matters</th></tr><tr><td>1</td><td>Point House spa EBITDA is a EUR 0.7m residual, not an estimate</td><td>Changes the real case for Option A if the true number is lower</td></tr><tr><td>2</td><td>18% competitor RevPAR uplift has no source</td><td>Main external justification for the spa investment</td></tr><tr><td>3</td><td>&quot;Spa guests spend more&quot; has no figure</td><td>Currently rhetorical, not quantified</td></tr><tr><td>4</td><td>No sale price given for Westbay/Dunmore</td><td>Option B&#x27;s funding capacity is unproven without it</td></tr><tr><td>5</td><td>Option C has no cost estimate</td><td>Cannot be compared to A or B</td></tr><tr><td>6</td><td>CEO and CFO have not agreed sequencing</td><td>This is the actual board decision, not a side note</td></tr><tr><td>7</td><td>No owner/date on &quot;align management, then decide&quot;</td><td>Without this, the decision has no forcing mechanism</td></tr></table></div></div><footer><div class="source">Source: Compiled from Quayside strategy brief, 2026</div><span class="pn">A1</span></footer></section><section class="slide l-text" id="s14" data-title="How the Option A EBITDA figures were derived"><div class="tracker">Appendix</div><h2 class="title">How the Option A EBITDA figures were derived</h2><div class="content text"><ul><li>Harbour View (0.8), Cliffside (0.6) and Saltings (0.5) are stated directly in the brief&#x27;s Option A table.</li><li>Point House (0.7) is this deck&#x27;s arithmetic residual: EUR 2.6m stated programme total minus the EUR 1.9m sum of the three named hotels. It is not a hotel-level estimate and should not be treated as one until confirmed.</li></ul></div><footer><div class="footnote">Recommend hotel ops produce an independent Point House estimate before this number is used in any capital request.</div><div class="source">Source: Quayside business case, Option A, 2026</div><span class="pn">A2</span></footer></section><section class="slide l-table" id="s15" data-title="Full key-findings register from the brief"><div class="tracker">Appendix</div><h2 class="title">Full key-findings register from the brief</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>#</th><th>Finding</th><th>Used in the main argument?</th></tr><tr><td>1</td><td>The market is changing</td><td>No — directional, no figure</td></tr><tr><td>2</td><td>Guests want spas</td><td>Yes — page 4/5</td></tr><tr><td>3</td><td>Competitors are investing</td><td>Yes, flagged unsourced — page 6</td></tr><tr><td>4</td><td>Two hotels are weak</td><td>Yes — page 8</td></tr><tr><td>5</td><td>Rooms are dated in some hotels</td><td>No — risk register, page 10</td></tr><tr><td>6</td><td>Business travel has not fully recovered</td><td>No — risk register, page 10</td></tr><tr><td>7</td><td>Staff turnover is high (32%)</td><td>No — risk register, page 10</td></tr></table></div></div><footer><div class="source">Source: Quayside key findings, 2026</div><span class="pn">A3</span></footer></section><section class="slide l-chart" id="s16" data-title="Westbay and Dunmore against the group average"><div class="tracker">Appendix</div><h2 class="title">Westbay and Dunmore against the group average</h2><div class="header">2025 EBITDA margin, %, by hotel grouping</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Westbay and Dunmore against the group average"><rect x="231.5" y="240.8" width="116.0" height="67.2" fill="#D9822B"/><text x="289.5" y="232.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.6</text><text x="291.5" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Westbay + Dunmore</text><rect x="798.5" y="50.4" width="116.0" height="257.6" fill="#B8C0CC"/><text x="856.5" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">13.8</text><text x="858.5" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Group average (9 hotels)</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">Westbay and Dunmore run at roughly a quarter of the group&#x27;s average margin, the clearest basis in the brief for calling them the two weakest hotels.</div><footer><div class="source">Source: Quayside P&amp;L, 2025</div><span class="pn">A4</span></footer></section><section class="slide l-table" id="s17" data-title="Quayside&#x27;s named hotels in this brief"><div class="tracker">Appendix</div><h2 class="title">Quayside&#x27;s named hotels in this brief</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Hotel</th><th>Role in this decision</th></tr><tr><td>Harbour View</td><td>Option A — spa capex, EUR 0.8m EBITDA/year</td></tr><tr><td>Cliffside</td><td>Option A — spa capex, EUR 0.6m EBITDA/year</td></tr><tr><td>Saltings</td><td>Option A — spa capex, EUR 0.5m EBITDA/year</td></tr><tr><td>Point House</td><td>Option A — spa capex, EBITDA not yet estimated</td></tr><tr><td>Westbay</td><td>Option B — proposed sale</td></tr><tr><td>Dunmore</td><td>Option B — proposed sale</td></tr></table></div><div class="side"><ul><li>The brief names 6 of Quayside&#x27;s 9 hotels. The remaining 3 are not referenced in this decision and are not covered in this deck.</li></ul></div></div><footer><div class="source">Source: Quayside strategy brief, 2026</div><span class="pn">A5</span></footer></section><section class="slide l-text" id="s18" data-title="A simple framework for the sequencing decision"><div class="tracker">Appendix</div><h2 class="title">A simple framework for the sequencing decision</h2><div class="content text"><ul><li>Three questions the board can use to resolve the CEO/CFO disagreement, without this deck choosing an answer: (1) Can Option A be funded without selling Westbay and Dunmore, and at what cost of capital? (2) What sale proceeds would Westbay and Dunmore realistically achieve, and do they cover EUR 7.5m? (3) What is lost by waiting for a sale to close before starting the spa programme, given competitors already have an 18-month-plus head start?</li></ul></div><footer><div class="footnote">This framework structures the decision; it does not supply the answer, which depends on financing terms and sale proceeds not given in the brief.</div><div class="source">Source: Team analysis based on Quayside strategy brief, 2026</div><span class="pn">A6</span></footer></section><section class="slide l-table" id="s19" data-title="Sources used in this deck"><div class="tracker">Appendix</div><h2 class="title">Sources used in this deck</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Source</th><th>Used for</th></tr><tr><td>Quayside booking system, 2025</td><td>Leisure/business room-night split</td></tr><tr><td>Quayside guest survey, n=212, August 2026</td><td>Spa as top-requested facility</td></tr><tr><td>Quayside P&amp;L, 2025</td><td>Group revenue/EBITDA; Westbay/Dunmore financials</td></tr><tr><td>Quayside business case, Option A, 2026</td><td>Spa capex and per-hotel EBITDA</td></tr><tr><td>Quayside business case, Option C, 2026</td><td>Confirmation that Option C is uncosted</td></tr><tr><td>Quayside strategy brief, 2026</td><td>CEO/CFO positions; key findings; next steps</td></tr><tr><td>Not provided</td><td>Competitor count and RevPAR uplift; room-condition, business-travel and staff-turnover figures</td></tr></table></div></div><footer><div class="source">Source: Compiled from the source brief, October 2026</div><span class="pn">A7</span></footer></section><section class="slide l-table" id="s20" data-title="Glossary"><div class="tracker">Appendix</div><h2 class="title">Glossary</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Term</th><th>Meaning</th></tr><tr><td>RevPAR</td><td>Revenue per available room</td></tr><tr><td>EBITDA margin</td><td>EBITDA as a % of revenue</td></tr><tr><td>Room night</td><td>One room occupied for one night; the standard unit for guest-mix analysis</td></tr><tr><td>Residual (this deck)</td><td>A number derived by subtraction, not independently measured</td></tr></table></div></div><footer><div class="source">Source: Standard hotel-industry usage</div><span class="pn">A8</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>How should Quayside respond to rising guest demand for spas? <span style='color:#8A93A3'>(1)</span></li><li>Guest demand for spas is sound and sourced, but two of management&#x27;s numbers are not yet confirmed and the CEO and CFO have not agreed on sequencing <span style='color:#8A93A3'>(2)</span></li><li>Quayside is a EUR 71m, 9-hotel business running a 13.8% EBITDA margin heading into the spa decision <span style='color:#8A93A3'>(3)</span></li><li>Leisure guests already generate 64% of room nights, nearly double the 36% from business travel <span style='color:#8A93A3'>(4)</span></li><li>Spa was the single most-requested facility in Quayside&#x27;s own guest survey <span style='color:#8A93A3'>(5)</span></li><li>Three competitors have added spas since 2023; the 18% RevPAR uplift management cites has no source behind it yet <span style='color:#8A93A3'>(6)</span></li><li>Option A&#x27;s EUR 7.5m spa programme claims EUR 2.6m EBITDA, but only EUR 1.9m is independently estimated <span style='color:#8A93A3'>(7)</span></li><li>Option B would sell Westbay and Dunmor

## File written by the run: deck.md

---
title: Quayside Hotels — spa opportunity and the funding decision
client: Quayside Hotels (fictional)
audience: Board of directors, pre-read
date: October 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
---

# Deck: How should Quayside respond to rising guest demand for spas?

*Fictional company. All figures invented for evaluation.*

**Opening (SCQA)**
- Situation: Quayside runs 9 hotels, 1,240 rooms, EUR 71m revenue and EUR 9.8m EBITDA in 2025; leisure guests already drive most room nights and are asking for spas by name.
- Complication: Three competitors have added spas since 2023, but Quayside's leadership has not agreed how to fund a response — the CEO backs a EUR 7.5m spa expansion, the CFO wants to sell two weak hotels first.
- Question: Should the board approve the spa expansion now, require the divestment first, or send the business case back for the missing numbers?
- Answer: The guest-demand case is sound and sourced, but two numbers behind it are not yet confirmed, and management has not aligned on sequencing — the board's decision today is on process, not on a finished recommendation.

**Key line**
1. Leisure guests are 64% of room nights and spa is the top-requested facility in a 212-guest survey (Quayside booking system, 2025; guest survey, Aug 2026).
2. The spa programme is costed at EUR 7.5m for EUR 2.6m EBITDA a year, but EUR 0.7m of that (Point House) is an unconfirmed residual, not an independent estimate.
3. Selling Westbay and Dunmore (EUR 0.4m combined EBITDA on EUR 11m revenue, Quayside P&L 2025) would self-fund the spa programme, per the CFO's own rationale.
4. The CEO recommends the spa expansion outright; the CFO recommends the sale first; the brief records no agreed sequencing.
5. Decision requested: resolve sequencing between the two options, conditional on confirming the Point House estimate and the source for the competitor RevPAR claim.

## 1. How should Quayside respond to rising guest demand for spas?
layout: title
subtitle: Resolving the funding sequence between spa expansion and portfolio divestment
note: Pre-read for the board. The decision request is on page 2 and again on page 11.

## 2. Guest demand for spas is sound and sourced, but two of management's numbers are not yet confirmed and the CEO and CFO have not agreed on sequencing
layout: summary
tracker: Executive summary
lead: Quayside is a EUR 71m, 9-hotel business whose leisure guests already drive most room nights and are asking for spas by name. The opportunity is well evidenced; the funding path is not yet agreed.
body:
- Leisure guests are 64% of room nights, and spa was the top-requested facility in a 212-guest survey (Quayside booking system, 2025; guest survey, Aug 2026).
- Three competitors have added spas since 2023, and management cites an 18% RevPAR uplift for spa competitors — no source has been provided for either figure; flagged for confirmation before it is used to size the decision.
- Option A (spas in 4 hotels, EUR 7.5m capex) is costed at EUR 2.6m EBITDA a year, but only EUR 1.9m of that is independently estimated (Harbour View, Cliffside, Saltings); the remaining EUR 0.7m (Point House) is an unconfirmed residual.
- Option B (sell Westbay and Dunmore, EUR 0.4m combined EBITDA on EUR 11m revenue) would self-fund Option A — but the CEO recommends Option A outright and the CFO recommends Option B first, with no agreed sequencing in the brief.
ask: **Decision requested today:** resolve whether Option A proceeds now, after Option B, or not before the Point House estimate and the RevPAR source are confirmed. No owner or date was given in the brief for this decision — ASSUMPTION: management to name an owner and a return date before the next board cycle.
source: Quayside booking system 2025; guest survey n=212, Aug 2026; Quayside P&L 2025
note: This page is the whole argument. Everything after it proves one of the four points above or flags what is still missing.

## 3. Quayside is a EUR 71m, 9-hotel business running a 13.8% EBITDA margin heading into the spa decision
layout: table
tracker: Market overview
| Metric | 2025 |
|---|---|
| Hotels | 9 |
| Rooms | 1,240 |
| Revenue | EUR 71m |
| EBITDA | EUR 9.8m |
| EBITDA margin | 13.8% |
body:
- The brief describes a coastal hotel market shifting toward experience-led, shorter breaks — directional, no market-size figure given.
footnote: No source was provided for the market-shift statement; shown as context only, not as a sized driver of the decision.
source: Quayside P&L 2025

## 4. Leisure guests already generate 64% of room nights, nearly double the 36% from business travel
layout: chart
tracker: Customer analysis
message: part-to-whole
chart: stacked-hbar
header: Room nights by guest type, % of total, 2025
highlight: 2025/Leisure
| Segment | Leisure | Business |
|---|---|---|
| 2025 | 64 | 36 |
takeaway: A leisure-majority base is the guest group most likely to value and pay for a spa.
source: Quayside booking system, 2025

## 5. Spa was the single most-requested facility in Quayside's own guest survey
layout: text
tracker: Customer analysis
body:
- In a 212-guest survey, "spa" was the facility guests asked for most — the clearest direct signal of demand in the brief.
- The brief also states "spa guests spend more," but gives no figure and no source for it. That claim is flagged, not used in any number in this deck.
footnote: Guest survey, n=212, August 2026. No numeric breakdown of how spa ranked against other facilities was provided beyond "most requested."
source: Quayside guest survey, n=212, August 2026

## 6. Three competitors have added spas since 2023; the 18% RevPAR uplift management cites has no source behind it yet
layout: text
tracker: Competitive landscape
body:
- The brief states three competitors have added spas since 2023 and that spa competitors see an 18% RevPAR uplift — unlike every other section in the brief, neither figure carries a citation.
- These two numbers are the main external justification for the spa programme's return; using them to size a EUR 7.5m investment without a source is a gap, not a detail.
footnote: ASSUMPTION / UNSOURCED — flagged for confirmation (which competitors, what RevPAR base, what period) before the board treats the 18% figure as evidence.
source: Not provided in the brief — flagged, no source available

## 7. Option A's EUR 7.5m spa programme claims EUR 2.6m EBITDA, but only EUR 1.9m is independently estimated
layout: table
tracker: Options
| Hotel | Spa EBITDA, EUR m/year |
|---|---|
| Harbour View | 0.8 |
| Cliffside | 0.6 |
| Saltings | 0.5 |
| Point House (unconfirmed residual) | 0.7 |
| Stated programme total | 2.6 |
body:
- Harbour View, Cliffside and Saltings sum to EUR 1.9m. The brief gives a programme total of EUR 2.6m but says Point House is "not yet estimated" — the EUR 0.7m shown for Point House is the arithmetic gap, not an estimate anyone has made.
footnote: Point House figure is a back-calculated residual, not a sourced estimate. Needs an independent number before this total is used for capital approval.
source: Quayside business case, Option A, 2026

## 8. Option B would sell Westbay and Dunmore (EUR 0.4m EBITDA on EUR 11m revenue) to fund Option A
layout: table
tracker: Options
| Hotel | 2025 revenue, EUR m | 2025 EBITDA, EUR m |
|---|---|---|
| Westbay + Dunmore (combined) | 11 | 0.4 |
body:
- Combined EBITDA margin is about 3.6%, against the 13.8% group average — the clearest evidence in the brief that these two hotels are the weakest in the portfolio.
- The brief states selling them "would fund" the EUR 7.5m Option A capex; it does not state the expected sale proceeds, so this is a funding rationale, not a costed transaction.
footnote: No sale price or valuation was given in the brief for Westbay or Dunmore.
source: Quayside P&L, 2025

## 9. Option C, refurbishing rooms across all hotels, has no cost estimate and is not ready for a decision
layout: text
tracker: Options
body:
- The brief names Option C but provides no capex, no EBITDA effect and no scope — it cannot be compared to Options A or B on the numbers available.
- Shown here as parked, not rejected: dated rooms appear separately in the risk register (page 10) as a reason it may need costing later.
footnote: Not costed in the brief — no figures to show.
source: Quayside business case, Option C, 2026

## 10. Beyond the spa decision, three risks need board attention on their own track, not as inputs to the Option A/B choice
layout: table
tracker: Key findings
| Risk | What the brief says | Source given |
|---|---|---|
| Room condition | Rooms are dated in some hotels | Not provided |
| Business travel | Has not fully recovered | Not provided |
| Staff turnover | 32% | Not provided |
body:
- These three items appear in the brief's "key findings" alongside the spa-decision drivers, but none of them carries a number that connects to Option A or B's EBITDA case — they are shown here as context and risk, kept separate so they do not quietly inflate the spa argument.
footnote: None of the three carries a cited source in the brief; shown as management-reported context, not decision-grade evidence.
source: Quayside key findings, 2026 (as reported, uncited)

## 11. The CEO backs Option A, the CFO backs Option B first — sequencing is unresolved and is the board's decision
layout: table
tracker: Recommendation
| Position | Recommends | Stated rationale |
|---|---|---|
| CEO | Option A now | Capture guest demand and competitor gap directly |
| CFO | Option B first | Use Westbay/Dunmore sale to self-fund Option A |
body:
- The brief states both positions and adds "both are attractive" with no resolution — that is not a recommendation, it is an open disagreement being brought to the board.
- The two options are not mutually exclusive on the facts given: the CFO's own rationale is that Option B funds Option A. The open question is sequencing and timing, not a choice between permanently doing one or the other.
ask: **Decision requested:** direct management to return with either (a) a sequenced plan — divest first, fund the spa programme from proceeds — or (b) a funded case for doing Option A now by another route, in both cases with the Point House estimate and the RevPAR source confirmed.
footnote: This deck does not select between the CEO's and CFO's positions. That choice belongs to the board or to an aligned management team, not to this analysis.
source: Quayside strategy brief, 2026

## 12. Before the next board cycle, three gaps need to close and one decision needs an owner and a date
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Independent Point House spa EBITDA estimate | Not named in brief — ASSUMPTION: hotel ops to confirm | Not named in brief |
| Source and verify the 18% competitor RevPAR uplift | Not named in brief — ASSUMPTION: strategy/finance team | Not named in brief |
| CEO/CFO alignment on sequencing (Option A vs. B-then-A) | CEO and CFO | Not named in brief |
| Return to board with a single, costed recommendation | Not named in brief — ASSUMPTION: CEO, with CFO sign-off | Not named in brief |
body:
- The brief's own next step is "align management, then decide" with no owner or date attached — the owners and dates above are flagged assumptions for management to confirm, not facts from the brief.
footnote: Every "not named in brief" cell is a genuine gap in the source document, not an omission in this deck.
source: Quayside strategy brief, 2026

## A1. Open items before this goes to the board as final
layout: table
tracker: Appendix
| # | Open item | Why it matters |
|---|---|---|
| 1 | Point House spa EBITDA is a EUR 0.7m residual, not an estimate | Changes the real case for Option A if the true number is lower |
| 2 | 18% competitor RevPAR uplift has no source | Main external justification for the spa investment |
| 3 | "Spa guests spend more" has no figure | Currently rhetorical, not quantified |
| 4 | No sale price given for Westbay/Dunmore | Option B's funding capacity is unproven without it |
| 5 | Option C has no cost estimate | Cannot be compared to A or B |
| 6 | CEO and CFO have not agreed sequencing | This is the actual board decision, not a side note |
| 7 | No owner/date on "align management, then decide" | Without this, the decision has no forcing mechanism |
source: Compiled from Quayside strategy brief, 2026

## A2. How the Option A EBITDA figures were derived
layout: text
tracker: Appendix
body:
- Harbour View (0.8), Cliffside (0.6) and Saltings (0.5) are stated directly in the brief's Option A table.
- Point House (0.7) is this deck's arithmetic residual: EUR 2.6m stated programme total minus the EUR 1.9m sum of the three named hotels. It is not a hotel-level estimate and should not be treated as one until confirmed.
footnote: Recommend hotel ops produce an independent Point House estimate before this number is used in any capital request.
source: Quayside business case, Option A, 2026

## A3. Full key-findings register from the brief
layout: table
tracker: Appendix
| # | Finding | Used in the main argument? |
|---|---|---|
| 1 | The market is changing | No — directional, no figure |
| 2 | Guests want spas | Yes — page 4/5 |
| 3 | Competitors are investing | Yes, flagged unsourced — page 6 |
| 4 | Two hotels are weak | Yes — page 8 |
| 5 | Rooms are dated in some hotels | No — risk register, page 10 |
| 6 | Business travel has not fully recovered | No — risk register, page 10 |
| 7 | Staff turnover is high (32%) | No — risk register, page 10 |
source: Quayside key findings, 2026

## A4. Westbay and Dunmore against the group average
layout: chart
tracker: Appendix
message: ranking
chart: bar
header: 2025 EBITDA margin, %, by hotel grouping
highlight: Westbay + Dunmore
| Grouping | EBITDA margin |
|---|---|
| Westbay + Dunmore | 3.6 |
| Group average (9 hotels) | 13.8 |
takeaway: Westbay and Dunmore run at roughly a quarter of the group's average margin, the clearest basis in the brief for calling them the two weakest hotels.
source: Quayside P&L, 2025

## A5. Quayside's named hotels in this brief
layout: table
tracker: Appendix
| Hotel | Role in this decision |
|---|---|
| Harbour View | Option A — spa capex, EUR 0.8m EBITDA/year |
| Cliffside | Option A — spa capex, EUR 0.6m EBITDA/year |
| Saltings | Option A — spa capex, EUR 0.5m EBITDA/year |
| Point House | Option A — spa capex, EBITDA not yet estimated |
| Westbay | Option B — proposed sale |
| Dunmore | Option B — proposed sale |
body:
- The brief names 6 of Quayside's 9 hotels. The remaining 3 are not referenced in this decision and are not covered in this deck.
source: Quayside strategy brief, 2026

## A6. A simple framework for the sequencing decision
layout: text
tracker: Appendix
body:
- Three questions the board can use to resolve the CEO/CFO disagreement, without this deck choosing an answer: (1) Can Option A be funded without selling Westbay and Dunmore, and at what cost of capital? (2) What sale proceeds would Westbay and Dunmore realistically achieve, and do they cover EUR 7.5m? (3) What is lost by waiting for a sale to close before starting the spa programme, given competitors already have an 18-month-plus head start?
footnote: This framework structures the decision; it does not supply the answer, which depends on financing terms and sale proceeds not given in the brief.
source: Team analysis based on Quayside strategy brief, 2026

## A7. Sources used in this deck
layout: table
tracker: Appendix
| Source | Used for |
|---|---|
| Quayside booking system, 2025 | Leisure/business room-night split |
| Quayside guest survey, n=212, August 2026 | Spa as top-requested facility |
| Quayside P&L, 2025 | Group revenue/EBITDA; Westbay/Dunmore financials |
| Quayside business case, Option A, 2026 | Spa capex and per-hotel EBITDA |
| Quayside business case, Option C, 2026 | Confirmation that Option C is uncosted |
| Quayside strategy brief, 2026 | CEO/CFO positions; key findings; next steps |
| Not provided | Competitor count and RevPAR uplift; room-condition, business-travel and staff-turnover figures |
source: Compiled from the source brief, October 2026

## A8. Glossary
layout: table
tracker: Appendix
| Term | Meaning |
|---|---|
| RevPAR | Revenue per available room |
| EBITDA margin | EBITDA as a % of revenue |
| Room night | One room occupied for one night; the standard unit for guest-mix analysis |
| Residual (this deck) | A number derived by subtraction, not independently measured |
source: Standard hotel-industry usage

