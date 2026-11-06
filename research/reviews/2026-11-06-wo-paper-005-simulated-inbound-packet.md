# WO-PAPER-005 — offline simulated inbound, Increment B

**ID:** REVIEW-M5-INBOUND-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for an open private increment.  
**Disposition requested:** Architect **ACCEPT or HOLD** of exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386` after independent review.  
**This packet does not accept that head.** It does not merge private [paper-bots PR #7](https://github.com/maff0000/paper-bots/pull/7) or this public pull request. Builder **152/152 is not Architect acceptance**. The parent did not re-execute the unittest suite. This public session did not run it. Increment B does not authenticate a sender. Synthetic provenance is not authenticated native provenance.

Accepted Increment A stays accepted. [REVIEW-M5-ACCEPT-001](2026-11-06-wo-paper-005-b87354-independent-acceptance.md) records the independent acceptance of private paper-bots PR #6 exact head `b87354d77dc4d94273291ae571c3837924f22fdd` and the normal merge to paper-bots main `ba001debca9e695fc3356c8720a17fa15836c31c`. That acceptance is the offline synthetic spool only. It does not authenticate native senders, implement a host access-control list, isolate NEO, or authorise a live bot message. [REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains the HOLD of exact older head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only. [REVIEW-M5-TRANSPORT-001](2026-11-06-wo-paper-005-offline-transport-packet.md) and [REVIEW-M5-TRANSPORT-002](2026-11-06-wo-paper-005-recovery-integrity-packet.md) stay the historical Increment A requests and are not edited here.

[REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains the acceptance of the offline in-process adapter, paper-bots main at that time `ff13c49ce2535992c7216f5742946b33bd805e53`. [REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Those HOLDs are valid only for those older exact heads. None of those files is edited here. Merged public [PR #10](https://github.com/maff0000/CGPT-INVESTMENT/pull/10) is closed history and is not reused.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-005-inbound-packet-ff96` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `git fetch origin main` returned `f21de7e5bfaa48617c9d47b631f18ff53408ae2f`, message `Merge PR #10 — WO-PAPER-005 Increment A exact-head Architect acceptance`, parents `1fc4491a095d914b855a2653cb8b753c7fbc3f13` and `936f4ab8e068365c5b448d5a5a9c2ea4678beb92`. That SHA is the parent of this public commit. `gh pr view 7 --repo maff0000/paper-bots` returned `Could not resolve to a Repository`. This session did not read private blobs |
| Parent-supplied private read-back, 6 Nov 2026 | Private PR #7 state, exact head, parent, base, branch, diff size, named paths, Increment B behaviour, the parent's reading of the private implementation, and the builder test report repeated in the private PR body. The parent reviewed the private head. This public session did not |
| Not claimed here | Architect acceptance of `124c0f2a`, a merge, a re-run of the 152 tests, authenticated native provenance, sender authentication, a host access-control list, NEO isolation, a live bot message, a changed host principal, vendor rights, or a fourth FMP call |

This public session did not copy private source, tests, fixtures, ledger rows, credentials, or implementation patches. Private facts below are the parent read-back. Naming a private path or SHA is not a copy of its contents.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main` before this write, and parent of this public commit | `f21de7e5bfaa48617c9d47b631f18ff53408ae2f` |
| Parents of that public main | `1fc4491a095d914b855a2653cb8b753c7fbc3f13`, `936f4ab8e068365c5b448d5a5a9c2ea4678beb92` |
| Private pull request | [paper-bots #7](https://github.com/maff0000/paper-bots/pull/7) |
| Private title | WO-PAPER-005 Increment B: offline simulated inbound handoff |
| Private branch | `cursor/wo-paper-005-increment-b-dc64` |
| Private head under review | `124c0f2af9e7a60a783718516c20697f3dd3c386` |
| Single parent of that commit, PR base, and paper-bots `main` | `ba001debca9e695fc3356c8720a17fa15836c31c` |
| Paper-bots `main` message, parent-read | `Merge WO-PAPER-005 Increment A offline transport (Architect accepted)` |
| Private state | OPEN, draft false, `merged` false, `merged_at` null, `mergeable` true, `mergeable_state` clean |
| Commits on the private PR | 1 |
| Diff versus accepted paper-bots main | 13 files, +1114 / −16 |
| GitHub `merge_commit_sha` | `8d835d4d2f2ead73ad278821c45e4dfc02924274` is a prospective test-merge SHA. It is not a merge |
| Public branch for this packet | `cursor/wo-paper-005-inbound-packet-ff96` |
| Public note | [WO-PAPER-005](../../work-orders/WO-PAPER-005-native-transport.md) |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |

## What Increment B is

Parent-read behaviour, not an Architect confirmation. Increment B is an offline simulation of how native-shaped bot output can reach the accepted Increment A spool and `paperbots.native_ingest`.

The adapter is `paperbots.native_inbound`. The record class is `simulated_inbound_handoff`. The envelope file is untrusted and cannot be the inbound record. The adapter hashes the envelope file bytes and does not read a sender out of the envelope object.

A valid record mints the existing Increment A sidecar and queues it on `native-transport-1`. Drain still calls `paperbots.native_ingest`. `synthetic_fixture` still drains. There is no second ledger. `paperbots.native_ingest`, the frozen QARP file, and the Increment A recovery machinery were not rewritten as a second ledger.

The closed record schema requires `simulation` `OFFLINE`, `authenticates_sender` false, `host_acl` `NOT_ENFORCED`, and `live_message_sent` false. Unknown fields fail closed. `parent_platform_metadata` stays refused, both as a record class and as a sidecar source.

The presented sender id is copied into the existing sidecar field `attested_native_bot_id`. That copy is the id the record presented. It is not authenticated native provenance.

Receipts, snapshots, explanations, CLI output, and `transport_limits()` keep `authenticates_sender` false. `transport_limits()` also sets `synthetic_provenance_is_authenticated_native_provenance` false and `simulated_inbound_handoff` to `OFFLINE_SIMULATION_NOT_AUTHENTICATION`.

Recovery still revalidates successful receipts, writes `RECOVERY_INTEGRITY` on mismatch, quarantines, and does not append. The new source is allowed through that recheck so a matching simulated receipt can archive. A mismatch still preserves the original receipt.

Private ADR 0014 amends the Increment B plan in private ADR 0013. ADR 0013 stays the Increment A record and is not withdrawn. The earlier public description of Increment B as parent-mediated live native messaging remains the historical plan in REVIEW-M5-TRANSPORT-001. This successor is the offline simulation. It is not that live message.

## Architect acceptance criterion the parent checked

The parent recorded this criterion: “The simulation must never present synthetic provenance as authenticated native provenance, even if every test passes.”

The parent reviewed the private inbound adapter, the transport patch, ADR 0014, the work-order Increment B section, the private README and runbook pointers, the fixtures, and the inbound tests at exact `124c0f2af9e7a60a783718516c20697f3dd3c386`. This public session did not. Parent-reported findings:

- The record builder cannot set `authenticates_sender` true.
- The parser refuses `authenticates_sender` other than false, `host_acl` other than `NOT_ENFORCED`, `live_message_sent` other than false, `simulation` other than `OFFLINE`, and record class `parent_platform_metadata`.
- Receipts and recovery records hard-code `authenticates_sender` false. Snapshots keep it false. The NEO reader still refuses a snapshot that claims authentication.
- Tests assert the flag stays false on the happy path, the synthetic-fixture path, a disagreeing presented sender, the same-user forge case, outage, quarantine, CLI stage, and limits.
- One test rejects a record that claims authentication, an enforced host access-control list, a live-message flag, a LIVE simulation, or `parent_platform_metadata`.
- The private tests assert that the source files do not contain a native send invocation or an HMAC import.

Those findings are the parent's reading. They are not this session's execution, and they are not Architect acceptance.

## HOLDs that stay HOLD

- `parent_platform_metadata` as proof of identity. It stays refused. A later live message does not unlock that string. It stays refused until a documented Python-verifiable sender signature exists.
- Sender authentication. A claimed bot name, role, producer field, shared secret, HMAC file, shared mailbox, in-process role check, or a file on this computer is not authentication.
- NEO isolation, until an independently enforced security boundary exists. The snapshot reader remains API isolation.
- Live native messaging. No native message was sent. A live message needs a separate written authorisation naming the sending principal, the receiving principal, and the exact handoff. That authorisation is not this work order, and it would not by itself permit `authenticates_sender` true or `parent_platform_metadata`.

Independent sender authentication and independently enforced NEO isolation cannot be securely completed on this shared computer. The parent re-read the official docs on 6 Nov 2026 and sent no probe. This public session did not repeat that read and sent no probe. The pages already recorded in [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md) say isolation is per Cursor user; bots of one user share one computer; a Bot has no identity or credentials of its own; screens are not security boundaries; there is no switch that disables bot-to-bot messaging.

A same-user process can write a well-formed `simulated_inbound_handoff` record for any allowlisted id, and Python will queue it. The private test of a same-user forge of another allowlisted id documents that limitation. That success is evidence for the HOLD, not evidence that a sender was authenticated.

Increment B can be completed as this offline simulation. It cannot be securely completed as sender authentication, a host access-control list, or NEO isolation. Those require Increment C.

## Revised sequence

1. Review private PR #7 as an offline simulation only. Acceptance would not authenticate a sender and would not isolate NEO.
2. Do not treat a later live message as the step that unlocks `parent_platform_metadata`. That string stays refused until a documented Python-verifiable sender signature exists.
3. Increment C comes first for independent sender authentication and for NEO isolation: a separate Cursor user, or another independently evidenced principal, whose computer alone can open the ledger and write attestation files.
4. A live native message, if wanted later, needs a separate written authorisation naming the sending principal, the receiving principal, and the exact handoff. That authorisation is not this work order.

## Private names

Names only. Contents are not copied. The parent-supplied diff is 13 files, +1114 / −16.

- added `src/paperbots/native_inbound.py`
- modified `src/paperbots/native_transport.py` (+22 / −7)
- added `tests/test_native_inbound.py`
- added `fixtures/native/wo005_inbound/` (`envelope.json`, `handoff.json`, `index.json`)
- added `docs/adr/0014-offline-simulated-inbound.md`
- modified `docs/adr/0010-native-role-contract.md`
- modified `docs/adr/0012-native-ledger-ingest.md`
- modified `docs/adr/0013-offline-native-transport.md`
- modified `docs/work-orders/WO-PAPER-005-native-transport.md`
- modified `README.md`
- modified `RUNBOOK.md`

## Tests

Parent-supplied builder report, repeated in the private PR body. The parent did not re-execute the suite on a local checkout. This public session did not run it. Command, as reported:

```bash
PYTHONPATH=src python3.9 -m unittest discover -s tests -v
PYTHONPATH=src python3.12 -m unittest discover -s tests -v
```

Python 3.9.25 and Python 3.12.3 each reported `Ran 152 tests` and `OK`, exit 0. The previous 136 Increment A tests are included in that count. **Builder 152/152 is not Architect acceptance.** The Architect should run the suite at exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386`.

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, broker or account read, vendor call, or trade-policy approval is granted.
- No bot message was sent. No host principal was changed.
- `authenticates_sender` stays false on receipts, snapshots, explanations, CLI output, and transport limits.
- Synthetic provenance is not authenticated native provenance.

## Sanitisation

This repository is public. This packet names private paths and SHAs. It does not copy private Python, tests, fixtures, ledger rows, credentials, or implementation patches. It does not invent bot secrets. It does not include live native message contents. None were sent.

## Limitations

- Increment B is an offline simulation into the accepted Increment A spool.
- It does not authenticate a sender and does not implement a host access-control list.
- A presented id copied into `attested_native_bot_id` is the id the record presented.
- The NEO snapshot reader remains API isolation. It is not an independently enforced security boundary.
- Same-user forgery of an allowlisted id can still be queued. That is evidence for the HOLD.
- Increment C is not this pull request.
- No native message was sent. No host user was changed.
- Paper-bots main stays `ba001debca9e695fc3356c8720a17fa15836c31c`. Private PR #7 is open.

## Restrictions

This packet authorises none of the following:

- acceptance of `124c0f2af9e7a60a783718516c20697f3dd3c386`
- merge of private PR #7 or of this public pull request
- `authenticates_sender` true, or presentation of synthetic provenance as authenticated native provenance
- `parent_platform_metadata` as proof of identity
- sender authentication, a host access-control list, or NEO isolation
- a live native message, or a change to host users, credentials, or permissions
- live orders, broker writes, or account reads
- vendor calls
- a scheduler or activation
- new entry, exit, stop, or risk parameters
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect review of exact private head `124c0f2af9e7a60a783718516c20697f3dd3c386`, including an independent run of the suite at that head, then an **ACCEPT** or **HOLD** recorded against that SHA. Acceptance of the offline simulation would not authenticate a sender and would not isolate NEO. Until that independent review exists, Increment B stays proposed. Passing builder tests, an open private pull request, and this public packet are review inputs. They are not the decision.

Rollback of an unaccepted increment is to leave paper-bots main at `ba001debca9e695fc3356c8720a17fa15836c31c` and public main at `f21de7e5bfaa48617c9d47b631f18ff53408ae2f` until a later reviewed merge. This file does not perform either merge.
