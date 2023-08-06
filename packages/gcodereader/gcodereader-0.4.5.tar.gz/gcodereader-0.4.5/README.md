<!--
SPDX-FileCopyrightText: 2022 German Aerospace Center (DLR)

SPDX-License-Identifier: MIT
-->
# gcodeReader


[![pipeline status](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/badges/main/pipeline.svg)](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/-/commits/main)
[![coverage report](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/badges/main/coverage.svg)](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/-/commits/main)
[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/-/blob/main/LICENSE)


Read gcode and translate into peridigm input

## Todos to setup project
- in gitlab activate CI/CD (settings→general→visibility→CI/CD)
- create token for pypi (todo: more text)
- adapt coverage percentage

## Features


* Free software: BSD license


* [Documentation](https://fa_sw.pages.gitlab.dlr.de/peridynamik/gcodereader)

- TODO: describe features


## Installation

### Installation from source
Get gcodereader source from

> https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader.git

and add the /src folder to pythonpath in the environment variables

### Installation as python package
Install it from [the gitlab packacke registry](https://gitlab.dlr.de/fa_sw/peridynamik/gcodereader/-/packages)

You can download the latest artifact (*.whl) and install it using


> cd gcodereader
> python setup.py install gcodereader<version>.whl


### Test the installation
In python execute:

> import gcodereader

### Developers

Developers may also install the pre-commit hook.

**Precommit**
1. install the pre-commit
   > pip install pre-commit
   or
   > conda isntall pre-commit
2. In the gcodereader folder
   > pre-commit install

This enables the pre-commit hooks defined in _.pre-commit-config.yaml_
and eases your commits and successful pipline runs.

## Usage

## Contributing to _gcodereader_

We welcome your contribution!

If you want to provide a code change, please:

* Create a fork of the GitLab project.
* Develop the feature/patch
* Provide a merge request.

> If it is the first time that you contribute, please add yourself to the list
> of contributors below.


## Citing

No citing required

## License



* Free software: BSD license
* Documentation: https://gcodereader.readthedocs.io.





## Change Log

see [changelog](changelog.md)

## CI Pipeline and Jobs for Developers

If you encounter any failed job on the pipeline you can run them locally for more information.
(prerequisite: have _make_ and _poetry_ installed [e.g. conda install make poetry])

See all availabe make targets used for the ci-jobs

> make list

Find the target with matching names and execute them locally e.g.:
> make test

If **check-formatting** fails, run the following to fix issues.
> make formatting

If **check-license-metadata** fails, run
> make check-license-metadata

identify the corresponding filename and run the following (include the filename in $filename)
> poetry run reuse addheader --copyright="German Aerospace Center (DLR)" --license="MIT" $filename

## Authors

[Jan-Timo Hesse](mailto:Jan-Timo.Hesse@dlr.de)
