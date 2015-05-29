#!/usr/bin/env python

import os
from setuptools import setup, find_packages

data_patterns = [
    'templates/**.html',
    'static/**.html',
    'static/**.jpg',
    'static/**.css',
    'static/**.js',
    'static/**.txt',
]

setup(
    name='relengapi-clobberer',
    version='0.5.2',
    description='The RelengAPI clobberer service.',
    author='Morgan Phillips',
    author_email='mphillips@mozilla.com',
    url='https://github.com/mozilla/build-relengapi-clobberer',
    entry_points={
        "relengapi.blueprints": [
            'clobberer = relengapi.blueprints.clobberer:bp',
        ],
        "relengapi.metadata": [
            'relengapi-clobberer = relengapi.blueprints.clobberer:metadata',
        ],
    },
    packages=find_packages(),
    namespace_packages=['relengapi', 'relengapi.blueprints'],
    data_files=[
        ('relengapi-' + dirpath, [os.path.join(dirpath, f) for f in files])
        for dirpath, _, files in os.walk('docs')
        # don't include directories not containing any files, as they will be
        # included in installed-filestxt, and deleted (rm -rf) on uninstall;
        # see https://bugzilla.mozilla.org/show_bug.cgi?id=1088676
        if files
    ],
    package_data={  # NOTE: these files must *also* be specified in MANIFEST.in
        'relengapi.blueprints.clobberer': data_patterns,
    },
    install_requires=[
        'Flask',
        'relengapi>=1.0.0',
    ],
    license='MPL2',
    extras_require={
        'test': [
            'nose',
            'mock',
            'pep8',
            'pyflakes',
            'coverage',
        ]
    })
