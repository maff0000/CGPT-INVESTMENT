# ADR-APP-001 — recorded Grok Bot platform findings
**Date:** 2026-11-05 (Europe/London)
**Status:** RECORDED FACTS. Not an architecture approval. Not a claim that the six roles are provisioned or that a hard access-control list exists.
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

## Consequence
Five teammates are parent-reported created, and T-Bot is reused. Handoff replies are still pending. The ledger bridge stays unverified. This cloud session does not provision agents or new infrastructure. The parent does the native creation.
