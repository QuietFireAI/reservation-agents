---
name: P12-ops-change-wave
description: "Swarm deployment: operational change short of closure (ride down, hours change, weather posture) to re-anchored inventory and informed guests. Agents 14, 02, 06, 11, 04, 13. The smaller sibling of P06 - closures stay closure.notice; the two waves never blur."
---

# Playbook P12 - Operational Change Wave

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
`event.change.notice` at 02/06/11/13 from 14 (operations/weather).

## Preconditions
- The change is a recorded operational fact with its effective window - a rumor is not a wave trigger.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Re-anchor
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 02 | Availability re-anchored; affected holds and sales enumerated | `availability.result` → 01, 03 (as needed) | inventory reflects the fact; ceiling re-checked, never assumed |
| 2 | 11 | Waitlist/capacity re-anchored; promotions pause until capacity re-confirmed | `capacity.alert` → queue, 14 (if triggered) | no promotion against unverified capacity |

### Phase 2 - Guests
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 06 | Affected bookings enumerated; options from published rules only | `modification.result` → 02, 05, 13 (per booking) | every affected booking has a disposition or a hold |
| 4 | 04 | Guest notices from posted facts and approved templates | `guest.message.send` → external | facts only - no speculation about duration or cause |

## HITL gates (hard stops)
- The safety capacity ceiling is physics at every step - no re-accommodation exceeds it (absolute line 1).
- Beyond-published-rule remedies route for signed authority - the wave does not widen the money lane.
- No safety statements in guest notices - operational facts only (line 5).

## Completion criteria
Inventory and waitlist re-anchored, every affected booking dispositioned or held with reason, guests informed from posted facts.

## Abort paths
- Change escalates to closure: P06 closure-rebooking wave takes over; this playbook's record hands off cleanly.
- Capacity cannot be re-confirmed: promotions and re-accommodations hold; the unknown blocks the gate.
