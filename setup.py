#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import join, dirname
import Encryptors.Caesar

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Encryptors',
    version=Encryptors.__version__,
    packages=find_packages(),
    url='https://github.com/Dezodemius/Encryptors',
    license='GNU General Public License v3.0',
    author='Yehor Hladkov',
    author_email='gladkovyegor@gmail.com',
    description='Encryption/decryption modules.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    test_suite='tests',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
            "Natural Language :: English",
            "Natural Language :: Russian",
            "Intended Audience :: Education",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
