#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jeroen Jacobs & Tomas Barry
# Copyright (c) 2014 Jeroen Jacobs
#
# License: MIT
#

"""This module exports the HamlLint plugin class."""

from SublimeLinter.lint import RubyLinter


class HamlLint(RubyLinter):
    """Provides an interface to haml-lint."""

    cmd = 'ruby -S haml-lint ${args} ${temp_file}'
    regex = r'^.+?:(?P<line>\d+) \[(:?(?P<warning>W)|(?P<error>E))\] (?P<message>.+)'
    tempfile_suffix = 'haml'

    defaults = {
        'selector': 'text.haml'
    }
