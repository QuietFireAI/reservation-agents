---
name: P01-new-reservation
description: "Swarm deployment: guest request to confirmed, recorded, communicated reservation. Agents 01, 02, 03, 05, 13, 04. Confirmed only against a live hold and a published-rate quote - overselling starts at intake, so it ends there too."
---

# Playbook P01 - New Reservation

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
Reservation request lands at 01 on any channel.

## Preconditions
- Published rate tables and capacity configuration are the current human-signed versions.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Facts (parallel)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 02 | Availability check; live hold with expiry; capacity basis stated | `availability.result` → 01, 03 | hold reference with expiry on record |
| 2 | 03 | Quote from published tables; source per line; validity window | `quote.package` → 01, 13 | sourced quote on record |

### Phase 2 - Confirm (gated on live hold + quote)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 01 | Confirm carrying both references; dead hold = re-run Phase 1 | `booking.confirm` → 02, 05, 13 | inventory decremented against the hold; folio opened; record written |
| 4 | 04 | Confirmation message on the approved template | `guest.message.send` | send logged verbatim |

## HITL gates (hard stops)
- No confirm without a live hold AND a published-rate quote - both references travel in the envelope.
- Card data never transits the swarm (PCI) - payment happens in the payment system; 05 records references.

## Completion criteria
Reservation confirmed against a live hold and published quote; inventory, folio, record, and confirmation all landed.

## Abort paths
- Hold expired before confirm: re-run Phase 1; never confirm against a dead hold.
- Availability unknown (system unreachable): confirms block; guest offered waitlist or later confirmation.
