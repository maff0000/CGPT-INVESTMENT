# VALIDATION-FIRST-001 — Freeze agent implementation until investment process is proven
**Date:** 2026-11-05 Europe/London | **Authority:** new research-process priority.

## Decision and corrective direction
**Process validation precedes automation.** The research sponsor and Architect agree that current QARP A/B/C, accumulation-proxy scout, chart labels and fundamental review are **unproven requirements hypotheses**. It would be premature to implement agents around arbitrary or weakly validated filters.

The previously documented **AGENT-SYSTEM-001** architecture remains useful as an **inactive future design reference**, not a go-ahead to build agents, connect brokers or submit orders. Phase 0 is explicitly **manual, prospective research validation**; further architecture work orders remain **BLOCKED** pending an independently evidenced gate decision.

## Immediate operational choice
- Existing **weekday US Close Equity Scout task is PAUSED** while the manual/prospective requirements protocol is established and tested. Scheduling history is preserved; no task results are claimed.
- The existing Monday all-sector research task remains research-only and is not evidence that the validation protocol has passed.
- No automated trading, API broker integration, private position disclosure or new live investment decisions are authorised.

## Proposed proof order
**G0 specification freeze** → **G1 manual reproducibility** → **G2 measured prospective selection outcomes against simple baselines** → **G3 independent replication and out-of-sample robustness** → **G4 decision whether *research-only* automation is justified**. Exact accepted requirements and sample sizes must be dated before G1 starts. A G1 run with no demonstrable excess return is **not** a proven investment edge.

Hard scientific controls: point-in-time source evidence, complete eligible universe and rejects, survivorship and look-ahead avoidance, cohort time stamps, chart reviewer agreement, no-signal days, realistic trade reference times/fees, separated strategic versus tactical outcome horizons, adverse and favourable excursions, failure cases, and no after-the-fact changes to the original record.

## Next bounded deliverable
Approve/freeze **VALIDATION v1.0**, resolve historical OHLCV/fundamental data sources and eligible universe, then perform manual same-day trial sessions using the [validation worksheet](../../templates/manual-equity-validation-review.md). Review technical/fundamental performance without misleading confirmations or automatic buy recommendations. Only successful evidence and an explicit follow-up architecture decision may release an agent research implementation WO.

[Validation requirements](../../docs/research-process-validation-charter.md) · [manual trial protocol](../../docs/research-validation-protocol.md) · [Agent design reference](../../docs/agent-equity-operating-system.md). This public record has no private portfolio data.
