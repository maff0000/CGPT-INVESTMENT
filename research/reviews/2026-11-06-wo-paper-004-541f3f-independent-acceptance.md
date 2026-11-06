# REVIEW-M4-ACCEPT-001 — WO-PAPER-004 independent exact-head acceptance

**Date:** 2026-11-06 (Europe/London)  
**Architect decision:** **ACCEPT — offline in-process synthetic native-to-ledger adapter only**. This is not a permission to trade, use real providers, schedule discovery, or claim authenticated native-app delivery.

## Exact-head and merge record

| Item | Verified result |
|---|---|
| [Private paper-bots PR #5](https://github.com/maff0000/paper-bots/pull/5) accepted head | `541f3f175da8ec684f942dea767a1352cf5df0fb` |
| Previously accepted private `main` / PR base | `b2cb75867d2408a0018333213a0dd2cfb91ac670` |
| **Private merge commit**, verified `main` | **`ff13c49ce2535992c7216f5742946b33bd805e53`** (normal merge commit, no squash/rebase) |
| [Private exact-head acceptance comment](https://github.com/maff0000/paper-bots/pull/5#issuecomment-6682357727) | Accepted only the bounded in-process path |
| [Public governance PR #9](https://github.com/maff0000/CGPT-INVESTMENT/pull/9) before this record | `5d669ebbdb3fdf9ff4f4be7034c0d4ca1690474f`, base `b0c8f55109fcc92d8f55ec7b593c696b9887475d` |
| Independent interpreter and full suite | Python **3.12.14**, **117 tests OK**, exit 0; GitHub exact HEAD reconstructed independently |
| Builder interpreter suites (not independently repeated) | Python 3.9.25: 117 OK; Python 3.12.3: 117 OK |
| Frozen QARP-ROTATION-001 v1.0.0 file SHA-256 | `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62` (unchanged; trade/stop authority NONE) |

## Independent adversarial evidence

The Architect reconstructed 80 source/test/fixture/schema files from exact private GitHub blob hashes and independently executed the full offline suite and a separate throwaway probe script. Rejected requests preserved both SQLite row count and hash tip.

| Probe | Verified result |
|---|---|
| E new write: `quality_state` object, list, bool, number, null, missing | Controlled `ValidationError`; no write |
| E replay: `quality_state` object, list, bool, number, null | Controlled `ValidationError`; no write |
| E exact replay | Idempotent duplicate; no write |
| S replay missing `parent_event_id` | `ValidationError`; no write |
| S replay contradictory `parent_event_hash` | `ValidationError`; no write |
| S replay forged `producer` role | `PermissionDenied`; no write |
| S replay diagnostic-only `note` | Duplicate; no write and no elevation |
| R replay changed accepted `quality_state` | `IdempotencyConflict`; no write |
| NEO review with object-valued `quality_state` | Controlled `ValidationError`; no write |
| Normal synthetic full chain | E→S→R→M→T→NEO, verified hash chain; T `NO_ORDER`, `order_created=false`, `is_fill=false`; NEO `NEO_REVIEW` only through this adapter |

Source inspection independently corroborated that the last correction adds a string type check before quality allowlist membership and reuses that validation for an explicitly provided NEO claim. Previous causal parent, semantic replay, role restrictions and `note` classification are preserved.

## Scope and limits of acceptance

Accepted: one offline, Python in-process, synthetic handoff through `paperbots.native_ingest`, with immutable evidence correlation and role checks, replay integrity, malformed-quality rejection and NEO read/review output. There were no vendor/broker/account calls during this audit.

**Not accepted / not demonstrated:** genuine native Grok Bot to Python transport, authenticated native sender identity, a separately protected ledger/NEO host principal or OS ACL, production source rights, live market universe, a scheduler, stop-dependent management, live trades or broker orders. A claimed producer or attested-ID function argument is not an actual platform security principal. Existing shared-user NEO handles may still write the historically allowed `NEO_REVIEW`, `NEO_COHORT` and `NEO_DISCOVERY_DIGEST` types; the ingest adapter itself only grants `NEO_REVIEW`.

G0 **OPEN**; provider rights **UNVERIFIED**; FMP remains exactly three historical calls, third HTTP 402, **no fourth call**; M-Bot/T-Bot stop-dependent functions **HOLD**; QARP entry/exit/stop doctrine authority **NONE**; no scheduler activation, new risk parameter, broker/account read, order or fill.

The earlier HOLDs of `553ec517455ce6ef797b049e65ec61389daa20da` ([REVIEW-M4-INDEP-001](2026-11-06-wo-paper-004-553ec5-independent-hold.md)) and `f4371c599fb1c45e28c403549090e92fd825ce67` ([REVIEW-M4-INDEP-002](2026-11-06-wo-paper-004-f4371c-independent-hold.md)) remain immutable correct findings for those *older exact heads*. This new ACCEPT applies only to `541f3f17`.

## Next bounded increment

Plan the real native-to-ledger delivery bridge and hard security boundary as a separate work order; discover the available native app identity and messaging hooks, require verifiable sender provenance, design a separately privileged ledger writer and protected NEO review access, and retain fail-closed behaviour. No live bot probe, transport activation, vendor call or scheduling without a separately approved scope/gate. Keep GitHub and exact-head independent audit canonical.
