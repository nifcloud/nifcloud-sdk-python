#!/usr/bin/env python
import codecs
import os.path
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as f:
        content = f.read()
    return content


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='nifcloud',
    version=find_version('nifcloud', '__init__.py'),
    description='Data-driven NIFCLOUD SDK for Python',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='FUJITSU CLOUD TECHNOLOGIES',
    url='https://github.com/nifcloud/nifcloud-sdk-python',
    packages=find_packages(exclude=['tests*']),
    package_data={'nifcloud': ['data/*.json',
                               'data/*/*/*.json']},
    include_package_data=True,
    install_requires=['botocore==1.31.1'],
    license='Apache License 2.0',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ),
)
