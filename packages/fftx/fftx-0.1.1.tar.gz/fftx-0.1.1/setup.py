##  Copyright (c) 2018-2023, Carnegie Mellon University
##  All rights reserved.
##
##  See LICENSE file for full information
##  SPDX-License-Identifier: BSD-3-Clause

##  fftx/setup.py

from setuptools import setup, find_packages
import codecs
import os.path
import glob

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="fftx",
    version=get_version("fftx/__init__.py"),
    license="BSD-3-Clause",
    description="A Python front end to access the high performance capabilities of the FFTX Project",
    long_description="This Python package provides NumPy/CuPy-compatible access to the high performance multi-platform code generation capabilities of the FFTX Project.  The package provides a single API for several FFTs, along with some convolution-like transforms, that run on either CPUs or GPUs (NVIDIA and AMD) and supports single and double precision and both C (row-major) and Fortran (column-major) arrays.  The API uses the dimensions, datatype, ordering, and location of an array to determine which variant of a transform to invoke, simplifying application code intended for multiple target environments.",
    url="https://github.com/spiral-software/python-package-fftx",
    project_urls={
        "Source Code": "https://github.com/spiral-software/python-package-fftx",
    },
    author="SpiralGen Inc.",
    author_email="Patrick.Broderick@spiralgen.com",
    python_requires=">=3.7",
    packages=find_packages(),
    include_package_data=True,
)
