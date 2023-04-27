import unittest
# from of_func import citi_names
from less_07_esy_calc.less_07_func_calc import esy_calc_4


class NameTestCase(unittest.TestCase):
    # def test_citi_names_three(self):
    #     right_citi_names = citi_names("Chicago", "washington", 320)
    #     self.assertEqual(right_citi_names, "Chicago Washington 320 Population")
    #
    # def test_citi_names_two(self):
    #     right_citi_names = citi_names("chicago", "washington")
    #     self.assertEqual(right_citi_names, "Chicago Washington")

    def test_calc_4_sum(self):
        for i in range(100000):
            right_sum = esy_calc_4(i, i)
            self.assertEqual(right_sum, i+i)
            right_sum2 = esy_calc_4(i, i, "+")
            self.assertEqual(right_sum2, i+i)

    def test_calc_4_min(self):
        right_min = esy_calc_4(10, 4, "-")
        self.assertEqual(right_min, 6)

    def test_calc_4_mul(self):
        right_mul = esy_calc_4(10, 2, "*")
        self.assertEqual(right_mul, 20)

    def test_calc_4_div(self):
        for i in range(100000):
            right_div = esy_calc_4(i, 2, "/")
            self.assertEqual(right_div, i/2)


if __name__ == "__name__":
    unittest.main
