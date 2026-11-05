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
T-Bot identifier `81d8cf38-188e-4592-b08d-b59d6e461e83` is recorded as the existing assistant and is not modified. This session did not list or open the app. E, S, R, M and NEO have no recorded app identifiers. **BLOCKED** on parent provisioning.

## 4. Created and integrated
No new app agent was created by this session. No role is integrated with the private Python package. **Not IMPLEMENTED.**

## 5. Demonstration message
No demonstration message was sent. **BLOCKED** until the parent provisions teammates and supplies probes.

## 6. Role-permission tests
Not run. A read-only persona for NEO is not hard enforcement. **BLOCKED** until tested. Do not claim an access-control list.

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
| [WO-APP-PRESENCE-001](../../work-orders/WO-APP-PRESENCE-001-grok-bot-teammates.md) | Parent provisions native teammates. This session does not | Not started |
| [WO-DISCOVERY-001](../../work-orders/WO-DISCOVERY-001-broad-offline-fixtures.md) | Private paper-bots workstream | Authorised. Head pending |
| Screening requirements review | Later owner choices | Checklist only |
| Exact-head acceptance of this packet | Architect, after parent details arrive | Not started |

## Acceptance gate
Stop here. App identifiers, probes, a demonstration message, permission tests, and the private discovery head are still absent. Do not treat this packet as acceptance of app integration or of broad discovery.
