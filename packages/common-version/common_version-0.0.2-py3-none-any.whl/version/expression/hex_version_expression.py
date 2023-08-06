# -*- coding: utf-8 -*-
from abc import ABC

from version.expression.base import VersionExpression
from version.expression.base_method import (
    handle_version_compatible,
    chinese_to_english_version, handle_version_or,
)
from version.version_base import Item, ItemGroup


class VersionHexExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):

        version_expression = chinese_to_english_version(version_expression)
        version_item = Item(valid=False)
        if "and" in version_expression or "or" in version_expression:
            # todo 暂时未考虑一个表达式中既有and又有or的情况
            if "and" in version_expression:
                version_dest_list = version_expression.split("and")
                items = []
                for version in version_dest_list:
                    part_version_item = self.handle_hex_compare(version, package_type)
                    items.append(part_version_item)
                version_item = ItemGroup(*items, is_or=False)
            elif "or" in version_expression:
                version_dest_list = version_expression.split("or")
                items = []
                for version in version_dest_list:
                    part_version_item = self.handle_hex_compare(version, package_type)
                    items.append(part_version_item)
                version_item = ItemGroup(*items, is_or=True)
        else:
            version_item = self.handle_hex_compare(version_expression, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_hex_compare(self, version_dest, package_type):

        version_dest = version_dest.replace(" ", "")
        if "~>" in version_dest:
            version_item = handle_version_compatible(version_dest, package_type)
        elif ">" in version_dest or "<" in version_dest:
            version_item = handle_version_or(version_dest, package_type)
        else:
            version_dest = version_dest.replace(" ", "")
            if version_dest and "*" != version_dest:
                version_item = Item(left_open=True, left=version_dest, right_open=True, right=version_dest)
            else:
                version_item = Item(left_open=True, right_open=True, left="", right="")
        return version_item
