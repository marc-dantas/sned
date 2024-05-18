from setuptools import setup, find_packages

NAME = "sned"
AUTHOR = "Marcio Dantas"
VERSION = "0.1.0"
DESCRIPTION = "A minimalistic Python editor"
LONG_DESCRIPTION = "A minimalistic and customizable Python code editor"

setup(
    name=NAME, 
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
)
