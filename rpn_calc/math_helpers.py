from math import factorial

"""
.. class:: MathHelpers
   :synopsis: Math helper functions used by the calculator.

.. moduleauthor:: Tammy Cravit <tammymakesthings@gmail.com
"""
class MathHelpers:

    @staticmethod
    def ncr(nval, rval):
        n = int(nval)
        r = int(rval)
        npr = factorial(n) // factorial(n-r)
        ncr = npr // factorial(r)
        return ncr

    @staticmethod
    def npr(nval, rval):
        n = int(nval)
        r = int(rval)
        npr = factorial(n) // factorial(n-r)
        return npr
