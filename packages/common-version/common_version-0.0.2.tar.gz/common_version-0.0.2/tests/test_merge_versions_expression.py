# -*- coding: UTF-8 -*-
"""
@Project:lj_spider_core
@File:test_merge_versions_expression.py
@IDE: PyCharm
@Author : hsc
@Date:2022/8/22 15:45
@function：
"""
from version import merge_version_expression

v1 = ["[2.2,2.2.27)||[3.2,3.2.13)||[4.0,4.0.2)", "[2.2,2.2.28)||[3.2,3.2.12)||[4.0,4.0.4)"]

v2 = ["[2.2.27,3)||[3.2.13,4)||[4.0.2,)", "[2.2.28,3)||[3.2.12,4)||[4.0.4,)"]

s = ['[,1.8.10)', 'sgc-pre-batch||0.0.1', 'sgc-pre-batch||0.0.2', ]


def test_merge_version_expression():
    assert "[2.2,2.2.28)||[3.2,3.2.13)||[4.0,4.0.4)" == merge_version_expression(v1, is_or=True).get_value()
    assert "[2.2.28,3)||[3.2.13,4)||[4.0.4,)" == merge_version_expression(v2, is_or=False).get_value()
    assert "sgc-pre-batch||[,1.8.10)" == merge_version_expression(s, is_or=True).get_value()
