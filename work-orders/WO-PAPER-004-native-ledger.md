# WO-PAPER-004 — attested native envelope ingest (public note)

**Current status, 2026-11-06:** quality-claim validation PROPOSED on the same private PR. Not accepted. Not merged.  
**Authoritative current packet:** [REVIEW-M4-VALID-001](../research/reviews/2026-11-06-wo-paper-004-quality-validation-packet.md), pinned to the head of `cursor/wo-paper-004-public-governance-9fb6`.  
**Standing HOLDs, not withdrawn:** [REVIEW-M4-INDEP-002](../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md) for `f4371c599fb1c45e28c403549090e92fd825ce67`, and [REVIEW-M4-INDEP-001](../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md) for `553ec517455ce6ef797b049e65ec61389daa20da`.  
**Parent PID:** [PID-EQUITY-PAPER-001](../docs/pid-equity-paper-system.md)  
**Private pull request:** [paper-bots #5](https://github.com/maff0000/paper-bots/pull/5)  
**Private work order path, not copied here:** `docs/work-orders/WO-PAPER-004-native-ledger.md`

## Current private head

| Item | Value |
|---|---|
| Public PR #9 start, fetched before this update | `10434796ec77570dd6dba1796d9e6a8caf7287eb` |
| Public main / base | `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| HOLD head that is the parent of the new commit | `f4371c599fb1c45e28c403549090e92fd825ce67` |
| Current head under review | `541f3f175da8ec684f942dea767a1352cf5df0fb` |
| Earlier HOLD, still standing | `553ec517455ce6ef797b049e65ec61389daa20da` |
| Private branch | `cursor/wo-paper-004-native-ledger-ce05` |
| Private base and unchanged paper-bots main | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| State | OPEN, draft false, `merged` false, `merged_at` null, mergeable clean |
| Diff versus accepted main | 10 files, +2129 / −4, 3 commits |
| This private commit | +110 / −9. Message: Reject a non-string quality claim before the allowlist check. |

`quality_state` must be a string before the allowlist test. Missing and null remain `ValidationError`. An object, array, boolean, or number is `ValidationError`, and is not a `TypeError`. E remains `UNCHECKED` only. S, R, M, and T may claim `UNCHECKED` or `NOT_APPLICABLE`, and that claim is stored. NEO review stays `NOT_APPLICABLE`. A missing `parent_event_id` on replay is rejected. A supplied `parent_event_hash` is checked on a new write and on replay. A changed accepted quality claim conflicts and does not append. `note` stays non-semantic. Frozen manifest SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged.

Names for this commit only: `src/paperbots/native_ingest.py`, `tests/test_native_ingest.py`, `docs/adr/0012-native-ledger-ingest.md`, `docs/work-orders/WO-PAPER-004-native-ledger.md`, `README.md`, `RUNBOOK.md`.

Builder transcript, not an Architect run, at `/tmp/wo004-quality`: Python 3.9.25 stderr `Ran 117 tests in 0.896s` OK; Python 3.12.3 stderr `Ran 117 tests in 0.903s` OK. Stdout empty. The HOLD head had 115 tests. CLI probe exit 1, stderr starts with `ValidationError:`, no traceback.

Live native execution remains UNVERIFIED. No host ACL. NEO may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`. `order_created` and `is_fill` stay false. G0 stays OPEN. Rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. No fourth call. No merge, live orders, vendor calls, scheduler, or new entry/exit/stop/risk parameters. Stop-dependent M/T stays HOLD.

Requested next step: Architect independent re-audit of `541f3f175da8ec684f942dea767a1352cf5df0fb`, then ACCEPT or HOLD on that exact head. This note is the handoff. It is not the decision, and it does not withdraw either HOLD.

## Replay-correction proposal — head `f4371c59`, later held

**Status at that time:** replay-integrity correction PROPOSED. Not accepted. Not merged. The HOLD of `553ec517455ce6ef797b049e65ec61389daa20da` stood.  
**Packet for that head:** [REVIEW-M4-REPLAY-001](../research/reviews/2026-11-06-wo-paper-004-replay-correction-packet.md)  
**Later decision:** [REVIEW-M4-INDEP-002](../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md).

Parent-read design of that proposal: one causal-parent check covers a new write and a replay. S, R, M, and T must name `parent_event_id`. A supplied `parent_event_hash` must match the stored parent. The writer does not fill either value from history. E remains `UNCHECKED` only. S, R, M, and T may claim `UNCHECKED` or `NOT_APPLICABLE`, and that claim is the stored `quality_state`. Changing it either way is an idempotency conflict and does not append. NEO's review stays `NOT_APPLICABLE`. `note` is non-semantic and cannot grant a role, parent, quality, or trading permission. Frozen manifest SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged.

Correction names only: `src/paperbots/native_ingest.py`, `tests/test_native_ingest.py`, `docs/adr/0012-native-ledger-ingest.md`, `docs/work-orders/WO-PAPER-004-native-ledger.md`, `README.md`, `RUNBOOK.md`.

Builder transcript, not an Architect run, at `/tmp/wo004-replay`: Python 3.9.25 stderr `Ran 115 tests in 0.765s` OK; Python 3.12.3 stderr `Ran 115 tests in 0.922s` OK. Stdout empty. The 115 include the 110 from the HOLD head plus missing-parent replay, contradictory parent hash, both quality directions, a changed identity claim, and the unchanged no-order / NEO checks.

Live native execution remains UNVERIFIED. No host ACL. The ingest check is not a host principal. NEO may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`. `order_created` and `is_fill` stay false. G0 stays OPEN. Rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. No fourth call. No merge, live orders, vendor calls, scheduler, or new entry/exit/stop/risk parameters. Stop-dependent M/T stays HOLD.

Requested next step at the time of that proposal: Architect independent re-audit of `f4371c599fb1c45e28c403549090e92fd825ce67`. That review is now REVIEW-M4-INDEP-002. The current requested review is the head in the section above.

## Original proposal record — head `553ec517`, later held

**Status at that time:** PROPOSED. Open on private paper-bots PR #5. Not accepted. Not merged.  
**Date:** 2026-11-06 (Europe/London)  
**Packet for that head:** [REVIEW-M4-NATIVE-001](../research/reviews/2026-11-06-wo-paper-004-native-ledger-packet.md)

## Heads recorded for the original proposal

| Item | Value |
|---|---|
| Public base, fetched before this note | `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| Private head of that proposal, later held | `553ec517455ce6ef797b049e65ec61389daa20da` |
| Private branch | `cursor/wo-paper-004-native-ledger-ce05` |
| Private base and unchanged paper-bots main | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| State | OPEN, `merged` false, `merged_at` null |
| Diff | 10 files, +1828 / −4, 1 commit |

Accepted M3 remains [REVIEW-M3-ACCEPT-001](../research/reviews/2026-11-06-m3-70a673-independent-acceptance.md): private PR #4 head `70a673f973bd52155d495f6873eb417374f4948b` merged to the paper-bots main SHA above. This note does not reopen that acceptance.

## What the private increment proposes

Private ADR 0012 amends private ADR 0010 and implements the adapter named in public [ADR-APP-001](../docs/adr/ADR-APP-001-platform-findings.md). `native-probe-1` still does not write. `native-ledger-1` is `paperbots.native_ingest`.

The attested native bot id is an argument and selects the role from the allowlist. A producer string inside the envelope is a claim and cannot append another role's event. One transactional writer sits in front of the existing ledger.

The synthetic chain is an UNCHECKED E candidate; an S screen of frozen QARP-ROTATION-001 v1.0.0 with entry authority NONE and UNKNOWN classification and source mapping; R HOLD; M research HOLD with no proposal; T `EXECUTION_REFUSAL` / `NO_ORDER` with `order_created` and `is_fill` false; NEO reconstructs the chain and may append `NEO_REVIEW` only. Frozen manifest SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged.

Builder-named interface, for the Architect's review of the private tree:

```text
python -m paperbots.native_ingest --attested-native-bot-id <platform id> --envelope <file>
```

Private fixture contents stay private. The real provisioned bot UUIDs are attested-identity fixtures. A live teammate message was not sent. Native-to-Python execution remains UNVERIFIED.

## Tests, as parent-confirmed builder transcript

Fresh detached worktree `/tmp/wo004-final` at the private head. Not an Architect run.

- Python 3.9.25: `PYTHONPATH=src python3.9 -m unittest discover -s tests -v` exited 0. Stderr `Ran 110 tests in 0.785s` / OK. Stdout empty.
- Python 3.12.3: `PYTHONPATH=src python3.12 -m unittest discover -s tests -v` exited 0. Builder final report stderr `Ran 110 tests in 0.696s` / OK. Stdout empty. Parent notes also record an earlier same-tree `Ran 110 tests in 0.691s` and a detached line `PY312 STDERR SUMMARY Ran 110 tests. OK`.

The integer 110 was observed on stderr. It includes the previously accepted tests plus `tests/test_native_ingest.py`.

## Isolation that was and was not built

In-process ingest refuses NEO writing decision or execution events. The pre-existing NEO handle may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`. That allowlist was not widened. No host ACL was created. One user's bots share the computer, files, logins, and permitted connectors. There is no switch that disables bot-to-bot messages. A JSON producer field does not authenticate the sender. A separate OS principal that alone can open the ledger, with the parent attesting the bot id from platform metadata, was proposed and not built.

## Exclusions

No merge. No live orders. No vendor calls. No scheduler. No new entry, exit, stop, or risk parameters. Stop-dependent M/T stays HOLD. G0 stays OPEN. Rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. No fourth call.

## Requested next step at the time of the original proposal

Architect independent re-audit of `553ec517455ce6ef797b049e65ec61389daa20da`, then ACCEPT or HOLD on that exact head. That review is now [REVIEW-M4-INDEP-001](../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md). The current requested review is the head in the section above.
