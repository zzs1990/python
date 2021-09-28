# -*- coding: utf-8 -*-
# cython_test setup.py
from distutils.core import setup
from Cython.Build import cythonize
setup(
    ext_modules=cythonize("cython_class_test.pyx")
)
