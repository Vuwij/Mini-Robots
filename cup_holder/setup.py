# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='cup_holder',
    version='0.1.0',
    description='Cup holding robot',
    long_description=readme,
    author='Jason Wang',
    author_email='vuwij@me.com',
    url='https://github.com/Vuwij/Robotics-Algorithms/cup_holder/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)