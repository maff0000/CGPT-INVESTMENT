# G0-DATA-001 — Price reconciliation, point-in-time sources and industry-specific valuation
**Draft for manual G0 approval, 2026-11-05. Not a frozen validation standard.**

## Problem found
In the first three-company trial, reputable market-data websites disagreed slightly about the 4 November closing prices. This matters near exact breakout levels. We also found that oil producers, industrial-gas compounders and REITs cannot be evaluated by the same unqualified PE, PEG or price/free-cash-flow cutoff.

## Proposed source hierarchy and failure rules
| Evidence | Source preference | Failure mode |
|---|---|---|
| Regular-session OHLCV | Approved, licensed, reproducible exchange/consolidated daily-bar provider; record regular session vs after-hours, raw/adjusted close, timezone, split/dividend method | If unavailable, CHART PENDING, not a guessed breakout |
| Independent close check | Second clearly identified source; record exact difference and market cutoff | If discrepancy could change breakout, support, entry ceiling or any verdict, HOLD until authoritative reconciliation, even if only cents |
| Macro data | Treasury/Fed/BLS/BEA/EIA official release, observing original publication date and vintage; secondary dated quotes labelled as such | Old macro releases must not be presented as same-day observations |
| Company fundamentals | Issuer IR or EDGAR by exact fiscal period and publication timestamp; vendor estimates explicitly separate from GAAP/non-GAAP actuals | Unknown inputs stay UNKNOWN |
| Earnings calendar | Issuer-confirmed date and release time, exchange calendar for 7-before/2-after | Missing or inconsistent timing blocks entry review |
| Screen eligibility | Contemporaneous real Finviz A/B/C output and recorded settings, or explicitly labelled independent approximation | Watchlist membership is never a Finviz PASS |
| Actual sector | Versioned taxonomy; keep research-origin lane separate, reconcile disputed provider labels | No hidden sector switch to make strength look better |

Finviz [official FAQ](https://finviz.com/help/faq) says it covers NASDAQ, NYSE and AMEX and is not permitted to sell raw historical data. Country=Any does not imply screening every global exchange. Verify commercial access, retention, onward distribution and historical OHLCV rights before choosing the canonical feed.

Each critical observation carries ticker and instrument identity, source, observation/effective time, company fiscal period where relevant, publication time, retrieval time, unit/currency, adjustment and time zone, VALID/UNKNOWN/CONFLICTED, calculation version and evidence URI. An event held as of 5 November is not treated as if known on 4 November.

## Actual Nov 4 vendor comparisons — small but real
| Company | Actual sector | Stock Analysis displayed close | Independent source displayed close | Absolute disagreement |
|---|---|---:|---:|---:|
| XOM | Energy | $169.49 | ChartExchange $169.46 | $0.03 |
| LIN | Materials | $524.74 | ChartExchange $524.91 | $0.17 |
| EQIX | Real Estate | $1,054.25 | MarketBeat $1,054.09 | $0.16 |

[Stock Analysis XOM](https://stockanalysis.com/stocks/xom/history/), [ChartExchange XOM](https://chartexchange.com/symbol/nyse-xom/historical), [Stock Analysis LIN](https://stockanalysis.com/stocks/lin/history/), [ChartExchange LIN](https://chartexchange.com/symbol/nasdaq-lin/historical/), [Stock Analysis EQIX](https://stockanalysis.com/stocks/eqix/history/), [MarketBeat EQIX](https://www.marketbeat.com/stocks/NASDAQ/EQIX/chart/).

These are working provider comparisons, **not canonical exchange auction closes**. Select the legal and authoritative feed at G0 before assigning breakout labels. No cherry-picking of the quote closest to a desired pivot.

## Industry financial logic
- **XOM, integrated energy:** use cycle-normalised upstream/downstream prices and margins, production, sustaining capital, balance sheet, distributions and at least three *illustrative, clearly non-predictive* oil stress cases. Do not annualise a war-influenced quarter as guaranteed owner earnings. Latest Q3 company FCF $19.1bn: [company release](https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results).
- **LIN, industrial gases:** reconcile GAAP with adjusted EPS, organic vs reported growth, pricing/pass-through, contract backlog conversion, after-capex cash, incremental ROIC and premium multiple compression. Issuer FY2026 **adjusted EPS** guidance $17.82–$17.92. A Stock Analysis price of $524.74 divided by midpoint $17.87 = **about 29.4x FY2026 issuer-adjusted EPS**, not strict Finviz forward PE and not fair value. [SEC-hosted release](https://www.sec.gov/Archives/edgar/data/1707925/000165495426009199/lin_ex991.htm).
- **EQIX, REIT/data centres:** use AFFO/share, source-specific AFFO definition, maintenance vs expansion capital, debt maturity/refinancing, dilution, contracted power and incremental returns. Issuer guidance **2026 AFFO/share $43.71–44.11**, so Stock Analysis price $1,054.25 divided by $43.91 midpoint = **about 24.0x AFFO/share**, NOT PE. Total company debt principal at 30 Sep about $25.2bn. [Q3 issuer release](https://newsroom.equinix.com/2026-10-28-Equinix-Reports-Third-Quarter-Results-and-Raises-2026-Guidance).

Do not loosen A/B/C globally: record strict result PASS/FAIL/UNKNOWN and a **separate explicit industry-specific research exception**. A qualified exception is not a falsely passed QARP screen.

## Macro incremental value needs a real comparator
A single researcher cannot credibly become blinded to the election and oil shock by simply imagining a macro-free world. Preferred design: reviewer A receives the company-only dated pack and independently freezes an opinion, reviewer B receives the same pack plus the macro overlay and independently freezes another, without seeing A's label. Report contamination from public news exposure. If two reviewers are unavailable, define a simple rules-only deterministic baseline **before** subsequent outcomes, but do not call it blind independent judgement.

## G0 gate status
Open: authorised historical/point-in-time OHLCV and licensing; exact close convention; earnings release-time checks; 20–60 day base and actual 10/prior-40 calculation; actual current A/B/C; industry cash-flow and bear/base/bull; outcome horizon and review roles; risk-free source hierarchy signoff.

**Do not begin G1 observation or claim a breakout/BUT verdict on this evidence.** No broker authority or agent work authorised.
