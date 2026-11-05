# Six-bot consolidation index — sanitised review packet
**ID:** REVIEW-PAPER-INDEX-001
**Date:** 2026-11-05 (Europe/London)
**Status:** **HOLD** on this governance pull request and on paper-bots PRs #1–#3. E-Bot code acceptance below is the Architect's, not this session's audit. Do not merge this pull request from this update.
**Public base verified by this session:** `a64c2f1d96a13f16963d8835713434c2be67c6f6` (`origin/main`, merge of [PR #6](https://github.com/maff0000/CGPT-INVESTMENT/pull/6))
**Documentation branch:** `cursor/paper-governance-progress-6067`
**Public pull request:** https://github.com/maff0000/CGPT-INVESTMENT/pull/7 (proposed; merging it accepts this status record only)
**Decision:** [PAPER-PROGRESS-001](../decisions/2026-11-05-paper-progress-sanitised.md)
**Progress log:** [WO progress](../../work-orders/2026-11-05-paper-stream-progress.md)

Public `origin/main` verified this session remains `a64c2f1d96a13f16963d8835713434c2be67c6f6`. Public PR #7 remains OPEN. The governance head before this correction packet was `099c5b4478cd8fc4a2a52cdf10a099fb06fe7139`. Private `maff0000/ebot` and `maff0000/paper-bots` were not readable here. The Architect's consolidated findings were read from the public comment on PR #7. The correction heads below are builder-reported and were not re-tested here.

Earlier sections that say E-Bot PR #2 is OPEN or HOLD are the builder-reported record before this Architect result. They are left in place.

## Architect independent review — 2026-11-05
**Evidence class:** ARCHITECT-INDEPENDENT. Reconstructed exact source, Python 3.12.14, offline. This public session did not re-run those tests and does not claim them as its own audit.
**Source read here:** [PR #7 comment](https://github.com/maff0000/CGPT-INVESTMENT/pull/7#issuecomment-6666139699).

| Target | Architect result | Disposition |
|---|---|---|
| E-Bot PR #2 head `3aa95daffe1497725aba8dbd80d4005d5afde16c` | 112 unittest cases OK. Source and read-only safeguards inspected. Merge commit `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | **CODE ACCEPTED AND MERGED.** G0 stays OPEN. Automated trading is not authorised. This session could not re-fetch that private main; `79b7ac90…` is not a commit on public CGPT-INVESTMENT `main` |
| paper-bots PR #1 head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` | 48 tests OK on Python 3.12.14, plus further risk-input tests | **HOLD.** Non-finite numeric risk: NaN can raise in sizing, Infinity can pass, and a non-finite fill can be accepted. Green tests are not acceptance |
| paper-bots PR #2 head `b6b7877884df6edc624691b50bb474b2b518ded8` | 59 tests OK on Python 3.12.14, plus further screen and ledger tests | **HOLD.** Infinity can become a verified screen match. A proxy can be labelled as an exact Finviz match. Cohort lineage keeps the final screen reference and omits upstream discovery references for a multi-candidate set. NaN market-cap can raise. Stacked on PR #1, which is also HOLD |
| paper-bots PR #3 head `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a` | Four private file hashes match the manifest. Preliminary privacy scan clear. Upstream source location not independently verified by the Architect | **POLICY HOLD.** Preservation integrity passed. Neither legacy profile is approved |

**Correction round:** the assigned round is builder-reported complete. The Architect's Python 3.12.14 findings apply to the prior heads in the table above, not to the new heads. Those new heads await an exact-head Architect re-review and are not accepted. Frozen QARP predicates stay unchanged. Paper and shadow only. No main merge, rebase, force-push, vendor call or broker call is reported for the round. E-Bot was not modified. The builder reports it did not re-read private E-Bot main because the API returned 404. The Architect-reported E-Bot main remains `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`.

## Builder correction heads — not re-audited
**Evidence class:** BUILDER-REPORTED. This session did not clone the private repository or re-run the tests.

### PR #1 numeric safety
https://github.com/maff0000/paper-bots/pull/1  
Base remains `3a1144bc544b3bc063808a42c723cbeabffb6ec9`. Architect-audited head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`. **New head `823203059466a30a11fe5a0e677f54c5482dc6fb`.**

| Builder report | Value |
|---|---|
| Tests | 52 passed on Python 3.12.3 and 52 passed on Python 3.9.25 |
| Reproduction at the old head | NaN raised; Infinity and bool were accepted as PASS |
| New helper | Rejects non-finite values and bools, without a crash. Valid finite types are preserved. No trading permission is added. No new risk cap is added |
| Files named | `numbers.py`, `riskcore.py`, `schemautil.py`, `reconcile.py`, `tests/test_numeric_safety.py`, `docs/work-orders/WO-PAPER-001-correction-numeric.md` |

### PR #2 screen lineage
https://github.com/maff0000/paper-bots/pull/2  
Git base is now the new PR #1 head `823203059466a30a11fe5a0e677f54c5482dc6fb`. Architect-audited head `b6b7877884df6edc624691b50bb474b2b518ded8`. Reported non-destructive merge `6b72d03b886502c3d50eb150a918eb676c3fae3a` imports the PR #1 correction. **New head `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b`.**

| Builder report | Value |
|---|---|
| Tests | 66 passed on Python 3.12.3 and 66 passed on Python 3.9.25 |
| Non-finite market cap | `UNKNOWN` / `NON_FINITE_INPUT`, not a verified match |
| Source label | Each observation keeps `source_mapping` and `source_id` as `PROXY_FIXTURE_NOT_EXACT` even when the run is labelled exact |
| Discovery link | Each screening event references its own discovery event |
| Multi-candidate cohort | Verified, near-miss, reject and unknown cohorts reference all four screen events in `parent_event_ids` and `screen_event_ids`. No cross-candidate parent |
| Unchanged authority | Frozen QARP thresholds. `entry_authority` remains NONE |
| Files named | `strategies/evaluate.py`, `strategies/screen.py`, `schemautil.py`, `docs/schemas/v0.2/catalog.json`, `tests/test_qarp.py`, `docs/work-orders/WO-PAPER-002-correction-lineage.md` |

### PR #3
Unchanged at `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a`. **POLICY HOLD.**

**Doctrine recommendation, not a parameter approval:** the Architect recommends writing a new equities doctrine without waiting for the missing May text. Legacy profiles stay historical. This record does not invent or approve entry, initial stop, trailing stop, exit or risk values. Stop-dependent M/T stays HOLD.

## Source SHAs

| Source | Exact identifier | Evidence class | Role in this packet |
|---|---|---|---|
| Public main | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | VERIFIED here | Merge PR #6, 2026-11-05 17:44:54 UTC. [Commit](https://github.com/maff0000/CGPT-INVESTMENT/commit/a64c2f1d96a13f16963d8835713434c2be67c6f6) |
| PR #6 head | `b7c81d730a9a61d53776c8729eb4556e091f0cf1` | VERIFIED here | Branch merged by that commit |
| Prior main (PR #6 first parent) | `fa87e83834643316ff1f1a87a8438b11a336ca1f` | VERIFIED here | Merge PR #4. Starting main named on [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5) |
| E-Bot PR #2 base | `50c0b66247498672b84e9fcae7e417a538a0e5c1` | REPORTED | Base of open [PR #2](https://github.com/maff0000/ebot/pull/2). Matches the base in the earlier public review |
| E-Bot last independent public review | `9b843dee03892e73f29da31997e5d07bfed564a7` | VERIFIED in [that review](2026-11-05-g0-d3-pr2-architect-hold.md) | Historical HOLD for that head only |
| E-Bot superseded reported head | `adb605fd676d06cf27830f35bf39c06d92d6a119` | REPORTED | Superseded before this packet was committed. Not independently reviewed |
| E-Bot reviewed head, now Architect-merged | `3aa95daffe1497725aba8dbd80d4005d5afde16c` | ARCHITECT-INDEPENDENT | Code accepted. Merge commit below. G0 remains OPEN |
| E-Bot private main after that merge | `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | ARCHITECT-REPORTED | Stated in the public PR #7 comment. Not re-fetched by this session. Not public CGPT-INVESTMENT main |
| Paper-bots bootstrap / private main if PRs stay unmerged | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | BUILDER-REPORTED | Base of [PR #1](https://github.com/maff0000/paper-bots/pull/1) and [PR #3](https://github.com/maff0000/paper-bots/pull/3) |
| Paper-bots PR #1 Architect-audited head | `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` | ARCHITECT-INDEPENDENT | HOLD for non-finite risk. Not the current candidate |
| Paper-bots PR #1 correction head | `823203059466a30a11fe5a0e677f54c5482dc6fb` | BUILDER-REPORTED | Current candidate. 52 tests on 3.9.25 and 3.12.3. Not re-audited. Not accepted |
| Paper-bots PR #2 Architect-audited head | `b6b7877884df6edc624691b50bb474b2b518ded8` | ARCHITECT-INDEPENDENT | HOLD for screen match and lineage. Not the current candidate |
| Paper-bots PR #2 import merge | `6b72d03b886502c3d50eb150a918eb676c3fae3a` | BUILDER-REPORTED | Non-destructive merge of the PR #1 correction onto the PR #2 branch |
| Paper-bots PR #2 correction head | `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` | BUILDER-REPORTED | Current candidate. Base `82320305…`. 66 tests on 3.9.25 and 3.12.3. Not re-audited. Not accepted |
| Paper-bots PR #3 head | `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a` | BUILDER-REPORTED | OPEN / UNMERGED. Docs-only private evidence. Base is the bootstrap. Not accepted |
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

The last independent review recorded in this public journal before the Architect's code acceptance remains the HOLD at `9b843dee03892e73f29da31997e5d07bfed564a7`: 105 offline tests passed on Python 3.12.14, and three malformed-response classifications were reproduced. That result applies to that head only. The Architect later accepted `3aa95daffe1497725aba8dbd80d4005d5afde16c` as code only.

## Paper-bots builder completion — pre-correction heads

All three private pull requests are reported **OPEN / UNMERGED**. None is accepted. This section is the builder record of the heads the Architect later audited. The correction heads are in the section above.

### PR #1 — WO-PAPER-001 mock chain
https://github.com/maff0000/paper-bots/pull/1  
Head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`. Base `3a1144bc544b3bc063808a42c723cbeabffb6ec9`.

| Builder report | Value |
|---|---|
| Shape | Six-role standard-library Python chain, deterministic risk gate, SQLite WAL append-only ledger with triggers and a hash chain |
| Tests | 48 passed on Python 3.9.25 and 48 passed on Python 3.12.3 |
| Cases named | Mock fills and reconciliation; earnings or invalid-data HOLD; no-signal; duplicate; ledger outage; stop-rule HOLD; UNCHECKED block |
| Network | No provider or broker network |
| Hosted CI | None reported |
| Independent audit | None |
| Private ADRs | 0001 private monorepo; 0002 ledger; 0003 role isolation; 0004 stop gap |

Builder-reported limits: no external ledger-tip notarisation, no calendar, no universe or live screen, no scheduler, and no owner risk caps. Simulator state is in-process. A synthetic fill is an interface demonstration only. `stop_authorised` is false. The run is not proof of trading-doctrine compliance.

### PR #2 — QARP-ROTATION-001 v1.0.0 registry
https://github.com/maff0000/paper-bots/pull/2  
Head `b6b7877884df6edc624691b50bb474b2b518ded8`. Base `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`, which is the unaccepted PR #1 head.

| Builder report | Value |
|---|---|
| Strategy | Frozen Finviz A/B/C for QARP-ROTATION-001 v1.0.0 through a versioned registry |
| Labels | Unknown, stale and proxy predicates are not passes. Near-miss and premium labels are separate. Rejected discoveries are retained |
| Ledger | Version 0.2 decision events |
| NEO | Selection cohorts and a fixture SPY/sector benchmark interface. Horizons 5/20/60 are still incomplete. No investment performance is claimed |
| Tests | 59 passed on Python 3.9.25 and 59 passed on Python 3.12.3. That count includes the prior 48 |
| Records | ADR 0005 and WO-PAPER-002 |
| Authority | `entry_authority` NONE. No live calls, chart engine, fair-value engine, or provider-metric equivalence |
| Stops | Stop paths remain HOLD |
| Independent audit | None. Builder evidence only |

### PR #3 — private evidence, docs only
https://github.com/maff0000/paper-bots/pull/3  
Head `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a`. Base `3a1144bc544b3bc063808a42c723cbeabffb6ec9`.

Docs only. The builder reports that the full July legacy evidence is hashed and was scanned in private. The full May doctrine is not in that recovery. Draft QARP entry, exit, stop, trail and risk values remain UNRESOLVED. No policy is approved. No tests are claimed for this docs pull request. The original private source commit remains `46b4d8c8f17490357c6d1536c5027e45341b7f11`. No private original content is copied into this public repository.

## Builder test coverage

| Pull request | Reported state | Head | Base | Builder tests | Independent audit |
|---|---|---|---|---|---|
| [Public #7](https://github.com/maff0000/CGPT-INVESTMENT/pull/7) | OPEN | this branch tip | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | Documentation and link check only | This packet is the status record, not a code audit |
| [ebot #2](https://github.com/maff0000/ebot/pull/2) | OPEN | `3aa95daffe1497725aba8dbd80d4005d5afde16c` | `50c0b66247498672b84e9fcae7e417a538a0e5c1` | 112 collected, 111 passed, 1 pre-existing skip, on each of Python 3.9.25 and 3.12.3. Zero live calls | Pending. Prior independent HOLD applies only to `9b843dee…` |
| [paper-bots #1](https://github.com/maff0000/paper-bots/pull/1) old | OPEN | `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | 48 passed on each of Python 3.9.25 and 3.12.3. Architect 3.12.14 audit of this head only | Architect HOLD |
| [paper-bots #1](https://github.com/maff0000/paper-bots/pull/1) new | OPEN | `823203059466a30a11fe5a0e677f54c5482dc6fb` | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | Builder: 52 passed on each of Python 3.12.3 and 3.9.25 | Not done. Awaiting re-review |
| [paper-bots #2](https://github.com/maff0000/paper-bots/pull/2) old | OPEN | `b6b7877884df6edc624691b50bb474b2b518ded8` | `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` | 59 passed on each of Python 3.9.25 and 3.12.3, including the prior 48. Architect 3.12.14 audit of this head only | Architect HOLD |
| [paper-bots #2](https://github.com/maff0000/paper-bots/pull/2) new | OPEN | `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` | `823203059466a30a11fe5a0e677f54c5482dc6fb` | Builder: 66 passed on each of Python 3.12.3 and 3.9.25 | Not done. Awaiting re-review |
| [paper-bots #3](https://github.com/maff0000/paper-bots/pull/3) | OPEN | `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a` | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | None claimed | None |

## Other tested evidence

| Item | Result available to this session | Class |
|---|---|---|
| Public main SHA | Matches `a64c2f1d96a13f16963d8835713434c2be67c6f6` after `git fetch origin main` | VERIFIED |
| WO-PAPER-001 tests | Builder reports 48 passed on each of Python 3.9.25 and 3.12.3 at `cdfcbb27…`. No hosted CI. Not re-run here | BUILDER-REPORTED |
| QARP-ROTATION-001 v1.0.0 implementation tests | Builder reports 59 passed on each of those interpreters at `b6b78778…`, including the prior 48. Not re-run here | BUILDER-REPORTED |
| Stream C recovery | Read-only attempt reported complete. July brief v0.3 and July architecture v2 recovered in full at private argus `46b4d8c8f17490357c6d1536c5027e45341b7f11`, with a reported hash match to the compared copies. Full May Trade doctrine not recovered. No writes, restarts, broker calls, vendor calls or credentials in that attempt. This session did not repeat it | REPORTED |
| FMP Stable API | Operator reports exactly three read-only calls. `profile` for SPY: HTTP 200, JSON list length 1. `historical-price-eod/light` for SPY, 2026-11-03 through 2026-11-04: HTTP 200, JSON list length 2. `batch-quote` for SPY and XOM: HTTP 402, non-JSON body, not parsed. No raw values retained. Not replayed here | REPORTED |

## Known gaps
1. Independent review of head `3aa95daffe1497725aba8dbd80d4005d5afde16c` has not happened. Builder-reported behaviour is not a closed G0 item.
2. Builder-reported limits that remain at that head: no holiday calendar; occupied ID 43 returns `AUTHORISATION_FAILURE` and no substitute id is used.
3. Paper-bots PR #2 depends on unaccepted PR #1. PR #3 is docs-only and is based on the bootstrap, not on either code head. None of the three is accepted.
4. Builder-reported paper-bots limits that remain: no external ledger-tip notarisation, calendar, universe or live screen, scheduler, or owner risk caps. Simulator state is in-process. NEO 5/20/60 horizons are incomplete. No chart engine, fair-value engine, or provider-metric equivalence. Private ADR numbers 0001–0005 are cited; their text was not independently read.
5. FMP plan name, licence, universe, quota and redistribution rights are UNVERIFIED. HTTP 402 is an access or payment refusal of the reported `batch-quote` call. It does not establish those rights. No further calls. No subscription upgrade.
6. No accepted entry, exit, initial-stop, trailing-stop or risk doctrine. The draft parameterised schema leaves those QARP values UNRESOLVED. July full texts and the unrecovered May source conflict as legacy profiles, and neither is approved. The full May source remains an access gap. That gap is not a finding that no historical rule ever existed.
7. G0 remains open. G1–G3 prospective outcomes are not available. Software tests are not investment-edge evidence.
8. Roadmap M0 and M1 have no accepted milestone.

## Deviations
- Text on merged PR #6 still names `9b843dee03892e73f29da31997e5d07bfed564a7` as the current PR #2 candidate. This packet records later reported heads and leaves that SHA as the last independently reviewed HOLD.
- Reported head `adb605fd…` was overtaken by `3aa95daf…` before this public packet was committed. The silent grouped-row gap reported at `adb605fd…` is a superseded builder claim, not an independently confirmed fix.
- QARP-ROTATION-001 v1.0.0 implementation now has builder-reported private PR #2 and WO-PAPER-002. The screening specification was already on main. The implementation base is an unaccepted head, and `entry_authority` is NONE.
- An earlier reading of FMP HTTP 402 as proof of specific plan terms is withdrawn. The status is UNVERIFIED.
- Stream C's earlier partial summaries conflict and are not approvals. Full July evidence is now builder-reported in private docs PR #3. The full May doctrine remains unrecovered. No further access is authorised. No private original text is in this public repository.
- This session could not perform the authorised independent E-Bot re-review. That is an access limit, not a failed test of the private code.

## Disposition

| Item | Disposition | Meaning in this packet |
|---|---|---|
| QARP-ROTATION-001 v1.0.0 screening specification | **ACCEPT** | Already merged on main by PR #6. Paper screening only. No order authority |
| Distinct M-Bot role and paper-only six-bot delivery direction | **ACCEPT** | Already merged under PAPER-LAUNCH-001. This row is not a new grant |
| Continued autonomous paper-only work under that merged direction | **HOLD** | Owner authorised the work to continue. Publishing this file is still proposed. Continuation is not milestone acceptance |
| E-Bot code at `3aa95daffe1497725aba8dbd80d4005d5afde16c`, merge `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | **ACCEPT — CODE ONLY** | Architect result. G0 stays OPEN. Automated trading is not authorised. Not this session's re-test |
| E-Bot PR #2 at `adb605fd676d06cf27830f35bf39c06d92d6a119` | **HOLD** | Superseded reported head. Not an acceptance target |
| E-Bot PR #2 at `9b843dee03892e73f29da31997e5d07bfed564a7` | **HOLD** | Prior independent review stands for that head |
| Paper-bots PR #1 audited head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` | **HOLD** | Architect finding for that head. 48 green tests were not acceptance |
| Paper-bots PR #1 correction `823203059466a30a11fe5a0e677f54c5482dc6fb` | **HOLD** | Builder reports 52 tests passed on 3.12.3 and 3.9.25. Not re-audited. Not accepted |
| Paper-bots PR #2 audited head `b6b7877884df6edc624691b50bb474b2b518ded8` | **HOLD** | Architect finding for that head. 59 green tests were not acceptance |
| Paper-bots PR #2 correction `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` | **HOLD** | Builder reports 66 tests passed on 3.12.3 and 3.9.25. Not re-audited. Not accepted |
| Paper-bots PR #3 at `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a` | **POLICY HOLD** | Architect: four hashes match and the privacy scan is clear. Neither legacy profile is approved |
| Paper-bots bootstrap `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | **HOLD** | Remains the unmerged base. Not a milestone acceptance |
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

Until that source is supplied and a doctrine is explicitly accepted, stop-dependent M-Bot and T-Bot management stays HOLD. Private docs preservation is builder-reported as [paper-bots PR #3](https://github.com/maff0000/paper-bots/pull/3) at `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a`. That pull request is open and not accepted. No private original text is copied here.

**NEED OWNER DECISION/ACCESS** applies to the missing May source and to the conflicting legacy profiles. It is not a request to choose numbers from the unrecovered text, and it is not a claim that the search proved no rule ever existed.

## Architectural deviations and unknowns
Builder-reported, and not independently checked:

- ADR 0001 records a private monorepo. ADR 0002 records a SQLite WAL append-only ledger with triggers and a hash chain, without external ledger-tip notarisation. ADR 0003 records role isolation. ADR 0004 records the stop gap. ADR 0005 records the QARP registry work with WO-PAPER-002.
- Simulator state stays in-process. A synthetic fill demonstrates the interface only. `stop_authorised` is false, so the fill is not doctrine-compliance proof.
- PR #2 is stacked on an unaccepted dependency. PR #3 branches from the bootstrap rather than from the code heads.
- NEO has a fixture benchmark interface. The 5/20/60 horizons are incomplete, and no investment performance is established.
- Source and rights mappings for live providers are not established. FMP rights remain UNVERIFIED. Further mapping work stays on mocks until rights exist.
- The full May doctrine is still an access gap. That is **NEED OWNER DECISION/ACCESS**, not a proof that no historical rule existed.

## Rollback
Public PR #7 stays unmerged. Paper-bots PRs #1, #2 and #3 stay unmerged until a later exact-head acceptance. The Architect's E-Bot code merge is already reported on the private repository and is not reverted here. Public main remains `a64c2f1d96a13f16963d8835713434c2be67c6f6`.

## Next work order
The one bounded correction round is builder-reported complete. Stop for an exact-head Architect re-review of `823203059466a30a11fe5a0e677f54c5482dc6fb` and `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b`. This public update does not accept those heads.

Unchanged gates: full May source unavailable (**NEED OWNER DECISION/ACCESS**); QARP entry, initial stop, trailing stop and exit not approved; FMP entitlement and licence UNVERIFIED; stop-dependent M/T HOLD; no scheduling and no live execution. PR #3 stays policy HOLD.

## Requested Architect action
Re-review the two new paper-bots heads. This governance revision records builder evidence only for those heads. It does not merge PR #7, accept the corrections, or approve doctrine parameters.
