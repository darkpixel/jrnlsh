#!/usr/bin/env python3

from cmd import Cmd
from subprocess import Popen
from shlex import quote

import shutil
import sys

class JrnlShell(Cmd):
    def run_command(self, command):
        process = Popen(command, shell=True)
        process.wait()

    def default(self, line):
        self.run_command('jrnl %s' % (quote(line)))

    def do_list(self, line):
        self.run_command('jrnl -from today')

    def do_edit(self, line):
        self.run_command('jrnl --edit')

    def do_quit(self, line):
        sys.exit(0)

    def do_exit(self, line):
        sys.exit(0)

    def do_EOF(self, line):
        sys.exit(0)

def run_cli():
    if shutil.which('jrnl') is None:
        raise(Exception('Unable to find \'jrnl\' command.  Is jrnl installed?'))

    prompt = JrnlShell()
    prompt.prompt = 'jrnl> '
    prompt.cmdloop()

if __name__ == '__main__':
    run_cli()
