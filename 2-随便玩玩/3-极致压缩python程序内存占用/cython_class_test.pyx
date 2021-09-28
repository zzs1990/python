# cython_class_test.pyx


cdef class CythonPoint:
    cdef public int x, y, z

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z