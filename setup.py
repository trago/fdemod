from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("fdemod._scanner", ["fdemod/_scanner.pyx"],
        include_dirs = [],
        libraries = [],
        library_dirs = []),
    # Everything but primes.pyx is included here.
 ]

setup(name='fdemod',
    version='0.1',
    description='Fringe pattern demodulation',
    author='Julio C. Estrada',
    author_email='julio@cimat.mx',
    #url='https://www.python.org/sigs/distutils-sig/',
    #package_dir = {'':'lib'},
    packages=['fdemod'],
    ext_modules = cythonize(extensions),
)