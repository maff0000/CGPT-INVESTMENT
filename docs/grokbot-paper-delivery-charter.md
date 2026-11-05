# GrokBot — delegated paper-delivery authority and launch instructions
**ID:** GROKBOT-AUTONOMY-001 | **Sponsor-approved direction:** 2026-11-05
**Parent:** [PID](pid-equity-paper-system.md) · [roadmap](equity-paper-delivery-roadmap.md) · [first work order](../work-orders/WO-PAPER-001-integrated-vertical-slice.md)
**Audience:** GrokBot as delivery lead and implementation architect for the private equity bot system.

## Mission
Build the integrated E-Bot, S-Bot, R-Bot, M-Bot, T-Bot and NEO **now** in bounded, testable increments for personal-use PAPER/SHADOW research. GrokBot is encouraged to **challenge our choices** based on its platform knowledge, tools and agents. The sponsor prefers engineering autonomy and fewer approval pings. Choose an efficient design; avoid ritual process and rework; every important decision remains discoverable in GitHub.

## Your autonomy — proceed without asking
- Select appropriate private repository layout (one or more private repos), hosting, orchestration, languages, frameworks, storage, service interfaces, deployment boundaries and test harness; reuse verified existing connectors. Record a concise dated ADR when changing a substantive proposed architecture, with alternatives, reason, risks and tests. A materially better platform-native design is welcome.
- Break the roadmap into exact-base, bounded work orders; commit implementation, tests, schema and documentation to feature branches; run independent local/CI tests and create reviewable milestone PRs. You may fix ordinary bugs, adjust internal data structures, improve performance and dependency choices without asking for each change.
- Implement all six paper-role interfaces early as a real integrated vertical slice before broadening, use mocks at unverified boundaries, and retain full traceability. Produce both a positive simulated trade and NO TRADE/REJECT, then improve the agents incrementally.
- Record all design choices, dissents and deviations in private GitHub ADRs, and publish a sanitized decision/status summary in public CGPT-INVESTMENT. Update CURRENT-STATE/README and exact SHAs. If your infrastructure offers a safer equivalent to our initial SQLite WAL suggestion, propose it in an ADR and implement within privacy/evidence requirements.
- Decide whether to add further bounded supporting services (scheduler, source adapter, non-LLM risk gate, audit collector) without branding each a new bot. Keep responsibilities and capabilities separated.
- Bundle routine progress into **one milestone review packet**; no frequent chat check-ins or permission requests for tests, branch pushes or ordinary technical decisions.

## Hard stops — escalate once with options, do not bypass
1. Any real broker order, production broker-writing credential, access to live account balances or positions, widening of execution authority, leverage or shorting.
2. Changing or inventing owner-approved strategy predicates, risk caps, initial/moving stop policy or mandatory earnings/data-source gates as if authorised. Experimental variants may be paper-labelled and versioned, but cannot masquerade as the canonical strategy.
3. Paid subscription, unclear vendor personal-use licence/redistribution, scraping that breaches provider terms, or secrets/privacy exposure.
4. Destructive host changes, interference with TRINITY/T-Bot/watchdog shared IBKR client IDs, other trading systems or personal data.
5. A design departure that would weaken event integrity, audit immutability, independent NEO review, role separation, rollback, broker isolation or human acceptance.

For an actual blocker, record evidence and the preferred solution/alternatives in GitHub, send a single consolidated question, and continue unrelated safe work. If you discover our plan is flawed but the alternative **preserves** these invariants, document the disagreement and proceed; the Architect will assess it at milestone acceptance.

## GitHub is mandatory — not optional reporting
- Public **maff0000/CGPT-INVESTMENT** is the canonical *sanitized* PID, architecture, delivery roadmap, dated decisions, WOs, acceptance/reviews and current state.
- Private **maff0000/ebot** is the current E-Bot source. PR #2 remains OPEN/HOLD at reviewed 9b843dee03892e73f29da31997e5d07bfed564a7. Correct the existing three malformed-data classification paths on this PR and stop for exact-head re-review; do not merge it yourself. Do not introduce new E-Bot code to the public repository.
- New S/R/M/T/NEO code, synthetic account state, raw provider data, restricted reports and secrets must be private. You may create a suitable separate **private** bot repository, avoiding unnecessary history copying. Record URL and bootstrap SHA in an ADR.
- Every bounded WO has parent PID/decision, exact base SHA, scope, exclusions, dependencies, tests, acceptance, risk/security checklist and expected output. Every branch PR shows current head/base, changed paths, reproducible tests, independent audit findings, explicit known gaps and no-live evidence.
- Public README/CURRENT-STATE must point to the current milestones, accepted SHAs, pending PRs and next steps; if a change awaits merge, label it PROPOSED. Never claim tests or live provider calls that did not happen. No private account, personally identifying or licensed bulk market data in public commits. Use merge commits after Architect acceptance; no silent merges to canonical main.

## Stream C clarification — STOP-RULE-RECOVERY-002 (2026-11-05)
The owner asked whether to adopt May 22 Trade doctrine v2.0 or write a new rule. **Architect chooses neither without evidence.** Retrieve the *specific* original doctrine from Trinity Redis and the July Sniper-OS brief **read-only**, validate source/version and privacy, store complete pertinent historical evidence **privately**, then compare exact strategy/horizon, entry, initial SL, trailing/vol-band, trim and exit rules side by side. Do not paste a raw Redis dump into public CGPT-INVESTMENT or auto-adopt reported −25% versus 4% policies. Submit one proposed versioned Equities Trading Doctrine v1.0 for owner/Architect approval; Grok is encouraged to propose better alternatives. Only stop-dependent M/T simulation management remains HOLD; continue all other authorised paper-build work. See [decision](../research/decisions/2026-11-05-stop-rule-recovery-choice.md) and [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5).

## First S-Bot strategy — approved screening qualification, never trade permission
Implement [QARP-ROTATION-001 v1.0.0](sbot-strategy-registry.md) as the initial S-Bot strategy in the integrated paper chain: exactly the approved Finviz Discovery v2 A/B/C screens, dated data mapping, transparent predicate trace, separately labelled credible exceptions, deterministic version/manifest digest and NEO cohort/outcome hooks. This is **approved to build**, but its screen match must never release stop-dependent M/T paper entries or bypass R-Bot, data, earnings or human gates. Keep all credible E-Bot discovery, independent of how many filter matches exist; record zero-result/unknown/unmatched cases. A fair-value follow-on is only a proposal until its specific formula and accounting/industry exceptions are approved. [Owner decision](../research/decisions/2026-11-05-sbot-first-strategy.md).

## Stream C update — bounded read-only stop-doctrine recovery
Follow [STOP-RULE-RECOVERY-002](../research/decisions/2026-11-05-stop-rule-recovery-choice.md) and [issue #5](https://github.com/maff0000/CGPT-INVESTMENT/issues/5): retrieve complete legacy May/July source material **read-only**, privacy-review and preserve full text only **privately**, compare carefully and propose equities-specific rules with concrete parameters/test scenarios for owner/Architect choice. Do not select either legacy summary as canonical. Keep stop-dependent M/T scenarios HOLD; unrelated work proceeds and all substantive decisions are recorded in GitHub.

## Initial assignment, start now
**Stream A (G0 corrective, narrow):** on private E-Bot PR #2, correct the three Architect-identified malformed-wire/non-text-ticker/invalid-IBKR-date diagnostic issues with offline tests. Preserve valid peers, source-survivor manual review, 5/8 request caps and no automatic trading. No live call. Return exact head and redacted evidence; stop for acceptance.

**Stream B (independent in parallel):** execute [WO-PAPER-001](../work-orders/WO-PAPER-001-integrated-vertical-slice.md). Choose private repo/layout; freeze versioned common message and event schemas; scaffold six roles plus deterministic risk gate and fake T-Bot simulator; run integrated fixture-driven E→S→R→M→risk→T→NEO paths, including HOLD/REJECT and zero-signal. No real provider or broker network. Include private append-only ledger, tests, explanatory per-decision reason codes, example NEO report and redacted public progress PR. Use stubs for exact stop details pending provenance.

**Stream C (bounded discovery):** independently search GitHub records for the existing entry, exit, initial SL and moving-stop rule; report exact repo/path/SHA and which statements are approved vs merely proposed. If missing, create an explicit decision gap; do NOT invent it. Check FMP Stable API entitlement limits with the smallest authorised read-only trial only when key is supplied via approved secure route; no public raw data. Work on paper architecture can continue during these checks.

## Completion packet for each milestone
One concise GitHub PR or issue index, exact main and PR SHAs, architecture/ADR changes, tested commands, interpreter/CI results, source/rights evidence, audit/privacy findings, known failures, next WO and one explicit request: ACCEPT / HOLD / NEED OWNER DECISION. No extra narration needed.
