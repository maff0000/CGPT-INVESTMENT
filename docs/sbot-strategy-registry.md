# S-Bot strategy registry — paper research, versioned and auditable
**Decision:** [SBOT-STRATEGY-001](../research/decisions/2026-11-05-sbot-first-strategy.md) (2026-11-05) | **Status:** **QARP-ROTATION-001 v1.0.0 APPROVED for PAPER screening implementation**, not live trading or paper-order admission.
**Research inputs:** [Finviz QARP Discovery v2](finviz-filters.md), [chart model](chart-stage-classification.md), [validation charter](research-process-validation-charter.md), [Grok delivery roadmap](equity-paper-delivery-roadmap.md).

## Registry
| Strategy ID | Version | Purpose | Status | Entry / exit / stop authority |
|---|---|---|---|---|
| **QARP-ROTATION-001** | **1.0.0** | Broad quality/valuation eligibility plus staged momentum A/B/C, and sector-aware research | **APPROVED for S-Bot paper screening** | **NONE — HOLD on stop-dependent M/T paths** |
| **FAIR-VALUE-COMPOUNDER-002** | not assigned | Cash-flow valuation, margin of safety, durable compounding; user shorthand "FVAQ" not yet defined | **PROPOSED ONLY** | NONE |
| Future strategies | new stable ID/version | Hypotheses proposed with explicit predicates, horizons and evidence | NOT APPROVED | NONE by default |

**Rule immutability:** stable ID + semantic version + canonical rule manifest SHA, effective date, responsible approver and exact input-definition version. Changed threshold, provider-equivalence or logic semantics requires a new version and dated decision; never reinterpret old ledgers or automatically promote experimental trials.

## QARP-ROTATION-001 v1.0.0 — frozen screen semantics
Use these exact v2 Finviz filter settings at a common observation cutoff. **Every unlisted filter is Any**. A/B/C memberships overlap by design; C ⊆ B ⊆ A where source and universe are the same. Do not count three memberships as three opportunities.

| Group | Finviz field | Exact setting |
|---|---|---|
| Descriptive | Exchange | **Any** |
| Descriptive | Country | **Any** |
| Descriptive | Market Cap. | **+Mid (over $2B)** |
| Descriptive | Price | **Over $10** |
| Descriptive | Average Volume | **Over 200K** |
| Descriptive | Sector | **Any** for all-sector; named sector for a sector-lane run |
| Fundamental | Forward P/E | **Under 25** |
| Fundamental | Price/Free Cash Flow | **Under 30** |
| Fundamental | Return on Invested Capital | **Over 10%** |
| Fundamental | LT Debt/Equity | **Under 1** |
| Fundamental | Operating Margin | **Over 5%** |
| Fundamental | Sales Growth TTM | **Positive** |
| Fundamental | EPS Growth Next Year | **Positive** |
| Technical: A | Performance / SMA50 / SMA200 | **Any / Any / Any** |
| Technical: B | Performance / SMA50 / SMA200 | **Month Up / Price above SMA50 / Any** |
| Technical: C | Performance / SMA50 / SMA200 | **Month Up / Price above SMA50 / Price above SMA200** |
| Technical: all variants | All other technical fields | **Any** |

**Source-mapping caution:** Finviz forward P/E, P/FCF, ROIC, momentum and SMA field definitions are not automatically equivalent to FMP, Massive, IBKR or independently computed fields. Per metric store provider, field provenance, as-of/freshness, exact-match/proxy/unknown interpretation and actual Finviz comparison when available. A proxy may rank an idea but must not claim verified Finviz A/B/C membership. Do not assume any provider has full worldwide coverage because Finviz Exchange/Country filters say Any; record universe shortfalls and licences.

## Separate outputs — not one verdict
1. **Universe:** E-Bot presents all credible names, deduplicated and preserving unselected/rejected/zero-signal cohorts. No arbitrary seven-candidate cap; the existing seven-plus weekly research objective is a *minimum output target*, not a bot limit or trading quota.
2. **Screen:** S-Bot records confirmed A/B/C matches; separately **QUALIFIED_NEAR_MISS**, **PREMIUM_EXCEPTION**, **NON_MATCH**, **UNKNOWN** and **UNSUPPORTED** as appropriate. For every candidate, persist each attempted predicate, observed value, definition, timestamp, pass/fail/unknown, source, exception rationale and missing fields. A one-field miss never becomes a silent pass.
3. **Chart:** classify independently from current, completed data into **BREAKING OUT**, **IN TREND**, **WATCH** with WATCH substate BASE FORMING / COILING / AT PIVOT; **CHART PENDING** when unverified. A chart classification is not the screen class.
4. **Research proposal:** independently investigate company financial quality and fair value; record sector/industry, current leadership/strength, risk-adjusted opportunity and human research priority. Screen, chart and investment verdict are different evidence fields. R-Bot independently applies earnings/macro/news skepticism and contrary cases.
5. **Entry management:** **M-Bot/T-Bot may not infer entry/stop/size/trail permission from this screen**, even at PRICE_OK and a confirmed breakout. Stop-dependent automated PAPER trade paths stay HOLD pending exact documented rules and gate acceptance.

## Strategy/NEO evidence contract (logical requirements, Grok chooses wire format)
Emit immutable linked observations in a **shared private append-only causal event ledger** with role/bot, strategy ID, version/manifest SHA, run ID, candidate/instrument identity, sector/industry, research lane, provider/licence classification, data-adjustment policy, observation timestamp (UTC and exchange session), ingested timestamp, source IDs, rule-by-rule assessment, Finviz A/B/C status, exception/rejection reasons, chart stage, handoff/veto state, and preceding-event correlation. Per-bot operational logs supplement the ledger; they are **not** NEO's canonical evidence.

- Every event references the **information available at the decision time**. Missing/stale data, source failure, ambiguous pivot, price mismatch and permission failure produce their own reason codes, never manufactured estimates or a suppressed row. G0 single-source fallback remains reviewable as UNCHECKED but blocks paper-entry authorisation.
- Record all screened-in, screened-out, qualified exceptions, R-Bot vetoes, unused candidates, no-signal days and changes in classification, including delisted/corporate-action cases where the source allows. No survivorship or winner-only selection.
- NEO computes *prospective*, frozen-cohort 5/20/60 completed-exchange-session observations (approximately 1/4/12 weeks), matched SPY and sector comparisons, failures, drawdowns, false positives, false negatives and research workload. Specify price return versus dividend-inclusive total return and available split/FX/cost adjustments; where unavailable, result = UNKNOWN/INCOMPLETE, never implied total-return precision.
- Keep **screen predictive utility** separate from **hypothetical trade profit**: net paper P&L requires separately accepted entry, fill, exit, stop, fees/slippage and an observable next-price clock. No look-ahead, same-close fills from after-close signals, synthetic live-return claims, backtested-edge claims, retroactive cohort edits or self-authorised strategy rewrites.
- NEO reports to Matt/Architect via private full evidence and **sanitised GitHub milestone/daily/weekly summaries** with exact code and strategy SHAs, cohort counts, uncertainty, competing explanations and proposals. Changes require a dated Architect/owner approval and new version. Until evidence accumulates, report measurements, not claimed alpha.

## Grok implementation and tests
Build a generic registry evaluator and event schema; select engine/scheduler/storage suited to the platform and record material changes in private ADRs. Provide deterministic offline fixtures for A-only, B, C, one boundary per numerical cutoff, UNKNOWN metrics, stale/mismapped provider, unsupported instrument, explicit near-miss, zero-candidate run, no-duplicate identities, C ⊆ B ⊆ A, chart != screen != action, and NEO evidence linking. A raw provider source outage must not erase surviving valid source research; only approved risk gates can permit a simulated entry, and the unresolved stop policy blocks those dependent pathways. Keep live broker writes disabled.

**Delivery:** one GitHub milestone PR with WO, exact base/head, changed paths, test/independent audit evidence, limited source licences, denial cases, sample sanitised ledger event and NEO output, open risks and a requested Architect ACCEPT/HOLD decision. Do not merge your own milestone PR.
