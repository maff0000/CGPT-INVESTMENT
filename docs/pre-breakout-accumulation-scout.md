# SCOUT-001 — Pre-breakout base, contraction and accumulation-proxy discovery
**Adopted as research pilot:** 2026-11-05 (Europe/London) | **No screener run or chart classification claimed.**

## Problem we are solving
Strict positive-month and price-above-50/200-SMA screens tend to select companies **after visible momentum begins**. A promising high-quality stock may spend weeks absorbing supply in a base **before** an actionable breakout. The project should identify that setup early enough to prepare a **price-aware, evidence-backed purchase assessment at the breakout**, rather than chase a large move once momentum is obvious.

Retain all existing [Finviz QARP v2 A/B/C](finviz-filters.md) screens unchanged. Add a **parallel, optional pre-breakout scout process** and WATCH substages. This is not a new mandatory fundamental screen, nor a fourth bullish chart group.

**Epistemic limit:** quiet volume and tightening price are **proxies** for possible supply absorption, **not proof of institutional accumulation** or a signal that future performance will be positive. Weak demand and distribution can also produce a quiet chart.

## WATCH substages, not new primary groups
| Internal watch phase | Chart behaviour | Next condition |
|---|---|---|
| **WATCH / BASE FORMING** | Multiweek range, potential repeated support/resistance, volatile corrections not yet consistently tightening | Demonstrate lower swing volatility, stable support and more favourable volume/RS |
| **WATCH / COILING** | Two or more successive pullbacks contract; repeated support holds; falling volume and narrower bars; reasonably stable/improving stock relative strength | Identify precise resistance/pivot and assess proximity, event and valuation |
| **WATCH / AT PIVOT** | Price approaches well-defined resistance (pilot interest: within ~0–5%) after a tight right side, without confirmed closing breakout | Regular-session close beyond resistance with credible participation, followed by confirmation/retest |
| **BREAKING OUT** | Confirmed close above prior resistance with supporting participation/RS (and source timestamp) | Run immediate independent BUY/WAIT/REJECT decision; not automatic order |
| **IN TREND** | Breakout holds and forms an advancing structure; or an existing uptrend continues | Review orderly pullback/addition only if risk/valuation justify |

If the current chart cannot be inspected, use **CHART PENDING**, not a made-up WATCH substage.

## What constitutes stronger pre-breakout evidence?
1. **Base structure:** typically 20–60 completed trading sessions or a justified longer base; mark two or more local highs near resistance and repeated support levels. Some genuine reversals have no prior uptrend; do not label them textbook VCP without one.
2. **Progressive contractions:** declining swing depths, such as illustrative 15% → 8% → 4%, with fewer wide-range candles toward the right side. Observe or calculate the last-10-session daily trading range versus the prior 40 sessions. **Provisional scouting hint: ratio <=0.75** (not a universal threshold).
3. **Volume quietening:** last-10-session mean *completed-session* volume versus the immediately preceding 40 sessions. **Provisional hint: <=0.80**. Look at **up-session vs down-session volume** and especially whether large-volume declines or failed resistance tests suggest distribution. Exclude/flag distortion from earnings spikes, holidays, splits or changed free float.
4. **Relative strength:** stock/SPY or stock/S&P 500 relative-price line and sector-relative line stable or improving over aligned 20/60-session periods while the stock's own price is flat. This is **not** merely RSI or a positive monthly total return. Check industry and sector strength as separate context.
5. **Pivot proximity:** regular-session close around 0–5% **below** documented price resistance. A rising share price well below the old high could still be constructing a base; a 52-week high is **not required** for early recovery setups.
6. **Moving-average context:** SMA20/50 flattening then rising supports the case; price holding support near SMA50 is constructive; SMA200 above price may signal early recovery and materially higher false-breakout risk. A valid pre-breakout scout need not pass B or C.
7. **Fundamental risk:** verify business quality, upcoming earnings calendar, underlying earnings revisions, recent secondary offerings, acquisitions and liquidity. A cheap-looking dormant stock is not automatically an accumulation opportunity.

**Pilot ratios must not be sold as proven predictive factors.** They will be adjusted after recording prospective hits, misses and false breakouts. Use completed daily price/volume bars for all ratios.

## Concrete Finviz look-up recipes
The fundamental **A/B/C presets are unchanged**. The following are **temporary exploratory overlays** applied to a fresh or copied scan; never overwrite canonical presets.

| Scan use | Starting population | Finviz trial fields | Why it helps / what it misses |
|---|---|---|---|
| **S1: Quiet-base scout** | A (fundamental passes), plus separately labelled premium-valuation exceptions | Performance **Any**; SMA50 **Any**; SMA200 **Any**; inspect **Volatility (Month)**, optional Pattern **Channel/Ascending Triangle/Wedge**, and distance to **20-day High/Low**. Use Charts view. | Finds bases before Month Up, including early recoveries; Finviz current-month volatility is *not* a time-series contraction test |
| **S2: Coiling near pivot** | S1 candidates plus existing WATCH queue | Prefer close within ~0–5% of recorded resistance (manual chart or 20-day-high proximity as **proxy**), optional sector-relative strength, **relative volume around or below 1** if the session is comparable, and visible SMA50 flattening | A low **today** RVOL is *not* the same as multiweek volume dry-up; confirm completed 10-day vs prior 40-day measurements |
| **S3: Breakout alert** | S2 + B/C and A early-recovery candidates | Price approaching or crossing base/pattern resistance; inspect price change and unusual/relative volume, SMA50/200 posture, chart. Prefer ~1.5x completed-session normal volume **as a quality clue**, not an absolute bar | Detects emerging demand; avoid intraday wick breakouts, excessively extended pivots and pre-earnings initiations |
| **S4: Similar-pattern discovery** | A credible example of a tightening base already identified | Finviz Advanced Charts **Find Similar Charts → Select Region**, choose Euclidean or Banded DTW and search other stocks; subsequently apply fundamentals | Finviz offers pattern-similarity search (September 2026); visual likeness is **not** proof of accumulation or investment quality; verify entitlement |

**Important Finviz functionality distinctions**
- Finviz **Volatility** is an average *daily high-to-low percentage range* over its stated window, not the **ratio of recent vs prior ranges** that proves progressive contraction. **ATR** is an absolute true-range unit and should be normalised by price for cross-stock comparisons.
- Finviz **Relative Volume** is the current session volume versus a three-month average, adjusted intraday; it cannot replace the 10-day versus prior-40-day historical comparison.
- Finviz supports chart Pattern, 20/50/52-week High/Low, SMA20/50/200, Volatility, ATR and Relative Volume. Its **Elite advanced indicators** include MACD, Money Flow Index, Bollinger Bands and EMA with customizable parameters. Access depends on subscription and the exact supported indicator operations; do not imply a custom contraction-ratio screen is available without verification.
- **Screener Charts view** permits rapid visual inspection; **Find Similar Charts** (Sept 2026) can use a selected chart region to retrieve similar price shapes, subject to access. These are discovery accelerators, **not** independently validated pattern scanners.
- Avoid setting a universal low-volatility maximum across all industries; biotech and software naturally move differently from utilities. Begin with **Any** and inspect dispersion in-sector. If trial numeric low-vol/relative-volume bands are used, log them explicitly and evaluate the missed candidates.

Primary Finviz source documentation: [Finviz screener help](https://finviz.com/help/screener), [Finviz chart patterns](https://finviz.com/help/technical-analysis/charts-patterns), [custom Screener Charts](https://finviz.com/blog/see-your-screener-results-w-fully-customizable-charts/), [Elite technical indicator filters](https://finviz.com/blog/unlock-powerful-trading-insights-with-intraday-timeframes-advanced-indicators-in-finviz-screener/) and [Find Similar Charts](https://finviz.com/blog/find-similar-charts-breakouts-and-patterns-that-match-your-trading-style/).

## Reproducible after-close candidate-scoring fields (only when valid historical OHLCV is available)
- **Range contraction ratio:** mean daily (high−low)/prior-close over last 10 completed trading days divided by same mean over **preceding** 40 days, after corporate-action adjustment.
- **Volume dry-up ratio:** mean completed daily share volume last 10 days / mean of immediately preceding 40 days; flag unusual event days and corporate actions.
- **Distance to pivot:** (documented prior base resistance − latest completed close) / resistance; meaningful only when a credible pivot exists and quote remains below it.
- **Relative price strength:** change in stock/sector-ETF and stock/SPY price ratios over aligned 20/60 completed trading days, dividend/corporate-action conventions stated.
- **Up/down-volume asymmetry:** completed up sessions' vs down sessions' volume adjusted for number of observations; used qualitatively, not a substitute for actual institutional transaction disclosure.
- **Sector/industry:** GICS-style sector and industry, relative 1-week/1-month/3-month performance, broader market regime; no automatic sector veto.

**No historical OHLCV data feed, bulk screener export, API or automated scanner is established by this policy.** Obtain legal/licensed data before any future scripted implementation; first verify prospective usefulness manually.

## What we measure during pilot
For each watch candidate record the date identified, Watch substage and evidence, sector, trigger resistance, event and valuation gates, date of subsequent breakout, first 5/20/60 trading-day return **and adverse excursion**, failure/retest outcome and benchmark. Include WATCHs that never break out to prevent survivorship bias. Evaluate precision, lead time and false-breakout rate before changing permanent Finviz presets.

## Decisions remain separate
**WATCH / AT PIVOT does not mean buy. BREAKING OUT does not mean buy.** Earnings, business valuation, expected downside, liquidity and the Independent Challenge protocol continue to determine BUY STARTER / BUY FULL / WAIT / REJECT. Preserve the >=7/week all-sector research aim, without requiring seven chart breakouts or forced trades.

Related: [CHART-001](chart-stage-classification.md), [Finviz baseline](finviz-filters.md), [decision](../research/decisions/2026-11-05-pre-breakout-scout.md).
