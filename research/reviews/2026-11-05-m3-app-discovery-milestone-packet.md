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
The sections above that name head `a6aa7f32acc8531a06e3e36044a4b9003c888323` record the head before the final private report. The final builder head is below. Native probes are finished. NEO `APP-A-NEO-002` is already received. No further native peer actions are requested.

## Final 14-item milestone packet — builder report, not an Architect audit
**Disposition:** **READY FOR ARCHITECT REVIEW of the bounded fixture only. Overall integration PARTIAL. Operational HOLD. Not accepted.** This session could not read private paper-bots (HTTP 404 on this credential only). The parent separately read accepted E-Bot `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` on GitHub this turn. That is not a global access block. Builder reports local head, origin branch and pull-request head match, and that private main is unchanged.

### 1. Starting heads
| Ref | SHA | Class |
|---|---|---|
| Public main | `20094068e20c2de0a659e8243657207c8d4cfbaa` | VERIFIED this session. Merge of PR #7 |
| Public PR #8 before this packet | `3ae374b4458d135c7efcb15042cbf6252a24c738` | VERIFIED this session |
| Paper-bots accepted main | `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d` | PARENT-VERIFIED. Not read here |
| E-Bot accepted main | `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | PARENT-VERIFIED this turn. Not read by this credential |
| Earlier recorded PR #4 head | `a6aa7f32acc8531a06e3e36044a4b9003c888323` | Superseded by the head in item 3. Not deleted from the earlier note |

### 2. Native identities, probe and NEO
Five created teammates and reused T-Bot `81d8cf38-188e-4592-b08d-b59d6e461e83` are already recorded. E to S to R to M have acknowledgements and downstream receipts. T received M-Bot's return for `APP-A-001-M-T`, not T's own return. `APP-A-NEO-001` remains historical `INCOMPLETE_EVIDENCE`. `APP-A-NEO-002` is bounded handoff evidence, partial, and production ledger completeness is unverified. No further native actions are requested. Chat is not a ledger bridge.

### 3. Private head and base
[PR #4](https://github.com/maff0000/paper-bots/pull/4). Branch `cursor/broad-discovery-003-1e9e`. Base `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d`. Head `ad5e30ae5502d77d8beec3399845f64116ff8702`. OPEN. Not merged. Not read here.

### 4. Files
Private paths at that head: `docs/work-orders/WO-PAPER-003-broad-discovery.md` (native appendix included), `docs/adr/0009-offline-broad-discovery.md`, `docs/adr/0010-native-role-contract.md`, `docs/reviews/2026-11-05-screening-requirements-review.md`, `docs/evidence/SOURCE-RIGHTS-003/matrix.md`, `fixtures/discovery/source_rights_v0.json`, `fixtures/discovery/us_equity_fixture_v0.json`, `fixtures/discovery/us_equity_fixture_zero.json`, `docs/status/2026-11-05-broad-discovery-sanitised.md`. Other changed areas, 20 files in total: README, schema 0.2, access, constants, discovery prepare and run, native contract, schema utility, and `tests/test_discovery.py`. Contents are not published here.

### 5. Implemented synthetic coverage — BUILDER
17 rows, 16 instruments, all 11 GICS sectors. This is not the actual listed US universe. Counts: 10 ADMITTED, 1 EXCLUDED (OTC), 1 UNKNOWN for missing freshness, 1 INVALID non-finite, 1 UNCHECKED survivor, 1 DATA_MISMATCH, 1 SOURCE_UNAVAILABLE. Dedup of one member preserves both sources. `seven_name_cap` is false. QARP is not applied to discovery. Documented exclusion classes are NON_US_PRIMARY, OTC, WARRANT, PREFERRED, ETN and BLANK_CHECK. Not every class is claimed to have been exercised by the fixture.

### 6. Screening — BUILDER
11 screen examples: verified, near-miss, non-match and unknown are demonstrated. An unsupported Finviz mapping is UNKNOWN. Frozen manifest hash `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged. Source survivors are screened as UNKNOWN. That choice is not an approved rule.

### 7. NEO digest — BUILDER, not an Architect reproduction
Readable text and machine evidence. The batch has 16 member identifiers and hashes. There are 11 screen identifiers and hashes, plus a cohort. The demo clock is synthetic `2026-11-10T14:30Z`, not an actual market snapshot. Run `acceptance-demo` has 41 events. The chain is reported OK. Tip `f2a8986fa1726cf947797f0ba2108a13b29b3eb39aa71712988d2377a19e73db`. `DISCOVERY_BATCH` `5c1e3588-304b-56bb-8e10-ca6bc10a285c`. `NEO_COHORT` `afdec7f3-6ba8-51b6-bdc4-b1f79b37c022`. Digest `8a609995-05fb-514e-995a-f0ff2e3efeaa`. The in-process Python NEO still appends that digest. It has an in-memory snapshot and no write method on the native role. That is not hard isolation, and it is not a write by the native NEO. **Material deviation, reported as such.**

### 8. Tests — BUILDER
Fresh detached worktree at exact `ad5e30ae5502d77d8beec3399845f64116ff8702`: 91 passed on Python 3.12.3 and 91 passed on Python 3.9.25, including the accepted 82. This is **not** an Architect Python 3.12.14 audit. Named coverage includes many names, no seven-cap, all sectors, zero, dedup, unknown, source failure, outage atomicity, semantic replay, provenance reject, rights, and the native envelope. Native offline envelopes are `SYN-APA01` and `SYN-APA02`. They are not the `APP-A` fixture identifiers, because the native chat was not re-executed. No bridge is claimed.

### 9. Rights
No provider entitlement is asserted. The three historical FMP calls remain the record. Further FMP calls are false. Rights stay UNVERIFIED. No new vendor call.

### 10. Owner choices still open — NOT APPROVED
Lawful actual-universe source. Whether UNCHECKED survivors are screened as UNKNOWN or held out. Whether sector-relative strength, earnings and chart stage become predicates. Seven research labels are not approved as strategies. FAIR-VALUE-COMPOUNDER-002 is not approved. Chart state is CHART_PENDING. Entry is NONE. Existing frozen QARP criteria are reviewed and not edited. New strategies and a scheduler stay blocked pending that review and verified rights.

### 11. Security limit
The builder's check is a limited import scan and a socket patch around the older scenarios. It is not a policy host audit and not a full network test of the new discovery path. There is no credential host scan and no app access-control proof. The diff reports no broker write, account query, vendor call, scheduler, new risk parameter or new credential.

### 12. ADRs
Private ADR 0009, offline broad discovery, and ADR 0010, native role contract, are cited by path at this head. They were not read here. Public ADR-APP-001 remains the platform-facts record. No new stop or risk value is adopted.

### 13. Public pull request
This packet is on PR #8. Base `20094068e20c2de0a659e8243657207c8d4cfbaa`. The head before this commit was `3ae374b4458d135c7efcb15042cbf6252a24c738`. The head after the push is the remote read-back. OPEN. Not merged.

### 14. Readiness and next work
**READY FOR ARCHITECT REVIEW of the bounded synthetic fixture only.** Overall integration remains **PARTIAL**. Operational state remains **HOLD**: G0 open, FMP rights unverified, May source unrecovered, doctrine unapproved, entry and stop policy unapproved, stop-dependent M/T on hold, no scheduler and no live execution. The public [screening review](../../docs/qarp-screening-requirements-review.md) now shows the frozen A/B/C predicates from the public registry. The private documentation-only transcription of the accepted manifest is requested and its head is **not claimed**. The 91 core tests are unchanged. One acceptance gate follows that documentation. App presence remains [WO-APP-PRESENCE-001](../../work-orders/WO-APP-PRESENCE-001-grok-bot-teammates.md) and is not a completed security boundary.
