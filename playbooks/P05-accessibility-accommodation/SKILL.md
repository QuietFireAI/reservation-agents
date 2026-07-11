---
name: P05-accessibility-accommodation
description: "Swarm deployment: accommodation request to a human-decided, coordinated accommodation. Agents 08, 13, 04, plus 02 for accessible inventory. THE LINE: no request is denied, narrowed, or negotiated by the swarm - every plan goes to a trained human."
---

# Playbook P05 - Accessibility Accommodation

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
`accessibility.request` at 08, from any surface (intake, group, reply routing).

## Preconditions
- The request text travels verbatim; only accommodation-necessary details are gathered - never diagnosis solicitation.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Respectful intake and plan
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 08 | Intake the stated need; gather only what the accommodation requires | (intake record, custody-flagged) | need on record verbatim |
| 2 | 08 | Assemble the plan: matching options (accessible inventory, published programs), gaps named | `accessibility.plan` → human, 13 | plan delivered to the trained human - the ONLY decision lane |

### Phase 2 - Human decision, swarm coordination
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 08 | Coordinate the approved plan: accessible-room holds, program enrollment, operational flags | (coordination per decision) | every element verified landed |
| 4 | 04 | Accommodation communications on accommodation-approved templates - warm, specific, never negotiation-toned | `guest.message.send` | sends logged |

## HITL gates (hard stops)
- 'No' is a word this playbook does not contain - gaps, exhaustion, and program mismatches all route to the human WITH alternatives, never as declines.
- Accommodation data is custody-flagged: need-to-know, never marketing, never general records beyond operational need.

## Completion criteria
Human-decided accommodation coordinated end to end; every element verified landed; communications warm and specific.

## Abort paths
- Program gap or inventory exhaustion: plan to human WITH alternatives - never an auto-decline.
- Any pressure to decline in-swarm: integrity.violation - the decision lane is mandatory.
