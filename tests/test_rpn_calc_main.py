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

import pytest


class TestRPNCalcMain:
    pass
