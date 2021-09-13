# -*- coding: utf-8 -*-
"""
-- 创建进度条
"""
from progressbar import *
import time

print(f"{'-'*16}创建进度条{'-'*16}")

total = 100


def do_some_work():
    time.sleep(0.1)


progress = ProgressBar()
for i in progress(range(total)):
    do_some_work()

print(f"{'-'*16}创建进度条{'-'*16}")
