# AGENT-SYSTEM-001 — Evidence-led equity research and controlled execution architecture
**MACRO-PROSPECTIVE-001 (2026-11-05):** backtesting is **deferred/optional** during requirement validation. Future research would require a dated macro/sector/company transmission packet, but implementation remains BLOCKED until **independent forward evidence** meets revised G0–G4. See [macro doctrine](macro-aware-equity-review.md) and [decision](../research/decisions/2026-11-05-macro-aware-forward-validation.md).

**SUPERSEDED IMPLEMENTATION PRIORITY:** VALIDATION-FIRST-001 (2026-11-05) blocks all agent construction until an explicit G0–G3 proof review and G4 research-build permission. See [validation charter](research-process-validation-charter.md) and [decision](../research/decisions/2026-11-05-validation-first-freeze.md).

**Draft architecture adopted for design:** 2026-11-05, Europe/London. **Implementation state:** design only; no agent trading authority, broker connection or live execution has been created.

## Mission and principles
Build a repeatable, **point-in-time, audited equity opportunity pipeline**: completed market session → data-quality validation → technical/fundamental discovery → independent challenge → investment committee decision → independent capital/risk authorisation → broker-controlled execution → reconciliation, lifecycle monitoring and research feedback.

The goal is **high-quality decisions and risk-adjusted outcomes**, not the maximum number of tickers or trades. A credible NO BUY is a successful outcome. The system must challenge speculative business narratives and measure false signals as well as winners.

**Separation:** Research agents may run autonomously. They may NEVER authorise their own trades or raise their own risk ceilings. Any production broker access is **disabled by default**, and requires separately approved scope, jurisdiction/broker assessment, tests, risk limits and **explicit per-order human authority**. Broker connection does not confer discretionary mandate. Professional manager-held accounts may not support third-party API orders at all; treat them as **adviser execution** through a separate human process.

## High-level pipeline
1. **Post-close Data Intake:** exchange calendar and last completed session; OHLCV, adjusted dividends/splits, sector & industry membership, benchmark, fundamentals including as-of/publication dates, confirmed events, company primary filings/news. Preserve UTC and exchange time, source, release time, hash/version and licence.
2. **Data Quality Gate:** reject stale, inconsistent, missing, unadjusted or pre-release/asynchronous data; confirm ticker/currency, corporate actions, duplicate sources, primary versus vendor consensus and survivorship/delisting coverage. Mark unavailable metrics UNKNOWN; never fabricate completeness.
3. **Deterministic Discovery:** preserve original Finviz QARP A/B/C screens; do not confuse a proprietary Finviz UI scan with our own replicate. Maintain distinct exception/strategic-compounder pass. Calculate SMA/relative-strength/price+volume contractions, 20–60-session base and resistance, pivot proximity, completed close breakouts; tag historical timestamps. Trial parameters remain unvalidated until prospectively evaluated.
4. **Sector and Regime:** record GICS-style actual sector + industry, sector and stock relative return vs S&P 500 (1w/1m/3m), breadth and market/volatility/credit/earnings regime. Sector fear does not automatically exclude exceptional businesses.
5. **Fundamental Qualification:** sources and latest 3–5 year economics: ROIC, margins, gross/organic revenue and EPS growth, after-capex cash flow and conversion, diluted shares, leverage, maturity and valuation. Forward P/E, PEG, EV/EBIT, P/FCF, FCF yield as relevant, and sector-specific alternatives (AFFO for REITs, normalised commodity cash flows, financial institution capital, utilities' allowed returns). PEG is conditional on reliable, consistent earnings-growth definitions; a low PEG by itself is not an investment thesis.
6. **Event/News Agent:** confirm earnings release date AND exchange-local release time from issuer sources; apply existing **7 exchange trading sessions before, release date, 2 complete regular sessions after** buying/addition gate, plus material-event holds. Classify news by materiality, source/date and actual thesis effect; do not allow AI to invent unannounced earnings or treat headlines as economic facts.
7. **Independent Challenge and Rank:** adversarial critic must identify the two best contrary explanations, structural capital impairment risk, bear/base/bull after-capex owner cash flow, valuation at current price, sector concentration, extended entry and alternative candidates. Agents should not simply validate the previous agent's prose. Rank priority with documented reasons and uncertainty, never a pseudo-precise confidence score from incomplete data.
8. **Candidate Pack:** present a limited prioritised queue by **BREAKING OUT, IN TREND, WATCH (BASE FORMING/COILING/AT PIVOT)**. Preserve **A/B/C eligibility** and **NOW/LATER investment readiness** as separate fields. Produce review-ready structured evidence, a chart and decision trigger; reject or disclose missing critical data.
9. **Investment Committee:** research sponsor and independent research architect review **business, chart, news, valuation, risk, portfolio overlap and contrary evidence**. Outcomes: BUY STARTER / BUY FULL (research verdict only), WAIT with trigger, REJECT. No automatic authorisation is inferred from a conversational conclusion.
10. **Separate Risk/Order Controller:** after a distinct human approval of a specific order, a deterministic controller verifies current holdings, buying power, intended exposure, authorised notional/quantity, price and slippage bounds, earnings and material event status, freshness, trading calendar, restricted instruments, kill switch and broker rules. If any check fails, fail closed.
11. **Broker Execution (later gated stage):** only execute an explicit, time-limited, immutable human-signed order ticket; prevent duplicate/replayed requests, capture acknowledgement, order/fill/cancel events, preserve an auditable state machine and reconcile with broker records. No broker secret exposed to LLMs.
12. **Monitoring and Learning:** reconcile positions/cash, FX, fees and dividends; monitor thesis deterioration, risk and events; track actual net performance separately from research hypothetical returns, SPY and sector benchmarks, 5/20/60-session forward performance, maximum adverse excursion, slippage, false breakout rate and drawdown. Feed *measured* errors back to candidate-screen calibration under versioned review, never hidden self-modification.

## Roles and trust boundaries
| Role / component | Allowed responsibilities | Prohibited |
|---|---|---|
| **Orchestrator / workflow controller** | Schedule, verify data completeness and step status, publish candidate packages, log evidence | Create or approve order mandates |
| **Market ETL / deterministic feature engine** | Fetch licensed data and compute reproducible OHLCV and ratios | Invent data, call a screenshot a complete screen |
| **Scout agents** | Propose charts from Finviz A/B/C and base-pattern evidence; sector-relative analysis | Assert verified breakout without completed close+volume |
| **Fundamental and events agents** | Verify statements, value scenarios and company calendar; classify primary vs secondary evidence | Clear earnings restrictions without confirmed release time |
| **Independent critic** | Seek contradiction, assess permanent-loss cases and alternative opportunity cost | Approve its own research conclusion without evidence |
| **Research committee** | Determine investability and which candidate gets further attention | Automatically create executable broker mandates |
| **Capital-risk service (non-LLM)** | Independently enforce immutable approved limits and approval signature | Accept edits from scouts or a persuasive text prompt |
| **Execution adapter (non-LLM)** | Submit only cleared signed tickets, reconcile fills, cancel/stop on control failure | Select tickers, raise limits, retry ambiguous orders blindly |
| **Portfolio monitor** | Reconcile actual positions/transactions and detect thesis/risk drift; expose failures | Silently trade or replace a user's approved strategy |

**Security:** public filings and scraped web content are untrusted prompt/data inputs. They must never be interpreted as privileged agent instructions. AI agents receive read-only public research data and constrained tool access. Strong separation for service credentials, broker tokens, approval keys and private data; role-based permissions, immutable audit events, idempotent tasks, retry policies and independent security tests.

## Two independent decision records
- **Public research dossier:** sources, sector, chart classification, watch/valuation, date, process methodology and non-identifying views. Public GitHub allowed; never include private positions, planned allocations, advice correspondence or order intent.
- **Private investment/order record:** suitable for a **separate private repository and encrypted, restricted-access database**. Includes actual account identities, liquidity commitments, risk budgets, signed approvals, broker events, holdings, P&L and tax-sensitive records. Do not copy into public GitHub through metadata, examples, screenshots or commit messages.

## Candidate progression states
DISCOVERED → DATA VALIDATED → CHART/FUNDAMENTALS REVIEWED → INDEPENDENT CHALLENGE PASSED → COMMITTEE REVIEW → WATCH/REJECT or APPROVED RESEARCH → PRIVATE RISK APPROVAL → AUTHORISED ORDER → ORDER SUBMITTED → RECONCILED → MONITORED.

**A technical BREAKING OUT is not "APPROVED RESEARCH" and APPROVED RESEARCH is not an authorised order.** Missing material data, stale price, unverified calendar, broken thesis or missing approval must produce a clear HOLD/FAIL state.

## MVP sequencing — don't build the broker adapter first
**Phase 0 — contracts and proof of data rights:** define evidence schema, as-of validity, accurate exchange calendar, sector taxonomy, completed-bar OHLCV provider, data entitlement, historical replay with splits/dividends and benchmark. Agree definition of "world-class" before model fitting.
**Phase 1 — research-only automated scout:** source -> deterministic features -> sector/event quality -> 3–10 evidence-backed candidate briefs, full candidate/reject log, dated GitHub public summaries. Never trade. Reconcile screen eligibility and chart stage manually during acceptance.
**Phase 2 — prospective shadow portfolio and paper trade:** maintain original public research baseline and private synthetic decisions at prices actually executable **after** detection time, include dividends/FX/fees/spread/slippage assumptions, trades missed and delistings. Paper trading must exercise duplicate prevention, partial fills, cancellations and outages. Minimum evidence target: **20 completed US sessions and 50 simulated order lifecycle cases**; these are initial test gates, not proof of expected investment alpha.
**Phase 3 — supervised live pilot, separate owner approval:** requires broker suitability/legal review, signed risk and order contracts, independent audit/DevSecOps, working kill switch, accurate reconciler, documented rollback and user approval for each bounded order. Prefer broker/provider orders via licensed/advised channel as applicable. No unattended discretionary trading.
**Phase 4 — expansion only on evidence:** compare historical and prospective signal quality to market and sector benchmarks, adverse selection, drawdowns, false positives, net return and operational reliability. Unattended orders remain **out of scope** unless a new explicit governing decision authorises them and all required legal, broker, risk and audit gates pass.

No phase may claim success from tests alone. Define separate go/no-go decisions, exact artefacts and acceptance for each stage; failure means pause or revert.

## Operational controls before any live order
- Order ticket has instrument identifier/exchange, side, quantity or notional, order type, strict limit, allowed trading session, expiry and provenance, authorising human, approving risk-check version, maximum exposure, no-margin flag, unique idempotency key and hash.
- Recheck at point of submission: latest broker holdings/exposure, cash, FX, aggregate correlated sector exposure, earnings/other event status, current quote freshness, halt/circuit breaker, price collar, maximum daily loss and drawdown. Unknown state => HOLD.
- Service-specific **kill switch** defaults engaged on connection loss, stale data, unexpected fills, broker mismatch, breach or audit/logging outage. A stop-loss order is not equivalent to a kill switch; either can fail during gaps. Escalate uncertain broker responses rather than duplicate.
- Broker acknowledgements are **not fills**. Track partial fills, rejections, replacements, cancellations, fees, corporate actions and end-of-day independent reconciliation. No agent may infer shares were bought from an HTTP 200.
- Approved accounts may differ: an externally managed portfolio may need an adviser instruction instead of API execution. System must not route across custody/account boundaries without explicit authority.

## Performance scorecard
| Dimension | Measurement | Why |
|---|---|---|
| **Research coverage** | Universe scanned, candidates filtered, factual completeness, sector balance, age of data | Avoid cherry-picking |
| **Signal utility** | False breakout rate, time identified before pivot, 5/20/60-session forward return, maximum adverse excursion, precision of WATCH→BREAKING OUT promotions | Measure whether early scouting adds value |
| **Investment quality** | Expected vs realised cash flow, bear/base/bull error, probability of permanent-loss events, conviction change | Don't mistake charts for economics |
| **Portfolio risk** | Drawdown, volatility, overlap/correlation, sector/FX concentration, liquidity consumed, scenario loss | Protect capital |
| **Execution** | Fill rate, implementation shortfall vs arrival price, slippage/fees/FX, duplicates rejected, unreconciled events, rejects and emergency stops | Measure actual trading quality |
| **Net investment outcome** | Benchmark/sector-relative net total return, time-weighted and money-weighted results appropriately, turnover and tax-relevant adjustments | Capital compounding, not vanity win rate |

Use post-close decision timestamps and earliest following executable session for prospective return studies; account for US/UK daylight-saving differences and market holidays. Store missing data explicitly. This design uses risk-control *principles* found in [FCA algorithmic trading systems guidance](https://handbook.fca.org.uk/handbook/mar7a/mar7as3), [FCA review of algorithmic trading controls](https://www.fca.org.uk/publications/multi-firm-reviews/algorithmic-trading-controls-high-level-observations), and [SEC Market Access Rule](https://www.sec.gov/rules-regulations/2011/06/risk-management-controls-brokers-or-dealers-market-access). **Specific legal applicability depends on the firm, account, broker and jurisdiction and needs separate review.**

## Next architecture decisions
1. Choose **licensed OHLCV and fundamentals feeds** and test historical replay, point-in-time statements, corporate action handling and ability to satisfy Finviz A/B/C without breach of terms.
2. Define **candidate JSON/schema**, evidence source type, freshness/UNKNOWN semantics and reproducible calculated features. See [candidate contract](candidate-evidence-contract.md).
3. Choose quality criteria and ranking evaluation metrics without overfitting; pilot across all 22 tracked names plus external scout leads.
4. Specify the private database and execution-authority contract separately, after deciding whether any actual account supports broker API orders.
5. Prove **daily scout** works as research-only before wiring execution; track latest GitHub/main and never overwrite concurrent commits.

## Related work
[Daily research runbook](daily-equity-scout-runbook.md), [Finviz v2](finviz-filters.md), [SCOUT-001](pre-breakout-accumulation-scout.md), [CHART-001](chart-stage-classification.md), [Independent Challenge](independent-investment-challenge.md), [Decision-to-invest](decision-to-invest.md), [Performance tracking](outcome-tracking.md), [public architecture adoption](../research/decisions/2026-11-05-agent-investment-system-architecture.md).
