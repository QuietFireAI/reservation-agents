---
name: P06-closure-rebooking-wave
description: "Swarm deployment: human closure declaration to coordinated rebooking, waitlist, and remedy response. Agents 14, 06, 11, 12, 04, 13. The human declares; the swarm relays the declaration verbatim with its policy set and runs the wave."
---

# Playbook P06 - Closure Rebooking Wave

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
Human closure declaration relayed by 14 as `closure.notice`.

## Preconditions
- The closure policy set (rebooking options, remedy set, waitlist effects) is attached to the declaration - a declaration without its policy set holds for human completion.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Relay (immediate, parallel)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Relay the declaration with policy set, narrower-scope rule on ambiguity | `closure.notice` → 06, 11, 12 | relay logged with scope as declared |
| 2 | 11 | Freeze affected waitlists per the policy | (waitlist state change) | freeze logged |

### Phase 2 - The wave
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 06 | Offer published rebooking options to affected reservations per policy order | `modification.result` per acceptance → 02, 05, 13 | each rebooking atomic |
| 4 | 12 | Apply the closure remedy set; beyond-set requests route to human | `recovery.plan` → human, 13 (as needed) | remedies recorded with the set cited |
| 5 | 04 | Wave communications per closure templates - operational facts, never weather promises | `guest.message.send` | sends logged |

### Phase 3 - Books
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 6 | 14 | Wave results into the EOD books: rebooked, refunded, pending, unreachable - all counted | `report.package` → human | wave section complete with gaps named |

## HITL gates (hard stops)
- The swarm never declares, extends, or lifts a closure - relay only (14's legal line).
- Scope ambiguity runs the narrower scope until the human expands it.

## Completion criteria
Wave complete: affected reservations rebooked/refunded/pending all counted in the EOD books with gaps named.

## Abort paths
- Declaration arrives without its policy set: relay holds for human completion.
- Scope ambiguity: narrower scope runs; expansion only on human direction.
