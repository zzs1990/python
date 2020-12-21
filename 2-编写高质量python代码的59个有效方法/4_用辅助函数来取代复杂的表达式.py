# -*- coding: utf-8 -*-
from urllib.parse import parse_qs

print(f"{'-'*16}4_用辅助函数来取代复杂的表达式{'-'*16}")
my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(my_values)

for color in ["red", "green", "opacity"]:
    print(f"{color.title()}: {my_values.get(color)}")

print("写法1：")
red = int(my_values.get("red", [""])[0] or 0)
green = int(my_values.get("green", [""])[0] or 0)
opacity = int(my_values.get("opacity", [""])[0] or 0)
print(f"red = {red}")
print(f"green = {green}")
print(f"opacity = {opacity}")

print("写法2：")
red = my_values.get("red", [""])
red = int(red[0]) if red[0] else 0
print(f"red = {red}")

print("写法3：总结为辅助函数")
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
red = get_first_int(my_values, "red", 0)
green = get_first_int(my_values, "green", 0)
opacity = get_first_int(my_values, "opacity", 0)
print(f"red = {red}")
print(f"green = {green}")
print(f"opacity = {opacity}")

# add demo here

print(f"{'-'*16}4_用辅助函数来取代复杂的表达式{'-'*16}")
