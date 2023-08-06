"""
Usage:
  odoo-manager [-V | --version] [-h | --help]
  odoo-manager <command> [options]

Options:
  -h, --help                Show this screen
  -V, --version             Show the installed version of odoo-manager

Commands:
  build
  convert
  format
  hello
  log
  new
  ps
  run
  setup
  stop

"""

import sys
import traceback
from inspect import getmembers, isclass
import odoo_manager
from odoo_manager.cli.exceptions import CommandException
from odoo_manager.core.shell import out

try:
    from docopt import docopt, DocoptExit
except ModuleNotFoundError:
    out("Failed to import 'docopt-ng'; see odoo-manager's requirements.txt", color="red")
    raise


def main():
    """
    Parse the CLI command & arguments, then execute the specified functionality.

    :return {NoneType}:
    """
    # Parse the CLI command & arguments (using `docopt-ng`)
    argv = sys.argv[1:] or ["--help"]
    command = getattr(odoo_manager.cli.commands, argv[0], None) if argv else None
    docstring = getattr(command, "__doc__", __doc__) or __doc__
    try:
        options = docopt(docstring, version=odoo_manager.version, more_magic=True, argv=argv)
    except DocoptExit as error:
        out(
            "Failed to parse arguments/options. You may be missing a required option or the command may be undocumented or unsupported.",
            color="red",
        )
        details = error.args[0].split("\n")
        out("  - (docopt response): {}\n".format(details[0]), color="yellow")
        out("Re-run with the --help flag for more usage details\n{}".format(" ".join(details[1:])), color="")
        sys.exit(1)
    except TypeError as error:
        message = error.args[0].split("\n")[0]
        if message == "docopt() got an unexpected keyword argument 'more_magic'":
            out("Make sure to 'pip uninstall docopt' so that 'docopt-ng' can be used", color="red")
            sys.exit(1)
        raise

    for option_name, option_passed in options.items():
        # Ignore any options which are not passed in from CLI execution
        if not option_passed:
            continue

        # Find & run the matching command,along with the given options/arguments
        if hasattr(odoo_manager.cli.commands, option_name):
            module = getattr(odoo_manager.cli.commands, option_name)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != "BaseCommand"][0]
            command = command(options)

            try:
                command.run()
                sys.exit(0)
            except CommandException as e:
                out("{}\n".format(str(e)), color="red")
                sys.exit(1)

            except Exception as e:
                if options.get("--verbose", False):
                    out(traceback.format_exc(), color="red")
                    sys.exit(1)
                else:
                    out("{}\n".format(e), color="red")
                    sys.exit(1)
        else:
            out(f"Failed to run: odoo-manager {' '.join(argv)}", color="red")
            sys.exit(1)
