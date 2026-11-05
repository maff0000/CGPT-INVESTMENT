# Paper stream progress — 2026-11-05
**Status:** PROPOSED public record. No software milestone is accepted in this file.
**Parent authority on main:** [PAPER-LAUNCH-001](../research/decisions/2026-11-05-paper-build-launch.md) at public `a64c2f1d96a13f16963d8835713434c2be67c6f6`
**Index:** [REVIEW-PAPER-INDEX-001](../research/reviews/2026-11-05-six-bot-consolidation-index.md)
**Public base for this documentation increment:** `a64c2f1d96a13f16963d8835713434c2be67c6f6`

## WO-GOV-001 — this public sanitised increment
**Scope:** record owner authorisation to continue autonomous paper-only six-bot delivery under merged PR #6; publish one consolidation index; correct the FMP entitlement reading; point living handoff files at the current reported E-Bot head.
**Exclusions:** implementation code, private evidence, personal data, secrets, infrastructure detail, raw vendor payloads, live calls, subscription changes, merges, invented pull-request URLs or heads.
**Tests:** document and link review only. The private E-Bot suite was not runnable from this session.
**Acceptance:** an open documentation pull request whose head states the dispositions in the index. Architect acceptance is separate and has not happened.
**Rollback:** close the unmerged documentation pull request. Merged PR #6 stays the public authority.
**Disposition:** **HOLD** until this pull request is accepted.

## WO-PAPER-001 — integrated mock vertical slice
**Spec:** [WO-PAPER-001](WO-PAPER-001-integrated-vertical-slice.md). Original scope is unchanged.
**Builder-reported completion:** [paper-bots PR #1](https://github.com/maff0000/paper-bots/pull/1), head `cdfcbb27c4e440fd1597217abc4e9cb34251c65f`, base `3a1144bc544b3bc063808a42c723cbeabffb6ec9`. OPEN / UNMERGED. Six-role standard-library chain, deterministic risk gate, SQLite WAL append-only triggers and hash ledger. 48 tests passed on each of Python 3.9.25 and 3.12.3. No provider or broker network, no hosted CI, no independent audit. ADRs 0001–0004. Synthetic fill is an interface demonstration only. `stop_authorised` false.
**Disposition:** **HOLD**. Builder completion is not acceptance.

## QARP-ROTATION-001 v1.0.0 — builder-reported implementation
**Spec already accepted on main:** [registry](../docs/sbot-strategy-registry.md) version 1.0.0, [SBOT-STRATEGY-001](../research/decisions/2026-11-05-sbot-first-strategy.md).
**Builder-reported completion:** [paper-bots PR #2](https://github.com/maff0000/paper-bots/pull/2), head `b6b7877884df6edc624691b50bb474b2b518ded8`, base `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` (unaccepted). WO-PAPER-002 and ADR 0005. 59 tests passed on each of Python 3.9.25 and 3.12.3, including the prior 48. `entry_authority` NONE. Stop paths HOLD. No live calls. Horizons 5/20/60 incomplete. No investment performance.
**Disposition of the specification:** **ACCEPT** (already on main). **Disposition of the implementation:** **HOLD**. Builder evidence only.

## Private evidence PR — docs only
[paper-bots PR #3](https://github.com/maff0000/paper-bots/pull/3), head `8e05f7f7da9ce232a5e1c38bea760ae231d3e52a`, base `3a1144bc544b3bc063808a42c723cbeabffb6ec9`. OPEN / UNMERGED. July full evidence reported hashed and private-scanned. May full text not recovered. No tests claimed. No policy approved. **HOLD**.

## Stream A — E-Bot PR #2 correction
**Repository PR:** https://github.com/maff0000/ebot/pull/2
**Builder-reported state before the Architect result:** OPEN / UNMERGED. The acceptance below supersedes that state for code only.
**Base reported:** `50c0b66247498672b84e9fcae7e417a538a0e5c1`
**Current reported head:** `3aa95daffe1497725aba8dbd80d4005d5afde16c`
**Superseded reported head:** `adb605fd676d06cf27830f35bf39c06d92d6a119` (grouped-row silent-skip gap was the builder report at that head; not independently reviewed)
**Last head independently reviewed in this public journal:** `9b843dee03892e73f29da31997e5d07bfed564a7`

### Builder-reported at the current head
- Tests: 112 collected, 111 passed, 1 pre-existing skip. Python 3.9.25 and 3.12.3. Zero live calls.
- Files changed this round: `ebot/massive.py`, `ebot/reconcile.py`, `tests/test_reconcile.py`, `docs/redacted-g0-d3-acceptance.md`.
- Non-object grouped rows: provider diagnostic `malformed_row` leads to `INVALID_DATA` for a symbol with no attributed row. No ticker is inferred. Valid object peers remain `PRICE_OK`. Empty results remain `UNCHECKED`.
- Three regression tests run through `urllib_send`.
- Automated trading remains false.
- Remaining reported gaps: no holiday calendar; occupied ID 43 returns `AUTHORISATION_FAILURE`; no substitute id is used.

### Independent evidence
This session could not read `maff0000/ebot`. The four named files were not reviewed and the 112 tests were not re-run. No live call was made. Disposition of the code is therefore not an independent acceptance.

**Architect result, not this session's re-test:** code at `3aa95daffe1497725aba8dbd80d4005d5afde16c` accepted and merged as `79b7ac90fe4cf7c6e974e476baca7c63cc24603f`. 112 tests OK on Python 3.12.14. **CODE ONLY.** G0 stays OPEN. Automated trading is not authorised. This session did not re-fetch the private main.
**Disposition:** **ACCEPT — CODE ONLY.** Earlier HOLD text above is the pre-acceptance builder record.

## Stream C — stop-rule recovery attempt complete
**Authority:** [STOP-RULE-RECOVERY-002](../research/decisions/2026-11-05-stop-rule-recovery-choice.md), [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5) (open).
**Reported result:** the authorised read-only attempt is complete. This public session did not repeat it. The report includes no writes, restarts, broker calls, vendor calls or credential use.
**Recovered:** July brief v0.3 and July architecture v2, full source, private argus commit `46b4d8c8f17490357c6d1536c5027e45341b7f11`. Reported hash match to the compared copies. **Not approved.**
**Not recovered:** the full May Trade doctrine. Access gap. Only the previously cited one-line excerpt is available, and its vol-band parameters are missing. This does not prove that no historical rule ever existed.
**Draft:** private preservation is builder-reported as paper-bots PR #3. QARP entry, exit, initial stop, trailing stop and risk values in that draft are explicitly UNRESOLVED. The draft is not an accepted doctrine.
**Dependency:** owner or operator provides the complete May source through an authorised authenticated exact-record export, or supplies it from backup. No bypass. No further access.
**Hold:** stop-dependent M-Bot and T-Bot paper position management. Other authorised paper work continues.
**Disposition:** recovered July texts **HOLD** (not approved). Missing May source and conflicting legacy profiles **NEED OWNER DECISION/ACCESS**. Stop-dependent M/T **HOLD**.

## FMP entitlement trial — closed pending new authority
**Reported calls:** exactly three, read-only Stable API, key not stored here, raw values not retained.
**Reported outcomes:** `profile` SPY HTTP 200 list length 1; `historical-price-eod/light` SPY for 2026-11-03 through 2026-11-04 HTTP 200 list length 2; `batch-quote` SPY,XOM HTTP 402 non-JSON body, not parsed.
**Rights:** UNVERIFIED. HTTP 402 supports an access or payment restriction on that call. It does not establish plan terms, licence, universe coverage, quotas or redistribution permission. Earlier repository FMP notes are not proof of this key's rights.
**Stop:** no further calls; no subscription upgrade.
**Disposition:** **HOLD**.

## Correction round — builder-reported complete, not accepted
PR #1 candidate `823203059466a30a11fe5a0e677f54c5482dc6fb`: 52 tests passed on each of Python 3.12.3 and 3.9.25. PR #2 candidate `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b`, base `823203059466a30a11fe5a0e677f54c5482dc6fb`, import merge `6b72d03b886502c3d50eb150a918eb676c3fae3a`: 66 tests passed on each interpreter. PR #3 unchanged. No main merge, rebase, force-push, vendor call or broker call. E-Bot not modified. These tests are builder evidence. The Architect's 3.12.14 audit applies to `cdfcbb27c4e440fd1597217abc4e9cb34251c65f` and `b6b7877884df6edc624691b50bb474b2b518ded8` only.
**Disposition:** **HOLD** pending exact-head re-review.

## M1 acceptance and remaining M2 hold
Architect, not this session: PR #1 `823203059466a30a11fe5a0e677f54c5482dc6fb` is accepted and merged as private main `1d4e62de7bd32bbb39b471536d0ba1a71eeffa06` after 52 Python 3.12.14 tests. Mock foundation only. PR #2 `bcaaef3e5c1d8707076b45c29d2e17f93bfebc7b` stays **HOLD** after 66 tests: swapped discovery parents and an incomplete NEO cohort are still accepted. PR #3 stays policy HOLD. Private SHAs were not re-fetched here.

## Next
One bounded correction is assigned and has no head yet. It must reject a swapped discovery parent and an incomplete cohort, validate candidate, event type, producer, run, session, chronology and strategy context, and reject without a partial ledger write. Tests on Python 3.9 and 3.12. Reconcile non-destructively onto `1d4e62de…`. Do not claim a final head before the evidence arrives. G0, FMP rights, the May access gap, doctrine parameters, stop-dependent M/T, scheduling and live execution stay blocked.
