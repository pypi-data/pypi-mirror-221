# -*- coding: utf-8 -*-
import re
from abc import ABC

from version.expression import handle_version_change_source
from version.expression.base import VersionExpression
from version.expression.base_method import (
    cut_left_and_right_dest, get_equal_item, chinese_to_english_version, handle_version_compatible, handle_version_or,
)
from version.version_base import Item, ItemGroup


class VersionSnykExpression(VersionExpression, ABC):

    def change_to_expression(self, package_type, version_expression):
        # version_expression = re.sub(r'([><=\^~][><=\^~]* +)', lambda matched: fun(matched), version_expression)
        version_expression = chinese_to_english_version(version_expression)
        version_expression = re.sub(r"[,<>=&|\^~]+ *", lambda matched: self.func(matched), version_expression)
        if "||" in version_expression:
            versions = version_expression.split("||")
            items = []
            for version in versions:
                part_item = self.handle_snyk_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        elif "&" in version_expression:
            versions = version_expression.split("&")
            items = []
            for version in versions:
                part_item = self.handle_snyk_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            if "*" == version_expression.replace(
                    " ", ""
            ) or not version_expression.replace(" ", ""):
                version_item = Item(left_open=True, right_open=True, left="", right="")
            else:
                version_item = self.handle_snyk_compare(
                    version_expression, package_type
                )
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_snyk_compare(self, version, package_type):
        if "[" in version or "]" in version or "(" in version or ")" in version:
            if "," in version:
                version_dest_list = version.split(",")
                version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                new_version = version.replace("[", '.')
                new_version = new_version.replace("(", '.')
                new_version = new_version.replace("]", '.')
                new_version = new_version.replace(")", '.')
                version_item = get_equal_item(new_version, package_type)
        elif ">" in version or "<" in version:
            version = version.replace(",", " ")
            if " " in version:
                version_dest_list = version.split(" ")
                if "" in version_dest_list:
                    version_dest_list.remove("")
                if len(version_dest_list) < 2:
                    version_item = handle_version_or(version, package_type)
                else:
                    version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                version_item = handle_version_change_source(version, package_type)
        elif "~" in version or "^" in version:
            version_item = handle_version_compatible(version, package_type)
        else:
            version = version.replace(" ", "")
            if version and version != "*" and version != "=*" and version != "-" and version != "=-":
                version_item = get_equal_item(version, package_type)
            else:
                if version == "=-" or version == '-':
                    version_item = Item(left_open=False, left="0", right_open=False, right="0")
                else:
                    version_item = Item(left_open=True, left="", right_open=True, right="")
        return version_item
