---
name: P02-modification-cycle
description: "Swarm deployment: change request to atomically applied modification across inventory, billing, and records. Agents 01, 06, 02, 05, 13, 04. Published change rules govern; waivers are human-signed."
---

# Playbook P02 - Modification Cycle

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
`modification.request` at 06 (from 01 intake or 04 reply routing).

## Preconditions
- Identity confirmation rule satisfied for the reservation being changed.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Rule and inventory
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 06 | Verify the published change rule; compute fee/refund per the published schedule | (rule check) | rule citation on the change record |
| 2 | 06 | Check inventory effects with 02 (the hold rule applies to changes) | (via availability facts) | target inventory verified |

### Phase 2 - Atomic apply
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 06 | Apply the change; report atomically to inventory, billing, records | `modification.result` → 02, 05, 13 | all three effects in one result; partials flagged, never hidden |
| 4 | 05 | Execute any published-rule refund; record with the rule cited | `refund.record` → 12, 13 | refund record carries the rule citation |
| 5 | 04 | Change confirmation on the approved template | `guest.message.send` | send logged |

## HITL gates (hard stops)
- Fee waivers and out-of-policy changes route to human verbatim; a signed decision executes via 05's authority path.
- Identity confirmation failure = no change, record holder notified, flag raised.

## Completion criteria
Change applied atomically across inventory, billing, and records; guest confirmed.

## Abort paths
- Identity confirmation fails: no change; record holder notified; flag raised.
- Rule conflict on fees: both readings to human; the change holds.
