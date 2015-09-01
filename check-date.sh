#! /bin/sh
#
# check-date.sh
# Copyright (C) 2015 djp <djp@transit>
#
# Distributed under terms of the MIT license.
#


# this script checks all +PENDING or +WAITING tasks, resetting the
# effective-date, if needed.  It is intended for initial and occasional use,
# trusting that the on-modify-edate-hook will keep most new or modified tasks
# in line.
