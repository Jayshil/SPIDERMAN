import setuptools
from distutils.core import setup, Extension

_web = Extension("spiderman._web",["c_src/_web.c","c_src/heron.c","c_src/segment.c","c_src/areas.c","c_src/intersection.c","c_src/generate.c","c_src/blocked.c","c_src/util.c","c_src/pyutil.c","c_src/web.c","c_src/orthographic.c","c_src/ephemeris.c","c_src/blackbody.c","c_src/spline.c","c_src/brightness_maps.c","c_src/legendre_polynomial.c","c_src/bicubic.c","c_src/nrutil.c"
], extra_compile_args = ["-std=c99"])

setup(	name='spiderman-package',
	version="1.0.3",
	author='Tom Louden',
	author_email = 't.louden@warwick.ac.uk',
	url = 'https://github.com/tomlouden/spiderman',
	download_url = 'https://github.com/tomlouden/spiderman/tarball/1.0.2',
	packages =['spiderman'],
	license = 'GNU GPLv3',
	description ='Fast secondary eclipse and phase curve modeling',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Programming Language :: Python'
		],
	install_requires = ['numpy', 'opencv-python'],
	setup_requires=['distutils', 'setuptools','wheel'],
    cmdclass={'build': build},
	ext_modules=[_web],
	package_data = {'spiderman': ['art/*','test_data/*']},
)
