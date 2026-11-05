# ADR-APP-001 — recorded Grok Bot platform findings
**Date:** 2026-11-05 (Europe/London)
**Status:** RECORDED FACTS. Not an architecture approval. Not a claim that the six roles are provisioned or that a hard access-control list exists.
**Evidence:** owner milestone brief. This session did not invoke agent creation, did not send a handoff, and did not inspect the app.

## Findings
- Creating an agent creates an individual messageable agent.
- Sending work to an agent is an asynchronous priority handoff.
- The current T-Bot identifier `81d8cf38-188e-4592-b08d-b59d6e461e83` is reused and is not modified by this record.
- The text supplied when an agent is created shapes its instructions. That text is not proven to be a hard tool access-control list.
- Agents on the same box share a filesystem.
- No automatic attachment of the private Python package, and no production ledger write bridge, has been verified.
- NEO is logically read-only. A persona statement does not enforce that limit. Hard capability enforcement has to be tested.

## Consequence
App teammates and any ledger bridge stay **PROPOSED** until probes and tests exist. Actual agent identifiers, other than the reused T-Bot identifier above, have not arrived. This cloud session does not provision agents. The parent does that.
