#!/usr/bin/env python3
# on-add_agenda.py / on-modify_agenda.py
#
# Maintains the edate (effective date) UDA — the earliest of any scheduled,
# due, until, or wait dates present on the task. This lets agenda reports show
# tasks in a single chronological sequence regardless of which date type is set.
#
# https://github.com/linuxcaffe/tw-agenda-hook
#
# Install:
#   cp on-add_agenda.py ~/.task/hooks/
#   ln -s on-add_agenda.py ~/.task/hooks/on-modify_agenda.py
#   chmod +x ~/.task/hooks/on-add_agenda.py
#
# UDA required (or use agenda.rc):
#   uda.edate.type=date
#   uda.edate.label=edate
#
# Retroactive update (existing tasks without edate):
#   task ( +PENDING or +WAITING ) modify +edate_checkall

import json
import sys


def create_edate(task):
    # Earliest of any date fields present — TW date strings are YYYYMMDDTHHMMSSZ
    # which sort correctly as plain strings.
    dates = [task[d] for d in ("scheduled", "due", "until", "wait") if d in task]
    if dates:
        task["edate"] = min(dates)
    elif "edate" in task:
        del task["edate"]

    # Retroactive batch update: remove the trigger tag after processing
    if "tags" in task and "edate_checkall" in task["tags"]:
        task["tags"].remove("edate_checkall")

    print(json.dumps(task))


task_line = ""
try:
    old_line = sys.stdin.readline()
    new_line = sys.stdin.readline()
    task_line = (new_line if new_line.strip() else old_line).strip()
    if not task_line:
        sys.exit(0)
    task = json.loads(task_line)
except (json.JSONDecodeError, ValueError) as e:
    print(f"[agenda-edate] JSON parse error: {e}", file=sys.stderr)
    if task_line:
        print(task_line)  # pass through unchanged
    sys.exit(0)

create_edate(task)
