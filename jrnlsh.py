#!/usr/bin/env python3

from cmd import Cmd
from subprocess import Popen
import sys

class JrnlShell(Cmd):
    def default(self, line):
        print(line)
        cmd = 'jrnl %s' % (line)
        process = Popen(cmd, shell=True)
        process.wait()

    def do_quit(self, arg):
        sys.exit(0)

    def do_exit(self, arg):
        sys.exit(0)

    def do_EOF(self, arg):
        sys.exit(0)

if __name__ == '__main__':
    prompt = JrnlShell()
    prompt.prompt = 'jrnl> '
    prompt.cmdloop()
