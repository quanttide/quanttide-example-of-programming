"""
CPI计算器单元测试
"""
import unittest

from cpi_calculator import calculate_cpi


class TestCpiCalculator(unittest.TestCase):
    """
    CPI计算器单元测试类
    """
    def test_calculate_cpi(self):
        """
        测试计算CPI函数
        """
        # 正常情况
        current_price = 100
        previous_price = 80
        cpi = calculate_cpi(current_price, previous_price)
        self.assertAlmostEqual(cpi, 25.0, delta=0.1)

        # 上年价格等于0
        current_price = 100
        previous_price = 0
        with self.assertRaises(ValueError):
            calculate_cpi(current_price, previous_price)
        
        # 上年价格小于0
        current_price = 100
        previous_price = -10
        with self.assertRaises(ValueError):
            calculate_cpi(current_price, previous_price)
            
        # 当前价格小于0
        current_price = -100
        previous_price = 80
        with self.assertRaises(ValueError):
            calculate_cpi(current_price, previous_price)
            
        # 当前价格等于0
        current_price = 0
        previous_price = 80
        with self.assertRaises(ValueError):
            calculate_cpi(current_price, previous_price)


if __name__ == "__main__":
    unittest.main()
