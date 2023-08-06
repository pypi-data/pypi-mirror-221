# -*- coding: utf-8 -*-
from abc import ABC

from lj_spider_core.version.exceptions import VersionDestError
from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import (
    arrangement_version,
    find_left_or_right_identifier,
    handle_version_comma, get_equal_item, cut_left_and_right_dest, handle_version_change_source,
    chinese_to_english_version, handle_version_compatible,
)
from lj_spider_core.version.version_base import Item, ItemGroup
from lj_spider_core.version.version_base.base_version import Version


class VersionNugetExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        if version_expression and version_expression != "-1":
            version_item = self.handle_nuget_compare(version_expression, package_type)
        else:
            version_expression = version_expression.replace(" ", "")
            if version_expression != "-1":
                raise VersionDestError(version_expression + "version_expression格式无效")
            else:
                version_item = Item(
                    left_open=True, left="", right_open=True, right=""
                )
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_nuget_compare(self, version_expression, package_type):
        if (
                "[" in version_expression or "]" in version_expression or
                "(" in version_expression or ")" in version_expression) \
                and "," in version_expression:
            version_item = handle_version_comma(version_expression, package_type)
        elif (
                ("," not in version_expression)
                and ("[" in version_expression or "(" in version_expression)
                and ("]" in version_expression or ")" in version_expression)
        ):
            version_dest = version_expression.replace(" ", "")
            if ">" in version_dest or "<" in version_expression:
                if "," in version_expression:
                    version_dest_list = version_expression.split(",")
                    version_item = cut_left_and_right_dest(version_dest_list, package_type)
                else:
                    version_item = handle_version_change_source(version_expression, package_type)
            else:
                new_version_dest = version_dest[1:-1]
                format_version_dest = arrangement_version(
                    new_version_dest, package_type
                )
                left_open, _ = find_left_or_right_identifier(version_dest[0])
                _, right_open = find_left_or_right_identifier(version_dest[-1])
                if isinstance(format_version_dest, Version):
                    if format_version_dest.new_version:
                        format_version = format_version_dest.new_version
                    else:
                        format_version = format_version_dest.old_version
                else:
                    format_version = format_version_dest
                version_item = Item(
                    left_open=left_open,
                    left=format_version,
                    right_open=right_open,
                    right=format_version,
                )
        elif ">" in version_expression or "<" in version_expression:
            if "," in version_expression:
                version_dest_list = version_expression.split(",")
                version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                version_item = handle_version_change_source(version_expression, package_type)
        elif "*" in version_expression and version_expression.replace("*", ""):
            version_item = handle_version_compatible(version_expression, package_type)
        else:
            version_expression = version_expression.replace(" ", "")
            if not version_expression.replace("*", ""):
                version_item = Item(left_open=True, left="", right_open=True, right="")
            else:
                version_item = get_equal_item(version_expression, package_type)
        return version_item
