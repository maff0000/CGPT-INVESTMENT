# Six-bot consolidation index — sanitised review packet
**ID:** REVIEW-PAPER-INDEX-001
**Date:** 2026-11-05 (Europe/London)
**Status:** **PROPOSED** pending acceptance of this documentation pull request. Do not merge it as software acceptance.
**Public base verified by this session:** `a64c2f1d96a13f16963d8835713434c2be67c6f6` (`origin/main`, merge of [PR #6](https://github.com/maff0000/CGPT-INVESTMENT/pull/6))
**Documentation branch:** `cursor/paper-governance-progress-6067`
**Decision:** [PAPER-PROGRESS-001](../decisions/2026-11-05-paper-progress-sanitised.md)
**Progress log:** [WO progress](../../work-orders/2026-11-05-paper-stream-progress.md)

This session did not clone a private repository, copy implementation, run a private test suite, make a vendor or broker call, or invent a missing pull-request URL.

## Source SHAs

| Source | Exact identifier | Evidence class | Role in this packet |
|---|---|---|---|
| Public main | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | VERIFIED here | Merge PR #6, 2026-11-05 17:44:54 UTC. [Commit](https://github.com/maff0000/CGPT-INVESTMENT/commit/a64c2f1d96a13f16963d8835713434c2be67c6f6) |
| PR #6 head | `b7c81d730a9a61d53776c8729eb4556e091f0cf1` | VERIFIED here | Branch merged by that commit |
| Prior main (PR #6 first parent) | `fa87e83834643316ff1f1a87a8438b11a336ca1f` | VERIFIED here | Merge PR #4. Starting main named on [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5) |
| E-Bot PR #2 base | `50c0b66247498672b84e9fcae7e417a538a0e5c1` | REPORTED | Base of open [PR #2](https://github.com/maff0000/ebot/pull/2). Matches the base in the earlier public review |
| E-Bot last independent public review | `9b843dee03892e73f29da31997e5d07bfed564a7` | VERIFIED in [that review](2026-11-05-g0-d3-pr2-architect-hold.md) | Historical HOLD for that head only |
| E-Bot superseded reported head | `adb605fd676d06cf27830f35bf39c06d92d6a119` | REPORTED | Superseded before this packet was committed. Not independently reviewed |
| E-Bot current reported candidate | `3aa95daffe1497725aba8dbd80d4005d5afde16c` | REPORTED | OPEN / UNMERGED. Supersedes `adb605fd…`. Awaiting Architect acceptance. Not accepted |
| Private paper-bots bootstrap | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | REPORTED | Bootstrap only. Repository URL, ADR SHA and any later head were not supplied and were not resolved |
| July brief v0.3 and July architecture v2 | private argus `46b4d8c8f17490357c6d1536c5027e45341b7f11` | REPORTED | Full texts recovered read-only. Recovery report says hashes matched the compared copies. Not approved. This session did not re-fetch the commit or recompute the hashes |
| May Trade doctrine, full source | ACCESS GAP | REPORTED | Full text not recovered. Only the previously cited one-line excerpt, which lacks vol-band parameters. This is not proof that no rule ever existed |

## E-Bot PR #2 — builder evidence and independent evidence

PR: https://github.com/maff0000/ebot/pull/2
State reported with this update: **OPEN / UNMERGED**. Awaiting Architect acceptance. This packet does not accept it.

### Builder-reported (not replayed here)
Current head `3aa95daffe1497725aba8dbd80d4005d5afde16c` supersedes `adb605fd676d06cf27830f35bf39c06d92d6a119` on the same PR. Base `50c0b66247498672b84e9fcae7e417a538a0e5c1`.

| Builder report | Value |
|---|---|
| Tests | 112 collected; 111 passed; 1 pre-existing skip |
| Interpreters | Python 3.9.25 and 3.12.3 |
| Live calls | Zero |
| Files changed this round | `ebot/massive.py`, `ebot/reconcile.py`, `tests/test_reconcile.py`, `docs/redacted-g0-d3-acceptance.md` |
| Non-object grouped rows | Provider diagnostic `malformed_row` maps to `INVALID_DATA` when the symbol has no attributed row. The ticker is not inferred |
| Valid object peers | Remain `PRICE_OK` |
| Empty results | Remain `UNCHECKED` |
| Regression tests | Three tests through `urllib_send` |
| Automated trading | Remains false |
| Earlier head `adb605fd…` | Builder then reported 109 tests, 108 passed, 1 skipped, and a remaining silent skip of non-object grouped rows. That head and that gap report are superseded by the claims in this table |

The earlier builder claim that the HTTP non-object JSON mapping, the provider-level non-text ticker diagnostic, and the IBKR invalid-date path were fixed was attached to superseded head `adb605fd…`. This session has no diff between the two heads, so those three fixes are not re-certified at `3aa95daf…`.

### Independent evidence from this session
| Check | Result |
|---|---|
| Read `maff0000/ebot` at `3aa95daffe1497725aba8dbd80d4005d5afde16c` | Not done. Git and the GitHub API both returned repository-not-found for this session's credential |
| Diff of the four named files | Not read |
| Re-run of the reported 112 tests | Not run |
| Live vendor or broker calls by this session | None |
| Comparison of `3aa95daf…` with `adb605fd…` or `9b843de…` | Not performed |
| Code acceptance | Not granted |

The last independent review in this public journal remains the HOLD at `9b843dee03892e73f29da31997e5d07bfed564a7`: 105 offline tests passed on Python 3.12.14, and three malformed-response classifications were reproduced. That result applies to that head only.

## Other tested evidence

| Item | Result available to this session | Class |
|---|---|---|
| Public main SHA | Matches `a64c2f1d96a13f16963d8835713434c2be67c6f6` after `git fetch origin main` | VERIFIED |
| WO-PAPER-001 milestone tests | No test log, head or acceptance packet supplied | UNKNOWN |
| QARP-ROTATION-001 v1.0.0 implementation tests | Work reported running. No result supplied | UNKNOWN |
| Stream C recovery | Read-only attempt reported complete. July brief v0.3 and July architecture v2 recovered in full at private argus `46b4d8c8f17490357c6d1536c5027e45341b7f11`, with a reported hash match to the compared copies. Full May Trade doctrine not recovered. No writes, restarts, broker calls, vendor calls or credentials in that attempt. This session did not repeat it | REPORTED |
| FMP Stable API | Operator reports exactly three read-only calls. `profile` for SPY: HTTP 200, JSON list length 1. `historical-price-eod/light` for SPY, 2026-11-03 through 2026-11-04: HTTP 200, JSON list length 2. `batch-quote` for SPY and XOM: HTTP 402, non-JSON body, not parsed. No raw values retained. Not replayed here | REPORTED |

## Known gaps
1. Independent review of head `3aa95daffe1497725aba8dbd80d4005d5afde16c` has not happened. Builder-reported behaviour is not a closed G0 item.
2. Builder-reported limits that remain at that head: no holiday calendar; occupied ID 43 returns `AUTHORISATION_FAILURE` and no substitute id is used.
3. No paper-bots pull-request URL or implementation head was supplied.
4. No private ADR identifier was readable, so this packet cites none.
5. FMP plan name, licence, universe, quota and redistribution rights are UNVERIFIED. HTTP 402 is an access or payment refusal of the reported `batch-quote` call. It does not establish those rights. No further calls. No subscription upgrade.
6. No accepted entry, exit, initial-stop, trailing-stop or risk doctrine. The draft parameterised schema leaves those QARP values UNRESOLVED. July full texts and the unrecovered May source conflict as legacy profiles, and neither is approved. The full May source remains an access gap. That gap is not a finding that no historical rule ever existed.
7. G0 remains open. G1–G3 prospective outcomes are not available. Software tests are not investment-edge evidence.
8. Roadmap M0 and M1 have no accepted milestone.

## Deviations
- Text on merged PR #6 still names `9b843dee03892e73f29da31997e5d07bfed564a7` as the current PR #2 candidate. This packet records later reported heads and leaves that SHA as the last independently reviewed HOLD.
- Reported head `adb605fd…` was overtaken by `3aa95daf…` before this public packet was committed. The silent grouped-row gap reported at `adb605fd…` is a superseded builder claim, not an independently confirmed fix.
- QARP-ROTATION-001 v1.0.0 implementation was reported running before a separate public implementation work-order id existed. The screening specification is already on main. This packet mints no SHA or pull-request URL for the unseen work.
- An earlier reading of FMP HTTP 402 as proof of specific plan terms is withdrawn. The status is UNVERIFIED.
- Stream C's earlier partial summaries conflict and are not approvals. The later read-only attempt recovered two July full texts and did not recover the full May doctrine. No further access is authorised. The private comparison and draft were handed to the paper-bots workstream for reviewed private preservation; no preservation SHA was supplied, so none is recorded.
- This session could not perform the authorised independent E-Bot re-review. That is an access limit, not a failed test of the private code.

## Disposition

| Item | Disposition | Meaning in this packet |
|---|---|---|
| QARP-ROTATION-001 v1.0.0 screening specification | **ACCEPT** | Already merged on main by PR #6. Paper screening only. No order authority |
| Distinct M-Bot role and paper-only six-bot delivery direction | **ACCEPT** | Already merged under PAPER-LAUNCH-001. This row is not a new grant |
| Continued autonomous paper-only work under that merged direction | **HOLD** | Owner authorised the work to continue. Publishing this file is still proposed. Continuation is not milestone acceptance |
| E-Bot PR #2 at `3aa95daffe1497725aba8dbd80d4005d5afde16c` | **HOLD** | Current reported candidate. Needs independent exact-head review. Awaiting Architect acceptance. Not accepted |
| E-Bot PR #2 at `adb605fd676d06cf27830f35bf39c06d92d6a119` | **HOLD** | Superseded reported head. Not an acceptance target |
| E-Bot PR #2 at `9b843dee03892e73f29da31997e5d07bfed564a7` | **HOLD** | Prior independent review stands for that head |
| Paper-bots bootstrap `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | **HOLD** | Bootstrap identifier only |
| WO-PAPER-001 integrated vertical slice | **HOLD** | Reported running. No acceptance evidence |
| QARP-ROTATION-001 v1.0.0 implementation | **HOLD** | Reported running. No test evidence in this packet |
| FAIR-VALUE-COMPOUNDER-002 | **HOLD** | Still proposed in the strategy registry. No specification to accept |
| July brief v0.3 and July architecture v2 | **HOLD** | Full texts reported recovered. Neither is an approved doctrine |
| May Trade doctrine, full source | **NEED OWNER DECISION/ACCESS** | Access gap. Only the previously cited one-line excerpt is in hand. Vol-band parameters are missing |
| Conflicting legacy profiles | **NEED OWNER DECISION/ACCESS** | Recovered July texts and the unrecovered May excerpt are not one policy. Neither is approved. The missing May source is not proof that no rule ever existed |
| Draft parameterised equities schema | **HOLD** | QARP entry, exit, initial stop, trailing stop and risk values are explicitly UNRESOLVED. Not a complete accepted doctrine |
| Stop-dependent M-Bot / T-Bot management | **HOLD** | Remains blocked. The recovery attempt being complete does not release it |
| FMP as a research source | **HOLD** | Three reported calls. Entitlement and rights UNVERIFIED. Calls stopped |
| Live trading, broker writes, scheduling | **HOLD** | Unauthorised |
| This documentation pull request | **HOLD** | Proposed status record. Architect acceptance is still required |

## Issue #5 dependency — NEED OWNER DECISION/ACCESS
Tracked by [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5). The authorised read-only recovery attempt is complete. This public packet is the sanitised result.

The full May Trade doctrine was not recovered. The owner or operator needs to provide that complete source through an authorised authenticated exact-record export, or supply it from backup. No bypass is authorised. No further access is attempted under this recovery.

Until that source is supplied and a doctrine is explicitly accepted, stop-dependent M-Bot and T-Bot management stays HOLD. The private comparison and unresolved draft were handed to the paper-bots workstream for reviewed private GitHub preservation. No private preservation URL or SHA was supplied here.

**NEED OWNER DECISION/ACCESS** applies to the missing May source and to the conflicting legacy profiles. It is not a request to choose numbers from the unrecovered text, and it is not a claim that the search proved no rule ever existed.

## Next work order
Keep the already running private work inside its existing bounds: WO-PAPER-001 and QARP-ROTATION-001 v1.0.0 implementation against the frozen registry. Do not resume Stream C access. Independent paper work continues.

The next reviewable E-Bot gate is an independent exact-head review of `3aa95daffe1497725aba8dbd80d4005d5afde16c`, including the builder-reported `malformed_row` / `INVALID_DATA` behaviour, empty-result `UNCHECKED` behaviour, peer `PRICE_OK` behaviour, the three `urllib_send` regressions, the absent holiday calendar, and the occupied ID 43 `AUTHORISATION_FAILURE` path. No live calls. Until that review exists, the head stays HOLD.

Further consolidation data may follow. Do not backfill missing heads, URLs or test totals.

## Requested Architect action
Accept this documentation PR only as a sanitised status record, or hold it. Acceptance of this PR does not accept E-Bot PR #2, WO-PAPER-001, the QARP implementation, either legacy profile, the unresolved draft, or FMP rights. The May-source item stays **NEED OWNER DECISION/ACCESS** after this PR is reviewed.
