import unittest
from bulb_switcher import bulb_switch


class TestBulbSwitcher(unittest.TestCase):

    def test_small_cases(self):
        self.assertEqual(bulb_switch(0), 0)
        self.assertEqual(bulb_switch(1), 1)
        self.assertEqual(bulb_switch(3), 1)

    def test_medium_cases(self):
        self.assertEqual(bulb_switch(10), 3)
        self.assertEqual(bulb_switch(16), 4)

    def test_large_cases(self):
        self.assertEqual(bulb_switch(100), 10)
        self.assertEqual(bulb_switch(1000), 31)


if __name__ == "__main__":
    unittest.main()
