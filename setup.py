from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("gazesdk",
		sources=["gazesdk.pyx"],              
		include_dirs = ['tobii/include'],
		libraries=["TobiiGazeCore64"],
		library_dirs = ['tobii/lib'],
    )
]

setup(
  name = "gazesdk",
  ext_modules = cythonize(ext_modules)
)