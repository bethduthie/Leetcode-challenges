import unittest
import testing


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(testing.add(5, 10), 15)
        self.assertEqual(testing.add(-1, 1), 0)
        self.assertEqual(testing.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(testing.subtract(5, 10), -5)
        self.assertEqual(testing.subtract(10, 5), 5)
        self.assertEqual(testing.subtract(2, -2), 4)
        self.assertEqual(testing.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(testing.multiply(5, 10), 50)
        self.assertEqual(testing.multiply(-2, 3), -6)
        self.assertEqual(testing.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(testing.divide(5, 10), 0.5)
        self.assertEqual(testing.divide(10, 5), 2)
        self.assertEqual(testing.divide(-5, 1), -5)
        self.assertEqual(testing.divide(-5, -5), 1)

        # self.assertRaises(ValueError, testing.divide, 10, 0)
        with self.assertRaises(ValueError):
            testing.divide(10, 0)
