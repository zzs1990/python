# -*- coding: utf-8 -*-
"""
--Author: zhangzs
元组tuple，一经初始化就不能修改，只能查询元素
因为tuple不可变，所以代码更安全
"""

print(f"{'-'*16}2_元组tuple基本操作{'-'*16}")


def func_1():
    """
    1.获取元组的指定元素
    """
    my_tuple = (1, 2, 3)
    print(f"定义了一个整数元组：{my_tuple}")
    index_1_elem = my_tuple[1]
    print(f"元组中索引1对应的元素为：{index_1_elem}")


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
