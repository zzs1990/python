# -*- coding: utf-8 -*-

print(f"{'-'*16}使用map{'-'*16}")


def upper(string):
    return string.upper()


my_list = list(map(upper, ["asdf", "fghj"]))
print(my_list)

list_of_ints = list(map(int, "1234567"))
print(list_of_ints)

print(f"{'-'*16}使用map{'-'*16}")
