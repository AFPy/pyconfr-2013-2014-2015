#!/usr/bin/env python

from setuptools import setup, find_packages

import symposion


setup(
    name="pyconfr",
    author="AFPy",
    author_email="orga@afpy.org",
    version="0.2",
    description="Symposion project for pyconfr 2013.",
    url="https://github.com/AFPy/pyconfr",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ),
)
