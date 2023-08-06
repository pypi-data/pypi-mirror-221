# -*- coding: utf-8 -*-
import re
from abc import ABC

from lj_spider_core.version.exceptions import VersionDestError
from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import (
    arrangement_version,
    # find_str_index,
    handle_version_comma,
    handle_version_compatible,
    handle_version_or,
    chinese_to_english_version,
    # fun
)
from lj_spider_core.version.version_base import Item, ItemGroup


class VersionNpmExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param pacage_type: 组件类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        version_dest = re.sub(r"[,<>=&|\^~]+ *", lambda matched: self.func(matched), version_expression)
        # version_dest = re.sub(r'([><=\^~][><=\^~]* *\d)', lambda matched: fun(matched), version_expression)
        # version_dest = find_str_index(version_expression, " ")
        if "||" in version_dest or "|" in version_dest:
            version_dest_list = []
            if "||" in version_dest:
                version_dest_list = version_dest.split("||")
            if "|" in version_dest and "||" not in version_dest:
                version_dest_list = version_dest.split("|")
            items = []
            for version in version_dest_list:
                version_item = self.handle_npm_compare(version, package_type)
                items.append(version_item)
            version_item = ItemGroup(*items, is_or=True)
        elif " " in version_dest and " - " not in version_dest:
            version_dest_list = version_dest.split(" ")
            items = []
            for version in version_dest_list:
                if version:
                    version_item = self.handle_npm_compare(version, package_type)
                    items.append(version_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_npm_compare(version_dest, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_npm_compare(self, version_dest, package_type):
        from lj_spider_core.version.version_base import Version
        if version_dest:
            if version_dest[0] == " ":
                version_dest = version_dest[1:]
            if version_dest[-1] == " ":
                version_dest = version_dest[0:-1]
        if "~" in version_dest or (".x" in version_dest and "/" not in version_dest):
            if "-" in version_dest:
                version_dest = version_dest.split("-")[0]
            if version_dest.replace("~", ""):
                version_item = handle_version_compatible(version_dest, package_type)
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        elif "^" in version_dest:
            version_dest = version_dest.replace(" ", "")
            version_dest = version_dest.replace("@", "")
            version_dest = version_dest.replace("^", "")
            version_dest = version_dest.replace("x", "0")
            version_dest = version_dest.replace("X", "0")
            version_dest = version_dest.replace("*", "0")
            if "-" in version_dest:
                version_dest = version_dest.split("-")[0]
            format_version_dest_obj = arrangement_version(version_dest, package_type)
            if isinstance(format_version_dest_obj, Version):
                if format_version_dest_obj.new_version:
                    format_version = format_version_dest_obj.new_version
                else:
                    raise VersionDestError(format_version_dest_obj.old_version + "格式化失败")
            else:
                format_version = version_dest
            if '.' in format_version:
                versions = format_version.split('.')
                new_version = versions[0] + '.0'
            else:
                new_version = format_version + '.0'
            max_version = Version.max_version_calculation(new_version)
            version_item = Item(
                left_open=True, left=format_version, right_open=False, right=max_version
            )
        elif " -" in version_dest:
            format_left_version_dest = arrangement_version(
                version_dest.split(" - ")[0], package_type
            )
            format_right_version_dest = arrangement_version(
                version_dest.split(" - ")[1], package_type
            )
            if isinstance(format_left_version_dest, Version):
                if format_left_version_dest.new_version:
                    left_version = format_left_version_dest.new_version
                else:
                    raise VersionDestError(format_left_version_dest.old_version + "格式化失败")
            else:
                left_version = format_left_version_dest
            if isinstance(format_right_version_dest, Version):
                if format_right_version_dest.new_version:
                    right_version = format_right_version_dest.new_version
                else:
                    raise VersionDestError(format_right_version_dest.old_version + "格式化失败")
            else:
                right_version = format_right_version_dest
            version_item = Item(
                left_open=True,
                left=left_version,
                right_open=True,
                right=right_version,
            )
        elif (">" in version_dest or "<" in version_dest) and " " not in version_dest:
            version_item = handle_version_or(version_dest, package_type)
        elif (">" in version_dest or "<" in version_dest) and " " in version_dest:
            version_item = handle_version_comma(version_dest, package_type)
        else:
            version_dest = version_dest.replace(" ", "")
            if version_dest and "*" != version_dest:
                version_item = Item(left_open=True, left=version_dest, right_open=True, right=version_dest)
                # version_item = get_equal_item(version_expression, package_type)
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
