import os
import pathlib

from setuptools import setup, find_packages
from setuptools_github import tools

initfile = pathlib.Path(__file__).parent / "src" / "argparse_plus" / "__init__.py"
version = tools.update_version(initfile, os.getenv("GITHUB_DUMP"))

setup(
    name="argparse-plus",
    version=version,
    description="An extension to argparse",
    url="https://github.com/cav71/argparse-plus",
    packages=find_packages("src"),

    # CHANGEME adds as many entry points as you need
    entry_points={
        "console_scripts": ["argparse_plus=argparse_plus:main"],
    },

    # CHANGEME replace "text/markdown" with "text/x-rst" for rst READMEs
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",

    # CHANGEME adds as many classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
