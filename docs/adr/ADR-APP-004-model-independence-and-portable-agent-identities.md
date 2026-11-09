# ADR-APP-004 — Model independence and portable agent identities

**Date:** 2026-11-09 (Europe/London)  
**Status:** PROPOSED — pending Architect acceptance. Not accepted. Not merged. Not an implementation.  
**Parent:** `PID-EQUITY-PAPER-001`, public main `4741c18eadda4d0636289e4773580d32c2e570bd`. Companion proposed [PID amendment SWARM-002](../amendments/PID-EQUITY-PAPER-001-SWARM-002.md) and [owner-nominated research protocol](../swarm/owner-nominated-research-protocol.md).  
**Builds on, and does not rewrite:** [ADR-APP-003](ADR-APP-003-the-rogue-alliance-autonomous-swarm.md), [SWARM-001](../amendments/PID-EQUITY-PAPER-001-SWARM-001.md), [team charter](../swarm/the-rogue-alliance-charter.md), [ADR-APP-001](ADR-APP-001-platform-findings.md), [ADR-APP-002](ADR-APP-002-bot-self-improvement.md).

## Authority

This file is architecture documentation only. It authorises no runtime implementation, no native message, no broker or wealth-manager integration, no trading, no new source onboarding, and no Claude deployment. It does not change ledger schemas or QARP. PAPER ONLY. G0 remains OPEN. Provider rights remain UNVERIFIED. QARP-ROTATION-001 v1.0.0 stays frozen. This decision must not delay or alter the private SWARM-B supervised native-agent demonstration.

## Decision sought

Separate the product from the model that first implements it.

**The Rogue Alliance** is the product and the organisational identity. **Grok** is the initial implementation environment. **Claude** is the intended second environment. Agent roles, mission, reasoning methodology, learning records and evidence contracts are model-independent. Platform-specific messaging, identity, tools, authentication and memory access are implemented through adapters.

No model or platform migration automatically inherits permissions, secrets or execution authority. Each of those must be re-granted explicitly for the destination environment. Agent performance must be evaluated independently on comparable missions before a platform migration is accepted. A future architecture may select different models for different roles.

**No Claude adapter is implemented or deployed by this decision.**

## What travels with the agent

The durable identity of each participant is its role inside The Rogue Alliance:

| Portable item | Meaning |
|---|---|
| Role | M-Bot, E-Bot, S-Bot, R-Bot, T-Bot or NEO, with the mission and boundaries already stated in ADR-APP-003 and the team charter |
| Mission | Protect and grow capital through evidence, risk-constrained decisions and compounding. The operating maxim remains: autonomous intelligence, deterministic authority, append-only evidence |
| Reasoning methodology | Independent first view, mandatory challenge, recorded dissent, provenance, and refusal to treat enthusiasm as evidence |
| Learning record | Versioned hypothesis, information cut-off, evidence, evaluation, counterargument, rollback and champion/challenger identity, as in ADR-APP-002 and ADR-APP-003 |
| Evidence contract | What was observed, claimed, challenged, requested and decided, with source, as-of time and version. The contract is logical. This ADR does not alter a ledger schema |

A platform user id, bot id, conversation store, credential or tool grant is not that identity. It does not travel with the role.

## What an adapter owns

An adapter is the only place that binds a portable role to one environment. It implements that environment's:

- messaging;
- identity binding;
- tools;
- authentication;
- memory access.

Grok is the adapter environment for the current paper programme, including the limits already recorded in ADR-APP-001. Those limits remain: on that platform, bots of one user share one computer; a created bot id and an instructional refusal are not a hard access-control list; a bot has no credentials of its own. A portable role name does not remove those limits.

Claude is named only as the intended second environment. This decision does not specify a Claude transport, principal, memory store, tool grant or authentication method, and it does not build one.

The existing [`claude-research/`](../../claude-research/README.md) folder is dated evidence written beside the journal. It is not a runtime, not an adapter, and not an agent deployment. This decision does not change that folder and does not treat its notes as a Claude platform binding or as permission to use Claude.

## Permissions do not migrate

A move from one environment to another, or a choice to run one role on a different model, carries the portable items above and nothing else.

Permissions, secrets and execution authority are re-granted explicitly for the destination. A grant on Grok is not a grant on Claude. A research conclusion is not an execution grant in either environment. Paper-only limits, the open G0 gate, unverified provider rights, the frozen QARP ruleset, and the non-LLM risk gate stay where they are until their own decisions change them.

Memory is not copied across environments as a side effect of a migration. Learning records that are safe to carry are the versioned, provenance-scoped proposals already required by ADR-APP-002. Secrets, account data, licensed raw feeds and personal portfolio records are not learning records and are not copied into this public repository.

## Evaluation before a migration is accepted

A platform migration of a role is accepted only after that role has been evaluated independently on comparable missions in the destination environment. Comparable means the same question, the same information cut-off and the same evidence contract, scored on factual error, disconfirming evidence, provenance, dissent and calibration.

A successful connection, a delivered message, or a vendor claim that one model is stronger is not that evaluation. The destination result is compared with the recorded baseline. Rejected comparisons stay traceable. This ADR does not define a metric schema and does not run a comparison.

A future architecture may assign different models to different roles. That assignment is a later decision. Each role still needs its own explicit grants and its own comparable-mission evaluation. No role is pre-assigned to Claude by this text.

## Relationship to current work

- ADR-APP-003, SWARM-001 and the team charter remain the organisational design. This ADR adds portability. It does not change their status, their text, or their gates.
- ADR-APP-001 remains the record of Grok platform facts. ADR-APP-002 remains the self-improvement requirement, including the rule that an agent may propose an improvement and may not itself replace an approved strategy, risk limit or live-trading permission.
- The private SWARM-B supervised native-agent demonstration continues on its existing authority. This public record does not pause, rewrite, expand, retarget or dispatch it, and it does not record a private SHA for it.
- Public documentation states the direction. Private implementation and operational evidence stay in the private repository. No source, fixture, schema, secret or ledger row is part of this proposal.

## Open questions

These remain explicit HOLDs. This ADR does not invent defaults for them:

1. The adapter interface that a later work order would implement.
2. Who accepts a comparable-mission evaluation, and on what frozen question set.
3. How a learning record moves without copying secrets, personal holdings or licensed raw data.
4. Whether, and when, any role should run on a model other than the initial Grok environment.

**Proposed decision:** record The Rogue Alliance as model-independent, with Grok as the initial environment and Claude as the intended second environment, and require explicit re-grant plus independent evaluation before any migration. This is not operational readiness, not a Claude deployment, and not a merge authorisation.
