import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

import rpn_calc

from rpn_calc.math_helpers import MathHelpers
from rpn_calc.calc_version import RPN_CALC_VERSION

