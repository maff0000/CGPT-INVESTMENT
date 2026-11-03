# Evidence notes: Visa (V) and Booking Holdings (BKNG), observed 2026-11-03

Researcher: Claude (independent research agent). Retrieval window: 2026-11-03, roughly 16:20–17:00 US Eastern (after the regular session close). Market-data snapshots are stockanalysis.com pages stamped "at close, Nov 3, 2026, 4:00 PM EST" unless noted; return series are Yahoo Finance daily closes (split-adjusted). Labels: [VERIFIED] primary filing / company release / dated market-data page; [REPORTED] secondary; [PROVISIONAL] Claude arithmetic or interpretation; [UNKNOWN] not found.

## BKNG data check: is $151.28 / 13.6x a data error, or did Booking split?

### Takeaway
Not a data error. Booking Holdings effected a **25-for-1 forward stock split on April 2, 2026**, announced February 18, 2026. The ~$150s post-split price equals ~$3,800–3,900 pre-split. The journal's $151.28 intraday and 13.6x forward P/E are consistent with the 2026-11-03 close of $155.67 and 13.99x [VERIFIED].

### Cited Findings
- 8-K Item 8.01: "On February 18, 2026, the Company announced a twenty-five-for-one forward stock split" [VERIFIED] — [SEC 8-K 2026-02-18](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000008/bkng-20260218.htm)
- Q4 2025 release: the Board approved a 25-to-1 split in Q1 2026, "effected on April 2, 2026" [VERIFIED] — [SEC ex99.1 Q4 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000008/q4-25bkngearningsrelease.htm)
- Q3 2026 release: "On April 2, 2026, the Company effected the 25-for-1 stock split"; all share and per-share data retroactively adjusted [VERIFIED] — [SEC ex99.1 Q3 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000044/q3-26bkngearningsrelease.htm)
- Split-adjusted trading began 2026-04-06 [REPORTED] — [Rallies.ai](https://rallies.ai/news/booking-holdings-jumps-as-25-for-1-stock-split-begins-post-split-trading-monday); pre-split closes quoted as $4,117.51 (Mar 30) [REPORTED] — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/4-000-stock-become-affordable-141559947.html)
- Close on 2026-11-03: $155.67 (+1.25%); after-hours $152.54; forward P/E 13.99; shares outstanding 751.38M [VERIFIED] — [stockanalysis BKNG statistics](https://stockanalysis.com/stocks/bkng/statistics/)

### Inferences
- $155.67 × 25 = $3,892 pre-split equivalent; journal $151.28 × 25 = $3,782 [PROVISIONAL]. Per-share history before April 2026 must be divided by 25. Pre-split EPS such as FY2025 adjusted EPS of $228.06 becomes $9.12 [PROVISIONAL].
- Forward P/E 13.99x at $155.67 implies a vendor next-twelve-month EPS of ~$11.13 [PROVISIONAL back-solve].

### Gaps
- Vendor forward-EPS definition (NTM or FY2027) [UNKNOWN].

## BKNG Q3 2026 results (released 2026-11-03 ~4:00 pm ET)

### Takeaway
Volumes beat and adjusted EPS grew +17%. GAAP revenue fell 1% because of a **$900M revenue reduction plus $100M accrued loss tied to an FTC matter**, excluded from adjusted figures. Q4 guidance is weak: room nights +1–3%, adjusted EBITDA about flat, with Middle East disruption assumed to last through year-end. Shares fell ~1.3–2% after hours [REPORTED].

### Cited Findings
- Timing: company notice (2026-11-02) said the release would be available "at approximately 4:00 p.m. ET on November 3", with a 4:30 pm ET call [VERIFIED] — [Booking IR notice](https://ir.bookingholdings.com/news/news-details/2026/Booking-Holdings-to-Make-Third-Quarter-2026-Earnings-Press-Release-Available-on-Companys-Investor-Relations-Website-on-November-3/default.aspx). 8-K (Items 2.02, 9.01) filed 2026-11-03 [VERIFIED] — [EDGAR index](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000044/0001075531-26-000044-index.htm)
- Q3 2026 vs Q3 2025 [VERIFIED, ex99.1]:
  - Room nights 345M (+7%). Gross bookings $54.5B (+10%; ~+11% constant currency). CC ADRs +~3%.
  - Revenue $8,893M vs $9,008M (−1%). Adjusted revenue $9,793M (+9%; ~+10% CC).
  - GAAP net income $2,717M (−1%). GAAP diluted EPS $3.61 vs $3.38 (+7%).
  - Adjusted net income $3,509M (+8%). Adjusted EPS $4.66 vs $3.98 (+17%).
  - Adjusted EBITDA $4,607M vs $4,231M (+9%). Margin 47.0%, flat year on year.
  - Diluted weighted shares 753M vs 814M (−7.5%).
- FTC: revenue reduced by $900M and a $100M loss accrued; details in 10-Q footnote 13 [VERIFIED, ex99.1]. Q3 10-Q not yet on EDGAR at ~17:00 ET [VERIFIED absence, EDGAR 10-Q list]. Q2 10-Q: FTC staff told Priceline in July 2026 they intended to recommend a complaint over disclosures, fees, customer support and billing [REPORTED via search summary of the [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001075531/000107553126000037/bkng-20260630.htm); not fetched directly].
- Cash and returns [VERIFIED, ex99.1]:
  - Operating cash flow: Q3 $1,137M (−21%); YTD $8,071M (+2%). FCF: Q3 $1,069M (−22%); YTD $7,820M (+2%).
  - Buybacks: Q3 $2.1B; YTD $9.9B; $12.4B authorisation remaining. Dividend $0.42/quarter.
- Balance sheet at 2026-09-30 [VERIFIED, ex99.1]:
  - Cash $15,814M; debt $1,987M short-term + $18,074M long-term.
  - Stockholders' deficit −$10,407M; deferred merchant bookings $6,450M.
- Costs [VERIFIED, ex99.1]:
  - Marketing 4.8% of gross bookings (4.7%). Adjusted fixed opex +6%.
  - Direct channel mix "mid-fifties" percent over the trailing four quarters. SBC $145M in Q3.
- Guidance (year on year) [VERIFIED, ex99.1]:
  - Q4: room nights +1–3%; gross bookings +2–4% (CC +4–6%); adjusted revenue +0–2% (CC +2–4%; ~2pt FX drag); adjusted EBITDA about flat.
  - FY2026: gross bookings and adjusted revenue high single digits; adjusted EBITDA high single digits; adjusted EPS low-to-mid teens.
  - Demand "moderated somewhat" late in Q3. October hit by Middle East travel disruption, higher airfares and "localized unrest in certain European cities".
- Consensus [REPORTED]: adjusted EPS ~$4.49 ([Newsquawk](https://www.newsquawk.com/headlines/booking-holdings-inc-bkng-q3-2026-usd-gross-bookings-545bln-exp-5269bln), [Investing.com](https://www.investing.com/news/earnings/booking-holdings-shares-fall-as-revenue-miss-and-travel-outlook-weigh-on-sentiment-4996454)); revenue ~$9.54–9.55B (compared against the GAAP $8.9B; adjusted $9.79B was above it) ; gross bookings ~$52.69B; room nights ~338.6M ([Yahoo/Zacks](https://finance.yahoo.com/markets/stocks/articles/exploring-analyst-estimates-booking-holdings-121506658.html)).
- After hours [REPORTED]: −1.3% ([Motley Fool, 4:19 pm](https://www.fool.com/investing/2026/11/03/booking-sees-q4-growth-stall-as-travel-cools-rapid-earnings-reaction/)); ~−2% ([Investing.com](https://www.investing.com/news/earnings/booking-holdings-shares-fall-as-revenue-miss-and-travel-outlook-weigh-on-sentiment-4996454)); stockanalysis after-hours $152.54 vs $155.67 close = −2.0% (quote time not stamped) [VERIFIED page; PROVISIONAL %].

### Inferences
- The "revenue miss" headline compares GAAP revenue, which includes the FTC charge, with consensus that excluded it. Adjusted revenue of $9.79B beat ~$9.55B [PROVISIONAL].
- TTM adjusted EPS = 9M26 $8.25 + Q4'25 $48.80/25 ($1.95) = $10.20, so $155.67 is 15.3x TTM adjusted [PROVISIONAL].
- FY2026 adjusted EPS implied at $10.22–10.49 ($9.12 × 1.12–1.15). That implies Q4 2026 adjusted EPS of ~$1.97–2.24 vs $1.95 a year ago [PROVISIONAL].
- Q3 FCF −22% while YTD is +2%, so working-capital timing is likely. The cause is [UNKNOWN].

### Gaps
- FTC complaint/settlement terms, cash timing and practice changes: Q3 10-Q footnote 13 not yet filed [UNKNOWN].
- Call commentary on AI traffic, October trends and the FY2027 framework: no transcript reviewed [UNKNOWN].
- Regular-session reaction on Nov 4–5 [UNKNOWN, future].

## BKNG multi-year quality, valuation, momentum, risks

### Cited Findings
- FY21–FY25 [VERIFIED; stockanalysis [income](https://stockanalysis.com/stocks/bkng/financials/) and [cash flow](https://stockanalysis.com/stocks/bkng/financials/cash-flow-statement/)]:
  - Revenue ($M): 10,958 / 17,090 / 21,365 / 23,739 / 26,917.
  - Operating margin: 24.0% / 28.5% / 27.7% / 32.0% / 35.2%.
  - FCF ($M): 2,516 / 6,186 / 6,999 / 7,894 / 9,087. Buybacks ($M): 163 / 6,621 / 10,377 / 6,509 / 6,440. SBC ($M): 376 / 404 / 530 / 599 / 617.
  - TTM (Jun-26): FCF $9,539M; buybacks $10,530M.
- Ratios FY21–FY25 / current [VERIFIED; [stockanalysis ratios](https://stockanalysis.com/stocks/bkng/financials/ratios/)]:
  - P/E 84.6 / 25.6 / 28.9 / 28.0 / 31.9 / 17.2. EV/EBITDA 31.1 / 14.4 / 19.3 / 20.2 / 17.2 / 11.7. P/FCF 39.2 / 12.6 / 17.7 / 20.8 / 19.0 / 12.4.
  - ROIC 32.6% / 75.4% / 63.5% / 53.1% / 60.9% / 92.5%. Equity is negative, so ROIC/ROE are distorted.
- FY2025 (pre-split basis) [VERIFIED, Q4 2025 ex99.1]: room nights 1,235M (+8%); gross bookings $186.1B (+12%); adjusted EPS $228.06 (+22%); FCF $9.1B (+15%). Transformation Program run-rate savings ~$550M by end-2026.
- Momentum (Yahoo split-adjusted closes, to 2026-11-03) [REPORTED, [Yahoo chart data](https://query1.finance.yahoo.com/v8/finance/chart/BKNG?range=2y&interval=1d)]:
  - BKNG: 1m −2.1%; 3m −19.9%; 6m −7.1%; 12m −22.6%. 52-week closing high $219.68 / low $147.94.
  - S&P 500: 1m −2.0%; 3m −2.2%; 6m +4.3%; 12m +10.5%.
  - stockanalysis [VERIFIED]: 50-day MA $169.03; 200-day MA $176.32; RSI 47; 52w −23.36%; beta 1.15.
- Peers at 2026-11-03 close [VERIFIED; stockanalysis [ABNB](https://stockanalysis.com/stocks/abnb/statistics/), [EXPE](https://stockanalysis.com/stocks/expe/statistics/), [TCOM](https://stockanalysis.com/stocks/tcom/statistics/)]:
  - ABNB $166.96: fwd P/E 29.6; P/FCF 20.3; EV/EBITDA 32.3; ROIC 16.8%; 52w +31.9%. Results Nov 5 after close.
  - EXPE $285.77: fwd P/E 12.6; P/FCF 7.8; EV/EBITDA 11.6; 52w +29.9%; shares −6.2%. Results Nov 4 after close.
  - TCOM $41.38: trailing P/E 7.8; fwd P/E 10.5; P/FCF 12.8; 52w −41.1%. Next results Nov 16 (estimated). Reports in RMB; vendor converts to USD.
- DMA: Booking.com designated a gatekeeper and must comply since 2024-11-14. An EC factsheet dated 2026-09-28 says businesses on Booking.com in the EEA can set prices freely [REPORTED via search snippet] — [EC DMA factsheet](https://digital-markets-act.ec.europa.eu/factsheet-how-dma-ensures-businesses-using-bookingcom-are-free-set-their-prices-and-bookingcom-2026-09-28_en?prefLang=sl). A hotel damages claim covering 2004–2024 parity clauses, backed by 30 national associations, is pending [REPORTED] — [Travel Weekly](https://travelweekly.co.uk/news/more-than-10000-european-hotels-seek-billions-in-claims-against-bookingcom).
- AI: Google is testing agentic hotel booking in AI Mode with OTAs as partners; Fogel says some traffic already runs through it [REPORTED] — [Hospitality-ON](https://hospitality-on.com/en/distribution/google-launches-ai-agent-hotel-booking-test-united-states), [AltexSoft](https://www.altexsoft.com/travel-industry-news/investors-are-nervous-googles-next-ai-agent-will-rival-otas). The Q3 release says Booking collaborates "with industry-leading AI platforms" [VERIFIED, ex99.1].

### Inferences
- BKNG trades at the bottom of its own FY22–25 range on P/FCF (12.4 vs 12.6–20.8) and below the range on EV/EBITDA (11.7 vs 14.4–20.2) [PROVISIONAL].
- Buybacks of ~$13B/year annualised are ~11% of market cap [PROVISIONAL]. Net debt ~$4.2B on the balance sheet; stockanalysis shows $3.41B [PROVISIONAL difference].
- FCF/GAAP net income has run 134–202% (FY22–25), helped by float from deferred merchant bookings [PROVISIONAL].

### Gaps
- AI-originated share of bookings and any commission concessions to AI platforms [UNKNOWN].
- Next results date: Q4 2025 was released 2026-02-18, so PROVISIONAL ~mid/late Feb 2027; no company notice [UNKNOWN].

## Visa FY2026 Q4 (released 2026-10-27, 16:05 ET)

### Takeaway
A clean beat: net revenue +13%, non-GAAP EPS $3.48 (+17%) vs ~$3.44 consensus [REPORTED]. Value-added services were +31% [REPORTED call]. Client incentives grew 21%, outpacing revenue. FY2027 guide: low-double-digit net revenue growth; adjusted EPS growth low double digits to low teens [REPORTED call]. The stock is +24.8% over 12 months vs S&P +10.5%, near its 52-week high, at ~28x forward (journal's ~28x confirmed: 27.98x) [VERIFIED].

### Cited Findings
- Q4 FY26 [VERIFIED, [SEC 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000126/q42026earningsrelease.htm); accepted 2026-10-27 16:05:22 per EDGAR]:
  - Net revenue $12,139M (+13% nominal and CC).
  - Service revenue $5,255M (+14%); data processing $6,245M (+16%); international transaction $4,115M (+8%); other $1,647M (+40%).
  - Client incentives $5,123M (+21%). GAAP opex $4,877M (+7%); non-GAAP opex $4,051M (+12%).
  - GAAP net income $6,002M / EPS $3.19 (+22%). Non-GAAP $6,552M / EPS $3.48 (+17%). Diluted shares 1.88B.
  - Volumes (CC): payments volume +9%; cross-border ex intra-Europe +14%; processed transactions 74.2B (+10%).
- Q4 non-GAAP adjustments (EPS) [VERIFIED]: litigation provision $469M pre-tax ($0.19); Visa Foundation contribution $282M ($0.11); equity-investment gains −$155M (−$0.06); intangibles amortisation $0.02; acquisition costs $0.01; deferred tax $0.02.
- FY2026 [VERIFIED]:
  - Net revenue $45,903M (+15%; CC +14%). GAAP EPS $12.32 (+21%); non-GAAP EPS $13.27 (+16%).
  - Litigation provision $1,724M ($0.70); severance $563M ($0.23); deferred tax benefit −$0.16.
  - Client incentives $18,317M (+16%). Operating cash flow $23,728M.
  - Buybacks ~61M shares for $20.5B (avg $335.49). Total returned $25.6B; $24.4B authorisation remaining.
  - Dividend +16% to $0.78/quarter. $405M litigation escrow deposit (EPS effect like a buyback at $366.81).
  - BioCatch acquisition ($2.4B cash) expected to close by end of fiscal Q2 2027.
  - Cash plus investments $14.2B; debt ~$22.1B. No outlook in the release.
- Call [REPORTED, [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/28/visa-v-q4-2026-earnings-call-transcript/)]:
  - FY27 (adjusted, CC): net revenue low double digits; opex low double digits, modestly below revenue; EPS low double digits to low teens; tax ~19%. Q2 is the growth low point; ~25% of payments volume up for renewal (20% in FY26).
  - Q1 FY27: net revenue low double digits; EPS growth "low end of mid-teens".
  - October to Oct 21: US payments volume +10%; cross-border ex intra-Europe +15%.
  - VAS revenue: Q4 $4B (+31% CC); FY $14B (+30%). CMS revenue +19% in FY26. Visa Direct >15B transactions.
  - Stablecoin settlement run rate >$25B annualised (10x YoY). ~50 agentic AI partners; volumes "very small".
- Reaction [REPORTED, [KuCoin blog](https://www.kucoin.com/blog/visa-stock-falls-after-q4-2026-earnings-beat-as-investors-weigh-2027-outlook)]: as much as −2.3% after hours Oct 27; Oct 28 close $400.60 (−0.31%).
- Market data, 2026-11-03 close [VERIFIED, [stockanalysis V](https://stockanalysis.com/stocks/v/statistics/)]:
  - Price $420.42; market cap $781.8B; EV $789.8B.
  - Trailing P/E 34.1; forward 27.98; P/FCF 35.5; EV/EBITDA 24.9.
  - ROIC 57.0%; FCF TTM $22.06B; shares −3.0% YoY; 50/200-day MA $383.16 / $343.15; RSI 69.
- History FY22–FY26 [VERIFIED; stockanalysis [ratios](https://stockanalysis.com/stocks/v/financials/ratios/), [income](https://stockanalysis.com/stocks/v/financials/), [cash flow](https://stockanalysis.com/stocks/v/financials/cash-flow-statement/)]:
  - P/E 23.3 / 25.6 / 26.9 / 32.0 / 28.1. Forward P/E 22.2 / 24.2 / 25.7 / 27.5 / 24.9. EV/EBITDA 17.1 / 19.2 / 21.1 / 22.9 / 21.1. P/FCF 19.1 / 22.1 / 28.0 / 29.4 / 29.9.
  - ROIC 40.1% / 44.9% / 46.3% / 49.1% / 57.2%. Operating margin 67.2% / 67.2% / 66.8% / 67.0% / 66.3%.
  - FCF ($M) 17,879 / 19,696 / 18,693 / 21,577 / 22,057. Buybacks ($M) 11,709 / 12,231 / 16,921 / 18,597 / 20,740. SBC ($M) 602 / 765 / 850 / 897 / 928.
  - FY2021 and earlier are not shown, so a 10-year history is [UNKNOWN].
- Peers, 2026-11-03 close [VERIFIED, stockanalysis]:
  - [MA](https://stockanalysis.com/stocks/ma/statistics/) $647.18: fwd 29.1; P/FCF 35.1; EV/EBITDA 25.1; ROIC 91%; 52w +17.3%.
  - [AXP](https://stockanalysis.com/stocks/axp/statistics/) $325.50: fwd 16.8; 52w −9.8%.
  - [PYPL](https://stockanalysis.com/stocks/pypl/statistics/) $58.21: fwd 9.9; P/FCF 7.7; 52w −15.6%.
- Momentum (Yahoo closes to 2026-11-03) [REPORTED, [Yahoo chart data](https://query1.finance.yahoo.com/v8/finance/chart/V?range=2y&interval=1d)]: V 1m +16.6%; 3m +13.8%; 6m +30.6%; 12m +24.8%; 52-week closing high $425.51 / low $295.52. MA 1m +17.2%; 6m +30.2%. S&P 500 as above.
- Litigation and regulation:
  - DOJ debit monopolisation suit (SDNY, filed Sept 2024) is in discovery. DOJ warned Visa's schedule could push trial to late 2027 or 2028 [REPORTED] — [Payments Dive](https://www.paymentsdive.com/news/doj-presses-visa-antitrust-case/808859/).
  - Revised merchant interchange settlement got **preliminary** approval on 2026-06-09: 10bp average reduction for five years, standard consumer credit rates capped at 1.25%, wider surcharging and card-category acceptance choice [REPORTED] — [PYMNTS](https://www.pymnts.com/credit-cards/2026/judge-signals-approval-for-visa-and-mastercard-swipe-fee-settlement/), [American Banker](https://www.americanbanker.com/payments/news/judge-approves-card-network-fee-settlement-with-merchants). Final approval possibly late 2026 or early 2027 [REPORTED].
  - Credit Card Competition Act reintroduced 2026-01-13 with presidential endorsement. Dropped from the crypto markup (Jan 30) and the housing bill (Mar 12). No vote scheduled as of the latest source found (Mar 2026) [REPORTED] — [Payments Dive](https://www.paymentsdive.com/news/ccca-seeks-new-path-to-passage/813789/), [PYMNTS](https://www.pymnts.com/credit-cards/2026/president-donald-trump-endorses-legislation-lower-credit-card-swipe-fees/), [American Banker](https://www.americanbanker.com/news/trump-backs-durbin-marshall-swipe-fee-bill).
- Next results: Q1 FY26 8-K was accepted 2026-01-29 16:05 ET [VERIFIED, [EDGAR](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000044/q12026earningsrelease.htm)], so PROVISIONAL late Jan 2027. No company notice found [UNKNOWN].

### Inferences
- Client incentives were 29.7% of gross revenue in Q4 and 28.5% for FY26 [PROVISIONAL]. Incentive growth (+21%) well above net revenue (+13%) plus ~25% renewals in FY27 is the main take-rate watch item.
- 27.98x forward implies ~$15.03 next-year EPS, about +13% on $13.27, at the top of the guide [PROVISIONAL]. The forward multiple sits ~12% above the FY22–26 average (24.9x). P/FCF (35.5) and EV/EBITDA (24.9) are above every FY22–26 year-end [PROVISIONAL].
- FY26 FCF/GAAP net income was 94% (87% of non-GAAP), below FY25's 109%. Litigation cash and escrow are a possible cause [PROVISIONAL].
- Recurring "one-offs": litigation provisions were $1.72B in FY26 and are excluded from non-GAAP every year. Treat part of them as a recurring cost of the franchise [PROVISIONAL].

### Gaps
- FY2026 10-K (litigation reserve detail, US covered litigation escrow balance) not yet filed (FY25 10-K was filed 2025-11-06) [UNKNOWN].
- DOJ case trial date and summary-judgment schedule [UNKNOWN]; CCCA activity after March 2026 [UNKNOWN].
- Visa 10-year valuation history [UNKNOWN]; VAS figures only from the call transcript, not the release [REPORTED].
