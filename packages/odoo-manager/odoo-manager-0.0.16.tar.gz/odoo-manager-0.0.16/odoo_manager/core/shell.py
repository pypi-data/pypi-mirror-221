import os
import re
from invoke import Config, Context
from termcolor import colored

U_SUCCESS = u"\u2713"
U_FAILURE = u"\u2716"


def get_context():
    """
    Get an invoke context object, used to run shell commands.

    :return {invoke.context.Context}: Returns the context object.
    """
    return Context(Config())


def run(cmd, ctx=None, *args, **kwargs):
    if not ctx:
        ctx = get_context()
    return ctx.run(cmd, *args, **kwargs)


def out(msg, color="green", run=True, ctx=None, is_error=False, **kwargs):
    """
    Run an echo command through invoke that prints text in color.

    For a list of colors see the termcolor documentation:
    https://pypi.org/project/termcolor/

    :param msg {str}:
    :param color {str}:
    :param run {bool}:
    :param ctx {invoke.context.Context}: Invoke context variable
    :param is_error {bool}:
        If True, echo output to stderr.
    :return {NoneType}:
    """
    if not ctx:
        ctx = get_context()

    if os.environ.get("INVOKE_ASCII", False) == "1":
        msg = msg.replace(U_SUCCESS, "PASS")
        msg = msg.replace(U_FAILURE, "FAIL")
        msg = msg.encode("utf-8").decode("ascii", "ignore")

    if run and os.environ.get("INVOKE_NO_COLOR", False) == "1":
        msg = re.sub(r"\s*\$\(tput[a-z0-9 ]+\)\s*", "", msg)
        ctx.run('echo "{}"'.format(msg), **kwargs)
        return msg

    reset = "\033[0m"

    msg = colored("{}{}".format(msg, reset), color or None)
    if run:
        # Output to stderr - https://stackoverflow.com/a/23550347/3330552
        prefix = ">&2 " if is_error else ""

        ctx.run('{}echo "{}"'.format(prefix, msg), **kwargs)
    return msg
