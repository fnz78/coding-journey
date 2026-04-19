import unittest
from src.solution import count_substrings


class TestCountSubstrings(unittest.TestCase):

    def test_example(self):
        self.assertEqual(count_substrings("0110111"), 9)

    def test_all_ones(self):
        self.assertEqual(count_substrings("111"), 6)

    def test_no_ones(self):
        self.assertEqual(count_substrings("000"), 0)

    def test_single_one(self):
        self.assertEqual(count_substrings("1"), 1)

    def test_mixed(self):
        self.assertEqual(count_substrings("10101"), 3)


if __name__ == "__main__":
    unittest.main()
