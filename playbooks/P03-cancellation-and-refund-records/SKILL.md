---
name: P03-cancellation-and-refund-records
description: "Swarm deployment: cancellation to released inventory, rule-cited refund records, and a clean guest record. Agents 01, 06, 02, 05, 12, 13, 04."
---

# Playbook P03 - Cancellation & Refund Records

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`cancellation.request` at 06.

## Preconditions
- Identity confirmation rule satisfied; the published cancellation schedule version is recorded.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Execute
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 06 | Cancel per the published schedule; compute the refund basis with the rule line cited | `modification.result` → 02, 05, 13 | inventory released; billing basis recorded |
| 2 | 05 | Execute the in-rule refund and record it; out-of-rule requests route to human | `refund.record` → 12, 13 | record carries rule citation or authority envelope_id |

### Phase 2 - Close the loop
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 04 | Cancellation confirmation with refund facts per template | `guest.message.send` | send logged |
| 4 | 13 | Guest record reflects cancellation, refund, and any human decisions verbatim | (record entries) | chronology complete |

## HITL gates (hard stops)
- A cancellation is never silently reversed - an un-cancel is a NEW booking against live inventory (06's tuple).
- Refunds beyond the published rule move only on signed `payment.authority`.

## Completion criteria
Cancellation executed per schedule; inventory released; refund recorded with rule or authority citation; record complete.

## Abort paths
- Out-of-rule refund request: facts to human; the cancellation itself completes.
