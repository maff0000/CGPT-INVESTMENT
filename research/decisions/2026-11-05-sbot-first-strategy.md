# SBOT-STRATEGY-001 — adopt the original QARP screen as S-Bot's first strategy
**Date:** 2026-11-05 (Europe/London) | **Sponsor:** Matt | **Architect decision:** adopt for PAPER/SHADOW S-Bot screening only.
**Strategy:** **QARP-ROTATION-001 v1.0.0** | **Canonical spec:** [S-Bot strategy registry](../../docs/sbot-strategy-registry.md) | **Prior accepted research:** [Finviz Discovery v2](../../docs/finviz-filters.md).

## Choice and rationale
Matt proposed the original stock-screening requirements or a fair-value-centred (possibly "FVAQ") strategy, and asked for a consistently designed interface so that further strategies can be added and NEO can compare their success. **Select the original QARP Discovery v2 A/B/C as strategy #1.** It already has explicit adopted numerical criteria and preserves the research approach (quality at a reasonable price + improving momentum + sector rotation). This is the shortest honest path to an evidence-producing six-bot paper system. It is *not* yet a proven edge, nor an automatically executable entry strategy.

A fair-value-led compounder strategy is attractive but cannot honestly be marked production-specified before its financial definition (after-capex cash flow, discounting or return assumptions, capital intensity, industry-specific treatments, margin-of-safety thresholds and horizon) is fixed. Register it as a **PROPOSED follow-on**, not as silently changed v1 predicates.

## Approved implementation boundary
- The exact A/B/C Finviz v2 predicates, including Exchange/Country = Any and every unspecified filter = Any, are frozen as **QARP-ROTATION-001 v1.0.0**. Provider mappings that do not faithfully reproduce Finviz must be labelled proxy/unknown, never exact by assertion.
- E-Bot may present **as many genuinely credible candidates as it finds**, with no arbitrary score or candidate ceiling. S-Bot must label each confirmed pass/near-miss/unknown/rejection; admitted premium/near-miss research exceptions never become fake A/B/C passes.
- S-Bot emits explainable screening/strategy qualification separately from chart WATCH/COILING/AT PIVOT/BREAKING OUT/IN TREND classification, valuation, R-Bot news/macro/earnings, M-Bot setup and deterministic T-Bot simulator eligibility. No screen pass alone means BUY or TRADE.
- Every scored observation contains stable strategy ID, immutable version/ruleset digest, as-of, provider + adjustment provenance, per-predicate result and reasons. NEO must receive positives, negatives, unknowns, misses, zero-signal cohorts and later real-world outcomes without hindsight contamination.
- Grok may choose an efficient native strategy engine and append-only event implementation, and challenge decisions in dated private ADRs with public sanitised summaries. It must not alter approved numerical screen semantics, trading permissions, stop policy or source rights without an explicit new version/decision.
- This decision **does not resolve STOP-RULE-RECOVERY-002**. Initial entries, protective stops, trailing-stop changes and paper position management dependent on them stay HOLD until an accepted strategy-specific trading doctrine exists. Independent mocked integration work continues.

## Acceptance and learning
Grok delivers repeatable fixtures showing exact v2 A/B/C membership and C ⊆ B ⊆ A at equal observation cutoffs; missing/stale/contradictory inputs become UNKNOWN, and a one-source fallback is reviewable but blocks automated paper-entry permission where required. NEO can reproduce every classification and outcomes by original version, compare against matched sector and SPY, and explicitly distinguish screening hit-rate from trade P&L or strategy alpha. No self-rewriting of old outcomes.

**Ownership of future changes:** Matt and CGPT Architect review objective NEO evidence and approve a new version before changed strategy rules become canonical. Grok owns technical implementation and milestone PRs, no silent merges.
