from distutils.core import setup
from Cython.Build import cythonize

from distutils.core import setup

setup(name='fdemod',
    version='0.1',
    description='Fringe pattern demodulation',
    author='Julio C. Estrada',
    author_email='julio@cimat.mx',
    #url='https://www.python.org/sigs/distutils-sig/',
    #packages=['distutils', 'distutils.command'],
    ext_modules = cythonize("hello.pyx"),
)
