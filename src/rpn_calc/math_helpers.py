# SPDX-FileCopyrightText: 2019-2023, Tammy Cravit
#
# SPDX-License-Identifier: MIT

from math import factorial


class MathHelpers:
    """
    Mathematic helper functions used by the calculator. This class is not
    instantiated, so any methods added here should be tagged with the
    `@staticmethod` decorator.
    """

    @staticmethod
    def ncr(nval, rval):
        """
        Calculate the number of combinations (nCr) given the size of the
        population and the size of each grouping.

        Args:
            n (int): The size of the total population
            r (int): The size of each grouping

        Returns:
            int: The number of possible unique combinations.

        Raises:
            ValueError: Raised if the values of n or r are negative.
        """

        n = int(nval)
        r = int(rval)

        if n < 0:
            raise ValueError("the value of n cannot be negative", n)
        if r < 0:
            raise ValueError("the value of r cannot be negative", r)

        npr = factorial(n) // factorial(n - r)
        ncr = npr // factorial(r)
        return ncr

    @staticmethod
    def npr(nval, rval):
        """
        Calculate the number of permutations (nPr) given the size of the
        population and the size of each grouping.

        Args:
            n (int): The size of the total population
            r (int): The size of each grouping

        Returns:
            int: The number of possible permutations.

        Raises:
                ValueError: Raised if the values of n or r are negative.
        """

        n = int(nval)
        r = int(rval)

        if n < 0:
            raise ValueError("the value of n cannot be negative", n)
        if r < 0:
            raise ValueError("the value of r cannot be negative", r)

        npr = factorial(n) // factorial(n - r)
        return npr
