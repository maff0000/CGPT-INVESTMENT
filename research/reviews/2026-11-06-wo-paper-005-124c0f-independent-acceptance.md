# REVIEW-M5-INDEP-002 — WO-PAPER-005 Increment B independent exact-head ACCEPT

**Date:** 2026-11-06 (Europe/London)  
**Architect disposition:** **ACCEPT — offline simulated inbound handoff ONLY**.  
**Authority exclusions:** Not sender authentication, protected NEO host isolation, live native messaging, vendor/broker data, scheduling, stop-policy approval or trading.

## Exact-head record

| Item | SHA or result |
|---|---|
| Private implementation | [paper-bots PR #7](https://github.com/maff0000/paper-bots/pull/7) |
| **Independently accepted private head** | `124c0f2af9e7a60a783718516c20697f3dd3c386` |
| Private parent/base before merge | `ba001debca9e695fc3356c8720a17fa15836c31c` |
| **Private merge commit** | `b30d0ce048317e064a2eccbfd0589ac29799d626` (GitHub normal merge) |
| Public governance branch before this acceptance record | [CGPT-INVESTMENT PR #11](https://github.com/maff0000/CGPT-INVESTMENT/pull/11), `c07205af0e1997754455f41a8efcb704f1696243` |
| Public main before PR | `f21de7e5bfaa48617c9d47b631f18ff53408ae2f` |

The public acceptance record is committed to the open governance PR for independent read-back. Its own commit SHA is not embedded in its contents. Public PR #11 remains subject to a separate exact-head merge check.

## Independent methodology and observations

- Reconstructed 101 relevant source, test, fixture, schema and supporting files from the private exact HEAD. Checked all 101 local Git blob object IDs against their GitHub tree SHA: **101 matched**.
- Ran `PYTHONPATH=src python3 -m unittest discover -s tests -q` on **Python 3.12.14**: **Ran 152 tests; OK; exit 0**. The initial partial reconstruction lacked the repository schema catalogs and rights matrix, so its failures were a local audit-copy omission; restoring those exact published blobs yielded the green result.
- Inspected `paperbots.native_inbound` and its interaction with `paperbots.native_transport` and the previously accepted `paperbots.native_ingest` writer.
- Ran a separate Architect-authored offline probe (not the builder's tests) that independently rejected claims of `authenticates_sender=true`, `live_message_sent=true`, `record_class=parent_platform_metadata`, `host_acl=ENFORCED`, wrong envelope hash and malformed presented-sender object. Each rejection left ledger rows and hash tip unchanged.
- The independent probe staged a valid synthetic E envelope with `simulated_inbound_handoff`, observed one `accepted` receipt with `authenticates_sender=false` and `host_acl=NOT_ENFORCED`, and verified the exact-submission retry returns the durable original receipt without a second append or hash-tip change.
- The exported NEO snapshot kept `authenticates_sender=false`; its reader did not expose an append or ingest method.
- The suite includes six-bot E→S→R→M→T→NEO synthetic chain, refusal of orders, outages, conflict/recovery and provenance tests; all passed. Builder's earlier Python 3.9/3.12 figures are separate from the independent Python 3.12.14 run.

## Acceptance boundary

This increment implements an **OFFLINE SIMULATION** of handoff files (untrusted envelope and a separate simulated inbound record) into the existing spool and existing single event-ledger writer. A presented ID copied into `attested_native_bot_id` remains an **unverified claim**, not independent platform attestation. Same-user processes can claim any allowlisted bot identity. The simulated record is not minted by the envelope contents; `parent_platform_metadata` stays refused. The system explicitly records no sender authentication, no host ACL and no native message.

**Increment C must precede any claim of independent sender authentication or protected NEO isolation.** A real native message requires its own separately approved, named-principal bounded test, and would not by itself prove identity.

G0 **OPEN**. Provider data rights **UNVERIFIED**. FMP remains the same three historical calls, third HTTP 402; no fourth call was made. Stop-dependent M/T remains **HOLD**. Frozen QARP-ROTATION-001 v1.0.0 SHA256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` unchanged. No broker, vendor, account-data, scheduler, real bot messages or live orders authorised or made.

Historical [REVIEW-M5-ACCEPT-001](2026-11-06-wo-paper-005-b87354-independent-acceptance.md), [REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md), M4 exact-head ACCEPT and HOLD records remain intact and are not reopened by this decision.

## Next sequence

Prepare a separate Git-tracked, bounded **Increment C principal-boundary design/work order**: prove what OS/Cursor user owns the ledger and spool, who can mint attestation sidecars, and how NEO read-only permissions are enforced *against other same-user bots*. If the environment cannot furnish an independent security principal, document that limitation and keep platform authentication/NEO security on HOLD. Continue independently reviewed offline development only; no live bot message or host-user modification without explicit authority.
