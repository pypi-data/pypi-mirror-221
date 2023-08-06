# -*- coding: utf-8 -*-
from abc import ABC

from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import get_equal_item, chinese_to_english_version
from lj_spider_core.version.version_base import ItemGroup, Item


class VersionNvdExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        if "||" in version_expression:
            version_expressions = version_expression.split("||")
            items = []
            for version in version_expressions:
                part_item = get_equal_item(version, package_type, is_del_brackets=True)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        else:
            version_dest = version_expression.replace(" ", "")
            if "=" in version_dest:
                version_item = get_equal_item(version_expression, package_type)
            else:
                if version_dest and "*" != version_dest:
                    version_item = Item(left_open=True, left=version_dest, right_open=True, right=version_dest)
                    # version_item = get_equal_item(version_expression, package_type)
                else:
                    version_item = Item(left_open=True, left="", right_open=True, right="")
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item
