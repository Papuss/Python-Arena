__author__ = 'Gazdik_Zsolt'

import unittest
from Prime_Factors import Prime_factor

class Prime_factor_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual([], Prime_factor.generate(1))

    def test_two(self):
        self.assertEqual([2], Prime_factor.generate(2))

    def test_three(self):
        self.assertEqual([3], Prime_factor.generate(3))

    def test_four(self):
        self.assertEqual([2, 2], Prime_factor.generate(4))

    def test_six(self):
        self.assertEqual([2, 3], Prime_factor.generate(6))

    def test_eight(self):
        self.assertEqual([2, 2, 2], Prime_factor.generate(8))

    def test_nine(self):
        self.assertEqual([3, 3], Prime_factor.generate(9))



if __name__ == '__main__':
    unittest.main()
