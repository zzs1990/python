# -*- coding: utf-8 -*-
"""
# list的显著特征：
# 列表中的每个元素都可变的，意味着可以对每个元素进行修改和删除；
# 列表是有序的，每个元素的位置是确定的，可以用索引去访问每个元素；
# 列表中的元素可以是Python中的任何对象；
# 可以为任意对象就意味着元素可以是字符串、整数、元组、也可以是list等Python中的对象。
# 参考链接：https://www.cnblogs.com/pychina/p/10219772.html
"""

print(f"{'-'*16}1_列表基本操作{'-'*16}")


def func_1():
    """
    1.直接创建列表 -- 形如 new_list = [1, 2, 3]
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"创建列表: {my_list}")

def func_2():
    """
    2.对列表中的指定位置变更数据 -- 形如 new_list[1] = 10
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始列表为: {my_list}")
    # 变更索引位置1 Yahoo的内容为Microsoft
    index_1_elem = my_list[1]
    my_list[1] = 'Microsoft'
    print(f"变更索引位置1的元素’{index_1_elem}‘的内容为'{'Microsoft'}'后，列表变为：{my_list}")

def func_3():
    """
    3.在列表后面追加元素 -- 形如 new_list.append(4)
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始列表为: {my_list}")
    # 尾部新增元素 'Alibaba'
    my_list.append('Alibaba')
    print(f"尾部新增元素'{'Alibaba'}'后，列表变为：{my_list}")

def func_4():
    """
    4.在指定位置插入元素 -- 形如 new_list.insert(1, 10)
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始列表为: {my_list}")
    # 插入元素 'Tencent'
    my_list.insert(1, 'Tencent')
    print(f"在指定位置索引[{1}]处插入元素'{'Tencent'}'后，列表变为：{my_list}")

def func_5():
    """
    5.删除元素 -- pop(), remove(), del
    """
    my_list = ['Google', 'Tencent', 'Microsoft', 'Baidu', 'Alibaba']
    print(f"初始列表为: {my_list}")
    # 删除尾部元素,会返回被删除元素
    del_elem = my_list.pop()
    print(f"删除尾部元素'{del_elem}'后,列表变为: {my_list}")
    # 删除索引为1的元素，并返回删除的元素
    index_1_elem = my_list.pop(1)
    print(f"删除索引为1的元素'{index_1_elem}'后,列表变为: {my_list}")
    # 删除列表中的Microsoft
    my_list.remove('Microsoft')
    print(f"删除列表中的元素'{'Microsoft'}'后,列表变为: {my_list}")
    # 删除列表中索引位置 1 到位置 3 的数据
    my_list = ['Google', 'Tencent', 'Microsoft', 'Baidu', 'Alibaba']
    print(f"恢复初始列表为: {my_list}")
    temp_list = my_list[1:3]
    del my_list[1:3]
    print(f"删除索引位置1到3的数据'{temp_list}'后,列表变为: {my_list}")

def func_6():
    """
    6.替换元素 -- 形如 new_list[1] = 10, 同 func_2
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始列表为: {my_list}")
    # 替换索引为0的元素为 'Tencent'
    index_0_elem = my_list[0]
    my_list[0] = 'Tencent'
    print(f"替换索引为0的元素'{index_0_elem}'为'{'Tencent'}'后,列表变为：{my_list}")

def func_7():
    """
    7.列表排序 -- sort()
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始字符串列表为: {my_list}")
    # 字符串列表排序,默认为False,即按ASCII码顺序排序
    my_list.sort()
    print(f"对字符串列表按ASCII码顺序排序后,列表变为：{my_list}")
    my_list.sort(reverse=True)
    print(f"对字符串列表按ASCII码逆序排序后,列表变为：{my_list}")
    my_list = [1, 3, 4, 2]
    print(f"初始数字列表为: {my_list}")
    # 数字列表排序,默认为False,即从小到大排序
    my_list.sort()
    print(f"对数字列表从小到大排序后,列表变为：{my_list}")
    my_list.sort(reverse=True)
    print(f"对数字列表从大到小排序后,列表变为：{my_list}")

def func_8():
    """
    8.获取列表长度 -- len()
    """
    my_list = ['Google', 'Yahoo', 'Baidu']
    print(f"初始列表为: {my_list}")
    # 替换索引为0的元素为 'Tencent'
    list_len = len(my_list)
    print(f"列表长度为：{list_len}")

def func_9():
    """
    9.获取列表指定位置的数据 -- my_list[1], my_list[1:5], my_list[:5], my_list[1:]
    """
    my_list = ['Google', 'Tencent', 'Microsoft', 'Baidu', 'Alibaba', 'Sina']
    print(f"初始列表为: {my_list}")
    # 获取索引位置1的数据
    index_1_elem = my_list[1]
    print(f"索引位置1的数据为: {index_1_elem}")
    # 获取索引位置1到索引4的数据
    index_1to4_elem = my_list[1:4 + 1]
    print(f"索引位置1到索引4的数据为: {index_1to4_elem}")
    # 获取起始位置（即索引0）到索引4的数据
    index_start_to4_elem = my_list[:4 + 1]
    print(f"起始位置（即索引0）到索引4的数据为: {index_start_to4_elem}")
    # 获取从索引位置1到末尾的数据
    index_1to_end_elem = my_list[1:]
    print(f"索引位置1到末尾的数据为: {index_1to_end_elem}")

def func_10():
    """
    10.用循环来创建列表 -- my_list = [i for i in range(5)]
    """
    my_list = [i for i in range(5)]
    print(f"通过循环方式获取到的数字列表为: {my_list}")

def func_11():
    """
    11.过滤列表中的内容放入新的列表中 -- my_list = [i for i in range(5) if i % 2 == 0]
    """
    my_list = [i for i in range(5) if i % 2 == 0]
    print(f"过滤列表中的偶数生成新的列表为: {my_list}")

def func_12():
    """
    12.嵌套式生成列表 -- my_list = [x+y for x in list_a for y in list_b]
    """
    # 生成一个10以内的奇数列表,5个元素，即[1, 3, 5, 7, 9]
    list_odd = [i for i in range(10) if i % 2 == 1]
    print(f"生成一个10以内的奇数列表: {list_odd}")
    # 生成一个10到101的20的倍数列表,5个元素，即[20, 40, 60, 80, 100]
    list_10_multi = [i for i in range(10, 101) if i % 20 == 0]
    print(f"生成一个10到100的20的倍数列表: {list_10_multi}")
    # 两个列表嵌套，得到的新列表为 5*5=25个元素
    my_list = [x+y for x in list_odd for y in list_10_multi]
    print(f"两个列表嵌套，每个元素相加得到的新列表为: {my_list}")


# function_docs 用于保存每条目录的基本描述信息，来源于函数的doc描述
function_docs = ["start"]
# catalog 字典结构：目录 + 对应操作函数
catalog = dict()
for j in range(1, 13):
    func_name = f"func_{j}"
    # 注1：eval() 可以把字符串里的字符转换为可执行代码，但只支持一行字符
    function_docs.append(eval(func_name).__doc__.split("\n")[1].strip())
    # 更新字典：{目录信息: 函数名}
    catalog.update({f"{function_docs[j]}": eval(func_name)})

for content in catalog.keys():
    func = catalog.get(content)
    print(f"\033[40;36m {content}: \033[0m")
    func()

print(f"{'-'*16}1_列表基本操作{'-'*16}")
