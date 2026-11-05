# MACRO-PROSPECTIVE-001 — Prefer in-time macro-aware validation to mechanical backtesting
**Date:** 2026-11-05 Europe/London | **Status:** adopted requirements amendment; G0 not frozen, outcomes not proven.

## Decision
The research sponsor prefers **contemporaneous, forward-only macro-and-company research**, instead of prioritising mechanical historical strategy backtests at this stage. Historical context remains useful for understanding firms, valuation and crisis sensitivity; the claim is **not** that well-designed point-in-time macro-aware backtests are impossible. They are expensive, highly assumption-sensitive and not required for the present requirements-validation objective.

**The process must now record dated contemporaneous macro conditions** before reviewing a company: nominal and real yields, yield curve, inflation, central-bank and economic-release calendars, oil/energy, credit/liquidity, FX, geopolitical/trade shocks, elections and confirmed policy/regulation, material shortages/bottlenecks, market breadth and relative sector performance. Avoid collecting every macro headline when its company-level cash-flow mechanism is absent.

Each relevant factor must pass **observed fact → company/sector economic transmission → exposure and time horizon → what is already priced in → conditional action/risk effect**, with explicit alternative explanations and unknowns. An election narrative, war headline or oil spike is not an independent buy signal.

## Amendment to VAL-FIRST-001
- **G0:** freeze macro dashboard, source types, timestamp, relevance and state codes together with existing A/B/C, chart and investment-gate requirements.
- **G1:** prospectively run *manual* full macro + sector + fundamentals + charts + valuation decisions, documenting ALL cases and errors, including no-signal days.
- **G2:** compare prospective decisions against a **predeclared macro-blind baseline** and market/sector/simpler technical controls using equivalent observation and price clocks; track missed opportunities and false vetoes. No after-the-fact macro excuse for bad trades.
- **G3:** independent, **additional prospective replication** in future observed conditions; **remove historical walk-forward backtest as mandatory proof gate**. Historical cases can support qualitative stress discussion, never a claim of validated performance.
- **G4:** research-agent implementation remains blocked pending explicit evidence-based authorisation. Broker integration/trading approval is a separate later decision.

No macro snapshot has yet been completed for G0, and the first manual prospective run has not started. Do not claim predictive superiority. The weekday after-close automation remains paused under VALIDATION-FIRST-001. The Monday seven-plus-sector research report is separate.

[Canonical macro overlay](../../docs/macro-aware-equity-review.md) | [Validation requirements](../../docs/research-process-validation-charter.md) | [Test protocol](../../docs/research-validation-protocol.md).
