# -*- coding: utf-8 -*-
import re
from abc import ABC

from lj_spider_core.version.expression import handle_version_change_source
from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import (
    cut_left_and_right_dest, get_equal_item, chinese_to_english_version,
    # handle_version_compatible,
)
from lj_spider_core.version.version_base import Item, ItemGroup


class VersionLinuxExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        version_expression = re.sub(r"[,<>=&|\^~]+ *", lambda matched: self.func(matched), version_expression)
        if "||" in version_expression:
            versions = version_expression.split("||")
            items = []
            for version in versions:
                part_item = self.handle_linux_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        elif "&" in version_expression:
            versions = version_expression.split("&")
            items = []
            for version in versions:
                part_item = self.handle_linux_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            if "*" == version_expression.replace(
                    " ", ""
            ) or not version_expression.replace(" ", ""):
                version_item = Item(left_open=True, right_open=True, left="", right="")
            else:
                version_item = self.handle_linux_compare(
                    version_expression, package_type
                )
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_linux_compare(self, version, package_type):
        if "[" in version or "]" in version or "(" in version or ")" in version:
            version_dest_list = version.split(",")
            version_item = cut_left_and_right_dest(version_dest_list, package_type)
        elif ">" in version or "<" in version:
            version = version.replace(",", " ")
            if " " in version:
                version_dest_list = version.split(" ")
                if "" in version_dest_list:
                    version_dest_list.remove("")
                version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                version_item = handle_version_change_source(version, package_type)
        else:
            if version.replace(" ", "") and version.replace(" ", "") != "*":
                version_item = get_equal_item(version, package_type)
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
