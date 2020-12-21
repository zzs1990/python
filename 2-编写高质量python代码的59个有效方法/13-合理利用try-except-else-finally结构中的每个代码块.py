# -*- coding: utf-8 -*-
num_list = [i for i in range(10)]

try:
    # 可能会抛出异常的代码
    new_list = [1 / i for i in num_list]
except ZeroDivisionError:
    # 异常处理
    print("除法运算中被除数不能为0")
    new_list = [1 / i for i in num_list if i != 0]
else:
    # 如果没有异常则执行的代码，应该尽量减少try语句下的代码，后续逻辑放else这边来
    print("计算无异常")
finally:
    # 无论如何都会执行的代码
    new_list = [round(data, 3) for data in new_list]
    print(f"最终得到的列表长度为：{len(new_list)}, 数据如下：")
    print(new_list)
