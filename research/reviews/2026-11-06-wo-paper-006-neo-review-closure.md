# REVIEW-M6-NEO-004 — WO-PAPER-006 private merge closure

**ID:** REVIEW-M6-NEO-004
**Date:** 6 November 2026 (Europe/London)
**Record type:** public closure of the private merge. Public [PR #13](https://github.com/maff0000/CGPT-INVESTMENT/pull/13) is not merged.
**Private pull request:** [paper-bots #9](https://github.com/maff0000/paper-bots/pull/9), `merged` true, `state` closed, not draft.
**Private merge SHA and verified private main:** `28fe536e03ab8df1704d119b045158cc0a766f4f`
**Accepted implementation SHA:** `4b3dac4c4137a5cb89a9587862e5fe25c464887b`

This file does not merge public PR #13. It does not invent a public merge SHA, and it does not quote a prospective public `merge_commit_sha`. It does not contain the SHA of the public commit that adds it. It is pinned to the head of `cursor/wo-paper-006-neo-review-packet-5d19` after that commit is pushed. The parent of this public commit is `e1a4399a9d9825c34b5366f3a87b03db1d7ae4bd`.

[REVIEW-M6-NEO-001](2026-11-06-wo-paper-006-neo-review-packet.md), [REVIEW-M6-NEO-002](2026-11-06-wo-paper-006-neo-review-correction-packet.md), and [REVIEW-M6-NEO-003](2026-11-06-wo-paper-006-neo-review-acceptance.md) stay. Their historical request, HOLD, and ACCEPT text is not rewritten. Historical REVIEW-M5 records are not edited.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | Public branch `cursor/wo-paper-006-neo-review-packet-5d19` head `e1a4399a9d9825c34b5366f3a87b03db1d7ae4bd`, parent `0295b9c8f167be2b1939ae7f084a32b557c7e1b9`. `git fetch origin main` returned `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. That main is unchanged. This session did not merge public PR #13 |
| Parent-supplied private read-back, 6 November 2026, Europe/London | The ordinary merge of private PR #9, `merged` true, `merged_at`, `merged_by`, the merge commit, its parents, its message, the tree comparison, and the confirmation that the accepted source was not modified after acceptance. This session could not open `maff0000/paper-bots` |
| Not claimed here | A public merge, a public merge SHA, a change to the accepted implementation, a sent handoff, trading activation, replacement of QARP-ROTATION-001 v1.0.0, sender authentication, Increment C deployment, a change of G0, verified provider rights, or release of stop-dependent M/T |

No private Python, tests, fixtures, credentials, or schema catalog JSON are copied here.

## Private merge

Parent merged private PR #9 with GitHub's ordinary merge commit (`merge_method=merge`), pinned to accepted head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`, then read the result back from GitHub.

| Item | Value |
|---|---|
| Private PR #9 | `merged` true, `state` closed, not draft |
| `merged_at` | `2026-11-06T14:38:00Z` (14:38 Europe/London) |
| `merged_by` | `maff0000` |
| Head SHA on that pull request | `4b3dac4c4137a5cb89a9587862e5fe25c464887b` |
| Actual merge commit | `28fe536e03ab8df1704d119b045158cc0a766f4f` |
| Verified private `main` | `28fe536e03ab8df1704d119b045158cc0a766f4f` |
| Merge commit message | `Merge PR #9 — WO-PAPER-006 synthetic NEO review` |
| First parent | `c0b9f540c09caec08fb87e77bf445d0e580f843e` (previous main, `Merge PR #8 — WO-PAPER-005 Increment C security-boundary design`) |
| Second parent | `4b3dac4c4137a5cb89a9587862e5fe25c464887b` (accepted head) |
| Compare `4b3dac4` to `28fe536e` | ahead, ahead 1, behind 0. The only additional commit is the merge commit |
| Merge-commit tree | `0b6fdcf3a14976b611fa22b9c4b44759c857f02f`, matching the accepted-head tree |
| Method | Ordinary merge. No squash. No rebase. No force-push |

Private main therefore contains the exact accepted implementation. The accepted private source was not modified after acceptance.

## History that stays

- [REVIEW-M6-NEO-001](2026-11-06-wo-paper-006-neo-review-packet.md) remains the historical request of submitted head `619a607ed1879c93a82e4e652b2edc7531efb530`. The HOLD of that head remains historical.
- [REVIEW-M6-NEO-002](2026-11-06-wo-paper-006-neo-review-correction-packet.md) remains the historical request of the correction. Intermediate head `4078c6a560901ea67eb217f0486cdc18d045efa2` remains historical.
- [REVIEW-M6-NEO-003](2026-11-06-wo-paper-006-neo-review-acceptance.md) remains the Architect ACCEPT of exact implementation `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. That acceptance does not apply to any later commit. The merge commit is not a new implementation.
- Historical REVIEW-M5 records are not edited.

## What this merge does not do

No live handoff was sent. Trading authority was not activated. QARP-ROTATION-001 v1.0.0 was not replaced. Frozen file SHA-256 remains `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. Ruleset digest remains `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. G0 remains OPEN. Provider rights remain UNVERIFIED. Stop-dependent M/T remain HOLD. Increment C isolation remains undeployed. `authenticates_sender` stays false. `parent_platform_metadata` stays refused.

Builder-reported Python 3.12.3 `Ran 162 tests`, `OK`, and `paperbots.decision_evidence check` reporting nine findings, remain builder-reported. The Architect reviewed code, contract, schema, and tests and did not independently execute Python. The parent did not re-execute Python.

## Public pull request

Public main remains `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. Public PR #13 is not merged by this record. No public merge SHA is named.
