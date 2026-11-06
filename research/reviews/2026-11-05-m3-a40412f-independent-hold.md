# M3 independent exact-head audit — HOLD

**ID:** REVIEW-M3-INDEP-001  
**Date:** 2026-11-05 (Europe/London)  
**Architect decision:** **HOLD** — implementation and milestone PRs remain open; no merge or operational approval.

## Exact-head verification

| Item | Verified SHA / status |
|---|---|
| [Private paper-bots PR #4](https://github.com/maff0000/paper-bots/pull/4) | HEAD `a40412f0876fd59526a6b663273f69b4df008ec4`; base `76dd4f9805c8b7d0ed6194cdb118c5096ab6d79d`; OPEN/UNMERGED |
| [Public governance PR #8](https://github.com/maff0000/CGPT-INVESTMENT/pull/8) | Reviewed initial HEAD `e2306a1f57b670382d31b22e5d002556b7b88858`; base `20094068e20c2de0a659e8243657207c8d4cfbaa`; OPEN/UNMERGED |
| Synthetic offline tests | Independently reconstructed and executed **91/91 OK**, Python **3.12.14**; Python 3.9 and 3.12.3 counts remain **builder-reported**, not repeated by Architect |
| Frozen QARP | Strategy manifest SHA-256 matched `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`; no strategy changes accepted |

No vendor, exchange, broker, account, live-data, order or scheduler calls were made during this independent review.

## Four reproducible defects

All examples below modify only a copy of the synthetic fixture and call `paperbots.discovery.prepare.prepare`. All are observable at the exact PR head. See [the private PR #4 corrective comment](https://github.com/maff0000/paper-bots/pull/4#issuecomment-6670496212) for bounded instructions.

1. **Contradictory duplicate source observations are silently collapsed.** Two rows for one synthetic instrument agree on metrics but one says source A PRESENT and the other says source A FAILED; source B PRESENT. Dedup keeps the first source A and returns `ADMITTED`. Conflict is lost and reliability overstated. Reproduce in both input orders.
2. **OTC listing can be admitted.** A synthetic row marked `listing: OTC` but `exclusion: null` returns `ADMITTED` even though OTC is an expressly excluded universe class. Listing and exclusion annotations need consistent validation.
3. **Stale sources can be admitted as current.** Two PRESENT sources dated `2020-01-01` paired with a later fixture as-of date still yield `ADMITTED`. Define and test a conservative fixture freshness/alignment rule. This is not a live-feed freshness specification.
4. **Wrong source-entry type causes a raw exception.** Setting a synthetic row's `sources` to an array containing text causes `AttributeError`, not a deliberate typed validation/fail-closed result. Rejected preflight must not partially write the ledger.

These defects were not covered by the 91 passing tests. They are classification/integrity blockers even though the simulated automated path stays BLOCKED.

## Native Grok teammates: evidence boundary

The 14-item packet documents six individually addressable identities and bounded **operator-/parent-reported synthetic chat handoff**, which is useful progress. The Architect's code-level inspection of the Python package does **not** independently prove platform identity security, a protected read-only NEO principal, native-message-to-Python-ledger execution or a real US equity universe. The platform reportedly shares one user's computer/files/connectors across bot personas. Treat persona refusals and producer IDs as claims, not hard access control. Native-to-ledger bridge, protected NEO isolation and provider entitlements remain **UNVERIFIED**.

## Authorised correction and next gate

GrokBot may complete **one bounded correction round** on existing private PR #4, adding regression tests for contradictory source dedup in both orders, listing/exclusion conflicts, stale or malformed timestamps, malformed source entry types, unchanged ledger on failed preflight, and preserving valid single-source `UNCHECKED` fallbacks. Record deviations, changed paths, exact heads/bases and test evidence in PR #4 and governance PR #8. Return for independent exact-head review; do not self-merge.

**Persistent gates:** G0 OPEN; FMP/Finviz/provider rights UNVERIFIED; real universe and operational cadence UNVERIFIED; May text unavailable; entry/exit/initial stop/trailing-stop/sizing policy not approved; stop-dependent M/T HOLD; live broker actions and scheduler activation NOT AUTHORISED.

This review supersedes the earlier `READY FOR ARCHITECT REVIEW` status for **these exact heads only**. It does not supersede accepted main or erase historical builder records.
