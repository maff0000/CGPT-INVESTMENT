# ADR-APP-001 — recorded Grok Bot platform findings
**Date:** 2026-11-05 (Europe/London)
**Status:** RECORDED FACTS. Not an architecture approval. Not a claim that the six roles are provisioned or that a hard access-control list exists. **Follow-on 2026-11-06:** the adapter named below is proposed on private paper-bots PR #5 and is not accepted. The host isolation gap remains open.
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

## Supported later adapter — not implemented
The documented minimal path, not a workaround and not started here, is offline validation of typed JSON, frozen strategy and role-transition checks, one central transactional writer, and a separate immutable hash snapshot plus audit result for NEO. A shared operating system makes an interface-level read-only flag not a security boundary. Strong NEO isolation needs a separate security principal, runtime and service with its own protected boundary. That boundary is not implemented. This record does not provision it.

## Follow-on — 2026-11-06, named adapter proposed, isolation gap open
The adapter named in the paragraph above is now proposed on private [paper-bots PR #5](https://github.com/maff0000/paper-bots/pull/5), head `553ec517455ce6ef797b049e65ec61389daa20da`, as `paperbots.native_ingest` (`native-ledger-1`). `native-probe-1` still does not write. The proposal is open and unmerged. The public handoff is [REVIEW-M4-NATIVE-001](../../research/reviews/2026-11-06-wo-paper-004-native-ledger-packet.md). The separate operating-system principal that alone can open the ledger was proposed and was not built. One user's bots still share the computer, files, logins, and permitted connectors. A JSON producer field does not authenticate the sender. This follow-on does not close the host isolation gap.

## Follow-on — 2026-11-06, replay correction proposed, HOLD of the prior head stands
The same private PR #5 now proposes head `f4371c599fb1c45e28c403549090e92fd825ce67` after a bounded replay-integrity correction. The public handoff is [REVIEW-M4-REPLAY-001](../../research/reviews/2026-11-06-wo-paper-004-replay-correction-packet.md). [REVIEW-M4-INDEP-001](../../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. The correction is open and unmerged. It does not add a host ACL or authenticate a native sender. That head was later held by [REVIEW-M4-INDEP-002](../../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md).

## Follow-on — 2026-11-06, quality-claim guard proposed, both prior HOLDs stand
The same private PR #5 now proposes head `541f3f175da8ec684f942dea767a1352cf5df0fb`. The public handoff is [REVIEW-M4-VALID-001](../../research/reviews/2026-11-06-wo-paper-004-quality-validation-packet.md), pinned to the head of `cursor/wo-paper-004-public-governance-9fb6`. [REVIEW-M4-INDEP-002](../../research/reviews/2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. [REVIEW-M4-INDEP-001](../../research/reviews/2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. A non-string quality claim is proposed to be a `ValidationError` before the allowlist test. This follow-on does not add a host ACL or authenticate a native sender.

## Consequence
Five teammates are parent-reported created, and T-Bot is reused. Handoff replies are still pending. The ledger bridge stays unverified. This cloud session does not provision agents or new infrastructure. The parent does the native creation.
