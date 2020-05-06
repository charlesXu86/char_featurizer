# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   set_up.py

@Time    :   2020-05-06 16:22

@Desc    :   setup

'''
from setuptools import find_packages, setup, convert_path
import pathlib


def _version():
    ns = {}
    with open(convert_path("char_featurizer/version.py"), "r") as fh:
        exec(fh.read(), ns)
    return ns['__version__']


__version = _version()

# Package meta-data.
NAME = 'char_featurizer'
DESCRIPTION = '中文字符特征提取工具，可以从中文汉字中提取出拼音、声调、拆分偏旁部首、四角编码，并且可以转化为tensor作为模型的输入。'
URL = 'https://github.com/charlesXu86/char_featurizer'
EMAIL = 'charlesxu86@163.com'
AUTHOR = 'xu'
LICENSE = 'MIT'

HERE = pathlib.Path(__file__).parent
with open("README.rst", "r") as fh:
    long_description = fh.read()

required = [ ]

setup(
    name=NAME,
    version=__version,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    package_data={'char_featurizer': ['resource/*.json', 'resource/*.txt', 'resource/*.pkl', '*.rst']},
    install_requires=required,
    license=LICENSE,
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: PyPy'], )
print("Welcome to char_featurizer, and char_featurizer version is {}".format(__version))
