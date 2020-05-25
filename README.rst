char_featurizer
==========================

**char_featurizer** 是一个汉字字符特征提取工具，他可以提取汉字的字音（包括声母、韵母、声调）、字形（偏旁、部首）、四角符号等信息。
同时可以将这些特征信息转换为tensor，作为模型的输入特征。这个项目是在安德森大佬的 `字符提取工具 <https://github.com/howl-anderson/hanzi_char_featurizer>`_ 的基础上做了优化整合

目前 **char_featurizer** 支持的功能有：

    1、字形特征提取

    2、字音特征提取

    3、四角编码提取

    4、tensor转换


二、安装使用
============

1、安装
>>>>>>>>>>>>>>>>>>

.. code:: python

    pip install char_featurizer

2、使用
>>>>>>>>>>>>>>>>>>>

1、字符特征提取

.. code:: python

    from char_featurizer import Featurizer

    featurizer = Featurizer()

    data = '明天去你家玩'

    result = featurizer.featurize(data)
    print(result)

2、作为特征输入模型

3、相关资源
>>>>>>>>>>>>>>>>>>>>>>

1、`汉字四角号码在线查询工具 <https://sijiao.911cha.com>`_



三、Update News
======================

    * 2020.5.4  完成V1版本

四、TO DO LIST
======================

    1、字符相似度计算（发音相似度、字形相似度）

    2、支持tf2


五、Resources
======================
