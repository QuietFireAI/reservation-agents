#!/usr/bin/env python3
"""Generate playbooks P01-P14 for the DispatcherAgents Reservation swarm."""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playbooks")

def build(p):
    s = f'---\nname: {p["num"]}-{p["slug"]}\ndescription: "{p["desc"]}"\n---\n\n'
    s += f'# Playbook {p["num"]} - {p["name"]}\n\n'
    s += "**Swarm:** DispatcherAgents Reservation Swarm (Parks & Resorts)\n**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)\n**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)\n\n"
    s += "## Trigger\n" + p["trigger"] + "\n\n## Preconditions\n"
    for x in p["pre"]: s += f"- {x}\n"
    s += "Precondition unmet = playbook does not start; `clarification.request` to human.\n\n## Deployment sequence\n"
    for title, rows in p["phases"]:
        s += f"\n### {title}\n| Step | Agent | Action | Intent | Proof of done |\n|---|---|---|---|---|\n"
        for r in rows: s += "| " + " | ".join(r) + " |\n"
    s += "\n## HITL gates (hard stops)\n"
    for g in p["gates"]: s += f"- {g}\n"
    s += "\n## Completion criteria\n" + p["completion"] + "\n\n## Abort paths\n"
    for a in p["abort"]: s += f"- {a}\n"
    if p.get("notes"): s += "\n## Notes for the Dispatcher\n" + p["notes"] + "\n"
    return s

from reservation_playbooks import PB  # single source (fork-drift fix 2026-07-18)
CA = {
 "P01": ("Reservation confirmed against a live hold and published quote; inventory, folio, record, and confirmation all landed.",
   ["Hold expired before confirm: re-run Phase 1; never confirm against a dead hold.",
    "Availability unknown (system unreachable): confirms block; guest offered waitlist or later confirmation."]),
 "P02": ("Change applied atomically across inventory, billing, and records; guest confirmed.",
   ["Identity confirmation fails: no change; record holder notified; flag raised.",
    "Rule conflict on fees: both readings to human; the change holds."]),
 "P03": ("Cancellation executed per schedule; inventory released; refund recorded with rule or authority citation; record complete.",
   ["Out-of-rule refund request: facts to human; the cancellation itself completes."]),
 "P04": ("Contract-ready package delivered to the human; block committed within rules; milestones armed.",
   ["Custom terms requested: package to human; no swarm commitment.",
    "Block would breach the capacity ceiling or accessible-inventory floor: the block shrinks or waits - the ceiling holds."]),
 "P05": ("Human-decided accommodation coordinated end to end; every element verified landed; communications warm and specific.",
   ["Program gap or inventory exhaustion: plan to human WITH alternatives - never an auto-decline.",
    "Any pressure to decline in-swarm: integrity.violation - the decision lane is mandatory."]),
 "P06": ("Wave complete: affected reservations rebooked/refunded/pending all counted in the EOD books with gaps named.",
   ["Declaration arrives without its policy set: relay holds for human completion.",
    "Scope ambiguity: narrower scope runs; expansion only on human direction."]),
 "P07": ("Promotion converted through the normal hold/confirm path, or expired per rule with the next offer issued.",
   ["Freed inventory evaporates before the hold: offer is withdrawn with the fact named; position kept per rule."]),
 "P08": ("Recovery resolved inside the published table, or human-decided beyond it; all records cited; guest informed.",
   ["Safety/injury/legal content: immediate human escalation; recovery scripting stops."]),
 "P09": ("Morning book delivered with every section sourced or marked absent.",
   ["Record source down: section marked absent; book still delivers on time."]),
 "P10": ("EOD books delivered; sweep complete with owners named; completion event logged for tomorrow's P09.",
   ["Morning baseline absent: sweep names that first and proceeds on records alone."]),
}
for p in PB:
    if p["num"] in CA:
        p["completion"], p["abort"] = CA[p["num"]]

def main():
    os.makedirs(ROOT, exist_ok=True)
    for p in PB:
        d = os.path.join(ROOT, f"{p['num']}-{p['slug']}")
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "SKILL.md"), "w").write(build(p))
        print("emitted", p["num"])

if __name__ == "__main__":
    main()
