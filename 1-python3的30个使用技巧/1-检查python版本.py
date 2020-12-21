import sys

print(f"{'-'*16}查看python版本{'-'*16}")
version = sys.version_info
print(f"获取到的python版本信息如下：\n{version}")

print(f"非必要请不要使用 python2.* 版本")
print(f"要求python版本大于2.7，并且不低于3.5，检查结果如下：\n")
if not version > (2, 7):
    print("You are using a python <= 2.7")
elif not version >= (3, 5):
    print("You are using python < 3.5, update now")
else:
    print(f"python version ok, no need to update")
