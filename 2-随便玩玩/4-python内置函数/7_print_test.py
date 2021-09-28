# -*- coding: utf-8 -*-
# 语法：print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
import sys
# print(help("print"))
info = ["hello", "world"]

with open("print_test.log", "a+") as fd_print:
    for i, data in enumerate(info, 1):
        print(f"第{i}个数据为{data}", end=".\n", file=fd_print, flush=True)
