#!python
#cython: language_level=3, boundscheck=False

cdef class Scanner:
    def __cinit__(self, saludo):
        print('hola' + saludo)
        
    def __init__(self, saludo):
        print('julio')
