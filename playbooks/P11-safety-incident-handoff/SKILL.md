---
name: P11-safety-incident-handoff
description: "Swarm deployment: safety matter detected anywhere to verbatim human handoff with the service lanes frozen. Agents 01/04/12 (detection), 13, 14. Absolute line 5 executing: safety matters are never service matters - no scripting, no statements, ever."
---

# Playbook P11 - Safety Incident Handoff

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off)

## Trigger
`safety.notice` from any detection point: intake (01), guest channel (04), or a recovery conversation (12).

## Preconditions
- The matter is captured verbatim with source, timestamp, and guest/booking reference - the handoff carries the guest's words, not a summary.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Handoff (same turn)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 01/04/12 | Route the matter verbatim; the service conversation stops | `safety.notice` → human, 13, 14 | verbatim record delivered, human alerted |
| 2 | 14 | Ops visibility same turn; on-the-ground response is human territory | (ops log; `agent.status` → 14 for any waiting lane) | ops aware inside the turn |

### Phase 2 - Freeze and record
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 12 | Any recovery case for this guest freezes pending human direction | (hold) | frozen case named with reason |
| 4 | 13 | Incident reference on the guest record - verbatim, custody-flagged | `interaction.log` | record complete, content verbatim |

## HITL gates (hard stops)
- No safety statement, reassurance, apology-implying-fault, or recovery scripting from any agent - the swarm's only move is the verbatim handoff.
- No service or marketing contact to this guest until explicit human direction - the freeze is guest-wide, not conversation-wide.

## Completion criteria
Verbatim handoff delivered same turn, ops visible, service lanes frozen for the guest, record complete; human owns everything after.

## Abort paths
- Ambiguity about whether a matter is safety: treat it as safety - the conservative read is the only read (line 5 doctrine).
- Guest continues messaging after handoff: received, logged, routed verbatim; no swarm reply.
