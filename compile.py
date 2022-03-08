from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("nisas.core",  ["nisas/core.py"]),
    #Extension("tests.integration.test_nisas",
    #          ["tests/integration/test_nisas.py"]),
    #   ... all your modules that need be compiled ...
]
setup(
    name='nisas',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
