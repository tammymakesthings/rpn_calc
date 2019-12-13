from math import factorial

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
