# MODFLOW developer tools

[![GitHub tag](https://img.shields.io/github/tag/MODFLOW-USGS/modflow-devtools.svg)](https://github.com/MODFLOW-USGS/modflow-devtools/tags/latest)
[![PyPI Version](https://img.shields.io/pypi/v/modflow-devtools.png)](https://pypi.python.org/pypi/modflow-devtools)
[![PyPI Versions](https://img.shields.io/pypi/pyversions/modflow-devtools.png)](https://pypi.python.org/pypi/modflow-devtools)
[![PyPI Status](https://img.shields.io/pypi/status/modflow-devtools.png)](https://pypi.python.org/pypi/modflow-devtools)
[![CI](https://github.com/MODFLOW-USGS/modflow-devtools/actions/workflows/ci.yml/badge.svg)](https://github.com/MODFLOW-USGS/modflow-devtools/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/modflow-devtools/badge/?version=latest)](https://modflow-devtools.readthedocs.io/en/latest/?badge=latest)

Python tools for MODFLOW development and testing.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Use cases](#use-cases)
- [Quickstart](#quickstart)
- [Documentation](#documentation)
- [MODFLOW Resources](#modflow-resources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Requirements

This project requires Python3.8+. Its only core dependencies are `numpy` and `pytest`.

## Installation

`modflow-devtools` is available on PyPI and can be installed with pip:

```shell
pip install modflow-devtools
```

This package pairs well with a few pytest plugins:

- `pytest-cases`
- `pytest-dotenv`
- `pytest-xdist`

These and a few other optional dependencies can be installed with:

```shell
pip install "modflow-devtools[test]"
```

To install from source and set up a development environment please see the [developer documentation](DEVELOPER.md).

## Use cases

This package contains shared tools for developing and testing MODFLOW 6 and FloPy, including standalone utilities as well as `pytest` fixtures, CLI options, and test cases:

- utilities for retrieving release information and downloading assets from the GitHub API
- a `ZipFile` subclass that [preserves file permissions](https://stackoverflow.com/questions/39296101/python-zipfile-removes-execute-permissions-from-binaries) (workaround for [Python #15795](https://bugs.python.org/issue15795))
- a `pytest` CLI option for smoke testing (running a fast subset of cases)
- a minimal `pytest-cases` framework for reusing test functions and data
- a set of keepable `pytest` temporary directory fixtures for each scope
- a set of fixtures to parametrize tests with models from external repos
  - `MODFLOW-USGS/modflow6-examples`
  - `MODFLOW-USGS/modflow6-testmodels`
  - `MODFLOW-USGS/modflow6-largetestmodels`
- a set of `pytest` markers to conditionally skip test cases based on
  - operating system
  - Python packages installed
  - executables available on the path

## Quickstart

To import `pytest` fixtures in a project consuming `modflow-devtools`, add the following to a `conftest.py` file:

```python
pytest_plugins = [ "modflow_devtools.fixtures" ]
```

**Note**: `pytest` requires this to be a top-level `conftest.py` file. Nested `conftest.py` files may override or extend this package's fixtures.

## Documentation

Usage documentation is available at [modflow-devtools.readthedocs.io](https://modflow-devtools.readthedocs.io/en/latest/).

## MODFLOW Resources

+ [MODFLOW and Related Programs](https://water.usgs.gov/ogw/modflow/)
+ [Online guide for MODFLOW-2000](https://water.usgs.gov/nrp/gwsoftware/modflow2000/Guide/)
+ [Online guide for MODFLOW-2005](https://water.usgs.gov/ogw/modflow/MODFLOW-2005-Guide/)
+ [Online guide for MODFLOW-NWT](https://water.usgs.gov/ogw/modflow-nwt/MODFLOW-NWT-Guide/)
