# Evidence notes: Cloudflare (NET) and Zscaler (ZS) — 2026-11-03

Author: Claude (independent research agent). Retrieved 2026-11-03 (Europe/London evening; US session closed). Market data: stockanalysis.com pages showing "at close, Nov 3, 2026, 4:00 PM EST". Labels: [VERIFIED] company release / SEC filing / dated market-data page; [REPORTED] secondary; [PROVISIONAL] Claude arithmetic or interpretation; [UNKNOWN] not found. Research evidence only; no buy/sell language.

## Q1. Next earnings dates and gate position

### Takeaway
NET Q3 2026 is company-confirmed for Thursday 2026-11-05 after the US close; ZS Q1 FY2027 has no company notice found, and the two vendor estimates conflict (Nov 24 vs Nov 27).

### Cited Findings
- NET: Q3 2026 results after US market close Thursday 2026-11-05; call 2:00 p.m. PT / 5:00 p.m. ET; notice published 2026-10-13 [VERIFIED] — [Cloudflare IR](https://www.cloudflare.net/news/news-details/2026/Cloudflare-Announces-Date-of-Third-Quarter-2026-Financial-Results/default.aspx)
- NET last results: Q2 2026 released 2026-08-06 [VERIFIED] — [Cloudflare IR Q2 release](https://www.cloudflare.net/news/news-details/2026/Cloudflare-Announces-Second-Quarter-2026-Financial-Results/default.aspx)
- ZS last results: Q4/FY2026 (to 2026-07-31) released 2026-09-03 [VERIFIED] — [SEC 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm)
- ZS next results: stockanalysis shows Tuesday 2026-11-24 after close (vendor estimate) [REPORTED] — [stockanalysis ZS statistics](https://stockanalysis.com/stocks/zs/statistics/); MFN calendar shows Q1 FY27 report 2026-11-27 22:05 Stockholm marked as estimated time [REPORTED, search snippet] — [MFN](https://mfn.se/all/a/zscaler-inc/zscaler-hosts-2026-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance-545a473b)
- Precedent: ZS announced Q1 FY2026 date in early November 2025 for a 2025-11-25 after-close release [REPORTED] — [Zscaler IR notice](https://ir.zscaler.com/news-releases/news-release-details/zscaler-host-first-quarter-fiscal-year-2026-earnings-conference)
- ir.zscaler.com returned HTTP 403 to automated fetch on 2026-11-03; the IR events page could not be checked directly.

### Inferences
- NET gate [PROVISIONAL count, EARNINGS-GATE-v1.1]: pre-window sessions Oct 27, 28, 29, 30, Nov 2, 3, 4 plus Nov 5 release day → PRE-EARNINGS BLOCK on Nov 3. After-close release: sessions 1–2 are Nov 6 and Nov 9; earliest re-review Nov 10, conditional.
- ZS gate [PROVISIONAL]: last results 61 days old (>30), next date not company-confirmed → UNKNOWN under v1.2. If Nov 24 after close is confirmed, block window is Nov 13, 16, 17, 18, 19, 20, 23 plus Nov 24. Nov 26 is Thanksgiving (closed) and Nov 27 an early-close session; conservatively Nov 27 is not a complete regular session, so sessions 1–2 would be Nov 25 and Nov 30, earliest re-review Dec 1.

### Gaps
- ZS company date notice [UNKNOWN]; expected in early November by precedent.

## Q2. NET latest quarter (Q2 2026, to 2026-06-30)

### Takeaway
Growth accelerated to +36% with NRR 120%, but GAAP operating margin was −29.6% after a $150.7M restructuring charge, FCF margin only 8%, and SBC ~23% of quarterly revenue.

### Cited Findings
- Revenue $696.1M vs $512.3M (+36%); current RPO +35% YoY [VERIFIED] — [Q2 release](https://www.cloudflare.net/news/news-details/2026/Cloudflare-Announces-Second-Quarter-2026-Financial-Results/default.aspx)
- Gross margin GAAP 71.8% (74.9%); non-GAAP 73.1% (76.3%) [VERIFIED] — same
- GAAP operating loss $205.7M (−29.6%; −13.1% prior), incl. $150.7M restructuring and other; non-GAAP operating income $96.1M (13.8% vs 14.1%) [VERIFIED] — same
- GAAP net loss $170.0M, EPS −$0.48; non-GAAP EPS $0.29 vs $0.21 [VERIFIED] — same
- Operating cash flow $117.6M; FCF $56.4M (8%) vs $33.3M (6%) [VERIFIED] — same
- Cash and AFS securities $4,162.8M at 2026-06-30 [VERIFIED] — same
- Guidance: Q3 revenue $736–737M, non-GAAP op income $129–130M, EPS $0.34; FY2026 revenue $2,864–2,870M, non-GAAP op income $443–445M, EPS $1.25–1.26 on ~374M shares [VERIFIED] — same
- Release omits customer counts, NRR and AI revenue [VERIFIED by absence] — same
- NRR 120% (+2 pts QoQ, +6 pts YoY); 4,698 customers >$100k (+27%), 73% of revenue; >80,000 paying customers added, +74% YoY paying customers; non-GAAP gross margin up sequentially for first time in 8 quarters [REPORTED, call summaries] — [Zacks](https://www.zacks.com/stock/news/2971165/cloudflare-q2-earnings-beat-estimates-on-large-customer-growth); [Quartr](https://quartr.com/events/cloudflare-inc-net-q2-2026_3s9oMh1m)
- Workforce cut >1,100 (~20%) announced with Q1 results in May 2026, framed as "agentic AI-first operating model" [REPORTED] — [TIKR](https://www.tikr.com/blog/cloudflare-1100-person-layoff-spooked-the-market-the-numbers-tell-a-different-story)
- 10-Q: total RPO $2,732.0M, 64% within 12 months; SBC Q2 $163.3M vs $125.5M (equity statement), 6M $274.1M vs $217.9M; weighted shares 354.33M vs 347.49M; shares outstanding 356.08M (Class A 322.62M + B 33.46M at 2026-07-21); convertible notes carrying value $1,293.3M current and $1,977.0M noncurrent; 6M capex $115.2M + capitalised software $20.2M [VERIFIED] — [SEC 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000054/cloud-20260630.htm)
- 2030 notes: $2.0B 0%, issued June 2025, conversion ~$247.67, capped call cap ~$469.73; 2026 notes conversion ~$191.34, combination settlement (cash principal, shares for excess) used for conversions [VERIFIED, search-snippet of 10-Qs] — [10-Q Q2](https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000054/cloud-20260630.htm); [10-Q Q1](https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000038/cloud-20260331.htm)
- New $2.175B 0% convertible notes due 2031 priced 2026-08-11 (option +$325M); conversion ~$496.94 (60% premium to $310.59); capped call cap ~$854.12; ~$225.8M capped-call cost; remainder general corporate purposes incl. possible debt repayment and acquisitions; settle 2026-08-13 [VERIFIED] — [SEC 8-K ex99.2](https://www.sec.gov/Archives/edgar/data/0001477333/000095010326012340/dp251721_ex9902.htm)
- Geography Q2: US 51%, EMEA 27%, APAC 14%, other 8% [VERIFIED] — 10-Q

### Inferences
- Q2 SBC $163.3M / revenue $696.1M ≈ 23.5% [PROVISIONAL].
- FY2026 guide midpoint $2,867M ≈ +32.2% on FY2025 $2,168M [PROVISIONAL].
- The 2031 issue priced days before the 2026 notes' expected maturity, functionally a refinancing; 2026 notes ($191.34 conversion) were in the money, so excess value settled in shares adds dilution [PROVISIONAL; settlement amounts UNKNOWN until Q3 10-Q].
- 2030 notes are in the money at $273.62; capped call offsets dilution up to $469.73 [PROVISIONAL].

### Gaps
- AI/Workers/AI Gateway/pay-per-crawl revenue: not disclosed; company does not break out product revenue [REPORTED] — [Kavout](https://www.kavout.com/market-lens/cloudflare-s-net-ai-acceleration-drives-premium-but-growth-segmentation-remains-opaque)
- Long-term target: a Spanish article says the CFO raised the long-term growth target from 40% to 50% at the 2026 Investor Day [REPORTED, single source] — [Ecosistema Startup](https://ecosistemastartup.com/cloudflare-eleva-meta-de-crecimiento-al-50-con-ia-agentica/); search summaries suggest Q1 call language referred to "Rule of 50" not 50% growth, and Investor Day was 2026-06-09 — [Quartr Investor Day](https://quartr.com/events/cloudflare-inc-net-investor-day-2026_3s9oMBao). Unresolved conflict.
- Total RPO YoY growth, final 2026 note settlement, restructuring savings [UNKNOWN].

## Q3. NET multi-year quality and valuation

### Takeaway
Revenue compounding ~30%+ for five years with FCF margin rising to ~13.6% TTM, but SBC (~20% of revenue) exceeds FCF every year, GAAP operating margin has never been positive, and multiples are at or near five-year highs and above every named peer except CRWD.

### Cited Findings
- Revenue FY21–FY25: $656M, $975M, $1,297M, $1,670M, $2,168M; TTM $2,512M; growth 52%, 49%, 33%, 29%, 30%, TTM 33.5%; gross margin 77.6%→74.5%, TTM 72.6%; operating margin −19.4%, −20.2%, −14.3%, −8.3%, −9.1%, TTM −7.8% [VERIFIED] — [stockanalysis income](https://stockanalysis.com/stocks/net/financials/)
- FCF FY21–FY25: −$28M, −$20M, $134M, $181M, $281M; TTM $342M; SBC $90M, $203M, $274M, $338M, $451M; TTM $508M; buybacks $4–60M/yr [VERIFIED] — [stockanalysis cash flow](https://stockanalysis.com/stocks/net/financials/cash-flow-statement/)
- Nov 3 close $273.62; market cap $97.43B; EV $96.80B; shares 356.08M (+2.02% YoY); fwd P/E 185.1; EV/sales 38.5; fwd P/S 29.9; EV/FCF 283; FCF margin 13.6%; ROIC −2.5%; debt $3.53B, cash $4.16B (June 30 basis); 52w +8.0%; 50-day MA $320.03; 200-day MA $248.95; RSI 35.9 [VERIFIED] — [stockanalysis NET statistics](https://stockanalysis.com/stocks/net/statistics/)
- History: EV/sales FY21–FY25 63.6, 15.2, 21.4, 21.9, 31.6; fwd P/E FY22–FY25 286, 162, 138, 176; EV/FCF FY23–FY25 208, 203, 244 [VERIFIED] — [stockanalysis ratios](https://stockanalysis.com/stocks/net/financials/ratios/)
- Peers (Nov 3 close): FSLY EV/S 4.97, fwd P/E 39.4, EV/FCF 67, 52w +154%, reports Nov 4 AMC; AKAM 3.94, 13.2, 17.8, +14%, reports Nov 5 AMC; DDOG 18.9, 83.2, 63.5, +36%, reports Nov 4 BMO; ZS 10.6, 45.9, 41.8, −32%; CRWD 45.8, 173, 153, +80% [VERIFIED] — [FSLY](https://stockanalysis.com/stocks/fsly/statistics/), [AKAM](https://stockanalysis.com/stocks/akam/statistics/), [DDOG](https://stockanalysis.com/stocks/ddog/statistics/), [CRWD](https://stockanalysis.com/stocks/crwd/statistics/)
- Price history: Oct 2 $349.07; Oct 6 $355.01; Oct 9 $360.93 (high in table); Aug 25 $277.58; Nov 3 $273.62. SPY Oct 2 $769.64, Aug 25 $765.91, Nov 3 $754.35 [VERIFIED] — [NET history](https://stockanalysis.com/stocks/net/history/), [SPY history](https://stockanalysis.com/etf/spy/history/)
- Mid-October ~15% weekly drop with no company news; record high Oct 6 [REPORTED] — [TIKR](https://www.tikr.com/blog/cloudflare-just-dropped-15-in-a-week-is-it-time-to-sell-or-load-up)

### Inferences [PROVISIONAL]
- SBC/revenue: FY21 13.7%, FY22 20.8%, FY23 21.1%, FY24 20.3%, FY25 20.8%, TTM 20.2%.
- FCF minus SBC: FY23 −$140M, FY24 −$158M, FY25 −$170M, TTM −$166M (TTM −6.6% of revenue).
- 1m (Oct 2→Nov 3) −21.6% vs SPY −2.0%; −24.2% from Oct 9 high; Aug 25→Nov 3 −1.4% vs SPY −1.5%.
- P/E on FY26 non-GAAP EPS guide midpoint $1.255 ≈ 218x; EV/FY26 revenue guide ≈ 33.8x.

### Gaps
- 3m/6m returns (dated closes before Aug 25 not retrieved) [UNKNOWN]. ROIC by year: stockanalysis shows ROCE only (−6.1% to −5.1%).

## Q4. ZS latest year (FY2026, to 2026-07-31) and FY2027 guidance

### Takeaway
Headline +25% growth is ~20% organic (Red Canary), FY2027 guides to ~17%, FCF margin fell to 23% on capex, and FCF after SBC is roughly zero to slightly negative.

### Cited Findings
- Q4: revenue $898.2M (+25%); ARR $3,771M (+25%), ex-Red Canary ($141M) $3,630M (+20%); net new ARR $246M (+24%; +17% ex-Red Canary); GAAP op loss $15.5M (−2%); non-GAAP op income $218.4M (24%); GAAP EPS −$0.02; non-GAAP EPS $1.19; SBC incl. payroll taxes $215.2M; FCF $60.8M (7%) vs $171.9M, capex + capitalised software $218.5M; deferred revenue $2,926M (+19%) [VERIFIED] — [SEC 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm)
- FY26: revenue $3,352.5M (+25%; ex-Red Canary $3,209M, +20%); GAAP op loss $133.3M (−4%); non-GAAP op income $767.1M (23%); GAAP EPS −$0.39; non-GAAP EPS $4.21 ($3.28); SBC incl. payroll taxes $841.6M ($685.5M); OCF $1,129.7M (34%); FCF $779.1M (23%) vs $726.7M (27%); GAAP weighted shares 160.2M vs 154.4M; non-GAAP diluted 167.1M vs 163.4M; cash + ST investments ~$3,474M; convertible notes $1,696.4M [VERIFIED] — same
- FY27 guide: ARR $4.396–4.426B (+16.6–17.4%); revenue $3.908–3.938B (+16.6–17.5%); non-GAAP op income $924–932M; EPS $4.86–4.90 on ~173M shares; FCF margin ~23.0–23.5%. Q1: revenue $935–939M (~19%), EPS $1.15–1.16 [VERIFIED] — same; reaffirmed 2026-10-06 at Investor Day, "$10 billion ARR target" with no timeline, no AI ARR, no buyback [VERIFIED via MFN reprint of company release] — [MFN](https://mfn.se/all/a/zscaler-inc/zscaler-hosts-2026-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance-545a473b)
- Security for AI bookings +50% QoQ, pipeline +75% QoQ; Zero Trust Everywhere customers >950 from 700; ~3% staff restructuring; capex elevated by memory/processor prices; Agentic SecOps on Red Canary tech [REPORTED] — [TIKR](https://www.tikr.com/pt/blog/zscalers-q4-earnings-beat-on-every-line-the-fy27-guide-didnt-follow-through); [Nasdaq call highlights](https://www.nasdaq.com/articles/zscaler-q4-earnings-call-highlights) (page timed out; snippet)
- Agentic AI product launches June 2026 [REPORTED, journal source] — [Zscaler press](https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai)
- Stock fell ~6.9% after results [REPORTED] — [Goldesel](https://goldesel.de/aktien/news/zscaler-ubertrifft-quartalsziele-und-legt-starken-ausblick-vor-aktie-fallt-69-prozent); closes Sep 3 $177.80, Sep 4 $169.80 [VERIFIED] — [ZS history](https://stockanalysis.com/stocks/zs/history/)

### Inferences [PROVISIONAL]
- FCF after SBC FY26: company FCF $779.1M − SBC $841.6M = −$62.5M (−1.9% of revenue); FY25 +$41.2M. On stockanalysis definitions ($852.4M − $821.9M) = +$30.4M. Either way ~0.
- SBC/revenue: FY22 37.5%, FY23 27.5%, FY24 24.3%, FY25 24.7%, FY26 24.5% (stockanalysis SBC) or 25.1% (company incl. payroll taxes).
- Net dilution ~3.5–3.8%/yr with no buyback; FY27 share guide 173M vs 167.1M (+3.5%).
- FY27 FCF midpoint ≈ 23.25% × $3.923B ≈ $912M.

### Gaps
- Dollar-based net retention (not in release; historically disclosed in 10-K) [UNKNOWN]; RPO, billings, $1M+ customer counts [UNKNOWN]; Security-for-AI ARR in dollars [UNKNOWN — not disclosed].

## Q5. ZS valuation, momentum and competition

### Takeaway
After a ~39% rebound from the Sep 8 low, ZS trades ~10.6x EV/sales and ~42x EV/FCF (stockanalysis), cheaper than PANW/CRWD/DDOG and below its own FY22–FY25 range, but growth is decelerating and FCF after SBC is ~0.

### Cited Findings
- Nov 3 close $225.09; market cap $36.70B; EV $35.10B; shares 163.05M (+3.77%); fwd P/E 45.9; EV/S 10.6; fwd P/S 9.5; EV/FCF 41.8; P/FCF 43.7; FCF TTM $852.35M (stockanalysis def.); net cash $1.61B; 52w −32.0%; 50-day MA $206.02; 200-day MA $166.99; RSI 50.0; short interest 3.65% [VERIFIED] — [stockanalysis ZS statistics](https://stockanalysis.com/stocks/zs/statistics/)
- History: EV/S FY22–FY26 19.6, 14.0, 12.1, 16.0, 6.8; fwd P/E 167, 80, 58, 83, 34; EV/FCF 84, 62, 41, 53, 27 [VERIFIED] — [stockanalysis ratios](https://stockanalysis.com/stocks/zs/financials/ratios/)
- History financials FY22–FY26 revenue $1,091M→$3,353M; operating margin −30.0%, −14.1%, −5.6%, −4.6%, −3.5%; cash acquisitions FY26 $918M [VERIFIED] — [income](https://stockanalysis.com/stocks/zs/financials/), [cash flow](https://stockanalysis.com/stocks/zs/financials/cash-flow-statement/)
- PANW Nov 3: EV/S 25.3, fwd P/E 83.8, EV/FCF 70.6, shares +7.76%, 52w +59%, reports Nov 18 AMC [VERIFIED] — [PANW](https://stockanalysis.com/stocks/panw/statistics/); CRWD reports Dec 1 AMC — [CRWD](https://stockanalysis.com/stocks/crwd/statistics/)
- Price path: Sep 8 low $161.94; Oct 2 $196.60; Oct 6 $212.25; Oct 26 high $260.45; Nov 3 $225.09 [VERIFIED] — [ZS history](https://stockanalysis.com/stocks/zs/history/)
- Rebound drivers: Investor Day reaffirmation, analyst target raises (Cantor $275, Baird $285), DA Davidson Neutral initiation $215 with +7.8% day Oct 21 [REPORTED, low-reliability aggregators] — [Quiver](https://www.quiverquant.com/news/Zscaler+gains+as+investor-day+outlook+and+analyst+target+hikes+support+shares); [Trefis](https://www.trefis.com/stock/zs/articles2/619928/why-is-zscaler-stock-going-up/2026-10-22)
- Competition: no reliable 2026 SASE share data found; vendor blogs cite Netskope data-protection strength, PANW Prisma Access ecosystem bundling, Cloudflare One as low-cost challenger with free tier [REPORTED, low quality] — [dope.security](https://dope.security/post/top-zscaler-competitors-2026); [Nasdaq/Zacks](https://www.nasdaq.com/articles/will-traction-sase-and-zero-trust-keep-driving-cloudflare)

### Inferences [PROVISIONAL]
- 1m (Oct 2→Nov 3) +14.5% vs SPY −2.0%; +39.0% from Sep 8 low; −13.6% from Oct 26 high.
- On company FCF $779.1M, P/FCF = 36.70/0.779 ≈ 47.1x and EV/FCF ≈ 45.1x; on FY27 FCF midpoint ~$912M, EV/FCF ≈ 38.5x; P/E on FY27 EPS midpoint $4.88 ≈ 46.1x; EV/FY27 revenue ≈ 8.9x.
- On FCF minus SBC, the EV/FCF multiple is undefined (≈0 or negative).

### Gaps
- 3m/6m returns [UNKNOWN]; independent market-share data (Gartner/IDC) [UNKNOWN]; NRR [UNKNOWN].
