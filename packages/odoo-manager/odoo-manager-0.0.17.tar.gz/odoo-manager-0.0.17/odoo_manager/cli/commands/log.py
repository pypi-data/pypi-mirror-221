"""
Usage: odoo-manager log [--grep=<pattern>] [--grep-inverse=<pattern>]
                        [-v | --verbose] [-h | --help]

Options:
  --grep=<pattern>          Filter the log to only show lines matching this pattern
  --grep-inverse=<pattern>  Filter the log to hid lines matching this pattern
  -h, --help                Show this screen
  -v, --verbose             Output additional information, where possible

Output Odoo log file contents in real time and optionally filter the output
which is shown.

"""

import sys
from invoke.exceptions import UnexpectedExit
from .base import BaseCommand


class Log(BaseCommand):
    def run(self):
        """
        Runs the command. See the parent class for more details about how
        commands are organized and ran.

        :return {NoneType}:
        """
        grep = self.options.get("--grep")
        grep_inverse = self.options.get("--grep-inverse")
        verbose = self.options.get("--verbose")

        logfile = self.paths.base(".container/log/odoo.log")
        cmd = f"tail -f {logfile}"
        if grep_inverse:
            cmd += f" | grep --line-buffered -v {grep_inverse}"
        if grep:
            cmd += f" | grep --line-buffered {grep}"

        try:
            self.ctx.run(cmd, pty=True, echo=bool(verbose))
        # When the user kills the log output, suppress the error that is raised
        except UnexpectedExit as error:
            sys.exit(0)
