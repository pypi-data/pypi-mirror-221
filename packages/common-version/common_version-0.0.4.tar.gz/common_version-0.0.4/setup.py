# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    entry_points={
        'console_scripts': [
            'lj_version = version.command.case:cli'
        ]
    }
)
