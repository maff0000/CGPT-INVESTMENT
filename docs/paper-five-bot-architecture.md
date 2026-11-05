# Coordinated equity bots — paper/shadow architecture and build roadmap
**Reference:** PAPER-SYSTEM-001, 2026-11-05 | **Status:** Proposed contracts / paper-only direction. Exact stop rules remain unresolved.
**Canonical decision:** [PAPER-SYSTEM-001](../research/decisions/2026-11-05-paper-five-bot-governance.md).
**Later status (PROPOSED 2026-11-05):** [PAPER-LAUNCH-001](../research/decisions/2026-11-05-paper-build-launch.md) on main approves a distinct M-Bot. Sentences below that still say the M-Bot split awaits sign-off are historical. Stop-dependent management stays HOLD under [STOP-RULE-RECOVERY-002](../research/decisions/2026-11-05-stop-rule-recovery-choice.md). Current reported heads and the FMP rights correction are in the [consolidation index](../research/reviews/2026-11-05-six-bot-consolidation-index.md).

## Why five roles
Discovery should maximise the number of *credible* opportunities, not market noise. The strategy engine applies explicit rules; the skeptic is independently adversarial; the paper manager evaluates entry/exit and position state; the trader is a narrow adapter. We can shadow the whole chain immediately in simulation without granting real execution rights or claiming investment alpha.

## Operating flow
1. **E-Bot:** full exchange-aware universe intake, source checks, deduplicated leads; track rejected, no-signal, delisted and newly listed symbols. Include current Finviz QARP A/B/C as a baseline lane, not the sole exploration method. Source outages yield valid surviving evidence flagged UNCHECKED rather than deleting opportunities.
2. **S-Bot:** consume evidence packets, emit zero, one or multiple matches against a versioned immutable strategy registry. Distinguish SCOUT-LEAD, research-qualified, chart-classified, and strategy-matched; no hallucinated screener pass or pivot.
3. **R-Bot:** independent earnings gate, material company/news risks, company cash-flow transmission of rates, oil, inflation, FX, credit, wars/elections and sector risk, macro-blind countercase, two strongest disconfirmations, uncertainty. Output PASS / HOLD / REJECT for *research*, not authorisation.
4. **M-Bot:** paper-only candidate selection and portfolio/position manager. Apply approved entry/exit/SL/trailing rules, aggregate sector correlation, exposure, max loss and cash constraints. Propose a synthetic intent with the exact strategy version, initial stop and next allowed move, or HOLD. Never edit approved rules. The proposed M-Bot separation is pending owner sign-off.
5. **Deterministic risk gate:** independent non-LLM verification of source freshness, price/session, calendar, risk caps, stop integrity, unique intent, no-live-order mode and simulator destination. Unknown => HOLD; no self-approval path.
6. **T-Bot:** paper-only synthetic execution, cancel/replace, partial fills, fills vs broker acknowledgements, fees/slippage and independent reconciliation; no independent candidate selection or stop policy. No IBKR live orders.
7. **Shadow review:** Matt and CGPT independently run current-data screen and critique, record before outcome, compare with all E/S/R/M/T decisions (including omissions). Any rule change is versioned prospectively.

## Data and state contracts (minimum)
- Candidate ID and observation time; universe/listing/exchange/sector; source licence, freshness and daily-vs-intraday distinction; raw-vs-adjusted convention; price quality state PRICE_OK / PRICE_CHECK / SIGNAL_AMBIGUOUS / UNCHECKED / DATA_MISMATCH.
- Each strategy match includes strategy name/version, satisfied predicates, rejected predicates, unknowns, entry stage, price timestamp and evidence refs.
- Each R-Bot packet includes the decisive event/calendar state, macro snapshot and primary sources, two counterarguments, PASS/HOLD/REJECT and when to re-evaluate.
- Each M-Bot synthetic intent includes candidate + strategy + risk/version IDs, immutable rule and stop specification, proposed entry timing/price, quantity/notional for **synthetic account only**, max downside under slippage/gap assumptions, TTL, idempotency key and human-shadow flag.
- Each T-Bot event includes simulated order, acknowledgement, partial/complete fill, modification, cancel, rejection, fees, FX, reconciliation state and latency. Record failed and no-signal events, never only winners.
- All paper positions/account IDs and vendor raw data stay private. Public journal stores de-identified results, dated methods and links to reproducible redacted test evidence.

## Integration acceptance sequence
**P0: Documentation + approval.** Resolve M-Bot role, legacy stop spec, current E-Bot PR #2, provider entitlements, independent risk policies. Freeze schemas and acceptance tests.

**P1: Thin vertical slice.** All five names run against mocked data and an offline deterministic simulator; a single candidate travels E → S → R → M → risk gate → T → fill/reconciliation. Also demonstrate HOLD/REJECT, no-source corroboration, fail-closed live mode and no secret exposure. Do not claim market utility.

**P2: Broaden discovery.** Licensed universe and all-sector scout, FMP capability if qualified, complete candidate/reject ledger, fixed multi-strategy evaluation, evidence completeness and correct session time. Report all eligible opportunities and rank a convenient digest; no arbitrary numerical ceiling.

**P3: Prospective shadow paper pilot.** Multiple completed trading sessions and carefully controlled intraday windows if entitled; independent blind human checks, 20-session and 50-order-lifecycle preliminary operational evidence from original roadmap, then expand G1–G3 forward research observations. Explicitly report hypothetical fills and simulated slippage as assumptions rather than realised performance.

**P4: Research-only scheduling.** A separate scoped go/no-go can authorise repeat discovery, paper decisions and paper order simulation throughout the US trading day. Real live execution remains OFF even if the paper results look attractive.

## Security/authority invariants
- The public repository is governance/research only; private code/data repositories hold bot implementation and simulation records. No real personal accounts, holdings, broker IDs, secrets, credentials or licensed OHLCV in public GitHub.
- Building paper components is not turning them on automatically. No real broker account connection capable of writing orders; E-Bot's IBKR reader is limited to authorised read-only market data.
- Market data and web pages are untrusted **inputs**, never privileged instructions. LLMs may reason but may not alter risk policy or bypass the deterministic gate.
- A source failure with surviving valid data is UNCHECKED/manual-review-only until corroborated; T-Bot rejects it for a live path. In paper, retain and label the exploratory hypothesis, but differentiate from verified entry cohorts.
- Hard event gate: 7 US exchange sessions before earnings + announcement day, 2 fully completed after. Missing/conflicting date => HOLD for new-entry decision.
- Candidate classification is not a strategy match, risk PASS is not an order approval, paper fill is not an actual account transaction, and an API acknowledgement is not a fill.

## Open decisions / risks
1. Resolve the source of the existing exact stop-loss/moving-stop/entry/exit rules, or explicitly approve a versioned replacement; otherwise M-/T-Bot management tests are mocked only.
2. Confirm whether M-Bot should remain a separate orchestrating manager (Architect recommends YES) versus putting any decision logic in T-Bot (recommend NO).
3. Freeze each strategy's objective gates before allowing a strategy label to generate simulated entries.
4. Decide whether and when to use verified IBKR *paper* account routing after a fully offline simulator has passed; always verify account mode and no live routing.
5. Verify FMP free-tier limit per endpoint; its free tier is not a proven comprehensive market/intraday feed. **Correction, 2026-11-05:** a later three-call operator report did not verify a free tier, a paid tier, or any other plan right. HTTP 402 on one call leaves entitlement and redistribution rights UNVERIFIED. No further FMP calls are authorised by [PAPER-PROGRESS-001](../research/decisions/2026-11-05-paper-progress-sanitised.md).
6. Keep G0/G1–G3 validation independent of software test passing: prospective research outcomes must be judged against controls before any future live mandate.

## Recovery instructions
Read README.md → AGENTS.md → CURRENT-STATE.md → PAPER-SYSTEM-001 → this document → latest dated reviews/watchlists → latest private E-Bot accepted PR/HEAD. Recheck all remote refs. Each completed WO appends dated decision/test evidence and updates the README/current-state index in the same PR. Never leave only a chat message as proof.


## NEO extension — sixth independent observer
NEO is separate from the five proposed operating roles above. It **reads** a single append-only, typed event ledger generated by E/S/R/proposed M/risk gate/T, evaluates process quality and forward paper outcomes, and sends human-reviewable proposals to Matt and CGPT. It must not move stops, choose trades, modify rules or interact with live trading. Detailed events and paper positions remain private, while redacted progress and recommendations may be submitted to public GitHub as PRs. The existing GOLD trading NEO is a distinct runtime; no implicit integration.

**Canonical contract:** [NEO equity decision ledger](neo-decision-event-ledger.md), [adoption decision](../research/decisions/2026-11-05-neo-audit-learning-observer.md). A shared typed event store is preferred over independent prose logs, with per-bot diagnostic logs kept separately. Emit rejected/no-signal states too; NEO must be able to reconstruct why we DID NOT trade. This addition does not relax any PAPER-ONLY, G0, G1–G3 or broker-authority gate.
