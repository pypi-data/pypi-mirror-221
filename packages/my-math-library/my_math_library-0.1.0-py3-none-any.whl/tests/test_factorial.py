import unittest

from my_math.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_positive(self):
        result = factorial(5)
        self.assertEqual(result, 120)

if __name__ == "__main__":
    unittest.main()
