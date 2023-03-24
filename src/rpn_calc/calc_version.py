# SPDX-FileCopyrightText: 2019-2023, Tammy Cravit
#
# SPDX-License-Identifier: MIT

"""
.. module:: rpn_calc
    :synopsis: Simple RPN calculator with a sly-based parser.

    .. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""

import tomli
import os.path

_RPN_CALC_MAJOR: int = 0
_RPN_CALC_MINOR: int = 0
_RPN_CALC_REVISION: int = 0

try:
    with open(
        os.path.join(os.path.dirname(__file__), "..", "..", "pyproject.toml"),
        "rb",
    ) as f:
        __config_dict = tomli.load(f)
    __version_parts = [
        int(x) for x in (__config_dict["tool"]["poetry"]["version"].split("."))
    ]
    _RPN_CALC_MAJOR, _RPN_CALC_MINOR, _RPN_CALC_REVISION = __version_parts[0:3]
except tomli.TOMLDecodeError:
    _RPN_CALC_MAJOR, _RPN_CALC_MINOR, _RPN_CALC_REVISION = [0, 0, 0]

RPN_CALC_VERSION = f"{_RPN_CALC_MAJOR}.{_RPN_CALC_MINOR}.{_RPN_CALC_REVISION}"
