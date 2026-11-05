# Finviz presets and version history
**Current recovered baseline: QARP Discovery v2, 2026-11-03.** Settings below preserve the supplied research history; they have not been executed again during repository initialisation.

Use the [Finviz screener](https://finviz.com/screener.ashx) and [official filter help](https://finviz.com/help/screener). Official help describes descriptive, fundamental and technical filters; forward P/E depends on forecast earnings. Review provider definitions rather than mixing different metric conventions.

## Shared v2 settings
| Tab | Field | Setting |
|---|---|---|
| Descriptive | Exchange | Any |
| Descriptive | Country | Any |
| Descriptive | Market Cap. | +Mid (over $2B) |
| Descriptive | Price | Over $10 |
| Descriptive | Average Volume | Over 200K |
| Descriptive | Sector | Any for discovery; one lane sector per sector run |
| Fundamental | Forward P/E | Under 25 |
| Fundamental | Price/Free Cash Flow | Under 30 |
| Fundamental | Return on Invested Capital | Over 10% |
| Fundamental | LT Debt/Equity | Under 1 |
| Fundamental | Operating Margin | Over 5% |
| Fundamental | Sales Growth TTM | Positive |
| Fundamental | EPS Growth Next Year | Positive |

**Every unlisted field is Any**, including earnings date, dividend yield, analyst recommendation, PEG, P/B, institutional activity, relative volume, RSI and pattern. Earnings safety is assessed separately, not inferred from Earnings Date = Any.

## Technical overlays on the same v2 fundamentals
| Field | A: Discovery | B: Emerging Momentum | C: Confirmed Momentum |
|---|---|---|---|
| Performance | Any | Month Up | Month Up |
| 50-Day SMA | Any | Price above SMA50 | Price above SMA50 |
| 200-Day SMA | Any | Any | Price above SMA200 |
| All other technical fields | Any | Any | Any |

At a common timestamp and universe, C should be a subset of B, which should be a subset of A. Do not add counts as unique names. A recovery watchlist can contain A names with weak charts and separately documented near-misses.

## SCOUT-001 — discover a tightening base before a breakout
Preserve the exact A/B/C presets above. A separate **exploratory scan** starts with A plus documented premium/near-miss exceptions and checks Finviz **Volatility, Pattern, distance to 20-day High, Relative Volume, and Screener Charts**. These are **snapshots**: Finviz volatility is an average daily high/low percentage range and RVOL is the intraday-adjusted current volume versus a 3-month mean, **not a 10-day versus prior-40-day contraction or volume dry-up measure**. Use completed bars to confirm the latter, and label WATCH / BASE FORMING, COILING, AT PIVOT before BREAKING OUT. Elite technical filters and Find Similar Charts may accelerate search; no custom indicator configuration or account preset was saved. See [SCOUT-001](pre-breakout-accumulation-scout.md).

## CHART-001 — separate breakout/trend/watch grouping (2026-11-05)
All A/B/C fundamental and SMA50/SMA200 screens remain unchanged. **After** screening, classify current charts as **BREAKING OUT / IN TREND / WATCH**, with actual sector and industry and date-aligned sector relative strength. A B or C screen pass does not prove a breakout. Finviz Pattern, distance from 52-week high, relative volume and Charts view are *optional exploratory overlays*, not new mandatory screen settings. See [CHART-001 rules](chart-stage-classification.md) and [22-name review queue](../research/watchlists/2026-11-05-chart-stage-audit.md). No live screen or chart classifications are claimed.

## Why v2 replaced strict cutoffs
The discussion identified share-count liquidity exclusions, near-miss margins, domicile exclusions, and stale balance sheets after acquisitions. v2 widens discovery while reserving stricter judgment for due diligence. Country = Any does not remove country risk; verify listing, domicile and exposures separately. Over 200K is a discovery proxy, not a full liquidity gate.

Manual checks: daily dollar turnover, recent acquisitions/debt changes, earnings revisions, actual business exposure, industry leadership, relative strength against the market, cash-flow quality and all event gates.

## Superseded settings (historical continuity)
| Version | Country / volume | ROIC | Forward P/E | P/FCF | Operating margin |
|---|---|---|---|---|---|
| Initial Quality + Value | USA / >500K | >10% | <30 | <30 | >10% |
| Refined QARP v1 | USA / >500K | >15% | <25 | <25 | >10% |
| Discovery v2 (current) | Any / >200K | >10% | <25 | <30 | >5% |

All retained market cap >$2B, price >$10, LT debt/equity <1, positive sales TTM and positive next-year EPS growth. Initial momentum used Month Up, above SMA50 and above SMA200; its early variant omitted SMA200. Refined v1 used the A/B/C structure above. v1 proposed relaxing valuation cutoffs to 30 if the universe was too narrow; do not automatically apply that older suggestion to v2.

REPORTED counts from the supplied history: initial screen 60; v1 A/B/C 71/36/29; strict industrial screen 7/2/1; later revised fundamental sector screens Healthcare 19 and Consumer Defensive 10. These are unverified historical snapshots, not current results or reproducibility evidence.

## Reproduction record
For every run record date/time/timezone, observation cutoff, all fields or saved public screen URL, version, sector, result count, unique symbols, exclusions and data delays. Verify the current interface supports each selected setting. Do not invent Finviz URL parameters or claim presets were saved to an account. Save concise observations and citations in accordance with provider rights.
