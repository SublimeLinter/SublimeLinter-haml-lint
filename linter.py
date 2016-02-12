#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jeroen Jacobs
# Copyright (c) 2014 Jeroen Jacobs
#
# License: MIT
#

"""This module exports the HamlLint plugin class."""

import os
from SublimeLinter.lint import RubyLinter, util


class HamlLint(RubyLinter):
    """Provides an interface to haml-lint."""

    syntax = 'ruby haml'
    cmd = 'ruby -S haml-lint'
    version_args = '-S haml-lint --version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.6.0'
    regex = r'^.+?:(?P<line>\d+) \[(:?(?P<warning>W)|(?P<error>E))\] (?P<message>.+)'
    tempfile_suffix = 'haml'
    config_file = ('--config', '.haml-lint.yml')

    def build_args(self, settings):
        """
        Return a list of args to add to cls.cmd.

        We hook into this method to find the rubocop config and set it as an
        environment variable for the rubocop linter to pick up.
        """
        rubocop_file = settings.get('rubocop-config', '.rubocop.yml')
        if self.filename:
            rubocop_config = util.find_file(
                os.path.dirname(self.filename),
                rubocop_file,
                aux_dirs='~'
            )
            print(rubocop_config)
            if rubocop_config:
                self.env['HAML_LINT_RUBOCOP_CONF'] = rubocop_config
            else:
                self.env.pop('HAML_LINT_RUBOCOP_CONF', None)

        return super().build_args(settings)
