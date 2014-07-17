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

from SublimeLinter.lint import RubyLinter


class HamlLint(RubyLinter):

    """Provides an interface to haml-lint."""

    syntax = 'ruby haml'
    cmd = 'haml-lint'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.6.0'
    regex = r'^.+?:(?P<line>\d+) \[(:?(?P<warning>W)|(?P<error>E))\] (?P<message>.+)'
    tempfile_suffix = 'haml'
    config_file = ('--config', '.haml-lint.yml')
