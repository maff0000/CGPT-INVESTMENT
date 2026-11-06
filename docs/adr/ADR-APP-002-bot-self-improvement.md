# ADR-APP-002 — Bot self-improvement
**Date:** 2026-11-06 (Europe/London)
**Status:** PROPOSED. Not accepted. Not merged. This public ADR records the parent-supplied self-improvement requirement for Architect review of private [paper-bots PR #9](https://github.com/maff0000/paper-bots/pull/9) exact head `619a607ed1879c93a82e4e652b2edc7531efb530`. It does not accept that head. It does not replace [ADR-APP-001](ADR-APP-001-platform-findings.md). Private ADR 0016 is the private record of the same requirement. This session did not read that file. The text below is the parent-supplied requirement, recorded verbatim, not a copy of private ADR prose beyond that requirement.
**Packet:** [REVIEW-M6-NEO-001](../../research/reviews/2026-11-06-wo-paper-006-neo-review-packet.md), pinned to the head of `cursor/wo-paper-006-neo-review-packet-5d19`. That packet does not contain the SHA of the public commit that adds it.
**Public note:** [WO-PAPER-006](../../work-orders/WO-PAPER-006-neo-decision-review.md)

**Successor pointer, 6 November 2026. Proposed. Not accepted.** The Architect HOLDs exact private head `619a607ed1879c93a82e4e652b2edc7531efb530`. The current head under review is `4b3dac4c4137a5cb89a9587862e5fe25c464887b`. Its parent `4078c6a560901ea67eb217f0486cdc18d045efa2` is the intermediate evidence-relationship correction. [REVIEW-M6-NEO-002](../../research/reviews/2026-11-06-wo-paper-006-neo-review-correction-packet.md) requests ACCEPT or HOLD of `4b3dac4c4137a5cb89a9587862e5fe25c464887b` and does not accept it. The requirement text below stays the recorded requirement. It is not rewritten by the HOLD.

**Synthetic boundary.** v0.3 stays explicitly synthetic. The report `producer` is `OFFLINE_DEMONSTRATOR` and `native_review_provenance` is `NOT_APPROVED`. A genuine native review needs a separately approved provenance representation and must not reuse this demonstrator schema. The offline demonstrator is not that native review.

## Requirement

AGENT SELF-IMPROVEMENT — MANDATORY CAPABILITY

Every Bot must be capable of proposing improvements to its own prompts, analytical methods and strategies, informed by its experience, NEO's findings and collaboration with other Bots.

Improvements must be versioned and recorded in GitHub, with the original hypothesis, evidence, proposed change, evaluation results and rollback path.

Bots may autonomously develop and test experimental versions in offline or shadow mode. Their accepted versions remain unchanged until independently reviewed.

NEO must track performance by Bot, strategy and version, evaluate whether proposed improvements genuinely outperform their baselines, and recommend promotion or rejection.

NEO itself must be subject to evaluation and improvement.

No Bot may alter historical evidence, silently replace approved trading rules, increase authorised risk or activate live execution.

The common objective is sustainable, risk-controlled growth of the trading ledger through continuous, measurable improvement.

Sequence: NEO finding → proposed change → GitHub decision → bounded implementation → independent review → acceptance. A Bot may also start at the proposed change from its own experience, without waiting for NEO.

## Autonomy

| Activity | Authority |
|---|---|
| Challenge another Bot's decision | Autonomous |
| Identify and explain mistakes | Autonomous |
| Research alternative methods | Autonomous |
| Propose strategy improvements | Autonomous |
| Create experimental Bot versions | Autonomous |
| Run offline/shadow comparisons | Autonomous |
| Recommend promotion of a better version | Autonomous |
| Replace an approved production strategy | Independent review required |
| Change risk limits or activate live trading | Explicit approval required |

This milestone records the table and stops at unevaluated proposals (`evaluation_status` `NOT_RUN`, `promotion` `NOT_RECOMMENDED`, `approved_strategy_replaced` false). It does not create an experimental Bot runtime or run a shadow comparison. Competing versions (for example S-Bot v1.0 vs v1.1) are a later roadmap item, not implemented here.

## What this milestone does with the requirement

Parent-read behaviour, not an Architect confirmation. S-Bot files its own earnings-quality method proposal from Bot experience. The experimental label is `1.1-shadow-not-run`. The original `STRATEGY_MATCH` stays. QARP-ROTATION-001 v1.0.0 is not replaced. Frozen file SHA-256 remains `e45f604c8c2da68d5cb06ce1dee5659a4b77e132f2e01303ecebf66877d19e62`. Ruleset digest remains `d3ad50fbdb152ddb62ddfdf6e115a2825edff591163eaa309f6f5b141e5a2fac`. Applying a proposal raises and does not write the frozen manifest.

The financial performance ledger and the decision-evidence ledger stay distinct. Today both are different event types in the one append-only ledger. An outcome append does not update the decision row.

## Boundaries that stay

`authenticates_sender` stays false. `parent_platform_metadata` stays refused. `live_message_sent` stays false. Synthetic provenance is not authenticated native provenance. The prepared T-Bot to NEO handoff is `PREPARED_NOT_SENT`. Increment C isolation deployment is deferred by t79u (6 November 2026). [REVIEW-M5-INDEP-003](../../research/reviews/2026-11-06-wo-paper-005-cf2dd5-independent-acceptance.md) and private ADR 0015 remain historical reference. They are not rewritten and not deployed. This ADR does not pursue additional Cursor users, separate computers, or dedicated NEO infrastructure.

G0 remains OPEN. Provider rights remain UNVERIFIED. FMP remains exactly three historical calls. Stop-dependent M/T remain HOLD. No scheduler, broker or account read, vendor call, order, or fill is granted by recording this requirement.

The head under review does not change this requirement's stop at unevaluated proposals. QARP-ROTATION-001 v1.0.0 stays unreplaced. The HOLD of `619a607` preserved that safeguard. Acceptance of `4b3dac4c4137a5cb89a9587862e5fe25c464887b` is not claimed here.
