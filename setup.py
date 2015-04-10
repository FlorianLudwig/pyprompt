# -*- coding: utf-8 -*-
import os
from setuptools import setup


setup(
    name="pyprompt",
    version="0.0.1",
    packages=['pyprompt'],
    install_requires=['GitPython==1.0.0'],
    entry_points={
        'console_scripts': [
            'pyprompt = pyprompt.cli:main'
        ],
    }
)
