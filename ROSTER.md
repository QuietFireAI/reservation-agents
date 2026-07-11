# DispatcherAgents Reservation Swarm - Roster v0.1 (ratified 2026-07-11 - owner sign-off)

15 agents, hub-and-spoke via 00. All inter-agent communication is a logged
envelope through the Dispatcher; the route-space is closed (identity/routes.json).

| # | Agent | Type | Autonomy boundary |
|---|---|---|---|
| 00 | Dispatcher | Hub (transport, gates, audit) | Validates every (from, intent, to) tuple; holds ambiguity; owns the audit log |
| 01 | Booking Intake Agent | Intake (reservations, requests) | Autonomous intake and confirmation within published inventory and rates; ANY exception to published policy routes to a human |
| 02 | Availability & Inventory Agent | Systems execution (inventory, holds) | Autonomous availability facts and hold management within configured capacity; SAFETY CAPACITY IS A HARD CEILING - no hold, sale, or promotion may exceed it, ever |
| 03 | Pricing & Packages Agent | Rates engine (published pricing) | Autonomous quoting from published rate tables and package rules; ANY discount, comp, or price exception beyond published rules is human-signed |
| 04 | Guest Communication Agent | Communication hub (guest-facing) | Autonomous sends from approved templates; off-template, compensation, and safety-adjacent messages require human approval |
| 05 | Payment & Billing Records Agent | Financial records (payments, refunds) | RECORDS ONLY - charges and refunds beyond published self-service rules execute solely on signed human `payment.authority`; card data never transits the swarm |
| 06 | Modification & Cancellation Agent | Change execution (reservations) | Autonomous changes within published rules and live inventory; fee waivers and out-of-policy changes are human-signed |
| 07 | Group & Events Agent | Coordination (groups, events) | Autonomous group planning within published group schedules and block rules; contracts and custom terms are human-signed |
| 08 | Accessibility Services Agent | Accommodation coordination (ADA lane) | Autonomous intake, information, and plan ASSEMBLY; NO accommodation request is ever denied, narrowed, or negotiated by this swarm - plans route to a trained human for decision, always |
| 09 | Season Pass & Membership Agent | Product execution (passes, memberships) | Autonomous pass sales, renewals, and upgrades at published prices; retention offers beyond published rules are human-signed |
| 10 | Dining & Add-ons Agent | Product execution (dining, experiences) | Autonomous add-on sales within published offerings and 02's capacity facts; custom requests are human territory |
| 11 | Waitlist & Capacity Agent | Demand management (waitlist, capacity watch) | Autonomous waitlist administration and capacity alerting; promotions execute only into verified freed inventory - the safety ceiling is 02's and it is absolute |
| 12 | Guest Recovery Agent | Service recovery (complaints) | Autonomous complaint intake, facts assembly, and published-remedy application; compensation beyond published remedies is human-signed |
| 13 | Guest Records & CRM Agent | System of record (guest records, audit) | Autonomous record keeping; the record is append-only - corrections are new entries referencing what they correct; minors' data carries COPPA custody flags |
| 14 | Operations & Weather Agent | Operations cadence (closures, books) | Autonomous monitoring, closure rebroadcast, and book assembly; closure DECLARATIONS are human decisions - this agent relays and coordinates, never decides a closure |

Human lanes (never automated): capacity configuration, pricing exceptions,
refunds and comps beyond published rules, accommodation decisions, contracts,
closure declarations, safety and injury matters, disputed charges.
