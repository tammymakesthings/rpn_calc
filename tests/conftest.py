import sys
import os
from pathlib import Path


import pytest
from fixtures import TestData


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')


import rpn_calc


from rpn_calc.math_helpers import MathHelpers
from rpn_calc.calc_version import RPN_CALC_VERSION
from rpn_calc.calc_lexer import CalcLexer
from rpn_calc.calc_main import CalcMain
from rpn_calc.calc_repl import CalcRepl


TestData.BASE_PATH = Path(__file__).parent / 'data'


@pytest.fixture()
def default_instance():
    return CalcMain(debug=True, verbose=True)


