# -*- coding: utf-8 -*-
from abc import ABC

from version.expression.base import VersionExpression
from version.expression.base_method import get_equal_item, chinese_to_english_version, handle_version_or
from version.version_base import Item, ItemGroup


class VersionCargoExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):
        """
        将表达式改变为通用版本表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        if ',' in version_expression:
            versions = version_expression.split(",")
            items = []
            for version in versions:
                part_version_item = self.handle_cargo_compare(version, package_type)
                items.append(part_version_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_cargo_compare(version_expression, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_cargo_compare(self, version_expression, package_type):
        from version.expression import (
            handle_version_compatible,
        )
        if "~" in version_expression:
            version_item = handle_version_compatible(version_expression, package_type)
        elif "*" in version_expression:
            if "*" != version_expression.replace(" ", ""):
                version_item = handle_version_compatible(
                    version_expression, package_type
                )
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        elif "^" in version_expression:
            version_item = handle_version_compatible(version_expression, package_type)
        elif ">" in version_expression or "<" in version_expression:
            version_item = handle_version_or(version_expression, package_type)
        elif version_expression and "=" not in version_expression:
            version_item = handle_version_compatible(version_expression, package_type)
        elif version_expression and "=" in version_expression:
            version_item = get_equal_item(version_expression, package_type)
        else:
            version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
