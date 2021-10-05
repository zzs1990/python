# -*- coding: utf-8 -*-
# 用法：filter(function or None, iterable)
# 过滤iterable中的元素，返回 满足function为True 的元素序列
# If function is None, return the items that are true.
# print(help("filter"))


def if_divide_by_3(num: int):
    """
    被3整除
    :param num: 整数
    :return: True or False
    """
    ret = False
    if num % 3 == 0:
        ret = True
    return ret


def filter_test():
    my_list = [i for i in range(10)]
    print(f"筛选前的序列为：{my_list}")
    new_filter_object = filter(if_divide_by_3, my_list)
    new_list = list(new_filter_object)
    print(f"筛选后的序列为：{new_list}")


def main():
    filter_test()


if __name__ == "__main__":
    main()
