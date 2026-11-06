# WO-PAPER-004 — attested native envelope ingest

> **ARCHITECT SUPERSESSION — 6 Nov 2026:** Builder handoff at private `553ec517455ce6ef797b049e65ec61389daa20da` is now independently **HOLD**, despite 110/110 Python 3.12.14 tests. Replay can silently replace an omitted required parent with stored evidence, ignore a wrong explicitly supplied parent hash, and ignore a changed allowed R quality claim. [Dated independent review](2026-11-06-wo-paper-004-553ec5-independent-hold.md). Both PRs remain OPEN/UNMERGED. No live Grok bridge or NEO OS ACL was proven; safety gates unchanged. Earlier builder-ready status below is historical.

**ID:** REVIEW-M4-NATIVE-001  
**Date:** 2026-11-06 (Europe/London)  
**Record type:** public governance packet for an open private increment.  
**Disposition requested:** Architect **ACCEPT or HOLD** after an independent re-audit of exact private head `553ec517455ce6ef797b049e65ec61389daa20da`.  
**This packet does not accept the increment.** It does not merge private paper-bots PR #5 or this public pull request. Builder tests below are a parent-confirmed transcript, not an Architect result.

Accepted M3 history stays accepted. [REVIEW-M3-ACCEPT-001](2026-11-06-m3-70a673-independent-acceptance.md) records the independent acceptance and ordinary merge of private paper-bots PR #4 head `70a673f973bd52155d495f6873eb417374f4948b` into paper-bots main `b2cb75867d2408a0018333213a0dd2cfb91ac670`. That acceptance is limited to synthetic offline discovery, provenance and fallback, typed provisional six-role interfaces, and the Python paper ledger and NEO digest. Earlier M3 HOLD files are unchanged historical evidence for their own heads. Banners that still describe paper-bots PR #4 as open or unmerged are historical snapshots of those earlier heads.

## Evidence classes

| Class | What it covers |
|---|---|
| Verified by this public session, before the write | `git fetch origin main` returned `b0c8f55109fcc92d8f55ec7b593c696b9887475d`, message `Merge M3: independently accepted offline discovery governance` |
| Parent-verified private read-back, 2026-11-06T07:43:00Z | PR #5 state, head, base, branch, file count, diff size, commit count, ADR 0012 rule, changed-file names, and the builder test transcript |
| Not claimed here | Architect acceptance, a merge, host ACL, live native execution, vendor rights, or a fourth FMP call |

This public session did not open `maff0000/paper-bots` and did not copy private source, fixtures, raw vendor data, or credentials. Private facts below are the parent read-back. The SHA of the public commit that adds this packet is intentionally absent from this file. Read the public branch after push.

## Starting heads and bases

| Item | SHA / state |
|---|---|
| Public `maff0000/CGPT-INVESTMENT` `origin/main`, required start and base | `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| Accepted M3 private head, already merged | `70a673f973bd52155d495f6873eb417374f4948b` |
| Private paper-bots `main`, unchanged, and PR #5 base | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| New private head under review | `553ec517455ce6ef797b049e65ec61389daa20da` |
| Parent PID | PID-EQUITY-PAPER-001 |
| Frozen QARP-ROTATION-001 v1.0.0 manifest SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged) |

## Private pull request

| Item | Parent-verified value |
|---|---|
| Pull request | [paper-bots #5](https://github.com/maff0000/paper-bots/pull/5) |
| Title | WO-PAPER-004: attested native envelope ingest |
| Branch | `cursor/wo-paper-004-native-ledger-ce05` |
| State | OPEN |
| `merged` | false |
| `merged_at` | null |
| Commits | 1 |
| `changed_files` | 10 |
| Diff size | +1828 / −4 |
| Private work order | `docs/work-orders/WO-PAPER-004-native-ledger.md` |
| Public sanitised note | [WO-PAPER-004](../../work-orders/WO-PAPER-004-native-ledger.md) |

## Changed-file manifest

Names only, versus accepted paper-bots main. No source, fixture body, or vendor payload is copied here.

1. `README.md`
2. `RUNBOOK.md`
3. `docs/adr/0010-native-role-contract.md`
4. `docs/adr/0012-native-ledger-ingest.md`
5. `docs/work-orders/WO-PAPER-004-native-ledger.md`
6. `fixtures/native/wo004_handoff.json`
7. `src/paperbots/ledger.py`
8. `src/paperbots/native_contract.py`
9. `src/paperbots/native_ingest.py`
10. `tests/test_native_ingest.py`

## Adopted rule

Parent-read from private ADR 0012:

The attested native bot id is an argument and selects the role from the allowlist. A producer string inside the envelope is a claim and cannot append another role's event. One transactional writer sits in front of the existing ledger.

Synthetic chain exercised in-process:

| Role | Reported result |
|---|---|
| E | UNCHECKED candidate |
| S | Screen of frozen QARP-ROTATION-001 v1.0.0; entry authority NONE; classification and source mapping UNKNOWN |
| R | HOLD |
| M | Research HOLD with no proposal |
| T | `EXECUTION_REFUSAL` / `NO_ORDER`; `order_created` false; `is_fill` false |
| NEO | Reconstructs the chain and may append `NEO_REVIEW` only |

## ADR 0012 summary

Private ADR 0012 amends private ADR 0010. It implements the adapter named, and not previously started, in public [ADR-APP-001](../../docs/adr/ADR-APP-001-platform-findings.md): offline validation of typed JSON, frozen strategy and role-transition checks, one central transactional writer, and a NEO audit result. `native-probe-1` still does not write. `native-ledger-1` is `paperbots.native_ingest`.

The parent-usable interface named by the builder is:

```text
python -m paperbots.native_ingest --attested-native-bot-id <platform id> --envelope <file>
```

That command is a name for the proposed private entry point. It is not a licence to run it against live teammates, vendor APIs, or an order path. Private fixture contents are not published. The real provisioned bot UUIDs are attested-identity fixtures. A live teammate message was not sent.

The named adapter is now proposed on private PR #5. The host-isolation gap in ADR-APP-001 stays open. See the next section.

## What was demonstrated

In-process synthetic envelopes were committed to the existing ledger, and NEO reconstructed that chain. Native-to-Python execution remains **UNVERIFIED**. The demonstration is the in-process writer and the reconstruction, on synthetic envelopes, at the private head above.

## NEO isolation

Be exact about the boundary that exists.

- In-process ingest refuses NEO writing decision or execution events.
- The pre-existing NEO handle may still append `NEO_REVIEW`, `NEO_COHORT`, and `NEO_DISCOVERY_DIGEST`. That allowlist was not widened.
- No host ACL was created.
- One user's bots share the computer, its files, logins, and permitted connectors.
- There is no switch that disables bot-to-bot messages.
- A JSON producer field does not authenticate the sender.
- An alternative was proposed and was not built: a separate operating-system principal that alone can open the ledger, with the parent attesting the bot id from platform metadata.

Interface refusal inside the process is not host isolation. This packet does not claim isolation that the platform does not provide.

## Tests

Parent-confirmed in the private builder transcript. Not an Architect run. Fresh detached worktree `/tmp/wo004-final` at `553ec517455ce6ef797b049e65ec61389daa20da`.

`PYTHONPATH=src python3.9 -m unittest discover -s tests -v`

- Interpreter: Python 3.9.25
- Exit 0
- Stderr: `Ran 110 tests in 0.785s` / OK
- Stdout empty

`PYTHONPATH=src python3.12 -m unittest discover -s tests -v`

- Interpreter: Python 3.12.3
- Exit 0
- Stdout empty
- Builder final report on that interpreter: stderr `Ran 110 tests in 0.696s` / OK
- The same parent notes also record an earlier same-tree run that printed `Ran 110 tests in 0.691s`, and a detached confirmation line `PY312 STDERR SUMMARY Ran 110 tests. OK`

The integer 110 was observed on stderr. It includes the previously accepted tests plus `tests/test_native_ingest.py`. The new file covers normal handoff and NEO explanation, rejected handoff, missing evidence, replay with unchanged semantic identity, semantic conflict that does not replace the row, write failure and recovery, claimed-role non-elevation, and the NEO protection result. These builder runs are not Architect acceptance.

## Security and data rights

- **G0 remains OPEN.**
- Provider rights remain **UNVERIFIED**. Finviz, FMP, Massive, and IBKR rights are not newly verified by this packet.
- FMP remains exactly three historical calls: `profile` SPY HTTP 200, one record; `historical-price-eod/light` SPY HTTP 200, two records; `batch-quote` SPY,XOM HTTP 402, non-JSON. That third result is an HTTP 402 non-JSON response. It is not a label "call 402". There is no fourth call.
- No vendor call, credential, raw bar, or private fixture body is added to this public repository.
- The frozen QARP manifest SHA-256 above is unchanged. No new entry, exit, stop, or risk parameter is adopted.

## Limitations

- The demonstrated path is in-process only.
- Live native execution is UNVERIFIED.
- No host ACL was created. Shared-computer platform limits remain.
- `native-probe-1` still does not write.
- A live teammate message was not sent.
- Paper-bots main is unchanged at the M3 merge commit. PR #5 is open.

## Restrictions

This packet authorises none of the following:

- merge of private PR #5 or of this public pull request
- live orders, broker writes, or account reads
- vendor calls
- a scheduler or activation
- new entry, exit, stop, or risk parameters
- release of stop-dependent M/T pathways, which remain **HOLD**

## Proposed disposition

Request an Architect re-audit of exact private head `553ec517455ce6ef797b049e65ec61389daa20da`, then an **ACCEPT** or **HOLD** recorded against that SHA. Until that independent review exists, the increment stays proposed. Passing builder tests, an open pull request, and this public packet are review inputs. They are not the decision.

Rollback of an unaccepted increment is to leave paper-bots main at `b2cb75867d2408a0018333213a0dd2cfb91ac670` and public main at `b0c8f55109fcc92d8f55ec7b593c696b9887475d` until a later reviewed merge. This file does not perform either merge.
