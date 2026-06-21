#!/usr/bin/env python3
"""Compatibility shim for legacy editable installs.

Project metadata lives in pyproject.toml. Prefer `uv sync` or
`python -m pip install -e .[dev]` for local development.
"""

from setuptools import setup

setup()
