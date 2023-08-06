from setuptools import setup

name = "types-Send2Trash"
description = "Typing stubs for Send2Trash"
long_description = '''
## Typing stubs for Send2Trash

This is a PEP 561 type stub package for the `Send2Trash` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`Send2Trash`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/Send2Trash. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `38dc97ba717c55c4c833f04c4bc9665f0a44fe7a` and was tested
with mypy 1.4.1, pyright 1.1.318, and
pytype 2023.7.21.
'''.lstrip()

setup(name=name,
      version="1.8.2.7",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/Send2Trash.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['send2trash-stubs'],
      package_data={'send2trash-stubs': ['__init__.pyi', '__main__.pyi', 'exceptions.pyi', 'util.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
