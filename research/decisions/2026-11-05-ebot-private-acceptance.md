# G0-EBOT-002 — Private manual E-Bot v0.1 accepted
**Date:** 2026-11-05 (Europe/London) | **Authority:** independent Investment Research Architect acceptance of a narrowly bounded private tool | **Scope:** software acceptance only; G0 remains OPEN.

## Decision and provenance
- A separate **private** E-Bot repository was verified; only standalone read-only code, tests and redacted operator instructions were admitted. The earlier public source-copy [PR #1](https://github.com/maff0000/CGPT-INVESTMENT/pull/1) was **closed without merging**. The public investment journal remains research/evidence only, with no executable E-Bot package admitted to `main`.
- The private correction PR was independently reviewed at head `7bc39bebf039804eed26129054988e5761632873`, then merged by a normal merge commit `50c0b66247498672b84e9fcae7e417a538a0e5c1`. The private `main` head and corrected file were read back successfully.
- The review copy's 26 files matched their GitHub blob hashes. An independent offline run completed **75 unit tests** successfully. Additional adversarial probes gave **18/18 correct HOLDs** for non-finite timestamp and OHLCV fields, and **2/2 correct pivot/price-source boundary results**. No key or live vendor request was used in the Architect review.
- The implementation is a deterministic manually invoked, allowlist-only five-GET Massive data check with private key handling, fail-closed validation and redacted diagnostics. The accepted human-facing name is **E-Bot**; the Python command/package identifier is `ebot`. It is **not** an investment selection agent or a broker.

## Prior credentialed trial (operator-reported, not independently replayed)
The operator separately reported **five successful read-only requests**, with **318 complete daily bars for each of XOM, LIN, EQIX and SPY** from 2025-08-01 through 2026-11-04, no invalid or duplicate records and 11 weekday gaps corresponding to exchange holidays. The 329 inclusive weekdays minus eleven closures is consistent with 318 sessions. Split adjustment was requested; dividends are **not** adjusted in the supplier's aggregate convention. This is evidence of reported access and sample coverage, not a second-source reconciliation, validated chart signal, licence sign-off or guaranteed data completeness. Only count/date metadata is recorded here, no raw vendor bar or credential.

## Deliberate v0.1 limitations
- Enforces at most **five requests per one-shot run** but does **not** automatically enforce the full one-minute gap between separate invocations. Operator must wait at least one minute; no scheduler, retry loop or unattended invocations are authorised. A cross-run throttle requires a new approval before any automation.
- Exchange holidays are manually classified; this tool has no official exchange-calendar engine and performs no dividend-adjustment, Finviz A/B/C screens, 10/40 contraction, SMA/chart classification or investment valuation.
- The key and any vendor returns remain outside the public repository. External credential-store and workstation access controls are operator-reported, not independently attested in this review.
- The original public reference probe's known fail-success path remains a historical audit finding; acceptance applies **only to the separate private E-Bot implementation**, not to that reference script.

## Gates unchanged
**G0 OPEN, G1 NOT STARTED, G2/G3 NOT STARTED, G4 BLOCKED.** D1 provider contract/commercial-use rights, D3 a second independently licensed close source, D4 independent indicator/chart calculations, D5 contemporaneous Finviz A/B/C, and D6 reviewer reconciliation/specification freeze remain outstanding. The separate Monday all-sector research task continues as research-only; weekday automated scout remains paused. No broker, autonomous investment agent, standing trade or purchase authorisation follows from this merge.

**Next bounded step:** verify permitted intended use and select an authorised independent EOD comparator for a manual D3 close/adjustment study using the accepted `<= $1.00 PRICE_OK`, `> $1.00 PRICE_CHECK` and separate `SIGNAL_AMBIGUOUS` rule. No additional live vendor call has been approved in this decision.
