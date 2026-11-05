# PAPER-SYSTEM-001 — GitHub continuity and coordinated shadow trading
**Recorded:** 2026-11-05 (Europe/London)
**Decision owner:** Matt (project sponsor)
**Status:** Owner direction accepted for governance and planning; paper-only construction may be specified in bounded work orders. No new bot beyond E-Bot has been implemented or independently accepted.
**Supersedes only:** the blanket hold on preparation of research/paper agent components under VALIDATION-FIRST-001, once each bounded work order is approved. The original G0 data acceptance and G1–G3 prospective proof still apply to performance claims. Live trading authority remains entirely absent.

## Sponsor direction and reasons
1. **GitHub is the authoritative, permanent handoff record.** Every substantive owner decision, rationale, requirement change, implementation/evidence result, blocker, acceptance, and next action must be added to GitHub during the same working increment. README, AGENTS and CURRENT-STATE should point to the latest record. Verify exact remote main HEAD before any change and the final commit or PR SHA after. An unmerged PR is proposed work, never accepted main. If GitHub cannot be updated, report the failure and do not pretend the decision has been persisted. This is a mandatory working rule, not an aspiration.
2. **Broad credible discovery, no arbitrary output ceiling.** E-Bot should produce every evidence-qualified lead rather than cap returns at the weekly >=7 research minimum. Separate broad leads from genuinely qualified candidates, record every rejection and no-signal run, deduplicate, rank an accessible digest, preserve underlying full ledger.
3. **Build the cooperating components now rather than wait for proof of investment alpha.** Implement in small bounded increments with integrated contracts and offline/paper testing; do not assume that working code proves predictive utility.
4. **Entire initial operating phase is paper/shadow only.** Autonomous simulated research, proposals, simulated entries/exits, stop updates and reconciliation may be developed after deterministic safeguards and specific work-order acceptance. Independently investigate candidates and compare human reviews to bot decisions prospectively, including false positives, missed winners and hypothetical costs. No real-account orders or discretionary investment authority.
5. **Internal, personal use only.** Vendor rights and plan permissions still require review. The public GitHub journal must not publish raw vendor data, credentials, actual account holdings, personal transactions or private order tickets.
6. **FMP added as candidate discovery/reference provider for a small entitlement trial**, not accepted as a reliable full-universe feed or intraday source. Test which Stable API endpoints, limits and licences actually apply before treating it as a production source; Massive/IBKR reconciliation remains a separate unmerged E-Bot PR #2.

## Recommended responsibilities (M-Bot decision pending explicit sign-off)
- **E-Bot — Explorer:** provider ingestion, data quality, sector/industry discovery, all credible lead packets and complete discovery ledger. No strategies, risk sign-offs, orders or broker writes.
- **S-Bot — Strategist:** match evidence against owner-approved, versioned strategy registry (QARP rotation, pre-breakout, trend, quality compounder, etc. only after exact entry/exclusion rules are frozen). May assign multiple strategies; cannot silently invent or modify rules.
- **R-Bot — Skeptic:** independent news/filing/earnings, macro and investment-risk challenge; at least two disconfirming theses, point-in-time observations, PASS/HOLD/REJECT with reasons. Never grants broker authority.
- **M-Bot — Manager (Architect recommendation):** isolated paper portfolio and decision coordinator; compare S/R recommendations, produce signed-equivalent synthetic paper intent with planned entry, initial stop, stop progression, exit/invalidation, exposure and attribution. May act as a *shadow* investment committee in paper only; cannot change approved strategy or risk limits, cannot approve live tickets.
- **T-Bot — Trader:** deterministic paper-order adapter and simulated fills, order lifecycle, replacement/cancel and position reconciliation; does not choose strategies, change stops without validated M-Bot instructions or route real orders. A separate deterministic risk controller must veto any noncompliant synthetic intent before T-Bot.
- **Matt and Research Architect:** independently inspect evidence, compare outcomes and approve rule changes. Not required in the paper order loop once its limited permissions and test gates pass; they retain all future live-trading authority.

## Critical unresolved stop / entry specification — STOP-RULE-RECOVERY-001
The owner reports that a previous GitHub record already defined entry, exit, initial stop loss and a moving/trailing-stop process. **The current CGPT-INVESTMENT main documents high-level execution guards, generic staged entries and stop conditions, but inspection has not located an exact, authorised numerical or state-machine trailing-stop algorithm.** Do not infer a percentage, ATR multiple, breakeven threshold, pivot rule, move-to-profit cadence or order-replacement semantics.

Before M-Bot or T-Bot is allowed to simulate managed entries and moving stops, locate the canonical record and record the exact source path and version, or ask the owner to re-approve a fresh explicit definition. Freeze strategy-specific rules for: eligible setup, signal time, entry trigger/limit, initial protective stop, maximum per-position and daily risk, stop move triggers, whether a stop can widen (default NO), partial fills, take-profit/time exits, overnight gaps, corporate actions, holidays, stale feed, broker/adapter failures, cancel/replace/idempotency and manual override. Model slippage, spreads and transaction costs. All ambiguous fields => HOLD.

## Paper-only amendment to validation gates
- **G0 remains OPEN.** Source fidelity, licences, universe, completed-vs-intraday observations and exact strategy/stop contracts must be checked and versioned; do not claim full source acceptance.
- **G4-P (new, paper development only):** authorise drafting *bounded, auditable work orders* to build and integrate E/S/R/M/T with a no-live-order guarantee. Separate each component's permissions, mocked services and evidence. This is not permission to turn on a scheduler, connect new broker-writing credentials or open positions without specific acceptance.
- **G1–G3 remain mandatory PROSPECTIVE research validation.** A paper fill/reconciliation test is operational proof, not proof of strategy alpha. Preserve timestamped cohorts, blind human comparison, misses, costs and macro-blind baseline.
- **G4-L (live execution): NOT AUTHORISED.** Requires separate architecture, account suitability, independent security/risk audit, explicit owner approval, deterministic live order controls and a new go/no-go. No paper testing can silently promote itself to live.
- Existing E-Bot private PR #2 (G0-D3), current head at this record: 9b843dee03892e73f29da31997e5d07bfed564a7, remains UNMERGED / acceptance pending. Do not silently merge it as part of this documentation change.

## Work sequence
1. Architect reviews E-Bot PR #2 at its latest exact head; accept/merge only after independent evidence review.
2. Small read-only FMP Stable API entitlement/universe/screener trial with strict call cap, key isolation and no public raw data.
3. Recover/freeze exact ENTRY / EXIT / INITIAL STOP / MOVING STOP contract; record unresolved points rather than inventing them.
4. Agree immutable inter-bot candidate, strategy, risk, synthetic order and fill event schemas, role permissions and paper-only kill switch.
5. Use bounded WOs to implement all five collaborating roles in parallel where interfaces are stable, then run integrated synthetic end-to-end tests (including bad news, stale prices, source unavailable, earnings veto, invalid stop, duplicate order, partial fill, gap and outage). No broker live connector.
6. Authorise controlled scheduled **research/paper** trial separately after operational acceptance; run human shadow reviews and forward outcomes. Preserve every candidate, reject, HOLD and synthetic fill in restricted data storage; publish only sanitised summaries and dated decisions.
7. Revisit live-trading permissions only as a separate future decision.

## Handoff / acceptance status
- Agreed: GitHub-as-truth, broad discovery, coherent multi-bot paper/shadow build priority, internal personal use, no current live trading.
- Architect recommendation, not yet final owner sign-off: separate M-Bot instead of putting discretionary paper management inside T-Bot.
- Unresolved: exact stop algorithm record; individual strategy thresholds; FMP endpoint entitlements and intraday quote rights; broker paper account verification; E-Bot PR #2 acceptance; stage-by-stage operational tests.
- All prior dated evidence remains historically true at its recorded time; this amendment changes **future paper development authority only**, not past status or evidence.
