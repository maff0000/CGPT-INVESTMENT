# QARP screening requirements — frozen criteria and equivalence matrix
**Date:** 2026-11-05 (Europe/London)
**Status:** Human-readable copy of the **already public frozen screen**. Not a new strategy approval. Not a claim that the private manifest was re-read, and not a claim that any provider field equals Finviz.
**Public sources, unchanged:** [QARP-ROTATION-001 v1.0.0](sbot-strategy-registry.md) and [Finviz Discovery v2](finviz-filters.md).
**Private accepted manifest hash, unchanged:** `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. **Ruleset digest, parent-reported at the locked private head:** `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. The parent directly read paper-bots PR #4 at `a40412f0876fd59526a6b663273f69b4df008ec4` and states that the private table contains these operators and units. This session did not re-read that file. The core 91-test result is unchanged. This public copy is not an acceptance.

## Frozen predicates — QARP-ROTATION-001 v1.0.0
Every unlisted Finviz filter is **Any**. At one observation cutoff and one universe, C ⊆ B ⊆ A. Three memberships are not three opportunities.

| Group | Field | Operator and value | Applies to |
|---|---|---|---|
| Descriptive | Exchange | Any | A, B and C |
| Descriptive | Country | Any | A, B and C |
| Descriptive | Market cap | +Mid, over $2 billion | A, B and C |
| Descriptive | Price | Over $10 | A, B and C |
| Descriptive | Average volume | Over 200 thousand shares | A, B and C |
| Descriptive | Sector | Any for all-sector; one named sector for a lane run | A, B and C |
| Fundamental | Forward P/E | Under 25 | A, B and C |
| Fundamental | Price / free cash flow | Under 30 | A, B and C |
| Fundamental | Return on invested capital | Over 10 percent | A, B and C |
| Fundamental | Long-term debt / equity | Under 1 | A, B and C |
| Fundamental | Operating margin | Over 5 percent | A, B and C |
| Fundamental | Sales growth, trailing twelve months | Positive | A, B and C |
| Fundamental | EPS growth, next year | Positive | A, B and C |
| Technical | Performance | A: Any. B: Month up. C: Month up | As stated |
| Technical | SMA 50 | A: Any. B: price above SMA 50. C: price above SMA 50 | As stated |
| Technical | SMA 200 | A: Any. B: Any. C: price above SMA 200 | As stated |
| Technical | Every other technical field | Any | A, B and C |

Earnings date, dividend, recommendation, PEG, price to book, relative volume, RSI and pattern remain **Any**. They are not silent extra gates. The separate earnings rule is seven sessions before the announcement, including announcement day, and two completed sessions after. Chart stage is after the screen: BREAKING OUT, IN TREND, or WATCH, otherwise CHART PENDING.

## Implemented, deferred, and owner choices
| Item | State |
|---|---|
| Frozen A/B/C values above | Public and unchanged. Private table parent-reported at `a40412f0876fd59526a6b663273f69b4df008ec4`. Manifest hash unchanged |
| Discovery universe | Broader than a QARP pass. No seven-name cap. QARP is not applied to the discovery count |
| Unknown or unmapped metric | UNKNOWN. Not an exact Finviz pass |
| Earnings gate | Separate from the screen. Fixture date source is not a live calendar |
| Chart stage | Deferred from the screen. CHART PENDING until observed |
| Sector-relative strength as a predicate | Owner choice. Not approved |
| UNCHECKED survivor screened as UNKNOWN versus held out | Owner choice. Not approved |
| Seven research labels as strategies | NOT APPROVED |
| FAIR-VALUE-COMPOUNDER-002 | NOT APPROVED |
| Entry, exit, initial stop, trailing stop and risk | NONE. Stop-dependent M/T HOLD |
| Scheduler and new strategies | BLOCKED until this review and verified rights |

## Three columns — capability, licence, Finviz equivalence
The accepted E-Bot interface below is the parent's fourth direct read of the accepted README at `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`. This session did not re-read that private file. The design is an accepted interface. It is not a current live permission.

| Capability | Accepted interface | Current licence or live permission | Finviz equivalence |
|---|---|---|---|
| Massive grouped and daily OHLCV | Read-only. Fixed symbols XOM, LIN, EQIX and SPY | Rights UNVERIFIED. Not a live permission | Not a Finviz fundamental or screen field |
| IBKR contract details | Read-only. Same four symbols | Rights UNVERIFIED. Not a live permission | Not a Finviz field |
| IBKR TRADES, regular trading hours | Read-only. Same four symbols | Rights UNVERIFIED. Not a live permission | Not SMA and not chart stage |
| Broad US listed universe | Not in the accepted E-Bot interface | Not granted | Not established |
| Forward P/E, P/FCF, ROIC, debt, margin, sales and EPS growth | Not implemented in the accepted E-Bot interface | FMP: exactly three historical calls. Profile SPY, HTTP 200, one record. Historical SPY, HTTP 200, two records. Batch quote SPY and XOM, HTTP 402, non-JSON. No fourth call. No licence tier or quota inferred. Rights UNVERIFIED | UNKNOWN |
| Month-up performance, SMA 50 and SMA 200 | Not implemented | No live permission | UNKNOWN |
| Chart stage | Not implemented | No live permission | Separate from A/B/C. CHART PENDING |
| Earnings dates | Separate public gate. Not a connected calendar | Source UNKNOWN | Finviz Earnings Date remains Any |
| Offline discovery fixtures | Builder-reported synthetic rows only | No provider entitlement asserted | Unsupported mapping stays UNKNOWN |

No new provider call is made by this correction. The locked private documentation head is `a40412f0876fd59526a6b663273f69b4df008ec4`. Earlier private heads remain historical.
