# REVIEW-M5-INDEP-003 — WO-PAPER-005 Increment C security-boundary DESIGN acceptance

**Date:** 2026-11-06 (Europe/London)  
**Architect decision:** **ACCEPT — documentation-only threat model, boundary design and security test plan.**  
**Not accepted:** any implemented host security boundary, native sender authentication, independently protected NEO, platform-signed handoff, live messaging, vendor/broker calls, scheduling or trading authority.

## Exact-head records

| Item | SHA / outcome |
|---|---|
| Private PR | [paper-bots #8](https://github.com/maff0000/paper-bots/pull/8) |
| Accepted private head | `cf2dd5ae752a85a645d510b38e4b2e800f1dc146` |
| Private base / parent | `b30d0ce048317e064a2eccbfd0589ac29799d626` |
| **Private merge commit** | `c0b9f540c09caec08fb87e77bf445d0e580f843e` (normal GitHub merge) |
| Public governance PR | [CGPT-INVESTMENT #12](https://github.com/maff0000/CGPT-INVESTMENT/pull/12) |
| Submitted public head | `0d4ddbf1d1a6f07c4c40fd27def0a8b84afdd92b` (later corrections and acceptance record on same branch) |
| Public base / main before merge | `a962ba0019c6c4a19478dcf0e356ba58b07d61ff` |
| Builder regression evidence | Python 3.12.3 `Ran 152 tests`, `OK`; builder evidence only |
| Architect code regression | Not rerun for documentation-only increment; source/test/fixture/schema Git objects identical to accepted Increment B |

## Independent Architect review

- Verified exact PR heads and bases from GitHub, and the changed-file patch list.
- Independently compared recursive Git trees of private base and exact head. **Only nine documentation paths changed** (`README.md`, `RUNBOOK.md`, ADRs 0010/0012/0013/0014, new ADR 0015, new Increment C security test plan, and WO-PAPER-005). **All `src/`, `tests/`, `fixtures/`, `examples/`, and `docs/schemas/` Git blob hashes are unchanged.**
- Read [private ADR 0015](https://github.com/maff0000/paper-bots/blob/cf2dd5ae752a85a645d510b38e4b2e800f1dc146/docs/adr/0015-security-boundary-design.md), [security test plan](https://github.com/maff0000/paper-bots/blob/cf2dd5ae752a85a645d510b38e4b2e800f1dc146/docs/security/2026-11-06-increment-c-security-test-plan.md), work-order successor and pointer changes. Findings: proposed principal remains absent, both security HOLDs are preserved, and no code path is represented as already enforcing a host ACL.
- Cross-checked primary platform documentation: [Grok Bot security FAQ](https://docs.x.ai/grok-bot/security-faq) states a computer is assigned per Cursor user, and same-user Bots share it; it recommends a separate Cursor user for workloads that need their own computer and credential set. [Inference Hooks](https://docs.x.ai/grok-bot/inference-hooks) signs model-input prompt frames to a security server; this does not authenticate the author of a ledger envelope.
- Corrected a nonblocking citation-row attribution in public REVIEW-M5-BOUNDARY-001: the separate-user recommendation belongs to the security FAQ rather than the Create-and-manage-Bots page.

## Security conclusions accepted as DESIGN, not deployment

1. Same-user Bots can access the same computer's files and connections; no independently enforceable writer or NEO file boundary exists today.
2. A **separate Cursor user** is a documented candidate for **file isolation**; creating it requires Matt's explicit infrastructure approval. That step **does not establish native Bot sender identity**. `authenticates_sender` remains false and `parent_platform_metadata` remains refused.
3. A separate source ledger user does not make exported NEO evidence authentic. A content SHA-256 stored beside the snapshot can be recomputed by a same-user adversary. Independent export verification would require a verifier whose minting secret/private key is inaccessible to readers, under a separately approved design and work order.
4. The platform documentation reviewed provides **no Python-verifiable Bot sender signature** for the live handoff. A delivery acknowledgement and the Enterprise Inference Hooks HMAC are not such a signature. Native sender authentication stays HOLD.
5. Shared Bots, in-process checks, same-user HMAC files, OS chmod flags on the shared Bot computer, and a second ledger are not accepted substitutes.
6. Future operational tests must be blocked pending the specific approved principal, credentials, transfer, reader boundary and signed-export design. No synthetic green test may be called a host ACL or authentication result.

## Explicit retained gates

G0 **OPEN**; provider rights **UNVERIFIED**; FMP remains the same three historical calls (third HTTP 402), **no fourth call**; stop-dependent M/T **HOLD**; QARP frozen manifest SHA256 `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` unchanged. No live native message, Cursor/OS account creation, user migration, Vault/credentials/permissions change, scheduler, broker/vendor/account data, new strategy risk parameter, order or fill.

Historic [REVIEW-M5-INDEP-002](2026-11-06-wo-paper-005-124c0f-independent-acceptance.md), [REVIEW-M5-ACCEPT-001](2026-11-06-wo-paper-005-b87354-independent-acceptance.md), [REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md), and previous M4 records are preserved without alteration.

## Next decision — Product Owner required

To actually deploy an isolated writer or NEO, submit a distinct bounded infrastructure Work Order identifying principals, message handoff and evidence transfer topology, key custody, cost, reversibility, and negative access tests. **Do not execute that work order** until Matt specifically approves creation/migration of users and relevant host changes. The separate sender-authentication requirement may remain HOLD even after file isolation. Live native messages require separate named-principal authorisation and do not, alone, prove sender identity.
