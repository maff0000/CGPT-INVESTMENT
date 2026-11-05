# STOP-RULE-RECOVERY-002 — recover legacy doctrines without adopting either
**Date:** 2026-11-05, Europe/London | **Owner:** Matt | **Architect decision:** bounded read-only recovery approved
**Source of initial discrepancy:** GrokBot Stream C operator report; original Redis text and July document have not yet been independently inspected in this decision record.
**Tracking:** [GitHub issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5)
**Current authority:** PAPER/SHADOW development only; all stop-dependent manager/execution decisions remain HOLD.

## Reported conflicting legacy material
1. GrokBot says the May 22 Trade doctrine v2.0 exists in Trinity's Redis, while GitHub contains only a summary of −25% hard stop, +50% and +100% trims, and an unspecified vol-band trail.
2. GrokBot says a July Sniper-OS brief instead uses a 4% stop and >=3:1 reward-to-risk, with 1.5×–2× ATR trailing only *proposed*.
3. Neither summary has complete provenance, strategy/horizon applicability or exact moving-stop specification in the current equity programme. Treat them as historical candidate evidence, not selected rules. Do not mix the percentages, infer missing parameters, or claim either is owner-approved for E/S/R/M/T/NEO.

## Decision
**Recover first, approve later.** GrokBot may retrieve exactly the full named May doctrine from Trinity Redis and the full July Sniper-OS brief **read-only**, without Redis dumps, changes to source systems, keys, other trading controls or live operations. Examine and preserve complete relevant historical originals privately only after checking for credentials, account data, personally sensitive information and licensed restrictions. Public GitHub receives only a sanitised dated comparison, evidence identifiers, implications and unresolved questions—not raw Redis material.

The output is a side-by-side matrix: intended strategy, instruments, holding horizon, entry, risk/sizing, initial SL, trailing rule formula and triggers, scale-out/trim, exit, gaps and event handling, time-of-observation, version and evidence of approval. Unknowns stay UNKNOWN. Grok should actively challenge both legacy designs and may recommend superior paper-trading alternatives with written rationale.

Prepare **proposed Equities Trading Doctrine v1.0** with separate rules per materially different equity strategy/horizon, using explicit testable parameters and safety states. This proposed version is NOT canonical until Matt and the Architect approve it in a dated decision. No adoption by default. Real-money trading remains entirely unauthorised.

## Concurrency and boundaries
- Continue E-Bot G0-D3 repair, E-Bot discovery/FMP checks, S-Bot strategy matching, R-Bot skeptical research, NEO append-only ledger/reporting and T-Bot **simulator infrastructure** using fixtures.
- Do not run M-Bot or T-Bot **stop-dependent synthetic entry/exit management** against guessed parameters. Demonstrate HOLD/no-trade and deterministic policy validation with fixtures until approved rule version exists.
- Preserve source privacy: full historical text only in appropriate private repository/data store with exact path/SHA and audit, not public CGPT-INVESTMENT. If the text contains unsafe material that cannot be safely copied, use a redacted private extract and report the limitation.
- One consolidated GitHub packet and one owner decision later; do not stop independent paper-build streams or request piecemeal approvals.

## Acceptance
Owner/Architect chooses the strategy-specific doctrine version after reviewing full recovered historical sources and Grok's comparative analysis. Record exact policy SHA, risk/stop version, test cases and affected work orders before unblocking simulated stop management. Until then the relevant M/T path is HOLD.
