import unittest
from program import string_numbers_till_n

class TestString(unittest.TestCase):
    def test1(self):
        result1 = string_numbers_till_n(2)
        self.assertEqual(result1, "0 1 2")
    def test2(self):
        result2 = string_numbers_till_n(5)
        self.assertEqual(result2, "0 1 2 3 4 5")
    def test3(self):
        result3 = string_numbers_till_n(10)
        self.assertEqual(result3, "0 1 2 3 4 5 6 7 8")
    def test4(self):
        result3 = string_numbers_till_n(0)
        self.assertEqual(result3, "0")


if __name__ == '__main__':
    unittest.main()
