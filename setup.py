from distutils.core import setup, Extension

fnv_mod = Extension('fnv_hash',
        sources = ['fnv_hash.c'])

setup(name = 'fnv1a',
        version = '0.1',
        description = 'A test',
        ext_modules = [fnv_mod],
        py_modules = ['fnv1a'])
