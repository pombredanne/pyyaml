#!/bin/env python

import os.path
import setuptools


ROOT = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(ROOT, "README.rst")) as fp:
    long_description = fp.read()


setuptools.setup(
    name="yaml",
    version="4.0.dev0",
    description="YAML parser and emitter for Python",
    long_description=long_description,
    license="MIT",
    url="https://github.com/dstufft/yaml",
    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",

        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],

    package_dir={"": "src"},
    packages=["yaml"],
)
