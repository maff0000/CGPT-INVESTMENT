# EXECUTION-BOUNDARY-001 — Human authorisation and broker isolation
**Design only:** 2026-11-05. **Status:** NO LIVE ORDER AUTHORITY GRANTED.

## Authorisation states
RESEARCH PROPOSAL → COMMITTEE OPINION → PRIVATE HUMAN ORDER APPROVAL → INDEPENDENT PRE-TRADE RISK PASS → SIGNED/TIME-BOUNDED TICKET → BROKER ACCEPTANCE → FILL/CANCEL/REJECT RECONCILIATION → MONITORING.

**A positive AI recommendation does not authorise a purchase.** A research note, GitHub commit, daily scouting automation or hypothetical price trigger is **never sufficient** to execute. The person authorised to trade must explicitly approve the precise instrument, side, size, order type/price ceiling and expiration, under suitable account/manager terms. If such authorisation is absent, no broker call.

## Core architecture
- Research agents have **NO BROKER WRITING CREDENTIALS**. Only a separately approved execution service can communicate with an eligible broker API.
- Capital/risk rules are deterministic and independent; both **human approval and risk service approval** required. Neither can be overwritten by the research LLM.
- Broker API credentials kept in a secrets manager under least privilege and segregated environments. Read-only connections precede paper credentials; no leaked tokens to logs, prompts or public research GitHub.
- Pre-trade veto for unknown/mismatched account exposure, stale quotes, material earnings/event gate, order too large, insufficient cash, unauthorised instrument, unsupported order type, excessive limit deviation, aggregate correlation/drawdown breach, session halt or invalid signature.
- Orders are **idempotent** and auditable: immutable approval record, unique client order IDs, bounded TTL, exactly-once logical intent and explicit reconciliation of ambiguous API responses; automatic retries cannot create duplicates.
- Separate **kill switch** stops new submissions (and, if authorised, cancels open orders) on data/feed outage, failure of reconciliation, price excursion or a configured emergency. Escalate to human; risk limits cannot be silently raised by agents.
- Start with **adviser/manual execution** for externally managed portfolios where third-party direct trading isn't authorised; do not assume all accounts permit unattended API access.

## Acceptance gates before broker code is enabled
- Explicit separate permission to work on execution implementation and a confirmed compatible broker/account type.
- Independent code security review, threat model and fail-closed incident tests.
- Replay and paper-test failure cases: stale prices, duplicates, exchange holiday, split/delist, delayed release, out-of-order fills, partial fills, disconnection, unexpected order status and risk-limit breaches.
- Show audit-proven results of successful *reconciliation*, not just HTTP success.
- Controlled supervised live pilot with per-order human approval and stop conditions after formal risk acceptance. **Unattended autonomous discretionary trading is not part of the current authorisation.**

Reference professional control standards as engineering inspiration, **not an assertion that a particular retail account automatically falls within regulated-firm algorithmic trading obligations**: [UK FCA MAR 7A.3](https://handbook.fca.org.uk/handbook/mar7a/mar7as3), [FCA 2025 multi-firm review](https://www.fca.org.uk/publications/multi-firm-reviews/algorithmic-trading-controls-high-level-observations), [US SEC Rule 15c3-5](https://www.sec.gov/rules-regulations/2011/06/risk-management-controls-brokers-or-dealers-market-access).
