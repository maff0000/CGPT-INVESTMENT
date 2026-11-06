# ADR-APP-001 — recorded Grok Bot platform findings
**Date:** 2026-11-05 (Europe/London)
**Status:** RECORDED FACTS. Not an architecture approval. Not a claim that the six roles are provisioned or that a hard access-control list exists. **Current proposal, 2026-11-06:** the WO-PAPER-005 recovery-integrity correction is open on private paper-bots PR #6, head `b87354d77dc4d94273291ae571c3837924f22fdd`, and is not accepted. [REVIEW-M5-INDEP-001](../../research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) HOLDs `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only. The correction does not authenticate native senders and does not implement a host access-control list. **Accepted history:** WO-PAPER-004 offline in-process adapter, paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`, [REVIEW-M4-ACCEPT-001](../../research/reviews/2026-11-06-wo-paper-004-541f3f-independent-acceptance.md). The host isolation gap remains open. Older sentences in this file that call the in-process adapter proposed or unmerged are historical for the heads they name.
**Evidence:** owner milestone brief. This session did not invoke agent creation, did not send a handoff, and did not inspect the app.

## Findings
- Creating an agent creates an individual messageable agent.
- Sending work to an agent is an asynchronous priority handoff.
- The current T-Bot identifier `81d8cf38-188e-4592-b08d-b59d6e461e83` is reused and is not modified by this record.
- Parent-reported created identifiers, not inspected by this session: E-Bot `53f42f0b-4b9e-429f-9317-6e7edf2d8e26`, S-Bot `5cddba3b-38ff-49c8-8e9b-37b63efebe3c`, R-Bot `76efa575-82b5-44c0-a0df-5647c78b0083`, M-Bot `59ccea20-1754-437f-8fa9-424ff18e5221`, NEO `e1e372c8-20e9-45a6-856f-4eabdf018308`. Handoff verification is pending.
- The text supplied when an agent is created shapes its instructions. That text is not proven to be a hard tool access-control list.
- Agents on the same box share a filesystem.
- No automatic attachment of the private Python package, and no production ledger write bridge, has been verified.
- NEO is logically read-only. A persona statement does not enforce that limit. Hard capability enforcement has to be tested.

## Official platform limit — read 2026-11-05
This session read the four public pages below. It ran no probes.

| Source | What it supports |
|---|---|
| [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) | Isolation is per user. Within one user, all of that user's bots share one computer. A login or file on that computer is available to every bot that user runs. A permitted connector is available to every bot that member runs |
| [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) | Bot-to-bot messages are visible asynchronous handoffs. There is no switch that disables bot-to-bot messaging. Instructions govern it |
| [Create and manage Bots](https://docs.x.ai/grok-bot/bots) | Each bot has its own name, conversation and memory. Bots have separate roles and conversations, and they share the computer. Files and sign-ins on that computer are not isolated per bot |
| [Security](https://cursor.com/docs/grok-bot/security) | Source-system permissions, per-action approvals, team connector policy, and Enterprise network and Auto-review controls complement least privilege. They sit beside per-user isolation |

Created identities and instructional refusals are therefore not a hard capability access-control list and not a read-only NEO. An authenticated binding from a bot identity to the private Python package is **UNVERIFIED**. A JSON producer identifier is a claim until that binding exists. No installed Python ledger execution is verified. The parent has the agent-creation tool. This executor did not use it. That is not a report that the tool is unavailable.

## Official platform limit — re-read 2026-11-06

This public session re-read the six pages below on 6 Nov 2026. No probe was sent. The 5 November table above stays the record of that earlier read.

| Source | What the re-read supports |
|---|---|
| [Security FAQ](https://docs.x.ai/grok-bot/security-faq) | Isolation is per Cursor user. Bots of one user share one computer. A Bot has no identity of its own. A separate computer and credential set means a separate Cursor user |
| [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) | Files, sign-ins, and command-line credentials are shared. Screens are separate work surfaces and are not security boundaries. The computer is assigned to the user, not to a Bot |
| [Security](https://cursor.com/docs/grok-bot/security) | A Bot has no identity or credentials of its own and acts as the signed-in member |
| [Create and manage Bots](https://docs.x.ai/grok-bot/bots) | Separate names, conversations, and memory still share the computer. Files and sign-ins are not isolated per Bot |
| [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) | There is no switch that disables bot-to-bot messaging |
| [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) | One user's Bots share one computer, files, logins, and permitted connectors |

## Supported later adapter — not implemented
The documented minimal path, not a workaround and not started here, is offline validation of typed JSON, frozen strategy and role-transition checks, one central transactional writer, and a separate immutable hash snapshot plus audit result for NEO. A shared operating system makes an interface-level read-only flag not a security boundary. Strong NEO isolation needs a separate security principal, runtime and service with its own protected boundary. That boundary is not implemented. This record does not provision it.

## Follow-on — 2026-11-06, recovery-integrity correction proposed, HOLD of `d57f2e32` stands

Private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) now proposes head `b87354d77dc4d94273291ae571c3837924f22fdd`. Its parent is the held head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1`. The public handoff is [REVIEW-M5-TRANSPORT-002](../../research/reviews/2026-11-06-wo-paper-005-recovery-integrity-packet.md), pinned to the head of `cursor/wo-paper-005-transport-packet-f3e8`. [REVIEW-M5-INDEP-001](../../research/reviews/2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains the HOLD of that older exact head. A terminal successful receipt no longer authorises archive by itself. Recovery rechecks the staged envelope and attestation against the durable receipt. A mismatch, a missing sidecar, or a corrupt sidecar preserves the original receipt, quarantines the mismatching evidence, and writes a separate recovery record with `kind` `RECOVERY_INTEGRITY`, without another ledger append. Quarantine is retention, not a host access-control list. This follow-on does not accept the new private head. It does not authenticate native senders and does not implement a host access-control list. Builder 136/136 is not Architect acceptance. Increments B and C remain gated.

## Historical proposal — 2026-11-06, WO-PAPER-005 Increment A at `d57f2e32`, later held

Private [paper-bots PR #6](https://github.com/maff0000/paper-bots/pull/6) proposes head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` on unchanged paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`. The public handoff is [REVIEW-M5-TRANSPORT-001](../../research/reviews/2026-11-06-wo-paper-005-offline-transport-packet.md), pinned to the head of `cursor/wo-paper-005-transport-packet-f3e8`. Increment A is an offline spool in front of the accepted in-process writer: an untrusted envelope plus a separate attestation sidecar. Only `synthetic_fixture` is accepted. `parent_platform_metadata` is named and refused. Missing, mismatched, or non-allowlisted attestation is fail-closed. The NEO snapshot reader has no write method. Its hash detects truncation and is not a signature. It does not stop another same-user Bot from opening the ledger file. A shared mailbox, an HMAC file, or an in-process role check is rejected as theatre. Increment B (parent-mediated live native messaging) and Increment C (a dedicated writer/NEO principal; the documented path is a separate Cursor user) are gated and are not implemented. No bot message was sent. No host principal was changed. This follow-on does not accept the private head. It does not authenticate native senders and does not implement a host access-control list. Builder 132/132 is not Architect acceptance.

The in-process adapter named in the sections below was later accepted, for that offline path only, by REVIEW-M4-ACCEPT-001 at paper-bots main `ff13c49ce2535992c7216f5742946b33bd805e53`. Those older follow-ons remain the historical proposals of the heads they name.

## Historical follow-on — 2026-11-06, named adapter proposed, isolation gap open
The adapter named in the Supported later adapter section was proposed on private [paper-bots PR #5](https://github.com/maff0000/paper-bots/pull/5), head `553ec517455ce6ef797b049e65ec61389daa20da`, as `paperbots.native_ingest` (`native-ledger-1`). `native-probe-1` still does not write. The proposal is open and unmerged. The public handoff is [REVIEW-M4-NATIVE-001](../../research/reviews/2026-11-06-wo-paper-004-native-ledger-packet.md). The separate operating-system principal that alone can open the ledger was proposed and was not built. One user's bots still share the computer, files, logins, and permitted connectors. A JSON producer field does not authenticate the sender. This follow-on does not close the host isolation gap.

## Historical follow-on — 2026-11-06, replay correction proposed, HOLD of the prior head stands
The same private PR #5 now proposes head `f4371c599fb1c45e28c403549090e92fd825ce67` after a bounded replay-integrity correction. The public handoff is [REVIEW-M4-REPLAY-001](../../research/reviews/2026-11-06-wo-paper-004-replay-correction-packet.md). [REVIEW-M4-INDEP-001](../../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. The correction is open and unmerged. It does not add a host ACL or authenticate a native sender. That head was later held by [REVIEW-M4-INDEP-002](../../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md).

## Historical follow-on — 2026-11-06, quality-claim guard proposed, both prior HOLDs stand
The same private PR #5 now proposes head `541f3f175da8ec684f942dea767a1352cf5df0fb`. The public handoff is [REVIEW-M4-VALID-001](../../research/reviews/2026-11-06-wo-paper-004-quality-validation-packet.md), pinned to the head of `cursor/wo-paper-004-public-governance-9fb6`. [REVIEW-M4-INDEP-002](../../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. [REVIEW-M4-INDEP-001](../../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. A non-string quality claim is proposed to be a `ValidationError` before the allowlist test. This follow-on does not add a host ACL or authenticate a native sender.

## Consequence
Five teammates are parent-reported created, and T-Bot is reused. Handoff replies are still pending. The ledger bridge stays unverified. This cloud session does not provision agents or new infrastructure. The parent does the native creation. Later acceptance of the offline in-process adapter does not verify native transport. The recovery-integrity correction is the current proposal. The `d57f2e32` follow-on remains the historical request later held by REVIEW-M5-INDEP-001. Neither authenticates native senders or implements a host access-control list.
