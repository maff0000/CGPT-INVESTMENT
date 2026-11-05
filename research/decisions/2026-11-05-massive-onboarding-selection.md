# G0-PROVIDER-001 — Select Massive Basic for manual data access trial
**2026-11-05 Europe/London.** Massive Stocks Basic is the **first provider candidate for private manual validation**. Free tier according to supplier: $0/month, 2 years of historical US stocks, grouped EOD, 5 requests/min, prior completed trading day available only after midnight America/New_York next calendar date.

**No actual account sign-in, token, private data, API call, 260-bar validation or paid subscription has occurred.** This is NOT final canonical data-source approval. A public read-only manual smoke probe and onboarding guide enable an account holder to test access without exposing credentials. Provider individual-use and redistribution restrictions are material and MUST be resolved before any commercial agent automation, SaaS, chart sharing or external dissemination. Do not commit Massive raw OHLCV.

**Proposed first trial:** XOM/LIN/EQIX/SPY 260+ day bars, one grouped date, independent-price comparison under G0-DATA-002 ($1 included acceptable, >$1 PRICE CHECK; pivot straddle independent), split adjustment checks; Finviz A/B/C remains independently untested.

**Next concrete dependency:** account holder activates Stocks Basic (if within usage terms) and executes the private manual read-only probe, then reports redacted pass/fail/counts. D1–D6 outstanding. **G0 open; G1 not started; no research agents or brokerage activity authorised.**

[Onboarding and controls](../../docs/g0-massive-onboarding.md), [manual probe source](../validation/g0_massive_readonly_probe.py).
