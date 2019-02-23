"""
    Grid-Strategy Package:

A package for organizing matplotlib plots.

"""

import setuptools


with open("README", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='grid-strategy',
    version='0.0.1',
    description='Python plot organizing package',
    license="MIT", # TODO: Update with current license
    long_description=long_description,
    author='Konstantinos Oikonomou, ',
    author_email='kons.oikonomou@gmail.com',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['matplotlib'],
)