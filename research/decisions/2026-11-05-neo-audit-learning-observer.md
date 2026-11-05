# NEO-LEARNING-001 — independent equity decision observer and evidence ledger
**Recorded:** 2026-11-05 (Europe/London)
**Owner direction:** Add an independent NEO that reviews paper trades, reconstructs why they were taken, analyses good/bad decisions and proposes targeted improvements. Matt and the Research Architect will review NEO's findings during shadow research.
**Status:** Architecture and evidence-contract decision accepted for paper/shadow design. Implementation NOT STARTED. No change to market-data rights or order authority.
**Related:** PAPER-SYSTEM-001, VALIDATION-FIRST-001 and MACRO-PROSPECTIVE-001.

## Decision and rationale
The trading workflow consists of E-Bot Explorer → S-Bot Strategist → R-Bot Skeptic → proposed M-Bot paper Manager → independent deterministic risk gate → T-Bot paper Trader/Reconciler. **NEO is a sixth, out-of-band read-only observer**; it does not sit in the approval path or trade pipeline and must not introduce latency or a circular self-approval path.

A collection of unrelated natural-language bot logs would be incomplete, hard to correlate and difficult to audit. Use **one shared, append-only, machine-readable event ledger** for all decision/evidence/state changes, plus short local per-bot operational diagnostics (health, retry, transport, stack traces privately, no secrets). Each producer owns and authenticates its own namespace; it may not update or delete prior events. NEO has read-only access to the canonical ledger and writes its own separately identified review events/reports. The executor/broker ledger remains the truth for fills, paper simulator for simulated fills; an LLM narrative cannot override either.

## Independent learning and safeguards
- Evaluate **process quality using only evidence available at decision time** separately from **ex-post outcomes**. A profitable but unjustified decision is not automatically good; a loss following a sound rule is not automatically a model defect.
- Examine positive, rejected, HOLD, missed, no-signal and expired candidates, including survivorship, earnings vetoes, UNCHECKED/INVALID_DATA and latency/data-source failures.
- Attribute observed issues to the correct E/S/R/M/risk gate/T stage where evidence supports it; label unverified causation as a hypothesis and collect counterevidence.
- Compare paper execution with plausible fills after detection, spread/fees/slippage, gap risk and explicit stop/entry strategy version; track 5/20/60-session prospective outcomes alongside sector, SPY and macro-blind baselines when observable.
- Every proposed improvement is a **change proposal**, never silently activated learning, strategy mutation, risk-limit adjustment or trade instruction. Matt/Architect approve a versioned rules amendment/work order, independent tests and prospective shadow evaluation before deployment.
- No authority to BUY, SELL, CLOSE, SIZE, move stops, edit risk rules, access broker credentials, alter the ledger, or make commits to protected main.
- This is an **equities-specific NEO deployment**; an existing NEO in a separate trading stack is a separate system. No automatic code, credential, model, dataset or broker-permission reuse.

## Storage and reporting decision
- **Paper MVP:** private SQLite WAL event table behind a single validated append interface (or equivalent atomic append-only ingestion), with JSON event envelopes and exportable JSONL for replay/NEO. Do not create a networked event bus just for six local roles. Store schema migrations and code versions in private GitHub; decision/event data and provider raw bars stay in a restricted private data directory/database with backups and retention controls.
- NEO reads a consistent event high-water mark and produces reproducible private trade-level evidence packs. Each report cites event IDs, immutable hashes, source/cutoff times and strategy versions.
- **GitHub review:** publish only redacted, non-identifying aggregate shadow findings and bounded change proposals in dated public research records, initially through a PR for Architect review. Never publish account details, order quantities, vendor price tables, raw order events, keys or licensed content in public GitHub. Detailed synthetic trade artifacts remain private.
- Keep this research journal and CURRENT-STATE/README updated with NEO review dates, results, corrections, rejected suggestions and accepted strategy versions. Never treat a report as an automatically accepted change.

## Initial verification gates
1. Freeze minimal shared schema and stage ownership; log each NO TRADE / HOLD / rejected case and provider/source quality, not only executions.
2. Prove causal correlation and UTC event ordering across all bots and each paper order; test duplicate messages, missing parent, out-of-order events, partial fills, stop modification, a failed producer and tamper attempt.
3. Prove NEO can replay the original decision using point-in-time inputs and produce a disconfirming explanation without looking ahead.
4. Prove NEO suggestions cannot alter active settings and no bot can submit live orders. Operator-controlled kill switch is testable.
5. Independently review a first batch of paper decisions/rejections with Matt before authorising unattended NEO GitHub report drafts.

See [event schema and operating contract](../../docs/neo-decision-event-ledger.md) and [existing paper architecture](../../docs/paper-five-bot-architecture.md).
