from math import factorial

class MathHelpers:
    """Mathematic helper functions used by the calculator. This class is not
    instantiated, so any methods added here should be tagged with the
    `@staticmethod` decorator."""


    @staticmethod
    def ncr(nval, rval):
        """Calculate the number of combinations (nCr) given the size of the
        population and the size of each grouping.

        Args:
            n (int): The size of the total population
            r (int): The size of each grouping

        Returns:
            int: The number of possible unique combinations."""
        n = int(nval)
        r = int(rval)
        npr = factorial(n) // factorial(n-r)
        ncr = npr // factorial(r)
        return ncr


    @staticmethod
    def npr(nval, rval):
        """Calculate the number of permutations (nPr) given the size of the
        population and the size of each grouping.

        Args:
            n (int): The size of the total population
            r (int): The size of each grouping

        Returns:
            int: The number of possible permutations."""
        n = int(nval)
        r = int(rval)
        npr = factorial(n) // factorial(n-r)
        return npr
