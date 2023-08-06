# Copyright (C) 2020 Deutsches Zentrum fuer Luft- und Raumfahrt(DLR, German Aerospace Center) <www.dlr.de>
# SPDX-FileCopyrightText: 2022 German Aerospace Center (DLR)
#
# SPDX-License-Identifier: MIT

"""Top-level package for gcodeReader."""

try:
    # For Python 3.8+
    import importlib.metadata as md
except ImportError:
    # For Python 3.7
    import importlib_metadata as md

from pathlib import Path

import tomlkit

name = Path(__file__).parent.name


def getPyprojectMeta(initPath):
    """Returns project data from pyproject.toml

    :param initPath: path to the packages main __init__.py file
    :return: dict with entries from tool.poetry in pyproject.toml
    """
    with open(Path(Path(initPath).parents[2], "pyproject.toml")) as pyproject:
        file_contents = pyproject.read()

    return tomlkit.parse(file_contents)["tool"]["poetry"]


try:
    # package is installed
    version = md.version(name)
    programDir = str(Path(__file__).parent)
except md.PackageNotFoundError:
    # package is not installed, read pyproject.toml
    try:
        # We have the full GitLab repository
        pkgMeta = getPyprojectMeta(__file__)
        version = str(pkgMeta["version"])
        programDir = str(Path(__file__).parents[3])
    except FileNotFoundError:
        # We have only the source code
        version = str("version not provided")
        programDir = str(Path(__file__).parent)


__author__ = """Jan-Timo Hesse"""
__email__ = "Jan-Timo.Hesse@dlr.de"
__version__ = version
