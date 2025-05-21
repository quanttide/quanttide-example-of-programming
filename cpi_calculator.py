"""
CPI计算器
"""

class CPICalculator:
    def __init__(self):
        pass

    def calculate_cpi(self, current_price, previous_price):
        """
        计算CPI
        :param current_price: 当前价格
        :param previous_price: 上年价格
        :return: CPI值
        """
        if previous_price == 0:
            raise ValueError("Previous price cannot be zero.")
        
        cpi = (current_price / previous_price) * 100
        return cpi


def calculate_cpi(current_price, previous_price):
    """
    计算CPI
    :param current_price: 当前价格
    :param previous_price: 上年价格
    :return: CPI值
    """
    if previous_price == 0:
        raise ValueError("Previous price cannot be zero.")
    
    cpi = (current_price / previous_price) * 100
    return cpi


def main():
    """
    主函数
    """
    current_price = float(input("Enter current price: "))
    previous_price = float(input("Enter previous price: "))
    
    try:
        cpi = calculate_cpi(current_price, previous_price)
        print(f"CPI: {cpi:.2f}%")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
