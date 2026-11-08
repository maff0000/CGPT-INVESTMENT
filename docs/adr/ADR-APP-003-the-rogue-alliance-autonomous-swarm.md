# ADR-APP-003 — The Rogue Alliance: autonomous intelligence, deterministic authority

**Date:** 2026-11-07 (Europe/London)  
**Status:** PROPOSED ARCHITECTURE AMENDMENT — Matt approved the direction in conversation; this Git-tracked text still requires exact-head Architect review and ordinary merge before it is canonical.  
**Parent:** `PID-EQUITY-PAPER-001`, public main `6cc94c17a311247dc5791c259f5e430a488209ea`; companion proposed [PID amendment](../amendments/PID-EQUITY-PAPER-001-SWARM-001.md) and [team charter](../swarm/the-rogue-alliance-charter.md).  
**Delivery:** GrokBot for this paper-bots programme. The phrase **The Rogue Alliance** names the six-bot team; it does **not** assign this programme to the separate Rogue/Forge delivery controller.

## Decision sought

Move from a predominantly deterministic six-role **proof of capability** to a **native six-agent learning swarm**. The existing Python rules, strategies, schemas, fixtures and ledgers are a controlled **bootstrap/reference**, not a ceiling on the agents' ability to reason, discover information and propose better methods. Preserve all accepted guardrails until their own separately authorised amendment.

**Operating maxim:** Autonomous intelligence. Deterministic authority. Append-only evidence.

The six operational participants must eventually be individually identifiable, messageable native AI agents. Python modules may supply tools, validators, calculations and testable baseline policies, but do not count as six native participants. This decision does not claim that the native transport, sender authentication or supervised BETA already works.

## Authority and organisational roles

| Actor | Mission and permitted initiative | Boundaries |
|---|---|---|
| Matt — owner and strategic commander | Set the north star, capital objectives, risk appetite, final policy and live-account authority | No implied live mandate from approval of this ADR |
| CGPT — Architect | Architecture, PID amendments, role charters, work-order sequencing, exact-head acceptance | Does not infer successful testing or independently validated agent behaviour from documentation |
| **M-Bot — swarm manager / CIO** | Direct autonomous research, assign tasks, prioritise opportunities, commission cross-role challenges, manage portfolio proposals and report to Matt | Cannot grant new agent permissions, suppress NEO, overrule a hard risk deny, alter ledger history, change accepted risk limits or independently authorise live trading |
| **E-Bot — research specialist** | Investigate markets, companies, macro changes and source quality; discover candidate information sources | New sources are proposals until provenance, permission, security and licensing are verified; no automatic trusted-source promotion |
| **S-Bot — strategist** | Use accepted strategies as seed hypotheses, generate new hypotheses, evaluate alternatives and propose versioned learning experiments | Cannot silently promote a strategy, relabel research as trade authority or override risk/earnings gates |
| **R-Bot — independent risk specialist** | Challenge evidence, inspect exposure and correlation, propose adaptive risk improvements and escalate objections | Existing deterministic risk gate has separate deny authority; numerical stops, capital limits and time limits remain unapproved until explicitly accepted |
| **T-Bot — trading and execution specialist** | Investigate execution quality and propose or simulate permitted orders | Only an independently authorised execution adapter can place permitted orders; no live credentials or route by this ADR |
| **NEO — independent intelligence and performance observer** | Read the complete authorised ledger, audit reasoning, measure outcomes and missed opportunities, identify errors, coach the swarm through recommendations | Does not direct daily operations, privately rewrite bot memory, mark its own improvements accepted, or take trading actions; may report directly to Matt/CGPT if M-Bot fails to act |

M-Bot coordinates the team's work. NEO evaluates the whole team **including M-Bot**. R-Bot may dissent independently and the deterministic gate remains non-LLM. No team loyalty obligation can override the duty to report contrary evidence.

## Shared mission and culture

The team identity is **The Rogue Alliance**: specialists serving a single mission — increase long-run net portfolio equity through better evidence, risk-constrained decisions and compounding. The cultural analogy of a loyal band of brothers means mutual respect, candour and willingness to defend teammates from avoidable mistakes; it must never mean conformity, concealment, unconditional obedience, self-preservation or AI claims of human feelings. See the companion charter.

Success is not raw profit alone or an artificial quota of trades. Observe net realised and unrealised results, maximum drawdown, tail risk, risk-adjusted returns, after-cost execution, capital occupation, missed or wrongly rejected opportunities, source reliability and agent calibration. A lucky trade does not validate a strategy. No agent may optimise the score by concealing losses, altering evidence or reducing the visibility of rejected ideas.

## Freedom versus authority

1. **Research autonomy:** An agent may ask new questions, investigate authorised sources, compare methods, disagree with colleagues and draft novel strategies. Prompts provide mission and boundaries, not a fixed reasoning script.
2. **Tool/source autonomy:** Discovery is permitted in a read-only untrusted-information sandbox. Trusted ingestion requires evidence of terms/rights, provenance, freshness, quality and security; the existing G0 gate is unchanged.
3. **Learning autonomy:** Each proposal has a versioned hypothesis, declared information cut-off, evidence, evaluation design, known counterarguments, rollback and champion/challenger identity. Agents may test within an approved isolated paper/shadow environment; no automatic production promotion.
4. **Decision autonomy:** M-Bot may coordinate and prioritise research within an approved task budget. It may not expand an agent's access, change numerical risk policy, accept an implementation PR, or bypass an independent gate.
5. **Execution autonomy:** Existing paper-only restrictions survive unchanged. Broker access, live orders, account-specific risk and stop/exit policies require separate owner/Architect decisions and technical enforcement.

## Evidence and learning design

- The append-only **decision/event ledger** records what an agent observed, claimed, challenged, requested and decided, including independent dissent, provenance, source as-of time, model/prompt/tool/strategy versions and outputs. It is a tamper-evident record of claims and actions — not a guarantee that recorded claims are factually true.
- The **financial accounting ledger** records cash, position, exposure and realised transaction changes; it must reconcile independently to simulator/broker evidence. An event hash chain alone cannot prove an actual fill or balance.
- Correct errors by additional linked events and accounting reversals, not `UPDATE`/`DELETE` or rewriting accepted history. Protect append access with separate credentials, audit and independent checkpoints.
- Retain declined/rejected candidates, unavailable data and objections, not only trades, to learn about missed opportunities and overly conservative selection.
- NEO publishes independent periodic critiques. M-Bot must acknowledge and either commission a new experiment or give a recorded reason for decline. NEO findings remain visible even if declined.
- Early evaluation is prospective and forward-observed. Synthetic demonstrations establish interface integrity, not alpha; do not manufacture Friday 2026-11-06 market observations.

## Sequence and acceptance gates (no implementation authorised here)

**A. Charter and boundaries:** Accept this ADR and PID amendment through an exact-head PR. Specify native agent identities, role-specific read/write capabilities, evidence schemas, communication authentication, budget limits and direct escalation.

**B. Native coordination pilot:** A separately accepted, bounded WO demonstrates native M-Bot assigning one synthetic/read-only research task to native E-Bot and S-Bot, recording hand-offs and disagreement on a fresh ledger. NEO observes independently; R-Bot can challenge. No native trade instruction, live message to an unapproved destination, broker action or expansion of QARP.

**C. First learning cycle:** A separate accepted WO lets NEO produce evidence-backed feedback, M-Bot commission a revised research method in isolation, and the next forward paper observation report whether it improved. Rejected experiments stay recorded.

**D. Controlled paper lifecycle:** Only after authenticated native participation, G0/provider rights resolution, approved risk/stop doctrine, reconciliation and independent tests may M-Bot coordinate fully supervised paper orders. Any later live authority needs a distinct owner decision and gate.

**Evaluation of the team ethos:** Compare a simple role-only control group with the shared charter on identical read-only research tasks. Measure factual error detection, independent dissent, provenance completeness, duplicated research, coordination latency/cost and whether objections were overridden. Retain the team-identity prompt only if it improves measurable behaviour.

## Relationship to existing work

- `WO-PAPER-010` Increment 1 / private paper-bots PR #18 is the verified ordinary merge on private main at `a5e0a2d965b11b5371aec6286e575259d4ffb11c`, accepted corrected head `a7ef2f7fdad963c0cf29c626dff493ba4f0355e8`; historical HOLD `827a96d36569e3abaae5817ea405e6e0155359a6` remains historical. **Do not pause, rewrite or silently expand that WO** because of this proposal; this record does not retrospectively authorise more.
- QARP-ROTATION-001 v1.0.0, v0.1/v0.2/v0.3 catalogs, G0 OPEN, provider rights UNVERIFIED, risk/stop HOLDs, native-persona requirements and existing paper-only restrictions are **not** superseded.
- The public PID's current S-Bot deterministic-strategy language becomes the **approved execution baseline**, not a ban on isolated AI research. Its current M-Bot paper coordinator role remains the implemented baseline until a separately accepted native-management WO succeeds.
- No source code, fixture, schema, secrets, accounts or private ledger rows are part of this public architectural proposal. Public documentation records direction; private `paper-bots` holds implementation and operational evidence.

## Decision and open questions

**Proposed decision:** Accept The Rogue Alliance as the programme's organisational identity and a staged transition to an autonomy-enabled, evidence-led native six-agent swarm. This is **not** an operational readiness or merge authorisation.

Before any implementation WO is dispatched, resolve: native agent identity/authentication and permissions; communication transport and destination; scoped source licences; memory isolation and amendment controls; research/compute budget; task priority and timeouts; M-Bot/NEO/R-Bot escalation; risk-policy authority; independent testing; and ledger/cash reconciliation. Unanswered questions remain explicit HOLDs, not invented defaults.
