import filecmp
import getpass
import os
import re
import sys
from urllib.parse import quote
from odoo_manager.core import shell
from . import configs, paths as path_helpers

pipe_dev_null = path_helpers.pipe_dev_null


def redirect(verbose=False):
    """
    :param verbose {bool}:
    :return {str}:
    """
    return "" if verbose else (" " + pipe_dev_null)


class console_colors(object):
    """
    Helper to hold some constant for shell colors.
    """

    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    ENDC = "\033[0m"


def print_diff_files(ctx, dcmp):
    """
    :param ctx {invoke.context.Context}: Invoke context variable
    :param dcmp:
    :return {NoneType}:
    """
    for name in dcmp.diff_files:
        print(
            console_colors.WARNING
            + "diff_file {} found in {} and {}".format(name, dcmp.left, dcmp.right)
            + console_colors.ENDC
        )
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(ctx, sub_dcmp)


def _git_clone(ctx, url, branch, output, depth=1):
    """
    Does a system call on git clone, returns the exit status from that system.

    :param url {str}:
    :param branch {str}:
    :return {int}: Returns int representing success or failure
    """
    return ctx.run(
        "git clone '{url}' '{output}' --branch={branch} --depth={depth} --quiet{pipe}".format(
            url=url, branch=branch, output=output, depth=depth, pipe=redirect()
        )
    )


def _get_git_config(user="", password=""):
    """
    Get the username and password to be used for Git clone. By priority, this
    will use:

    :param user {str}: (optional) The username to be used for Git clone.
    :param password {str}: (optional) The password to be used for Git clone.
    :return {dict}:
        The Git configuration data to be used for cloning.
        Example:
            {
                "username": "my_github_user",
                "password": "mysecretpassword",
            }
    """
    git_config = {}
    if user and password:
        # Use the given user and password
        git_config["username"] = user
        git_config["password"] = password
    elif configs.config.has_option("options", "USERNAME") and configs.config.has_option("options", "PASSWORD"):
        # Use the configuration's user and password
        git_config["username"] = configs.config.get("options", "USERNAME")
        git_config["password"] = configs.config.get("options", "PASSWORD")
    else:
        # Request user input
        git_config["username"] = quote(input("Git username? "))
        git_config["password"] = quote(getpass.getpass("Git password? "))
    return git_config


def _get_git_urls(repo_url, fallback_url=""):
    """
    Generate HTTP and SSH URLs for the given URL.  If a fallback URL is given,
    then use that URL for the HTTP URL.

    Example #1:
      Input:
          repo_url = "git@github.com-blue:gobluestingray/blue_odoo_addons.git"
          fallback_url = "git@github.com:gobluestingray/blue_odoo_addons.git"

      Output:
          {
              "http": "https://github.com/gobluestingray/blue_odoo_addons.git",
              "ssh": "git@github.com-blue:gobluestingray/blue_odoo_addons.git",
          }

    Example #2:
      Input:
          repo_url = "https://github.com/OCA/account-payment"
          fallback_url = ""

      Output:
        {
            "http": "https://github.com/OCA/account-payment",
            "ssh": "git@github.com:OCA/account-payment",
        }

    :param repo_url {str}: The repository URL
    :param fallback_url {str}: (Optional) The fallback repository URL
    :return {dict}: A mapping of the URLs for HTTP and SSH
    """
    http_url = repo_url.replace("git@", "https://").replace(".com:", ".com/").replace(".org:", ".org/")
    ssh_url = (
        repo_url.replace("https://", "git@")
        .replace("http://", "git@")
        .replace(".com/", ".com:")
        .replace(".org/", ".org:")
    )

    # Use the fallback URL for the http URL
    # This deals with failures with the Github deploy key
    if fallback_url:
        http_url = fallback_url.replace("git@", "https://").replace(".com:", ".com/").replace(".org:", ".org/")

    return {"ssh": ssh_url, "http": http_url}


def _get_git_url_obscured(git_clone_url):
    """
    Remove the password from a Git clone URL.
    Example:
        Input:  git clone https://my_github_user:mysecretpassword@github.com/odoo/enterprise
        Output: git clone https://my_github_user:******@github.com/odoo/enterprise
    :param git_clone_url {str}: The Git URL which needs password to be obscured.
    :return {str}: The given URL with Git Password obscured, if found.
    """
    # Find the Git password, which would be between ":" and "@" characters.
    # https://stackoverflow.com/a/36247211/3330552
    password = re.search(r"https:\/\/[^:]*:([^@]*)@.*?$", git_clone_url).group(1)

    # If found, replace the password with asterisks
    return git_clone_url.replace(password, "******")


def git_clone(ctx, url, branch, repo_name, output, depth=1, user="", password="", original_url=""):
    """
    Clone the provided git repository.

    :param ctx {invoke.context.Context}: Invoke context variable
    :param url {str}: The repository URL
    :param branch {str}: The wanted branch of the repository
    :param repo_name {str}: The name of the repository
    :param output {str}:
        What to name the repository directory on the local file system
    :param depth {int}:
        (Optional) How deep of a clone that git makes; default is 1 level
    :param user {str}: (Optional) The Github username
    :param password {str}: (Optional) The user's Github password
    :param original_url {str}:
        (Optional) If the URL has been changed in some way (such as using some
        sort of SSH "alias" for Github deploy keys,) this URL is the original
        repository URL
    :return {NoneType}:
    """
    urls = _get_git_urls(url, fallback_url=original_url)

    try:
        shell.out("        *Trying to clone {}...".format(urls["ssh"]), color="yellow")
        _git_clone(ctx, urls["ssh"], branch, output, depth=depth)
    except:
        try:
            shell.out("        *Trying to clone {}...".format(urls["http"]), color="yellow")
            _git_clone(ctx, urls["http"], branch, output, depth=depth)
        except:
            try:
                credentials = _get_git_config(user, password)
                credentials_url = "https://{username}:{password}@{url}".format(
                    username=credentials.get("username"), password=credentials.get("password"), url=urls["http"][8:]
                )

                shell.out(
                    "        *Trying to clone {}...".format(_get_git_url_obscured(credentials_url)), color="yellow"
                )

                _git_clone(ctx, credentials_url, branch, output, depth=depth)
            except:
                shell.out("        Sorry, could not clone the repo {}".format(repo_name), color="red")


def diff_dependency_git(ctx, name, module_config, log=True):
    """
    :param name:
    :param module_config:
    :return: dict Paths for the modules
    """
    paths = path_helpers.Paths()

    if log:
        shell.out("  Processing {}...".format(name), color="yellow")

    # Add the Github deploy key "alias" to the git URL if needed
    deploy_key = module_config.get("deploy-key", False)
    environ = configs.config.get("options", "ENVIRONMENT")
    repo_url = module_config["url"]
    url_domain = repo_url.split(":")[0]

    if deploy_key and url_domain == "git@github.com" and environ != "local":
        url_domain = "{domain}-{key}".format(domain=url_domain, key=deploy_key)
        repo_url = "{domain}:{url}".format(domain=url_domain, url=":".join(repo_url.split(":")[1:]))

    repo_name = repo_url.replace(".git", "").split("/").pop()
    repo_temp_path = paths.base("_make_tmp/{}".format(repo_name))
    original_path = paths.base("_lib/{}".format(name))

    # If there is no repo cloned down into the temp folder yet, then we are
    # going to `git clone` it down so that we can access modules that we need to
    # move into `_lib`
    if not os.path.isdir(repo_temp_path):
        shell.out("    *Starting git clone for {}...".format(repo_url), color="yellow")

        repo_branch = module_config["branch"]

        git_clone(
            ctx,
            repo_url,
            repo_branch,
            repo_name,
            output=paths.base("_make_tmp/{}".format(repo_name)),
            original_url=module_config["url"],
        )

    # Once we've got the modules and files setup, then we are going to check and
    # see if we want to run a diff on these these or not
    if os.path.isdir(paths.base("{temp_path}/{module_name}".format(temp_path=repo_temp_path, module_name=name))):
        temp_module_path = paths.base("{temp_path}/{module_name}".format(temp_path=repo_temp_path, module_name=name))

        if log and os.path.isdir(original_path):
            print_diff_files(ctx, filecmp.dircmp(original_path, temp_module_path))
    else:
        shell.out(
            " ** Unable to find {module_name} in {repo}.".format(repo=repo_url, module_name=name),
            color="red",
        )

        exit(1)

    return {"original": original_path, "updated": temp_module_path}


def diff_dependency(ctx, name, module_config, log=True):
    """
    :param ctx {invoke.context.Context}: Invoke context variable
    :param name {str}:
    :param module_config:
    :return {NoneType}:
    """
    if "type" in module_config:
        dependency_fn = getattr(sys.modules[__name__], "diff_dependency_{type}".format(type=module_config["type"]))

        if dependency_fn:
            return dependency_fn(ctx, name, module_config, log)
    else:
        return diff_dependency_git(ctx, name, module_config, log)


def update_dependency(ctx, name, module_config):
    """
    :param ctx {invoke.context.Context}: Invoke context variable
    :param name {str}:
    :param module_config:
    :return {NoneType}:
    """
    diff_paths = diff_dependency(ctx, name, module_config, log=False)

    shell.out("  Updating lib with {}...".format(os.path.basename(diff_paths["original"])), color="yellow")
    os.system("rm -rf {}".format(diff_paths["original"]))
    os.system("cp -R {} {}".format(diff_paths["updated"], diff_paths["original"]))
