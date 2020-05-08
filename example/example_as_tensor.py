# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   example_as_tensor.py
 
@Time    :   2020/5/6 4:12 下午
 
@Desc    :
 
"""

import tensorflow as tf
import char_featurizer

data = '/home/xsq/nlp_code/char_featurizer/data/data.txt'
data2 = '明天去你家玩'

feature = char_featurizer.featurize_as_tensor(data2)

with tf.Session() as sess:
    sess.run(tf.compat.v1.initializers.tables_initializer())
    for _ in range(1):
        print('+' * 20)
        data = sess.run(feature)
        print(data)