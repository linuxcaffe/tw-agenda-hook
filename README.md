# tw-effective-date-hook
a hook script to synthesize the value of a date:date uda, to be used with taskwarrior (http://taskwarrior.org) in the quest to arrive at an effecive agenda report, among other benefits. 

status:proposal

A task can have several dates; due-date, scheduled, until-date or wait-date. This hook script populates a new uda; "date" with the "effective date". If a task has any of these four dates, the effective date is a hierachy of scheduled --> due --> until --> wait. That means
- if it has a sched:date, it's the sched:date
- if it has no sched:date, but a due:date, it's the due:date
- if no due:date, but an until:date, it's the until:date
- if it has no until:date, but a wait:date, it's the wait:date
- if no wait:date (or any of the others) it has no effective date at all, the uda is cleared.
- 
The hook script regenerates the date:date (if needed) on-modify and on-add, keeping the effective-date up-to-date.

In order to regenerate the effective date uda for every task in your data, an external (non-hook) script (check-date.sh) could be run occasionally, to reset older tasks, or anything that might have slipped through the cracks. 

This will provide improved use of the scheduled attribute and a chronological sorting of tasks using multiple date-fields, a.k.a. agenda.

It doesn't matter which language this hook script is written in. It should be as simple as possible, but no simpler.  



