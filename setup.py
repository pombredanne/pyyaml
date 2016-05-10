#!/bin/env python

import sys
import setuptools


setuptools.setup(
    name="PyYAML",
    version="3.10",
    description="YAML parser and emitter for Python",
    long_description="""\
YAML is a data serialization format designed for human readability
and interaction with scripting languages.  PyYAML is a YAML parser
and emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.""",
    author="Kirill Simonov",
    author_email="xi@resolvent.net",
    license="MIT",
    url="http://pyyaml.org/wiki/PyYAML",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],

    package_dir={"": {2: "lib", 3: "lib3"}[sys.version_info[0]]},
    packages=["yaml"],
)
