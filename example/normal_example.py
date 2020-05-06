# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   normal_example.py
 
@Time    :   2020/5/6 3:58 下午
 
@Desc    :
 
"""

from char_featurizer import Featurizer

featurizer = Featurizer()

data = '明天去你家玩'

result = featurizer.featurize(data)
print(result)