from setuptools import setup

name = "types-uWSGI"
description = "Typing stubs for uWSGI"
long_description = '''
## Typing stubs for uWSGI

This is a PEP 561 type stub package for the `uWSGI` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`uWSGI`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/uWSGI. All fixes for
types and metadata should be contributed there.

Type hints for uWSGI's [Python API](https://uwsgi-docs.readthedocs.io/en/latest/PythonModule.html). Note that this API is available only when running Python code inside a uWSGI process and some parts of the API are only present when corresponding configuration options have been enabled.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `21cb2cb546e1bd120091d6fe7087c847e0297d39` and was tested
with mypy 1.4.1, pyright 1.1.318, and
pytype 2023.7.21.
'''.lstrip()

setup(name=name,
      version="2.0.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/uWSGI.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['uwsgi-stubs', 'uwsgidecorators-stubs'],
      package_data={'uwsgi-stubs': ['__init__.pyi', 'METADATA.toml'], 'uwsgidecorators-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
