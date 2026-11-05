# G0-PROBE-AUDIT-001 — Reference probe fail-closed readiness review
**Date:** 2026-11-05 (Europe/London) | **Type:** independent read-only architecture/acceptance audit | **Outcome:** **HOLD** for accepting the reference probe as an E-Bot validation result.

## Scope and source baseline
Reviewed public `main` at `5bdfc4fbd820686239b17b474582b8cf6a65f852`, including `README.md`, `AGENTS.md`, `CURRENT-STATE.md`, the G0 validation charter/protocol, Massive onboarding, `docs/g0-ebot-manual-utility-brief.md`, and `research/validation/g0_massive_readonly_probe.py`. The GrokBot-built E-Bot implementation was **not available for this review**. This review does **not** assess its code or claim it failed testing.

The public reference script is a manual smoke-test aid, **not** a provider, chart, signal or investment approval. No authentication, live Massive request, market-data ingestion, Finviz screen, production modification or trading action occurred.

## Reproducible offline defect — false-success result
Used an in-memory monkeypatch of the public probe's `fetch` and hidden-key input (a dummy non-credential). The simulated grouped-market response returned `status=OK` and **zero results**; each of the four simulated ticker responses returned `status=OK` with **260 distinct timestamps only**, deliberately omitting actual OHLCV fields. No network was accessed.

Observed result:

| Check | Actual observed behaviour | Required acceptance behaviour |
|---|---|---|
| Grouped data missing | Printed `HOLD: grouped data missing one or more test instruments` | Run must remain HOLD/FAIL |
| Four 260-record timestamp-only responses | Printed `bars>=260=True` for all four | Missing `o/h/l/c/v` must fail bar-integrity validation |
| Overall process return code | **0 (success)** despite the foregoing | **Nonzero / explicit HOLD or FAIL**, never PASS |

**Finding P0:** a wrapper or human could mistake exit code 0 for a passed access/data-quality test. The reference implementation checks counts, status and timestamp uniqueness but does not verify price/volume fields, ordering, expected session coverage, or a genuine top-level PASS/HOLD/FAIL aggregate. Missing grouped coverage is currently informational only. An error after partial retrieval does not provide a complete structured partial-run summary. These are code-review findings about the **public reference**, not conclusions about GrokBot's separate deliverable.

## Acceptance checks for the bounded E-Bot v0.1
Before approval of its offline implementation, independently confirm:

1. **Fail closed:** grouped missing sample, partial responses, invalid bar, zero bars, out-of-order/duplicated timestamps, or absent required OHLCV fields return explicit HOLD/FAIL and non-success process status. Include synthetic counterexamples matching this review.
2. **Access timing:** reject a requested session that is not a completed, entitled US session under the Basic after-midnight-Eastern cutoff; distinguish market holiday from invalid data.
3. **Call budget:** cap at five GETs per single run, consider attempts in the same rolling minute, and report a 429/403 without unsafe repeated calls or misleading success. Report safe partial progress after errors.
4. **Data lineage:** check ticker identity, source adjustment convention, earliest/latest sessions, 260+ valid completed bars per symbol, and redacted per-symbol summary. A single-source trial must say `SECOND_SOURCE_NOT_TESTED`.
5. **Prompt/security controls:** unsupported free text fails before any external request; no shell command interpolation, scheduler, broker action, raw vendor bars, API key exposure or credentials in repository/logs.
6. **Offline evidence first:** review test cases and outcomes before the human locally supplies the key and separately authorises the credentialed manual call.

These implement existing [G0-EBOT-001](../../docs/g0-ebot-manual-utility-brief.md) requirements, not new functionality or a widened work order. No changes to the public probe code are authorised by this audit alone.

## Provider and validation dependencies unchanged
- **D1 licence:** Massive Basic is a proposed private manual trial only. Individual, non-business terms do not grant commercial-agent use or redistribution; classification and intended use need an explicit account-holder check. Refer to [Massive individual terms](https://massive.com/legal/individuals-terms-of-service) and [redistribution guidance](https://massive.com/knowledge-base/article/how-can-i-redistribute-massives-market-data).
- **D2–D4 data:** no authenticated grouped/260-bar results exist yet; independent price comparison, corporate-action treatment and manual chart validation are outstanding. Apply `<= $1.00 PRICE_OK`, `> $1.00 PRICE_CHECK`, independent `SIGNAL_AMBIGUOUS` for a critical pivot straddle.
- **D5–D6 process:** Finviz A/B/C point-in-time evidence, second-provider reconciliation, full macro snapshot and frozen universe/benchmarks remain open. E-Bot success alone cannot close G0 or start G1.

**Decision:** keep G0 **OPEN**, G1 **NOT STARTED**, automated equity agents and broker execution **BLOCKED**. Await GrokBot's delivered code and offline test report. Review it against these counterexamples, then consider a separately authorised, credentialed manual provider test. Preserve all existing candidate/watchlist verdicts as dated historical research only.
