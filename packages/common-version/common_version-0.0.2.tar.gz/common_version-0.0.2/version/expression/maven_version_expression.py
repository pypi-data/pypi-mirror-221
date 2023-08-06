# -*- coding: utf-8 -*-
from abc import ABC

from version.expression.base import VersionExpression
from version.expression.base_method import (
    cut_left_and_right_dest,
    get_equal_item,
    chinese_to_english_version,
)
from version.version_base import Item, ItemGroup


class VersionMavenExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):
        version_expression = chinese_to_english_version(version_expression)
        version_expression = version_expression.replace(" ", "")
        version_expression = version_expression.replace(")(", ")&(")
        version_expression = version_expression.replace("][", "]&[")
        version_expression = version_expression.replace("](", "]&(")
        version_expression = version_expression.replace(")[", ")&[")
        version_expression = version_expression.replace("),[", ")||[")
        version_expression = version_expression.replace("),(", ")||(")
        version_expression = version_expression.replace("],[", "]||[")
        version_expression = version_expression.replace("],(", "]||(")
        if "&" in version_expression:
            versions = version_expression.split("&")
            items = []
            for version in versions:
                part_item = self.handle_maven_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=False)
        elif "||" in version_expression:
            versions = version_expression.split("||")
            items = []
            for version in versions:
                part_item = self.handle_maven_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        else:
            version_item = self.handle_maven_compare(version_expression, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_maven_compare(self, version_expression, package_type):
        if version_expression:
            if "," in version_expression and (
                    "[" in version_expression
                    or "(" in version_expression
                    or "]" in version_expression
                    or ")" in version_expression
            ):
                version_dest_list = version_expression.split(",")
                version_item = cut_left_and_right_dest(version_dest_list, package_type)
            else:
                if "[" in version_expression:
                    version_dest = version_expression.replace(" ", "")
                    version_item = get_equal_item(version_dest[1:-1], package_type, is_del_brackets=True)
                elif version_expression:
                    version_item = get_equal_item(version_expression, package_type, is_del_brackets=True)
                else:
                    version_item = Item(
                        left_open=True, left="", right_open=True, right=""
                    )
        else:
            version_item = Item(
                left_open=True, left="", right_open=True, right=""
            )
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item
    #
    # def format_maven(self, version_dest, package_type):
    #     """
    #     版本格式化之后再拼接
    #     :param version_dest:
    #     :return:
    #     """
    #     cut_version_list = cut_version_with_comma(version_dest)
    #     new_item_group = ItemGroup()
    #     for cut_version in cut_version_list:
    #         new_cut_version = cut_version.replace(" ", "")
    #         new_left_cut_version = new_cut_version.split(",")
    #         new_item = cut_left_and_right_dest(new_left_cut_version, package_type)
    #         new_item_group = ItemGroup(new_item_group, new_item, is_or=True)
    #     return new_item_group
