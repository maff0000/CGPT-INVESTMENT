# WO-PAPER-004 — quality-claim type guard

**ID:** REVIEW-M4-VALID-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for a bounded correction on the existing private pull request.  
**Disposition requested:** Architect **ACCEPT or HOLD** after an independent re-audit of exact private head `541f3f175da8ec684f942dea767a1352cf5df0fb`.  
**This packet does not accept that head.** It does not merge private paper-bots PR #5 or public PR #9. It does not withdraw the HOLDs of `553ec517455ce6ef797b049e65ec61389daa20da` or `f4371c599fb1c45e28c403549090e92fd825ce67`.

[REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Neither file is edited here. [REVIEW-M4-REPLAY-001](2026-11-06-wo-paper-004-replay-correction-packet.md) stays the historical proposal of the replay correction. Accepted M3 history stays accepted in [REVIEW-M3-ACCEPT-001](2026-11-06-m3-70a673-independent-acceptance.md): private PR #4 head `70a673f973bd52155d495f6873eb417374f4948b`, paper-bots main `b2cb75867d2408a0018333213a0dd2cfb91ac670`, public main `b0c8f55109fcc92d8f55ec7b593c696b9887475d`.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-004-public-governance-9fb6` after that commit is pushed.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `b0c8f55109fcc92d8f55ec7b593c696b9887475d`. Public PR #9 head `10434796ec77570dd6dba1796d9e6a8caf7287eb`, parent `62769b0206eb11c84a3d618c31106bd106d855c3`. PR #9 OPEN, draft false, `mergedAt` null, base that same main SHA |
| Parent-verified private read-back, 2026-11-06 Europe/London | PR #5 state after the quality-claim correction, both private SHAs, the new commit's parent, file names, reproduced `TypeError`, design, and builder stderr count 117 |
| Not claimed here | Architect acceptance of `541f3f17`, withdrawal of either HOLD, a merge, host ACL, live native execution, vendor rights, or a fourth FMP call |

This public session did not open `maff0000/paper-bots` and did not copy private source, fixtures, raw vendor data, or credentials.

## Heads

| Item | SHA / state |
|---|---|
| Public PR #9 start for this update | `10434796ec77570dd6dba1796d9e6a8caf7287eb` |
| Parent of that public commit | `62769b0206eb11c84a3d618c31106bd106d855c3` |
| Public `main` / PR #9 base | `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| Private PR | [paper-bots #5](https://github.com/maff0000/paper-bots/pull/5) |
| Private branch | `cursor/wo-paper-004-native-ledger-ce05` |
| Starting HOLD head, REVIEW-M4-INDEP-002 | `f4371c599fb1c45e28c403549090e92fd825ce67` |
| Parent of the new private commit | `f4371c599fb1c45e28c403549090e92fd825ce67` |
| Ending / current private head under review | `541f3f175da8ec684f942dea767a1352cf5df0fb` |
| Private commit message | Reject a non-string quality claim before the allowlist check. |
| Unchanged paper-bots main and PR base | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| Private state | OPEN, draft false, `merged` false, `merged_at` null, mergeable clean |
| Private PR versus accepted main | 3 commits, 10 files, +2129 / −4 |
| This private commit only | +110 / −9 |
| Earlier HOLD, still standing | `553ec517455ce6ef797b049e65ec61389daa20da`, REVIEW-M4-INDEP-001 |
| Frozen QARP-ROTATION-001 v1.0.0 manifest SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Public note | [WO-PAPER-004](../../work-orders/WO-PAPER-004-native-ledger.md), pinned to this branch head |

## Reproduced failure on the HOLD head

On `f4371c599fb1c45e28c403549090e92fd825ce67`, a valid synthetic E envelope whose `quality_state` was replaced by the object `{"unsafe":"UNCHECKED"}` raised unhandled `TypeError: unhashable type: 'dict'` at the quality allowlist membership test. An equivalent list raised `TypeError: unhashable type: 'list'`. Ledger row count and hash tip were unchanged. The CLI did not catch `TypeError`. This matches the failure recorded in REVIEW-M4-INDEP-002.

## Correction

Parent-read behaviour, not an Architect confirmation. `quality_state` must be a string before the allowlist test. Missing and null remain `ValidationError`. An object, array, boolean, or number is `ValidationError`, and is not a `TypeError`. Accepted string values and role-specific restrictions are unchanged:

- E is `UNCHECKED` only.
- S, R, M, and T may claim `UNCHECKED` or `NOT_APPLICABLE`, and that claim is stored.
- NEO review stays `NOT_APPLICABLE`.

The three earlier replay-integrity behaviours remain. A missing `parent_event_id` on replay is rejected. A supplied `parent_event_hash` is checked on a new write and on replay. A changed accepted quality claim conflicts and does not append. `note` remains a non-semantic diagnostic.

The path still records research HOLD and `NO_ORDER` evidence only. `order_created` and `is_fill` stay false.

## Correction file names

Names only, for the new private commit. No source is copied.

1. `src/paperbots/native_ingest.py`
2. `tests/test_native_ingest.py`
3. `docs/adr/0012-native-ledger-ingest.md`
4. `docs/work-orders/WO-PAPER-004-native-ledger.md`
5. `README.md`
6. `RUNBOOK.md`

## Tests

Builder transcript, not an Architect run. Detached worktree `/tmp/wo004-quality` at `541f3f175da8ec684f942dea767a1352cf5df0fb`. Stdout empty, 0 bytes, on both commands.

`PYTHONPATH=src python3.9 -m unittest discover -s tests -v`

- Interpreter: Python 3.9.25
- Exit 0
- Stderr: `Ran 117 tests in 0.896s` / OK

`PYTHONPATH=src python3.12 -m unittest discover -s tests -v`

- Interpreter: Python 3.12.3
- Exit 0
- Stderr: `Ran 117 tests in 0.903s` / OK

The integer 117 was observed on stderr. The HOLD head `f4371c59` had 115 tests. A CLI probe of the corrected tree exited 1. Stderr starts with `ValidationError:`. There is no traceback. Builder tests are not Architect acceptance.

## Remaining limitations

- The demonstrated path is an in-process synthetic adapter.
- Live native execution remains **UNVERIFIED**.
- Native platform authentication is not implemented.
- A protected NEO host principal is not implemented. The ingest check is not a host ACL.
- The pre-existing NEO handle may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`.
- This packet does not withdraw REVIEW-M4-INDEP-001 or REVIEW-M4-INDEP-002.

## Operational restrictions

- **G0 remains OPEN.** Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. There is no fourth call.
- Stop-dependent M/T remains **HOLD**.
- No broker, vendor call, scheduler, live order, new risk parameter, or merge.
- No new entry, exit, or stop parameter.

## Proposed disposition

Request an Architect re-audit of exact private head `541f3f175da8ec684f942dea767a1352cf5df0fb`, then an **ACCEPT** or **HOLD** recorded against that SHA. Until that independent review exists, the correction stays proposed. The HOLDs of `553ec517455ce6ef797b049e65ec61389daa20da` and `f4371c599fb1c45e28c403549090e92fd825ce67` stand for those heads. This public packet is the handoff. It is not that decision.
