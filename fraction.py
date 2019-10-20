from math import gcd, copysign


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        common_div = gcd(numerator, denominator)
        if common_div == 0:
            common_div = 1
        self.numerator = int((numerator / common_div) / copysign(1, denominator))
        self.denominator = int((denominator / common_div) / copysign(1, denominator))
        if self.denominator != 0:
            self.equal = self.numerator / self.denominator
        elif self.denominator == 0:
            self.equal = "UNDEFINED."

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        add_new_numerator = (self.numerator * frac.denominator) +\
                            (frac.numerator * self.denominator)
        add_new_denominator = self.denominator * frac.denominator
        if add_new_denominator == 0:
            raise ValueError("UNDEFINED.")
        return Fraction(add_new_numerator, add_new_denominator)

    def __mul__(self, frac):
        mul_new_numerator = self.numerator * frac.numerator
        mul_new_denominator = self.denominator * frac.denominator
        if mul_new_denominator == 0:
            raise ValueError("UNDEFINED.")
        return Fraction(mul_new_numerator, mul_new_denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.equal == frac.equal

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator:.0f}'
        elif self.denominator == 0:
            raise ValueError("UNDEFINED.")
        elif self.numerator == 0:
            return '0'
        return f'{self.numerator:.0f}/{self.denominator:.0f}'
