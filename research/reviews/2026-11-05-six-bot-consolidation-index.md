# Six-bot consolidation index — sanitised review packet

**ARCHITECT DISPOSITION UPDATE — 2026-11-05:** See [independent exact-head M2/preservation review](2026-11-05-paper-bots-m2-preservation-exact-head-audit.md). Private paper-bots PR #3 head `531967980bcec40576d929ce32f8bb9900e498f6` **accepted and merged for preservation only**, merge `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`. PR #2 head `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` **HOLD** after 72 independent offline tests because idempotent replay can mask changed discovery parent and NEO emits a divergent correlation. Grok correction ordered in PR #2 comment `6667409366`. Public governance PR #7 remains OPEN/UNMERGED. All trading-policy and G0/FMP/scheduling/live-execution gates unchanged. The remainder of this consolidated builder packet is retained as historical evidence, not the latest acceptance status.

**SUPERSESSION — correction round authorised, head not yet supplied (2026-11-05).** This session fast-forwarded onto verified public head `8677c421869f5f46fe4ede724e31058c391384ed` and did not rewrite it. Private comment `6667409366` returned not-found here, so its text is **not verified by this session**. The public audit file on that head is the Architect record. One bounded repair is assigned to the existing paper-bots workstream: reject a replay that hides a changed discovery parent, keep the NEO correlation on the validated chain, merge accepted private main `928b6967b31ad4bf3b3404cf04b1978c25aaff6d` non-destructively, test on Python 3.9 and 3.12, and record an ADR. **No new head is recorded until that evidence arrives.** E-Bot `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` and M1 `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` stay accepted and unchanged. PR #3's merge is historical evidence only and adopts no policy. The repair head supplied after this note is in the final 13-item packet. It is builder-reported and not accepted.
**ID:** REVIEW-PAPER-INDEX-001
**Date:** 2026-11-05 (Europe/London)
**Status:** **HOLD** on this governance pull request, on paper-bots PR #2 lineage, and on PR #3 policy. E-Bot code and the paper-bots mock foundation are Architect-accepted. This session did not re-test them. Do not merge this pull request from this update.
**Public base verified by this session:** `a64c2f1d96a13f16963d8835713434c2be67c6f6` (`origin/main`, merge of [PR #6](https://github.com/maff0000/CGPT-INVESTMENT/pull/6))
**Documentation branch:** `cursor/paper-governance-progress-6067`
**Public pull request:** https://github.com/maff0000/CGPT-INVESTMENT/pull/7 (proposed; merging it accepts this status record only)
**Decision:** [PAPER-PROGRESS-001](../decisions/2026-11-05-paper-progress-sanitised.md)
**Progress log:** [WO progress](../../work-orders/2026-11-05-paper-stream-progress.md)

**Read-back this session (VERIFIED):** public `origin/main` is `a64c2f1d96a13f16963d8835713434c2be67c6f6`. Public PR #7 is OPEN. Before this revision its head was `18badb7118d6acff4fec2c6533889f82161d8340`, matching the last reviewed head, so there was no drift. Private `maff0000/ebot` and `maff0000/paper-bots` returned not-found. Their main SHAs below are **ARCHITECT-REPORTED** from the public comments, not re-read by this session, and they are not commits on public main.

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

**Correction round as first submitted:** the builder reported it complete, with no main merge, rebase, force-push, vendor call or broker call. E-Bot was not modified. The builder did not re-read private E-Bot main because the API returned 404. The later Architect review of those submitted heads is in the next major section. Frozen QARP predicates stay unchanged. Paper and shadow only. The Architect-reported E-Bot main remains `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`.

## Builder correction heads — submitted evidence
**Evidence class:** BUILDER-REPORTED. This session did not clone the private repository or re-run the tests. The Architect later accepted the PR #1 head and held the PR #2 head. Those dispositions are above this historical builder table.

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

## Architect correction-round review — 2026-11-05
**Evidence class:** ARCHITECT-INDEPENDENT, read from [PR #7 comment](https://github.com/maff0000/CGPT-INVESTMENT/pull/7#issuecomment-6667026399). Python 3.12.14, offline. This session did not reconstruct or re-run the tests. Private review threads were not readable here.

| Target | Architect result | Disposition |
|---|---|---|
| paper-bots PR #1 head `823203059466a30a11fe5a0e677f54c5482dc6fb` | 52 tests OK, including non-finite size and fill checks that fail closed | **ACCEPTED AND MERGED.** Private main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06`. Mock six-bot foundation only. No strategy, stop, scheduling or live authority |
| paper-bots PR #2 head `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` | 66 tests OK. Non-finite screen inputs stay unknown, proxy labels stay proxy, and ordered E→S→NEO linkage holds for the repaired cases | **HOLD.** Two adversarial defects remain: a swapped discovery parent is accepted, and an incomplete NEO cohort is accepted |
| paper-bots PR #3 head `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a` | Prior four-hash match stands. Branch is reported non-mergeable against the new private main | **POLICY HOLD.** Preservation bytes stay intact. Neither legacy profile is approved. May full text is not recovered |
| E-Bot private main `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | Unchanged from the preceding code acceptance | **CODE ACCEPTED.** G0 stays OPEN |

**Next correction, assigned and not yet evidenced:** one bounded round on the existing paper-bots workstream. Validate candidate, event type, producer, run, session, chronology and strategy context. Require the exact screen parents for a cohort. Reject atomically, with no partial ledger write. Test on Python 3.9 and 3.12. Reconcile PR #2 non-destructively onto accepted main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06`. Reconcile the PR #3 preservation branch without changing the four full hashes, without a force-push, and without treating legacy text as approved. No new heads are recorded until that evidence arrives. No new functionality is authorised by this note.

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
| Paper-bots bootstrap | `3a1144bc544b3bc063808a42c723cbeabffb6ec9` | BUILDER-REPORTED | Original base of PR #1 and PR #3. Superseded as private main by the M1 merge below |
| Paper-bots accepted private main | `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | ARCHITECT-REPORTED | Merge of PR #1. Mock foundation only. Not re-fetched here. Not public main |
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
| Paper-bots PR #1 correction `823203059466a30a11fe5a0e677f54c5482dc6fb`, merge `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | **ACCEPT — MOCK FOUNDATION ONLY** | Architect: 52 tests on Python 3.12.14, including non-finite safety. Not a strategy or stop acceptance |
| Paper-bots PR #2 audited head `b6b7877884df6edc624691b50bb474b2b518ded8` | **HOLD** | Architect finding for that earlier head. 59 green tests were not acceptance |
| Paper-bots PR #2 correction `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` | **HOLD** | Architect: 66 tests OK and the first three defects are fixed. Swapped discovery parents and an incomplete NEO cohort are still accepted |
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
Public PR #7 stays unmerged. Paper-bots PR #1 is Architect-reported as merged to private main. PR #2 and PR #3 stay unmerged. The Architect's E-Bot code merge is already reported and is not reverted here. Public main remains `a64c2f1d96a13f16963d8835713434c2be67c6f6`.

## Next work order — superseded for the current head
The 12-item packet below was the builder submission later reviewed by the Architect. That review is at the top of this file. The active next step is the bounded replay and correlation repair. Its head is not supplied.

Unchanged blocks: G0 OPEN; FMP entitlement and licence UNVERIFIED; full May source **NEED OWNER DECISION/ACCESS**; entry, exit, initial stop, trailing stop and risk policy unapproved; stop-dependent M/T HOLD; no scheduling; no live execution.

## Final 12-item acceptance packet — 2026-11-05
**Disposition requested:** **READY FOR ARCHITECT ACCEPTANCE** of the PR #2 correction and of PR #3 preservation only. Stop and risk policy stay **HOLD**. This session does not accept either pull request.

**Evidence classes.** Public `origin/main` and the pre-commit PR #7 head are **VERIFIED** by this session. Private SHAs, tests, rejects, ledger behaviour and the four hashes are **BUILDER-REPORTED**. The builder reports a remote read-back of private main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06`. This session received HTTP 404 for that repository, so it did not verify the private heads. The Architect's 52-test and 66-test Python 3.12.14 results remain **historical** for `823203059466a30a11fe5a0e677f54c5482dc6fb` and `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b`. They are not an audit of the heads below.

### 1. Repositories, branches, bases and heads
| Repository | Branch | Base | Head | State |
|---|---|---|---|---|
| Public `maff0000/CGPT-INVESTMENT` | `main` | — | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | VERIFIED this session |
| Public PR #7 | `cursor/paper-governance-progress-6067` | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | `817a029139677641c55dd51d899aa7b7f89922b6` before this packet | VERIFIED, OPEN. Supersedes the stale reference `18badb7118d6acff4fec2c6533889f82161d8340` |
| Private `maff0000/ebot` | accepted main, name not re-read | — | `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | ARCHITECT-REPORTED. Not refetched. E-Bot not modified in this round |
| Private `maff0000/paper-bots` | accepted main, name not re-read | — | `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | BUILDER reports remote verification. Not visible here |
| [paper-bots PR #2](https://github.com/maff0000/paper-bots/pull/2) | `cursor/qarp-rotation-001-1e9e` | `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` | BUILDER-REPORTED. OPEN / UNMERGED. Normal merge `00423b5b5bd35d36b7a00c776785adc688da094b`. No force-push, rebase or main merge |
| [paper-bots PR #3](https://github.com/maff0000/paper-bots/pull/3) | **NOT SUPPLIED.** This session could not read the private pull request, so no branch name is invented | `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` | `531967980bcec40576d929ce32f8bb9900e498f6` | BUILDER-REPORTED. OPEN / UNMERGED |

### 2. Changed files and work orders
PR #2, builder-reported paths: `src/paperbots/strategies/lineage.py`, `strategies/screen.py`, `ledger.py`, `access.py`, `docs/schemas/v0.2/catalog.json`, `tests/test_lineage.py`, `docs/adr/0006-screen-lineage-identity.md`, `docs/work-orders/WO-PAPER-002-correction-evidence-integrity.md`. Work order named: WO-PAPER-002 correction for evidence integrity. ADR 0006 is cited by path only. PR #3 conflict is reported in README only. The four original evidence files are reported unchanged.

### 3. Summary
Discovery parents are checked for candidate identity, event type `CANDIDATE`, producer `EBOT`, correlation, session and chronology. A swapped order is rejected and is not silently repaired. A cohort must be the exact screen set: no missing, extra or duplicate identifiers, and the same run, session, strategy `1.0.0` and digest. Checks run before validation, and the ledger write is an atomic batch.

### 4. Tests on Python 3.9 and 3.12
Builder reports 72 tests passed on Python 3.12.3 and 72 passed on Python 3.9.25 for the PR #2 branch. Builder reports 52 tests passed on each of those interpreters for the PR #3 branch. This session did not run them. The Architect's earlier 52 and 66 Python 3.12.14 results stay attached to the previous heads.

### 5. Audits and security, kept distinct
No new independent audit was performed for `453cc99e…` or `53196798…`. No vendor, broker or account call is reported. No secret or private original is copied here. The named rejection cases are builder-reported coverage of the 72-test run, not a separate security audit.

### 6. REJECT evidence
Builder reports that these cases are rejected and leave the ledger row count and hash tip unchanged: swapped parents, missing parent, wrong candidate, cross-correlation, cross-session, wrong event type, future discovery, incomplete cohort, duplicate identifier, and wrong strategy version or digest. A valid two-candidate chain is reported to verify. This session did not inspect the assertions inside the test file.

### 7. Ledger and idempotency
Builder reports: replay adds zero rows; a zero-row case and same-name duplicate observations are recorded; numeric and proxy cases stay green; an injected ledger outage writes zero rows for the batch. Pre-validation plus an atomic batch is the reported control. No partial ledger write is claimed as independently proven.

### 8. Four preservation hashes
Recomputed after the reported PR #3 merge, builder-reported, originals unchanged:

| Item | SHA-256 |
|---|---|
| July brief | `a3ffdb12f68a31bbf944f23e0a34646109d891f10f0f5bb6c9ccafb851b587f3` |
| July architecture | `d2e7331d544d6c938d5049475c201a01aeee8b5b1f4dc932f918aad0e62fa876` |
| Matrix | `86b3de6684648b1b53ab5104862f81fafdad0903db6c7ca059a4209c8bac4485` |
| Draft | `3658f7731af92bd479581fbb98f12993740dccb65f8e83e9256e811015206a59` |

May text is not recovered. No path is invented for it. Legacy material is not approved. The draft stays a draft.

### 9. Public PR #7 state
OPEN. Not merged. Base `a64c2f1d96a13f16963d8835713434c2be67c6f6`. Head before this packet `817a029139677641c55dd51d899aa7b7f89922b6`, verified on the remote. The SHA of this packet is the branch tip after the push and is recorded by read-back, not guessed in advance.

### 10. Limitations
G0 remains open. FMP entitlement and licence are UNVERIFIED. The full May source is unavailable. Entry, exit, initial stop, trailing stop and risk policy are unapproved. Stop-dependent M/T stays HOLD. No scheduling and no live execution. NEO 5/20/60 horizons and investment performance are not established. No external ledger-tip notarisation is claimed. PR #3's branch name was not supplied and could not be read.

### 11. Next work order
Exact-head Architect review of `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` and `531967980bcec40576d929ce32f8bb9900e498f6`. Not started. Further integration and source-rights work only after that acceptance.

### 12. Readiness
**READY FOR ARCHITECT ACCEPTANCE** of the PR #2 screen-lineage correction and of PR #3 preservation only. Not accepted by this packet. Stop and risk policy remain **HOLD**.

## Requested Architect action
The request above applied to `453cc99e…` and `53196798…`. The Architect has since held the first and merged the second for preservation only. This governance pull request stays unmerged.

## 13-item packet — awaiting the repair head
Superseded by the filled packet at the end of this file. The table below is the pre-result reserve and is kept as history.

| Item | Status |
|---|---|
| 1. Verified starts | Public main `a64c2f1d96a13f16963d8835713434c2be67c6f6` and PR #7 `8677c421869f5f46fe4ede724e31058c391384ed` were read back before this note. Private comment `6667409366` was not readable here |
| 2. Exact PR #2 head and base | Held head `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4`. Repair head **NOT SUPPLIED**. Reconcile onto `928b6967b31ad4bf3b3404cf04b1978c25aaff6d` |
| 3. Reconciliation | Required to be a non-destructive merge of current private main. Result **NOT SUPPLIED** |
| 4. Files | **NOT SUPPLIED** |
| 5. Fixes | Required: replay must not hide a changed discovery parent; NEO correlation must stay with the validated chain |
| 6. Regressions | Required on Python 3.9 and 3.12. Results **NOT SUPPLIED** |
| 7. Results | **NOT SUPPLIED** |
| 8. Integrity | Prior four preservation hashes stand for the merged evidence. Repair integrity **NOT SUPPLIED** |
| 9. Security | No new vendor, broker, credential or May-access action is authorised |
| 10. ADR | Required with the repair. Identifier **NOT SUPPLIED** |
| 11. Gaps | G0, FMP rights, full May source, entry/exit/initial/trailing/risk approval, stop-dependent M/T, scheduling and live execution remain blocked |
| 12. Public PR #7 head | `8677c421869f5f46fe4ede724e31058c391384ed` before this note. The tip after this note is the remote read-back |
| 13. Readiness | Repair **IN PROGRESS**. Not ready for acceptance until the head and tests arrive |

## Final 13-item packet — builder submission, not accepted
**Disposition:** **READY FOR ARCHITECT ACCEPTANCE** of [paper-bots PR #2](https://github.com/maff0000/paper-bots/pull/2) head `e403f29db0fe74f7b2b5f3ad7d84f160a966df22`. This session does not accept it. The Architect's 72-test Python 3.12.14 result remains historical for `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` and is not an audit of the new head. Private paper-bots returned not-found here. The builder reports a remote read-back in which the local head, the origin branch and the pull-request head are all `e403f29db0fe74f7b2b5f3ad7d84f160a966df22`, private main is unchanged, and the pull request is mergeable.

### 1. Verified starts
| Ref | SHA | Class |
|---|---|---|
| Public main | `a64c2f1d96a13f16963d8835713434c2be67c6f6` | VERIFIED this session |
| Public PR #7 before this packet | `2de57d153b1f1cc810c145300f59c2795a0efbc0` | VERIFIED this session. Parent includes Architect head `8677c421869f5f46fe4ede724e31058c391384ed` |
| Paper-bots accepted main at repair start | `928b6967b31ad4bf3b3404cf04b1978c25aaff6d` | BUILDER-REPORTED read-back. Includes the preservation merge. Not refetched here |
| Prior PR #2 head | `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` | ARCHITECT-INDEPENDENT hold, 72 tests on Python 3.12.14 |
| E-Bot accepted main | `79b7ac90fe4cf7c6e974e476baca7c63cc24603f` | ARCHITECT-REPORTED. Not refetched. Unchanged this round |

### 2. Exact PR #2 head and base
Branch `cursor/qarp-rotation-001-1e9e`. Head `e403f29db0fe74f7b2b5f3ad7d84f160a966df22`. Base `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`. OPEN / UNMERGED.

### 3. Reconciliation
Ordinary merge `2df940bff49023f7a8eb396f1b54c934816ddf65`, parents `453cc99ebc5c6926fa30037bde9e4bbfb4a18bc4` and `928b6967b31ad4bf3b3404cf04b1978c25aaff6d`. No rewrite, force-push or merge to main. The builder reports the diff against main is QARP and lineage only, and does not duplicate M1. Accepted M1 and the four preservation hashes are reported unchanged.

### 4. Files and work order
`src/paperbots/ledger.py`, `src/paperbots/strategies/screen.py`, `src/paperbots/schemautil.py`, `docs/schemas/v0.2/catalog.json`, `tests/test_lineage.py`, `docs/adr/0007-replay-identity-and-chain-correlation.md`, `docs/work-orders/WO-PAPER-002-correction-replay-identity.md`, and a dated supersession appended to the private README. Historical private records are reported preserved. ADR 0007 is cited by path only.

### 5. Fixes
Replay identity now includes output hash, parent IDs, input hashes, correlation, session, producer, event type, rule version, and payload strategy ID, version, digest, run, instrument and source mapping. An exact replay returns the identical event and adds zero rows. A changed but valid parent conflicts inside the atomic batch and rolls back. It does not return the old mismatched provenance. The same key with a changed parent is rejected. A truly new decision requires a different run, instrument or index. The cohort envelope carries `correlation_id` and `chain_correlation_id` from the validated screens and upstream discovery. A conflicting run correlation is rejected before insert. A zero-candidate cohort uses the explicit zero-screen correlation.

### 6. Regressions
Builder reports the full unittest suite: 73 passed on Python 3.12.3 and 73 passed on Python 3.9.25. Covered cases reported with that run: exact same-parent screen and cohort replay; second valid parent, missing parent, and foreign correlation or session rejected; two-candidate chain continuity; missing, extra and duplicate cohort parents; conflicting cohort run correlation; zero-candidate continuity; rejections leave row count and tip unchanged; replay adds zero rows; outage writes zero rows; prior numeric, provenance, paper and role-isolation cases stay green. This session did not run the suite or open the test file.

### 7. Results
Screen append remains S-Bot only. Cohort append remains NEO only. `entry_authority` remains NONE. Thresholds and the stop registry are unchanged. No broker, vendor, credential or scheduler path is reported added.

### 8. Integrity
The four preservation hashes from the merged evidence are reported unchanged. Replay and rejection paths are reported to leave the hash tip unchanged except for an accepted new event. No partial write is reported for a conflicting parent or an outage.

### 9. Security
No vendor call, order, account query, credential use or new May-access route is reported. No private original is copied here. This is not a new independent security audit.

### 10. ADR
`docs/adr/0007-replay-identity-and-chain-correlation.md`, builder-reported. Not read here.

### 11. Gaps
G0 stays OPEN. FMP rights stay UNVERIFIED. The full May source is unrecovered. The doctrine is unapproved. Entry, exit, initial stop, trailing stop and risk approval are absent. Stop-dependent M/T, scheduling and live execution stay blocked. The Architect has not reviewed `e403f29d…`.

### 12. Public PR #7 head
OPEN. Base `a64c2f1d96a13f16963d8835713434c2be67c6f6`. Head before this packet `2de57d153b1f1cc810c145300f59c2795a0efbc0`, verified on the remote. The tip after this packet is the remote read-back.

### 13. Readiness
**READY FOR ARCHITECT ACCEPTANCE. Not accepted.** The next work order is an exact-head independent review on Python 3.12.14 before any merge. It is not started.
