# -*- coding: utf-8 -*-
from abc import ABC

from version.exceptions import VersionDestError
from version.expression.base import VersionExpression
from version.expression.base_method import chinese_to_english_version
from version.version_base import Item, ItemGroup


class VersionComposerExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):
        from version.expression import find_str_index

        version_expression = chinese_to_english_version(version_expression)
        version_dest = find_str_index(version_expression, " ")
        version_dest = version_dest.replace("||", "|")
        if "|" in version_dest:
            version_dest_list = version_dest.split("|")
            items = []
            for version in version_dest_list:
                part_item = self.handle_composer_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=True)
        elif "," in version_dest or (" " in version_dest and " -" not in version_dest and " as" not in version_dest):
            if "," in version_dest:
                version_dest_list = version_dest.split(",")
            else:
                version_dest_list = version_dest.split(" ")
            items = []
            for version in version_dest_list:
                part_item = self.handle_composer_compare(version, package_type)
                items.append(part_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_composer_compare(version_dest, package_type)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_composer_compare(self, version_dest, package_type):
        from version.version_base import Version
        from version.expression import (
            arrangement_version,
            handle_version_compatible,
            handle_version_or,
        )
        version_dest = version_dest.lower()

        if " as" in version_dest:
            version_dest = version_dest.split(" as")[0]
            version_dest = version_dest.replace(" ", "")
            version_item = Item(left_open=True, left=version_dest, right_open=True, right=version_dest)
        elif "~" in version_dest:
            version_item = handle_version_compatible(version_dest, package_type)
        elif "^" in version_dest:
            version_item = handle_version_compatible(version_dest, package_type)
        elif ">" in version_dest or "<" in version_dest:
            version_item = handle_version_or(version_dest, package_type)
        # elif (">" in version_dest or "<" in version_dest) and " " not in version_dest:
        #     version_item = handle_version_or(version_dest, package_type)
        # elif (">" in version_dest or "<" in version_dest) and " " in version_dest:
        #     version_item = handle_version_comma(version_dest, package_type)
        elif ".x" in version_dest:
            if ".x-dev" not in version_dest:
                version_item = handle_version_compatible(version_dest, package_type)
            else:
                version_dest = version_dest.replace(".x-dev", ".0.dev")
                format_version_dest = arrangement_version(
                    version_dest, package_type
                )
                if isinstance(format_version_dest, Version):
                    if format_version_dest.new_version:
                        left_version = format_version_dest.new_version
                    else:
                        raise VersionDestError(format_version_dest.old_version + "格式化失败")
                else:
                    left_version = format_version_dest
                version_item = Item(
                    left_open=True,
                    left=left_version,
                    right_open=True,
                    right=left_version,
                )
        elif " -" in version_dest:
            format_left_version_dest = arrangement_version(
                version_dest.split("-")[0], package_type
            )
            format_right_version_dest = arrangement_version(
                version_dest.split("-")[1], package_type
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
        elif "*" in version_dest:
            if "*" != version_dest.replace(" ", ""):
                format_version_dest = arrangement_version(
                    version_dest, package_type, is_del_identifier=True
                )
                if isinstance(format_version_dest, Version):
                    version_dest_list = format_version_dest.new_version.split("*")
                    min_version_dest = version_dest_list[0]
                    if min_version_dest[-1] == ".":
                        min_version = version_dest_list[0] + "0"
                    else:
                        min_version = version_dest_list[0] + ".0"
                    max_version = Version.max_version_calculation(min_version)
                    version_item = Item(
                        left_open=True, right_open=False, left=min_version, right=max_version
                    )
                else:
                    raise VersionDestError("格式化失败：{}".format(version_dest))
            else:
                version_item = Item(left_open=True, left="", right_open=True, right="")
        else:
            version_dest = version_dest.replace(" ", "")
            if version_dest and "*" != version_dest:
                version_item = Item(left_open=True, left=version_dest, right_open=True, right=version_dest)
            else:
                version_item = Item(
                    left_open=True,
                    right_open=True,
                    left="",
                    right="",
                )
        return version_item
