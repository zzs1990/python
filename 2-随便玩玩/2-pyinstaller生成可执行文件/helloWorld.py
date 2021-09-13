# -*- coding: utf-8 -*-
import time

print("Hello World")
print("开始倒计时...")
for i in range(5, 0, -1):
    print(f"{i}")
    time.sleep(1)
print("Game Over")
time.sleep(2)
