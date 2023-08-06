"""
 * Copyright of this product 2013-2023,
 * Machbase Corporation(or Inc.) or its subsidiaries.
 * All Rights reserved.
"""
#coding=utf8

import os, re, shutil, zipfile, platform, sys
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

setup(
    name='testmhdbAPI',
    version='1.5',
    description='Machbase-Python3-API',
    long_description='Python3 module for Machbase',
    url='http://www.machbase.com',
    author='machbase',
    author_email='support@machbase.com',
    platforms='LINUX',
    packages=find_packages(),
    package_data={"machbaseAPI":['*.so']}
)

args = sys.argv
p = platform.system()

if p == 'Windows' and args[1] == 'install':
    os.chdir(get_python_lib())
    dirs = os.listdir()
    for file in dirs:
        if re.match('^(machbaseAPI-)[a-z0-9A-Z-.]+.egg$', file):
            newName = file.replace('.egg', '.zip')
            os.rename(file, newName)
            with zipfile.ZipFile(newName) as target_zip:
                target_zip.extractall(get_python_lib())
            if os.path.exists('EGG-INFO'):
                shutil.rmtree('EGG-INFO')
            os.remove(newName)
            break
    print('machbaseAPI setting complete.')