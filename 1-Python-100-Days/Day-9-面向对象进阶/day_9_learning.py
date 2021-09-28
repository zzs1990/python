# -*- coding: utf-8 -*-
"""
******************** 人生苦短，我用Python ********************
--- Day 1: 面向对象进阶
--- Notes:
  --1. @property装饰器，包装getter和setter方法
  --2. __slots__魔法
--- Author: zhangzai
--- My Motto:
  --1. 达则兼济天下，穷则独善其身
  --2. 修学储能，先博后渊
******************** 人生苦短，我用Python ********************
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
