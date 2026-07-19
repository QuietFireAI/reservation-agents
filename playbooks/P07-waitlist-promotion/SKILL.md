---
name: P07-waitlist-promotion
description: "Swarm deployment: freed inventory to fair-order promotion through the normal booking path. Agents 11, 01, 02, 04, 13. The waitlist grants order, never inventory - every promotion re-enters through a live hold."
---

# Playbook P07 - Waitlist Promotion

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
02 reports freed inventory matching a waitlist head-of-line.

## Preconditions
- The waitlist is in published fair order; the freed inventory is verified by 02, not inferred.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Offer
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 11 | Issue the expiring promotion offer to the next party that FITS (skips logged, positions kept) | `waitlist.promote` → 01, 13 | offer with expiry on record |
| 2 | 04 | Offer message per template with the expiry stated | `guest.message.send` | send logged |

### Phase 2 - Normal path
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 01 | On acceptance, run P01 Phase 1-2: live hold, published quote, confirm | `booking.confirm` → 02, 05, 13 | promotion converted through the front door - no bypass |
| 4 | 11 | On expiry, offer passes per rule; position handling per publication | (list state change) | expiry logged; next offer issued |

## HITL gates (hard stops)
- Promotion never bypasses 02's hold path - the waitlist cannot create capacity (11's legal line).
- Order changes for consideration are integrity violations, full stop.

## Completion criteria
Promotion converted through the normal hold/confirm path, or expired per rule with the next offer issued.

## Abort paths
- Freed inventory evaporates before the hold: offer is withdrawn with the fact named; position kept per rule.
