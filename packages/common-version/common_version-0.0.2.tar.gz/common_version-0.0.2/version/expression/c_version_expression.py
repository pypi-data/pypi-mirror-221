# -*- coding: utf-8 -*-
import re
from abc import ABC

from version.expression.base import VersionExpression
from version.expression.base_method import chinese_to_english_version, handle_version_or, \
    handle_version_compatible
from version.version_base import Item, ItemGroup


class VersionCExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):
        """
        将表达式改变为通用版本表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = version_expression.replace('[', "")
        version_expression = version_expression.replace(']', "")
        version_expression = chinese_to_english_version(version_expression)
        version_expression = re.sub(r"[,<>=&|\^~]+ *", lambda matched: self.func(matched), version_expression)
        if " " in version_expression:
            version_dest_list = version_expression.split(" ")
            items = []
            for version in version_dest_list:
                if version:
                    version_item = self.handle_conan_compare(version, package_type)
                    items.append(version_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_conan_compare(version_expression, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_conan_compare(self, version_expression, package_type):
        if ">" in version_expression or "<" in version_expression:
            version_item = handle_version_or(
                version_expression, package_type
            )
        elif "~=" in version_expression:
            version_item = handle_version_compatible(version_expression, package_type)
        else:
            version_expression = version_expression.replace(" ", "")
            if version_expression:
                version_item = Item(left_open=True, left=version_expression, right_open=True, right=version_expression)
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
