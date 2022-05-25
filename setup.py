from setuptools import setup, find_packages


setup(
    name="paniko",
    version="1.0.0",
    packages=find_packages(where="paniko"),
    license="Apache 2.0",
    long_description=open("README.md", encoding='utf-8').read(),
    description="Python Kaniko https://github.com/GoogleContainerTools/Kaniko",
    install_requires=[],
    tests_require=["codecov>=2", "coverage>=4"],
    setup_requires=["twine>=1", "mkdocs>=1"],
    author="William Clark",
    author_email="wfclark5@outlook.com",
    maintainer="William Clark",
    maintainer_email="wfclark5@outlook.com",
    zip_safe=True,
)
