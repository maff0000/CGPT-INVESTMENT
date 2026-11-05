# RESEARCH-VALIDATION-001 — Prospective manual testing protocol
**Version:** Draft v0.1, 2026-11-05 Europe/London | **Cannot claim proof until the G0 specification is frozen and daily evidence exists.**

**MACRO-PROSPECTIVE-001 amendment:** prospective, **macro-aware** manual validation is the primary test. Mechanical retrospective strategy backtesting is deferred/optional. G3 now means **additional independent forward replication** (not a mandatory historical walk-forward). Read [macro doctrine](macro-aware-equity-review.md), the [G0–G4 amendment](../research/decisions/2026-11-05-macro-aware-forward-validation.md) and the revised [session worksheet](../templates/manual-equity-validation-review.md).

## Predeclare test hypothesis and falsifiers
- **H1 discovery:** a qualifying WATCH / COILING or AT PIVOT identifies subsequent BUY-eligible breakouts earlier than waiting only for current Finviz C momentum.
- **H2 chart classification:** independent reviewers can distinguish WATCH/BREAKING OUT/IN TREND consistently from the same completed-bar evidence.
- **H3 quality/risk:** integrating fundamental earnings, cash, valuation and event gates reduces poor entry outcomes without excluding every worthwhile candidate.
- **H5 macro utility:** a timestamped macro-to-company causal overlay improves decisions, risk handling or trade selection versus a **predeclared macro-blind baseline** using identical candidates. Falsifier: it adds no incremental value or causes more costly false vetoes.
- **H4 incremental utility:** the fully specified research decision workflow delivers more decision-useful and better **net risk-adjusted hypothetical outcomes** than a simple, low-effort baseline. Not claimed, to be tested.

Nulls are explicit: coiling may be noise; chart agreement may be poor; event/valuation gates may merely defer returns; a simpler rule may outperform. Treat adverse results as valid.

## Mandatory macro context before looking at candidate outcomes
Every prospective session must capture material contemporaneous information under [MACRO-PROSPECTIVE-001](macro-aware-equity-review.md): US nominal 2/10-year yields and real yields, yield-curve direction, oil/energy, inflation/labour and monetary events, credit/liquidity, FX, confirmed geopolitical/trade/election/regulatory developments, material shortages, sector relative strength, and explicit source/timing/uncertainty.

For each *material* macro factor, document **verified observation / expectation / scenario** separately; state the company's causal exposure, segment or cost/financing mechanism, time horizon, *potential priced-in effect*, contrary explanation and whether it changes the decision. **No post-hoc macro explanation is permitted to revise the original decision record.** If an input is not available, mark UNKNOWN; if no material change, record NO MATERIAL CHANGE with a dated check. Do not require a macro headline for each stock or use politics as an unverified market forecast.

**Macro comparison:** at each decision point freeze both the actual macro-aware research verdict and a simpler **counterfactual macro-blind verdict** using the same company, prices, earnings info and chart/fundamental criteria, *before* forward outcomes are known. Record cases macro overlay prevents adverse exposure AND where it falsely blocks a winner; avoid subjective retrospective explanations.

## EOD source tolerance (G0-DATA-002)
Use **<= $1.00 accepted / >$1.00 PRICE CHECK** only when comparing identical USD instrument, session and adjustment convention. Preserve independent SIGNAL_AMBIGUOUS for cases where small source difference crosses the research pivot/limit. Retain both source observations and compute indicators only from a consistently chosen canonical series **after authorised trial**; no Cherry-picked close. [Rule and D1–D6 provider validation](g0-price-tolerance-and-provider-trial.md). **No feed has been selected or historical bars fetched as of this amendment.**

## Sample design and point-in-time discipline
1. **Universe census:** daily record exchange session date, approved US listings, eligible count and number excluded by each filter. Retain symbols that delist or stop trading. Do not evaluate only the already-interesting 22 names or six external seeds; those are *convenience portfolios*, not unbiased discovery evidence.
2. **Sources:** Finviz contemporary A/B/C reports must be saved with exact settings and provider data cutoff (and entitlement restrictions). For systematic history use lawful OHLCV plus point-in-time earnings and fundamentals; **Finviz does not provide historical screener snapshots**. If no acceptable source, mark test BLOCKED and use only prospective manual observation.
3. **Timestamp:** record completed regular session and detection time in US/Eastern and UTC, source release time and retrieval time, including original macro release vintage and event date. Fiscal figures are usable only **after** public release. Weekend/holiday and after-hours reports have separate first-executable-session treatment.
4. **Snapshot freeze:** preserve before-outcome screen, chart stage, source, pivot, objections, valuation/earnings gate, BUY/WAIT/REJECT research opinion and next trigger. New facts create a later dated revision; never rewrite the original label.
5. **Complete cohort:** log screen names that fail manual verification, near misses, absent breakout days, names rejected by earnings, all WATCH candidates that never break out, delistings and missing-price outcomes. Group duplicate tickers rather than counting them as multiple independent wins.
6. **Reviewer blindness:** independent second reviewer receives same date-cutoff data, without the first reviewer's label or future prices. Compare breakout and watch-stage agreement; adjudicate disagreements with explicit rule changes for a *future* version only.

## Deterministic measurements and precise conventions
- Pre-breakout observed base: specify 20–60 prior completed sessions and independently verify at least two meaningful resistance contacts; adjustable/alternative bases require a dated documented exception.
- Volatility contraction candidate: mean daily (high−low)/previous close for completed last 10 sessions divided by mean over **immediately preceding 40** sessions (no overlap).
- Volume dry-up candidate: mean share volume last 10 completed sessions divided by **immediately preceding 40** sessions; handle split-adjusted volume consistently and mark earnings-distorted days.
- Current candidate pilot hints: range ratio <=0.75, volume ratio <=0.80, pivot distance 0–5% *below* resistance, 1.5x completed-session breakout volume. Each is **provisional**, not a proven buy signal.
- Relative price-strength metrics: compare stock/sector and stock/SPY ratio over aligned sessions; report sector/industry and market 1w/1m/3m context. Do not confuse RSI and relative strength.
- BREAKING OUT requires a real completed regular-session close beyond documented resistance with participation assessed; intraday-only cross remains WATCH. If volume is not supportive, record **lower-confidence** rather than asserting a clean signal.
- IN TREND requires sustained chart structure and SMA slope evidence; a one-day price above SMA50/200 does not prove trend.
- PEG defined only when comparable P/E earnings period and forward growth estimate are positive, interpretable and similarly dated. Unreliable/negative denominator => N/A; report durable cash, dilution and capex separately.
- Earnings gate counts **exchange sessions**, not calendar days; use company IR release time. Unknown => entry BLOCKED. News must have publication time before judgement.
- Classify discoveries and investment judgements separately; a strong chart does not clear economics or capital risk.

## Comparators to avoid self-deception
**Compare identical candidate entry clocks, exposure caps and cost assumptions**, or say the studies are not directly comparable:
- Market/sector benchmark purchased at the next actually executable session after signal.
- Same-day Finviz A/B/C cohort without the accumulation overlay (or unranked eligible names, on a predeclared sampling basis).
- Simpler rule: closing breakout above prior 20/55-day high or above SMA50/SMA200, with matched liquidity/earnings criteria.
- Optional random/sector-matched eligibility sample (seed recorded in advance) for discovery false-positive analysis.
- A separate long-horizon compounder study with appropriate holding window. Do not assess a 5-year business thesis only on 20-day price action.

## Outcomes, adverse selection and entry definition
Declare *before* observing outcomes: signal eligibility, reference price (e.g. following regular session **open** for after-close signal), whether confirmation/retest is required, maximum extension and stop/invalidation policy, what to do when entry gaps over a stated cap, expiry, optional sizing, all trading costs and FX, and how exits are modelled. If not frozen, report only **forward price movements**, not hypothetical trade returns or performance.

Track **5/20/60 regular-session** forward price return, time to breakout, volume/retest, peak-to-trough maximum adverse excursion and maximum favourable excursion (consistent OHLCV path), stop/gap effects, event exclusions, opportunity cost, turnover, gross/net model return and benchmark excess return where valid. Keep dividend-adjusted and raw series consistent and disclose the convention. Track poor cases at least as carefully as winners.

**Primary process scorecard:** reproducibility, missing critical data, chart reviewer agreement, event-gate violations, candidate burden per review, detection-to-decision latency and privacy breaches.
**Secondary signal scorecard:** share of WATCHs later breaking out, verified breakout follow-through, false breakout/reversal frequency, 5/20/60 excess return, adverse excursion and sample uncertainty.
**Tertiary portfolio scorecard:** mock equal-risk/equal-notional exposure, max drawdown, net CAGR/total return (only for sufficiently long horizons), concentrated sector risks, benchmark comparison and implementation costs.

## Gates and predeclared stopping rules
- **G0:** approve data/market scope, rulebook, **macro observation snapshot and transmission test**, horizon cohorts, fees/entry clock, baseline and pilot metrics. No tuning based on subsequent sample.
- **G1:** prospectively run macro dashboard and candidate research on provisional 20–30 completed US sessions; propose acceptance >=95% required fact completeness, 100% hard event-gate compliance, >=30 dual reviewed chart cases, explicit missing/UNKNOWN logging and manageable time. Critical missing event/time or misleading BUY is a FAIL regardless of percentage.
- **G2:** collect sufficiently mature forward returns for predeclared macro-aware AND macro-blind decisions across **multiple** cohorts, compare predeclared simple controls net of costs and report dispersion (not just averages). A small sample does not demonstrate statistical significance. If no detectable improvement, classify NOT PROVEN or REJECT, rather than soften criteria after results.
- **G3:** independently replicate the frozen process using **additional future observations**, with newly observed macro developments, independent challenge and a holdout prospective cohort. No historical backtesting is mandatory; historical business and crisis examples are qualitative context only. Version every tested adjustment; no p-hacking or hindsight regime narratives.
- **G4:** only after Architect/owner accept the measured evidence, permit a bounded requirement/WO for a **research-only** automation implementation. Broker execution requires new private governance and explicit authorisation, not this protocol.

**Current test status: NOT STARTED.** No validated extra return, hit rate, performance edge, false breakout rate, or measured 10/40 signal effectiveness exists today.

## Reporting and Git governance
For every prospective manual session, use [the dated worksheet](../templates/manual-equity-validation-review.md). Store non-identifying public observations with source links and exact UTC/exchange cutoffs under research/validation/. Preserve both candidate packet and reviewer disagreements, all rejects and no-signal days. When GitHub modifications are made fetch main HEAD, avoid overwriting peer changes, use expected SHA and verify readback. Private portfolio application never enters the repository.
