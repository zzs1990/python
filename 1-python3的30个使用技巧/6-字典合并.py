# -*- coding: utf-8 -*-
print(f"{'-'*16}字典合并{'-'*16}")

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 1, "c": 3, "d": 4}
print(f"待合并的两个字典为：\n{dict_1}\n{dict_2}")
merged_dict = {**dict_1, **dict_2}
print(f"合并后的字典为：\n{merged_dict}")

print(f"{'-'*16}字典合并{'-'*16}")
