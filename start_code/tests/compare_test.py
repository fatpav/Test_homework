import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_can_tell_if_number_is_not_greater(self):
        self.assertEqual("5 is not greater than 7", compare(5, 7))

    