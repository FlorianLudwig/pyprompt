# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="pyprompt",
    version="0.0.1",
    packages=['pyprompt'],
    install_requires=['GitPython==1.0.0'],
    author='Florian Ludwig',
    author_email='vierzigundzwei@gmail.com',
    entry_points={
        'console_scripts': [
            'pyprompt = pyprompt.cli:main'
        ],
    },
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ]
)
