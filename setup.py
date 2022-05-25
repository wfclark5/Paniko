import os
import paniko

from setuptools import setup, find_packages




VERSION = (1, 0, 0)

__title__ = 'paniko'
__author__ = 'William Clark'
__email__ = 'wfclark5@outlook.com'
__license__ = 'Apache License 2.0'
__version__ = '.'.join(map(str, VERSION))

setup(
    name='paniko',
    version='1.0.0',
    packages=find_packages(
        exclude=('tests', '*tests', '*tests*')
    ),  # We throw away from the assembly too much.
    include_package_data=True,
    license='Apache 2.0',  # Put the license.
    description='Python Kaniko https://github.com/GoogleContainerTools/Kaniko',
    install_requires=[],
    tests_require=['codecov>=2', 'coverage>=4'],
    setup_requires=['twine>=1', 'mkdocs>=1'],
    author='William Clark',
    author_email='wfclark5@outlook.com',
    maintainer='William Clark',
    maintainer_email='wfclark5@outlook.com',
    zip_safe=True,
)
