# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   __init__.py.py
 
@Time    :   2020/5/6 2:29 下午
 
@Desc    :
 
"""
import pickle
import os
import pathlib

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)


class FourCornerMethod(object):
    def __init__(self):
        data_file = basedir + '/resource/data_four_corner.pkl'

        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char, default=None):
        return self.data.get(input_char, default)


if __name__ == "__main__":
    fcm = FourCornerMethod()
    result = fcm.query('名')

    print(result)
