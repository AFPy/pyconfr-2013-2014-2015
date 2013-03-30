#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="pyconfr",
    author="AFPy",
    author_email="orga@afpy.org",
    version="0.2",
    description="Symposion project for pyconfr 2013.",
    url="https://github.com/AFPy/pyconfr",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires = [
        "django",
        "django-debug-toolbar",
        "django-forms-bootstrap",
        "django-mailer",
        "django-markitup",
        "django-model-utils",
        "django-reversion",
        "django-sitetree",
        "django-taggit",
        "django-timezones",
        "django-user-accounts",
        "easy-thumbnails",
        "markdown",
        "metron", # 0.2.dev3
        "pinax-theme-bootstrap",
        "pinax-theme-bootstrap-account",
        "pinax-utils",
        "pil",
        "pytz",
        "symposion",
    ],
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ),
)
