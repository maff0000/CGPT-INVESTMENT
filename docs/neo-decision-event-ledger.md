# NEO equity-learning event ledger — AI-readable decision contract
**ID:** NEO-EVENT-001 | **Draft design adopted:** 2026-11-05 | **Scope:** internal personal-use US-equity paper/shadow system only.
**Decision:** [NEO-LEARNING-001](../research/decisions/2026-11-05-neo-audit-learning-observer.md).

## Architecture
Maintain **one canonical append-only, structured event stream** for decisions and state changes, with **per-bot diagnostic logs** used only for local health and faults. The event stream is the evidence NEO reconstructs; diagnostics are not independent competing decision histories. Use a private SQLite database in WAL mode behind one typed append interface for the first standalone paper deployment. Export deterministic JSONL snapshots with consistent high-water mark; do not depend on human-written prose or manual joins across separate files. Later PostgreSQL/event broker migration must preserve IDs and semantics.

Emit at decision time. Every event should be written regardless of PASS/HOLD/REJECT, no-signal day, missing source, ignored candidate, simulated order or failure. A retry must not duplicate a logical event. Producer identity and per-stage access are checked by the ingest service; bot code receives only the minimum capabilities it needs.

## Required common envelope
| Field | Purpose / validation |
|---|---|
| schema_version, event_type, event_id | Stable version, allowlisted type and globally unique immutable event ID |
| correlation_id, candidate_id, decision_id, parent_event_ids | Entire decision chain and exact parent lineage; require trace integrity |
| producer_bot, producer_version, model_version, rule_version | Authenticated author and exact software/model/strategy versions |
| observed_at_utc, produced_at_utc, market_session | When fact became knowable, when decision was made, exchange session; canonical UTC, no unlabelled local NOW() |
| source_as_of_utc, fetched_at_utc, source_id, entitlement_tag | Provenance; source release lag and free/paid rights without copying raw vendor response |
| input_ref_ids, input_hashes, output_hash | Immutably referenced inputs and decision output, not invented citations |
| quality_state, uncertainty, reason_codes | PRICE_OK / PRICE_CHECK / SIGNAL_AMBIGUOUS / UNCHECKED / INVALID_DATA / DATA_MISMATCH or appropriately typed stage states, explicit UNKNOWN |
| decision_action, rule_checks, short_explanation | Deterministic action token, pass/fail/unknown predicates and a bounded plain-language why |
| expires_at_utc, supersedes_event_id | TTL and correction/supersession through a NEW event; never edit past records |
| safety_mode, risk_gate_version | Explicit PAPER_ONLY invariant and checked deterministic gate version |

Only stage-relevant fields are required on each event, validated against a versioned schema. Do not fill unavailable values with zero, model guesses, the current wall clock, or post-event facts.

## Bot-specific event families
| Producer | Minimum emission | NEO questions |
|---|---|---|
| E-Bot | universe scan, qualified/rejected lead, data source and quality, score features, sector/event timestamp, no-signal cohort | What did discovery see or miss? Was the provider valid/late? |
| S-Bot | strategy match/non-match, criteria/version, thresholds, entry stage and counterexamples | Did a defined strategy really match, and with what contemporaneous evidence? |
| R-Bot | independent risk PASS/HOLD/REJECT, news and macro source stamps, event/earnings gate, at least two contrary arguments | Were risks identified in time? Was a veto justified? |
| M-Bot (proposed) | paper entry/no-trade proposal, simulated sizing, initial stop, each allowed trailing-stop move, thesis invalidation and exit under approved rule version | Was every entry/exit/SL transition authorised by the frozen paper rules? |
| Deterministic risk gate | PASS/BLOCK and each specific check's result, effective caps and fail-closed status | Was a hard limit bypassed, or did an unknown appropriately cause HOLD? |
| T-Bot | paper order ack, partial/full fill, rejection, cancel/replace, fees/spread/slippage and independent reconciliation | Did the fill actually occur in the simulator, and do positions reconcile? |
| NEO | retrospective review, hypothesis, evidence conflict, recommended experiment, decision/outcome split, confidence/unknown | Is the assessment reproducible and honest about hindsight? |
| Human shadow reviewer | parallel timestamped assessment, disagreement, disposition and rule-change approval | Did our manual review reach a different conclusion, and why? |

## NEO report — required sections
1. **Coverage:** period, market sessions and ledger high-water mark, candidates, rejected/missed and no-signal counts, evidence completeness, source-failure and version summary. Do not claim an unseen session was processed.
2. **Causal trade reconstruction:** decision IDs and exact E→S→R→M→risk→T event chain; market facts known at signal time; final synthetic entry, stop progression, exit and costs. Missing evidence => UNVERIFIABLE.
3. **Process quality vs P&L:** stage-by-stage rule adherence and information quality **at decision time**; separately forward outcome versus appropriate benchmark, costs, adverse excursion and execution realism.
4. **Failure taxonomy:** data/source, discovery omissions, wrong strategy match, missed risk, invalid entry or stop transition, execution/reconciliation errors and false positive critique; label attribution certainty.
5. **Counterfactuals and disagreement:** skipped winners, profitable bad decisions, correctly declined losers, human-shadow differences, alternate explanations and uncertainty.
6. **Proposed changes:** one or more small change requests, target bot/contract, original vs proposed rule version, evidence, expected test, regression risks and explicit approval required. No automatic tuning.
7. **Status:** GREEN process compliant, AMBER explainable open uncertainty, RED policy violation/ledger incompleteness; separate operational health from predictive performance. Propose next review date, do not falsely certify alpha.

## Protection and retention
- A shared log means one logical ledger, **not** one shared write permission. Bot emitters can append only their own typed records; NEO reads canonicals but only writes separate NEO reviews. No producer updates/deletes earlier events. A corrected decision is a superseding append event with reason and reviewer.
- Sensitive/private paper position data, any actual broker information, API credentials and raw licensed market observations are never published in this public repo. Sanitised GitHub reports contain aggregate statistics, versioned rule references, appropriately permissible ticker research and links to private evidence IDs without exposing private URIs.
- Keep append acknowledgements, idempotency, backup/restore, schema validation, cross-event hashes and audit integrity tests. Log service failure is a HOLD for decisions that require evidence; never silently continue a trade decision whose causal record cannot be persisted.
- NEO has no broker capability and cannot set, widen or disable stop rules. Production/live T-Bot remains off. An existing NEO in the GOLD trading stack is separate and must not be connected implicitly.

## Acceptance examples (offline)
- E-Bot emits zero qualifying candidates: explicit SCAN_COMPLETE with eligible/excluded counts and no paper order.
- Massive unavailable with valid IBKR data: UNCHECKED evidence survives for research; deterministic risk blocks order eligibility.
- A malformed-provider response is INVALID_DATA, not a provider outage; NEO can explain attribution without losing the valid other source.
- R-Bot HOLD before earnings prevents M/T synthetic entry; NEO sees the veto.
- M-Bot stop move lacks frozen rule evidence: risk gate blocks; event emitted and reconciled.
- T-Bot receives duplicate synthetic intent or simulated partial fill: one logical order, accurate fill/position ledger and independent reconciliation.
- NEO proposes a strategy alteration based on forward results: report only; prior strategy remains unchanged until GitHub amendment and human acceptance.
