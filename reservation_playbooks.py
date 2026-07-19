# reservation-agents playbooks P01-P10.
PB = [
 dict(num="P01", slug="new-reservation", name="New Reservation",
  desc="Swarm deployment: guest request to confirmed, recorded, communicated reservation. Agents 01, 02, 03, 05, 13, 04. Confirmed only against a live hold and a published-rate quote - overselling starts at intake, so it ends there too.",
  trigger="Reservation request lands at 01 on any channel.",
  pre=["Published rate tables and capacity configuration are the current human-signed versions."],
  phases=[
   ("Phase 1 - Facts (parallel)", [
    ("1","02","Availability check; live hold with expiry; capacity basis stated","`availability.result` → 01, 03","hold reference with expiry on record"),
    ("2","03","Quote from published tables; source per line; validity window","`quote.package` → 01, 13","sourced quote on record"),
   ]),
   ("Phase 2 - Confirm (gated on live hold + quote)", [
    ("3","01","Confirm carrying both references; dead hold = re-run Phase 1","`booking.confirm` → 02, 05, 13","inventory decremented against the hold; folio opened; record written"),
    ("4","04","Confirmation message on the approved template","`guest.message.send`","send logged verbatim"),
   ]),
  ],
  gates=["No confirm without a live hold AND a published-rate quote - both references travel in the envelope.",
         "Card data never transits the swarm (PCI) - payment happens in the payment system; 05 records references."]),

 dict(num="P02", slug="modification-cycle", name="Modification Cycle",
  desc="Swarm deployment: change request to atomically applied modification across inventory, billing, and records. Agents 01, 06, 02, 05, 13, 04. Published change rules govern; waivers are human-signed.",
  trigger="`modification.request` at 06 (from 01 intake or 04 reply routing).",
  pre=["Identity confirmation rule satisfied for the reservation being changed."],
  phases=[
   ("Phase 1 - Rule and inventory", [
    ("1","06","Verify the published change rule; compute fee/refund per the published schedule","(rule check)","rule citation on the change record"),
    ("2","06","Check inventory effects with 02 (the hold rule applies to changes)","(via availability facts)","target inventory verified"),
   ]),
   ("Phase 2 - Atomic apply", [
    ("3","06","Apply the change; report atomically to inventory, billing, records","`modification.result` → 02, 05, 13","all three effects in one result; partials flagged, never hidden"),
    ("4","05","Execute any published-rule refund; record with the rule cited","`refund.record` → 12, 13","refund record carries the rule citation"),
    ("5","04","Change confirmation on the approved template","`guest.message.send`","send logged"),
   ]),
  ],
  gates=["Fee waivers and out-of-policy changes route to human verbatim; a signed decision executes via 05's authority path.",
         "Identity confirmation failure = no change, record holder notified, flag raised."]),

 dict(num="P03", slug="cancellation-and-refund-records", name="Cancellation & Refund Records",
  desc="Swarm deployment: cancellation to released inventory, rule-cited refund records, and a clean guest record. Agents 01, 06, 02, 05, 12, 13, 04.",
  trigger="`cancellation.request` at 06.",
  pre=["Identity confirmation rule satisfied; the published cancellation schedule version is recorded."],
  phases=[
   ("Phase 1 - Execute", [
    ("1","06","Cancel per the published schedule; compute the refund basis with the rule line cited","`modification.result` → 02, 05, 13","inventory released; billing basis recorded"),
    ("2","05","Execute the in-rule refund and record it; out-of-rule requests route to human","`refund.record` → 12, 13","record carries rule citation or authority envelope_id"),
   ]),
   ("Phase 2 - Close the loop", [
    ("3","04","Cancellation confirmation with refund facts per template","`guest.message.send`","send logged"),
    ("4","13","Guest record reflects cancellation, refund, and any human decisions verbatim","(record entries)","chronology complete"),
   ]),
  ],
  gates=["A cancellation is never silently reversed - an un-cancel is a NEW booking against live inventory (06's tuple).",
         "Refunds beyond the published rule move only on signed `payment.authority`."]),

 dict(num="P04", slug="group-booking", name="Group Booking",
  desc="Swarm deployment: group inquiry to contract-ready package and managed block. Agents 01, 07, 03, 02, 08, 10, 13, 04. The human signs contracts; the swarm builds the plan and holds the block inside the same capacity ceiling as everything else.",
  trigger="`group.inquiry` at 07.",
  pre=["Published group tier schedule and block rules are current."],
  phases=[
   ("Phase 1 - Plan assembly (parallel)", [
    ("1","07","Assemble the plan: block size, dates, supervision-ratio facts for minor groups (counts only, COPPA)","(plan draft)","plan draft with published-rule basis"),
    ("2","03","Group tier pricing per the published schedule","`quote.package` → 07, 13","tier quote sourced"),
    ("3","07","Route individual accommodation needs to 08 - group scale never dilutes individual accommodation","`accessibility.request` → 08","each need in 08's lane"),
    ("4","07","Group add-ons (catering, events) per published offerings","`addon.request` → 10","add-on set attached to the plan"),
   ]),
   ("Phase 2 - Block and package", [
    ("5","07","Commit the block via the plan within block rules and the capacity ceiling","`group.plan` → 02, 03, 13","block on inventory with release date"),
    ("6","07","Contract-ready package to the human: plan, pricing, custom requests verbatim","(human queue)","human signs or directs; decision recorded via 13"),
    ("7","04","Milestone messages (deposits, rooming lists, final counts) per template","`guest.message.send`","milestone sends logged"),
   ]),
  ],
  gates=["Contracts, custom pricing, and liability terms are human-signed - the swarm packages, never commits.",
         "Final counts exceeding the block do not stretch it (07's tuple) - waitlist or human decision."]),

 dict(num="P05", slug="accessibility-accommodation", name="Accessibility Accommodation",
  desc="Swarm deployment: accommodation request to a human-decided, coordinated accommodation. Agents 08, 13, 04, plus 02 for accessible inventory. THE LINE: no request is denied, narrowed, or negotiated by the swarm - every plan goes to a trained human.",
  trigger="`accessibility.request` at 08, from any surface (intake, group, reply routing).",
  pre=["The request text travels verbatim; only accommodation-necessary details are gathered - never diagnosis solicitation."],
  phases=[
   ("Phase 1 - Respectful intake and plan", [
    ("1","08","Intake the stated need; gather only what the accommodation requires","(intake record, custody-flagged)","need on record verbatim"),
    ("2","08","Assemble the plan: matching options (accessible inventory, published programs), gaps named","`accessibility.plan` → human, 13","plan delivered to the trained human - the ONLY decision lane"),
   ]),
   ("Phase 2 - Human decision, swarm coordination", [
    ("3","08","Coordinate the approved plan: accessible-room holds, program enrollment, operational flags","(coordination per decision)","every element verified landed"),
    ("4","04","Accommodation communications on accommodation-approved templates - warm, specific, never negotiation-toned","`guest.message.send`","sends logged"),
   ]),
  ],
  gates=["'No' is a word this playbook does not contain - gaps, exhaustion, and program mismatches all route to the human WITH alternatives, never as declines.",
         "Accommodation data is custody-flagged: need-to-know, never marketing, never general records beyond operational need."]),

 dict(num="P06", slug="closure-rebooking-wave", name="Closure Rebooking Wave",
  desc="Swarm deployment: human closure declaration to coordinated rebooking, waitlist, and remedy response. Agents 14, 06, 11, 12, 04, 13. The human declares; the swarm relays the declaration verbatim with its policy set and runs the wave.",
  trigger="Human closure declaration relayed by 14 as `closure.notice`.",
  pre=["The closure policy set (rebooking options, remedy set, waitlist effects) is attached to the declaration - a declaration without its policy set holds for human completion."],
  phases=[
   ("Phase 1 - Relay (immediate, parallel)", [
    ("1","14","Relay the declaration with policy set, narrower-scope rule on ambiguity","`closure.notice` → 06, 11, 12","relay logged with scope as declared"),
    ("2","11","Freeze affected waitlists per the policy","(waitlist state change)","freeze logged"),
   ]),
   ("Phase 2 - The wave", [
    ("3","06","Offer published rebooking options to affected reservations per policy order","`modification.result` per acceptance → 02, 05, 13","each rebooking atomic"),
    ("4","12","Apply the closure remedy set; beyond-set requests route to human","`recovery.plan` → human, 13 (as needed)","remedies recorded with the set cited"),
    ("5","04","Wave communications per closure templates - operational facts, never weather promises","`guest.message.send`","sends logged"),
   ]),
   ("Phase 3 - Books", [
    ("6","14","Wave results into the EOD books: rebooked, refunded, pending, unreachable - all counted","`report.package` → human","wave section complete with gaps named"),
   ]),
  ],
  gates=["The swarm never declares, extends, or lifts a closure - relay only (14's legal line).",
         "Scope ambiguity runs the narrower scope until the human expands it."]),

 dict(num="P07", slug="waitlist-promotion", name="Waitlist Promotion",
  desc="Swarm deployment: freed inventory to fair-order promotion through the normal booking path. Agents 11, 01, 02, 04, 13. The waitlist grants order, never inventory - every promotion re-enters through a live hold.",
  trigger="02 reports freed inventory matching a waitlist head-of-line.",
  pre=["The waitlist is in published fair order; the freed inventory is verified by 02, not inferred."],
  phases=[
   ("Phase 1 - Offer", [
    ("1","11","Issue the expiring promotion offer to the next party that FITS (skips logged, positions kept)","`waitlist.promote` → 01, 13","offer with expiry on record"),
    ("2","04","Offer message per template with the expiry stated","`guest.message.send`","send logged"),
   ]),
   ("Phase 2 - Normal path", [
    ("3","01","On acceptance, run P01 Phase 1-2: live hold, published quote, confirm","`booking.confirm` → 02, 05, 13","promotion converted through the front door - no bypass"),
    ("4","11","On expiry, offer passes per rule; position handling per publication","(list state change)","expiry logged; next offer issued"),
   ]),
  ],
  gates=["Promotion never bypasses 02's hold path - the waitlist cannot create capacity (11's legal line).",
         "Order changes for consideration are integrity violations, full stop."]),

 dict(num="P08", slug="complaint-recovery", name="Complaint Recovery",
  desc="Swarm deployment: complaint to facts-based recovery inside the published remedy table, with human decisions beyond it. Agents 12, 13, 05, 04. Injuries and safety matters exit to humans immediately - recovery never handles a safety matter as a service matter.",
  trigger="`complaint.intake` at 12, or complaint content in 04's reply routing.",
  pre=["Safety/injury screen runs FIRST on every complaint - a safety hit escalates before any recovery step."],
  phases=[
   ("Phase 1 - Facts first", [
    ("1","12","Assemble the fact base from records before any response beyond acknowledgment","`record.request` → 13","chronology attached"),
    ("2","04","Acknowledgment per template - empathy and process facts, no fault statements","`guest.message.send`","ack logged"),
   ]),
   ("Phase 2 - Remedy", [
    ("3","12","Apply the published remedy table where it covers the case; record via 13","(remedy application)","remedy recorded with the table line cited"),
    ("4","12","Beyond the table: assemble the recovery plan for human decision - facts, timeline, options, guest impact","`recovery.plan` → human, 13","plan delivered; decision recorded"),
    ("5","05","Any refund basis executes on rules or signed authority","`refund.record` → 12, 13","record carries rule or authority"),
    ("6","04","Resolution communication per template after the decision","`guest.message.send`","send logged with the decision reference"),
   ]),
  ],
  gates=["Injury, safety, and legal-threat content escalates to humans immediately and verbatim - before recovery scripting (12's legal line).",
         "No fault or liability admissions in any guest communication."]),

 dict(num="P09", slug="morning-operations", name="Morning Operations",
  desc="Swarm deployment: the operations morning book. Today's arrivals, capacity picture, weather outlook facts, waitlist state, yesterday's exceptions - assembled from records for human review before gates open. Agents 14, 13, 11.",
  trigger="Scheduled daily start (owner-configured time) or owner command.",
  pre=["EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED, never silently thinner."],
  phases=[
   ("Assemble (parallel, all to human review)", [
    ("1","14","Pull today's arrivals and yesterday's exceptions from the record","`record.request` → 13","arrivals + exceptions sections sourced"),
    ("2","14","Capacity picture from 11's alert stream and utilization facts","(from `capacity.alert` stream)","capacity section current"),
    ("3","14","Weather outlook facts and operational status - facts with timestamps, never predictions-as-promises","(monitoring pull)","outlook section sourced"),
   ]),
   ("Present", [
    ("4","14","Deliver the morning book; unavailable sources marked absent","`report.package` → human","book delivered; the human directs, the book never self-executes"),
   ]),
  ],
  gates=["A source unavailable at assembly time is a named absence - never yesterday's numbers backfilled (14's tuple)."]),

 dict(num="P10", slug="end-of-day-books", name="End-of-Day Books",
  desc="Swarm deployment: the closing books. Bookings, changes, cancellations, capacity events, recovery cases, the missed-item sweep against the morning book. Agents 14, 13. Gaps named; a clean-looking book with hidden gaps is the named failure.",
  trigger="Scheduled day end (owner-configured time) or owner command.",
  pre=["The morning book (P09) exists as the sweep baseline; if absent, the sweep names that first."],
  phases=[
   ("Assemble", [
    ("1","14","Pull the day's activity chronology: bookings, changes, cancellations, promotions, recoveries","`record.request` → 13","activity section sourced with timestamps"),
    ("2","14","Capacity events reconciliation: alerts fired, closures relayed, waves run","(from alert stream + records)","capacity reconciliation complete"),
    ("3","14","Missed-item sweep: every morning-book item without a day touch, named with its owner","(sweep vs. P09 baseline)","sweep complete; no silent reassignment"),
   ]),
   ("Present", [
    ("4","14","Deliver the EOD books","`report.package` → human","books delivered; P10 completion event logged for tomorrow's P09"),
   ]),
  ],
  gates=["The sweep never reassigns - it names (14's tuple). Reassignment is the human's morning decision."]),

 dict(num="P11", slug="safety-incident-handoff", name="Safety Incident Handoff",
  desc="Swarm deployment: safety matter detected anywhere to verbatim human handoff with the service lanes frozen. Agents 01/04/12 (detection), 13, 14. Absolute line 5 executing: safety matters are never service matters - no scripting, no statements, ever.",
  trigger="`safety.notice` from any detection point: intake (01), guest channel (04), or a recovery conversation (12).",
  pre=["The matter is captured verbatim with source, timestamp, and guest/booking reference - the handoff carries the guest's words, not a summary."],
  phases=[
   ("Phase 1 - Handoff (same turn)", [
    ("1","01/04/12","Route the matter verbatim; the service conversation stops","`safety.notice` \u2192 human, 13, 14","verbatim record delivered, human alerted"),
    ("2","14","Ops visibility same turn; on-the-ground response is human territory","(ops log; `agent.status` \u2192 14 for any waiting lane)","ops aware inside the turn"),
   ]),
   ("Phase 2 - Freeze and record", [
    ("3","12","Any recovery case for this guest freezes pending human direction","(hold)","frozen case named with reason"),
    ("4","13","Incident reference on the guest record - verbatim, custody-flagged","`interaction.log`","record complete, content verbatim"),
   ]),
  ],
  gates=["No safety statement, reassurance, apology-implying-fault, or recovery scripting from any agent - the swarm's only move is the verbatim handoff.",
         "No service or marketing contact to this guest until explicit human direction - the freeze is guest-wide, not conversation-wide."],
  completion="Verbatim handoff delivered same turn, ops visible, service lanes frozen for the guest, record complete; human owns everything after.",
  abort=["Ambiguity about whether a matter is safety: treat it as safety - the conservative read is the only read (line 5 doctrine).",
         "Guest continues messaging after handoff: received, logged, routed verbatim; no swarm reply."]),

 dict(num="P12", slug="ops-change-wave", name="Operational Change Wave",
  desc="Swarm deployment: operational change short of closure (ride down, hours change, weather posture) to re-anchored inventory and informed guests. Agents 14, 02, 06, 11, 04, 13. The smaller sibling of P06 - closures stay closure.notice; the two waves never blur.",
  trigger="`event.change.notice` at 02/06/11/13 from 14 (operations/weather).",
  pre=["The change is a recorded operational fact with its effective window - a rumor is not a wave trigger."],
  phases=[
   ("Phase 1 - Re-anchor", [
    ("1","02","Availability re-anchored; affected holds and sales enumerated","`availability.result` \u2192 01, 03 (as needed)","inventory reflects the fact; ceiling re-checked, never assumed"),
    ("2","11","Waitlist/capacity re-anchored; promotions pause until capacity re-confirmed","`capacity.alert` \u2192 queue, 14 (if triggered)","no promotion against unverified capacity"),
   ]),
   ("Phase 2 - Guests", [
    ("3","06","Affected bookings enumerated; options from published rules only","`modification.result` \u2192 02, 05, 13 (per booking)","every affected booking has a disposition or a hold"),
    ("4","04","Guest notices from posted facts and approved templates","`guest.message.send` \u2192 external","facts only - no speculation about duration or cause"),
   ]),
  ],
  gates=["The safety capacity ceiling is physics at every step - no re-accommodation exceeds it (absolute line 1).",
         "Beyond-published-rule remedies route for signed authority - the wave does not widen the money lane.",
         "No safety statements in guest notices - operational facts only (line 5)."],
  completion="Inventory and waitlist re-anchored, every affected booking dispositioned or held with reason, guests informed from posted facts.",
  abort=["Change escalates to closure: P06 closure-rebooking wave takes over; this playbook's record hands off cleanly.",
         "Capacity cannot be re-confirmed: promotions and re-accommodations hold; the unknown blocks the gate."]),

 dict(num="P13", slug="pricing-exception-cycle", name="Pricing Exception Cycle",
  desc="Swarm deployment: quote outside published tables to signed authority and a cited quote. Agents 03, 07, 13. Zero-threshold doctrine: published rules apply automatically with citation; everything else, any amount, is signed.",
  trigger="`pricing.exception` at human/13 from 03 - a requested quote (individual or group) falls outside the published tables.",
  pre=["The published-table computation is on record showing exactly where the request exits the rules - the exception names its delta."],
  phases=[
   ("Phase 1 - Package", [
    ("1","03","Exception package: published computation, requested terms, the delta as fact","`pricing.exception` \u2192 human, 13","every number carries its source"),
    ("2","13","Guest/group history attached (existence and facts, no judgment)","`record.response` \u2192 03","context complete"),
   ]),
   ("Phase 2 - Signed issue", [
    ("3","03","Quote issues only on signed authority, citing the envelope","(await `pricing.authority` \u2190 human); then `quote.package` \u2192 01/07, 13","signed envelope on the chain before the quote moves"),
   ]),
  ],
  gates=["No quote outside published tables issues unsigned - there is no discretion lane, no de-minimis exception (zero-threshold doctrine, ratified 2026-07-18).",
         "The exception and its approval travel together on the record - a cited quote is auditable end to end."],
  completion="Signed quote issued with the authority cited, or the exception declined/expired with that recorded the same way.",
  abort=["Authority not received before the quote's validity window closes: the exception expires on record; the guest is informed from published facts.",
         "Request mutates while pending: fresh exception package - a changed request is a new exception, never an edit to a pending one."]),

 dict(num="P14", slug="guest-data-request", name="Guest Data Request Response",
  desc="Swarm deployment: guest data access or deletion request to human-approved response inside the clock. Agents 13, 14, 04. Minors' custody flags honored per item (absolute line 4); release and deletion are human decisions.",
  trigger="Guest data access/deletion request lands via 04 (guest channel) or 01 (intake).",
  pre=["The request is captured verbatim with date, requester identity basis, scope, and the applicable response window."],
  phases=[
   ("Phase 1 - Clock and inventory", [
    ("1","14","Response clock visible in operations reporting","(ops clock; `report.package` carries it)","clock live in the daily book"),
    ("2","13","Disclosure inventory: existence, type, date, source per item; minors' custody flags named","`records.disclosure.package` \u2192 human, 14","inventory delivered inside the window's lead-time"),
   ]),
   ("Phase 2 - Human decision and response", [
    ("3","13","Record the human's release/deletion decision and execution","`record.response` + `interaction.log`","itemized decision record: who, what, when, under whose approval"),
    ("4","04","Respond to the guest per the approved scope, from templates","`guest.message.send` \u2192 external","response artifact on record"),
   ]),
  ],
  gates=["Nothing beyond the human's itemized approval is disclosed or deleted - the approval is the ceiling.",
         "Identity verification questions route to the human - the swarm never adjudicates who is entitled to a minor's data (line 4).",
         "Deletion touching financial/audit records routes with the retention obligation named - conflicting duties are human calls."],
  completion="Human-approved response delivered inside the clock with a complete itemized record; or refusal/clarification recorded the same way.",
  abort=["Requester identity cannot be established from the record: human decision before any data moves.",
         "Scope ambiguous or overbroad: clarification before any work product leaves the swarm."]),
]
