# -*- coding: utf-8 -*-
print(f"{'-'*16}正则表达式学习{'-'*16}")
# 1. 生成包含一串数字的 list
print(f"\n1. 生成包含一串数字的 list")
my_list = [i for i in range(10)]
print(f"type: [{type(my_list)}]")
print(f"my_list: {my_list}")

# 2. 做一些数学运算
print(f"\n2. 做一些数学运算")
squares_list = [i**2 for i in range(10)]
print(f"type: [{type(squares_list)}]")
print(f"squares_list: {squares_list}")


# 3.调用一个外部函数
print(f"\n3.调用一个外部函数")
def add_2_operation(x):
    return x + 2
add2_list = [add_2_operation(i) for i in range(10)]
print(f"type: [{type(add2_list)}]")
print(f"add2_list: {add2_list}")

# 4. 生成 list 时用 if 语句进行筛选
print(f"\n4. 生成 list 时用 if 语句进行筛选")
odds_list = [i for i in range(10) if i%2 != 0]
print(f"type: [{type(odds_list)}]")
print(f"odds_list: {odds_list}")

print(f"{'-'*16}正则表达式学习{'-'*16}")
