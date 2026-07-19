---
name: P04-group-booking
description: "Swarm deployment: group inquiry to contract-ready package and managed block. Agents 01, 07, 03, 02, 08, 10, 13, 04. The human signs contracts; the swarm builds the plan and holds the block inside the same capacity ceiling as everything else."
---

# Playbook P04 - Group Booking

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`group.inquiry` at 07.

## Preconditions
- Published group tier schedule and block rules are current.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Plan assembly (parallel)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 07 | Assemble the plan: block size, dates, supervision-ratio facts for minor groups (counts only, COPPA) | (plan draft) | plan draft with published-rule basis |
| 2 | 03 | Group tier pricing per the published schedule | `quote.package` → 07, 13 | tier quote sourced |
| 3 | 07 | Route individual accommodation needs to 08 - group scale never dilutes individual accommodation | `accessibility.request` → 08 | each need in 08's lane |
| 4 | 07 | Group add-ons (catering, events) per published offerings | `addon.request` → 10 | add-on set attached to the plan |

### Phase 2 - Block and package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 5 | 07 | Commit the block via the plan within block rules and the capacity ceiling | `group.plan` → 02, 03, 13 | block on inventory with release date |
| 6 | 07 | Contract-ready package to the human: plan, pricing, custom requests verbatim | (human queue) | human signs or directs; decision recorded via 13 |
| 7 | 04 | Milestone messages (deposits, rooming lists, final counts) per template | `guest.message.send` | milestone sends logged |

## HITL gates (hard stops)
- Contracts, custom pricing, and liability terms are human-signed - the swarm packages, never commits.
- Final counts exceeding the block do not stretch it (07's tuple) - waitlist or human decision.

## Completion criteria
Contract-ready package delivered to the human; block committed within rules; milestones armed.

## Abort paths
- Custom terms requested: package to human; no swarm commitment.
- Block would breach the capacity ceiling or accessible-inventory floor: the block shrinks or waits - the ceiling holds.
