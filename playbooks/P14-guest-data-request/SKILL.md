---
name: P14-guest-data-request
description: "Swarm deployment: guest data access or deletion request to human-approved response inside the clock. Agents 13, 14, 04. Minors' custody flags honored per item (absolute line 4); release and deletion are human decisions."
---

# Playbook P14 - Guest Data Request Response

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
Guest data access/deletion request lands via 04 (guest channel) or 01 (intake).

## Preconditions
- The request is captured verbatim with date, requester identity basis, scope, and the applicable response window.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Clock and inventory
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Response clock visible in operations reporting | (ops clock; `report.package` carries it) | clock live in the daily book |
| 2 | 13 | Disclosure inventory: existence, type, date, source per item; minors' custody flags named | `records.disclosure.package` → human, 14 | inventory delivered inside the window's lead-time |

### Phase 2 - Human decision and response
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 13 | Record the human's release/deletion decision and execution | `record.response` + `interaction.log` | itemized decision record: who, what, when, under whose approval |
| 4 | 04 | Respond to the guest per the approved scope, from templates | `guest.message.send` → external | response artifact on record |

## HITL gates (hard stops)
- Nothing beyond the human's itemized approval is disclosed or deleted - the approval is the ceiling.
- Identity verification questions route to the human - the swarm never adjudicates who is entitled to a minor's data (line 4).
- Deletion touching financial/audit records routes with the retention obligation named - conflicting duties are human calls.

## Completion criteria
Human-approved response delivered inside the clock with a complete itemized record; or refusal/clarification recorded the same way.

## Abort paths
- Requester identity cannot be established from the record: human decision before any data moves.
- Scope ambiguous or overbroad: clarification before any work product leaves the swarm.
