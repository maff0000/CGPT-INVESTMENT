# PID-EQUITY-PAPER-001 — AI-first equity discovery, paper trading and learning
**Owner:** Matt | **Architect:** CGPT | **Delivery lead:** GrokBot
**Date/authority:** 2026-11-05, Europe/London — sponsor-approved integrated paper-only build.
**Parent decisions:** PAPER-SYSTEM-001, NEO-LEARNING-001, VALIDATION-FIRST-001 as amended for paper builds.
**Status:** APPROVED DELIVERY DIRECTION, NOT OPERATIONAL ACCEPTANCE.

## Why
Build a reusable, personally operated, evidence-led equity research and simulated-trading system. Discover every credible US stock opportunity, test defined strategies, independently challenge risk and macro exposure, model rigorous entry/exit/stop management, execute synthetic orders, and learn continuously from all decisions, including rejections and missed opportunities. The system is internal/personal, not for commercial redistribution.

## What — six bounded specialist roles
- **E-Bot Explorer:** broad lawful universe, data validation, source corroboration, full candidate/reject history.
- **S-Bot Strategist:** versioned owner-approved strategy rules with deterministic predicate evidence; no undisclosed rule invention.
- **R-Bot Skeptic:** primary news/earnings and in-time macro risk challenge with a reasoned PASS/HOLD/REJECT.
- **M-Bot Manager:** sponsor now **approves a distinct M-Bot** for paper-only decision coordination, hypothetical entries, exits, initial and moving stops, portfolio constraints, and why/not-trade decisions.
- **T-Bot Trader:** isolated paper-order simulator/adapter, lifecycle, cancel/replace and reconciliation. No independent discretionary decisions.
- **NEO Observer:** independent, read-only, point-in-time causal review and prospective outcome learning from the complete ledger; proposes improvements for human review, cannot enact changes.
A non-LLM **deterministic risk gate** sits before T-Bot. Matt/CGPT shadow, inspect evidence and approve policy changes. One shared typed, append-only decision event ledger links all roles, plus minimal per-bot technical logs.

## Non-negotiable boundaries
- **PAPER ONLY** for every order and position. No production broker write credentials, live account orders, personal portfolio account integration, leveraged or short trading, or inference of a future live mandate.
- Existing E-Bot market-data access stays read-only and must not disrupt shared IBKR Gateway clients. Its G0-D3 PR #2 is OPEN/HOLD. Builder-reported head `3aa95daffe1497725aba8dbd80d4005d5afde16c` is not independently accepted. See the [consolidation index](../research/reviews/2026-11-05-six-bot-consolidation-index.md).
- The owner recalls exact entry/exit/stop/trailing rules previously documented; recover provenance and version before using them for active paper position management. If absent, block only the dependent trade-management path, not mock contract work.
- Respect 7-session pre-earnings + announcement day block and 2 fully completed sessions post-event, as well as unknown-source and source-disagreement holds. Surviving valid single-source data remains research-visible as UNCHECKED; it never clears a trading permission.
- Licensed data and secrets remain outside public GitHub. Public journal includes sanitised methodology/status; private GitHub and restricted private data hold code, audit events and synthetic positions.
- No hindsight data in decision-time records. NEO recommendations require reviewed, versioned forward trials. Paper results are **not** proof of investment alpha, which remains subject to G1–G3 prospective comparison.

## Success criteria for first operational shadow pilot
1. All six roles exchange versioned evidence packets, including no-signal and reject cases, without shared writable brokerage authority.
2. Deterministic synthetic entry→fill→stop change→exit/cancel paths are fully reconcilable; risk/stop policy unknowns cause HOLD.
3. Complete event lineage with UTC observation/decision/fill time, source validity, immutable strategy/agent versions and NEO review; failure to log blocks dependent paper action.
4. Broad credible discovery with full universe/rejection ledger and ranked digest; no artificial seven-name maximum or padded candidates.
5. Offline fail-closed negative cases for source outage vs invalid payload, unknown earnings, duplicated orders, stale prices, shared Gateway isolation, split/corporate actions, stop widening, partial fills and data loss.
6. Initial prospective supervised paper observation target: 20 completed US sessions and 50 synthetic order-lifecycle tests, as *operational* evidence, with baseline/sector/macro-blind comparisons continuing beyond.

## Delivery ownership
GrokBot may choose its native frameworks, service topology, repo structure, languages, storage and hosting in **private** scope; the initially recommended local SQLite WAL event store can be replaced by a superior demonstrated design through a dated ADR. GrokBot should actively challenge weak architectural assumptions. Only risk/trading boundaries, personal data, licence/secret restrictions and exact strategy authority are immutable without owner approval.

Implementation authority is delegated **within the companion autonomy charter and roadmap**, through Grok-authored bounded Git-tracked work orders and milestone PRs. Architect acceptance occurs at milestone PR boundaries, not each engineering decision. No code merge to protected/canonical main without Architect acceptance. Initial work order: WO-PAPER-001.
