# -*- coding: utf-8 -*-
# 用法：zip(*iterables)
# 将多个可迭代对象从左到右一一对应拆分为元组，然后组成一个新的可迭代对象
# print(help("zip"))


def zip_test():
    list_1 = [i for i in range(1, 10, 2)]
    print(f"list_1 为：{list_1}")
    list_2 = list("abcde")
    print(f"list_2 为：{list_2}")
    zip_list = list(zip(list_1, list_2))
    print(f"zip_list 为：{zip_list}")
    zip_dict = dict(zip(list_1, list_2))
    print(f"zip_dict 为：{zip_dict}")


def main():
    zip_test()


if __name__ == "__main__":
    main()
