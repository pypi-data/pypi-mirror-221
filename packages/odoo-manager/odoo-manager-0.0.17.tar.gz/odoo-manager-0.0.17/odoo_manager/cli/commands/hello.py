"""
Usage: odoo-manager hello [-h | --help]

Options:
  -h, --help                Show this screen

"""

from odoo_manager.core.shell import out
from .base import BaseCommand


class Hello(BaseCommand):
    def __init__(self, options, *args, **kwargs):
        super(Hello, self).__init__(options, depends_on_project=False, *args, **kwargs)

    def run(self):
        out("Hello!")
