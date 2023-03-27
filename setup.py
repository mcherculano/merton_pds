# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:32:21 2023

@author: colburm
"""

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='merton_pds',
    url=' ',
    author='Miguel C. Herculano',
    author_email='miguelcbherculano@gmail.com',
    # Needed to actually package something
    packages=['merton_pds'],
    # Needed for dependencies
    install_requires=['numpy','pandas','scipy.optimize','scipy.stats'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='library with a simple probability of default calculator',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)