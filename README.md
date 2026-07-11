# reservation-agents - park & resort reservations vertical for the DispatcherAgents runtime

An **identity side-load**: everything vertical-specific for a 15-agent
park/resort reservations swarm, loadable into the content-neutral
[dispatcher-agents](https://github.com/QuietFireAI/dispatcher-agents) runtime.
The runtime never contains vertical text; this repo never contains transport
code. That split is the architecture.

**Status: v0.1 DRAFT - owner ratification pending. Not runtime-hardened. No
licensed legal, accessibility (ADA), or payment-compliance (PCI) review has
been performed.**

## What this is for

Reservations and guest operations at attraction scale: bookings confirmed only
against live holds and published rates, changes and cancellations per published
rules, group plans, season passes, dining and add-ons, fair-order waitlists,
closure rebooking waves, service recovery inside a published remedy table, and
the morning/end-of-day books.

What it never does - the five absolute lines (identity/IDENTITY-park-reservation-agent.md):

1. The safety capacity ceiling is physics - nothing exceeds it, and no
   in-swarm override exists.
2. No accommodation is ever denied by the swarm - every accessibility plan
   routes to a trained human for the decision.
3. No unsigned money beyond published rules - and card data never transits
   the swarm (PCI).
4. Minors' data is minimized and never marketed (COPPA).
5. Safety matters are never service matters - immediate human escalation.

## Layout

| Path | What it is |
|---|---|
| `identity/routes.json` | The closed track: 36 (intent, senders, receivers) routes - single source of truth |
| `identity/priority.json` | JIT playbook priority classes (DRAFT) |
| `identity/IDENTITY-park-reservation-agent.md` | The identity declaration |
| `00-dispatcher/ ... 14-operations-weather/` | 15 agent SKILL.md + DECISIONS.md (tuple layer) |
| `playbooks/P01 ... P10` | Deployment playbooks: new reservation through EOD books |
| `SWARM.md` | Framework manifest + swarm-level tuples |
| `MANNERS.md` | Conduct constants, hash-registered at boot attestation |
| `TUPLE_INDEX.md` | Generated drill-down: tuple → agent → playbooks |
| `generate_skills.py` / `gen_meta.py` / `gen_playbooks.py` / `gen_tuple_index.py` | Generators - data tables are the spec; files are build artifacts |
| `verify_swarm.py` | Enforcement: tuple legality, edge completeness, regression - exit 0 = clean |

## Verify

```bash
python3 verify_swarm.py    # 0 failures, 0 warnings expected
```

## Load into the runtime

```bash
git clone https://github.com/QuietFireAI/dispatcher-agents.git
git clone https://github.com/QuietFireAI/reservation-agents.git
cd dispatcher-agents && pip install -e ".[pillars,crypto,dev]"
```

```python
from dispatcher.loader import load_identity
ident = load_identity("/path/to/reservation-agents")
```

The loader is fail-closed: no routes.json, no track, no load. The DRAFT
priority table loads with its draft state warned and audited - never silently.

## Sibling identities

- [listing-agents](https://github.com/QuietFireAI/listing-agents) - real-estate listing vertical (ratified)
- [claim-agents](https://github.com/QuietFireAI/claim-agents) - insurance claims vertical (DRAFT)

## License

Proprietary - see LICENSE (placeholder pending legal review).
