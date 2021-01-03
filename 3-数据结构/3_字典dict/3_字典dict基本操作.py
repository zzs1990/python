# -*- coding: utf-8 -*-
"""
--Author: zhangzs
--Mailbox: 755354493@qq.com
字典（Dictionary），一种可变容器模型，且可存储任意类型对象
字典基本格式：new_dict = {key1 : value1, key2 : value2 }
参考链接：
1. python中的四种数据结构：https://www.cnblogs.com/pychina/p/10219772.html
2. 菜鸟教程：https://www.runoob.com/python/python-dictionary.html
"""

print(f"{'-'*16}3_字典dict基本操作{'-'*16}")


def func_1():
    """
    1.创建一个字典
    """
    null_dict_1 = {}
    print(f"通过大括号方式创建了一个空字典1：{null_dict_1}")
    null_dict_2 = dict()
    print(f"通过dict()方法创建了一个空字典2：{null_dict_2}")
    dict_3 = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(f"通过直接赋值方式创建了一个字典3：{dict_3}")
    dict_4 = {k: v for k, v in dict_3.items()}
    print(f"通过常规字典生成式方法创建了一个字典4：{dict_4}")
    dict_5 = {k: v for k, v in dict_3.items() if k % 2 == 0}
    print(f"通过加限制条件的字典生成式方法创建了一个字典5：{dict_5}")
    # fromkeys：使用指定的序列作为键，使用一个值作为字典的所有的键的值
    keys = [1, 2, 3, 4]
    dict_6 = dict.fromkeys(keys, "1111")
    print(f"通过fromkeys方式创建了一个字典6：{dict_6}")


def func_2():
    """
    2.字典的常规操作，包括访问/删除/变更/清空
    """
    my_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(f"通过直接赋值方式创建了一个字典：{my_dict}")
    # 打印键值1对应的值
    print(f"键值1对应的值为：{my_dict[1]}")
    # 打印键值5对应的值, 键值不存在时get方式可设置默认值
    print(f"键值5(该键值不存在)对应的值为：{my_dict.get(5, 'five')}")
    # 修改键值1对应的值为"one-1"
    my_dict[1] = "one-1"
    print(f"修改键值1对应的值为{'one-1'}后字典变为：{my_dict}")
    # 删除键值2和其对应的值
    del my_dict[2]
    print(f"删除键值2和其对应的值后字典变为：{my_dict}")
    my_dict.clear()
    print(f"清空后字典变为：{my_dict}")


def func_3():
    """
    3.检测字典中是否存在某成员, 键值检测
    """
    my_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(f"通过直接赋值方式创建了一个字典：{my_dict}")
    if 2 in my_dict:
        print(f"键值{2}包含在字典{my_dict}中")
    if "two" in my_dict:
        print(f"数值{'two'}包含在字典{my_dict}中")
    if (2, "two") in my_dict:
        print(f"键值对{(2, 'two')}包含在字典{my_dict}中")


def func_4():
    """
    4.使用for循环访问字典
    """
    my_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(f"通过直接赋值方式创建了一个字典：{my_dict}")
    # 方式1
    print(f"通过方式1 for循环访问字典：")
    for key in my_dict:
        print(key, my_dict[key])
    # 方式2
    print(f"通过方式2 for循环访问字典：")
    for key in my_dict.keys():
        print(key, my_dict[key])
    # 方式3
    print(f"通过方式3 for循环访问字典：")
    for value in my_dict.values():
        print(value)
    # 方式4
    print(f"通过方式4 for循环访问字典：")
    for key, value in my_dict.items():
        print(f"{key}--->{value}")


def func_5():
    """
    5.返回字典的字符串形式
    """
    my_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(f"通过直接赋值方式创建了一个字典：{my_dict}")
    str_dict = str(my_dict)
    print(f"该字典的字符串{type(str_dict)}格式为：{str_dict}")


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

print(f"{'-'*16}3_字典dict基本操作{'-'*16}")
