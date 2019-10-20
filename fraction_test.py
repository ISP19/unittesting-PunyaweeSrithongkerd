import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        # New test cases.
        with self.assertRaises(ValueError):
            f = Fraction(0, 0)
            print(f)
            f = Fraction(1, 0)
            print(f)
        f = Fraction(0, 1)
        self.assertEqual("0", f.__str__())
        f = Fraction(0)
        self.assertEqual("0", f.__str__())
        f = Fraction(0, -1)
        self.assertEqual("0", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12)+Fraction(2, 3))
        # New test cases
        # 1/2 = 1/4 + 2/8
        self.assertEqual(Fraction(1, 2), Fraction(1, 4) + Fraction(2, 8))
        # 3/4 = 9/12 + 0
        self.assertEqual(Fraction(3, 4), Fraction(9, 12) + Fraction(0))
        # 1 = 1/2 + 2/4
        self.assertEqual(Fraction(1), Fraction(1, 2) + Fraction(2, 4))
        with self.assertRaises(ValueError):
            Fraction(1, 0)+Fraction(2, 3)
            Fraction(1, 12)+Fraction(2, 0)
            Fraction(0, 0)+Fraction(2, 0)

    def test_mul(self):
        # 1/4 = 1/2 * 1/2
        self.assertEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        i = Fraction(3, 0)
        j = Fraction(0, 1)
        k = Fraction(0)
        self.assertTrue(j.__eq__(k))
        self.assertFalse(i.__eq__(j))


if __name__ == '__main__':
     unittest.main(verbosity=2)