# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   __init__.py.py
 
@Time    :   2020/5/6 11:08 上午
 
@Desc    :
 
"""

import pickle
import os
import pathlib

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)


class HanziChaizi(object):
    def __init__(self):
        data_file = basedir + '/resource/data_chaizi.pkl'

        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char, default=None):
        result = self.data.get(input_char, default)
        return result[0]


if __name__ == "__main__":
    hc = HanziChaizi()
    result = hc.query('名')

    print(result)
