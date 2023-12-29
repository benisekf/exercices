import unittest
from max_consecutive_zeros import max_consecutive_zeros

class TestMaxConsecutiveZeros(unittest.TestCase):
    def test_case_22(self):
        self.assertEqual(max_consecutive_zeros(22), 1)

    def test_case_25(self):
        self.assertEqual(max_consecutive_zeros(25), 2)

    def test_case_268(self):
        self.assertEqual(max_consecutive_zeros(268), 4)

if __name__ == '__main__':
    unittest.main()