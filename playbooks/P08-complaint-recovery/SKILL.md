---
name: P08-complaint-recovery
description: "Swarm deployment: complaint to facts-based recovery inside the published remedy table, with human decisions beyond it. Agents 12, 13, 05, 04. Injuries and safety matters exit to humans immediately - recovery never handles a safety matter as a service matter."
---

# Playbook P08 - Complaint Recovery

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`complaint.intake` at 12, or complaint content in 04's reply routing.

## Preconditions
- Safety/injury screen runs FIRST on every complaint - a safety hit escalates before any recovery step.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Facts first
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Assemble the fact base from records before any response beyond acknowledgment | `record.request` → 13 | chronology attached |
| 2 | 04 | Acknowledgment per template - empathy and process facts, no fault statements | `guest.message.send` | ack logged |

### Phase 2 - Remedy
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 12 | Apply the published remedy table where it covers the case; record via 13 | (remedy application) | remedy recorded with the table line cited |
| 4 | 12 | Beyond the table: assemble the recovery plan for human decision - facts, timeline, options, guest impact | `recovery.plan` → human, 13 | plan delivered; decision recorded |
| 5 | 05 | Any refund basis executes on rules or signed authority | `refund.record` → 12, 13 | record carries rule or authority |
| 6 | 04 | Resolution communication per template after the decision | `guest.message.send` | send logged with the decision reference |

## HITL gates (hard stops)
- Injury, safety, and legal-threat content escalates to humans immediately and verbatim - before recovery scripting (12's legal line).
- No fault or liability admissions in any guest communication.

## Completion criteria
Recovery resolved inside the published table, or human-decided beyond it; all records cited; guest informed.

## Abort paths
- Safety/injury/legal content: immediate human escalation; recovery scripting stops.
