# Data provenance and public-content policy
## Evidence labels
| Label | Definition |
|---|---|
| VERIFIED | A specific claim checked against an identified source, with date, relevant period and retrieval timestamp |
| REPORTED | A historical observation supplied from prior research; not independently checked in this repository |
| PROVISIONAL | An interpretation or working thesis, with evidence still incomplete |
| UNKNOWN | Missing or unresolved; never treat as zero, false or pass |
| PROPOSED | A new rule or parameter awaiting adoption/testing |

Verification is claim-specific. Verifying a source exists does not verify every claim attributed to it. A historical fact can be verified yet stale for a current decision.

## Source hierarchy
Use company filings and investor-relations releases for reported results and confirmed earnings schedules. Use reliable market-data sources for prices, volumes and screen fields, with their definitions and delays. Treat estimates as estimates, separate from realised results. Secondary calendars help discover events; primary announcements confirm them.

For each claim record source ID, direct URL, publisher, publication timestamp if available, retrieval timestamp with timezone, observation/as-of time, fiscal period, currency/units, raw metric versus calculation, and verification status. Unknown timestamps must say UNKNOWN, never invented. Record conflicting sources and the unresolved impact.

## Founding history
The supplied discussion establishes process intent and the original candidates. It does not independently verify its assistant-generated market figures or company claims. Preserve concise research summaries rather than copying private transcripts. Missing original URLs cannot be reconstructed from domain labels. The register in [2026-11-03 sources](../research/sources/2026-11-03.md) records this limitation.

## Corrections and freshness
Append a dated correction linking the original record, wrong claim, replacement evidence and effect on the decision. Do not silently restate historic snapshots using later knowledge. Refresh screen/market evidence each review and earnings timing on the day of entry review. A delayed or conflicting input can block a decision.

## Public data minimisation
Exclude personal names beyond unavoidable public repository identity, contact details, private chat links/IDs, account/portfolio information, credentials, local filesystem paths and private documents. Cite public primary evidence and publish concise facts/analysis only; public availability does not imply a licence to redistribute datasets or full reports. Keep trading records outside this public research repository.

See [source template](../templates/source-record.md) and [outcome rules](outcome-tracking.md).
