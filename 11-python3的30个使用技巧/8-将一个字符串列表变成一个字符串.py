# -*- coding: utf-8 -*-

print(f"{'-'*16}将一个字符串列表变成一个字符串{'-'*16}")

my_list = ["hello", "world", "I'm", "Jupiter"]
print(f"待合并的字符串列表为：\n{my_list}")

#  String.join() 可以连接任何可迭代对象，不只是列表
print(f"String.join() 可以连接任何可迭代对象，不只是列表")
my_string = " ".join(my_list)
print(f"合并后的字符串为：\n{my_string}")

print(f"{'-'*16}将一个字符串列表变成一个字符串{'-'*16}")
