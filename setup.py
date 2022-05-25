import os
import paniko

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    README = f.read()


setup(
    name=paniko.__title__,
    version=paniko.__version__,
    packages=find_packages(
        exclude=('tests', '*tests', '*tests*')
    ),  # We throw away from the assembly too much.
    include_package_data=True,
    test_suite='tests',  # Include tests.
    license='Apache 2.0',  # Put the license.
    description='Python paniko https://github.com/GoogleContainerTools/Kaniko',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=[],
    tests_require=['codecov>=2', 'coverage>=4'],
    setup_requires=['twine>=1', 'mkdocs>=1'],
    url=paniko.__url__,
    author=paniko.__author__,
    author_email=paniko.__email__,
    maintainer='William Clark',
    maintainer_email='wfclark5@outlook.com',
    classifiers=[
        'Environment :: Server Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=True,
)
