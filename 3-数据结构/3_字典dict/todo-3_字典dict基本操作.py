# -*- coding: utf-8 -*-
"""
--Author: zhangzs
"""

print(f"{'-'*16}3_字典dict基本操作{'-'*16}")

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
