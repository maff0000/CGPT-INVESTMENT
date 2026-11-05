# Equity paper system — accelerated integrated delivery roadmap
**ID:** ROADMAP-PAPER-001 | **Approved direction:** 2026-11-05 | **Owner:** Matt
**Parent:** [PID-EQUITY-PAPER-001](pid-equity-paper-system.md) | **Autonomy:** [GrokBot delivery charter](grokbot-paper-delivery-charter.md) | **Launch WO:** [WO-PAPER-001](../work-orders/WO-PAPER-001-integrated-vertical-slice.md).
**Status:** BUILD AUTHORIZED UNDER BOUNDED PAPER-ONLY WOs; no milestone accepted yet.

## Progress snapshot — PROPOSED 2026-11-05
No milestone below is accepted. Details and dispositions: [consolidation index](../research/reviews/2026-11-05-six-bot-consolidation-index.md).

- **M0 E-Bot code:** Architect accepted and merged head `3aa95daffe1497725aba8dbd80d4005d5afde16c` as `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`. Code only. G0 stays OPEN. This snapshot did not re-fetch the private main.
- **M0 stops:** the authorised read-only recovery attempt is complete. July brief v0.3 and July architecture v2 were reported recovered in full at private argus `46b4d8c8f17490357c6d1536c5027e45341b7f11` and are not approved. The full May Trade doctrine was not recovered. Conflicting legacy profiles and that access gap are **NEED OWNER DECISION/ACCESS**. Stop-dependent M/T management stays HOLD. No further access.
- **M0 FMP:** three operator-reported read-only calls. Entitlement and rights UNVERIFIED. No further calls.
- **M1:** Architect HOLD remains on audited head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`. Builder reports correction head `823203059466a30a11fe5a0e677f54c5482dc6fb` with 52 tests passed on each of Python 3.12.3 and 3.9.25. Not re-audited. **HOLD**.
- **QARP-ROTATION-001 v1.0.0:** the screening specification is on main. Architect HOLD remains on audited head `b6b7877884df6edc624691b50bb474b2b518ded8`. Builder reports correction head `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` with 66 tests passed on each interpreter. `entry_authority` NONE. Not re-audited. **HOLD**.

## Guiding principle
**Deliver one thin working vertical slice across all six bots early**, then deepen E/S/R/M/T/NEO in parallel where shared contracts are stable. Do not wait months for prospective alpha proof before writing paper software, but do not confuse passing tests or simulated P&L with validated investability. No live orders. Grok chooses the most effective implementation details and documents its reasoning, including challenges to this roadmap.

| Milestone | Work to deliver | Gate / concrete acceptance |
|---|---|---|
| **M0 — Close G0-D3 safely** | Fix exact three malformed-data classification paths on private ebot PR #2 and supply production-wire negative tests, no extra live calls; independently discover the canonical historical entry/exit/trailing-stop document; bounded FMP Stable API entitlement/restriction assessment if key available | E-Bot exact-head corrected PR awaits independent Architect acceptance; no false INVALID_DATA↔UNAVAILABLE; stop source path/version identified or explicit unresolved record |
| **M1 — Foundation + full chain** | Private repo/layout ADR; versioned E/S/R/M/risk/T/NEO contracts; shared append-only event interface; minimal deterministic fixture-driven run through all roles and NEO report; README/run commands and private/public separation | One complete mock candidate and NO-TRADE case traverses all six; UTC causal ledger, idempotency, isolated permissions, no live broker hooks; independent tests and audit evidence |
| **M2 — Broad discovery** | US universe and source licences; FMP trial/batch/filter limits; Massive/IBKR where approved; screen and 260-bar/sector/valuation feature quality; dedup; full candidate/reject ledger, ranked human digest | Reproducible universe/cutoffs, all credible candidates retained, zero-signal cohorts recorded; no provider rights assumption, intraday only if actually entitled; incomplete source produces UNCHECKED and risk blocks |
| **M3 — Strategy, skepticism and management** | S-Bot registered QARP/accumulation/trend/compounder strategies with explicit predicates; R-Bot macro/news/earnings adversarial challenge; M-Bot candidate selection, entry/exit/initial-moving SL (only after recovered/frozen rules); deterministic risk veto | Versioned strategies, explainable stage transitions, two disconfirming risks, hard earnings gate and repeatable stop transitions; every HOLD/REJECT logged; no rule self-modification |
| **M4 — Paper execution + NEO depth** | T-Bot deterministic synthetic order simulator, fill/partial/cancel/replace and risk gate; NEO causal post-trade/no-trade review, missed-winner and disagreement analysis; human-shadow comparison and sanitized GitHub PR report | >=50 adversarial synthetic lifecycle scenarios, independent reconciler, no live order API, NEO report reproduces known-time reasoning distinct from later results; no auto strategy edits |
| **M5 — Scheduled shadow operation** | Controlled scheduler during permitted US session windows (and EOD confirmation) using only verified data rights; source health, no-signal and error reports, operator stop/kill; daily/weekly NEO reports and retrospective human comparison | First 20 completed US sessions of prospective logs, clear as-of timestamps, complete rejects/misses, failsafe outage behaviour, measured operational health. G1–G3 prospective utility remains open |
| **M6 — Evaluation and controlled iteration** | Identify weak rules and false positives, compare SPY/sector/macro-blind baselines, version rule change proposals and deliver small WOs | Matt + Architect accept/reject change with evidence; no performance claims without prospective data; live trading remains a separate future PID/decision |

## Frozen first S-Bot strategy — M3 dependency clarification
Matt selected [QARP-ROTATION-001 v1.0.0](sbot-strategy-registry.md) (Finviz QARP Discovery v2 A/B/C) as the first S-Bot screening and qualification strategy. Implementation can start alongside M1/M2 using deterministic mocks, then real permissioned data only when provider mapping, timestamps and rights are evidenced. The strategy is **not** an entry/exit or stop doctrine. Preserve separately labelled near-misses/premium exceptions and all rejected/unknown cohorts for NEO; no maximum on credible discoveries. Second fair-value-led strategy stays PROPOSED pending a complete quantitative specification. Stop-dependent M/T management stays HOLD pending STOP-RULE-RECOVERY-002 acceptance; other M3 work may proceed. [Decision](../research/decisions/2026-11-05-sbot-first-strategy.md).

## Parallelism and dependencies
- M0 E-Bot correction may run **in parallel** with M1 private mocked vertical-slice foundation. Do not import an unaccepted PR head as accepted canonical code. Use interface stubs until E-Bot is accepted.
- M2 discovery and M3 independent strategy/risk components may proceed in parallel once M1 schemas are frozen. Stop-dependent M-Bot logic stays stubbed/HOLD until exact rule is recovered.
- NEO event parsing and evaluation harness start in M1, **not** after trading is complete. Detailed NEO quality review, T-Bot simulator and manual shadow worksheets deepen in M3–M4.
- M5 scheduling only after M2–M4 operational tests and data entitlement evidence; every session must be labelled INTRADAY PROVISIONAL vs COMPLETED SESSION. No broker-writing connection is included.
- Faster alternative sequencing is welcome: Grok must write an ADR with impact, benefit and test plan, then proceed if invariants remain intact.

## Work-order and milestone cadence
1. Grok fetches exact GitHub HEADs, reads README/AGENTS/CURRENT-STATE/PID/roadmap/NEO and stop-rule/G0 reviews, creates a **bounded WO** per implementation milestone/independent component with actual parent decision, exact repository base SHA, changed scope, exclusions, tests, security checks, acceptance and rollback.
2. Grok can **execute approved-roadmap paper-only WOs without asking for routine per-step permission**. It owns technical choices and ADRs, may commit freely to feature branches and open PRs, but must not merge those PRs to canonical main.
3. Each milestone PR contains code, test evidence, private redacted log examples, data-source rights checks, architectural deviations, security audit, limitations and exact head/base. Only ask Architect/Matt at milestone review or a true stop condition.
4. GitHub is the handoff truth: update public sanitised CURRENT-STATE/README at each milestone and private code README/ADRs/WOs at each increment; NEVER leave rationale solely in chat or a Grok session.
5. If provider credentials, licences, numerical rules or safe paper execution are missing, record BLOCKED with a tested stub and proceed with unrelated milestones. Do not manufacture data or silently weaken a check.

## Explicit out of scope
Actual capital, personal account details on public GitHub, real orders, automatic approval to trade, broker stop order deployment, production execution credentials, leverage/shorting, speculative auto-tuning, public redistribution of market-data dumps, system-host changes unrelated to this project.
