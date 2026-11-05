# CHART-001 — Chart stage, sector and Finviz research priority
**Adopted:** 2026-11-05, Europe/London. **Status:** operational pilot to refine with evidence.

## Three separate fields
1. **Finviz eligibility:** retain QARP Discovery v2 **A / B / C** scans exactly as previously specified. A = fundamentals only; B = A plus Month Up and price above 50-day SMA; C = B plus price above 200-day SMA. Screen membership overlaps; it is not a chart label.
2. **Chart stage:** classify only from a **fresh, dated daily/weekly chart and volume evidence** into BREAKING OUT / IN TREND / WATCH. Unknown charts remain CHART PENDING. Failed or invalid theses can be archived.
3. **Investment action:** BUY STARTER / BUY FULL / WAIT / REJECT, independently supported by economics, valuation, earnings/event restrictions and portfolio risk. A breakout **does not imply BUY**.

## Chart groups
| Group | Definition | Chart inspection | Investment meaning |
|---|---|---|---|
| **BREAKING OUT** | Regular-session daily close through a meaningful, recorded multiweek resistance/base, rather than a wick or an indicator cross alone | Base length and level; closing distance above resistance; prior volume, close-day relative volume; stock strength vs S&P 500 and sector; 50/200 SMA posture; nearest support/extension | **Top priority for immediate buy-or-wait review**, not automatic purchase |
| **IN TREND** | Established advancing price structure, preferably above rising 50/200-day SMAs with higher highs/lows and positive relative performance | SMA50/SMA200 direction and separation, 20/50-day pullback area, support tests, extended moves, trend stage, sector/industry leadership | Could still be an attractive current buy, especially on orderly pullbacks; not necessarily too late |
| **WATCH** | Qualified business but no verified breakout or attractive uptrend/entry; includes consolidation, recovery, under-resistance, or a stretched/ineligible setup | Explicit resistance/promotion level, basing, improving swing lows, trend repair, event date, next catalyst | Monitor without treating the pattern as ready to buy |

**Workflow-only states:** CHART PENDING (not yet inspected with current OHLCV) and INVALIDATED/ARCHIVED (failed thesis or setup). Neither is a fourth bullish category. A stock **approaching** resistance remains WATCH with a high-priority **near-breakout flag** until a close is confirmed.

## Provisional breakout standards — not inflexible screener cutoffs
- Identify a real 20–60 **trading-session** consolidation/base, or explain another structurally valid boundary. Mark the precise prior resistance and base dates.
- Prefer a regular-session daily **close** through the level, ideally with a meaningful volatility-adjusted buffer and continuation/retest. Intraday price spikes are only candidates.
- Prefer relative volume around **1.5x or more on the completed breakout session**; it is an empirical pilot guide, not a universal rule. Finviz Relative Volume is adjusted intraday and is not itself a finished-day confirmation.
- Assess stock strength vs **S&P 500 and its own sector** over aligned dates, and relative sector performance vs S&P 500 over **1-week, 1-month and 3-month** intervals.
- Document extension/distance from the pivot and location of realistic technical invalidation. A stock already extended or above fair value can be **BREAKING OUT / WAIT**.
- Do not veto early recoveries below the SMA200 if the base and economics are demonstrable, but require a clearer risk assessment.
- Existing **7 exchange sessions before earnings plus results day, then 2 complete regular sessions after** remains the hard initiation/addition block. Business fundamentals, valuation and independent challenge can also veto a purchase.

## In-trend standards
Prefer an ascending SMA50, price above SMA50 and SMA200, and a persistent higher-high/higher-low sequence with broadly positive relative strength. Record the SMA50 versus SMA200 **ordering and both slopes**, not just whether price is over them. A sharp vertical run far above SMA50 (e.g., roughly 8–10% as an **alert**, adjusted for volatility) can be In Trend but still have unattractive entry risk. Pullback/retest opportunities may be more robust than chasing breakouts.

## Mandatory sector/industry overlay
Every row: actual **sector and industry**, last confirmed relative sector and stock performance vs benchmark, sector state (LEADING/IMPROVING/WEAKENING/WEAK/UNASSESSED) and dates. Research discovery lane may differ from actual sector: historical defensive-lane **OLLI** is tracked as Consumer Discretionary in the current sector inventory, with vendor taxonomy differences noted. Sector weakness is a **risk context**, never automatic veto on exceptional early leaders.

## Finviz look-up process — all A/B/C screens retained
1. **Run A, B, C unchanged** and record universe, sector, time and precise filter settings; deduplicate, and preserve the membership labels. The current screen documentation is [Finviz filters](finviz-filters.md).
2. **Breaking-out candidates first:** inspect B/C plus potential A recoveries. Trial optional **Pattern** filters (Horizontal S/R, trendline resistance, triangle ascending), price proximity to 52-week high, **Relative Volume** and the **Charts** view. Chart pattern and new high are only discovery cues, not automatically validated breakouts.
3. **In-trend next:** B/C candidates with rising 50/200-day averages; inspect entry proximity to support, leadership and extension.
4. **Watch third:** A-screen candidates, named watchlist companies and premium-quality exceptions excluded by the strict QARP filter. Each Watch name must have a promotion trigger.
5. **After screening:** perform economic valuation and earnings/event review separately; publish a concrete BUY/WAIT/REJECT view for priority setups.
6. **Continuous improvement:** log false breakouts, missed early leaders, false trend labels and outcomes. Changes to pilot parameters require a new dated evidence-backed decision. Do not claim a backtested edge from a screening rule alone.

Finviz official references: [Screener help](https://finviz.com/help/screener), [Chart-pattern guidance](https://finviz.com/help/technical-analysis/charts-patterns), and [Charts-view description](https://finviz.com/blog/see-your-screener-results-w-fully-customizable-charts/). No Finviz account preset was edited and no live Finviz or 22-company chart scan was run in the creation of this methodology.

## Reproducibility standard
Record per company: **symbol, name, actual sector, industry, research lane, A/B/C membership and date, chart group and date, daily-close price, base/resistance, SMA20/50/200 levels and slopes, relative volume, stock/sector RS, earnings gate, valuation/downside, BUY/WAIT/REJECT decision and next chart trigger**. Never infer chart group from an investment verdict.

First 22-company audit queue: [2026-11-05 chart-stage audit](../research/watchlists/2026-11-05-chart-stage-audit.md). All 22 remain CHART PENDING until charts are actually reviewed; **that does not mean none are breaking out**.
