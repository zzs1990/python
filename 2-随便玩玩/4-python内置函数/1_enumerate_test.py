# -*- coding: utf-8 -*-
# 用法：enumerate(iterable, start=0)
# 返回序列中元素的索引值和元素
# print(help("enumerate"))


def enumerate_test():
    my_list = ["XiaoMing", "XiaoHong", "XiaoBai"]
    print("直接打印结果为：")
    for i in enumerate(my_list):
        print(i)
    print("\nindex从1开始：")
    for index, item in enumerate(my_list, 1):
        print(f"第 {index} 个元素是 {item}")


def main():
    enumerate_test()


if __name__ == "__main__":
    main()
