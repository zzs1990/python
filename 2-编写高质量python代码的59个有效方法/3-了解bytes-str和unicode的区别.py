# -*- coding: utf-8 -*-
from sys import getsizeof

print(f"{'-'*16}3-了解bytes,str和unicode的区别{'-'*16}")

# 1. bytes 函数:
# Python3 内置函数, 返回一个新的 bytes 对象，
# 该对象是一个 0 <= x < 256 区间内的整数不可变序列
# 语法：class bytes([source[, encoding[, errors]]])
print("1-bytes 测试:")
print(f"参考链接：{'https://www.runoob.com/python3/python3-func-bytes.html'}")
print("1.1 如果没有输入任何参数，默认就是初始化数组为0个元素:")
tmp_bytes = bytes()
print(tmp_bytes)
# 输出：b''
print("1.2 如果 source 为整数，则返回一个长度为 source 的初始化数组:")
int_bytes = bytes(1)
print(int_bytes)
# 输出：b'\x01'
print("1.3 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列:")
try:
    str_bytes = bytes('hello')
except TypeError:
    print(f"exception: {TypeError}")
    str_bytes = bytes('hello', encoding="utf-8")
else:
    print("no exception")
finally:
    print(str_bytes)
# 输出：b'hello'
print("1.4 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数:")
int_list_bytes = bytes([1, 2, 3, 4])
print(int_list_bytes)
# 输出：b'\x01\x02\x03\x04'

# 2. str 函数:
# Python3 内置函数, 将对象转化为适于人阅读的字符串形式，
# 语法：class str(object='')
print("2-str 测试: 输出数据用@@隔开以示区分")
print(f"参考链接：{'https://www.runoob.com/python/python-func-str.html'}")
print("2.1 输入为整数:")
int_str = str(1)
print(f"str(1) = @@{int_str}@@, 输出类型为：{type(int_str)}")
print("2.2 输入为整数列表:")
int_list_str = str([1, 2, 3, 4])
print(f"str([1, 2, 3, 4]) = @@{int_list_str}@@, 输出类型为：{type(int_list_str)}")
print("2.3 输入为字典:")
dict_str = str({"Xiaoming": 80, "Xiaogang": 91})
print(f"dict_str = @@{dict_str}@@, 输出类型为：{type(dict_str)}")

# 3. unicode 函数:
# python3中废弃了该函数，不详细介绍
# Python2中有两类字符串，分别是str与unicode
# Unicode编码是固定2个字节代表一个字符,
# 而Utf-8是对英文只用一个字节，对中文是3个字节
# 在字符串前加上u即unicode编码
unicode_str = u"hello"
unicode_str_size = getsizeof(unicode_str)
print(f"unicode_str[{unicode_str_size}] = [{unicode_str}]")
print(f"类型为：{type(unicode_str)}")
chinese_str = u"你好"
chinese_str_size = getsizeof(chinese_str)
print(f"chinese_str[{chinese_str_size}] = [{chinese_str}]")
print(f"类型为：{type(chinese_str)}")

print(f"{'-'*16}3-了解bytes,str和unicode的区别{'-'*16}")
