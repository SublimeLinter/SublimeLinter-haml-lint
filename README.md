SublimeLinter-haml-lint
=======================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-haml-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-haml-lint)

This linter plugin for [SublimeLinter](http://sublimelinter.com)  provides an interface to [haml-lint](https://github.com/brigade/haml-lint). It will be used with files that have the “Ruby Haml” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please install via [Package Control](https://sublime.wbond.net/installation).

Before using this plugin, you must ensure that `haml-lint` is installed on your system. To install `haml-lint`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `haml-lint` by typing the following in a terminal:
   ```
   [sudo] gem install haml_lint
   ```
   **Note:** Make sure you type `haml_lint` with an underscore (`_`). `gem install haml-lint` will get you an outdated executable.

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://www.sublimelinter.com/en/latest/troubleshooting.html) for more information.

### Linter configuration
In order for `haml-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `haml-lint`, you can proceed to install the SublimeLinter-contrib-haml-lint plugin if it is not yet installed.

The default configuration is as follows:

```
    defaults = {
        '--config': '${folder}/.haml-lint.yml',
        'env': {
            'HAML_LINT_RUBOCOP_CONF': '${folder}/.rubocop.yml'
        }
    }
```

If you have your configuration files somewhere else or with a different name, you must set this using the Linter settings.

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
