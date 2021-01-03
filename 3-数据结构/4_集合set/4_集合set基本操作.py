# -*- coding: utf-8 -*-
"""
--Author: zhangzs
--Mailbox: 755354493@qq.com
集合set,集合中每个元素都是无序的、不重复的任意对象
特征：
1. 无序性 -- 无法使用索引和分片
2. 唯一性 -- 可以用来排除重复数据
"""

print(f"{'-'*16}4_集合set基本操作{'-'*16}")


def func_1():
    """
    1.创建一个集合
    """
    null_set = set()
    print(f"创建了一个空集合：{null_set},其类型为{type(null_set)}")
    # 创建集合要以list作为输入，通过add方法增加元素，remove方法删除元素
    digit_list = [1, 2, 3, 4, 5]
    digit_set = set(digit_list)
    print(f"输入列表{digit_list}得到集合{digit_set}")
    digit_set.add(6)
    print(f"新增元素6后集合变为：{digit_set}")
    digit_set.remove(2)
    print(f"删除元素2后集合变为：{digit_set}")


def func_2():
    """
    2.集合的基本函数：交集-intersection，差集-difference，并集-union
    """
    # 交集：AB  两个集合的所有公共元素组成的集合
    # 并集：A+B 包含两个集合所有元素的最小集合
    # 差集：A-B 元素在集合A中，但不在集合B中
    # 子集：A中所有元素都在B中，则A是B的子集，B是A的超集
    set_1 = {1, 2, 3, 4, 5, 6, 7}
    set_2 = {5, 6, 7, 8, 9}
    print(f"创建了两个集合：{set_1}和{set_2}")
    inter_set = set_1.intersection(set_2)
    print(f"两个集合的交集为：{inter_set}")
    diff_set = set_1.difference(set_2)
    print(f"两个集合的差集为：{diff_set}")
    union_set = set_1.union(set_2)
    print(f"两个集合的并集为：{union_set}")
    if_subset = set_1.issubset(set_2)
    print(f"集合{set_1}是否为集合{set_2}的子集：{if_subset}")
    set_3 = {1, 2, 3}
    if_subset = set_3.issubset(set_1)
    print(f"集合{set_3}是否为集合{set_1}的子集：{if_subset}")
    if_subset = set_1.issubset(set_3)
    print(f"集合{set_1}是否为集合{set_3}的子集：{if_subset}")
    if_subset = set_1.issubset(set_1)
    print(f"集合{set_1}是否为集合{set_1}的子集：{if_subset}")
    is_superset = set_1.issuperset(set_3)
    print(f"集合{set_1}是否为集合{set_3}的超集：{is_superset}")
    is_superset = set_3.issuperset(set_1)
    print(f"集合{set_3}是否为集合{set_1}的超集：{is_superset}")
    is_superset = set_1.issuperset(set_1)
    print(f"集合{set_1}是否为集合{set_1}的超集：{is_superset}")


def func_3():
    """
    3.创建一个冰冻集合--不可以进行任何修改的集合
    """
    frozen_set = frozenset([1, 2, 3, 4, 5])
    print(f"创建了一个冰冻集合：{frozen_set}")
    try:
        frozen_set.add(6)
        print(f"新增元素6后冰冻集合变为：{frozen_set}")
    except AttributeError:
        print(f"{'frozenset'} object has no attribute {'add'}")
    try:
        frozen_set.remove(2)
        print(f"删除元素2后冰冻集合变为：{frozen_set}")
    except AttributeError:
        print(f"{'frozenset'} object has no attribute {'remove'}")


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

print(f"{'-'*16}4_集合set基本操作{'-'*16}")
