# WO-PAPER-006 — synthetic NEO decision review

> **DATED HOLD AND SUCCESSOR POINTER — 6 November 2026. This file is not rewritten.** The Architect HOLDs exact private head `619a607ed1879c93a82e4e652b2edc7531efb530`. That HOLD answers the historical request below. It does not delete the request, and it does not accept a later head. The current proposal is exact head `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. Its parent `4078c6a560901ea67eb217f0486cdc18d045efa2` is the intermediate evidence-relationship correction, whose own parent is the held head. The successor packet is [REVIEW-M6-NEO-002](2026-11-06-wo-paper-006-neo-review-correction-packet.md). It requests Architect ACCEPT or HOLD of `4b3dac4c4137a5cb89a9587862e5fe25c464887b` and does not accept it. Public PR head before the successor write: `1c6c1423d05e62c52a73a6b37e62cb43b4ca2d9c`. Public main remains `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`. The text below stays the historical request of `619a607`.

> **ACCEPT POINTER — 6 November 2026.** [REVIEW-M6-NEO-003](2026-11-06-wo-paper-006-neo-review-acceptance.md) records Architect ACCEPT of exact `4b3dac4c4137a5cb89a9587862e5fe25c464887b` only. The HOLD pointer above and the historical request below stay. Neither pull request is merged.

> **CLOSURE POINTER — 6 November 2026.** [REVIEW-M6-NEO-004](2026-11-06-wo-paper-006-neo-review-closure.md) records the ordinary private merge at `28fe536e03ab8df1704d119b045158cc0a766f4f`. The HOLD and ACCEPT pointers above stay. Public PR #13 is not merged.

**ID:** REVIEW-M6-NEO-001
**Date:** 2026-11-06 (Europe/London)
**Record type:** public governance packet for an open private increment.
**Disposition requested:** Architect **ACCEPT or HOLD** of exact private head `619a607ed1879c93a82e4e652b2edc7531efb530` after independent review.
**This packet does not accept that head.** It does not merge private [paper-bots PR #9](https://github.com/maff0000/paper-bots/pull/9) or this public pull request. It does not send a message. It does not copy private Python, tests, fixtures, or schema catalog JSON. Builder-reported `Ran 161 tests` is not Architect acceptance. The parent did not re-execute the suite. This public session did not run it.

Accepted Increment C stays accepted as a design only, with no deployment. [REVIEW-M5-INDEP-003](2026-11-06-wo-paper-005-cf2dd5-independent-acceptance.md) records the independent acceptance of private paper-bots PR #8 exact head `cf2dd5ae752a85a645d510b38e4b2e800f1dc146` and the ordinary merge to paper-bots main `c0b9f540c09caec08fb87e77bf445d0e580f843e`. That acceptance does not create a writer or NEO principal. Increment C isolation deployment is deferred by t79u (6 November 2026). Private ADR 0015 and REVIEW-M5-INDEP-003 remain historical reference. They are not rewritten and not deployed. This packet does not pursue additional Cursor users, separate computers, or dedicated NEO infrastructure.

Accepted Increment B stays accepted. [REVIEW-M5-INDEP-002](2026-11-06-wo-paper-005-124c0f-independent-acceptance.md) records the independent acceptance of private paper-bots PR #7 exact head `124c0f2af9e7a60a783718516c20697f3dd3c386` and the ordinary merge to paper-bots main `b30d0ce048317e064a2eccbfd0589ac29799d626`. Accepted Increment A stays accepted. [REVIEW-M5-ACCEPT-001](2026-11-06-wo-paper-005-b87354-independent-acceptance.md) records the independent acceptance of private paper-bots PR #6 exact head `b87354d77dc4d94273291ae571c3837924f22fdd` and the ordinary merge to paper-bots main `ba001debca9e695fc3356c8720a17fa15836c31c`. [REVIEW-M5-INDEP-001](2026-11-06-wo-paper-005-d57f2e-independent-hold.md) remains the HOLD of exact older head `d57f2e3211cb0ecd171278f26ee4b6f4aca8a9c1` only. [REVIEW-M5-TRANSPORT-001](2026-11-06-wo-paper-005-offline-transport-packet.md), [REVIEW-M5-TRANSPORT-002](2026-11-06-wo-paper-005-recovery-integrity-packet.md), [REVIEW-M5-INBOUND-001](2026-11-06-wo-paper-005-simulated-inbound-packet.md), and [REVIEW-M5-BOUNDARY-001](2026-11-06-wo-paper-005-security-boundary-packet.md) stay historical and are not edited here.

[REVIEW-M4-ACCEPT-001](2026-11-06-wo-paper-004-541f3f-independent-acceptance.md) remains the acceptance of the offline in-process adapter. [REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md) remains the HOLD of `553ec517455ce6ef797b049e65ec61389daa20da`. [REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md) remains the HOLD of `f4371c599fb1c45e28c403549090e92fd825ce67`. Those HOLDs are valid only for those older exact heads. None of those files is edited here. Merged public [PR #10](https://github.com/maff0000/CGPT-INVESTMENT/pull/10), [PR #11](https://github.com/maff0000/CGPT-INVESTMENT/pull/11), and [PR #12](https://github.com/maff0000/CGPT-INVESTMENT/pull/12) are closed history and are not reused.

This file does not contain the SHA of the public commit that adds it. The packet is pinned to the head of branch `cursor/wo-paper-006-neo-review-packet-5d19` after that commit is pushed. Read the public branch after push.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `git fetch origin main` returned `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56`, message `Merge PR #12 — WO-PAPER-005 Increment C security-design acceptance`, parents `a962ba0019c6c4a19478dcf0e356ba58b07d61ff` and `d6fc7957613792478d3ea436bed616d409738113`. That SHA is current `main` and the parent of this public commit. `gh pr view 9 --repo maff0000/paper-bots` returned `Could not resolve to a Repository`. This session did not read private blobs |
| Parent-supplied private read-back, 6 Nov 2026 | Private PR #9 state, exact head, parent, base, branch, author and creation times, commit message, diff size, named paths, the eight findings, quality labels, the contract decision, the self-improvement requirement, the prepared message, the builder report, and the parent's reading of the work order, ADR 0016, the playbook, the example review, the contract note, the prepared handoff, the planted-session README, and the new tests. This public session did not |
| Not claimed here | Architect acceptance of `619a607e`, a merge, a prospective merge-commit SHA, a re-run of the 161 tests, sender authentication, a host access-control list, an implemented principal, NEO isolation, a live bot message, deployment of Increment C, an experimental Bot runtime, a shadow comparison, replacement of QARP-ROTATION-001 v1.0.0, vendor rights, or a fourth FMP call |

This public session did not copy private Python, tests, fixture JSON, schema catalog JSON, ledger rows, or credentials. Private facts below are the parent read-back. Naming a private path or SHA is not a copy of its contents.

## Heads

| Item | SHA / state |
|---|---|
| Public `origin/main` before this write, and parent of this public commit | `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` |
| Public main message | `Merge PR #12 — WO-PAPER-005 Increment C security-design acceptance` |
| Parents of that public main | `a962ba0019c6c4a19478dcf0e356ba58b07d61ff`, `d6fc7957613792478d3ea436bed616d409738113` |
| Private pull request | [paper-bots #9](https://github.com/maff0000/paper-bots/pull/9) |
| Private title | WO-PAPER-006 synthetic NEO review (proposed, not accepted) |
| Private branch | `cursor/wo-paper-006-neo-review-877f` |
| Private head under review | `619a607ed1879c93a82e4e652b2edc7531efb530` |
| Single parent of that commit, PR base, and paper-bots `main` at open | `c0b9f540c09caec08fb87e77bf445d0e580f843e` |
| Private state | OPEN, not draft, not merged |
| Commits on the private PR | 1. Author Cursor Agent. Author date `2026-11-06T13:49:35Z`. PR created `2026-11-06T13:49:53Z` |
| Private commit message | `Add WO-PAPER-006 synthetic NEO decision review. Record a v0.3 decision-evidence contract on the existing ledger, a planted six-Bot session, and an offline NEO review that separates decision quality from a later mark. The prepared T-Bot to NEO handoff is not sent.` |
| Diff versus paper-bots main at open | 25 files, +4437 / −1 |
| GitHub `merge_commit_sha` | This session could not read the private pull request. The parent read-back did not quote a prospective SHA and instructed this packet not to write one. If GitHub shows one, it is not a merge. This packet does not report one |
| Public branch for this packet | `cursor/wo-paper-006-neo-review-packet-5d19` |
| Public note | [WO-PAPER-006](../../work-orders/WO-PAPER-006-neo-decision-review.md) |
| Public ADR | [ADR-APP-002](../../docs/adr/ADR-APP-002-bot-self-improvement.md) |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |
| Ruleset digest | `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac` (unchanged) |

## What the increment is

Parent-read behaviour, not an Architect confirmation. A synthetic six-Bot decision session and the first example NEO review of it. E, S, R, M, and T emit structured decision evidence. An offline demonstrator applies playbook `NEO-REVIEW-PLAYBOOK-v0.1`, written for the existing native NEO Bot, and writes an example report. The demonstrator is labelled SYNTHETIC / OFFLINE and is not the native NEO Bot. The module docstring on `src/paperbots/neo_report.py` says that module is not the native NEO Bot and does not apply this playbook. No native message was sent.

Session `WO006-SYN-SESSION-001`. Correlation `00600006-0006-4000-8000-000000000001`. Market session `FIXTURE-2026-11-06`. Risk gate `NOT_INVOKED_NO_AUTHORITY`. Predictive performance `NOT_ASSESSED`.

This milestone is NEO's analytical value on synthetic evidence. Competing versions are later. Increment C isolation remains deferred.

## Planted findings

| ID | Class | What the review finds |
|---|---|---|
| `F-REASON-S-EARNINGS` | `REASONING_DOES_NOT_FOLLOW` | S-Bot asserts earnings_quality PASS; the input is FAIL |
| `F-REASON-S-MARGIN` | `REASONING_DOES_NOT_FOLLOW` | S-Bot asserts gross_margin_direction EXPANDING; the input is DETERIORATING |
| `F-MISSING-S-CONFIRMATION` | `MISSING_EVIDENCE` | S-Bot records STRATEGY_MATCH while independent_confirmation is ABSENT and the stated requirement is PRESENT |
| `F-BROKEN-M-CAUSAL` | `BROKEN_CAUSAL_REFERENCE` | M-Bot cites causal id `00600006-0006-4000-8000-000000000099`, which is not in the session |
| `F-INCONSISTENT-M-RBOT` | `CROSS_BOT_INCONSISTENCY` | M-Bot asserts R-Bot action PASS; R-Bot's decision is HOLD |
| `F-MISSING-M-SKEPTIC` | `MISSING_EVIDENCE` | M-Bot proposes PROPOSE_SHADOW_ENTRY and does not cite R-Bot's HOLD that blocked a new entry |
| `F-MISSED-S-WO006B` | `MISSED_OPPORTUNITY` | E-Bot recorded SYN-WO006B as meeting the stated threshold; S-Bot recorded no decision for it |
| `F-OUTCOME-M-MARK` | `FAVOURABLE_OUTCOME_POOR_DECISION` | A later synthetic mark moves SYN-WO006A from 100.00 SYN to 112.00 SYN; M-Bot quality stays POOR. The mark is not a fill |

Quality labels: E SOUND, S POOR, R SOUND, M POOR, T SOUND, NEO NOT_A_DECISION. A favourable mark does not upgrade a poor decision. A sound control stays sound when its mark is favourable.

## Contract decision

Parent-supplied decision. The private schema catalog JSON is not copied here.

`native-ledger-1` stays as accepted. It drops `note` and writes a fixed explanation, so it cannot carry reasoning NEO can judge. v0.2 payloads are closed. ADR 0008 treats a payload change as a different decision. The new contract is schema v0.3, `decision-evidence-1`, on the same append-only ledger. There is no second ledger. Event types on this path:

| Event type | Who may append it |
|---|---|
| `DECISION_EVIDENCE` | E, S, R, M, T |
| `SYNTHETIC_OUTCOME_MARK` | T |
| `NEO_SESSION_REVIEW` | NEO |
| `IMPROVEMENT_PROPOSAL` | the Bot named `proposed_by` |

Pre-existing role handles are not widened and cannot append these types or an order/fill. `authenticates_sender` stays false. `parent_platform_metadata` stays refused. `live_message_sent` stays false. Synthetic provenance is not authenticated native provenance.

The parent-reported addition in `src/paperbots/constants.py` is `SCHEMA_VERSION_V03 = "0.3.0"`. That source file is not copied here.

The financial performance ledger and the decision-evidence ledger stay distinct. Today both are different event types in the one append-only ledger. An outcome append does not update the decision row.

## Self-improvement requirement

Recorded verbatim as a first-class architectural requirement. The public ADR is [ADR-APP-002](../../docs/adr/ADR-APP-002-bot-self-improvement.md). [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md) keeps the platform findings and receives a pointer only. This packet does not accept the requirement by recording it.

AGENT SELF-IMPROVEMENT — MANDATORY CAPABILITY

Every Bot must be capable of proposing improvements to its own prompts, analytical methods and strategies, informed by its experience, NEO's findings and collaboration with other Bots.

Improvements must be versioned and recorded in GitHub, with the original hypothesis, evidence, proposed change, evaluation results and rollback path.

Bots may autonomously develop and test experimental versions in offline or shadow mode. Their accepted versions remain unchanged until independently reviewed.

NEO must track performance by Bot, strategy and version, evaluate whether proposed improvements genuinely outperform their baselines, and recommend promotion or rejection.

NEO itself must be subject to evaluation and improvement.

No Bot may alter historical evidence, silently replace approved trading rules, increase authorised risk or activate live execution.

The common objective is sustainable, risk-controlled growth of the trading ledger through continuous, measurable improvement.

Sequence: NEO finding → proposed change → GitHub decision → bounded implementation → independent review → acceptance. A Bot may also start at the proposed change from its own experience, without waiting for NEO.

| Activity | Authority |
|---|---|
| Challenge another Bot's decision | Autonomous |
| Identify and explain mistakes | Autonomous |
| Research alternative methods | Autonomous |
| Propose strategy improvements | Autonomous |
| Create experimental Bot versions | Autonomous |
| Run offline/shadow comparisons | Autonomous |
| Recommend promotion of a better version | Autonomous |
| Replace an approved production strategy | Independent review required |
| Change risk limits or activate live trading | Explicit approval required |

This milestone records the table and stops at unevaluated proposals (`evaluation_status` `NOT_RUN`, `promotion` `NOT_RECOMMENDED`, `approved_strategy_replaced` false). It does not create an experimental Bot runtime or run a shadow comparison. Competing versions (for example S-Bot v1.0 vs v1.1) are a later roadmap item, not implemented here.

S-Bot files its own earnings-quality method proposal from Bot experience (experimental label `1.1-shadow-not-run`). The original `STRATEGY_MATCH` stays. QARP-ROTATION-001 v1.0.0 is not replaced. Frozen file SHA-256 remains `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. Ruleset digest remains `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. Applying a proposal raises and does not write the frozen manifest.

## Prepared handoff (not sent)

Named sender: T-Bot `81d8cf38-188e-4592-b08d-b59d6e461e83`.
Named recipient: NEO `e1e372c8-20e9-45a6-856f-4eabdf018308`.
Status: `PREPARED_NOT_SENT`. `live_message_sent` false. `authenticates_sender` false. `parent_platform_metadata` REFUSED. The send function raises and does not send.

Exact message text (the text that would later need named-principal authorisation):

```
T-Bot asks NEO to review synthetic offline session WO006-SYN-SESSION-001 under decision-evidence contract decision-evidence-1 and NEO review playbook NEO-REVIEW-PLAYBOOK-v0.1.

The session is fixture evidence for E-Bot, S-Bot, R-Bot, M-Bot, and T-Bot, plus one synthetic outcome mark. The mark is not an order and not a fill. Correlation 00600006-0006-4000-8000-000000000001. Market session FIXTURE-2026-11-06.

Report findings and a proposed improvement for each Bot. Keep decision quality separate from the later mark. Do not treat a favourable mark as a better decision. Do not promote a strategy. Do not change a risk limit. Do not activate trading. Do not replace QARP-ROTATION-001 v1.0.0.

This handoff is prepared only. It has not been sent. Sender identity is not authenticated. Synthetic provenance is not authenticated native provenance.
```

Later questions from NEO back to S-Bot or M-Bot are described, not prepared as sendable messages. This packet does not invent that question text.

## Private names

Names only. Contents are not copied. The parent-supplied diff is 25 files, +4437 / −1. Per-file blob SHAs were not in the parent read-back and are not invented here. ADR 0015 was not edited.

Added:

- `docs/work-orders/WO-PAPER-006-neo-decision-review.md`
- `docs/adr/0016-bot-self-improvement.md`
- `docs/roadmap/bot-self-improvement.md`
- `docs/contracts/decision-evidence-1.md`
- `docs/schemas/v0.3/README.md`
- `docs/schemas/v0.3/catalog.json`
- `docs/neo/NEO-REVIEW-PLAYBOOK-v0.1.md`
- `docs/reviews/2026-11-06-neo-wo006-synthetic.md`
- `examples/wo006_neo_session_review.json`
- `docs/handoffs/2026-11-06-tbot-to-neo-wo006-PREPARED-NOT-SENT.md`
- `fixtures/native/wo006_session/README.md`
- `fixtures/native/wo006_session/session.json`
- `src/paperbots/decision_evidence.py`
- `tests/test_decision_evidence.py`

Modified (pointer / catalog / docstring only, except the new modules above):

- `README.md`, `RUNBOOK.md`
- `docs/adr/0010-native-role-contract.md` (+2)
- `docs/adr/0012-native-ledger-ingest.md` (+2)
- `docs/schemas/v0.2/README.md` (+2)
- `docs/work-orders/WO-PAPER-005-native-transport.md` (+4 successor paragraph only; no deletions of Increment A/B/C text)
- `fixtures/README.md` (+1)
- `src/paperbots/constants.py` (adds `SCHEMA_VERSION_V03 = "0.3.0"`)
- `src/paperbots/native_contract.py`
- `src/paperbots/schemautil.py`
- `src/paperbots/neo_report.py` (module docstring only: it is not the native NEO Bot and does not apply this playbook)

## Tests

Parent-supplied builder report. The parent reviewed the published documents and tests through GitHub and did not re-execute the suite. This public session did not run it.

Python 3.12.3, command `PYTHONPATH=src python3 -m unittest discover -s tests -q`, reported `Ran 161 tests`, `OK`, exit 0. The 161 includes the previous 152. Python 3.9 was not installed in that builder environment. **Builder 161 is not Architect acceptance.**

The parent read the work order, ADR 0016, the playbook, the example review, the contract note, the prepared handoff, the planted-session README, and the new tests. The tests lock:

- the eight planted findings
- quality independent of the mark
- rejection of `authenticates_sender` true, `parent_platform_metadata`, trading permission, and a replaced strategy version
- append-only ingest and replay
- no silent QARP replacement
- closed pre-existing role allowlists
- named unsent handoff
- committed report matches a fresh review

No private test body or test method name is copied here.

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402 non-JSON. There is no fourth call.
- Stop-dependent M/T pathways remain **HOLD**.
- No scheduler, live order, broker or account read, vendor call, or trade-policy approval is granted.
- No bot message was sent. No Cursor user, OS account, credential, or permission was created or changed.
- `authenticates_sender` stays false. `parent_platform_metadata` stays refused. `live_message_sent` stays false.
- Increment C isolation deployment remains deferred.

## Sanitisation

This repository is public. This packet names private paths and SHAs. It quotes the prepared message because that text is the handoff a later authorisation would have to name. It records the self-improvement requirement verbatim. It does not copy private Python, tests, fixture JSON, or schema catalog JSON. It does not invent bot secrets. It does not include a live native message. None was sent.

## Decisions in this public packet

- A new public ADR, [ADR-APP-002](../../docs/adr/ADR-APP-002-bot-self-improvement.md), holds the requirement. ADR-APP-001 stays the platform-findings record and receives a pointer.
- The predecessor work order receives a successor pointer. Its Increment A, B, and C text is not rewritten.
- Historical REVIEW-M5 files are not edited.
- The private repository is not edited.
- No prospective merge-commit SHA is recorded for either pull request.

## Deviations

None that add scope. This session could not open `maff0000/paper-bots`, which is the condition the parent read-back covers. Per-file blob SHAs were not supplied and are not invented. The question text of later NEO-to-S or NEO-to-M messages was not supplied and is not invented.

## Limitations

- The increment is proposed. An open private pull request and this public packet are review inputs. They are not the decision.
- The offline demonstrator is not the native NEO Bot.
- The prepared handoff was not sent. Sender identity is not authenticated. Synthetic provenance is not authenticated native provenance.
- `authenticates_sender` stays false. `parent_platform_metadata` stays refused.
- A favourable mark does not change decision quality. The mark is not an order and not a fill.
- QARP-ROTATION-001 v1.0.0 is not replaced. The earnings-quality proposal is `1.1-shadow-not-run`.
- Competing versions are not implemented. No experimental runtime and no shadow comparison were run.
- Increment C isolation is not deployed. No separate Cursor user, computer, or dedicated NEO infrastructure is created here.
- Sender authentication, a host access-control list, NEO isolation, and live messaging remain HOLD.
- Parent-verified paper-bots main at open is `c0b9f540c09caec08fb87e77bf445d0e580f843e`. Private PR #9 is open and unmerged. This session did not re-read that repository.
- Builder 161 is not an independent re-run.

## Restrictions

This packet authorises none of the following:

- acceptance of `619a607ed1879c93a82e4e652b2edc7531efb530`
- merge of private PR #9 or of this public pull request
- `authenticates_sender` true, or presentation of synthetic provenance as authenticated native provenance
- `parent_platform_metadata` as proof of identity
- sending the prepared T-Bot to NEO handoff
- sender authentication, a host access-control list, or NEO isolation
- deployment of Increment C, a new Cursor user, or a separate computer
- replacement of QARP-ROTATION-001 v1.0.0 or a silent write of the frozen manifest
- promotion of the `1.1-shadow-not-run` proposal
- an experimental Bot runtime or a shadow comparison
- live orders, broker writes, or account reads
- vendor calls, including a fourth FMP call
- a scheduler or activation
- new entry, exit, stop, or risk parameters
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect review of exact private head `619a607ed1879c93a82e4e652b2edc7531efb530`, then an **ACCEPT** or **HOLD** recorded against that SHA. Acceptance would record the synthetic review, the `decision-evidence-1` contract on the existing ledger, and the self-improvement requirement at unevaluated-proposal status. It would not send the handoff, would not replace an approved strategy, would not authenticate a sender, would not deploy Increment C isolation, and would not create an experimental runtime. Until that independent review exists, WO-PAPER-006 stays proposed.

Rollback of an unaccepted increment is to leave paper-bots main at `c0b9f540c09caec08fb87e77bf445d0e580f843e` and public main at `0cb49b0b5bb1df0e7e7c9e3d7d8eaf74f8e66e56` until a later reviewed merge. This file does not perform either merge.
