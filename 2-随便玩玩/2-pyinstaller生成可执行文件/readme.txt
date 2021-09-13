1. 简单工具-倒计时显示--dist下生成一个exe文件，但文件较大 6.4M
pyinstaller -F helloWorld.py

2. 图形界面wxPython -- dist下生成一个exe文件，但文件较大 13.3M
pyinstaller -F wxHelloWorld.py

3. pipenv -- 管理虚拟环境的命令行工具
指定目录下执行： pipenv install --python 3.7
参考pipenv使用说明文档操作即可，实际生成的exe大小和2相同


