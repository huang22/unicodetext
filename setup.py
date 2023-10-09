#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Author  huang22
Date    ：2023/10/8 15:36
"""
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="unicodetext",
        version="1.2",
        author="huang22",
        include_package_data=True,
        license='MIT',
        description="Processing unicode text",
        packages=find_packages(),
    )
