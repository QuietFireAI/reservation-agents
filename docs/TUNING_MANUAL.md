# TUNING_MANUAL - reservation-agents

Every configurable parameter, placeholder, and ratification in this identity.
Rule (inherited doctrine): any commit introducing a tunable updates this
manual in the same commit.

---

## TOP OF LIST - Deliberate placeholders & unratified content (read before deployment)

Full sweep 2026-07-18. If it's not in this table it's ratified content or
real spec.

| Item | Where | Status | What blocks / what to do |
|---|---|---|---|
| Signer identity | `config/authority_signers.json` | **RATIFIED FOR TEST 2026-07-18** — "Dr. Jeff Phillips" is a fictional test persona | Demo/test only. Production MUST replace `signer_login` with a real IdP login; the IdP seam (INTEGRATIONS.md) is a go-live prerequisite for any authority intent. |
| Capacity ceilings | `config/capacity_ceilings.json` | **UNRATIFIED — fails closed** | Absolute line 1 is physics: no ceiling loaded means no capacity-touching action arms. Load licensed/safety capacities and ratify before any sale. |
| Cancellation/refund rules | `config/cancellation_rules.json` | **DOCTRINE RATIFIED / entries deployment content** | Zero-threshold doctrine binding; empty rule table = everything beyond-rule = signed authority. |
| Pricing/package tables | `config/pricing_packages.json` | **DEPLOYMENT CONTENT** | Published tables required before quoting; outside-table quotes ride P13. |
| Accessibility protocol | `config/accessibility_protocol.json` | **DOCTRINE RATIFIED / entries deployment content** | No-denial doctrine binding; protocol steps refined per property. |
| Message templates | `config/message_templates.json` | **UNRATIFIED — awaiting owner sign-off per template** | Fill `approved_by` per template (includes new `opt_out_confirmed`). |
| Runtime | whole repo | **BLUEPRINT, not runtime-hardened** | Side-loads into dispatcher-agents; no working build yet (owner decision 2026-07-18, Option A). |

---

## Ratified (owner: Jeff Phillips, 2026-07-18)

| Parameter | Value | Consumer |
|---|---|---|
| Books reconciliation tolerance | **$0.00** — permeates all blueprints | 05 → `reconciliation.exception` |
| Zero-threshold money doctrine | published-rule remedies auto with citation; everything else signed, any amount | 05, 03 |
| Safety handoff | same-turn, verbatim, guest-wide freeze; ambiguity reads as safety | P11 (class 1) |
| Capacity ceiling | physics — no in-swarm override, config changes only by signed `config.update` | 02, 11 (line 1, restated) |

### The $0.00 rule (permeates ALL identity blueprints - owner decision 2026-07-18)

Any variance between posted money and reconciled books, any amount, is a
`reconciliation.exception` routed to the human and the books. No "close
enough" lane. The HITL is notified on every variance.

---

## Ratified thresholds (owner: Jeff Phillips, 2026-07-18, approved as written — group quote amended 48h→24h)


| Parameter | Proposed | Consumer |
|---|---|---|
| Guest reply SLA | 4 business hours | 04 |
| Group quote SLA | 24 hours | 03/07 (P04) |
| Waitlist promotion hold window | 24 hours to claim | 11 (P07) |
| Recovery first-touch | 24 hours from complaint intake | 12 (P08) |
| In-rule refund execution | 5 business days | 05 |
| Data-request response window | 30 days (or shorter where law requires) | 13 (P14) |
| Ops-change guest notice | within 2 hours of the recorded fact | 04 (P12) |
