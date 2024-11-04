# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2024/11/4 上午9:48
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""

VERSION = '1.0.0'
from setuptools import setup, find_packages

setup(
    name='yck',
    version=VERSION,
    py_modules=['yck'],
    install_requires=['clickhouse-driver', 'pandas', 'polars'],

    author='ZhangYundi',
    author_email='yundi.xxii@outlook.com',
    packages=find_packages(include=['yck', 'yck.*']),
    description='Query clickhouse cluster and return pandas dataframe or polars dataframe',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/link-yundi/yck',

    scripts=[],
    package_data={},
)