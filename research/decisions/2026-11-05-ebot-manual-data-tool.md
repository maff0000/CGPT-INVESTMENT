# G0-EBOT-001 — Authorise a minimal manual E-Bot data-test runner
**Naming correction (same date):** **E-Bot** is the intended name. User reports GrokBot is building it, but completion/acceptance remains unverified. This corrects the earlier naming only; no new authority is granted.

**2026-11-05 Europe/London | Decision status:** narrowly scoped implementation brief approved by research sponsor; **GrokBot build not yet undertaken/verified**.

The sponsor wants a basic **E-Bot**, built by **GrokBot**, which can run manually supplied, allowlisted tasks as a first step. This is a **bounded exception to the existing "no research agents before G0 proof" rule**: E-Bot v0.1 is a **manual read-only Massive data validation utility**, not an autonomous equity candidate system or investor decision engine.

**Authorised:** code and offline tests in a separate private/nonproduction E-Bot workspace; operator-only manual task interface; reuse existing public reference `research/validation/g0_massive_readonly_probe.py`; grouped US daily bar + four symbols XOM/LIN/EQIX/SPY OHLCV test of at least 260 completed sessions; safe diagnostics, no raw bars in public GitHub; human configures credentials only after offline acceptance. Five requests maximum for a complete test, respect Basic data lag and usage rights.

**Not authorised:** scheduling/cron, daemon, unbounded prompts or shell access, new cloud services, LLM infrastructure, Finviz scraping, portfolio decisions, broker integrations, live trades, API key transmission through prompts, commercial use under unverified individual rights, or unapproved public repo modifications.

**G0 OPEN, G1 not started, no canonical provider yet selected.** A successful credentialed probe later proves only access and basic bar coverage, not screener validity or investment alpha.

[Full GrokBot brief](../../docs/g0-ebot-manual-utility-brief.md); [Massive onboarding](../../docs/g0-massive-onboarding.md).
