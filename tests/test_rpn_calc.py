import sys
import os
import pytest

import rpn_calc
from rpn_calc.calc_version import RPN_CALC_VERSION


def test_rpn_calc_module():
    assert(RPN_CALC_VERSION is not None)
    assert(3 == len(RPN_CALC_VERSION.split('.')))
    for i in RPN_CALC_VERSION.split('.'):
        assert((int(i) >= 0) and (int(i) <= 99999))
