"""
Usage:
  odoo-manager new (module | project) [-n | --name=<name>] [-v | --verbose] [-h | --help]

Options:
  -h, --help                Show this screen
  -n, --name=<name>         Pass a name for the project or module.
  -v, --verbose             Enable verbose details.

Create a new module or project from the related scaffold project.
Specify the type of data being created and its name.

"""

import getpass
import os
import re
from urllib.parse import quote
from odoo_manager.core import git, shell
from .base import BaseCommand


class New(BaseCommand):
    def __init__(self, options, *args, **kwargs):
        """
        Construct a New command object for `odoo-manager new`.

        :return {NoneType}:
        """
        super(New, self).__init__(options, depends_on_project=False, *args, **kwargs)
        self.supported_commands = ("project", "module")

    def run_project(self):
        """
        Handles `odoo-manager new project`.

        :return {NoneType}:
        """
        shell.out("Making a new project...")

        verbose = self.options.get("--verbose", False)
        name = self.options.get("--name", [False])[0]
        shell.out(name)
        branch = "master"

        if not name:
            shell.out('Missing project name. Try "odoo-manager new project --name=my_project"')
            return

        try:
            shell.run(
                'git clone git@github.com:gobluestingray/odoo_project_scaffold.git {} --branch="{}" "{}"'.format(
                    "--quiet" if not verbose else "", branch, name
                )
            )
        except:  # pylint: disable=bare-except
            shell.out("Invalid credentials.", color="red")

        shell.run('rm -rf "./{}/.git"'.format(name))
        shell.out("Successfully created the project:")
        shell.out("  name:         {}".format(name), color="light_grey")

    def run_module(self):
        """
        Handles `odoo-manager new module`.
        """
        verbose = self.options.get("--verbose", False)
        name = self.options.get("--name", [False]) or [False]
        name = name[0]

        if name:
            shell.out(f" > The technical name of the module will be '{name}'", color="light_blue")
        else:
            name = input(shell.out(" > What is the technical name of the module? ", color="light_blue", run=False))

        branch = input(
            shell.out(" > What is the version of the module (9.0, 10.0, 11.0, etc.)? ", color="light_blue", run=False)
        )
        module_display_name = input(
            shell.out(" > What is the display name of the module? ", color="light_blue", run=False)
        )
        module_category = input(shell.out(" > What is the category of the module? ", color="light_blue", run=False))
        module_tagline = input(
            shell.out(" > What is a tagline for the module (1 sentence description)? ", color="light_blue", run=False)
        )
        module_summary = input(
            shell.out(" > What is a summary/short explanation of the module? ", color="light_blue", run=False)
        )

        shell.out("\n")
        shell.out("Generating the module...")

        try:
            shell.run(
                'git clone git@github.com:gobluestingray/odoo_module_scaffold.git {} --branch="{}" "{}"'.format(
                    "--quiet" if not verbose else "", branch, name
                )
            )
        except:  # pylint: disable=bare-except
            shell.out("Invalid credentials.", color="red")

        shell.run('rm -rf "./{}/.git"'.format(name))

        # Wire the defaults to the module. There are a few things that every
        # module needs:
        #
        # 1. New readme.md file
        # 2. Updated __manifest__.py
        # 3. Updated static/description/index.html
        with open("./{}/readme.md".format(name), "w") as readme_file:
            readme_file.write("# {} ({})".format(module_display_name, name))

        with open("./{}/static/description/index.html".format(name), "w") as index_html_file:
            index_html_file.write(
                """
<section class="oe_container">
    <div class="oe_row oe_spaced">
        <div class="oe_span12">
            <h2 class="oe_slogan">{}</h2>
            <h3 class="oe_slogan">{}</h3>
        </div>
    </div>
</section>\n""".lstrip().format(
                    module_display_name, module_tagline
                )
            )

        manifest_content = False
        manifest_files = ("__manifest__.py", "__openerp__.py")

        for potential_manifest_file in manifest_files:
            if os.path.isfile("./{}/{}".format(name, potential_manifest_file)):
                with open("./{}/{}".format(name, potential_manifest_file), "r") as manifest_file:
                    manifest_content = manifest_file.read()
                    manifest_content = re.sub(
                        r'[\'"]+name[\'"]+:\s+[\'"]+(.*)[\'"]+,',
                        '"name": "{}",'.format(module_display_name),
                        manifest_content,
                    )
                    manifest_content = re.sub(
                        r'[\'"]+category[\'"]+:\s+[\'"]+(.*)[\'"]+,',
                        '"category": "{}",'.format(module_category),
                        manifest_content,
                    )
                    manifest_content = re.sub(
                        r'[\'"]+version[\'"]+:\s+[\'"]+(.*)[\'"]+,',
                        '"version": "{}",'.format(branch + ".0"),
                        manifest_content,
                    )
                    manifest_content = re.sub(
                        r'[\'"]+summary[\'"]+:\s+[\'"]+(.*)[\'"]+,',
                        '"summary": "{}",'.format(module_tagline),
                        manifest_content,
                    )
                    manifest_content = re.sub(
                        r'[\'"]+description[\'"]+:\s+[\'"]+(.*)[\'"]+,',
                        '"description": "{}",'.format(module_summary),
                        manifest_content,
                    )

                if manifest_content:
                    with open("./{}/{}".format(name, potential_manifest_file), "w") as manifest_file:
                        manifest_file.write(manifest_content)

        shell.out("Successfully created the module:")
        shell.out("  name:         {}".format(name), color="light_grey")
        shell.out("  branch:       {}".format(branch), color="light_grey")
        shell.out("  display name: {}".format(module_display_name), color="light_grey")
        shell.out("  category:     {}".format(module_category), color="light_grey")
        shell.out("  tagline:      {}".format(module_tagline), color="light_grey")
        shell.out("  summary:      {}".format(module_summary), color="light_grey")
