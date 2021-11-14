import sys
import os
import pytest


import rpn_calc
from rpn_calc.math_helpers import MathHelpers


class TestMathHelpers:

    def test_ncr_npr_functions_exist():
        assert("ncr" in dir(MathHelpers))
        assert("npr" in dir(MathHelpers))

    def test_ncr_npr_functions_perform_math_correctly():
        assert(28 == MathHelpers.ncr(8, 2))
        assert(56 == MathHelpers.npr(8, 2))

    def test_ncr_npr_functions_handle_big_numbers_correctly():
        assert(86493225 == MathHelpers.ncr(30, 12))
        assert(41430393164160000 == MathHelpers.npr(30, 12))

    def test_ncr_npr_functions_handle_zero_args():
        assert(1 == MathHelpers.ncr(8, 0))
        assert(1 == MathHelpers.npr(8, 0))

    def test_ncr_npr_functions_handle_one_args():
        assert(8 == MathHelpers.ncr(8, 1))
        assert(8 == MathHelpers.npr(8, 1))

    def test_ncr_npr_functions_handle_reversed_args():
        assert(28 == MathHelpers.ncr(2, 8))
        assert(56 == MathHelpers.npr(2, 8))

    def test_ncr_npr_functions_raise_exception_floating_args():
        with pytest.raises(ValueError):
            MatHelpers.ncr(8.5, 2)
        with pytest.raises(ValueError):
            MatHelpers.ncr(8, 2.5)
        with pytest.raises(ValueError):
            MatHelpers.npr(8.5, 2)
        with pytest.raises(ValueError):
            MatHelpers.npr(8, 2.5)
            
    def test_ncr_npr_functions_raise_exception_nonintable_args():
        with pytest.raises(ValueError):
            MathHelpers.ncr(8, "Squid")
        with pytest.raises(ValueError):
            MathHelpers.ncr("Squid", 2)
        with pytest.raises(ValueError):
            MathHelpers.npr(8, "Squid")
        with pytest.raises(ValueError):
            MathHelpers.npr("Squid", 2)
