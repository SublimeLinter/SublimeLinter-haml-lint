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
    cmd = 'ruby -S haml-lint'
    regex = r'^.+?:(?P<line>\d+) \[(:?(?P<warning>W)|(?P<error>E))\] (?P<message>.+)'
    tempfile_suffix = 'haml'

    defaults = {
        '--config': '${folder}/.haml-lint.yml',
        'env': {
            'HAML_LINT_RUBOCOP_CONF': '${folder}/.rubocop.yml'
        }
    }
