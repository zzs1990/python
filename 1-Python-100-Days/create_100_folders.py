# -*- coding: utf-8 -*-
import os
import shutil


def main():
    folders_cnt = 100
    curr_path = os.getcwd()
    module_py_path = os.path.join(curr_path, "module.py")
    for i in range(1, folders_cnt+1):
        folder_name = f"Day-{i}-TODO"
        folder_path = os.path.join(curr_path, folder_name)
        # 创建文件夹，拷贝模板文件，创建src和tests目录
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            py_name = f"day_{i}_learning.py"
            os.chdir(folder_path)
            shutil.copy2(module_py_path, py_name)
            folder_list = [
                "src",
                "tests",
            ]
            for folder in folder_list:
                if not os.path.exists(folder):
                    os.mkdir(folder)
            os.chdir(curr_path)


if __name__ == "__main__":
    main()
