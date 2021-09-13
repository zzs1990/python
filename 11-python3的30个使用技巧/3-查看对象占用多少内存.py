# -*- coding: utf-8 -*-
import sys
# 可以使用 sys.getsizeof() 来查看你创建的对象占用的内存大小

print(f"{'-'*16}查看所创建对象占用的内存{'-'*16}")

# range 函数只返回了一个类似 list 的类
# 10000个数据的类似 list 的类只占用 48 字节
class_list = range(10000)
print(f"size(range(10000)): {sys.getsizeof(class_list)}")

# 10000个数据list 占用 87616 字节
real_list = [x for x in range(10000)]
print(f"size(real_list): {sys.getsizeof(real_list)}")

print(f"{'-'*16}查看所创建对象占用的内存{'-'*16}")
