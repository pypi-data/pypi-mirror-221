# -*- coding: utf-8 -*-
from abc import ABC

from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.version_base import Item


class VersionGoExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        # version_expression = chinese_to_english_version(version_expression)
        if version_expression:
            version_item = Item(left_open=True, right_open=True, left=version_expression, right=version_expression)
        else:
            version_item = Item(left_open=True, right_open=True, left="", right="")
        return version_item
