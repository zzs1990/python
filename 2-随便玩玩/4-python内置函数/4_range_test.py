# -*- coding: utf-8 -*-
# 用法：range(start, stop[, step])
# 返回一个从start开始，到stop结束，步长为step的对象，不包含stop
# print(help("range"))


def range_test():
    my_list = [i for i in range(1, 10, 2)]
    print(f"range生成的序列为：{my_list}")
    my_object = range(1, 10, 3)
    print(f"range生成的对象为：{my_object}")
    my_list = list(my_object)
    print(f"range生成的序列为：{my_list}")


def main():
    range_test()


if __name__ == "__main__":
    main()
