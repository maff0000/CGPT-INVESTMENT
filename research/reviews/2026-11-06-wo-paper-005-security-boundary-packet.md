# WO-PAPER-005 — Increment C security-boundary design

**ID:** REVIEW-M5-BOUNDARY-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for an open private design.  
**Disposition requested:** Architect **ACCEPT or HOLD** of exact private head `cf2dd5ae752a85a645d510b38e4b2e800f1dc146` after independent review of the published design.  
**This packet does not accept that head.** It does not merge private [paper-bots PR #8](https://github.com/maff0000/paper-bots/pull/8) or this public pull request. It does not create a Cursor user, an OS account, a shared Bot, a credential, or a permission. It does not send a message. Builder-reported `Ran 152 tests` is a regression of the unchanged Increment B suite. It is not a new Increment C count, and it is not Architect acceptance. The parent did not re-execute the suite. This public session did not run it.

Accepted Increment B stays accepted. [REVIEW-M5-INDEP-002](2026-11-06-wo-paper-005-124c0f-independent-acceptance.md) records the independent acceptance of private paper-bots PR #7 exact head `124c0f2af9e7a60a783718516c20697f3dd3c386` and the ordinary merge to paper-bots main `b30d0ce048317e064a2eccbfd0589ac29799d626`. That acceptance is the offline `simulated_inbound_handoff` path into the accepted spool. Presented native ID is not authenticated. Accepted Increment A stays accepted. [REVIEW-M5-ACCEPT-001](2026-11-06-wo-paper-005-b87354-independent-acceptance.md) records the independent acceptance of private paper-bots PR #6 exact head `b87354d77dc4d94273291ae571c3837924f22fdd` and the ordinary merge to paper-bots main `ba001debca9e695fc3356c8720a17fa15836c31c`. That acceptance is the offline synthetic spool only. [REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains the HOLD of exact older head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only. [REVIEW-M5-TRANSPORT-001](2026-11-06-wo-paper-005-offline-transport-packet.md), [REVIEW-M5-TRANSPORT-002](2026-11-06-wo-paper-005-recovery-integrity-packet.md), and [REVIEW-M5-INBOUND-001](2026-11-06-wo-paper-005-simulated-inbound-packet.md) stay the historical Increment A and Increment B requests and are not edited here.

[REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains the acceptance of the offline in-process adapter. [REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Those HOLDs are valid only for those older exact heads. None of those files is edited here. Merged public [PR #11](https://github.com/maff0000/CGPT-INVESTMENT/pull/11) is closed history and is not reused.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-005-security-boundary-packet-e603` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `git fetch origin main` returned `a962ba0019c6c4a19478dcf0e356ba58b07d61ff`, message `Merge PR #11 — WO-PAPER-005 Increment B offline inbound acceptance`, parents `f21de7e5bfaa48617c9d47b631f18ff53408ae2f` and `88d78226dc151c92ab249634ef30757fd0b55d36`. That SHA is the parent of this public commit. `gh pr view 8 --repo maff0000/paper-bots` returned `Could not resolve to a Repository`. This session did not read private blobs and did not re-read the platform pages |
| Parent-supplied private read-back, 6 Nov 2026 | Private PR #8 state, exact head, parent, base, branch, author and creation times, diff size, named paths, the parent's reading of private ADR 0015 and the private security-test plan, the builder regression report, and the parent's same-day inspection of the live handoff descriptor. The parent reviewed the published documents. This public session did not |
| Not claimed here | Architect acceptance of `cf2dd5ae`, a merge, a re-run of the 152 tests, a new Increment C test count, sender authentication, a host access-control list, an implemented principal, NEO isolation, a live bot message, a new Cursor user or OS account, a shared Bot, a deployed credential, vendor rights, or a fourth FMP call |

This public session did not copy private source, tests, fixtures, ledger rows, credentials, or design prose beyond the parent paraphrase recorded below. Private facts below are the parent read-back. Naming a private path or SHA is not a copy of its contents.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main` before this write, and parent of this public commit | `a962ba0019c6c4a19478dcf0e356ba58b07d61ff` |
| Public main message | `Merge PR #11 — WO-PAPER-005 Increment B offline inbound acceptance` |
| Parents of that public main | `f21de7e5bfaa48617c9d47b631f18ff53408ae2f`, `88d78226dc151c92ab249634ef30757fd0b55d36` |
| Private pull request | [paper-bots #8](https://github.com/maff0000/paper-bots/pull/8) |
| Private title | WO-PAPER-005 Increment C: security-boundary design (proposed, not accepted) |
| Private branch | `cursor/wo-paper-005-increment-c-security-boundary-5bb9` |
| Private head under review | `cf2dd5ae752a85a645d510b38e4b2e800f1dc146` |
| Single parent of that commit, PR base, and paper-bots `main` at open | `b30d0ce048317e064a2eccbfd0589ac29799d626` |
| Private state | OPEN, draft false, `merged` false, `merged_at` null |
| Commits on the private PR | 1. Author date `2026-11-06T12:39:06Z`. PR created `2026-11-06T12:39:27Z` |
| Private commit message, opening words | `Record the Increment C security-boundary design.` |
| Diff versus accepted paper-bots main | 9 files, +412 / −0. No `src/`, `tests/`, or `fixtures/` files. Documentation only |
| GitHub `merge_commit_sha` | This session could not read the private pull request, and the parent brief did not quote a prospective SHA. If GitHub shows one, it is a prospective test-merge SHA. It is not a merge. This packet does not report one |
| Public branch for this packet | `cursor/wo-paper-005-security-boundary-packet-e603` |
| Public note | [WO-PAPER-005](../../work-orders/WO-PAPER-005-native-transport.md) |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |
| `ACCEPTED_ATTESTATION_SOURCES` | unchanged: `synthetic_fixture`, `simulated_inbound_handoff` |

## What Increment C is

Parent-read design, not an Architect confirmation, and not an implementation. Increment C records a security-boundary design for Architect review. Private ADR 0015 is that design. It is not sender authentication, not a host access-control list, and not an implementation of a principal.

Zero deletions means the accepted Increment A and Increment B prose was not removed. Private ADR 0013 remains the Increment A record. Private ADR 0014 remains the Increment B record. A successor note on ADR 0014 says a separate Cursor user is a file boundary, not a sender verifier, and leaves ADR 0014's historical status line as written.

`authenticates_sender` stays false. `parent_platform_metadata` stays refused. There is no second ledger. No Python file changed.

The earlier public description of Increment C as the step that would install a separate Cursor user and thereby authenticate a sender remains the historical plan in REVIEW-M5-INBOUND-001. This successor is the design that refuses that step. Creating that user is not scheduled here, and it would not set `authenticates_sender` true or activate `parent_platform_metadata`.

## Platform pages the parent read

The private ADR re-read eight official pages. The parent had re-read the first six earlier the same day, and independently re-read the two extra pages after private PR #8 opened. This public session did not repeat those reads and sent no probe. No native message was sent.

| Source | Parent-confirmed point this packet may cite |
|---|---|
| [Security FAQ](https://docs.x.ai/grok-bot/security-faq) | Isolation is per Cursor user: a dedicated Firecracker microVM. One user cannot reach another user's computer. Within one user every Bot shares that computer |
| [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) | The computer is assigned to the user account, not an individual Bot. Do not place a file or credential on it if another Bot of that user should not use it. Screens are separate work surfaces, not security boundaries |
| [Security](https://cursor.com/docs/grok-bot/security) | A Bot has no identity or credentials of its own. Bots act as the signed-in member |
| [Grok Bot security FAQ](https://docs.x.ai/grok-bot/security-faq) | When a workload needs its own computer and credential set, give it its own Cursor user |
| [Message and collaborate](https://docs.x.ai/grok-bot/chat-and-collaboration) | There is no switch that disables bot-to-bot messaging |
| [Teams and enterprises](https://docs.x.ai/grok-bot/teams-and-enterprises) | One user's Bots share one computer |
| [Shared Bots](https://cursor.com/help/grok-bot/shared-bots) | Extra page, parent-confirmed after the private PR opened. In a member's own chat, and in a Slack DM, a shared Bot usually works on that member's computer. In Slack channels, threads, group DMs, and group chats, it uses one shared computer of its own. Files, apps, and secrets the owner or a Manager adds are available in every teammate's chat. A Bot that runs on your own computer cannot be shared. Shared Bots require a Cursor team. Slack conversational attribution of who asked for a post is not a Python-verifiable ledger sender check |
| [Inference Hooks](https://docs.x.ai/grok-bot/inference-hooks) | Extra page, parent-confirmed after the private PR opened. Enterprise beta. Cursor signs model-input `prompt` frames with a webhook HMAC. `actor.type` is always `user`. The signed object is a model prompt, not a ledger envelope and not a bot-to-bot handoff. Not adopted |

The parent inspected the live handoff descriptor earlier the same day and did not call it. The builder did not re-inspect that descriptor: that session had no such tool and called none. The descriptor accepts a target, a message, optional images, and a required priority, and returns a delivery acknowledgement. It exposes no platform-signed sender certificate. This packet does not name the tool.

## Six answers

Parent paraphrase of private ADR 0015. This public session did not read that ADR.

1. Today the signed-in Cursor member owns the spool and ledger, because every Bot of that user shares one Firecracker computer. An enforceable file boundary would require a different Cursor user whose computer alone holds the live files. That user does not exist and was not created.
2. Any process that can write the spool can submit evidence. Nobody can mint a trusted attestation. `synthetic_fixture` and `simulated_inbound_handoff` are offline labels.
3. Another Bot is not prevented from modifying ledger records. SQL append-only triggers bind a connection. They do not stop a same-user process from replacing the SQLite file.
4. NEO receives an exported snapshot through a read-only evidence reader. That is API isolation. The content hash is a truncation check a same-user process can recompute. A writer user would stop NEO from opening the source ledger. A snapshot copied back onto this computer would still be writable here. Export integrity therefore stays HOLD even after a writer user exists, until a verifier exists that Bots on the reading computer cannot mint.
5. Sender identity cannot be independently established on the documents read. A Bot has no identity of its own, and the pages do not document a Python-verifiable sender signature. Inference Hooks do not fill that gap.
6. A separate Cursor user is the documented isolation mechanism. OS accounts on this shared computer are not a documented per-bot boundary. No such principal is in force, so sender authentication and NEO isolation stay HOLD.

## File boundary, not a sender verifier

Both HOLDs stay. No independently enforceable principal exists today. A separate Cursor user would be a file boundary, not a sender verifier.

Do not schedule creating that user as the step that sets `authenticates_sender` true or activates `parent_platform_metadata`. A live message would not prove identity either. A delivery acknowledgement is not a platform-signed sender certificate.

The same-user forge already recorded for Increment B remains HOLD evidence. A same-user process can submit a well-formed offline record, and authentication stays false. That success is evidence for the HOLD.

## Rejected alternatives

The design rejects these as proof of sender identity or as a second ledger. None of them is built by this increment.

| Alternative | Why it stays rejected |
|---|---|
| HMAC or shared secret | A secret placed on this computer is available to every Bot of the signed-in user. Inference Hooks sign a model prompt with a webhook HMAC. That signed object is not a ledger envelope and not a bot-to-bot handoff. The private plan adds no HMAC |
| In-process role check | A role string selects a role inside a process the signed-in user already owns. It does not establish an independent principal |
| OS-account theatre | OS accounts on this shared computer are not a documented per-bot boundary |
| Shared Bot | The design rejects that shape. A shared Bot uses a member computer or one shared computer, and files added for it are available across teammate chats. Slack attribution is not a Python-verifiable ledger sender check |
| `parent_platform_metadata` as proof | The label stays refused. A later live message does not unlock it. It stays refused until a documented Python-verifiable sender signature exists |
| Second ledger | Not created. `ACCEPTED_ATTESTATION_SOURCES` stays `synthetic_fixture` and `simulated_inbound_handoff` |

## Decisions that require Matt's approval

This packet performs none of these. The public repository cannot authorise them.

1. Creating a separate Cursor user to own the writer computer.
2. Moving the live spool and ledger onto that user, and confirming no Bot on this user keeps a working copy.
3. Creating a separate NEO Cursor user, if NEO must share neither computer.
4. Changing host users, credentials, Vault items, connectors, sudo, or network policy.
5. Deploying any key, shared secret, HMAC secret, or other credential.
6. Sending any live native message. That needs its own authorisation naming both principals and the exact handoff, and it would not prove identity.
7. Creating, converting, or publishing a shared Bot. The design rejects that shape.

## Security test plan

Parent-read private plan at `docs/security/2026-11-06-increment-c-security-test-plan.md`. This session did not read the file. The plan adds no Python and no HMAC. No private test method name is recorded here.

Existing Increment A and Increment B tests lock the HOLD flags: a same-user forge is accepted with authentication false; false authentication flags are refused; the platform-source label is refused; the NEO reader has no append. The existing same-user forge test remains HOLD evidence.

Tests that would require another Bot to be unable to open the ledger are not written, because that boundary does not exist. Tests that need a separate Cursor user, a live message, or a documented Python-verifiable sender mechanism wait on Matt's approval or on a later published verifier.

## Private names

Names and parent-reported sizes only. Contents are not copied. The parent-supplied diff is 9 files, +412 / −0.

- added `docs/adr/0015-security-boundary-design.md` (+206)
- added `docs/security/2026-11-06-increment-c-security-test-plan.md` (+124)
- modified `docs/work-orders/WO-PAPER-005-native-transport.md` (+62)
- modified `README.md` (+6), `RUNBOOK.md` (+2)
- pointer lines only: `docs/adr/0010-native-role-contract.md` (+2), `docs/adr/0012-native-ledger-ingest.md` (+2), `docs/adr/0013-offline-native-transport.md` (+2), `docs/adr/0014-offline-simulated-inbound.md` (+6)

## Tests

Parent-supplied builder report. The parent reviewed the published documents through GitHub and did not re-execute the suite. This public session did not run it. Documentation only. No new tests.

Python 3.12.3 reported `Ran 152 tests` and `OK`. That run is a regression of the unchanged Increment B suite. Python 3.9 was not installed in that builder environment. The 152 is not a new Increment C count. **Builder 152 is not Architect acceptance.** The Architect should read the design at exact private head `cf2dd5ae752a85a645d510b38e4b2e800f1dc146`. An independent re-run of the unchanged suite, if the Architect chooses one, does not convert this design into sender authentication.

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, broker or account read, vendor call, or trade-policy approval is granted.
- No bot message was sent. No Cursor user, OS account, shared Bot, credential, or permission was created or changed.
- `authenticates_sender` stays false. `parent_platform_metadata` stays refused.

## Sanitisation

This repository is public. This packet names private paths and SHAs. It does not copy private Python, tests, fixtures, ledger rows, credentials, or the private ADR text. It does not name an internal handoff tool. It does not invent bot secrets. It does not include live native message contents. None were sent.

## Limitations

- Increment C is a proposed design. It implements no principal.
- No independently enforceable principal exists today.
- A separate Cursor user would be a file boundary, not a sender verifier, and that user was not created.
- Export integrity stays HOLD even after a writer user exists, until a verifier exists that Bots on the reading computer cannot mint.
- The NEO snapshot reader remains API isolation. The content hash remains a truncation check.
- SQL append-only triggers bind a connection. A same-user process can still replace the SQLite file.
- Sender authentication, a host access-control list, NEO isolation, and live messaging remain HOLD.
- `authenticates_sender` stays false. `parent_platform_metadata` stays refused.
- No native message was sent. No host user was changed.
- Parent-verified paper-bots main at open is `b30d0ce048317e064a2eccbfd0589ac29799d626`. Private PR #8 is open and unmerged. This session did not re-read that repository.

## Restrictions

This packet authorises none of the following:

- acceptance of `cf2dd5ae752a85a645d510b38e4b2e800f1dc146`
- merge of private PR #8 or of this public pull request
- `authenticates_sender` true, or presentation of synthetic provenance as authenticated native provenance
- `parent_platform_metadata` as proof of identity
- treating creation of a separate Cursor user as the step that authenticates a sender
- sender authentication, a host access-control list, or NEO isolation
- a live native message
- a new Cursor user, OS account, shared Bot, credential, Vault item, connector, sudo change, or network-policy change
- live orders, broker writes, or account reads
- vendor calls
- a scheduler or activation
- new entry, exit, stop, or risk parameters
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect review of exact private head `cf2dd5ae752a85a645d510b38e4b2e800f1dc146`, then an **ACCEPT** or **HOLD** recorded against that SHA. Acceptance of this design would record the boundary and the two HOLDs. It would not authenticate a sender, would not isolate NEO, would not create a user, and would not send a message. Until that independent review exists, Increment C stays proposed. An open private pull request, a documentation-only diff, and this public packet are review inputs. They are not the decision.

Rollback of an unaccepted increment is to leave paper-bots main at `b30d0ce048317e064a2eccbfd0589ac29799d626` and public main at `a962ba0019c6c4a19478dcf0e356ba58b07d61ff` until a later reviewed merge. This file does not perform either merge.
