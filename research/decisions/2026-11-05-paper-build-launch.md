# PAPER-LAUNCH-001 — approve integrated six-bot delivery with GrokBot autonomy
**Decision date:** 2026-11-05, Europe/London | **Decision owner:** Matt
**Status:** OWNER APPROVED BUILD DIRECTION, subject to paper-only trust boundaries and Architect milestone review.
**Prior state:** GitHub main 6b5f3401c409d99896f41c97bac70119f5e848a5, E-Bot private main 50c0b66247498672b84e9fcae7e417a538a0e5c1, E-Bot PR #2 OPEN/HOLD at 9b843dee03892e73f29da31997e5d07bfed564a7.

## What Matt approved
- All six roles **E, S, R, M, T, NEO**, plus deterministic risk gate, integrated early and developed as real **paper/shadow-only** software. **M-Bot's separate Manager role is now OWNER APPROVED**, superseding its provisional status in PAPER-SYSTEM-001 and NEO-LEARNING-001.
- GrokBot is the delivery implementer and is encouraged to challenge architectural choices because it knows its platform and agent-building infrastructure. It has discretion over technical implementation, hosting and repository layout within explicit security/role/data invariants.
- Grok may prepare and execute bounded work orders and collaborate internally without a lengthy prompt/approval loop. It must nevertheless record every important design/build decision, disagreement, test, blocker, PR and exact SHA in GitHub for Architect review. No unreviewed merge to canonical main.
- Architect/Matt review **milestone PR packets**, not every minor code/design choice. Grok should escalate only a material authority, license, secrets, safety or strategy-contract conflict; otherwise record ADR and continue.
- Prospective paper trading and NEO learning are priorities; G0 source rights/identity, exact stop rules and G1–G3 investment utility gates are not silently waived. The owner has not authorised live capital or a broker-writing path.

## Architecture decision
Use one coherent, versioned event/data contract across six roles; separate read-only NEO from the order path; T-Bot narrow paper order/reconciliation adapter; deterministic risk veto cannot be bypassed by M/R/LLMs. The recommended SQLite event ledger is an implementation starting point, not an enforced vendor choice if Grok documents and proves a better alternative.

## Sequence / owner availability
Run the pending narrow E-Bot correction and mock six-bot foundation in parallel; investigate the canonical trailing-stop specification and FMP entitlement without blocking independent mocked work. Build all interfaces early, deepen discovery, strategy/risk/manager/trader/NEO capabilities and schedule bounded paper-only observation only after operational evidence. Use [delivery roadmap](../../docs/equity-paper-delivery-roadmap.md), [Grok charter](../../docs/grokbot-paper-delivery-charter.md), [PID](../../docs/pid-equity-paper-system.md) and [first WO](../../work-orders/WO-PAPER-001-integrated-vertical-slice.md).

## Recovery
Grok's exact implementation work order and PR remain the authority for each bounded run, with approved work on branches only. Public investment GitHub is research/governance truth; private code and event/data repositories are implementation truth. Record status in README and CURRENT-STATE at each milestone. Prior dated decisions remain historical evidence; this decision changes future delivery authority only.
