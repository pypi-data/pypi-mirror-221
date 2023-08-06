import unittest

from my_math.square import square


class TestSquare(unittest.TestCase):
    def test_positive_number(self):
        result = square(5)
        self.assertEqual(result, 25)

    def test_negative_number(self):
        result = square(-3)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
