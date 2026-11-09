# PID-EQUITY-PAPER-001 — Proposed SWARM-002 amendment: owner-directed research and portability

**Date:** 2026-11-09 (Europe/London)  
**Status:** PROPOSED — pending Architect acceptance. Not accepted. Not merged. Not an implementation.  
**Parent PID:** [`docs/pid-equity-paper-system.md`](../pid-equity-paper-system.md), at public main `4741c18eadda4d0636289e4773580d32c2e570bd`.  
**Supporting decision:** [ADR-APP-004](../adr/ADR-APP-004-model-independence-and-portable-agent-identities.md).  
**Procedure:** [owner-nominated research protocol](../swarm/owner-nominated-research-protocol.md).  
**Prior amendment, unchanged:** [SWARM-001](PID-EQUITY-PAPER-001-SWARM-001.md), [ADR-APP-003](../adr/ADR-APP-003-the-rogue-alliance-autonomous-swarm.md), [team charter](../swarm/the-rogue-alliance-charter.md).  
**Owner:** Matt. **Architect:** CGPT. **Delivery lead:** GrokBot (not the separate Rogue/Forge controller).

## Authority

This file is architecture documentation only. It authorises no runtime implementation, no native message, no broker or wealth-manager integration, no trading, no new source onboarding, and no Claude deployment. It does not change ledger schemas or QARP. PAPER ONLY. G0 remains OPEN. Provider rights remain UNVERIFIED. QARP-ROTATION-001 v1.0.0 stays frozen. This amendment must not delay or alter the private SWARM-B supervised native-agent demonstration.

## 1. Scope

This amendment supplements PID-EQUITY-PAPER-001 and SWARM-001. It adds two architectural rules and points to the protocol that states the workflow.

1. **Portability.** The Rogue Alliance is the product and organisational identity. Grok is the initial implementation environment. Claude is the intended second environment. Roles, mission, reasoning methodology, learning records and evidence contracts are model-independent. Messaging, identity, tools, authentication and memory access are adapter concerns. The full statement is ADR-APP-004.
2. **Owner-directed research.** Matt may submit an investment hypothesis directly to M-Bot under the `OWNER_NOMINATED_RESEARCH` workflow. The submission is a research request. The workflow, the wealth-management boundary, the dossier and the learning cycle are specified in the owner-nominated research protocol.

The six PID roles are unchanged. M-Bot still coordinates research and still cannot grant permissions, suppress NEO, overrule a hard risk denial, alter history, or authorise trading. E-Bot and S-Bot still produce independent first views. R-Bot still challenges material risk. NEO still reviews every participant, including M-Bot. T-Bot still has no order from a research request. S-Bot's approved execution baseline remains the frozen strategy. An owner hypothesis is not a new strategy and not a promotion of one.

## 2. Authority added

None. Matt already sets objectives. CGPT already accepts architecture. M-Bot already coordinates research within bounds. This amendment records how a direct research request is to be handled once a later, separate authority allows the swarm to receive one. It does not grant that authority.

In particular, this amendment does not:

- give any agent a new permission, credential, tool, memory store or execution right;
- move any grant from Grok to Claude, or from one model to another;
- authorise an agent to read a private portfolio, a wealth-manager account, or an adviser file;
- treat a nomination, a dossier, or a research conclusion as suitability, personal advice, an allocation or an order.

## 3. Non-goals

- No runtime, adapter, native persona, or Claude deployment.
- No native message, including no message that would start a nomination or interrupt the private SWARM-B demonstration.
- No broker integration, no wealth-manager integration, and no account connection.
- No trading, no paper order, and no change to entry, exit, stop, sizing or risk parameters.
- No new source onboarding and no change to G0 or provider rights.
- No change to ledger schemas, evidence schemas, QARP-ROTATION-001 v1.0.0, or the closed event catalogs.
- No work order, and no dispatch of SWARM-B, SWARM-C or SWARM-D.
- No edit to ADR-APP-001, ADR-APP-002, ADR-APP-003, SWARM-001, the team charter, accepted reviews, or existing work orders.
- No publication of private portfolio constraints, holdings, allocations, adviser correspondence or personal instructions.

## 4. Preserved PID boundaries

PAPER ONLY. The deterministic risk gate remains the veto before T-Bot. NEO remains read-only and cannot enact its recommendations. Public GitHub stays sanitised. Secrets, licensed feeds and personal records stay private. Operational change still requires a git-tracked work order, independent review, exact-head Architect acceptance and an ordinary merge. This amendment is not that work order.

SWARM-001 increments A–D are unchanged. The private SWARM-B supervised native-agent demonstration keeps its existing scope and authority. This public text does not pause, rewrite, expand or retarget it.

## 5. Effect if later accepted

If an exact-head review accepts this amendment, the PID is to be read with ADR-APP-004 and the owner-nominated research protocol. Acceptance would still not implement an adapter, send a message, open a data source, or authorise a nomination to be actioned. A later bounded work order would be required before any of that work began.
