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
| E-Bot | Explorer | `53f42f0b-4b9e-429f-9317-6e7edf2d8e26` | Created. Bounded chat verified. Full integration partial |
| S-Bot | Strategist | `5cddba3b-38ff-49c8-8e9b-37b63efebe3c` | Created. Bounded chat verified. Full integration partial |
| R-Bot | Risk Skeptic | `76efa575-82b5-44c0-a0df-5647c78b0083` | Created. Bounded chat verified. Full integration partial |
| M-Bot | Manager | `59ccea20-1754-437f-8fa9-424ff18e5221` | Created. Bounded chat verified. Full integration partial |
| T-Bot | Trading | `81d8cf38-188e-4592-b08d-b59d6e461e83` | Existing. Reused unchanged. Received M-Bot's return |
| NEO | Independent Observer | `e1e372c8-20e9-45a6-856f-4eabdf018308` | Created. Second audit received. Full integration partial |

## 4. Created and integrated
Five app teammates are **PARENT-REPORTED created**. T-Bot already existed. Integration with the private Python package and the production ledger is **not verified**. Native profile text is not a hard access-control list. **Ledger bridge: UNVERIFIED.**

## 5. Demonstration message
The parent sent five priority typed acceptance probes. The first record was delivery acknowledgement only. Peer transcripts have since been read by a read-only executor, and the parent read the probe JSON and Markdown. Those files are not on this cloud session. Tool-call identifiers from the transcripts are not service receipt identifiers and are not republished here. No event hash is invented. Long peer payloads in the official transcript are abbreviated and are not a byte-exact archive.

**Parent-observed chat result, not a production pass.** Five distinct identity and refusal responses were actually received for E, S, R, M and NEO. E to S, S to R, and R to M each have a tool acknowledgement and an attributed downstream receipt in the peer transcripts. M to T has a tool acknowledgement. T, the current assistant, received M-Bot's full JSON return for task `APP-A-001-M-T`. The producer is M-Bot and the recipient is T-Bot. It is not T's own return. That return is a research HOLD only. Candidate identifiers `fixture:APP-A-001:001` and `fixture:APP-A-001:002` are unchanged. Symbols are `FIXTURE_ALPHA` and `FIXTURE_BETA`. Quality is UNCHECKED. Qualification is UNKNOWN. Entry is NONE. There was no proposal, risk-gate invocation, ledger write, fill or order. This shows the chat pipeline only. It is not production ledger, schema or broker integration. Correlation `APP-A-001` and envelope `native-probe-1` remain a provisional chat. **`native-probe-1` is not an accepted production ledger contract.**

**Chronology, recorded and not repaired.** The original fixture input `20:30:00 GMT` was 52 seconds ahead of E's actual `20:29:08 GMT`. S reused E's time and was not measured separately. R's actual stamp is `20:30:30 GMT`. M's `20:30:00` is an explicit minute-precision turn marker, not measured seconds. No latency or freshness claim is made. No time is corrected after the fact.

**NEO.** Audit `APP-A-NEO-001` returned `INCOMPLETE_EVIDENCE` for the empty chain, the future time, and the missing explicit risk stage. That result remains the valid historical record. Audit `APP-A-NEO-002` has now been received. Its verdict is **bounded native handoff evidence, partial; production ledger completeness unverified.** The gate state `NOT_INVOKED_NO_PROPOSAL` was never a pass. NEO reports no file, ledger, external, gate, proposal, order or fill action, and no production, trading or fill-readiness approval. JSON call identifiers are not service receipts. Immutable ledger parents, full unabbreviated payloads, production schema conformance, an enforced access-control list, a protected NEO runtime, and native Python ledger wiring are all **UNVERIFIED**.

## 6. Role-permission tests
Identity and refusal replies were received. That is not a passed permission test. A profile is not a hard access-control list. NEO's read-only role is not a tested runtime boundary. An authenticated producer binding is not verified. **No pass is claimed.**

## 7. Broad coverage
[WO-DISCOVERY-001](../../work-orders/WO-DISCOVERY-001-broad-offline-fixtures.md) now has a private head. [PR #4](https://github.com/maff0000/paper-bots/pull/4) is open and unmerged. Base `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d`. Head `a6aa7f32acc8531a06e3e36044a4b9003c888323`. Branch `cursor/broad-discovery-003-1e9e`. **PARENT-VERIFIED** metadata from a GitHub connector read-back. This session could not read the repository. Builder reports 91 tests passed on each of Python 3.12.3 and 3.9.25, and that count includes the previously accepted 82. The named work is an offline adapter, synthetic discovery, a NEO digest, a screening review, a rights matrix, and ADR 0010. Those results are **BUILDER**, not an Architect audit. Universe counts and exact coverage are **not in this public record**. The parent has requested the full private evidence, a fresh-process run, files, counts, coverage and security. That report is pending and may move the head. No real market data is published here.

## 8. Rights matrix
| Source | State |
|---|---|
| Offline fixtures | BUILDER-REPORTED at private head `a6aa7f32acc8531a06e3e36044a4b9003c888323`, path `docs/evidence/SOURCE-RIGHTS-003/matrix.md`. Contents not read here. No live pull |
| FMP | BLOCKED. Rights UNVERIFIED |
| Massive / other vendors | No new call. No licence assumed |
| Broker | BLOCKED. No writes, orders, or position reads |

## 9. Screening requirements
Public [checklist](../../docs/qarp-screening-requirements-review.md) is unchanged and approves nothing new. The private review at `docs/reviews/2026-11-05-screening-requirements-review.md` on head `a6aa7f32acc8531a06e3e36044a4b9003c888323` was not read here. Frozen QARP v1.0.0 is unchanged. Unknown metric mappings are not exact Finviz matches. Additional strategies are **NOT APPROVED**.

## 10. NEO
Logically read-only. Official platform documentation says bots of one user share one computer, its files and its logins, so an interface-level read-only flag is not a security boundary. Hard capability enforcement is **not tested**. Strong isolation would need a separate security principal, runtime and service. That boundary is **not implemented**. A JSON producer identifier is a claim only. **PROPOSED** behaviour, **BLOCKED** as a proven control.

## 11. Tests and security
Builder, not Architect: 91 tests passed on each of Python 3.12.3 and 3.9.25 at the private head above, including the accepted 82. A fresh-process confirmation is part of the pending full private report and is not claimed here. No vendor, broker, credential, account or scheduler action is reported for this build. App and ledger-bridge tests remain **BLOCKED**. Native probes are finished. NEO `APP-A-NEO-002` is already provided. No further peer actions are requested.

## 12. ADRs
Public [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md) records platform facts only. The builder cites private ADR 0010 at the discovery head. Its text was not read here. No new stop or risk value is adopted.

## 13. Pull-request heads and bases
| Pull request | Base | Head | State |
|---|---|---|---|
| This public milestone PR | `20094068e20c2de0a659e8243657207c8d4cfbaa` | the remote read-back after push | OPEN. Not merged |
| [paper-bots PR #4](https://github.com/maff0000/paper-bots/pull/4) | `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d` | `a6aa7f32acc8531a06e3e36044a4b9003c888323` | PARENT-VERIFIED open, not merged. Branch `cursor/broad-discovery-003-1e9e`. Not read here. Final private report may move the head |

## 14. Next work orders
| Order | Owner of the action | State |
|---|---|---|
| [WO-APP-PRESENCE-001](../../work-orders/WO-APP-PRESENCE-001-grok-bot-teammates.md) | Parent created five teammates and reused T-Bot. Peer replies and permission tests are still open | Created. Verification pending |
| [WO-DISCOVERY-001](../../work-orders/WO-DISCOVERY-001-broad-offline-fixtures.md) | Private paper-bots workstream | Head `a6aa7f32acc8531a06e3e36044a4b9003c888323` recorded. BUILDER tests. Full report pending |
| Screening requirements review | Later owner choices | Checklist only |
| Exact-head acceptance of this packet | Architect, after parent details arrive | Not started |

## Acceptance gate
The native creation, behaviour and chat evidence is **PARTIAL** against full integration. NEO `APP-A-NEO-002` is already received. No further native peer actions are requested. The 14 sections above now cite private PR #4. They are **begun, not final**: the full private evidence report is still pending and may update the head. Test counts and coverage claims in this file for that head are **BUILDER**, not Architect. No runtime access-control list, authenticated producer binding, protected read-only NEO, or accepted production ledger is claimed.
