"""
@Description: 
@Usage: 
@Author: liuxianglong
@Date: 2021/8/21 下午6:44
"""
# !/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='cs_sender',
    version='V1.5.1',
    description=(
        'scrapy extension for spider monitor web framework cralwer-studio'
    ),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='liuxianglong',
    author_email='liu_xianglong@live.com',
    maintainer='liuxianglong',
    maintainer_email='liu_xianglong@live.com',
    license='BSD License',
    packages=['cs_sender'],
    py_modules=["cs_sender.__init__"],
    platforms=["all"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'scrapy', 'requests'
    ]
)