Cython方式编译：
1. 先编辑 cython_class_test.pyx 文件，定义类；
2. 再编辑 cython_setup.py 文件，指定要编译的文件；
3. 编译 python cython_setup.py build_ext --inplace，生成pyd文件，重命名一下即可；