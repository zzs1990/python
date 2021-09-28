# -*- coding: utf-8 -*-
# 用法：map(func, *iterables)
# 将func用于iterables中每个元素，输出一个新的iterable对象
# print(help("map"))


def remainder_divide_by_3(num: int):
    """
    除3取余
    :param num: 整数
    :return: True or False
    """
    return num % 3


def map_test():
    my_list = [i for i in range(10)]
    print(f"筛选前的序列为：{my_list}")
    new_map_object = map(remainder_divide_by_3, my_list)
    new_list = list(new_map_object)
    print(f"筛选后的序列为：{new_list}")


def main():
    map_test()


if __name__ == "__main__":
    main()
