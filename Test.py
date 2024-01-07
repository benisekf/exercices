import unittest
from max_consecutive_zeros import max_consecutive_zeros
class TestMaxConsecutiveZeros(unittest.TestCase):
    def test_case_22(self):
        result = max_consecutive_zeros(22)
        print(f"Result for 22: {result}")
        self.assertEqual(result, 1)
    def test_case_25(self):
        result = max_consecutive_zeros(25)
        print(f"Result for 25: {result}")
        self.assertEqual(result, 2)
    def test_case_268(self):
        result = max_consecutive_zeros(268)
        print(f"Result for 268: {result}")
        self.assertEqual(result, 4)
if __name__ == '__main__':
    unittest.main()

