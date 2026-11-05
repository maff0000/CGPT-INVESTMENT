# G0-DATA-002 — $1 source tolerance and OHLCV provider acceptance trial
**Accepted price-review preference:** 2026-11-05 (Europe/London) | **G0 state:** data-provider evaluation OPEN, no selected feed or downloaded dataset.

## Exact user-approved USD price discrepancy rule
Compare two vendor **regular-session closing prices for the same USD-listed instrument and the same completed US session**, with raw-versus-adjusted and share class already reconciled. Let absolute_difference = absolute value of (price A − price B), in USD **per share**.

| Absolute difference | Source-review state | Meaning |
|---|---|---|
| **<= $1.00, inclusive** | **PRICE_OK** | No routine PRICE CHECK flag or automatic refusal to research. Log both quotes, difference and percentage for audit but do not unnecessarily escalate cents. |
| **> $1.00** | **PRICE_CHECK** | Investigate source timestamps, adjustments, currency, stock splits, stale sessions, corporate actions and price convention. Do not use a disputed close as a definitive signal while material. |
| **Either amount where input dates / instruments / currencies / adjustments differ** | **DATA_MISMATCH** | Compare like with like first; the $1 rule only applies after basic identity/time integrity passes. |
| **Either amount where one source crosses a nominated breakout/pivot/limit but the other does not** | **SIGNAL_AMBIGUOUS** | **No verified BREAKING OUT or entry price confirmation until chart/broker-appropriate authoritative price resolves it**. This is a *decision/evidence* safeguard, not a routine PRICE CHECK flag and not a company rejection. |

Under the exact user-requested threshold, **a $1.00 discrepancy is accepted, $1.01 is flagged**. The rule is a quote-quality policy, **not a definition of a tradeable spread, buy limit, permitted slippage or price certainty**. Record percent disagreement as context, especially for lower-priced eligible shares, but **do not secretly add a competing percentage-price flag** without an explicit future requirements decision.

**Legacy XOM/LIN/EQIX diagnostic:** Nov 4 XOM $169.49/$169.46 → $0.03 PRICE_OK; LIN $524.74/$524.91 → $0.17 PRICE_OK; EQIX $1,054.25/$1,054.09 → $0.16 PRICE_OK. None needs PRICE_CHECK under the revised rule. Source provenance remains useful for research and accounting.

## Concrete test cases for G0 manual approval
| Source A | Source B | Reference pivot | Expected result |
|---:|---:|---:|---|
| $100.00 | $100.99 | None | PRICE_OK |
| $100.00 | $101.00 | None | PRICE_OK — boundary |
| $100.00 | $101.01 | None | PRICE_CHECK |
| $100.20 | $100.70 | $100.50 | PRICE_OK **plus SIGNAL_AMBIGUOUS**; do not confirm breakout |
| $100.00 | $100.20 | None, but one bar from another session | DATA_MISMATCH |
| $25 raw | $12.50 split-adjusted | None | DATA_MISMATCH; not a legitimate $12.50 source disagreement |

## Verified provider shortlist (documentation only; no account/API keys accessed)
| Data provider | Verified service ability | Timeliness and licence questions | G0 priority |
|---|---|---|---|
| **Massive (formerly Polygon)** | [All-US grouped daily OHLCV](https://massive.com/docs/rest/stocks/aggregates/daily-market-summary), [ticker bars](https://massive.com/docs/rest/stocks/overview), splits/dividends, [2 yrs history and 5 calls/min on Basic free](https://massive.com/pricing?product=stocks). Grouped EOD Basic can request the preceding session from **00:00 ET next day**: [provider confirmation](https://massive.com/knowledge-base/article/on-the-free-basic-plan-when-can-i-pull-the-previous-trading-days-data). | Split-adjusted by default; **not dividend-adjusted**: [official FAQ](https://massive.com/knowledge-base/article/is-massives-stock-data-adjusted-for-splits-or-dividends). Basic is listed **individual use**, not blanket permission for a hosted service or redistribution. Need trial account/data licence and real price tests. Provider flat files are often later and may be corrected. | **First manual acceptance candidate**, conditional |
| **Tiingo** | [EOD price API](https://www.tiingo.com/documentation/end-of-day) includes raw and **split/dividend-adjusted OHLCV**, dividends/splits and metadata. | US EOD generally becomes available around **17:30 ET**, with exchange corrections sometimes up to **20:00 ET**; no credential or commercial use rights confirmed. Good cross-check if access/terms permit. | **Independent comparator**, conditional |
| **EODHD** | [Official plans](https://eodhd.com/help/plans): free tier 20 calls/day and one year EOD/split/dividend data; wider paid bulk EOD and delisted coverage; fundamentals subscription separate. | Free plan insufficient for full-market nightly scan; **personal plan** is not presumed to allow enterprise/agent use or public redistribution. Test adjustment and history semantics before adoption. | **Alternative** |
| **Finviz** | [Official filters and SMA50/200](https://finviz.com/help/screener); [screening and ELITE exports](https://finviz.com/knowledge-base/screener/getting-started-with-screener/introduction-to-screener). | **No historical screener snapshots**. Finviz is a validation baseline for A/B/C, **not** an assumed licensed OHLCV API. No scripted scraping permission has been established. | **Independent manual screener benchmark**, not a canonical data feed |

**Provisional preference:** test Massive Basic using documented US grouped EOD, then independently compare 22 watched names plus SPY/sector ETF daily closes against a second authorised source. This is a **trial proposal, not provider selection, data download or implementation authorisation**. Paid/commercial plans only if price, licence, schedule and coverage evidence justify them.

## Why one reliable 200-bar-plus history matters
Our 200-day SMA requires at least **200 completed sessions**; robust lookback and slope checks need more. A first *manual* candidate data trial should inspect **~260 completed daily bars** for a small subset (XOM/LIN/EQIX, representative low-price and high-price names, SPY and key sector ETFs). The 10/prior-40 volume and daily-range comparison needs 50 **non-overlapping** completed sessions; proposed 20–60-session base needs the same market series and objective resistance adjudication. A two-year feed should cover the pilot. Do not compute or claim metrics without data.

## Acceptance plan — no agents, no code construction authorised
**D1 — Contract:** check whether the available plan legally permits manual retrieval, storage of sample OHLCV, a reproducible research report and any subsequent automated or public use. If unclear, HOLD for terms/provider confirmation. The free individual plan is **not** acceptance of future commercial agent use.
**D2 — Data sample:** choose one completed session, retrieve OHLCV **using an authorised account** for XOM/LIN/EQIX and at least two differently priced stocks, SPY and relevant sector proxies; record request/returned timestamps and raw/adjusted.
**D3 — Close reconciliation:** compare a second source for same session; apply **PRICE_OK vs PRICE_CHECK at >$1.00**, plus independent DATA_MISMATCH and SIGNAL_AMBIGUOUS. Log observed discrepancies; do not invent zero errors.
**D4 — Historical mechanics:** acquire 260 completed bars per representative name; check missing/duplicated sessions, split/ETF/corporate action behaviour, SMA50/SMA200 and slope, 10/40 contraction and volume ratio, 20–60 base and pivot. Verify independently on manually inspected charts.
**D5 — Current Finviz:** contemporaneously reproduce A/B/C on the same observation date, timestamp screenshot/export/settings and record overlapping memberships, provider definition differences and exceptional industry cases. Never infer Finviz PASS from another vendor's numbers.
**D6 — Manual acceptance:** a fresh reviewer signs off data coverage, integrity/limits and observed differences; freeze detailed G0 source policy **only after** sample is complete and validated. G1 then begins prospective manual reviews under frozen rules.

## Open issues and hold states
No Massive/Tiingo/EODHD credentials, data exports, 260-bar charts, actual fresh Finviz A/B/C results or licence terms have been tested yet. No provider is final; no 22-company scan has occurred. **G0 OPEN, G1 NOT STARTED, agents/brokers BLOCKED**. Quote discrepancy policy has been accepted; full pipeline data proof has not.

Related: [older G0-DATA-001 findings](g0-data-integrity-and-valuation-rules.md), [original QARP screens](finviz-filters.md), [validation charter](research-process-validation-charter.md), [price-source worksheet](../templates/g0-price-source-comparison.md), [decision](../research/decisions/2026-11-05-price-tolerance-provider-trial.md).
