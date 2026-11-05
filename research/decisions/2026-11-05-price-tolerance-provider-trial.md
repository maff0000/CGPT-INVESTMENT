# G0-DATA-002 — Accept $1 price difference and stage provider trials
**Date:** 2026-11-05 Europe/London | **Status:** price review threshold ACCEPTED; market-data provider and entire G0 not yet accepted.

## User-authorised change
For the same USD instrument, session and price convention, **vendor closing-price absolute difference <=$1.00 is acceptable without the routine PRICE CHECK flag**. **Difference >$1.00 raises PRICE_CHECK** for source diagnosis. This supersedes G0-DATA-001's tendency to over-escalate cents.

Do not confuse normal source tolerance with **signal validation**: if two ordinary close reports straddle a documented pivot or entry ceiling, tag **SIGNAL_AMBIGUOUS** and hold confirmation until independently resolved; this does not raise PRICE CHECK if the spread is within $1.00. Date/currency/share-class/adjustment mismatch raises DATA_MISMATCH regardless of absolute amount. Never cherry-pick the value that agrees with a desired buy signal.

Previous Nov4 XOM ($0.03), LIN ($0.17), EQIX ($0.16) quote differences are all **PRICE_OK** under new policy.

## Source selection research
Official public documentation supports a **conditional manual G0 trial** of **Massive Basic** (US market grouped EOD, 2-year history, five calls/min, prior session available from 00:00 ET next day); **Tiingo** as a complementary adjusted/raw price and correction check; **EODHD** as another option. **Finviz remains the manual A/B/C baseline and does not provide historical screener results**. Free individual subscriptions are not evidence of a commercial/agent data licence.

## Explicit limit
This decision does not claim that an API account, provider licence, actual 260-bar data, fresh Finviz report or same-day 22-name scan has been obtained. The next task is **manual D1–D6 vendor and chart-proof acceptance**, not an agent implementation. G0 remains OPEN; G1/agent build/trading BLOCKED.

[Accepted policy and provider tests](../../docs/g0-price-tolerance-and-provider-trial.md) | [Test worksheet](../../templates/g0-price-source-comparison.md) | [Previous three-company diagnostic](../validation/2026-11-05-cross-sector-company-dry-run.md).
