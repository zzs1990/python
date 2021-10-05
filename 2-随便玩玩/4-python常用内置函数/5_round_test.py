# -*- coding: utf-8 -*-
# 用法：round(number, ndigits=None)
# 四舍五入，如果ndigits缺省，则返回值为整数，否则返回与number同类型的数
# print(help("round"))


def round_test():
    data_1 = round(1.23)
    print(f"round(1.23)为：{data_1}")
    data_2 = round(1.23, 0)
    print(f"round(1.23, 0)为：{data_2}")
    data_3 = round(1.23, 1)
    print(f"round(1.23, 1)为：{data_3}")
    data_4 = round(1.23, 2)
    print(f"round(1.23, 2)为：{data_4}")
    data_5 = round(1.23, 3)
    print(f"round(1.23, 3)为：{data_5}")
    data_6 = round(10, 3)
    print(f"round(10, 3)为：{data_6}")


def main():
    round_test()


if __name__ == "__main__":
    main()
