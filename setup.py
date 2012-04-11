#!/usr/bin/python

__version__ = '1.0.1'

sdict = {
    'name' : 'dynamixel',
    'version' : __version__,
    'description' : "Dynamixel Servo Library",
    'url': 'http://github.com/iandanforth/pydynamixel',
    'download_url' : 'https://github.com/iandanforth/pydynamixel/downloads',
    'author' : 'Patrick Goebel',
    'author_email' : 'patrick@pirobot.org',
    'maintainer' : 'Ian Danforth',
    'maintainer_email' : 'iandanforth@gmail.com',
    'keywords' : ['dynamixel', 'robotis', 'ax-12'],
    'license' : 'GPL',
    'packages' : ['dynamixel'],
    'classifiers' : [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
