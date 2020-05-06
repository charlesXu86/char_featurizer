# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   chaizi.py
 
@Time    :   2020/4/29 10:58 上午
 
@Desc    :
 
"""

from char_featurizer.chaizi import HanziChaizi


class ChaiZi(object):
    def __init__(self, params=None):
        self.params = params if params else {}
        self.hc = HanziChaizi()

    def extract(self, char_seq):
        result = [self.hc.query(i) for i in char_seq]
        return result


if __name__ == "__main__":
    obj = ChaiZi()
    result = obj.extract('明天去你家玩儿')

    print(result)
