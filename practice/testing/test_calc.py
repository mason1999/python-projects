# run this normally
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15, msg = "BLAH BLAH BLAH")
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 5), -6)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(-1, 5), -5)
        self.assertEqual(calc.mul(-1, -1), 1)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 5), -0.2)
        self.assertEqual(calc.div(-1, -1), 1)
        self.assertRaises(ValueError, calc.div, 5, 0)
        # alternative way of testing exceptions: with context manager
        with self.assertRaises(ValueError):
            calc.div(5, 0)
if __name__ == '__main__':
    unittest.main()