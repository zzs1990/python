# -*- coding: utf-8 -*-
"""
--Author: zhangzs
--Mailbox: 755354493@qq.com
元组tuple，一经初始化就不能修改，只能查询元素
因为tuple不可变，所以代码更安全
"""

print(f"{'-'*16}2_元组tuple基本操作{'-'*16}")


def func_1():
    """
    1.创建一个新元组
    """
    null_tuple = ()
    print(f"创建了一个空元组：{null_tuple}")
    only_one_elem_tuple = (1, )
    print(f"创建了一个单一元素元组：{only_one_elem_tuple}")
    digit_tuple = (1, 2, 3)
    print(f"创建了一个整数元组：{digit_tuple}")
    str_tuple = ("ab", "cd")
    print(f"创建了一个字符串元组：{str_tuple}")
    joined_tuple = digit_tuple + str_tuple
    print(f"组合数字元组{digit_tuple}和字符串元组{str_tuple}得到一个新元组：{joined_tuple}")


def func_2():
    """
    2.获取元组的指定元素
    """
    my_tuple = (1, 2, 3, 4)
    print(f"定义了一个整数元组：{my_tuple}")
    index_0_elem = my_tuple[0]
    print(f"元组中索引0对应的元素为：{index_0_elem}")
    index_1_to_3_elem = my_tuple[1:3]
    print(f"元组中索引1到3对应的元素集为：{index_1_to_3_elem}")


def func_3():
    """
    3.计算元组元素的个数
    """
    my_tuple = (1, 2, 3, 4)
    tuple_len = len(my_tuple)
    print(f"定义了一个长度为{tuple_len}的整数元组：{my_tuple}")


def func_4():
    """
    4.删除元组
    """
    my_tuple = (1, 2, 3, 4)
    print(f"定义了一个整数元组：{my_tuple}")
    try:
        del my_tuple
        print(f"删除元组后元组变为：{my_tuple}")
    except NameError:
        print(f"删除元组后，该元组就不存在了")


def func_5():
    """
    5.元组的内置函数：返回最大最小元素max()/min()，将序列转换为元组tuple()
    """
    my_tuple = (1, 2, 3, 4)
    print(f"定义了一个整数元组：{my_tuple}")
    print(f"元组中的最大元素为{max(my_tuple)}，最小元素为{min(my_tuple)}")
    my_list = ['a', 'b', 'c', 'd']
    print(f"将列表{my_list}转换为元组{tuple(my_list)}")


# ------------------ 以下为固定内容，修改请告知作者 ------------------
# 动态获取当前文件中定义的以 func_[数字] 命名的函数个数
func_num = 0
while True:
    try:
        func_name = f"func_{func_num+1}"
        eval(func_name)
        func_num += 1
    except NameError:
        break

# function_docs 用于保存每条目录的基本描述信息，来源于函数的doc描述
function_docs = ["START"]
# catalog 字典结构：目录 + 对应操作函数
catalog = dict()
for j in range(1, func_num+1):
    func_name = f"func_{j}"
    # 注1：eval() 可以把字符串里的字符转换为可执行代码，但只支持一行字符
    function_docs.append(eval(func_name).__doc__.split("\n")[1].strip())
    # 更新字典：{目录信息: 函数名}
    catalog.update({f"{function_docs[j]}": eval(func_name)})

# 循环执行当前文件中定义的以 func_[数字] 命名的所有函数
for content in catalog.keys():
    func = catalog.get(content)
    print(f"\033[42;31m {content}: \033[0m")
    func()
function_docs.append("END")
# ------------------ 以上为固定内容，修改请告知作者 ------------------

print(f"{'-'*16}2_元组tuple基本操作{'-'*16}")
