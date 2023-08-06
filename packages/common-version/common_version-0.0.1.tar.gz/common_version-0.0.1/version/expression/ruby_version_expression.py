# -*- coding: utf-8 -*-
from abc import ABC

from lj_spider_core.version.exceptions import VersionDestError
from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import (
    arrangement_version,
    handle_version_compatible,
    # get_equal_item,
    chinese_to_english_version, handle_version_or,
)
from lj_spider_core.version.version_base import Item, ItemGroup


class VersionRubyExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):

        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        version_expression = version_expression.replace(" ", "")
        if "," in version_expression:
            versions = version_expression.split(",")
            items = []
            for version in versions:
                part_version_item = self.handle_ruby_compare(version, package_type)
                items.append(part_version_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_ruby_compare(version_expression, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_ruby_compare(self, version_expression, package_type):
        if (
                ">" in version_expression or "<" in version_expression
        ) and "~" not in version_expression:
            version_item = handle_version_or(
                version_expression, package_type
            )
        elif "~>" in version_expression:
            version_item = handle_version_compatible(version_expression, package_type)
        elif "!=" in version_expression:
            version_item = self.handle_ruby_matching(version_expression, package_type)
        else:
            version_expression = version_expression.replace(" ", "")
            version_expression = version_expression.replace("=", "")
            if version_expression and "*" != version_expression:
                version_item = Item(left_open=True, left=version_expression, right_open=True, right=version_expression)
            else:
                version_item = Item(left_open=True, right_open=True, left="", right="")
        return version_item

    def handle_ruby_matching(self, version_dest, package_type):
        from lj_spider_core.version.version_base import Version
        """
         != 逻辑   例如  !=1.1.1   --->   [,1.1.1)||(1.1.1,]
        :param version_dest:
        :return:
        """
        format_version_dest = arrangement_version(
            version_dest, package_type, is_del_identifier=True
        )
        if isinstance(format_version_dest, Version):
            if format_version_dest.new_version:
                format_version = format_version_dest.new_version
            else:
                raise VersionDestError(format_version_dest.old_version + "version_expression格式化失败")
        else:
            format_version = format_version_dest
        left_item = Item(
            left_open=True, right_open=False, left="", right=format_version
        )
        right_item = Item(
            left_open=False, right_open=True, left=format_version, right=""
        )
        group = ItemGroup(left_item, right_item, is_or=True)
        return group
