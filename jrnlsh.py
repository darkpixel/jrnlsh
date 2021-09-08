#!/usr/bin/env python3

from cmd import Cmd
from subprocess import Popen
from shlex import quote

import sys

class JrnlShell(Cmd):
    def default(self, line):
        cmd = 'jrnl %s' % (quote(line))
        process = Popen(cmd, shell=True)
        process.wait()

    def do_list(self, line):
        cmd = 'jrnl -from today'
        process = Popen(cmd, shell=True)
        process.wait()

    def do_quit(self, line):
        sys.exit(0)

    def do_exit(self, line):
        sys.exit(0)

    def do_EOF(self, line):
        sys.exit(0)

if __name__ == '__main__':
    prompt = JrnlShell()
    prompt.prompt = 'jrnl> '
    prompt.cmdloop()
