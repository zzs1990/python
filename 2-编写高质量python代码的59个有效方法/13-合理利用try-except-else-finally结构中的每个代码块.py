# -*- coding: utf-8 -*-
try:
    # 可能会抛出异常的代码
    a = 1 / 0
except:
    # 异常处理
    print("除法运算中被除数不能为0")
    a = 1
else:
    a = 1 / 0.3
    # 如果没有异常则执行的代码，应该尽量减少try语句下的代码，后续逻辑放else这边来
    a = round(a, 3)
    print(a)
finally:
    # 无论如何都会执行的代码
    print(f"相除结束，a = {a}")
