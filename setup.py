from distutils.core import setup, Extension

name = "swig_c_code"
version = "1.0"

setup(name=name, version=version,
      ext_modules=[Extension(name='_swig_c_code',
                             sources=["swig_c_code.i", "src/swig_c_code.c"],
                             include_dirs=['src'])
                   ])
