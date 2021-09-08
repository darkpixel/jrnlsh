#!/usr/bin/env python3

from cmd import Cmd
from subprocess import Popen
from shlex import quote

import shutil
import sys

class JrnlShell(Cmd):
    def run_command(self, command):
        """ Run a command, wait for it to return. """
        process = Popen(command, shell=True)
        process.wait()

    def check_command(self, command):
        """ Check if a command exists, error if it does not exist. """
        if shutil.which(command) is None:
            raise(Exception('Unable to find \'%s\' command.' % (command)))

    def default(self, line):
        self.run_command('jrnl %s' % (quote(line)))

    def do_list(self, line):
        """ List today's jornal entries. """
        self.run_command('jrnl -from today')

    def do_edit(self, line):
        """ Edit your journal. """
        self.run_command('jrnl --edit')

    def do_quit(self, line):
        """ Exit """
        sys.exit(0)

    def do_time(self, line):
        """ Start a new timewarrior entry. """
        self.check_command('timew')
        self.run_command('timew start %s' % (line))

    def do_start(self, line):
        """ Start a new timewarrior entry. """
        self.check_command('timew')
        self.run_command('timew start %s' % (line))

    def do_stop(self, line):
        """ Stop the running timewarrior entry. """
        self.check_command('timew')
        self.run_command('timew stop')

    def do_fill(self, line):
        """ Start a new timewarrior entry and backfill it. """
        self.check_command('timew')
        self.run_command('timew start :fill %s' % (line))

    def do_status(self, line):
        """ Show the current status from jrnl and timewarrior. """
        self.check_command('timew')
        self.run_command('jrnl -n 1')
        self.run_command('timew')

    def do_exit(self, line):
        """ Exit. """
        sys.exit(0)

    def do_EOF(self, line):
        """ Exit. """
        sys.exit(0)

def run_cli():
    if shutil.which('jrnl') is None:
        raise(Exception('Unable to find \'jrnl\' command.  Is jrnl installed?'))

    prompt = JrnlShell()
    prompt.prompt = 'jrnl> '
    prompt.cmdloop()

if __name__ == '__main__':
    run_cli()
