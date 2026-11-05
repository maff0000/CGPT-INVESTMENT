# DAILY-SCOUT-001 — After-US-close equity scouting runbook
**Adopted:** 2026-11-05 (Europe/London) | **Current status:** previously scheduled recurring scout is **PAUSED** under [VALIDATION-FIRST-001](research-process-validation-charter.md). This runbook is a future execution reference, not permission to run an unvalidated automated pipeline.

## Purpose
Operate a **repeatable research and decision desk** for early-stage bases, coiling/at-pivot stocks, completed breakouts and still-investable trend continuations. Keep discovery independent of investment endorsement. A high-quality chart is not a great business at any price.

**Scheduling:** a weekday after-US-close ChatGPT research task was created but is **currently paused** while manual criteria and outcomes are validated. It is distinct from the established Monday weekly all-sector idea process; neither replaces the other. A scheduled task **is not proof** that future results, OHLCV data access or GitHub writes will be available. Never claim a nightly report exists without checking the actual dated output and GitHub HEAD.

## Authoritative read order for new sessions
1. [README](../README.md), [agent rules](../AGENTS.md) and [current state](../CURRENT-STATE.md).
2. [Independent investment challenge](independent-investment-challenge.md), [QARP Finviz A/B/C baseline](finviz-filters.md).
3. [Chart-stage definitions](chart-stage-classification.md), [pre-breakout discovery](pre-breakout-accumulation-scout.md), [investment action decision rule](decision-to-invest.md), [earnings and event gates](earnings-risk-gates.md).
4. [Current 22-name chart audit](../research/watchlists/2026-11-05-chart-stage-audit.md) plus any **newer dated** charts, reviews and decisions.
5. [First six-candidate pilot](../research/reviews/2026-11-05-first-pre-breakout-pilot.md), [pilot conclusion](../research/decisions/2026-11-05-first-pre-breakout-pilot.md), and *then* subsequent daily reports. Never treat initial historic prices/pivots as live.

## After-close operating loop
1. **Session guard:** confirm a completed US regular trading day, close timestamp and holiday/calendar. If none, say **NO NEW SESSION**; do not create fictional price moves.
2. **Universe:** preserve 22 established research names and research a few additional *external scouting leads*. New scanner names are **not** automatic additions to qualified QARP universe. Continue separate weekly >=7 all-sector work.
3. **Screen:** use Finviz A/B/C as documented **without tightening the core filters**. Search promising A-level recoveries, B/C near-breakouts and named compounder exceptions; record any data/vendor limitations and which source actually produced each candidate. **Do not claim a Finviz export if only an external scanner or web sources were used.**
4. **Classify only on verified charts:** maintain distinct **Finviz membership**, **chart stage**, and **investment decision**. Inside WATCH distinguish BASE FORMING, COILING, AT PIVOT. BREAKING OUT requires a verified regular-session close over *independently checked* resistance; IN TREND requires sustained structural evidence. Missing OHLCV = CHART PENDING, never invented status.
5. **Sector context:** actual sector/industry, sector-relative 1w/1m/3m trend vs S&P 500 and stock relative strength. Sector weakness informs risk but cannot automatically exclude early industry leaders.
6. **Setup evidence:** quote and trading date, support/resistance/pivot, SMA50/SMA200 levels and slope if available, price extension, completed-session volume, relative volume and (if historical data permits) last-10 vs prior-40 completed-session price-range and volume contraction. Label ratios **UNKNOWN** if not computed; a scanner-provided pivot is an **unverified candidate reference** until checked.
7. **Independent economic decision:** price-aware quality/valuation/downside, balance sheet, contradictory evidence and company events. **No initiation in seven exchange trading sessions before earnings plus announcement day; wait two complete sessions afterwards**, unless a longer material-event hold is warranted. Produce a small ranked BUY STARTER / WAIT with trigger / REJECT desk; **zero buys is a valid result**.
8. **Write and verify:** produce a dated report with price/source timestamps, ranking, promotion/demotion reasons, no-chase/no-catching-falling-knives checks and next evidence needed. If GitHub write permission is actually available, fetch current HEAD, inspect whether report exists, **append** dated public record to `research/reviews/YYYY-MM-DD-...`, update concise current-state/report index and changelog, use an expected-SHA/non-force branch update and read back the commit. Preserve concurrent research from other agents. If GitHub write cannot be done, deliver report in chat and disclose **NOT COMMITTED**.
9. **Outcome logging:** record every candidate's initial snapshot and watch failures, then 5/20/60-session later outcomes (including adverse excursion) when data becomes available. Do not retroactively cherry-pick successful examples.

## SCOUT-002 pilot facts that matter (not evergreen signals)
As of **2026-11-05**, an external VCP scanner supplied six unvetted names **SJM, CPAY, VOYA, ABNB, DE, BDX**, with older pivot references checked against Nov 4 prices and scheduled earnings. **SJM** was still near old resistance; **CPAY** crossed an old pivot into earnings; **VOYA and DE** were above old pivots requiring extension/quality review; **ABNB** crossed intraday but not at close; **BDX** was extended into earnings. None was a validated QARP pass or cleared purchase. Historic **EME** and **ALGN** pricing illustrated why a stale starter price is not a standing order—sharp selloffs can reflect new risk and rallies can invalidate old entry value. See the [full pilot](../research/reviews/2026-11-05-first-pre-breakout-pilot.md) for dated sources and qualifiers.

## Known gaps / next research tasks
- No complete, reproducible Finviz A/B/C rerun or public saved screen URL established.
- Existing 22-company [chart audit queue](../research/watchlists/2026-11-05-chart-stage-audit.md) remains CHART PENDING until per-stock fresh OHLCV and market-sector evidence exists.
- No systematic OHLCV **10/40 contraction and volume-dry-up** calculations or demonstrated predictive advantage. Do not overstate scanner accuracy.
- Independent QARP fundamental due diligence and event/risk/valuation checks still needed on **all six** new leads before any admission to canonical active universe.
- No broker execution or automatic order integration. Use [independent challenge doctrine](independent-investment-challenge.md) to resist narrative-led buys.

## Publication boundary
Only publish public company facts, neutral process, candidate research and repeatable evaluation logic. Keep personal positions, balances, loss history, target allocations, private execution plans, individual correspondence and any identifiable personal investment decisions **outside this public GitHub repository**. Do not publish scheduled-task identifiers or account settings. The public continuity notes should be useful but not constitute a transcript or private investment ledger.

## Continuation prompt seed
> Resume CGPT-INVESTMENT from latest GitHub main: read README.md, AGENTS.md, CURRENT-STATE.md and docs/daily-equity-scout-runbook.md, followed by latest dated pilot and watchlists. Maintain QARP A/B/C and independent evidence-based valuation/earnings challenge. Run or review the next completed-session pre-breakout scout with verified sectors and chart data. Preserve all prior results and concurrent commits. Do not infer chart stages, live prices, investments or GitHub writes; report evidence gaps explicitly. Commit only de-identified public research, verify the actual main SHA, and distinguish scheduled tasks from successfully completed reports.
