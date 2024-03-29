jrnlsh.py
=========

This is a very simple program that makes working with jrnl (and timewarrior) a bit easier.

Any text entered at the prompt will automatically be passed to jrnl to make a new entry.  Text is automatically escaped too.

No more typing:

    jrnl 'I\'m going to conquer the world today'

Just type it into jrnlsh:

    jrnl> I'm going to conquer the world today
    [Entry added to default journal]
    jrnl>


# Commands

There are a few convenience commands available in jrnlsh:

## edit
Open up your jrnl in your preferred editor so you can make changes

## list
Show today's journal entries

## status
Show your most recent jrnl entry along with the current timewarrior entry

    jrnl> status
    2021-09-10 10:00 Just doin' stuff

    Tracking stuff
      Started 2021-09-10T09:10:00
      Current            10:14:14
      Total               1:04:14
    jrnl>

## start (and time)
Start a new timewarrior entry.  If there is a running timewarrior entry, it will be stopped and the new one will be started.  You can include tags after the start command.

    jrnl> start customer1 support phone
    Tracking customer1 support phone
    Note: 'customer1' is a new tag.
      Started 2021-09-10T10:16:13
      Current                  13
      Total               0:00:00
    jrnl>

## stop
Stop your currently running timewarrior entry.

    jrnl> stop
    Recorded customer1 support phone
      Started 2021-09-10T10:14:24
      Ended                 17:22
      Total               0:02:58
    jrnl>

## fill
Start a new time warrior entry with the ```:fill``` option.  You can use this in case you stop timewarrior, get up to leave your desk, then your phone rings, and you spend the next 20 minutes distracted on the call and forget to start timewarrior again.  ;)

    jrnl> fill customer1 support phone
    Backfilled to 2021-09-10T10:17:58
    Tracking customer1 support phone
      Started 2021-09-10T10:17:58
      Current               18:04
      Total               0:00:06
    jrnl>


## Status

There are 'day', 'week', 'month', and 'year' commands to display a summary from timewarrior.

    jrnl> week
    Wk Date       Day Tags     Start      End     Time    Total
    W2 2023-01-09 Mon pm, proj1 6:24:34 19:35:48 13:11:14 13:11:14
    W2 2023-01-10 Tue pm, proj2 5:54:01 17:40:26 11:46:25 11:46:25
    W2 2023-01-11 Wed pm, proj3 6:18:22 17:45:00 11:26:38 11:26:38
    W2 2023-01-12 Thu pm, proj4 6:16:52 18:05:55 11:49:03 11:49:03
                                                          48:13:20
    jrnl>

