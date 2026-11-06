# WO-PAPER-005 — offline native transport (public note)

> **CURRENT ARCHITECT DECISION — 6 November 2026: WO-PAPER-005 Increment B OFFLINE SIMULATED INBOUND ACCEPTED AND MERGED.** Independent exact-head review accepted [paper-bots PR #7](https://github.com/maff0000/paper-bots/pull/7) at `124c0f2af9e7a60a783718516c20697f3dd3c386`: **101/101 reconstructed Git blobs matched; 152/152 Python 3.12.14 tests passed; independent adverse-input and replay probes passed.** Private main was merged by ordinary merge commit `b30d0ce048317e064a2eccbfd0589ac29799d626`. See [REVIEW-M5-INDEP-002](../research/reviews/2026-11-06-wo-paper-005-124c0f-independent-acceptance.md). Previous 'CURRENT — Proposed' notices below are retained as chronological builder evidence but **superseded by this Architect decision**. Acceptance applies only to `simulated_inbound_handoff` and the previously accepted offline spool; presented native ID is **not authenticated**. `parent_platform_metadata`, real native messaging, NEO host/principal isolation and sender authentication remain **HOLD pending separate authority and Increment C**. G0 **OPEN**, source rights **UNVERIFIED**, stop-dependent M/T **HOLD**; no broker/vendor/account-data calls, scheduler, live orders or new trading parameters.

> **CURRENT ARCHITECT DECISION — 6 November 2026: ACCEPTED AND MERGED, WO-PAPER-005 Increment A (OFFLINE SYNTHETIC ONLY).** Private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) exact head `b87354d77dc4d94273291ae571c3837924f22fdd` passed independent Python 3.12.14 tests **136/136** plus separate synthetic chain, successful receipt recovery, altered/missing/corrupt sidecar quarantine, and crash-before-receipt replay probes. Private main is merge commit `ba001debca9e695fc3356c8720a17fa15836c31c`. See [REVIEW-M5-ACCEPT-001](../research/reviews/2026-11-06-wo-paper-005-b87354-independent-acceptance.md). The previous [REVIEW-M5-INDEP-001](../research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) **remains historical HOLD for exact older head** `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` **only**; similarly earlier M4 exact-head HOLDs and ACCEPT remain unchanged. Earlier 'CURRENT' status notices below are retained as chronological evidence and **superseded by this notice**. This acceptance does **not** authenticate native senders, implement a host ACL or protected NEO identity, authorise real bot messaging, or enable Increment B/C. G0 **OPEN**; provider rights **UNVERIFIED**; stop-dependent M/T **HOLD**; no vendor/broker/account reads, scheduler, live orders, risk parameter change, or host principal change.

> **HISTORICAL EXACT-HEAD HOLD (SUPERSEDED FOR CURRENT STATUS) — WO-PAPER-005 INCREMENT A HOLD (6 Nov 2026).** The independent review **HOLDs** private paper-bots PR #6 exact head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` after 132/132 independently run Python 3.12.14 tests and a separate crash/recovery probe that found a corrupted processing envelope silently archived as `accepted` when a terminal receipt exists. Read [REVIEW-M5-INDEP-001](https://github.com/maff0000/CGPT-INVESTMENT/blob/330c006522effd37ca435f754659f075564d6f72/research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) and [private PR #6 corrective instructions](https://github.com/maff0000/paper-bots/pull/6#issuecomment-6683142810). **The earlier 'CURRENT/PROPOSED' builder notices below are historical pre-audit snapshots; do not accept or merge PRs #6/#10.** M4 remains ACCEPTED. G0 OPEN, provider rights UNVERIFIED, FMP three historical calls only, stop-dependent M/T HOLD; native messaging/host ACL remain UNVERIFIED; no live/vendor/broker calls, scheduling or orders.

> **CURRENT — Increment A, 6 Nov 2026. Proposed. Not accepted. Not merged.** Private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` is parent-verified OPEN, draft false, `merged` false, `merged_at` null, mergeable clean. Parent of that commit, and unchanged paper-bots main, is `ff13c49ce2535992c7216f5742946b33bd805e53`. [REVIEW-M5-TRANSPORT-001](../research/reviews/2026-11-06-wo-paper-005-offline-transport-packet.md) is pinned to the head of `cursor/wo-paper-005-transport-packet-f3e8` and does not contain that public commit's SHA. Builder 132/132 is not Architect acceptance. This increment does not authenticate native senders and does not implement a host access-control list. [REVIEW-M4-ACCEPT-001](../research/reviews/2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains accepted history for the offline in-process adapter only. Earlier HOLDs of `553ec517455ce6ef797b049e65ec61389daa20da` and `f4371c599fb1c45e28c403549090e92fd825ce67` remain valid only for those older exact heads.

**Status:** Recovery-integrity correction PROPOSED for Architect ACCEPT or HOLD of `b87354d77dc4d94273291ae571c3837924f22fdd`. Not accepted. Not merged. REVIEW-M5-INDEP-001 still HOLDs `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only.  
**Authoritative packet:** [REVIEW-M5-TRANSPORT-002](../research/reviews/2026-11-06-wo-paper-005-recovery-integrity-packet.md)  
**Historical packet for the held head:** [REVIEW-M5-TRANSPORT-001](../research/reviews/2026-11-06-wo-paper-005-offline-transport-packet.md)  
**Parent PID:** [PID-EQUITY-PAPER-001](../docs/pid-equity-paper-system.md)  
**Private pull request:** [paper-bots #6](https://github.com/maff0000/paper-bots/pull/6)  
**Private work order path, not copied here:** `docs/work-orders/WO-PAPER-005-native-transport.md`  
**Accepted predecessor:** [WO-PAPER-004](WO-PAPER-004-native-ledger.md), paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`

## Recovery-integrity correction under review

Parent-read behaviour, not an Architect confirmation. A terminal successful receipt (`accepted` or `duplicate`) no longer authorises archive by itself. Recovery rechecks the staged envelope and attestation against the durable receipt: envelope SHA-256, submission id, attested native identity, source, and transport contract. A match archives and returns the stored receipt. A mismatch, a missing sidecar, or a corrupt sidecar leaves the original receipt untouched, retains the mismatching evidence in quarantine, and writes a separate recovery record with `kind` `RECOVERY_INTEGRITY`. The ledger is not appended to, and row count and hash tip stay unchanged. Matching recovery, crash-before-receipt duplicate behaviour with no second append, and retryable ledger-outage behaviour remain intact.

The private correction is `b87354d77dc4d94273291ae571c3837924f22fdd`, parent `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`, message `Revalidate successful spool recovery before archive.` Private PR #6 stays OPEN: 2 commits, 23 files, +2043/−3 versus accepted main. The correction itself is 6 files, +312/−12, covering documentation plus the offline transport implementation and its tests. Those implementation and test paths are not named here.

Builder transcript, not an Architect run, detached worktree at the new private head: Python 3.9.25 exit 0, stdout 0 bytes, wall 1.954s, stderr `Ran 136 tests in 1.615s` / OK; Python 3.12.3 exit 0, stdout 0 bytes, wall 1.266s, stderr `Ran 136 tests in 1.108s` / OK. The held head had 132. Builder 136/136 is not Architect acceptance.

Quarantine is retention, not a host access-control list. This correction does not authenticate native senders. Increments B and C stay gated. G0 stays OPEN. Provider rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. No fourth call. Stop-dependent M/T stays HOLD. No merge.

Requested next step: Architect ACCEPT or HOLD of exact private head `b87354d77dc4d94273291ae571c3837924f22fdd`. This note is not that decision.

## Parent-verified heads

The table below is the Increment A proposal later held by REVIEW-M5-INDEP-001. It is not the head now under review.

| Item | Value |
|---|---|
| Public `origin/main` before this note | `1fc4491a095d914b855a2653cb8b753c7fbc3f13` |
| Parents of that public main | `b0c8f55109fcc92d8f55ec7b593c696b9887475d`, `8d3c32ebd34c94d182833e7fcb865865bf62e1e5` |
| Private branch | `cursor/wo-paper-005-native-transport-2076` |
| Private head under review | `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` |
| Parent of that commit / unchanged paper-bots main | `ff13c49ce2535992c7216f5742946b33bd805e53` |
| Private state | OPEN, draft false, `merged` false, `merged_at` null, mergeable clean |
| Diff versus accepted main | 1 commit, 23 files, +1743 / −3 |
| Private commit message | Add an offline spool in front of the accepted native writer. |

Merged public [PR #9](https://github.com/maff0000/CGPT-INVESTMENT/pull/9) is the closed WO-PAPER-004 governance record. This note does not reopen it.

## Discovery findings

Re-read on 6 Nov 2026 from the public pages. No probe was sent.

- [Security FAQ](https://docs.x.ai/grok-bot/security-faq): isolation is per Cursor user. Bots of one user share one computer. A Bot has no identity of its own. A workload that needs its own computer and credential set is given its own Cursor user.
- [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps): files, sign-ins, and command-line credentials are shared. Screens are separate work surfaces and are not security boundaries.
- [Security](https://cursor.com/docs/grok-bot/security): a Bot has no identity or credentials of its own and acts as the signed-in member.
- [Bots](https://docs.x.ai/grok-bot/bots): separate names, conversations, and memory still share the computer. Files and sign-ins are not isolated per Bot.
- [Chat and collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration): there is no switch that disables bot-to-bot messaging.
- [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises): one user's Bots share one computer, files, logins, and permitted connectors. The documented separate-computer path is a separate Cursor user.

A shared mailbox, an HMAC file, or an in-process role check is rejected as theatre in private ADR 0013. Those mechanisms are not built here.

## Increment A — demonstrated on the private head

Offline spool in front of accepted `paperbots.native_ingest`. Submission is an untrusted envelope plus a separate attestation sidecar (`attested_native_bot_id`, `attestation_source`, `submission_id`, envelope file SHA-256). The envelope cannot mint the sidecar. Missing, mismatched, or non-allowlisted attestation is fail-closed and does not write.

Receipts: `accepted` (event id and hash), `duplicate`, `conflict`, `validation`, `permission`, `attestation_missing`, `transport_error`. Exclusive lock. Crash or outage drain does not double-append. A crash after commit and before the receipt is `duplicate`, because the receipt follows ledger state. Drain order is lexical `submission_id`. One ledger transaction per submission.

Only `synthetic_fixture` is accepted. `parent_platform_metadata` is named and refused, so a source label cannot be read as platform proof.

The NEO snapshot reader has no write method. The snapshot hash detects truncation and is not a signature. The reader does not stop another same-user Bot from opening the ledger file.

## Increments B and C — gated

| Increment | What it would be | State |
|---|---|---|
| B | Parent-mediated live native messaging | Not implemented |
| C | Dedicated writer/NEO principal. Official recommendation: a separate Cursor user | Not implemented |

Neither increment is this pull request. No bot message was sent. No host principal was changed.

## Unchanged decision semantics

Replay, quality type guard, role binding, causal parents, and `note` as non-semantic stay as accepted in WO-PAPER-004. Synthetic path remains `NO_ORDER`, with `order_created` false and `is_fill` false. Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` is unchanged.

## Private names

Names only. Fixture bodies are not copied. The 23-file diff includes files inside the fixture directory.

- `src/paperbots/native_transport.py`
- `src/paperbots/errors.py`
- `tests/test_native_transport.py`
- `docs/adr/0013-offline-native-transport.md`
- `docs/work-orders/WO-PAPER-005-native-transport.md`
- `fixtures/native/wo005_transport/`
- Pointer updates: `docs/adr/0010-native-role-contract.md`, `docs/adr/0012-native-ledger-ingest.md`, `docs/work-orders/WO-PAPER-004-native-ledger.md`, `README.md`, `RUNBOOK.md`

## Builder tests

Parent-confirmed from detached worktree `/tmp/wo005-final` at `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`. Command `PYTHONPATH=src python3.X -m unittest discover -s tests -v`. Not an Architect run.

- Python 3.9.25: exit 0, stdout 0 bytes, wall 1.733s, stderr `Ran 132 tests in 1.412s` / OK.
- Python 3.12.3: exit 0, stdout 0 bytes, wall 1.436s, stderr `Ran 132 tests in 1.286s` / OK.

The 132 include the previously accepted 117. Builder 132/132 is not Architect acceptance.

## Exclusions

No merge. No acceptance of the private head by this note. No live native messaging. No dedicated writer principal. No host access-control list. No bot message. No host-principal change. No scheduler. No live order. No broker or account read. No vendor call. No new entry, exit, stop, or risk parameter. No trade-policy approval.

G0 stays OPEN. Provider rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. No fourth call. Stop-dependent M/T stays HOLD.

## Remaining limitations

This increment does not authenticate native senders and does not implement a host access-control list. The snapshot hash is a truncation check, not a signature. Another Bot of the same user can still open the ledger file. Increments B and C remain gated. Paper-bots main stays `ff13c49ce2535992c7216f5742946b33bd805e53` until an Architect decision and a later reviewed merge.

## Requested next step

Architect independent re-audit of exact private head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`, then ACCEPT or HOLD on that head. This note is the handoff. It is not the decision.

## Increment B — proposed successor, not a rewrite of Increment A

**Status:** PROPOSED for Architect ACCEPT or HOLD of exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386`. Not accepted. Not merged.  
**Authoritative packet:** [REVIEW-M5-INBOUND-001](../research/reviews/2026-11-06-wo-paper-005-simulated-inbound-packet.md)  
**Accepted Increment A:** [REVIEW-M5-ACCEPT-001](../research/reviews/2026-11-06-wo-paper-005-b87354-independent-acceptance.md), paper-bots main `ba001debca9e695fc3356c8720a17fa15836c31c`  
**Historical HOLD, unchanged:** [REVIEW-M5-INDEP-001](../research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) still HOLDs `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only  
**Private pull request:** [paper-bots #7](https://github.com/maff0000/paper-bots/pull/7)

The sections above are the Increment A record. They stay. The table that calls Increment B "parent-mediated live native messaging" and "not implemented" is that historical plan. This section is the successor under review. It does not turn Increment A into this increment, and it does not activate `parent_platform_metadata`.

### Parent-read private state

This public session could not open `maff0000/paper-bots`. The facts below are the parent's 6 Nov 2026 GitHub read-back.

| Item | Value |
|---|---|
| Private state | OPEN, draft false, `merged` false, `merged_at` null, `mergeable` true, `mergeable_state` clean |
| Branch | `cursor/wo-paper-005-increment-b-dc64` |
| Exact head | `124c0f2af9e7a60a783718516c20697f3dd3c386` |
| Single parent, PR base, and paper-bots `main` | `ba001debca9e695fc3356c8720a17fa15836c31c` |
| Paper-bots `main` message | `Merge WO-PAPER-005 Increment A offline transport (Architect accepted)` |
| Commits / diff | 1 commit, 13 files, +1114 / −16 |
| Prospective test-merge SHA | `8d835d4d2f2ead73ad278821c45e4dfc02924274` is **not** a merge |
| Public `origin/main` before this note | `f21de7e5bfaa48617c9d47b631f18ff53408ae2f` |
| Frozen QARP file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |

`paperbots.native_ingest`, the frozen QARP file, and the Increment A recovery machinery were not rewritten as a second ledger.

### What the simulation is

Parent-read behaviour, not an Architect confirmation. The adapter is `paperbots.native_inbound`. The record class is `simulated_inbound_handoff`. The envelope file is untrusted and cannot be the inbound record. The adapter hashes the envelope file bytes and does not read a sender out of the envelope object.

A valid record mints the existing Increment A sidecar and queues it on `native-transport-1`. Drain still calls `paperbots.native_ingest`. `synthetic_fixture` still drains. There is no second ledger.

The closed record schema requires `simulation` `OFFLINE`, `authenticates_sender` false, `host_acl` `NOT_ENFORCED`, and `live_message_sent` false. Unknown fields fail closed. `parent_platform_metadata` stays refused, both as a record class and as a sidecar source.

The presented sender id is copied into the existing sidecar field `attested_native_bot_id`. That copy is the id the record presented. It is not authenticated native provenance. Receipts, snapshots, explanations, CLI output, and `transport_limits()` keep `authenticates_sender` false. `transport_limits()` also sets `synthetic_provenance_is_authenticated_native_provenance` false and `simulated_inbound_handoff` to `OFFLINE_SIMULATION_NOT_AUTHENTICATION`.

Recovery still revalidates successful receipts, writes `RECOVERY_INTEGRITY` on mismatch, quarantines, and does not append. The new source is allowed through that recheck so a matching simulated receipt can archive. A mismatch still preserves the original receipt.

Private ADR 0014 amends the Increment B plan in ADR 0013. ADR 0013 stays the Increment A record and is not withdrawn.

### Acceptance criterion and parent findings

The parent checked this criterion: the simulation must never present synthetic provenance as authenticated native provenance, even if every test passes. The parent read the private inbound adapter, the transport patch, ADR 0014, the private work-order section, README and runbook pointers, fixtures, and inbound tests at exact `124c0f2a`. This session did not.

Parent-reported, and not an Architect run: the record builder cannot set `authenticates_sender` true. The parser refuses any other value for `authenticates_sender`, `host_acl`, `live_message_sent`, and `simulation`, and refuses record class `parent_platform_metadata`. Receipts, recovery records, and snapshots keep `authenticates_sender` false. The NEO reader still refuses a snapshot that claims authentication. Tests assert the flag stays false on the happy path, the synthetic-fixture path, a disagreeing presented sender, the same-user forge case, outage, quarantine, CLI stage, and limits. A further test rejects a claimed authentication, an enforced host access-control list, a live-message flag, a LIVE simulation, and `parent_platform_metadata`. The private tests assert that the source files do not contain a native send invocation or an HMAC import.

### HOLDs that stay HOLD

Sender authentication stays HOLD. A claimed bot name, role, producer field, shared secret, HMAC file, shared mailbox, in-process role check, or a file on this computer is not authentication. NEO isolation stays HOLD until an independently enforced security boundary exists. Live native messaging stays HOLD. No native message was sent. `parent_platform_metadata` stays refused. A later live message would not unlock that string, and a live-message authorisation would not by itself permit `authenticates_sender` true.

A same-user process can write a well-formed `simulated_inbound_handoff` for any allowlisted id, and Python will queue it. The private same-user forge test documents that limitation. That success is evidence for the HOLD, not evidence that a sender was authenticated. Increment B can be completed as this offline simulation. It cannot be securely completed as sender authentication, a host access-control list, or NEO isolation. Those require Increment C: a separate Cursor user, or another independently evidenced principal, whose computer alone can open the ledger and write attestation files.

### Private names

Names only. Contents are not copied.

- added `src/paperbots/native_inbound.py`
- modified `src/paperbots/native_transport.py` (+22 / −7)
- added `tests/test_native_inbound.py`
- added `fixtures/native/wo005_inbound/` (`envelope.json`, `handoff.json`, `index.json`)
- added `docs/adr/0014-offline-simulated-inbound.md`
- modified `docs/adr/0010-native-role-contract.md`, `docs/adr/0012-native-ledger-ingest.md`, `docs/adr/0013-offline-native-transport.md`
- modified `docs/work-orders/WO-PAPER-005-native-transport.md`, `README.md`, `RUNBOOK.md`

### Builder tests

The parent did not re-execute the suite. The builder reported, and the private PR body repeats, `PYTHONPATH=src python3.9 -m unittest discover -s tests -v` and the same command with `python3.12`. Python 3.9.25 and Python 3.12.3 each reported `Ran 152 tests` and `OK`, exit 0. The previous 136 Increment A tests are included. Builder 152/152 is not Architect acceptance. The Architect should run the suite at exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386`.

### Exclusions

No merge. No acceptance of the private head by this note. No live native message. No host-user change. No sender authentication. No host access-control list. No NEO isolation. No scheduler. No live order. No broker or account read. No vendor call. No new entry, exit, stop, or risk parameter.

G0 stays OPEN. Provider rights stay UNVERIFIED. FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. No fourth call. Stop-dependent M/T stays HOLD.

### Requested next step for Increment B

Architect independent review of exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386`, then ACCEPT or HOLD on that head. Acceptance of the offline simulation would not authenticate a sender and would not isolate NEO. This section is the handoff. It is not the decision.
