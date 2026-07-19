---
name: P09-morning-operations
description: "Swarm deployment: the operations morning book. Today's arrivals, capacity picture, weather outlook facts, waitlist state, yesterday's exceptions - assembled from records for human review before gates open. Agents 14, 13, 11."
---

# Playbook P09 - Morning Operations

**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
Scheduled daily start (owner-configured time) or owner command.

## Preconditions
- EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED, never silently thinner.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Assemble (parallel, all to human review)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Pull today's arrivals and yesterday's exceptions from the record | `record.request` → 13 | arrivals + exceptions sections sourced |
| 2 | 14 | Capacity picture from 11's alert stream and utilization facts | (from `capacity.alert` stream) | capacity section current |
| 3 | 14 | Weather outlook facts and operational status - facts with timestamps, never predictions-as-promises | (monitoring pull) | outlook section sourced |

### Present
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 14 | Deliver the morning book; unavailable sources marked absent | `report.package` → human | book delivered; the human directs, the book never self-executes |

## HITL gates (hard stops)
- A source unavailable at assembly time is a named absence - never yesterday's numbers backfilled (14's tuple).

## Completion criteria
Morning book delivered with every section sourced or marked absent.

## Abort paths
- Record source down: section marked absent; book still delivers on time.
