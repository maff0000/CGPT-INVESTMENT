# Changelog
Record material research-process changes and link dated decisions. Do not rewrite earlier observations.

## 2026-11-05 — G0-DATA-002: $1 discrepancy tolerance and practical EOD provider acceptance route
- Adopted precisely **abs(vendor close A − B) <=$1.00 accepted with no PRICE CHECK; >$1.00 flagged** for same USD instrument/session/adjustment. A straddled critical pivot independently triggers **SIGNAL_AMBIGUOUS**, not a routine quote flag. Missing date/split/currency integrity = DATA_MISMATCH.
- Retested historical XOM/LIN/EQIX discrepancy examples **$0.03/$0.17/$0.16: all PRICE_OK**; superseded over-escalation in G0-DATA-001.
- Sourced official **Massive grouped OHLCV/Basic next-day data availability**, **Tiingo raw+adjusted EOD/corrections** and **EODHD** plan alternatives; licensing, API account and actual bar integrity remain UNVERIFIED.
- Added [G0-DATA-002 price/provider test policy](docs/g0-price-tolerance-and-provider-trial.md), [manual test worksheet](templates/g0-price-source-comparison.md) and [decision](research/decisions/2026-11-05-price-tolerance-provider-trial.md). No G0 freeze, no G1 or agent implementation.


## 2026-11-05 — G0-CROSS-SECTOR-001 company, price and valuation trial
- Documented [three-company diagnostic](research/validation/2026-11-05-cross-sector-company-dry-run.md): XOM, LIN, EQIX, issuer Q3 releases, Nov4 price evidence and macro transmission.
- Found small conflicting close quotes and industry-incomparable PE/PEG/FCF rules; proposed [source and sector valuation governance](docs/g0-data-integrity-and-valuation-rules.md) and [decision](research/decisions/2026-11-05-cross-sector-company-dry-run.md).
- No valid chart classification, Finviz A/B/C export, earnings-gate approval or fair-value buy conclusion; all three WAIT pending data. G0 not yet frozen, G1 not started, no agent/broker work.


## 2026-11-05 — G0-MACRO-001: first actual dated macro observation, not proof of selection rules
- Completed [manual macro dry-run](research/validation/2026-11-05-macro-g0-dry-run.md) for Nov4 US close, reporting Treasury 2/10yr nominal yield, secondary 10yr TIPS, Fed, Sep CPI/PCE, credit as of Nov3, Nov4 Brent/WTI, elections, sector ETFs, next BLS releases.
- Drew conditional causal tests for actual research-sector exposures rather than treating the market rally or oil decline as an automatic buy. Documented different data cutoffs, primary-vs-secondary evidence, unknown physical shortages and missing contemporaneous sector return periods.
- [G0 trial decision](research/decisions/2026-11-05-macro-g0-dry-run.md): regime MIXED/EVENT-DRIVEN/SELECTIVE, **G0 still open, no G1/agent approvals or trades**, and missing macro data/issuer economics before a proper investment review.


## 2026-11-05 — MACRO-PROSPECTIVE-001: macro-aware in-time research, defer mandatory backtesting
- Adopted **contemporaneous, prospective** equity-selection requirements rather than mandatory retrospective backtesting; historical cases remain business context, not claimed performance validation.
- Created [macro-aware review doctrine](docs/macro-aware-equity-review.md) and [dated G0–G4 validation amendment](research/decisions/2026-11-05-macro-aware-forward-validation.md), including rates/real yields, commodities, macro calendars, credit/FX, geopolitics/policy and supply bottlenecks.
- Each relevant macro factor now requires source/timestamp, company-specific causal channel, exposure/time horizon, contrary case, and assessment of what may already be priced in.
- Updated [manual test protocol](docs/research-validation-protocol.md), [requirements](docs/research-process-validation-charter.md), and [worksheet](templates/manual-equity-validation-review.md): G3 **independent forward replication**, G2 prospective macro-adjusted vs predeclared macro-blind baseline; no historic backtest gate. Agents remain unapproved; daily scout remains paused.


## 2026-11-05 — VALIDATION-FIRST-001: prove requirements before agents
- Declared the Finviz v2 A/B/C, pre-breakout accumulation proxy, chart classifications and research verdict processes **unvalidated hypotheses**, not a known statistical edge; blocked AGENT-SYSTEM-001 build work.
- Published the [manual validation charter](docs/research-process-validation-charter.md), [prospective test protocol](docs/research-validation-protocol.md), [daily review worksheet](templates/manual-equity-validation-review.md) and [formal freeze](research/decisions/2026-11-05-validation-first-freeze.md). Established G0 specification freeze → G1 reproducibility → G2 comparative prospective outcomes → G3 independent replication → G4 explicit research-only automation go/no-go.
- Verified Finviz's official note that **historical screener results are unavailable**; require contemporaneous archives or licensed point-in-time sources for credible outcomes. Prevent survivorship/look-ahead, cherry-picking and post-hoc tuning.
- **Paused** previously enabled US Close Equity Scout recurring research automation while defining and proving the manual requirements. Monday all-sector idea research remains separate. No broker order, implementation WO, private investment data or agent build authority.


## 2026-11-05 — AGENT-SYSTEM-001: end-to-end research architecture, governance and evidence contracts
- Documented staged **post-close data validation → deterministic discovery → sector/fundamental/event/challenge research → human committee → distinct risk/order authorisation → broker execution (future) → reconciliation and outcome learning**.
- Added [architecture and phased delivery](docs/agent-equity-operating-system.md), [public candidate evidence contract](docs/candidate-evidence-contract.md), [execution/governance boundary](docs/execution-authorisation-boundary.md), and [architecture decision](research/decisions/2026-11-05-agent-investment-system-architecture.md).
- **No live execution approval, broker API setup, investment orders or portfolio details**. Existing Finviz A/B/C, WATCH/COILING/BREAKING OUT/IN TREND, 7+2 earnings, independent owner-conviction checks and daily scouting remain unchanged. Research shadow/paper/reconciler acceptance precedes any supervised live consideration.


## 2026-11-05 — DAILY-SCOUT-001: weekday research task and durable handoff
- Confirmed a **weekday after-US-close equity scouting research task** is enabled, **separate** from the Monday >=7 all-sector report. Scheduled task creation does not establish future completed reports, actual market-data coverage or GitHub writes.
- Added [operating and continuation runbook](docs/daily-equity-scout-runbook.md) and [decision](research/decisions/2026-11-05-daily-scout-operating-plan.md), with the exact recovery read order and SCOUT-002 pilot lessons.
- Each future report must validate the completed US session, highlight confirmed and unconfirmed chart conditions, sector and business risk, 7+2 earnings gate and independent decision. Record dated findings in GitHub only with verified permissions and readback; otherwise disclose absent commit.
- No new trades, personal portfolio information, scan claims or unverified backtested returns added.


## 2026-11-05 — SCOUT-002: first practical pre-breakout scan and live event gate checks
- Piloted the new [scouting workflow](research/reviews/2026-11-05-first-pre-breakout-pilot.md) against six named public VCP-screen leads from Nov2 scanner prices, updated to Nov4 completed US session closes, with sector, primary earnings and preliminary business checks.
- SJM was near an old resistance, CPAY and VOYA beyond old pivots, ABNB did not close above its pivot; BDX extended into results and DE faces Nov25 earnings. **None rated an executable BUY**.
- Existing EME/ALGN thresholds tested against new prices and adverse/positive price moves; neither historical price condition is a standing order. No personal finance disclosed or broker action.
- [SCOUT-002 decision](research/decisions/2026-11-05-first-pre-breakout-pilot.md); strict caveat: **no Finviz or full 22-company scan, no independently calculated 10/40 contraction ratios**. New names are leads only, preserving current active universe.


## 2026-11-05 — SCOUT-001: find tightening bases before momentum
- Added a separate, non-mandatory pre-breakout scouting route: QARP **A** plus explicit exceptions, before momentum screens B/C, with **WATCH / BASE FORMING, COILING, AT PIVOT** substages.
- Differentiated Finviz **Volatility / Relative Volume / chart Pattern** snapshots from actual **historical contraction and volume dry-up**. Proposed prospective 10-versus-prior-40-session features, support/resistance, stock/sector RS, misleading-signal checks and outcome logging.
- Confirmed Finviz's **Screener Charts view, Elite advanced filters and Find Similar Charts** as useful scout aids subject to availability. No live scan, OHLCV ingestion or stock reclassification is claimed.
- Documented [method](docs/pre-breakout-accumulation-scout.md) and [dated decision](research/decisions/2026-11-05-pre-breakout-scout.md). All v2 A/B/C and previous chart/investment gates preserved.

## 2026-11-05 — CHART-001: Breaking Out, In Trend and Watch
- Preserved QARP Discovery v2 A/B/C filters and added **independent chart stages**, with BREAKING OUT first priority for buy/WAIT review, not automatic purchase.
- Made actual sector/industry, relative sector strength, SMA slopes, volume, documented resistance and separate economic/earnings decision mandatory for a classification.
- Recorded exploratory Finviz Pattern/near-high/relative-volume overlays and an initial [22-company audit queue](research/watchlists/2026-11-05-chart-stage-audit.md). **All chart stages currently pending verification**; no live chart audit or broker trades.
- Canonical [methodology](docs/chart-stage-classification.md) and [decision](research/decisions/2026-11-05-chart-stage-pipeline.md).


## 2026-11-04 — Current 22-company inventory and sector classification
- Verified historical 13-company three-sector discovery list and 9-name all-sector list = **22 unique active names**, across **11 actual sectors**.
- **OLLI** remained historically filed in the Consumer Defensive discovery cohort but independent GICS-style business profiles classify it **Consumer Discretionary / Broadline Retail**, contrary to another vendor's Consumer Staples classification; recorded classification discrepancy and preserved original dated lists. See [classification note](docs/sector-rotation.md).

## 2026-11-03 — PUBLIC-001: non-identifying investment collaboration agreement
- Published a concise [working agreement](docs/independent-research-relationship.md) defining the independent-research relationship and constructive disagreement, using only a generic anonymised example.
- Strengthened the public-write check to exclude investor-specific preferences, portfolio circumstances, private decision thresholds, proposed orders and personal conversation excerpts. Existing dated research is preserved; no history rewriting or public disclosure of personal facts was performed.

## 2026-11-03 — INDEPENDENT-001: challenge conviction, prohibit narrative-led endorsements
- Owner explicitly requires the Architect to **challenge enthusiasm with evidence-based investment protocol rather than follow unsupported perceptions**.
- Added mandatory six-stage independent challenge process, source grades, contradictory evidence requirement, after-capex valuation, risk permissions, and dissenting BUY/WAIT/REJECT verdicts.
- [Alphabet claim-evidence challenge](research/reviews/2026-11-03-alphabet-claim-evidence-challenge.md): Google AI/Search/TPU strengths verified; necessary OpenAI/Anthropic search dependence, exclusive Cloudflare partnership and near-term quantum earnings **not verified**; Cloudflare/OpenAI pilot and regulatory remedies are contrary evidence.
- Preserved prior dated conviction/entry records as history, while clarifying **strong strategic business thesis != current purchase endorsement**. No private holdings or instructions published.

## 2026-11-03 — STRATEGIC-004: Alphabet vs Microsoft/Amazon, early-entry thesis
- Recorded the owner's greater business conviction in **GOOGL relative to MSFT and AMZN**, with 2026 Q3/2027 Q1 primary operating evidence, Nov 3 indicative forward multiples, downside scenarios and the distinction between **a 40% sector decline, a 40% share decline from an earlier peak and a fresh 40% share decline**.
- Corrected six-month GOOGL historical price change to approximately **−27%** (May 1 reference to Nov 3), subject to the vendor's recorded close.
- A limited initial strategic-entry research opinion is conditionally acceptable **without obliging later averaging down or exhausting opportunity reserves**; no amount or private portfolio information entered. See [decision record](research/decisions/2026-11-03-alphabet-relative-conviction-entry.md).

## 2026-11-03 — STRATEGIC-003 / OPPORTUNITY-RESERVE-001: full-stack Alphabet and dry-powder doctrine
- Recorded Alphabet's **full-stack AI business thesis** spanning index/discovery, distribution, Search monetisation, custom TPU chips, models and enterprise Cloud. Flagged capex/FCF, AI search ad-yield and regulatory failure cases; thesis is owner conviction, not a price-independent approved buy.
- Clarified **gilt/liquidity reserves as potential funding for long-term equities and market dislocations**, not a permanently ring-fenced defensive allocation. Added anti-mechanical laddering policy: market regime + company fundamentals + refreshed valuation + liquidity/correlation budget must all permit each tranche.
- New [GOOGL thesis](research/decisions/2026-11-03-alphabet-full-stack-thesis.md), [reserve policy](docs/opportunity-reserve-deployment.md) and [dated clarification](research/decisions/2026-11-03-opportunity-reserve-clarification.md). No account amounts or positions published.

## 2026-11-03 — STRATEGIC-002: staged accumulation methodology
- Added a **public, generic staged-acquisition framework** for long-horizon strategic equities, with portfolio concentration and liquidity checks preceding any position increase.
- Documented illustrative **35%/30%/35%** tranches, conditional rather than automatic purchases, post-earnings validation, downside stress and reasons to stop additional buys.
- The strategy records **no personal holdings, cost basis, current losses, manager identity, approved amounts or trades**. See [framework](docs/strategic-staged-accumulation.md) and [dated record](research/decisions/2026-11-03-alphabet-staged-framework.md).

## 2026-11-03 — STRATEGY-001: three complementary investment mandates
- Adopted **strategic 5–10-year compounders**, **immediate measured-risk opportunities**, and **future candidates** as three complementary outcomes. Strategy horizon and **NOW/LATER entry status are separate**, so long-term ownership does not require positive short-term sector momentum nor permit price-independent purchases.
- Made [investment strategy](docs/investment-strategy.md) canonical, with [adopted decision record](research/decisions/2026-11-03-three-mandate-strategy.md). Updated README, AGENTS, CURRENT-STATE and near-term action policy. Preserved the existing GOOGL conviction, prior dated records and independent research.
- All-sector weekly minimum **7 evidenced investment ideas**, the 7+2 earnings policy, risk/valuation checks and no-execution boundaries unchanged.

## 2026-11-03 — STRATEGIC-001: Alphabet long-horizon preference
- Owner expressed **long-term strategic ownership interest in Alphabet/GOOGL via professional wealth management**, separate from tactical sector rotation.
- Documented [GOOGL thesis and diligence requirements](research/decisions/2026-11-03-alphabet-long-term.md): Q3 cash flow, $195–205bn 2026 capex guidance, rising expected 2027 capex, Search disruption and Cloud growth, valuation, concentration and staged-entry review.
- **No purchase, allocation, pricing instruction or portfolio disclosure**; original weekly all-sector nine-name list and unrelated Claude research untouched.

## 2026-11-03 — Weekly All-Sector research automation enabled
- Created and confirmed a recurring **Monday morning Europe/London** ChatGPT task for at least seven verified investment research ideas per week, first run expected 2026-11-09.
- The task attempts GitHub append only when appropriate connector access is present; **a schedule is not evidence of successful future research or commit**. No trading or broker actions are configured.

## 2026-11-03 — ALL-SECTOR-001: weekly seven-plus opportunity programme
- Added a **parallel** search across all eight sectors beyond the three existing priority lanes; target **>=7 substantiated potential investments per week**, not seven purchases or manufactured ideas.
- Established explicit **AI second-phase/AI adoption/agentic security** lens with a quality+price+event requirement and an independent non-AI control.
- First pilot selected **nine distinct public companies in eight sectors**: NET, ZS, GOOGL, V, BKNG, NEE, LIN, EQIX, XOM. NET/BKNG are earnings blocked; other names have named valuation/event risks. Not strict QARP v2 screen passes by default.
- Wrote [policy](docs/all-sector-opportunity-pipeline.md), [decision](research/decisions/2026-11-03-all-sector-expansion.md), [pilot](research/reviews/2026-11-03-all-sector-pilot.md), [watchlist](research/watchlists/2026-11-03-all-sector-09.md) and [sources](research/sources/2026-11-03-all-sector-evidence.md).

## 2026-11-03 — ACTION-003/004: complete bounded Industrial and Consumer Defensive comparison
- Evaluated EME vs GEV using primary Q3 filings, FY2027 adjusted EPS forecasts, hypothetical bear/base/bull scenarios, and earnings/other-event gates.
- **EME conditional BUY STARTER <=$700** with new quote/calendar/correlation checks; **GEV WAIT** after exceptional demand and customer advance/deposit cash effects, plus $9bn announced Trench deal.
- Expanded established Consumer Defensive sector search with **UL and CCEP** as active monitored candidates; UL **Nov 4 Investor Event hold**, CCEP **Nov 3 results two-session cooling hold**. CLX rejected as misleading earnings rebound; PG evaluated but not advanced.
- Added `CURRENT-STATE.md`, dated decision records, up-to-date 13-name watchlist and evidence references. No transactions and no private holdings.
- Initial bounded decision work concluded. Await owner's **planned final process stage** before any additional architecture/implementation.

## 2026-11-03 — ACTION-002: price-aware NOW decisions in the two established sectors
- Completed an initial comparative earnings/valuation/risk review for **ALGN vs ISRG** (Healthcare) and **MDLZ vs PEP vs OLLI** (Consumer Defensive), using cited dated public financial releases and quotes.
- **ALGN conditional BUY STARTER at <=$155** with explicit downside and new earnings calendar check; **ISRG WAIT <=$375**. None of the three Defensive names passes near-term upside/downside: **MDLZ WAIT <=$58, PEP WAIT <=$125, OLLI WAIT <=$78 plus underlying comp-sales recovery**. Limits are analyst research hypotheses, not orders.
- Recorded transparent 12–18-month adjusted-EPS × hypothetical terminal-P/E bear/base/bull *sensitivity cases*, not discounted intrinsic values, and separate price/event limitations. No financial trade, broker instruction or portfolio data.
- Added [event scheduling clarification](research/decisions/2026-11-03-earnings-scheduling-clarification.md) (v1.2): a newly reported company with no next calendar date can be reviewed conditionally on a same-day IR check rather than be frozen for months; 7+2 safety windows unchanged.
- See [decision review](research/reviews/2026-11-03-invest-now-two-lanes.md) and [action queue](research/watchlists/2026-11-03-now-later-decisions.md).

## 2026-11-03 — Two owner-nominated premium-valuation businesses
- Explicitly documented that **Healthcare and Consumer Defensive have been screened but not yet fully evaluated for purchase decisions**.
- Added Intuitive Surgical (ISRG) to Healthcare and GE Vernova (GEV) to Industrials. Both fail v2 forward P/E <25 and are labelled exceptions, not screen hits.
- Reviewed company Q3 releases and stock valuations. GEV's strong FCF is substantially influenced by customer advance payments; do not mistake headline FCF for sustainable owner earnings.
- Preserved the original nine-name watchlist and established an eleven-name updated snapshot. See [sector and premium-candidate review](research/reviews/2026-11-03-two-sector-and-premium-candidates.md).

## 2026-11-03 — ACTION-001: Now vs Later, measured investment risk
- User corrected excessive research-only drift: pursue **immediate purchases as well as future candidates**.
- Adopted two decision queues (NOW/LATER) and explicit BUY STARTER / BUY FULL / WAIT / REJECT verdicts; retain seven-plus-two earnings gate and no auto-execution.
- Added [decision-to-invest](docs/decision-to-invest.md), [decision record](research/decisions/2026-11-03-investment-urgency.md), [investment template](templates/investment-decision.md), [ranked decision desk](research/reviews/2026-11-03-investment-decision-desk.md) and [queue](research/watchlists/2026-11-03-investment-priority.md).
- First live near-term candidates: ALGN, EME and MDLZ; all decisions conditional on intraday quotes and unverified future events; no trades executed.

## 2026-11-03 — Event update 02: ADMA and FERG verification
- Confirmed ADMA November 4 after-close Q3 release and Ferguson November 9 6:45 AM ET Q3 release against their corporate announcements.
- Recorded both as PRE-EARNINGS BLOCK and updated the dated watchlist without altering the bootstrap baseline. See [event review](research/reviews/2026-11-03-events-02.md).

## 2026-11-03 — Cycle 01: earnings gate adopted and primary-source company checks
- Corrected previously mis-recovered five-session blackout to the **agreed seven exchange-trading-session pre-earnings block**; preserved the two-full-session post-release rule. The original founding record is retained unchanged; see [decision amendment](research/decisions/2026-11-03-earnings-gate-adoption.md).
- Verified published earnings dates for ZWS, MDLZ and GMED, and selected company-release metrics; documented first [research cycle](research/reviews/2026-11-03-cycle-01.md).
- Created initial ZWS, MDLZ and GMED dossiers with missing price/valuation evidence clearly labelled UNKNOWN; no entry approval or investment claim.

## 2026-11-03 — Initial framework
- Established public QARP research journal and continuity instructions.
- Recovered Discovery v2 as current baseline; retained original and refined v1 presets as history.
- Preserved one emerging / two established sector lanes and nine original research candidates.
- Recorded historical sector and stock observations as REPORTED, with no independent market verification claimed.
- Documented earnings/event gates, daily/weekly reviews, provenance and prospective outcomes.
- Added reusable research templates and initial decisions, sector assessment, watchlist, source register and handoff.
- Marked numerical earnings window, scoring and outcome horizons PROPOSED; left missing inputs UNKNOWN.

See [founding decisions](research/decisions/2026-11-03.md).
