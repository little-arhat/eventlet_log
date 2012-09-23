#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import eventlet_log

setup(
    name='eventlet_log',
    version=eventlet_log.__version__,
    description='''Damn simple logging wrapper compatible with eventlet.''',
    long_description=open('README.rst').read(),
    author=eventlet_log.__author__,
    author_email='sokolov.r.v@gmail.com',
    url='https://github.com/little-arhat/eventlet_log',
    packages=[
        'eventlet_log'
    ],
    install_requires=['eventlet'],
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
