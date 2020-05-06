# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   parse.py
 
@Time    :   2020/5/6 11:22 上午
 
@Desc    :
 
"""

import pickle
import pathlib
import os

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)

data = {}

for i in [basedir + '/resource/chaizi-ft.txt', basedir + '/resource/chaizi-jt.txt']:
    with open(i, 'rt') as fd:
        for line in fd:
            item_list = line.strip().split('\t')
            key = item_list[0]
            value = [i.strip().split() for i in item_list[1:]]

            data[key] = value

output_file = basedir + '/resource/data_chaizi.pkl'

with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)
