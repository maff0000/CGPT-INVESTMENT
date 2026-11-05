# AGENT-SYSTEM-001 — Design an independent agent-driven equity investment pipeline
**Decision date:** 2026-11-05 Europe/London | **Status:** architecture accepted for requirements planning; **NOT implementation or live-trading approval**.

## Intent
Transform manual Finviz/SCOUT-002 research into a staged operating model: completed market close → trustworthy feeds → deterministic A/B/C and base/volume/sector features → AI-assisted fundamentals/news and independent critique → small decision-ready candidate packages → human + independent research committee decision → distinct explicit private order approval and deterministic pre-trade risk → broker execution only where authorised → reconciliation and outcomes/learning.

The existing [independent judgement rule](../../docs/independent-investment-challenge.md), [7+2 earnings gate](../../docs/earnings-risk-gates.md), [market scouting method](../../docs/pre-breakout-accumulation-scout.md), and QARP v2 A/B/C are unchanged. This architecture **adds governance, traceability, role separation, security and a feedback loop** rather than inventing a new investment signal.

## Non-negotiable
1. No assistant/agent access to place real orders because it wrote an attractive candidate.
2. A discretionary research decision is **not** a broker authorisation. Separate precise private human authorisation AND independent deterministic risk pass.
3. Public GitHub stores only neutral reusable methodology and public-company evidence; actual portfolio values, broker, identities, orders, credentials, positions, performance and private instruction must live elsewhere.
4. No fake real-time feeds, filled prices or verified Finviz exports. Data provenance and as-of time are mandatory.
5. No autonomous self-adjusting filters, weights or capital limits without a dated version and acceptance.
6. Fail-closed on unknown events, data, approval, reconciliation or infrastructure.
7. Performance monitoring must compare signal quality and *realised net investment results* against suitable benchmarks, distinguish hypothetical research returns, and log failures.

## Work order sequence recommended
- **ARCH-DATA-001:** licensed source/data model, exchange calendar, point-in-time OHLCV/fundamentals/replay, sector mapping and quality validations.
- **ARCH-SCOUT-002:** deterministic feature engine, A/B/C reproduction and pre-breakout 10/40 price-volume tests, sector context; maintain WATCH phases and chart classifications.
- **ARCH-QUAL-003:** LLM research agents for filings/earnings/news, sector-appropriate cash/PEG analysis, independent challenge and reproducible candidate reports.
- **ARCH-COMMITTEE-004:** short candidate packets, committee dispositions and dated audit trail.
- **ARCH-MONITOR-005:** separate research-signal outcomes and simulated portfolio lifecycle, shadow and paper execution.
- **ARCH-EXEC-006:** gated execution feasibility only **after** above proves reliable, with broker/adviser permissions, privacy architecture, independent risk controller, signed order ticket, audit, kill switch and reconciliation.

Each should have independent acceptance, quantitative quality metrics, privacy review and rollback gates. Do not begin live execution as part of a discovery Work Order.

Reference docs: [architecture](../../docs/agent-equity-operating-system.md), [candidate data contract](../../docs/candidate-evidence-contract.md), [order governance](../../docs/execution-authorisation-boundary.md), and [daily-scout runbook](../../docs/daily-equity-scout-runbook.md).
