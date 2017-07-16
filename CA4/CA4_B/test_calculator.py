import unittest

from calculator import Calculator


# test the calculator functionality
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # test addition for integer, float and complex
    def testAdd(self):
        self.assertEqual(6, self.calc.add(2, 4))
        self.assertEqual(4, self.calc.add(4, 0))
        self.assertEqual(4.5, self.calc.add(5.5, -1))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(round(5 / 6.0, 4),
                         round(self.calc.add(2 / 4.0, 2 / 6.0), 4))
        self.assertEqual(1 + 2j, self.calc.add(1, 2j))

    # test adding two lists
    def testAddList(self):
        self.assertEqual([6, 4], self.calc.add([2, 0], 4))
        self.assertEqual([6, 4], self.calc.add(4, [2, 0]))
        self.assertEqual([6, 4, 4.5, 0, 1 + 2j],
                         self.calc.add([2, 4, 5.5, -2, 1],
                                       [4, 0, -1, 2, 2j]))

    # test subtraction for integer, float and complex
    def testSubtract(self):
        self.assertEqual(10, self.calc.subtract(20, 10))
        self.assertEqual(-5, self.calc.subtract(5, 10))
        self.assertAlmostEqual(0.1, self.calc.subtract(10, 9.9))
        self.assertEqual(0, self.calc.subtract(4, 4))
        self.assertEqual(-5j, self.calc.subtract(0, 5j))

    # test subtracting two lists
    def testSubtractList(self):
        self.assertEqual([15, 5], self.calc.subtract([20, 10], 5))
        self.assertEqual([15, 5], self.calc.subtract(20, [5, 15]))
        self.assertEqual([10, -5, 0, -5j],
                         self.calc.subtract(
                             [20, 5, 4, 0],
                             [10, 10, 4, 5j]))

    # test multiplication for integer, float and complex
    def testMultiply(self):
        self.assertEqual(10, self.calc.multiply(2, 5))
        self.assertEqual(-5, self.calc.multiply(5, -1))
        self.assertEqual(6.46, self.calc.multiply(1.9, 3.4))
        self.assertEqual(27j, self.calc.multiply(9, 3j))
        self.assertEqual(0, self.calc.multiply(0, 4))

    # test multiplication for list
    def testMultiplyList(self):
        self.assertEqual([10, -5], self.calc.multiply([2, -1], 5))
        self.assertEqual([-5, 10], self.calc.multiply(5, [-1, 2]))
        self.assertEqual([3, 36], self.calc.multiply([1, 9], [3, 4]))

    # test division for integer, float and complex
    # test for divisor equal to zero to raise an error
    def testDivide(self):
        self.assertEqual(0, self.calc.divide(0, 2))
        self.assertEqual(10, self.calc.divide(50, 5))
        self.assertEqual(-0.1, self.calc.divide(1, -10))
        self.assertEqual(round(5.0 / 6, 4), round(self.calc.divide(5, 6), 4))
        self.assertEqual(2j, self.calc.divide(-4, 2j))
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # test divide for list
    def testDivideList(self):
        self.assertEqual([10, 2], self.calc.divide([50, 10], 5))
        self.assertEqual([1, 2], self.calc.divide(10, [10, 5]))
        self.assertEqual([-4, 1], self.calc.divide([-4, 2], [1, 2]))

    # test square root for integer, float and complex
    def testSquare_root(self):
        self.assertEqual(4, self.calc.square_root(16))
        self.assertEqual(10, self.calc.square_root(100))
        self.assertEqual(1.1, self.calc.square_root(1.21))
        self.assertEqual(1, self.calc.square_root(1))
        self.assertAlmostEqual(1j, self.calc.square_root(-1 + 0j))

    # test square root for list
    def testSquare_rootList(self):
        self.assertEqual([4, 10], self.calc.square_root([16, 100]))

    # test nth root for integer, float and complex
    # test n equals zero raises an error
    def testnth_root(self):
        self.assertEqual(2, self.calc.nth_root(16, 4))
        self.assertEqual(3, self.calc.nth_root(27, 3))
        self.assertEqual(10, self.calc.nth_root(100, 2))
        self.assertAlmostEqual(0.3, self.calc.nth_root(0.027, 3))
        self.assertAlmostEqual((1.732 + 1j), self.calc.nth_root(8j, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.nth_root(4, 0)

    # test nth root for list
    def testnth_rootList(self):
        self.assertEqual([2, 3], self.calc.nth_root([8, 27], 3))
        self.assertEqual([4, 2], self.calc.nth_root(16, [2, 4]))
        self.assertEqual([3, 2], self.calc.nth_root([9, 16], [2, 4]))

    # test power for integer, float and complex
    def testPower(self):
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(121, self.calc.power(-11, 2))
        self.assertAlmostEqual(29.791, self.calc.power(3.1, 3))
        self.assertEqual(1024, self.calc.power(16, 2.5))
        self.assertEqual(1, self.calc.power(1j, 0))
        self.assertEqual(-1, self.calc.power(1j, 2))

    # test power for list
    def testPowerList(self):
        self.assertEqual([9, 27], self.calc.power(3, [2, 3]))
        self.assertEqual([8, 27], self.calc.power([2, 3], 3))
        self.assertEqual([4, 27], self.calc.power([2, 3], [2, 3]))

    # test logarithm for integer and float
    # test raises an error if x is not a real number
    def testLogarithm(self):
        self.assertEqual(3, round(self.calc.logarithm(1000), 4))
        self.assertEqual(2, self.calc.logarithm(100))
        self.assertEqual(0, self.calc.logarithm(1))
        self.assertAlmostEqual(-1, self.calc.logarithm(0.1))
        with self.assertRaises(ValueError):
            self.calc.logarithm(2j)

    # test logarithm for list
    def testLogarithmList(self):
        self.assertEqual([2, 0], self.calc.logarithm([100, 1]))

    # test factorial for natural numbers
    # test raises an error if n is negative or a fraction
    def testFactorial(self):
        self.assertEqual(5040, self.calc.factorial(7))
        self.assertEqual(3628800, self.calc.factorial(10))
        self.assertEqual(1, self.calc.factorial(1))
        self.assertEqual(1, self.calc.factorial(0))
        with self.assertRaises(ValueError):
            self.calc.factorial(-3)
        with self.assertRaises(ValueError):
            self.calc.factorial(0.6)

    # test factorial for list
    def testFactorialList(self):
        self.assertEqual([5040, 3628800, 1, 1], self.calc.factorial([7, 10, 1, 0]))

    # test reciprocal for integer, float, complex and non zero
    # test raises an error if the parameter equals zero
    def testReciprocal(self):
        self.assertEqual(0.2, self.calc.reciprocal(5))
        self.assertEqual(-0.2, self.calc.reciprocal(-5))
        self.assertEqual(4, self.calc.reciprocal(0.25))
        self.assertEqual(10, self.calc.reciprocal(0.1))
        self.assertEqual(round(1 / 36.0, 4), round(self.calc.reciprocal(36), 4))
        self.assertEqual(-1j, self.calc.reciprocal(1j))
        with self.assertRaises(ValueError):
            self.calc.reciprocal(0)

    # test reciprocal for list
    def testReciprocalList(self):
        self.assertEqual([-0.2, 10, 0.2], self.calc.reciprocal([-5, 0.1, 5]))


if __name__ == '__main__':
    unittest.main()
