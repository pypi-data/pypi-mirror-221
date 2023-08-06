"""
Usage: odoo-manager run [--args=<build_args>] [-d | --detach] [--show-cmd]
                        [--compose=<compose_file>] [-u | --update] [--rebuild]
                        [-v | --verbose] [-h | --help]

Options:
  --args=<build_args>       Specify the ODOO_FLAGS to be used
  --compose=<compose_file>  The docker compose file to be used
  -d, --detach              Detached mode: Run containers in the background
  -h, --help                Show this screen
  --rebuild                 (not implemented...) Rebuild the container before running the command
  --show-cmd                Output the `docker compose up` command being run
  -u, --update              (not implemented...) Update the build before running the command
  -v, --verbose             Output additional information, where possible

"""
# TODO: Remove unused options. See docstring above for reference.
# TODO: Remove `--show-cmd` and merge that functionality into `--verbose`

from invoke import UnexpectedExit
from odoo_manager.core import configs, shell, validation
from odoo_manager.core.git import redirect
from .base import BaseCommand


class Run(BaseCommand):
    """
    Represents the `odoo-manager run` command which runs the current odoo
    project locally.
    """

    def run(self):
        """
        Runs the command. See the parent class for more details about how
        commands are organized and ran.

        :return {NoneType}:
        """
        validation.check_env(configs.config, ["PIP_EXE", "ODOO_EXE", "LOCAL_PORT"])

        if self.options.get("--rebuild", False):
            # Tasks.build(ctx, update=update, verbose=verbose)
            shell.out("Rebuild is not supported yet.", color="yellow")
            exit(0)

        args = self.options.get("--args", "")
        if (
            args
            and ("-i" in args or "--install" in args or "-u" in args or "--upgrade" in args)
            and ("-d" not in args and "--database" not in args)
        ):
            shell.out("Make sure you include the -d flag when trying to upgrade or install modules.", color="yellow")
            exit(1)

        compose = self.options.get("--compose", False)
        verbose = self.options.get("--verbose", False)
        detach = self.options.get("--detach", False)

        # We are going to rewrite args every time no matter if it was passed
        # in or not. We don't want to run into a situation where a user uses
        # args once, and then has the same flags passed in over and over since
        # the odoo.env file will be written.
        #
        # If the user passes in args, then the next time does not, we should
        # assume we need to write an empty string to the odoo.env.
        if configs.config.has_option("options", "ODOO_FLAGS"):
            configs.config["options"].update({"ODOO_FLAGS": args or ""})
            with open(".env", "w") as configfile:
                configs.config.write(configfile, space_around_delimiters=False)

        shell.out("Running project...")
        if not verbose:
            shell.out(
                "You are not running in verbose mode, so container logs/output will not appear here. Tail "
                "logs or run this command with the --verbose flag to see output. It may take a minute for "
                "all containers to fully start.",
                color="yellow",
            )
        shell.out("  detach?: {}".format(detach), color="light_grey")
        shell.out("  args:    {}".format(args or "None"), color="light_grey")
        shell.out("  port:    {}".format(configs.config.get("options", "LOCAL_PORT")), color="light_grey")
        shell.out(
            "  url:     http://localhost:{}".format(configs.config.get("options", "LOCAL_PORT")), color="light_grey"
        )

        try:
            cmd = "docker compose {} up {}{}".format(
                f"-f {compose}" if compose else "",
                "-d" if detach else "",
                redirect(verbose),
            )

            self.ctx.run(cmd, echo=verbose)
        except UnexpectedExit as e:
            # Handle the unexpected exit while trying to run docker compose up.
            # There are a couple of scenarios. We only care about an error code
            # "1" coming back which means that our program died on it's own. We
            # do not care about the user stopping the command with a ctrl-c
            # input.
            if e.result.exited == 1:
                shell.out(
                    "There was a problem running docker compose.{}".format(
                        " Try again with --verbose to see the error information." if not verbose else ""
                    ),
                    color="magenta",
                )
