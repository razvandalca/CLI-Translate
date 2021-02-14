#!/usr/bin/env python
from setuptools import setup

setup(
    entry_points={
        'console_scripts': ['gtranslate=gtranslate.app:main'],
        'gtranslate.cli': [
            'translate=gtranslate.translate:Translate',
        ]

    }
)
