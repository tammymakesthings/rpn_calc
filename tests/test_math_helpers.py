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

from rpn_calc.math_helpers import MathHelpers as mh

import pytest


class TestMathHelpers:
    @pytest.mark.parametrize(
        ["input_population", "input_sets", "expected_value"],
        [
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0],
            [9.0, 3.0, 84.0],
            [49.0, 6.0, 13983816.0],
        ],
    )
    def test_ncr_with_valid_inputs(
        self,
        input_population: float,
        input_sets: float,
        expected_value: float,
    ):
        assert mh.ncr(input_population, input_sets) == expected_value

    @pytest.mark.parametrize(
        ["input_population", "input_sets", "expected_value"],
        [
            [0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0],
            [9.0, 3.0, 504.0],
            [49.0, 6.0, 10068347520.0],
        ],
    )
    def test_npr_with_valid_inputs(
        self,
        input_population: float,
        input_sets: float,
        expected_value: float,
    ):
        assert mh.npr(input_population, input_sets) == expected_value

    def test_ncr_throws_exception_on_string_input(self):
        with pytest.raises(ValueError):
            _ = mh.ncr("Fish", "Paste")

    def test_npr_throws_exception_on_string_input(self):
        with pytest.raises(ValueError):
            _ = mh.npr("Fish", "Paste")

    def test_ncr_throws_exception_on_reversed_operands(self):
        with pytest.raises(ValueError):
            _ = mh.ncr(6, 49)

    def test_npr_throws_exception_on_reversed_operands(self):
        with pytest.raises(ValueError):
            _ = mh.npr(6, 49)

    @pytest.mark.parametrize(
        ["input_population", "input_sets"],
        [
            [-100, 12],
            [100, -12],
        ],
    )
    def test_ncr_throws_exception_on_negative_operands(
        self, input_population, input_sets
    ):
        with pytest.raises(ValueError):
            _ = mh.ncr(6, 49)

    @pytest.mark.parametrize(
        ["input_population", "input_sets"],
        [
            [-100, 12],
            [100, -12],
        ],
    )
    def test_npr_throws_exception_on_negative_operands(
        self, input_population, input_sets
    ):
        with pytest.raises(ValueError):
            _ = mh.npr(input_population, input_sets)
