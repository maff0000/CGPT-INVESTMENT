# Candidate evidence contract — research agent handoff
**Version:** CANDIDATE-CONTRACT-001 | **Draft:** 2026-11-05 | **Applies to public market research only.**

## Core principle
A candidate is a **reproducible evidence package**, not a prose ticker tip. Distinguish source-backed facts, deterministic calculated features and analyst hypotheses; every value has timestamp, origin, confidence/UNKNOWN and applicable accounting convention. Public data only.

| Field group | Required candidate packet fields | Source rules |
|---|---|---|
| **Identity** | Ticker, exchange, instrument unique identifier, listing currency, real sector and industry, research lane, corporate action as-of | Never silently confuse dual share classes, ADRs or regional listings |
| **Market snapshot** | Last *completed* regular session and local/UTC time, OHLCV adjusted status, quote vendor/timestamp, SPY and sector ETF comparable observations | A 16:00 close cannot be used by a process that ran earlier; holidays and after-hours separate |
| **Screen trace** | QARP A/B/C fields evaluated and individual pass/fail/unknown; specific exception policy; filters version | A chart opinion is never proof of a Finviz strict pass |
| **Technical stage** | WATCH subtype / BREAKING OUT / IN TREND / CHART PENDING, resistance/support, base dates, SMA20/50/200 and slopes, RVOL, 10-versus-prior-40 range and volume features, extension, confirmed close | Computed deterministically; mark unavailable metrics UNKNOWN, scanner-provided levels UNVERIFIED |
| **Sector/regime** | Actual GICS-style sector and industry, sector return minus benchmark for aligned 1w/1m/3m, stock-to-sector relative performance, market regime | Reconcile sector mapping against dated reference |
| **Company quality** | Revenue and **organic** growth, EPS estimate and revisions, ROIC, dilution, operating margin, owner free cash flow, capital intensity, balance sheet/maturities | Primary company reports with published/as-of dates; vendor estimates clearly separate |
| **Valuation** | Forward P/E with period/definition, PEG with compatible forward growth and positive meaningful earnings, P/FCF or FCF yield, sector alternative, base/bear/bull and margin of safety | No blanket metric for REITs, banks, commodity companies or negative EPS |
| **News/events** | Earnings release UTC/local time, issuer-confirmed status, 7-before/2-after state, other corporate events, material filing references, last check | Missing or conflicting event blocks new-entry review |
| **Challenge** | Two disconfirming factors, alternative explanation of move, permanent capital risk, valuation downside, unknowns | Separate critic from promoting scout |
| **Decision** | Priority, proposed BUY STARTER / BUY FULL / WAIT / REJECT research verdict, next evidence/pivot trigger, specific reason **not** to buy, reviewer, approved version | Investment opinion is never a trade order |

## Provenance
Every critical fact should carry: citation or approved vendor source URI, source publication and observation time, fetch time, effective/as-of date, timezone, calculation/code version, missing/estimated/verified state and expected freshness. No derived score with undefined inputs. If two price vendors disagree, disclose both and refrain from an assumed fill price.

## Simplified promotion and data gates
- **SCOUT-LEAD:** may come from external patterns; incomplete fundamentals are allowed **but clearly labelled**.
- **RESEARCH-QUALIFIED:** all mandatory business quality and source/price freshness checks, plus explicit exception for non-QARP companies.
- **CHART-CLASSIFIED:** independently verified current OHLCV and sector context.
- **COMMITTEE-READY:** challenge and valuation complete, confirmed event status and downside; prioritized candidate pack.
- **RESEARCH-ACTION:** buy/wait/reject opinion after committee. **Not order authorisation**.
- **PRIVATE EXECUTION:** separate broker/account-specific signed order approval and deterministic risk controller; never use a public research ID alone as permission to trade.

A candidacy can be WAIT or REJECT at any step. Do not backfill missing facts with model predictions disguised as observations.

## Minimal output packet example (illustrative, fictional data)
| Symbol | Sector | Finviz membership | Chart stage | Entry status | Evidence completeness |
|---|---|---|---|---|---|
| SAMPLE | Industrials | A PASS, B UNKNOWN, C UNKNOWN | WATCH / COILING (hypothetical) | WAIT — earnings gate unknown | Incomplete; no buy review |

**No individual investor data**: no holdings, manager identities, orders, limit amounts for specific accounts, intended weights, private allocation or transaction reports. Preserve deeper private accounting separately from this public contract.
