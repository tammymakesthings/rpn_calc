# SPDX-FileCopyrightText: 2019-2023, Tammy Cravit
#
# SPDX-License-Identifier: MIT

"""
.. module:: rpn_calc
    :synopsis: Simple RPN calculator with a sly-based parser.

.. moduleauthor:: Tammy Cravit <tammy@tammymakesthings.com>
.. version: 0.0.2
"""

import sys, os

file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(file_path, "..", "src"))

from rpn_calc.calc_version import (
    _RPN_CALC_MAJOR,
    _RPN_CALC_MINOR,
    _RPN_CALC_REVISION,
    RPN_CALC_VERSION,
)

import pytest


class TestRPNCalcVersion:
    def test_version_number_components_exist(self):
        assert all(
            [
                isinstance(_RPN_CALC_MAJOR, int),
                isinstance(_RPN_CALC_MINOR, int),
                isinstance(_RPN_CALC_REVISION, int),
            ]
        )

    def test_version_number_components_are_valid(self):
        assert all(
            [
                (_RPN_CALC_MAJOR >= 0),
                (_RPN_CALC_MINOR >= 0),
                (_RPN_CALC_REVISION >= 0),
            ]
        )

    def test_version_string(self):
        expected_version_string = (
            f"{_RPN_CALC_MAJOR}.{_RPN_CALC_MINOR}.{_RPN_CALC_REVISION}"
        )
        assert RPN_CALC_VERSION == expected_version_string
