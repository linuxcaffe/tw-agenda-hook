#!/usr/bin/env python
#
# PoC of djpstuff. https://github.com/linuxcaffe/tw-effective-date-hook
#
# Save as on-add_agenda.py in hooks directory, then change to hooks folder and:
#  $ ln -s on-add_agenda.py on-modify_agenda.py
#  $ chmod +x on-add_agenda.py
#
# UDA needed:
# uda.edate.label=edate
# uda.edate.type=date
#
# UDA needed for checking all tasks:
# uda.edate_checkall.label=foobar
# uda.edate_checkall.type=string
#
# In order to set an edate on existing tasks, run:
#  $ task modify edate_checkall:DOITNOW

import json
import sys

def do_djp_stuff(task):
    edate = None
    for d in ["wait", "until", "due", "scheduled"]:
        if d in task:
            edate = task[d]
    if "date" in task and not edate:
        del task["edate"]
    elif edate:
        task["edate"] = edate

    # This is for retroactively adding "edate" to all tasks. See above.
    if "edate_checkall" in task:
        del task["edate_checkall"]

    print(json.dumps(task))


old = sys.stdin.readline()
new = sys.stdin.readline()

if not new:
    do_djp_stuff(json.loads(old))
else:
    do_djp_stuff(json.loads(new))
