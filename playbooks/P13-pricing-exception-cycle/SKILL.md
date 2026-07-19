---
name: P13-pricing-exception-cycle
description: "Swarm deployment: quote outside published tables to signed authority and a cited quote. Agents 03, 07, 13. Zero-threshold doctrine: published rules apply automatically with citation; everything else, any amount, is signed."
---

# Playbook P13 - Pricing Exception Cycle

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
`pricing.exception` at human/13 from 03 - a requested quote (individual or group) falls outside the published tables.

## Preconditions
- The published-table computation is on record showing exactly where the request exits the rules - the exception names its delta.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 03 | Exception package: published computation, requested terms, the delta as fact | `pricing.exception` → human, 13 | every number carries its source |
| 2 | 13 | Guest/group history attached (existence and facts, no judgment) | `record.response` → 03 | context complete |

### Phase 2 - Signed issue
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 03 | Quote issues only on signed authority, citing the envelope | (await `pricing.authority` ← human); then `quote.package` → 01/07, 13 | signed envelope on the chain before the quote moves |

## HITL gates (hard stops)
- No quote outside published tables issues unsigned - there is no discretion lane, no de-minimis exception (zero-threshold doctrine, ratified 2026-07-18).
- The exception and its approval travel together on the record - a cited quote is auditable end to end.

## Completion criteria
Signed quote issued with the authority cited, or the exception declined/expired with that recorded the same way.

## Abort paths
- Authority not received before the quote's validity window closes: the exception expires on record; the guest is informed from published facts.
- Request mutates while pending: fresh exception package - a changed request is a new exception, never an edit to a pending one.
