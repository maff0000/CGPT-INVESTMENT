# VALIDATION-FIRST-001 — Equity research requirements and proof charter
**Date:** 2026-11-05, Europe/London | **Decision:** MANDATORY BEFORE AGENT BUILD | **Evidence status:** NOT YET PROVEN.

**MACRO-PROSPECTIVE-001 amendment (2026-11-05):** this charter now prioritises **in-time, prospectively recorded macro-aware research**. Conventional mechanical retrospective strategy backtesting is **optional and deferred**, **not** a G0–G4 acceptance requirement. Historical financial performance/valuation data can inform context. G3 means **additional independent forward validation**, not a mandatory separate historical walk-forward study. Read [macro doctrine](macro-aware-equity-review.md) and [decision](../research/decisions/2026-11-05-macro-aware-forward-validation.md). Do not claim prospective process proof before observation.

## Direction
**Prove the process, then automate it.** The current Finviz QARP v2 screens, chart-stage model, WATCH/COILING/AT PIVOT research, earnings gate, independent thesis challenge and candidate scoring are a coherent **candidate methodology**, not a validated investment edge. Neither 22 historically selected stocks nor six external scanner leads constitute a representative test. The proposed agent operating system is **architectural reference only**, not an approved software build.

This project aims to develop a **repeatable, decision-useful equity selection process** which finds high-quality, well-valued opportunities, identifies early price structures, rejects weak/crowded/unsafe ideas, and produces reproducible investor review decisions. A small number of excellent candidates is preferable to a quota of trades.

### Three separate validation questions
| Question | What successful evidence would look like | Status |
|---|---|---|
| **Process validity** | Two reviewers applying the same frozen definitions to the same market-close snapshot reach broadly consistent classifications, evidence packs, and earnings gates; all unknowns disclosed | UNPROVEN |
| **Predictive/investment utility** | Prospectively timestamped candidate groups and hypothetical decisions improve selected *net-of-cost* return/risk or avoid adverse selection versus simple benchmarks, including failures and missed names | UNPROVEN |
| **Operational repeatability** | Daily manual process closes within practical time, has stable data provenance, complete negative and positive case tracking, and no unreviewed gate breach | UNPROVEN |

**World-class means a disciplined and independently testable process, not a promise of outperformance**. Evidence may demonstrate that a screen has no useful predictive power. In that case: change or discard it, record the falsification, and retest a new version without hiding the prior failure.

## Non-negotiable invariants
1. Retain **Finviz QARP v2 A/B/C** exactly as the current *baseline*: [current filters](finviz-filters.md). A/B/C membership, actual **chart stage**, fundamental investment **eligibility** and realised results are **four different things**.
2. Group price action as **WATCH / BASE FORMING / COILING / AT PIVOT**, **BREAKING OUT**, **IN TREND**, with CHART PENDING for missing evidence; identify a documented resistance and a completed regular-session close before confirming a breakout.
3. A quiet base, low RVOL or hypothetical VCP is **NOT PROOF of institutional accumulation**. All trial range, volume and pivot thresholds remain **HYPOTHESES**.
4. **Company quality and fair price** must stand independently of charts: profitability, ROIC, after-capex cash flow, working capital, balance sheet, corporate actions, valuation, downside; use industry-specific metrics for financials, REITs, utilities and cyclicals. **PEG is a secondary clue**, not a universal gate, especially when growth/earnings is unstable.
5. Read public primary earnings releases and filings; hard **seven exchange sessions before earnings plus announcement date, two full sessions after** before *new-entry/addition review*. Unknown/conflicting events block.
6. **Independent challenge:** two material contrary explanations, capital loss case, precise WAIT/REJECT triggers; high user or analyst conviction can never clear a gate.
7. **Macro, sector, industry and market context** are mandatory, timestamped and explicitly connected to company-level cash flows/valuation, with expectations and contrary evidence; a war/election/oil story is not a buy signal. Sector, industry and market context are mandatory and time-matched. No automatic sector veto; avoid treating a highly correlated group as diversified.
8. Record **all** eligible screen counts, screened-out/rejected names, missed winners, watch failures, event exclusions and delistings wherever data permits. No curated winners-only study.
9. All actions and results must use **realistic observability and execution clocks**. A close-after-screen signal cannot be notionally bought at the same day's close. Prices, splits, dividends, FX, turnover, slippage and fees must be measured or clearly assumed before comparisons.
10. All public GitHub work stays **non-identifying public research**, not personal holdings, cash reserves, individual buy intentions, actual order quantities or account/adviser information.

## Requirements to prove, with acceptance evidence
| Requirement | Manual acceptance artefact | Failure / HOLD condition |
|---|---|---|
| R01 **Universe and data rights** | Written exchange/listing universe; point-in-time eligible tickers, new/delisted names, provider licence & timestamps, company ID mapping | Universe cannot be reproduced; unlicensed exports or missing as-of |
| R02 **A/B/C reproducibility** | Same-day Finviz filter screenshot/export or exact saved values; independent line-by-line sample and exception log | Claim of screen pass without real evidence; stale fundamentals |
| R03 **Pre-breakout discovery** | At least one prospective complete daily cohort ledger incl. zero-signal days, scored base/volume and sector observations, rejection reasons | Subjective post-hoc pattern labels; retrospective cherry-pick |
| R04 **Chart classification reliability** | Independent blind dual-review of a fixed sample; adjudicated disagreements; named base/pivot, SMA and volume evidence | Two reviewers assign incompatible stage to same completed chart without explanation |
| R05 **Fundamental/valuation assessment** | Consistent company dossiers with bear/base/bull, after-capex owner cash, documented industry-specific exceptions and value ceilings | PEG/P-E-only or price-action-only buy recommendation |
| R06 **News/earnings reliability** | Company-verified schedule with exact local release time, event gate state and timestamped source; contradiction checks | Missing earnings time or gate breach |
| R07 **Independent decision discipline** | BUY STARTER / BUY FULL / WAIT / REJECT plus falsification and next review; decisions timestamped *before* results | Enthusiasm, old price thresholds or story used as substitute for evidence |
| R08 **Opportunity and baseline comparison** | Predeclared matched sector/index and simple strategy baselines, defined observable entry and exit, gross/net returns, adverse excursion | Uses today's winners or hindsight fills in performance claims |
| R09 **Risk/portfolio suitability boundary** | Public generic loss/scenario rules plus separate private authorisation workflow if later needed | Public leakage, unapproved sizing or an AI recommendation described as a trade |
| R11 **Contemporaneous macro transmission** | Dated fact-vs-hypothesis dashboard, nominal/real yields, oil/energy, central-bank/inflation, credit, FX, geopolitical/election/trade facts, shortages and company cash-flow effects, alternate scenarios and priced-in expectations | Hindsight explanations, unsourced events, no company mechanism or missed macro release risk |
| R10 **Durable learning and recovery** | Daily reproducible audit, candidate versions, all failures, weekly decisions, GitHub main SHA, documented unresolved unknowns | No record of rejects/false breakouts or unverified commits |

## Proof programme: sequential gates
**G0 — SPECIFICATION FREEZE.** Resolve objective, investable universe, style/holding-horizon differences, baseline screens, chart rules and uncertainty codes, **macro snapshot/source/time and company-transmission rules**, independent reviewer process, evaluation benchmarks, data availability, fees and trade clock. Freeze as **VALIDATION v1.0** *before* using future outcomes to tune it. Current state: **OPEN**.

**G1 — MACRO-AWARE MANUAL REPRODUCIBILITY.** Before company judgements archive the *in-time* macro fact/forecast and sector impact snapshot. Over a provisional **20–30 completed US sessions** (not necessarily consecutive if unavailable), apply the agreed process and track every result, including no signals. Provisional operating acceptance: **>=95% evidence completeness on required fields**, **100% verified event/valuation gate compliance for actionable opinions**, audited agreement on a **minimum 30 blind-reviewed stage classifications**, and a sustainable review cadence. The 30 samples and 95% are **proposal thresholds**, not claims they ensure predictive edge. Exclude UNKNOWN from neither denominator nor reporting. Status: **NOT STARTED**.

**G2 — COMPETITIVE UTILITY.** Compare prospective **macro-aware** WATCH→AT-PIVOT→BREAKING-OUT and IN-TREND decisions against an otherwise matched **macro-blind version**, and with **(i) all eligible A/B/C without chart ranking, (ii) simple confirmed-breakout/momentum baseline, (iii) market and sector buy-and-hold** on the *same timestamps and reasonable holding periods*. Include outcome distributions, maximum adverse excursion, failed signals, opportunity cost, costs and adverse market regimes. Predeclare metrics, not just a favourable retrospective statistic. **At least 60 completed sessions after each signal are needed to evaluate its 60-session outcome**; a 20-session G1 pilot by itself cannot prove investment advantage. Status: **NOT STARTED**.

**G3 — INDEPENDENT FORWARD REPLICATION.** A blind reviewer repeats the *frozen* process on **additional future trading sessions** with separately observed macro conditions and relevant company facts; include sectors, failed candidates and market changes. No separate historical walk-forward backtest is required. Hold out future cohorts from rule tuning and record every variant. **90–120 US sessions of prospective monitoring** is a provisional early-process benchmark, not statistical proof: regime diversity, realised events, sample size and uncertain effects determine confidence. Failure to improve outcomes must be reported, not rationalised. Status: **NOT STARTED**.

**G4 — AUTOMATION REQUIREMENTS PERMISSION.** Only after G0–G3 evidence and an explicit independent go/no-go decision may the project authorise a **bounded build work order** for *research-only automation*. The execution/broker adapter requires entirely separate later risk, broker/legal, paper, audit and individual order authorisation. Status: **BLOCKED**.

**Do not interpret a calendar minimum or an observation count as statistical validation.** The number of independent candidate events, uncertainty and variety of market regimes determine the real confidence. A surprising negative result is valuable if accurately recorded.

## Open requirements requiring a decision, not guesswork
- Define **eligible market** precisely: Finviz's universe is US-listed equities, even when Country=Any; US ADR/foreign domicile semantics, minimum dollar liquidity, splits/delistings and ETF/financial-sector exceptions need a written rule.
- Define **mandate/horizon** and eligible risk type: strategic 5–10yr compounders versus tactical 5/20/60-session breakouts may need separate baselines and investment actions; do not impose one chart-entry signal on every compounder.
- Confirm access/rights to **current and recent completed-session OHLCV**, optional historical chart context, and **publication-time fundamentals/macro vintages**. Backtesting is not mandatory. Finviz explicitly does **not provide historical screener data**: [official introduction](https://finviz.com/knowledge-base/screener/getting-started-with-screener/introduction-to-screener).
- Define sector taxonomy, event time stamps and genuine as-of data; normalise price and share-volume for splits and corp actions.
- Define how a BUY opinion is tested without inventing a portfolio-sized investment or treating hypothetical returns as real P&L.
- Define cost/slippage ranges and treatment of missing data/corporate actions and multiple candidates from the same sector.

## External validation doctrine
CFA Institute [2026 Active Equity Strategies](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/active-equity-investing-strategies) describes investment process, valuation, bias and cost/model pitfalls. [2026 Backtesting & Simulation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) discusses rolling walk-forward evaluation and stress analysis. CFA Research Foundation [Investment Model Validation](https://rpc.cfainstitute.org/-/media/documents/article/rf-brief/investment-model-validation.pdf) addresses survivorship/look-ahead. [SEC performance bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-47) warns that backtested results are hypothetical and cherry-picking misleads.

**Read next:** [prospective manual test protocol](research-validation-protocol.md), [daily review worksheet](../templates/manual-equity-validation-review.md) and [decision to freeze automation](../research/decisions/2026-11-05-validation-first-freeze.md).
