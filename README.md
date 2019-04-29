SublimeLinter-haml-lint
=======================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-haml-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-haml-lint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)  provides an interface to [haml-lint](https://github.com/brigade/haml-lint).
It will be used with files that have the "Ruby Haml" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please install via [Package Control](https://packagecontrol.io).

Before using this plugin, ensure that `haml-lint` is installed on your system.
To install `haml-lint`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `haml-lint` by typing the following in a terminal:
   ```
   [sudo] gem install haml_lint
   ```
   **Note:** Make sure you type `haml_lint` with an underscore (`_`). `gem install haml-lint` will get you an outdated executable.

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://www.sublimelinter.com/en/latest/troubleshooting.html) for more information.

Please make sure that the path to `haml-lint` is available to SublimeLinter. 
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


### Linter configuration
The default configuration is as follows:

```
'selector': 'text.haml'
```

If you have your configuration files somewhere else or with a different name, set this using the Linter settings.


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
