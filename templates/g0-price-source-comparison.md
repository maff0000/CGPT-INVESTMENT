# G0-DATA-002 — Manual EOD source comparison test
**Blank template, not evidence that a market data subscription or chart run exists.** Copy per session/provider and preserve raw provenance privately where licensed. Publish only permitted derived/source facts.

## Scope
- Sample date and actual US regular session: TBD
- Data provider / entitlement / licence and plan: TBD
- Endpoint/input and request time: TBD
- Raw vs split/dividend-adjusted convention: TBD
- Final correction cutoff and observation timestamp: TBD
- Second source / quote date/time and licence: TBD
- Next G0 reviewer and observed plan restrictions: TBD

## Price discrepancy checks
| Symbol | Listing / currency | Session | Provider A close | Provider B close | Absolute difference | Data aligned? | PRICE_OK or PRICE_CHECK | SIGNAL_AMBIGUOUS? | Provenance |
|---|---|---|---:|---:|---:|---|---|---|---|
| XOM | NYSE / USD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | UNVERIFIED | UNASSESSED | UNASSESSED | |
| LIN | NASDAQ / USD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | UNVERIFIED | UNASSESSED | UNASSESSED | |
| EQIX | NASDAQ / USD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | UNVERIFIED | UNASSESSED | UNASSESSED | |
| SPY | US / USD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | UNVERIFIED | UNASSESSED | UNASSESSED | |
| Two additional different-price stocks | TBD | TBD | UNKNOWN | UNKNOWN | UNKNOWN | UNVERIFIED | UNASSESSED | UNASSESSED | |

**Apply:** same listing, same regular session, same adjustment basis; **absolute difference <=$1.00 → PRICE_OK; >$1.00 → PRICE_CHECK**. Mismatched date/currency/split → DATA_MISMATCH regardless of difference. Pivot straddled → SIGNAL_AMBIGUOUS regardless of difference, not a routine PRICE_CHECK if <=$1.

## Completed-bar coverage and actual indicators
| Instrument | Count of completed bars | Duplicate/missing dates | SMA50/SMA200 and slopes verified | 10/prior-40 volatility | 10/prior-40 volume | 20–60 session base verified |
|---|---:|---|---|---|---|---|
| XOM | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| LIN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| EQIX | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| SPY | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

## Provider acceptance
- Licence permits this manual test and derived publication: YES / NO / UNKNOWN
- Provider corrections/delayed data documented and handled: YES / NO / UNKNOWN
- Finviz contemporaneous A/B/C evidence captured with same-day cutoff: YES / NO / UNKNOWN
- Corporate action continuity verified on at least one known split/dividend: YES / NO / UNKNOWN
- Two reviewer reconciliation for critical pivot judgement: YES / NO / UNKNOWN
- **D1–D6 conclusion:** ACCEPT / HOLD / REJECT, with exact evidence and failure reasons

**No future results or G1 outcomes may be backdated into the snapshot.** No vendor subscription, API key or personal holdings in public GitHub.
