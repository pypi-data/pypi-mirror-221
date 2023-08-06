# -*- coding: utf-8 -*-
import re
from abc import ABC

from version.exceptions import VersionDestError
from version.expression import handle_version_change_source
from version.expression.base import VersionExpression
from version.expression.base_method import (
    cut_left_and_right_dest,
    chinese_to_english_version, handle_version_compatible, arrangement_version,
)
from version.version_base import Item, ItemGroup


class VersionOtherExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):

        version_expression = chinese_to_english_version(version_expression)
        version_expression = re.sub(r"[,<>=&|\^~]+ *", lambda matched: self.func(matched), version_expression)
        # version_expression = re.sub(r'([><=\^~][><=\^~]* *\d)', lambda matched: fun(matched), version_expression)
        if "|" in version_expression:
            versions = version_expression.split("|")
            items = []
            for version in versions:
                part_item = self.handle_other_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        elif "," in version_expression and ('[' not in version_expression and "(" not in version_expression):
            versions = version_expression.split(",")
            items = []
            for version in versions:
                part_item = self.handle_other_compare(version, package_type)
                if isinstance(part_item, list):
                    items += part_item
                else:
                    items.append(part_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            if "*" == version_expression.replace(
                    " ", ""
            ) or not version_expression.replace(" ", ""):
                version_item = Item(left_open=True, right_open=True, left="", right="")
            else:
                version_item = self.handle_other_compare(
                    version_expression, package_type
                )
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_other_compare(self, version, package_type):
        from version.version_base import Version
        if "[" in version or "]" in version or "(" in version or ")" in version:
            version_dest_list = version.split(",")
            version_item = cut_left_and_right_dest(version_dest_list, package_type)
        elif "!=" in version:
            new_version_dest = arrangement_version(
                version, package_type, is_del_identifier=True
            )
            if isinstance(new_version_dest, Version):
                if new_version_dest.new_version:
                    format_version = new_version_dest.new_version
                else:
                    raise VersionDestError(new_version_dest.old_version + "version_expression格式化失败")
            else:
                format_version = new_version_dest
            left_item = Item(
                left_open=True, right_open=False, left="", right=format_version
            )
            right_item = Item(
                left_open=False, right_open=True, left=format_version, right=""
            )
            group = ItemGroup(left_item, right_item, is_or=True)
            return group
        elif ">" in version or "<" in version:
            if " " in version:
                version_dest_list = version.split(" ")
                if " " in version_dest_list:
                    version_dest_list.remove("")
                version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                version = version.replace(" ", "")
                version_item = handle_version_change_source(version, package_type)

        elif "~" in version or "^" in version or "*" in version:
            version_item = handle_version_compatible(version, package_type)
        else:
            if version.replace(" ", "") and version.replace(" ", "") != "*":
                version = version.replace(" ", "")
                version_item = Item(left_open=True, left=version, right_open=True, right=version)
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
