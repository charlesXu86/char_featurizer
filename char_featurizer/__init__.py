# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   __init__.py.py
 
@Time    :   2020/4/29 10:57 上午
 
@Desc    :
 
"""

import functools
import tensorflow as tf

from char_featurizer.featurizer.four_corner import FourCorner
from char_featurizer.featurizer.pinyin_parts import PinYinParts


class Featurizer(object):
    def __init__(self, featurizers=None):
        self.featurizers = featurizers if featurizers else [PinYinParts(), FourCorner()]

    def featurize(self, char_seq):
        featurize_result = []
        for featurizer in self.featurizers:
            featurize_result.extend(featurizer.extract(char_seq))

        return tuple(featurize_result)

    def get_vocabulary(self):
        featurize_vocabulary = []
        for featurizer in self.featurizers:
            featurize_vocabulary.extend(featurizer.get_vocabulary())

        return featurize_vocabulary

    def get_data_type(self):
        featurize_vocabulary = []
        for featurizer in self.featurizers:
            data_type = featurizer.get_data_type()
            featurize_vocabulary.extend(data_type)

        return tuple(featurize_vocabulary)

    def get_data_shape(self):
        featurize_vocabulary = []
        for featurizer in self.featurizers:
            data_shape = featurizer.get_data_shape()
            featurize_vocabulary.extend(data_shape)

        return tuple(featurize_vocabulary)


def featurize_as_tensor(data_file, featurizers=None):
    '''
    将字符特征转换为向量
    :param data_file:
    :param featurizers:
    :return:
    '''
    obj = Featurizer(featurizers)

    def gen(data_file):
        with open(data_file, 'rt') as fd:
            for line in fd:
                res = obj.featurize(line.strip())
                yield res

    data_type = obj.get_data_type()
    data_shape = obj.get_data_shape()

    dataset = tf.data.Dataset.from_generator(
        functools.partial(gen, data_file=data_file),
        data_type,
        data_shape
    )

    featurize_result = dataset.make_one_shot_iterator().get_next()

    featurize_vocab = obj.get_vocabulary()

    def build_feature_column(key_, vocabulary_list):
        return tf.feature_column.indicator_column(
            tf.feature_column.categorical_column_with_vocabulary_list(
                key=key_,
                vocabulary_list=vocabulary_list)
        )

    feature_keys = ['feature_{}'.format(i) for i in range(len(featurize_result))]
    feature_columns = list(
        map(
            lambda x: build_feature_column(
                feature_keys[x],
                featurize_vocab[x]
            ),
            range(len(featurize_result))
        )
    )

    data = {feature_keys[i]: featurize_result[i] for i in range(len(featurize_result))}

    feature = tf.feature_column.input_layer(data, feature_columns)

    return feature

def featurize_as_tensor2(sentence, featurizers=None):
    '''
    将字符特征转换为向量
    :param data_file:
    :param featurizers:
    :return:
    '''
    obj = Featurizer(featurizers)

    def gen(sentence):
        res = obj.featurize(sentence.strip())
        yield res

    data_type = obj.get_data_type()
    data_shape = obj.get_data_shape()

    dataset = tf.data.Dataset.from_generator(
        functools.partial(gen, data_file=sentence),
        data_type,
        data_shape
    )

    featurize_result = dataset.make_one_shot_iterator().get_next()

    featurize_vocab = obj.get_vocabulary()

    def build_feature_column(key_, vocabulary_list):
        return tf.feature_column.indicator_column(
            tf.feature_column.categorical_column_with_vocabulary_list(
                key=key_,
                vocabulary_list=vocabulary_list)
        )

    feature_keys = ['feature_{}'.format(i) for i in range(len(featurize_result))]
    feature_columns = list(
        map(
            lambda x: build_feature_column(
                feature_keys[x],
                featurize_vocab[x]
            ),
            range(len(featurize_result))
        )
    )

    data = {feature_keys[i]: featurize_result[i] for i in range(len(featurize_result))}

    feature = tf.feature_column.input_layer(data, feature_columns)

    return feature


if __name__ == "__main__":
    pass