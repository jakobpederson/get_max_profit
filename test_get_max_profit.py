import unittest
import get_max_profit

VALUES = [10, 7, 5, 8, 11, 9, 1, 0]
VALUES_ONE = [10]
EXPECTED = 6


class GetMaxProfitTest(unittest.TestCase):

    def setUp(self):
        self.calculator = get_max_profit.GetMaxProfit()


    def test_get_max_difference(self):
        result = self.calculator.get_max_difference(VALUES)
        self.assertEqual(EXPECTED, result)

    def test_check_values_length_if_gt_2(self):
        self.assertEqual(True, self.calculator.check_values_length(VALUES))

    def test_check_values_length_if_lt_2(self):
        self.assertEqual(False, self.calculator.check_values_length(VALUES_ONE))

    def test_calculate_max_profit(self):
        result = self.calculator.calculate_max_profit(VALUES)
        result_one = self.calculator.calculate_max_profit(VALUES_ONE)
        self.assertEqual(EXPECTED, result)
        self.assertEqual('Error: not enough values', result_one)
