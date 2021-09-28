# -*- coding: utf-8 -*-
from sys import getsizeof as sys_getsizeof
from collections import namedtuple
from recordclass import recordclass
from recordclass import make_dataclass
from cython_class_test import CythonPoint

# 1. 简单字典，内存占用232字节
simple_dict = {
    "x": 1,
    "y": 2,
    "z": 3,
}
print(f"1. 字典 simple_dict 内存占用 {sys_getsizeof(simple_dict)} 字节")
print(f"simple_dict.get('x') = {simple_dict.get('x')}\n")


# 2. 对象及类的属性值，内存占用152字节， 48+104
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
point_A = Point(1, 2, 3)
print(f"2. 类和对象 point_A 内存占用 {sys_getsizeof(point_A)} 字节")
print(f"point_A.__dict__ 内存占用 {sys_getsizeof(point_A.__dict__)} 字节")
print(f"point_A.x = {point_A.x}\n")

# 3. collections中的namedtuple可代替字典，内存占用64字节
namedTuplePoint = namedtuple("Point", ["x", "y", "z"])
point_B = namedTuplePoint(1, 2, 3)
print(f"3. namedtuple point_B 内存占用 {sys_getsizeof(point_B)} 字节")
print(f"point_B.x = {point_B.x}\n")


# 4. __slots__ 方式，内存占用 56 字节
class Point:
    __slots__ = "x", "y", "z"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
point_C = Point(1, 2, 3)
print(f"4. 类__slots__方式 point_C 内存占用 {sys_getsizeof(point_C)} 字节")
print(f"point_C.x = {point_C.x}\n")

# 5. 第三方包 recordclass 中的 mutabletuple 类型，内存占用40字节
mutableTuplePoint = recordclass("Point", ["x", "y", "z"])
point_D = mutableTuplePoint(1, 2, 3)
print(f"5. 第三方包 recordclass mutabletuple point_D 内存占用 {sys_getsizeof(point_D)} 字节")
print(f"point_D.x = {point_D.x}\n")

# 6. 第三方包 recordclass 中的 make_dataclass 类型，内存占用40字节
dataClassPoint = make_dataclass("Point", ["x", "y", "z"])
point_E = dataClassPoint(1, 2, 3)
print(f"6. 第三方包 recordclass make_dataclass point_E 内存占用 {sys_getsizeof(point_E)} 字节")
print(f"point_E.x = {point_E.x}\n")

# 7. Cython 方式导入，内存占用32字节
point_F = CythonPoint(1, 2, 3)
print(f"7. Cython CythonPoint point_F 内存占用 {sys_getsizeof(point_F)} 字节")
print(f"point_F.x = {point_F.x}\n")
