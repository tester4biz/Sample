# -*- coding: utf-8 -*-

from main import main
import unittest


class TestMain(unittest.TestCase):

    def test_tashizan(self):
        m = main.Main('jiro', 28)
        self.assertEqual(m.get_name(), 'jiro')
        self.assertEqual(m.get_age(), 28)

if __name__ == "__main__":
    unittest.main()
