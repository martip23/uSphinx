"""
uSphinx
=======

a rewrite of the Python Spinx tool. Documents are
stored in a git style  file system. Extensions
include literate programming tools.

"""

# -*- coding: utf-8 -*-

readme = open('README.rst').read()
import usphinx.__about__ as about

from setuptools import setup, find_packages

requires = ['Sphinx>=1.3']

setup(
    name=about.__title__,
    version=about.__version__,
    url=about.__url__,
    license=about.__license__,
    author=about.__author__,
    author_email=about.__email__,
    description=about.__summary__,
    long_description=readme,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
)
