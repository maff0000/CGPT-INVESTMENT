# WO-PAPER-001 — first integrated six-bot vertical slice (mock-only)
**Parent PID:** [PID-EQUITY-PAPER-001](../docs/pid-equity-paper-system.md)
**Authority:** [GROKBOT-AUTONOMY-001](../docs/grokbot-paper-delivery-charter.md) · [ROADMAP-PAPER-001](../docs/equity-paper-delivery-roadmap.md)
**Approved by sponsor:** 2026-11-05 for bounded paper-only work. **Delivery owner:** GrokBot.
**Governance starting main SHA:** 6b5f3401c409d99896f41c97bac70119f5e848a5.
**Existing E-Bot canonical private main at dispatch:** 50c0b66247498672b84e9fcae7e417a538a0e5c1. E-Bot PR #2 9b843dee03892e73f29da31997e5d07bfed564a7 is unmerged HOLD and must not be represented as accepted main.
**Private implementation base:** record exact current branch/main SHA before implementation; if a new private repository is required, create a minimal bootstrap commit and log its SHA before adding implementation. If any baseline has moved, re-read and log before work. No unstated base.

## Scope
1. Grok determines an efficient private-only repo/layout and records a short ADR. Do not expose private implementation/source in public CGPT-INVESTMENT.
2. Define v0.1 schema for candidate, strategy verdict, skeptic verdict, paper manager decision, deterministic risk decision, synthetic order/fill and NEO review with canonical UTC provenance, common correlation IDs, rule/code versions, idempotency and bounded reason codes.
3. Implement minimal mocks/adapters for six roles and a deterministic non-LLM risk gate, with an append-only single shared event ledger (SQLite WAL or better justified equivalent) and separate minimal technical logs.
4. Execute exactly reproducible mock cases: (a) eligible candidate → strategy match → skeptic PASS → manager synthetic proposal → risk PASS → paper execution+reconciliation → NEO review; (b) hard earnings HOLD or invalid data → no trade; (c) no-signal session; (d) duplicate intent / ledger outage blocks safe continuation; (e) stopped/missing trailing rule results in HOLD, not invented stop.
5. NEO produces a machine-readable evidence packet and a private human summary distinguishing rule compliance at decision time from later simulated outcome. Produce sanitized aggregate-only GitHub status.
6. Unit, integration, privacy, injection/fault and role-isolation tests and a simple operator runbook in private repo.

## Exclusions
No Massive/FMP/IBKR live provider calls, real broker accounts or orders, real paper Gateway writes, live position imports, scheduled scan, paid provider onboarding, external runtime code fetch without inspection, hidden strategy tuning, source licence assumptions, unapproved stop parameters, personal holdings or licensed price history in public GitHub. No code changes to existing E-Bot open PR #2 under this WO (separate Stream A).

## Acceptance criteria
- Full six-role mock chain generates complete typed causal event ledger and NEO review with consistent UTC observation/decision/fill clocks.
- Every role's data/decision ownership and permissions proven by negative tests; NEO read-only, T-Bot paper-only, risk independent, no route to real order API.
- Both success and veto/no-signal paths, retries, duplicate intent and audit outage are tested. No false fill on acknowledgement.
- Synthetic stop-management path remains blocked until exact rules are proven; a stub can demonstrate stop-state validation without inventing parameters.
- A clean install/test command, no secrets in logs/public repo, private code PR with changed-file scope and exact head/base, independent test evidence and security review.
- Public GitHub gets only sanitized dated status and remaining blockers. Architect milestone acceptance is required before canonical merge.

## Delivery autonomy
Within these bounds, Grok may alter its implementation strategy, tools, local storage and deployment arrangement and document the decision in an ADR. Do not request routine per-step approvals. If blocked on one dependency, isolate with tests and continue another safe component. End with a single PR review packet.

## Progress addendum — 2026-11-05 (PROPOSED)
See [stream progress](2026-11-05-paper-stream-progress.md). Builder reports completion at paper-bots PR #1 head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`, with 48 tests passed on each of Python 3.9.25 and 3.12.3. That evidence is not an independent audit. This addendum does not change the original scope or acceptance criteria. Disposition of this work order remains **HOLD**.
