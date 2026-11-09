# OWNER_NOMINATED_RESEARCH — owner-nominated research protocol (proposed)

**Date:** 2026-11-09 (Europe/London)  
**Status:** PROPOSED — pending Architect acceptance. Not accepted. Not merged. Not an operating instruction.  
**Parents:** [ADR-APP-004](../adr/ADR-APP-004-model-independence-and-portable-agent-identities.md), [SWARM-002](../amendments/PID-EQUITY-PAPER-001-SWARM-002.md), [ADR-APP-003](../adr/ADR-APP-003-the-rogue-alliance-autonomous-swarm.md), [team charter](the-rogue-alliance-charter.md).  
**Also applies:** [INDEPENDENT-001](../independent-investment-challenge.md), [public working agreement](../independent-research-relationship.md), [three-mandate strategy](../investment-strategy.md), [execution boundary](../execution-authorisation-boundary.md).

## Authority

This file is architecture documentation only. It authorises no runtime implementation, no native message, no broker or wealth-manager integration, no trading, no new source onboarding, and no Claude deployment. It does not change ledger schemas or QARP. PAPER ONLY. G0 remains OPEN. Provider rights remain UNVERIFIED. QARP-ROTATION-001 v1.0.0 stays frozen. This protocol must not delay or alter the private SWARM-B supervised native-agent demonstration.

No agent sends a nomination, opens a case, or messages another agent because this file exists.

## What a nomination is

Matt may submit an investment hypothesis directly to M-Bot. The submission is a **research request**.

It is not a positive signal, not evidence that the security is attractive, not a strategy promotion, and not trading authorisation. The team tests the hypothesis. It does not anchor on it. The optional owner thesis is a claim to be examined, labelled as such, and kept separate from every agent's conclusion.

The same duty already applies under INDEPENDENT-001 and the public working agreement: investigate the claim, seek disconfirming evidence, and disagree when the evidence disagrees. A nomination does not relax QARP, an earnings gate, a source-rights hold, or the execution boundary. A research conclusion is never an order.

## Workflow

1. **Submission.** Matt sends M-Bot one nomination. It contains one or more security identifiers, an investment objective, and a proposed holding horizon. It may also contain an optional owner thesis. It may also refer to portfolio or allocation constraints. Those constraints are private. They are never written into this public repository or into any public ledger. If a private channel for them does not yet exist, M-Bot records that they were not received. It does not ask for them to be pasted into a public file.
2. **Clarification.** M-Bot does not assign the case while the identifier, the objective, or the horizon is missing. M-Bot asks Matt for the missing item and waits. An absent thesis is allowed. Absent portfolio information is allowed, and the later portfolio section is then marked INCOMPLETE.
3. **Assignment.** M-Bot assigns a bounded read-only research task. E-Bot covers the business, the sources and the economic evidence. S-Bot covers the strategy and valuation hypothesis against the accepted baseline. The frozen QARP ruleset is a baseline, not a target the case must pass, and not a ruleset the case may edit. T-Bot is not given an execution task.
4. **Independent first views.** E-Bot and S-Bot each write a first view before seeing the other's view. Each view states the hypothesis in neutral terms, separates fact from inference, and records at least two substantive disconfirming points, or states that the counter-evidence is UNKNOWN and where it would be found. Neither view is written to confirm the owner thesis.
5. **Challenge.** R-Bot then performs a mandatory material-risk challenge. R-Bot sees the sealed first views and the stated hypothesis. R-Bot is not bound by either view or by the owner thesis. The first views stay as written. R-Bot's objection identifies the disputed evidence, the missing information, or the risk.
6. **Synthesis.** M-Bot writes a synthesis that shows the agreements and the disagreements in full. M-Bot does not average them away and does not replace a dissent with a smoother conclusion. Where the evidence is thin, the synthesis says so.
7. **NEO review.** NEO reviews the research quality and the behaviour of every participating agent, including M-Bot. NEO checks whether disconfirming evidence was sought, whether the owner thesis was treated as a target, whether dissent was preserved, and whether unknowns were filled in. NEO does not direct the case and does not edit another agent's record.
8. **Delivery.** M-Bot delivers one consolidated Investment Decision Dossier to Matt. The dossier is the research product. It is not sent to a broker, a venue, or a wealth manager.

## Wealth-management boundary

Three layers stay separate.

| Layer | Who acts | What this layer may do |
|---|---|---|
| 1. Alliance research | The Rogue Alliance | Propose hypotheses, valuation scenarios, risk concerns and questions for a wealth manager |
| 2. Personal decision | Matt | Decide, outside this research system, whether the research is worth taking further |
| 3. Advice and execution | An authorised wealth manager | Assess suitability and, if instructed by Matt through that manager's own process, execute |

The Alliance does not sit in layer 2 or layer 3. It must not infer that a holding was purchased, that an allocation was approved, or that a wealth manager was instructed. A dossier question addressed to a wealth manager is a question Matt may choose to pass on. It is not an instruction from the Alliance, and it is not evidence that a manager received it.

There is no wealth-management account connection. This work is not personal advice and not a suitability assessment. Personal risk budget, tax, liquidity need and existing holdings are inputs only when Matt has supplied them privately and lawfully, and even then they are used only to mark what the research cannot see.

## Portfolio-level assessment

When the nomination names more than one security, the dossier includes a portfolio-level assessment of those names together. When it names one security, the same section still exists, and it says what cannot be judged.

The assessment covers only what the evidence supports:

- aggregate sector and industry exposure of the named securities;
- economic and thematic correlation among them;
- concentration and overlapping business risks;
- currency exposure;
- interest-rate and macro sensitivity;
- downside scenarios;
- existing holdings and liquidity commitments, only when those facts were supplied privately and lawfully.

If portfolio information was not supplied, the assessment is labelled **INCOMPLETE**. The missing holdings and weights are left unknown. They are never invented, estimated from a public filing of an unrelated holder, or copied from an earlier research note. Public information about the named securities can still support a comparison of those securities with each other. That comparison does not become a statement about Matt's portfolio.

## Investment Decision Dossier

One dossier, in this order:

1. **Company and business analysis.** What the business sells, to whom, and which claims are fact, inference, or unknown. One subsection per named security.
2. **Financial quality.** Cash generation after capital spending, dilution, balance-sheet strain and the quality of the reported numbers, with sources.
3. **Independent valuation.** What the evidence implies at the observed price, and what remains unpriced. A lower multiple or a growth rate is not itself a valuation.
4. **Long-term thesis.** The economic proposition under test, restated without adopting it. Horizon is the horizon Matt proposed, checked against the evidence rather than assumed.
5. **Bear, base and bull scenarios.** Each scenario states what must be true. A speculative partnership or uncontracted opportunity is worth nothing in the base case.
6. **Catalysts and event risk.** Dated events, earnings gates and what is already known. A missing date stays missing.
7. **Portfolio compatibility.** The assessment above, labelled INCOMPLETE where the private inputs are absent.
8. **R-Bot objections.** The material-risk challenge, unedited in substance, including any point M-Bot did not adopt.
9. **NEO observations.** Research quality and behaviour of every participant, including M-Bot.
10. **M-Bot research conclusion.** One research label of BUY STARTER, BUY FULL, WAIT (with a concrete reconsideration condition), or REJECT. The conclusion is labelled **research-only**. It is distinct from execution authority. It authorises no order, no size and no account instruction.
11. **Evidence gaps and conditions for reconsideration.** What is unknown, and the evidence, price or event that would reopen the conclusion.
12. **Source provenance and timestamps.** Source, publication time, retrieval time, market timezone, licence status where relevant, and the information cut-off. Model, prompt, tool and strategy versions are recorded when a later implementation exists. This protocol does not create those fields in a schema.

## Learning cycle

The cycle follows ADR-APP-002 and ADR-APP-003. This protocol does not run it.

1. NEO evaluates the evidence and the behaviour of every participating agent, including M-Bot.
2. NEO identifies weaknesses and improvements that the record can demonstrate.
3. M-Bot considers each finding and acknowledges it. A decline is recorded with a reason. NEO's finding stays visible.
4. An improvement becomes a versioned proposal: hypothesis, evidence, proposed change, evaluation design and rollback.
5. An experiment runs only after separate approval, and it compares the old method with the new method.
6. An improvement is adopted only when the comparison has been independently verified.
7. Rejected improvements and previous versions stay traceable. History is not rewritten.

Agents may propose improvements from their own experience without waiting for NEO. They cannot promote themselves into new permissions, replace an approved strategy, or change a production policy. Recommendation is not adoption.

## Sanitised illustration

This illustration is generic. It is not a nomination, not a holding, and not a case the team has run.

Matt submits identifiers EXAMPLE-A and EXAMPLE-B, objective "compare two claimed compounders", horizon "multi-year". The optional thesis is "each has a durable installed base". No portfolio weights, account facts, or adviser correspondence are included.

E-Bot's first view finds evidenced cash generation at EXAMPLE-A and an uncontracted growth claim at EXAMPLE-B that is worth nothing in the base case. S-Bot's first view, written without E-Bot's text, finds that EXAMPLE-A's price already discounts the installed-base claim, and that EXAMPLE-B's strategy match is unknown. Both record disconfirming points before seeing each other.

R-Bot objects that the two businesses depend on the same customer spending cycle, so the pair concentrates one demand risk. M-Bot's synthesis records that objection and does not remove it. Portfolio holdings were not supplied, so portfolio compatibility is INCOMPLETE. The research conclusion is WAIT for both names, with a stated evidence condition for reconsideration. NEO notes whether either first view echoed the owner thesis. The dossier stops at research. No purchase is inferred, no wealth manager is instructed, and no order is created.

## Public record

A public copy of a real dossier would breach the [public working agreement](../independent-research-relationship.md). Private constraints, holdings, allocations, adviser correspondence and the text of a personal request stay outside this repository. A later public note, if any, is a sanitised method note, not the case file.
