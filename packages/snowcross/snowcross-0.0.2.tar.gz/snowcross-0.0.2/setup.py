#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise ValueError("Requires Python 3.6+")


def requires_from_file(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as f:
        return [x.strip() for x in f if x.strip()]


with open("DESCRIPTION.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="snowcross",
    use_scm_version=True,
    description="Adaptors for tools and services in a Snowflake-centric data platform",
    long_description=description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    install_requires=requires_from_file("requirements.txt"),
    extras_require={
        "test": requires_from_file("requirements-test.txt"),
    },
    setup_requires=["setuptools_scm"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
