YAML
====

.. image:: https://img.shields.io/pypi/v/yaml.svg
    :target: https://pypi.python.org/pypi/yaml/
    :alt: Latest Version

.. image:: https://travis-ci.org/dstufft/yaml.svg?branch=master
    :target: https://travis-ci.org/dstufft/yaml


``yaml`` is a Python package which parses and emits YAML 1.1. It supports
Python 2.6-2.7, Python 3.3+, PyPy and PyPy3.

.. code-block:: pycon

    >>> import yaml
    >>> yaml.loads("""
    ...     mydict:
    ...         - 1
    ...         - 2
    ...         - 3
    ...     """)
    {'mydict': [1, 2, 3]}


Discussion
~~~~~~~~~~

If you run into bugs, you can file them in our `issue tracker`_.


.. _`issue tracker`: https://github.com/dstufft/yaml/issues
