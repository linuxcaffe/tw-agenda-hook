## tw-agenda-hook

is a taskwarrior extension that provides an edate (effective date) and agenda reports. With this hook installed, tasks can have any combination of scheduled, due, until or wait dates, and can then be sorted by edate (aka agenda) combining all of those into a coherent chronological order.

status: Working well, still in testing

caveat: Perpetual Proof of Concept, until a "real programmer" can apply some real expertise, but it worksforme.

see also: needs.txt help file for more detailed install/ config/ usage suggestions.

### Features
- hook-script automatically generates edate for all new and modified tasks
- check_edate script provided, to batch-process tasks when getting started

new reports;
- agenda
- agd (today)
- agt (tomorrow)
- agw (this week)
- agnw (next week)
- agm (this month)
- agnm (next month)
- agx (before now)
- edate (diagnostic, if edate and agenda give the same # of tasks, it's working)

These reports can be used in combination with any other task filters, so that 'task pro:foo agw' will ahow all foo task that are "on your agenda" this week. 

(edate can also be used in your own reports)

### Advantages

Without this extension, tasks can be sorted by due OR sched OR until OR wait, and the user has to choose which ONE of these dates to use as a primary sort. This forces the user to apply hard-due-dates (for example) where a sched:date might be more accurate. Similarly, with this extension, users can assign just a wait:date, or an until:date, or any combination, and those tasks will be shown in chronological sequence, along with tasks that might have only a due:date or sched:date. 

### Benefits

Taskwarrior users with this extension can assign the type of date (sched, due, until, wait) that makes sense for the specific task.

- due:date when tasks are actually due (have a hard deadline) 
- sched:date when you decide you want to do a task, but with no external deadline
- until:date for those tasks that can't be done after that date (like "go to event")
- wait:date for those tasks you don't want to see till then

and whatever combination of dates you choose, those tasks will be sorted together according to "effective date".

### Bugs

### Credits


