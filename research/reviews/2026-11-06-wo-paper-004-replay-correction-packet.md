# WO-PAPER-004 — replay-integrity correction

**ID:** REVIEW-M4-REPLAY-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for a bounded correction on the existing private pull request.  
**Disposition requested:** Architect **ACCEPT or HOLD** after an independent re-audit of exact private head `f4371c599fb1c45e28c403549090e92fd825ce67`.  
**This packet does not accept the increment.** It does not merge private paper-bots PR #5 or public PR #9.

[REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the **HOLD** of `553ec517455ce6ef797b049e65ec61389daa20da`. This packet does not withdraw that HOLD and does not edit that file. Accepted M3 history stays accepted in [REVIEW-M3-ACCEPT-001](2026-11-06-m3-70a673-independent-acceptance.md): private PR #4 head `70a673f973bd52155d495f6873eb417374f4948b`, paper-bots main `b2cb75867d2408a0018333213a0dd2cfb91ac670`.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `origin/main` `b0c8f55109fcc92d8f55ec7b593c696b9887475d`. Public PR #9 head and `origin/cursor/wo-paper-004-public-governance-9fb6` `0cf2d0cb77501343df4ab9755940794b93ec14c4`. PR #9 OPEN, `mergedAt` null, base that same main SHA |
| Parent-verified private read-back, 2026-11-06 Europe/London | PR #5 state after the correction, both private SHAs, diff size, correction file names, reproduced failures, design text, and the builder stderr count 115 |
| Not claimed here | Architect acceptance of `f4371c59`, withdrawal of the HOLD at `553ec517`, a merge, host ACL, live native execution, vendor rights, or a fourth FMP call |

This public session did not open `maff0000/paper-bots` and did not copy private source, fixtures, raw vendor data, or credentials. The SHA of the public commit that adds this packet is intentionally absent from this file. Read the public branch after push.

## Starting and ending heads

| Item | SHA / state |
|---|---|
| Public PR #9 start for this update | `0cf2d0cb77501343df4ab9755940794b93ec14c4` |
| Public `main` / PR #9 base | `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| Private PR | [paper-bots #5](https://github.com/maff0000/paper-bots/pull/5), title "WO-PAPER-004: attested native envelope ingest" |
| Private branch | `cursor/wo-paper-004-native-ledger-ce05` |
| Starting HOLD head | `553ec517455ce6ef797b049e65ec61389daa20da` |
| Ending / current private head under review | `f4371c599fb1c45e28c403549090e92fd825ce67` |
| Unchanged paper-bots main and PR base | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| Private state | OPEN, `merged` false, `merged_at` null, draft false |
| Commits on the private PR | 2 |
| Diff versus accepted main | 10 files, +2028 / −4 |
| Frozen QARP-ROTATION-001 v1.0.0 manifest SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Public note | [WO-PAPER-004](../../work-orders/WO-PAPER-004-native-ledger.md) |

## Reproduced failures on the HOLD head

These are the failures reproduced on `553ec517455ce6ef797b049e65ec61389daa20da`, matching [REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) and the [Architect comment](https://github.com/maff0000/paper-bots/pull/5#issuecomment-6680880523). Row count and hash tip did not change. The parent read-back classes that as input-to-evidence fidelity, not deletion.

1. Replay S after removing `parent_event_id` returned `duplicate=True`. The replay helper copied the stored predecessor.
2. Replay S with `parent_event_hash` of 64 zeros returned `duplicate=True`. Only the new-write path checked a supplied hash.
3. Replay R changing `quality_state` from `NOT_APPLICABLE` to `UNCHECKED` returned `duplicate=True` because the writer stored `NOT_APPLICABLE`.

## Correction design

Parent-read from the updated private PR body. This is the recorded design, not an Architect confirmation that the three probes now conflict.

One causal-parent check now covers a new write and a replay. S, R, M, and T must name `parent_event_id`. A supplied `parent_event_hash` must match the stored parent. The writer does not fill either value from history.

E remains `UNCHECKED` only. S, R, M, and T may claim `UNCHECKED` or `NOT_APPLICABLE`, and that claim is the stored `quality_state`. Changing it either way is an idempotency conflict and does not append. NEO's review stays `NOT_APPLICABLE`. A different NEO quality claim is rejected.

`note` is intentionally non-semantic. It is not copied into the event and cannot grant a role, a parent, a quality, or trading permission, so a retry that changes only `note` stays `duplicate=True`. An unchanged semantic retry also stays `duplicate=True`. ADR 0012 records the field split.

The path still records research HOLD and `NO_ORDER` evidence only. `order_created` and `is_fill` stay false.

## Correction file names

Names only. No source is copied. These are the files the parent names for the correction. The pull request versus accepted main remains the 10-file diff above.

1. `src/paperbots/native_ingest.py`
2. `tests/test_native_ingest.py`
3. `docs/adr/0012-native-ledger-ingest.md`
4. `docs/work-orders/WO-PAPER-004-native-ledger.md`
5. `README.md`
6. `RUNBOOK.md`

## Tests

Builder transcript, not an Architect run. Detached worktree `/tmp/wo004-replay` at `f4371c599fb1c45e28c403549090e92fd825ce67`. Stdout empty on both commands.

`PYTHONPATH=src python3.9 -m unittest discover -s tests -v`

- Interpreter: Python 3.9.25
- Exit 0
- Stderr: `Ran 115 tests in 0.765s` / OK

`PYTHONPATH=src python3.12 -m unittest discover -s tests -v`

- Interpreter: Python 3.12.3
- Exit 0
- Stderr: `Ran 115 tests in 0.922s` / OK

The integer 115 was observed on stderr. The HOLD head had 110 tests. These 115 include those tests plus missing-parent replay, contradictory parent hash, both quality directions, a changed identity claim, and the unchanged no-order / NEO checks. Builder tests are not Architect acceptance.

## Remaining limitations

- The demonstrated path is an in-process synthetic adapter.
- Live native execution remains **UNVERIFIED**. Native platform authentication is not implemented.
- A protected NEO host principal is not implemented. The ingest check is not a host ACL.
- The pre-existing NEO handle may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`.
- One user's bots share the computer, files, logins, and permitted connectors. A JSON producer field does not authenticate the sender.
- This correction does not withdraw the HOLD at `553ec517455ce6ef797b049e65ec61389daa20da`.

## Security, data rights, and restrictions

- **G0 remains OPEN.** Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. That third result is an HTTP 402 non-JSON response. It is not a label "call 402". There is no fourth call.
- No merge of private PR #5 or of public PR #9 is authorised by this packet.
- No live orders, broker writes, vendor calls, bot messages, or scheduler.
- No new entry, exit, stop, or risk parameter. Stop-dependent M/T remains **HOLD**.

## Proposed disposition

Request an Architect re-audit of exact private head `f4371c599fb1c45e28c403549090e92fd825ce67`, then an **ACCEPT** or **HOLD** recorded against that SHA. Until that independent review exists, the correction stays proposed. The HOLD of `553ec517455ce6ef797b049e65ec61389daa20da` stands for that head. Passing builder tests and this public packet are review inputs. They are not the decision.

Paper-bots main stays `b2cb75867d2408a0018333213a0dd2cfb91ac670`. Public main stays `b0c8f55109fcc92d8f55ec7b593c696b9887475d` until a later reviewed merge of this governance record. This file performs neither merge.
