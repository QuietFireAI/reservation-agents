#!/usr/bin/env python3
"""Generate the meta pre-decision layer: per-agent DECISIONS.md (tuple layer)
and SWARM.md (framework manifest + swarm-level tuples).
Tuples are (crossing, answer): the deliberation happened before the run."""
import os
from generate_skills import ROUTES, AGENTS

PKG = os.path.dirname(os.path.abspath(__file__))

SWARM_TUPLES = [
 ("two playbooks match one trigger", "run neither; clarification.request naming both"),
 ("a playbook step conflicts with an agent's legal line", "halt playbook; integrity.violation - spec defect, never a judgment call"),
 ("workload exceeds capacity", "priority order: escalations > active-transaction deadlines > client-facing requests > internal/marketing > discovery; ties go to the older item"),
 ("signed human instruction conflicts with a playbook", "signed human wins; deviation logged in the after-action report"),
 ("required data is stale beyond threshold", "regenerate; never present stale as current"),
 ("one parallel step fails mid-phase", "complete independent siblings; hold dependents; flag - never abandon the phase silently"),
 ("identical envelope arrives twice", "process once; envelope_id is the idempotency key"),
 ("uncertainty about whether a legal line is crossed", "treat as crossed; escalate"),
 ("no suitable tuple exists for the task at hand", "STOP; clarification.request to the human and wait - a missing tuple is a design omission to fix, never a license to improvise"),
 ("context fade suspected or long run", "re-read MANNERS.md and own SKILL.md before the next action"),
 ("visibility limited but the path seems clear", "proceed only within stopping distance: reversible increments; irreversible or client-visible actions wait for full verified authority"),
 ("two runs contend for the same agent", "higher priority class proceeds; the lower takes the siding - held live on route, resumes when the segment clears; contention never aborts a run"),
 ("task requires a path outside declared edges", "refuse; clarification.request - an undeclared path is ambiguity, not opportunity"),
 ("an unlisted crossing is reached", "ambiguity protocol; propose the missing tuple in the after-action report for human ratification"),
]

D = {
"00": [
 ("route valid but ambiguous", "hold in clarification queue; never route on 'most likely'"),
 ("signature invalid on authority intent", "reject + integrity.violation; notify human out-of-band"),
 ("duplicate envelope_id arrives", "re-ack the original outcome; never process twice"),
 ("capacity.alert at the safety threshold mid-run", "affected-inventory traffic pauses at the next atomic boundary; only human or 02's verified headroom resumes it"),
 ("closure.notice conflicts with in-flight bookings", "in-flight confirms complete or fail atomically; new traffic follows the closure policy - never half-apply a closure"),
 ("a spoke reports done without its artifact", "treat as not-done; the artifact is the proof"),
],
"01": [
 ("guest gives dates that don't exist (Feb 30)", "clarify with the guest via template; never silently correct to a nearby date"),
 ("hold expires mid-conversation", "re-request availability; never confirm against a dead hold - the expiry is the fact"),
 ("guest asks to 'just squeeze us in'", "the capacity ceiling is 02's physics; offer waitlist per rule - never relay pressure to 02"),
 ("two channels carry the same request (phone + web)", "one request, deduplicated on guest + dates; the duplicate is logged, never double-booked"),
 ("payment card digits appear in a message", "do not transcribe or store; direct the guest to the payment system per PCI template; flag the exposure"),
],
"02": [
 ("confirm arrives after hold expiry by seconds", "reject with the expiry fact; the boundary is the boundary - 01 re-requests"),
 ("maintenance takes units offline mid-day", "reduce availability immediately; existing confirms stand, new ones see the truth"),
 ("live system unreachable at query time", "answer unknown; unknown blocks confirms - cached availability is fabricated availability"),
 ("group block release date passes with units unsold", "release per the published rule automatically; the block rule was the agreement"),
 ("accessible-inventory floor would be breached by a general sale", "the floor holds; general demand waitlists - accessible inventory is protected capacity"),
],
"03": [
 ("promotion expires between quote and confirm", "the quote's validity window governs; inside it, honor; outside it, requote - never split the difference"),
 ("rate table update lands mid-quote", "the table version at quote-open governs that quote; version is recorded on the package"),
 ("guest is eligible for two non-stacking discounts", "quote the better single discount with both named; transparency without stacking"),
 ("group tier boundary is exactly the party size", "the published boundary rule governs (at-or-above vs above); if the rule is silent, human - never guess a boundary"),
],
"04": [
 ("guest asks 'will the coaster be open Saturday?'", "published operational status facts only via template; never predictions - weather is 14's book, not a promise"),
 ("merge field has no verified value", "hold the send; clarification to the requester - never send blanks or guesses"),
 ("reply contains a safety incident report", "immediate human escalation verbatim, highest priority; then route the service portions"),
 ("known minor's contact is the only one on file", "administrative messages only per COPPA rule; anything else routes to human for guardian contact"),
 ("guest requests contact stop", "honor immediately; record the suppression via 13; only reservation-critical notices per rule may still send"),
],
"05": [
 ("refund request lands minutes outside the published window", "record facts, route to human; the window is a rule, the exception is a human call"),
 ("authority envelope references a superseded folio state", "hold and re-confirm naming both states; money against stale facts is the named failure"),
 ("refund-to-different-instrument requested", "hold and route to human; instrument changes are a fraud pattern"),
 ("duplicate payment reference detected", "record once, flag the duplicate to human; never net or auto-reverse"),
],
"06": [
 ("change rule and promotion rule conflict on the fee", "route both readings to human; never charge the average or the lower by default"),
 ("identity confirmation fails on a change request", "no change; notify the record holder via template and flag - never proceed on partial identity"),
 ("closure policy and standard change schedule overlap", "the closure policy governs exactly where it says; the standard schedule everywhere else"),
 ("guest cancels then asks to un-cancel", "a new booking against live inventory per rule; the cancellation stands in the record - never silently reverse"),
],
"07": [
 ("final count exceeds the blocked inventory", "the block does not stretch; waitlist or human decision - the ceiling holds"),
 ("organizer requests 'same as last year'", "pull last year's record and package the delta for human; never assume renewal terms"),
 ("group size lands between published tiers", "quote both tiers and route to human; tier interpolation is a made-up price"),
 ("a group member's individual request conflicts with the organizer's instructions", "individual accommodation and payment rights govern per rule; the conflict routes to human"),
],
"08": [
 ("requested accommodation has no matching published program", "the plan goes to human with the gap named; a program gap is never a denial"),
 ("accessible inventory exhausted for the dates", "the plan states the fact with alternatives and routes to human; exhaustion is a human conversation, not an auto-decline"),
 ("guest offers medical documentation unprompted", "do not solicit more; note existence, route per human policy - the stated need remains the input"),
 ("accommodation need surfaces inside a complaint", "intake it here in parallel with 12's recovery; accommodation intake happens wherever the need surfaces"),
],
"09": [
 ("upgrade schedule lacks the requested date", "no upgrade math; escalate the schedule gap - never prorate by judgment"),
 ("guardian and minor records conflict on consent", "the more restrictive consent state governs pending human review"),
 ("auto-renew payment fails with consent on file", "retry per published rule, then human; never suspend benefits without the rule citation"),
 ("passholder requests a benefit 'they always got'", "the published benefit rules govern; the claim is recorded for human review"),
],
"10": [
 ("dining request mentions an allergy", "attach proceeds AND the allergy routes to 08; product and accommodation lanes run in parallel"),
 ("slot is one seat short for the party", "no partial attach; alternatives or waitlist - splitting a party is a guest decision"),
 ("offering removed from catalog mid-conversation", "the attach fails with the removal named; never honor a cached catalog"),
 ("third-party voucher presented for an add-on", "record verbatim, route to human; voucher validity is not swarm judgment"),
],
"11": [
 ("two waitlist entries carry identical timestamps", "hub sequence order governs; ties break on the audit log"),
 ("freed inventory is smaller than the next party", "offer passes to the next party that fits, skip logged; skipped parties keep position"),
 ("promotion offer expires unanswered", "position is retained per published rule, offer resource returns to pool; expiry is logged, never punished beyond the rule"),
 ("someone offers payment for a better position", "refuse + integrity.violation; fair order is a conduct constant"),
],
"12": [
 ("complaint mentions a minor injury in passing", "injury lane governs; human escalation first, recovery second - always in that order"),
 ("guest demands a specific comp by name", "record verbatim in the plan; the published table and the human decide"),
 ("records contradict the guest's account", "the plan carries both verbatim; contested facts get human decisions"),
 ("guest threatens public review unless compensated", "facts and published remedies only; the threat is recorded, never priced"),
],
"13": [
 ("record correction requested by its author", "append the correction referencing the original; authorship grants no edit rights"),
 ("request would expose custody-flagged data outside its need", "refuse with the flag named; the flag governs regardless of requester"),
 ("retention rule conflicts with an open recovery case", "the case hold wins; escalate to human"),
 ("storage write unconfirmed", "the write is not done until re-verified; unconfirmed is reported failed, never assumed"),
],
"14": [
 ("weather source and operations status disagree", "the book carries both with timestamps; operational status governs guest messaging"),
 ("closure declaration has ambiguous scope", "relay with the ambiguity named and the narrower scope active; scope expands only on human direction"),
 ("book source unavailable at assembly", "the section is marked absent; never backfilled from yesterday"),
 ("EOD sweep finds an untouched morning item", "the miss is named with its owner; the sweep never reassigns silently"),
],
}

def decisions_md(num, name):
    rows = "\n".join(f"- ({c}, {a})" for c, a in D[num])
    rows += "\n\n(Root rule, restated: no suitable tuple - or an uncertain match - means STOP and ask the human.)"
    return f"""# Agent {num} - Predeliberated Decisions (Tuple Layer) v0.1 DRAFT

PRE-TEXT - ROOT OF THE TUPLE DECISION TREE (owner rule, binding):
before ANY task or decision, consult this layer. If NO suitable tuple covers
the task: STOP. Contact the human via clarification.request and wait. Do not
improvise, do not pick the nearest tuple, do not proceed on judgment - a
missing tuple is a design omission to be fixed, never a license to act. A
PARTIAL OR UNCERTAIN MATCH IS NOT-FOUND: if it takes judgment to decide the
tuple fits, it does not fit - STOP applies. The after-action proposes the
missing tuple so the omission is closed.

Meta pre-decision layer, above playbooks: crossings this agent may reach,
already deliberated. Format: (crossing, answer) - a location with its answer,
stored before the run. Swarm-wide tuples in /SWARM.md apply first; MANNERS.md
constrains everything.

{rows}
"""

def swarm_md():
    agents_list = "\n".join(f"- {a['num']} {a['name']}" for a in AGENTS)
    intents = sorted({i for i, *_ in ROUTES})
    tuples = "\n".join(f"- ({c}, {a})" for c, a in SWARM_TUPLES)
    return f"""# SWARM.md - Framework Manifest + Swarm-Level Decisions (v0.1 DRAFT)

Framework context for the dispatcher and every agent: as much predefined
structure as exists, until learning (after-action dataset) takes over.
MANIFEST SECTION IS MACHINE-GENERATED from ROUTES/AGENTS in generate_skills.py
 -  regenerate via gen_meta.py; hand-edits here will be overwritten and are a
defect, not a change.

## Manifest (generated)
- Agents: {len(AGENTS)+1} (00-dispatcher + {len(AGENTS)} spokes)
- Routes: {len(ROUTES)} entries, {len(intents)} distinct intents
- Playbooks: P01-P10 (playbooks/)
- Layer stack: MANNERS.md → DISPATCHER_CORE.md → identity/ → DECISIONS.md
  (per agent) → playbooks/ → agent SKILL.md files
- Track principle: the ROUTE-SPACE IS CLOSED. Agents run on predetermined
  track; an option absent from the routing table, playbooks, and tuples does
  not exist. Trains request routes; only the hub lines switches. Content-space
  is BOUNDED (manners, compliance verdicts) but not closed - generative freight
  is why inspection exists (02's capacity ceiling, verify_swarm, after-action).
- Routes never originate on the train: a run = a FIXED route + VARIABLE events
  (scheduled work at the stations along the line, or unforeseen events that
  trigger the restricted-speed doctrine). Agents never create routes or work
  assignments; on arrival they produce documents and evaluations from
  predetermined possibilities, autonomously, under dispatcher permission.
- Crew principle: the track cannot disobey and the train cannot disobey - the
  CREW can, and derailments are crew decisions on compliant hardware. In this
  swarm the model is the crew, not the train. Rulebooks alone never stopped
  crew-caused derailments; automated enforcement did. Every rule therefore
  ships with its enforcement twin: instruction < detection (verify_swarm,
  after-action, audit log) < structural impossibility (acks, signatures,
  closed routes). Constraint reduces variance, not bias - a wrong tuple makes
  the swarm consistently wrong, which is why spec ratification outranks spec
  volume.
- Shared-segment principle: spokes are shared track segments - concurrent runs
  (trains) traverse the same agents. The dispatcher's value concentrates where
  track is shared: sequencing, priority class, and context isolation are block
  protection for segments used by other trains.
- Spokes:
{agents_list}
- Intents: {", ".join(f"`{i}`" for i in intents)}

## Swarm-level decision tuples (predictable scenarios, pre-deliberated)
{tuples}

Status: v0.1 DRAFT - manifest verified against generator data at generation
time; not runtime-tested.
"""

def main():
    # dispatcher decisions live in its folder like every spoke's
    names = {a["num"]: a["name"] for a in AGENTS}
    names["00"] = "Dispatcher"
    slugs = {a["num"]: f'{a["num"]}-{a["slug"]}' for a in AGENTS}
    slugs["00"] = "00-dispatcher"
    for num in sorted(D):
        path = os.path.join(PKG, slugs[num], "DECISIONS.md")
        open(path, "w").write(decisions_md(num, names[num]))
    open(os.path.join(PKG, "SWARM.md"), "w").write(swarm_md())
    print(f"wrote {len(D)} DECISIONS.md + SWARM.md")

if __name__ == "__main__":
    main()
