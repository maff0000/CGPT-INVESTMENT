# M3 milestone packet — app teammates and broad discovery
**ID:** REVIEW-M3-001
**Date:** 2026-11-05 (Europe/London)
**Public base verified this session:** `20094068e20c2de0a659e8243657207c8d4cfbaa` (`origin/main`, merge of [PR #7](https://github.com/maff0000/CGPT-INVESTMENT/pull/7))
**This packet:** a new governance pull request. It does not edit the merged PR #7 history.
**Private objects:** this session received not-found for `maff0000/paper-bots` and `maff0000/ebot`. The parent states those mains were verified on GitHub. That is **PARENT-VERIFIED**, not a read-back by this session.

Labels used below: **VERIFIED**, **PARENT-VERIFIED**, **IMPLEMENTED**, **PROPOSED**, **BLOCKED**. Nothing in the app or discovery workstream is **IMPLEMENTED** yet.

## 1. Starting heads
| Ref | SHA | Class |
|---|---|---|
| Public main | `20094068e20c2de0a659e8243657207c8d4cfbaa` | VERIFIED |
| Merged PR #7 head | `f977a7d255f8c1d2ae94ec4ae9c2660012ff2878` | VERIFIED from the merged pull request |
| Paper-bots accepted main | `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d` | PARENT-VERIFIED. Not read here |
| E-Bot accepted main | `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | PARENT-VERIFIED. Not read here. Code only. G0 OPEN |

## 2. Platform findings
Recorded in [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md). Creating an agent creates an individual messageable agent. A handoff is asynchronous. The description shapes instructions and is **not proven** as a hard tool access-control list. The same box shares a filesystem. No Python attachment and no production ledger write bridge are verified. **PROPOSED** until probes arrive.

## 3. Actual bots
**PARENT-REPORTED 5 Nov.** This session did not create the agents and did not open the app. Five teammates were created. T-Bot was reused and not modified. No extra T-Bot was created.

| Role | Name | Identifier | State |
|---|---|---|---|
| E-Bot | Explorer | `53f42f0b-4b9e-429f-9317-6e7edf2d8e26` | Created. Handoff verification pending |
| S-Bot | Strategist | `5cddba3b-38ff-49c8-8e9b-37b63efebe3c` | Created. Handoff verification pending |
| R-Bot | Risk Skeptic | `76efa575-82b5-44c0-a0df-5647c78b0083` | Created. Handoff verification pending |
| M-Bot | Manager | `59ccea20-1754-437f-8fa9-424ff18e5221` | Created. Handoff verification pending |
| T-Bot | Trading | `81d8cf38-188e-4592-b08d-b59d6e461e83` | Existing. Reused unchanged |
| NEO | Independent Observer | `e1e372c8-20e9-45a6-856f-4eabdf018308` | Created. Handoff verification pending |

## 4. Created and integrated
Five app teammates are **PARENT-REPORTED created**. T-Bot already existed. Integration with the private Python package and the production ledger is **not verified**. Native profile text is not a hard access-control list. **Ledger bridge: UNVERIFIED.**

## 5. Demonstration message
The parent sent five priority typed acceptance probes. Only delivery acknowledgement is reported so far. Real peer replies are pending. **No pass is claimed.** The probes ask each role for a capability and restriction report, and for an out-of-authority rejection, without a dangerous action. They use two synthetic UNCHECKED candidates, `FIXTURE_ALPHA` / `fixture:APP-A-001:001` and `FIXTURE_BETA` / `002`, inside a provisional `native-probe-1` envelope. That envelope carries task, correlation, producer, recipient type, time, session, source and a paper-only payload. The requested chain is one hop per role, E to S to R to M to T, correlation `APP-A-001`. NEO first receives an empty chain and should report `INCOMPLETE_EVIDENCE`, then later evidence of actual receipt. The probes include no vendor data, repository access, credential, ledger write, gate execution, paper fill or broker operation. **`native-probe-1` is not an accepted production ledger contract.** Handoff verification remains **pending**.

## 6. Role-permission tests
Not passed. The probes request the reports and the out-of-authority rejections. Peer replies have not arrived. A profile policy is not a hard access-control list. NEO's read-only role is still not a tested enforcement. **Pending.**

## 7. Broad coverage
[WO-DISCOVERY-001](../../work-orders/WO-DISCOVERY-001-broad-offline-fixtures.md): offline US fixtures, no QARP cap on the universe, no seven-name cap, stable identifiers, provenance, dedup, unknowns, UNCHECKED survivors, NEO trace, human and machine evidence. Private head **not supplied**. **PROPOSED.**

## 8. Rights matrix
| Source | State |
|---|---|
| Offline fixtures | PROPOSED. No live pull |
| FMP | BLOCKED. Rights UNVERIFIED |
| Massive / other vendors | No new call. No licence assumed |
| Broker | BLOCKED. No writes, orders, or position reads |

## 9. Screening requirements
[Checklist](../../docs/qarp-screening-requirements-review.md). Frozen QARP v1.0.0 is unchanged. Unknown metric mappings are not exact Finviz matches. Additional strategies are **NOT APPROVED**. Owner choices remain open. **PROPOSED.**

## 10. NEO
Logically read-only. Hard capability enforcement is **not tested** and is not claimed from the persona. **PROPOSED** behaviour, **BLOCKED** as a proven control.

## 11. Tests and security
No new test run belongs to this milestone. No vendor, broker, credential, account, or scheduler action. **BLOCKED** for app and ledger-bridge tests.

## 12. ADRs
Public [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md) records platform facts only. A private discovery ADR is **not supplied**. No new stop or risk value is adopted.

## 13. Pull-request heads and bases
| Pull request | Base | Head | State |
|---|---|---|---|
| This public milestone PR | `20094068e20c2de0a659e8243657207c8d4cfbaa` | the remote read-back after push | OPEN. Not merged |
| Private discovery implementation | `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d` named as the start | **NOT SUPPLIED** | Not invented. Not complete |

## 14. Next work orders
| Order | Owner of the action | State |
|---|---|---|
| [WO-APP-PRESENCE-001](../../work-orders/WO-APP-PRESENCE-001-grok-bot-teammates.md) | Parent created five teammates and reused T-Bot. Peer replies and permission tests are still open | Created. Verification pending |
| [WO-DISCOVERY-001](../../work-orders/WO-DISCOVERY-001-broad-offline-fixtures.md) | Private paper-bots workstream | Authorised. Head pending |
| Screening requirements review | Later owner choices | Checklist only |
| Exact-head acceptance of this packet | Architect, after parent details arrive | Not started |

## Acceptance gate
Five identifiers and five delivery acknowledgements are recorded. Peer replies, permission results, a ledger bridge, and the private discovery head are still absent. Do not treat this packet as acceptance of app integration or of broad discovery.
