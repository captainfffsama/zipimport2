from distutils import extension
from setuptools import setup,find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions=[
    Extension("zipimport2",["zipimport2.pyx"])
]

setup(
        name="zipimport2",
        version='v0.1',
        description='zipimport support encrypt zip',
        author='captainfffsama',
        author_email='tuanzhangsama@outlook.com',
        packages=find_packages(),
        include_package_data=True,
        license='MIT License',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        ext_modules=cythonize(extensions,language_level=3)
)
