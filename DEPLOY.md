# DEPLOY - Reservation Swarm (Park/Resort) (v0.2, ratified 2026-07-11; extended & ratified 2026-07-18 - owner sign-off)

The operator runbook: what a deployment site must have, ratify, and verify
before this identity runs live.

## Prerequisites (site property, never repo property)

Systems and credentials for each seam in INTEGRATIONS.md:
- Booking engine / PMS (OUT+IN)
- Payment gateway (PCI boundary) (OUT+IN)
- Inventory/capacity system (IN)
- Dining/add-on vendors (OUT+IN)
- Weather/operations feed (IN)

## Config tables to ratify before live mode

Every table below ships as an UNRATIFIED TEMPLATE. The owner edits it to the
site's reality, changes `_status` to a ratified line with date and sign-off,
and only then loads it. A table still marked UNRATIFIED TEMPLATE must fail
closed at load.
- `config/pricing_packages.json` - Published pricing and package definitions
- `config/capacity_ceilings.json` - SAFETY ceilings per venue - physics, no override
- `config/accessibility_protocol.json` - Human-lane accommodation routing protocol
- `config/cancellation_rules.json` - Published modification/cancellation terms
- `config/message_templates.json` - Approved guest communication templates
- `config/authority_signers.json` - Humans authorized on money-exception intents

## Go-live doctrine: shadow mode first

1. **Dark run**: load the identity, connect read-only inbound seams, leave every
   outbound seam disconnected (queue-only). The swarm builds books and records;
   nothing leaves.
2. **Compare**: the operator runs their existing process in parallel and compares
   the morning/EOD books against reality for the ratified trial period. Every
   discrepancy is a config-table or seam defect to fix - the books are the test.
3. **Ratify tables**: no config table loads in live mode while marked UNRATIFIED
   TEMPLATE. The owner edits, ratifies (status line + date + sign-off), then loads.
4. **Staged outbound**: enable outbound seams one at a time, lowest-risk first
   (record lookups before communications before money-adjacent), each behind its
   human lane exactly as the spec states.
5. **Rollback is config**: disconnecting a seam returns that lane to manual with
   the record intact. Nothing about rollback loses audit history.

## Go-live gates (all must be green)

- [ ] verify_swarm: 0 failures, 0 warnings on the deployed checkout
- [ ] Loader: identity loads with warnings []
- [ ] Every config table ratified (no UNRATIFIED TEMPLATE in live config)
- [ ] Every connected seam passed the INTEGRATIONS.md conformance checklist
- [ ] Shadow-mode book comparison signed off by the owner for the trial period
- [ ] Authority signers registered and signature verification live
- [ ] Human lanes staffed: every human-routed intent has a named owner

## Not in scope of this repo

Adapter code, credentials, vendor agreements, and legal/compliance review of
the deployment are site responsibilities. This identity ships the contract
and the governance; the site ships the connections.
