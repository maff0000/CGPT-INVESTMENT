# Align Technology (ALGN) and Globus Medical (GMED): QARP deep dive (as of 2026-11-03)

Conventions: VERIFIED means taken from a company release, SEC filing or a dated market-data page, with the URL given. DERIVED means my own arithmetic on verified numbers. INTERPRETATION means analysis or opinion. UNKNOWN means I could not confirm it. Market-data multiples come from stockanalysis.com, read on 2026-11-03 at about 3:30–3:40 PM EST (intraday, not the close). This is research, not a recommendation.

Main sources:
- ALGN Q3'26 release (8-K, dated 2026-10-28): https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm
- GMED Q2'26 release (8-K exhibit 99.1, dated 2026-08-06): https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm
- GMED Q3 scheduling release (GlobeNewswire, 2026-10-12, mirrored on Finviz): https://finviz.com/news/401371/globus-medical-schedules-third-quarter-earnings-release-and-conference-call. The IR page is https://www.investors.globusmedical.com/node/13126 but it returned HTTP 403 to my fetch.
- Multiples: https://stockanalysis.com/stocks/algn/statistics/, https://stockanalysis.com/stocks/gmed/statistics/, and the /financials/ratios/ pages for each.

## Q1. Next earnings release (verified date and time)

### Takeaway
GMED: the claim of 2026-11-05 is CONFIRMED. Results come after the market close on Thursday, November 5, 2026, with the call at 4:30 PM ET. ALGN: Q3 2026 was already reported on 2026-10-28, after the close. ALGN's next report (Q4 2026) is not yet scheduled and is UNKNOWN; based on past timing it probably falls in late January or early February 2027.

### Cited Findings
- GMED, VERIFIED: the company release of 2026-10-12, 4:01 PM, GlobeNewswire, says Globus will report Q3 2026 results "after the market close on Thursday, November 5, 2026" and hold a call "at 4:30 p.m. Eastern Time" — [Finviz mirror of GlobeNewswire release](https://finviz.com/news/401371/globus-medical-schedules-third-quarter-earnings-release-and-conference-call). Original IR page: [investors.globusmedical.com/node/13126](https://www.investors.globusmedical.com/node/13126), which returned 403 when I fetched it. Also reported by [MyChesCo](https://www.mychesco.com/a/news/regional/globus-medical-sets-november-5-earnings-report-and-call/).
- ALGN, VERIFIED: the Q3 2026 release is dated 2026-10-28. A third-party report says it was filed at 4:02 PM ET — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm); [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg). The date had been pre-announced: "Align Technology to announce third quarter 2026 results on October 28, 2026" — [Finviz](https://finviz.com/news/397754/align-technology-to-announce-third-quarter-2026-results-on-october-28-2026).
- Conflict: one aggregator listed ALGN's Q3 date as 2026-10-26. The company's 8-K and pre-announcement both say 10-28, so treat 10-26 as an error — noted in search results; primary [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm).

### Inferences
- GMED reports two days after this note. Every GMED "latest quarter" figure below is Q2 2026 (dated 2026-08-06) and will be out of date after 2026-11-05.

### Gaps
- ALGN Q4 2026 report date: UNKNOWN, not yet announced.
- I could not fetch the GMED release directly from the IR site (403). Verification relies on the verbatim GlobeNewswire text mirrored on Finviz.

## Q2. Latest quarter: results, guidance and stock reaction

### Takeaway
ALGN Q3'26 was a small beat with low growth: revenue +1.9% YoY, aligner volume +6.6%, and price per case down. Margins improved, and non-GAAP EPS of $2.80 was about 1% above consensus. Shares fell after the report. GMED Q2'26 was strong: sales +5.9% (+9% ex-Nevro), adjusted EBITDA margin 35.4%, non-GAAP EPS of $1.34 (+56%), and FY EPS guidance raised. Enabling tech and Nevro were weak.

### Cited Findings: ALGN Q3 2026 (quarter ended 2026-09-30; released 2026-10-28) — all from the [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm) unless noted
- **Revenue**
  - Total revenue was $1,014.8M, up 1.9% YoY and down 3.9% QoQ.
  - Clear Aligner revenue was $839.3M, up 4.2% YoY and down 3.6% QoQ.
  - Imaging Systems and CAD/CAM Services revenue was $175.5M, down 7.6% YoY.
- **Currency:** FX cut revenue by about $5.0M YoY (about 0.5%). Constant-currency growth was therefore about 2.4% (DERIVED). FX reduced diluted EPS by about $0.24 YoY.
- **Volume and price**
  - Clear Aligner shipments were 690,635 cases, up 6.6% YoY and down 0.2% QoQ.
  - Revenue per case was $1,215, versus $1,260 in Q2'26 and $1,245 in Q3'25 (about -2.4% YoY, DERIVED).
- **Margins**
  - GAAP gross margin 68.7%; non-GAAP gross margin 70.4%.
  - GAAP operating margin 16.7%, versus 9.7% in Q3'25.
  - Non-GAAP operating margin 24.4%, versus 23.9% in Q3'25. In constant currency, the non-GAAP operating margin was 25.8% YoY.
- **EPS:** GAAP $1.90 versus $0.78; non-GAAP $2.80 versus $2.61 (+7.3%, DERIVED).
- **Cash flow:** operating cash flow was $526.7M for the nine months. Q3 operating cash flow, capex and FCF were not broken out (UNKNOWN). Cash was $1,144.9M at 9/30/26.
- **Buybacks:** about 627.3K shares repurchased at an average of $164.73, roughly $103M (DERIVED). $630.0M remains on the $1.0B program, and the company expects to repurchase up to $300M in Q4. FY26 buybacks are guided at about $500M.
- **Restructuring:** $17.2M of restructuring and other charges on the income statement, $28.5M in total across the non-GAAP reconciliation. Q4 is guided at $7–9M.
- **Q4'26 guidance**
  - Revenue $1,000–1,020M.
  - Aligner volume up low single digits YoY; aligner ASP down about 1% YoY.
  - Systems & Services revenue $170–180M.
  - GAAP operating margin about 20%; non-GAAP operating margin about 26%.
- **FY26 guidance**
  - Revenue $4,110–4,130M.
  - Aligner volume and revenue up about 5–6%.
  - Systems & Services revenue $715–725M.
  - Non-GAAP operating margin about 23.7%; GAAP operating margin about 16.2%.
  - Capex $125–150M.
- **2027 commentary:** management pointed to further revenue growth and about 100 bp of operating margin expansion, without assuming a consumer recovery — [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg) (secondary source; not confirmed against the transcript).
- **Versus consensus:** EPS $2.80 versus $2.77 estimated; revenue $1.01B versus $1.00B estimated; the fourth straight EPS beat — [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg).
- **Stock reaction:** shares "sold off immediately after the filing." No percentage was given — [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg). Price on 2026-11-03 (intraday) was $151.44, versus a Q3 average buyback price of $164.73 — [stockanalysis](https://stockanalysis.com/stocks/algn/statistics/).
- **Prior quarter:** Q3 guidance ($1.000–1.020B), given at Q2 in late July 2026, was well below the roughly $1.047B consensus, and the stock slid — [Chartmill](https://www.chartmill.com/news/ALGN/Chartmill-52048-Align-Technology-NASDAQALGN-Slides-After-Q3-Guidance-Misses-Estimates-Despite-Inline-Q2-Results).

### Cited Findings: GMED Q2 2026 (quarter ended 2026-06-30; released 2026-08-06; OLDER, with Q3 due 2026-11-05) — from the [SEC 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm) unless noted
- **Sales**
  - Net sales $789.6M, up 5.9% reported and 5.6% in constant currency.
  - Musculoskeletal Solutions $763.5M (about +7.5%, DERIVED from $710.2M); Enabling Technologies $26.1M (about -26%).
  - U.S. $619.1M (+3.0%); International $170.5M (+18.0% reported, +16.2% constant currency).
- **Growth ex-Nevro:** about 9%, with U.S. spine +7% and international spine +14%. Nevro revenue fell 14.3% YoY — [Nasdaq call highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights), as surfaced in search (I could not fetch the full page because it timed out). The 9% ex-Nevro figure appears in the CEO quote in the 8-K.
- **EPS:** GAAP $1.10, down 26.2%. The year-ago quarter included a $110.5M bargain-purchase gain from the Nevro deal. Non-GAAP EPS was $1.34, up 55.8% from $0.86.
- **Margins:** GAAP gross margin 66.8% (prior year 63.3%); adjusted gross margin 69.4% (prior year 67.4%). Adjusted EBITDA was $279.8M, a 35.4% margin versus 28.0% a year earlier.
- **Cash flow:** operating cash flow $209.7M; capex $33.2M; FCF $176.6M for the quarter and $339.3M year to date.
- **Balance sheet:** cash $507.7M, $840.5M including marketable securities. No borrowings appear on the balance sheet.
- **Buybacks:** $136.1M in H1'26. Q2 alone was about 1.6M shares and $136M, with $253.9M of authorization left — [Nasdaq highlights via search](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights). Conflict: the 8-K's H1 figure of $136.1M and the secondary "Q2 $136M" figure may be the same money; treat the Q2-only figure as unconfirmed.
- **FY26 guidance:** revenue reaffirmed at $3.18–3.22B. Non-GAAP EPS raised to $4.95–5.05 from $4.70–4.80. No GAAP EPS guidance.
- **Stock reaction to Q2:** UNKNOWN; not found.
- **Conflict:** one aggregator listed Q2 EPS as $1.12, while the company's non-GAAP figure is $1.34 — noted in search results; primary [8-K](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm).

### Inferences
- ALGN: revenue (+1.9%) is growing much more slowly than volume (+6.6%). Lower price per case (mix, discounts, DSO and lower-priced products) and falling scanner revenue explain the gap. The EPS gain is mostly cost-driven: margin work plus buybacks.
- ALGN FY26 revenue guidance implies roughly 2–2.5% growth on FY25 revenue of about $4.03B. FY25 is DERIVED from stockanalysis ratios and is approximate.
- GMED: the Q2 EPS jump came mostly from margin expansion (adjusted EBITDA +740 bp) rather than revenue. Q3 on 11-05 will test whether the raised EPS guidance holds while enabling tech and Nevro stay weak.

### Gaps
- ALGN Q3 operating cash flow, capex and FCF on their own; exact share-price move after earnings.
- GMED Q3 consensus; GMED Q2 stock reaction.

## Q3. ALGN specifics: teen vs adult, iTero, ASP, competition, restructuring, buybacks. Is the "early recovery" real?

### Takeaway
There are real but narrow early signs. North American orthodontist shipments grew YoY for the first time in six quarters, DSO shipments grew double digits, and utilization rose. But revenue growth is only about 2%, price per case is falling, and scanner revenue is shrinking. The recovery shows up in volume, not in pricing or revenue.

### Cited Findings
- **Demand signals:** North American orthodontist shipments rose YoY for the first time in six quarters, DSO shipments grew double digits, and international growth was "broad-based." No regional revenue breakdown was given — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm); [Becker's Dental](https://www.beckersdental.com/?p=28060).
- **Doctors:** 90,910 Invisalign-trained doctors received shipments (Q3'25: 88,155). Utilization was 7.6 cases per doctor (Q2'26: 7.8; Q3'25: 7.3). Total doctor customers exceed 307K — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm).
- **CFO comment:** demand is still affected by softer discretionary healthcare spending and capital equipment investment — [Becker's](https://www.beckersdental.com/?p=28060); [Quiver Quant](https://www.quiverquant.com/news/Align+Technology+Q3+Revenue+Reaches+%241.015+Billion+as+Net+Income+Rises).
- **Teen vs adult:** the Q3'26 split is UNKNOWN; it was not in the release, and no transcript was retrieved. Older context: Q1 2025 teen volume was 225.8K, +13.3% YoY — [Benzinga](https://www.benzinga.com/general/health-care/25/04/45120927/align-technology-stock-rallies-after-q1-eps-revenues-beat-estimates) (OLD). Q4 2025 commentary cited teen and early-intervention growth (Invisalign First, Palate Expander) — [Barchart](https://www.barchart.com/story/news/39019/algn-q4-deep-dive-dso-expansion-and-new-products-drive-growth-amid-stable-markets) (OLD).
- **iTero:** Imaging/CAD-CAM revenue was down 7.6% YoY. Cumulative iTero units placed exceed 157,000 (up double digits YoY), including leased, rented and certified pre-owned units — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm). Secondary sources blame a shift to lower-priced scanners and flexible leasing — noted in search results; not independently verified. There is a new U.S. pilot of an iTero-scan-based Invisalign Sports Guard — [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg).
- **Pricing:** price per case fell to $1,215 from $1,245 a year earlier. Q4 aligner ASP is guided down about 1% YoY, and FY ASP "slightly down" — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm).
- **Restructuring and margins:** the GAAP operating margin rose to 16.7% from 9.7% as restructuring charges fell. Q4 is guided to a non-GAAP operating margin of about 26%, and 2027 commentary points to about 100 bp more — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm); [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg).
- **Share count:** shares outstanding are down 2.39% YoY — [stockanalysis](https://stockanalysis.com/stocks/algn/statistics/).
- **Analyst moves:** an Evercore ISI downgrade made the headlines (date not confirmed; it appears to be 2026) — [Finviz](https://finviz.com/news/398502/align-technology-shares-fall-after-evercore-isi-downgrades-stock).

### Inferences
- The "early recovery" is real only in volume and in parts of North America. Falling price per case and lower-priced or leased scanners suggest ALGN is defending share against cheaper aligners, DSO bargaining power and scanner competition by giving up price. This fits a competition story better than a clean cyclical recovery.

### Gaps
- Teen/adult split, the competitive share figures (DSO private labels, lower-cost aligners), and Q3 iTero unit numbers were not found. A call transcript is needed.

## Q4. GMED specifics: NuVasive, Nevro, ExcelsiusGPS, share, organic growth, margins and FCF, accounting

### Takeaway
The NuVasive integration looks to be paying off in margins: adjusted EBITDA margin was 35.4% versus 28.0% a year earlier, and FCF has grown from about $104M (FY22) to $756M TTM. Nevro is a drag on revenue but its margin has turned positive. Enabling Technologies (robots) fell 26% in Q2. The large bargain-purchase gain on Nevro is an accounting item worth watching.

### Cited Findings
- **Growth ex-Nevro:** about 9% total; U.S. spine +7%, international spine +14% — [8-K](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm); [Nasdaq highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights).
- **Nevro:** revenue fell 14.3% YoY in Q2'26 and was roughly flat sequentially. About 75% of open Nevro sales roles were filled, and management expects trial volumes to recover by year-end. Nevro's stand-alone adjusted EBITDA margin was reportedly 22.4%, up from -1.4% — [Nasdaq highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights), via search summary and other secondary sources.
- **Accounting:** Q2'25 included a $110.5M bargain-purchase gain on Nevro, which inflated year-ago GAAP EPS — [8-K](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm).
- **Enabling Technologies:** $26.1M, down about 26% YoY. Management tied this to customers shifting to more flexible capital acquisition (placements rather than outright sales) and named enabling tech and Nevro as H2 risks — [8-K](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm); [Nasdaq highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights).
- **NuVasive synergies:** no quantified synergy figure found. The CFO credited synergy realization for part of the margin gain — [Nasdaq highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights).
- **Multi-year history** (DERIVED by the stockanalysis page tool from market cap and ratios; approximate) — [stockanalysis ratios](https://stockanalysis.com/stocks/gmed/financials/ratios/):

  | | FY21 | FY22 | FY23 | FY24 | FY25 |
  |---|---|---|---|---|---|
  | Revenue | ~$958M | ~$1.02B | ~$1.57B | ~$2.52B | ~$2.94B |
  | FCF | ~$219M | ~$104M | ~$165M | ~$405M | ~$589M |

  TTM FCF is $755.6M — [stockanalysis stats](https://stockanalysis.com/stocks/gmed/statistics/).

### Inferences
- Most of the revenue growth since FY22 is acquired: NuVasive closed in 2023 and Nevro in 2025. Organic growth appears to be mid-to-high single digits based on the Q2 ex-Nevro figure.
- A 26% fall in robot sales could be a timing or financing-mix effect (placements rather than sales). It still deserves watching as a leading indicator of the robot-driven implant pull-through thesis.

### Gaps
- Market share versus Medtronic, Stryker spine and ATEC; ExcelsiusGPS unit counts; NuVasive synergy dollars; any accounting concerns beyond the bargain gain. None of these were found in my limited search budget (UNKNOWN).

## Q5. Quality over 3–5 years: ROIC, FCF conversion, organic vs acquired growth, dilution, leverage

### Takeaway
Both are essentially debt-free (about $112M of debt each) and both are shrinking their share counts. ALGN has the higher ROIC (about 16–19%) but flat revenue for about five years. GMED's ROIC dipped after NuVasive and has recovered to about 14%, with fast but mostly acquired growth.

### Cited Findings
- **ALGN** — [stockanalysis ratios](https://stockanalysis.com/stocks/algn/financials/ratios/); [stats](https://stockanalysis.com/stocks/algn/statistics/):
  - ROIC: 30.2% (FY21), 14.9% (FY22), 16.5% (FY23), 16.3% (FY24), 16.2% (FY25), 18.9% (current).
  - Debt/Equity about 0.03–0.04 throughout.
  - Derived revenue: ~$3.95B (FY21), ~$3.74B (FY22), ~$3.87B (FY23), ~$4.00B (FY24), ~$4.03B (FY25).
  - Derived FCF: ~$772M, ~$277M, ~$608M, ~$623M, ~$491M for FY21–FY25; TTM $647.5M.
  - Shares outstanding -2.39% YoY; cash $1.14B versus debt $112M.
- **GMED** — [stockanalysis ratios](https://stockanalysis.com/stocks/gmed/financials/ratios/); [stats](https://stockanalysis.com/stocks/gmed/statistics/):
  - ROIC: 13.5% (FY21), 13.7% (FY22), 7.5% (FY23), 9.6% (FY24), 13.4% (FY25), 13.9% (current).
  - Debt/Equity 0.13 (FY23–24), 0.02 now.
  - Shares outstanding -1.18% YoY; cash $595M versus debt $112M (the stats page shows a different cash figure from the 8-K's $508M cash plus $841M including securities; definitions differ).

### Inferences
- ALGN: high-quality balance sheet and returns, but revenue has been flat for five years. FCF conversion is volatile (TTM FCF is about 16% of revenue). It does not fit "quality compounder" without a growth restart.
- GMED: improving quality. ROIC is back to pre-NuVasive levels and FCF margin is about 24% TTM (DERIVED: $756M divided by about $3.1B of TTM revenue, which is approximate). The NuVasive share issuance in 2023 diluted holders; buybacks now offset part of it.

### Gaps
- Precise FCF conversion (FCF divided by net income) by year, and SEC-verified revenue and FCF history, were not fetched directly from the 10-Ks.

## Q6. Valuation vs history and peers; bear/base/bull

### Takeaway
Both trade at five-year lows on every multiple shown. ALGN: forward P/E 12.7, EV/EBITDA 10.5, P/FCF 17.0. GMED: forward P/E 15.6, EV/EBITDA 9.9, P/FCF 14.2. Peer multiples were not retrieved (UNKNOWN).

### Cited Findings
- **ALGN** at $151.44, 2026-11-03 intraday — [stockanalysis](https://stockanalysis.com/stocks/algn/statistics/):
  - Market cap $10.76B; EV $9.73B.
  - Trailing P/E 22.1; forward P/E 12.7; EV/EBITDA 10.45; P/FCF 17.0.
  - History of P/E / EV/EBITDA / P/FCF — [ratios](https://stockanalysis.com/stocks/algn/financials/ratios/):

  | Year | P/E | EV/EBITDA | P/FCF |
  |---|---|---|---|
  | FY21 | 67.1 | 46.7 | 67.2 |
  | FY22 | 45.6 | 19.8 | 59.5 |
  | FY23 | 47.2 | 24.8 | 34.5 |
  | FY24 | 36.9 | 17.9 | 25.0 |
  | FY25 | 27.3 | 12.1 | 22.8 |

- **GMED** at $79.57, 2026-11-03 intraday — [stockanalysis](https://stockanalysis.com/stocks/gmed/statistics/):
  - Market cap $10.68B; EV $9.95B.
  - Trailing P/E 20.4; forward P/E 15.6; EV/EBITDA 9.87; P/FCF 14.2.
  - History of P/E / EV/EBITDA / P/FCF — [ratios](https://stockanalysis.com/stocks/gmed/financials/ratios/):

  | Year | P/E | EV/EBITDA | P/FCF |
  |---|---|---|---|
  | FY21 | 49.1 | 24.0 | 33.4 |
  | FY22 | 39.0 | 21.3 | 71.0 |
  | FY23 | 59.8 | 17.0 | 44.4 |
  | FY24 | 109.4 | 16.0 | 27.8 |
  | FY25 | 21.7 | 13.0 | 19.9 |

### Inferences
- Forward EPS implied by the forward P/E (DERIVED): ALGN about $11.9 ($151.44 / 12.7); GMED about $5.11 ($79.57 / 15.58), which is close to the FY26 guidance of $4.95–5.05.
- **Illustrative scenarios** (INTERPRETATION, not forecasts; 12–24 month framing):
  - **ALGN**
    - Bear: revenue roughly flat, ASP keeps falling, and the margin target slips. About $10.5 EPS at 11x gives about $115.
    - Base: low-single-digit growth and +100 bp margin as management indicated. About $12 EPS at 14x gives about $168.
    - Bull: volume recovery spreads (teen, DSO, North America) and ASP stabilizes. About $13 EPS at 18x gives about $235.
  - **GMED**
    - Bear: enabling tech and Nevro keep falling, spine slows to low single digits, and margins plateau. About $4.8 EPS at 13x gives about $62.
    - Base: high-single-digit organic spine growth with stable margins. About $5.5 EPS (2027) at 16x gives about $88.
    - Bull: robot pull-through, a Nevro turnaround and further synergies. About $6 EPS at 20x gives about $120.
  - These EPS and multiple inputs are my own assumptions. They are not consensus.

### Gaps
- Peer multiples (Straumann, Envista, Dentsply Sirona for ALGN; Stryker, Zimmer Biomet, Medtronic, ATEC for GMED) were not retrieved: UNKNOWN. The report writer should get these from a dated source before making any "cheaper than peers" claim.

## Q7. Momentum: 1m/3m/6m vs S&P 500

### Takeaway
Only 52-week changes were obtained: ALGN +10.9% and GMED +31.9% as of 2026-11-03. 1m/3m/6m returns and S&P 500 comparisons are UNKNOWN.

### Cited Findings
- 52-week price change and 5-year beta, from the [ALGN](https://stockanalysis.com/stocks/algn/statistics/) and [GMED](https://stockanalysis.com/stocks/gmed/statistics/) stats pages:
  - ALGN: +10.86%; beta 1.74.
  - GMED: +31.86%; beta 0.96.
- ALGN context: one secondary source cited ALGN year-to-date down more than 35%. It is undated and conflicts with the +10.9% 52-week figure, so treat it as unreliable — noted in search results.
- ALGN post-Q3: shares sold off after the 10-28 release — [24/7 Wall St](https://247wallst.com/cards/align-technology-q3-2026-earnings-algn-01m6227grfc5a468kr1q3qjssg). The current price of $151 sits below the Q3 average buyback price of $164.73 (DERIVED, suggesting the stock fell in or after Q3).

### Gaps
- 1m/3m/6m returns and the S&P 500 benchmark: UNKNOWN.

## Q8. Thesis-breakers: what would invalidate QARP

### Takeaway
ALGN's thesis rests on margin expansion plus buybacks on flat revenue. It breaks if price per case and volume both fall, or if the 2027 margin target slips. GMED's thesis rests on organic spine share gains plus integration margins. It breaks if the 11-05 report shows organic deceleration, a guidance cut, or continued declines in enabling tech and Nevro.

### Cited Findings
- **ALGN**
  - Q4 guidance already assumes ASP down about 1% and only low-single-digit volume growth — [8-K](https://www.sec.gov/Archives/edgar/data/0001097149/000109714926000077/algn-q326earningspressrele.htm).
  - Scanner revenue is down 7.6% — same source.
  - Management cites soft discretionary spending — [Becker's](https://www.beckersdental.com/?p=28060).
- **GMED**
  - Management flagged enabling tech and Nevro as H2 downside risks — [Nasdaq highlights](https://www.nasdaq.com/articles/globus-medical-q2-earnings-call-highlights).
  - Revenue guidance was only reaffirmed while EPS guidance was raised — [8-K](https://www.sec.gov/Archives/edgar/data/0001237831/000162828026054353/gmed-q22026ex991.htm).

### Inferences
- **ALGN invalidation signals** (INTERPRETATION):
  - Aligner volume turns negative YoY again, or North American orthodontist shipments fall again.
  - Price per case falls more than about 3% YoY.
  - The FY27 operating margin outlook drops below the FY26 level of about 23.7%.
  - Imaging revenue keeps falling double digits, signalling lost share in scanners, which feed the aligner funnel.
  - Buybacks are cut.
  - Evidence of share loss to DSO private-label or low-cost aligners.
- **GMED invalidation signals** (INTERPRETATION):
  - Q3 (11-05) organic or ex-Nevro growth falls below about 5%.
  - FY26 revenue guidance is cut below $3.18B, or EPS guidance is cut.
  - Enabling tech declines continue for several quarters without placement data.
  - Nevro revenue keeps falling double digits.
  - Adjusted EBITDA margin moves back toward 30%.
  - FCF conversion weakens, for example from inventory or instrument-set build.
  - Any restatement or controls issue tied to acquisition accounting.
  - A large dilutive acquisition.

### Gaps
- Short interest, insider activity and any SEC comment letters were not checked.
