"""
Usage: odoo-manager stop [-h | --help]

Options:
  -h, --help                Show this screen

Stop all containers running in this directory.

"""

from odoo_manager.core import shell
from odoo_manager.core.git import redirect
from .base import BaseCommand


class Stop(BaseCommand):
    """
    Represents the `odoo-manager stop` command which shuts down the running
    instances locally for the current odoo project.
    """

    def run(self):
        """
        Runs the command. See the parent class for more details about how
        commands are organized and ran.

        :return {NoneType}:
        """
        shell.out("Stopping containers...")
        self.ctx.run("docker compose stop{}".format(redirect(verbose=False)))
        shell.out("Containers stopped.")
