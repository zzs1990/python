# -*- coding: utf-8 -*-
"""
-- 给文字加颜色和背景
"""
from colorama import Fore, Back, Style

print(f"{'-'*16}给文字加颜色和背景{'-'*16}")

print(Fore.RED + "some red text")
print(Back.GREEN + "with green background")
print(Style.DIM + "in dim text")
print(Style.RESET_ALL)
print("back to normal")

print(f"{'-'*16}给文字加颜色和背景{'-'*16}")

