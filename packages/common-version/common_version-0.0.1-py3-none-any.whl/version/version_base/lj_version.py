# -*- coding: utf-8 -*-
import enum

from lj_spider_core.version.version_base import ItemGroup, Item


class CompareType(enum.Enum):
    COMPARE = "compare"
    EQUAL = "=="


def get_sort_version_obj(version_objs, last_sort_versions):
    final_version_objs = []
    for version in last_sort_versions:
        for version_obj in version_objs:
            if version_obj.new_version == version:
                final_version_objs.append(version_obj)
    return final_version_objs


class LjVersion:
    def __init__(self, version_str=None, package_type=None):
        self.version_str = version_str
        self.format_version = ""
        self.package_type = package_type
        self.format_version_obj = self.format_compare_version()
        self.format_version_list = list()

    def format_compare_version(self):
        from lj_spider_core.version import (
            get_base_version
        )
        version_obj = get_base_version(self.package_type, self.version_str)
        if version_obj.new_version:
            self.format_version = version_obj.new_version
        else:
            self.format_version = version_obj.old_version
        return version_obj

    def version_compare(self, version1, version2):
        from lj_spider_core.version import (
            get_base_version
        )
        version1_obj = get_base_version(self.package_type, version1)
        version2_obj = get_base_version(self.package_type, version2)
        return version1_obj.__cmp__(version2_obj)

    def format_version_lj_list(self, lj_expression):
        """
        格式化棱镜表达式
        :param lj_expression:
        :param version_str:
        :return:
        """
        if "||" in lj_expression:
            self.format_version_list = lj_expression.split("||")
        else:
            self.format_version_list.append(lj_expression)

    # def compare_version(self, compare_type, version_dest):
    #     from lj_spider_core.version.version_base import Version
    #     from lj_spider_core.version import version_compare
    #     if isinstance(compare_type, str):
    #         compare_type = CompareType(compare_type)
    #     assert compare_type in CompareType
    #     flag = None
    #     if CompareType.EQUAL == compare_type:
    #         if version_dest == self.version_str:
    #             flag = 0
    #     else:
    #         if isinstance(self.format_version_obj, Version):
    #             flag = version_compare(self.package_type,
    #                                    self.format_version_obj.old_version, version_dest
    #                                    )
    #         else:
    #             if version_dest == self.version_str:
    #                 flag = 0
    #     return flag
    #
    # def compare_version_equal(self, format_version1, format_version2):
    #     from lj_spider_core.version import is_canonical
    #     from lj_spider_core.version.expression.base_method import (
    #         compare_version_size,
    #     )
    #     if is_canonical(self.package_type, format_version2.new_version) and is_canonical(
    #             self.package_type, format_version1.new_version,
    #     ):
    #         flag = compare_version_size(
    #             format_version1.new_version, format_version2.new_version, self.package_type
    #         )
    #     else:
    #         flag = None
    #     return flag
    #
    # def compare_left_and_right(self, version_dest):
    #     left_version = version_dest.split(",")[0]
    #     left_identifier = version_dest[0]
    #     right_version = version_dest.split(",")[1]
    #     right_identifier = version_dest[-1]
    #     if len(left_version) > 1:
    #         left_version = left_version.replace("[", "")
    #         left_version = left_version.replace("(", "")
    #         flag_left = self.compare_version("compare", left_version)
    #     else:
    #         flag_left = 1
    #     if len(right_version) > 1:
    #         right_version = right_version.replace("]", "")
    #         right_version = right_version.replace(")", "")
    #         flag_right = self.compare_version("compare", right_version)
    #     else:
    #         flag_right = -1
    #     if flag_left == 1 and (
    #             flag_right is True
    #             or flag_right == -1
    #             or (flag_right == 0 and right_identifier == "]")
    #     ):
    #         flag = True
    #     elif (
    #             flag_left == 0
    #             and left_identifier == "["
    #             and (flag_right == -1 or (flag_right == 0 and right_identifier == "]"))
    #     ):
    #         flag = True
    #     else:
    #         flag = False
    #     return flag

    def get_part_item(self, version):
        left_open = True if version[0] == "[" else False
        right_open = True if version[-1] == "]" else False
        left_version = version.split(",")[0]
        left_version = left_version[1:]
        left_version = left_version.replace(" ", "")
        right_version = version.split(",")[-1]
        right_version = right_version[:-1]
        right_version = right_version.replace(" ", "")
        return Item(left_open=left_open, left=left_version, right_open=right_open, right=right_version)

    def get_lj_version_item(self, lj_expression):
        all_item = []
        self.format_version_lj_list(lj_expression)
        for version in self.format_version_list:
            if "[" in version or "(" in version:
                part_item = self.get_part_item(version)
            else:
                if version.replace(" ", "") == "*":
                    part_item = Item(left_open=True, left="", right_open=True, right="")
                else:
                    version = version.replace(" ", "")
                    part_item = Item(left_open=True, left=version, right_open=True, right=version)
            all_item.append(part_item)
        ret = ItemGroup(*all_item, is_or=True)
        ret = ret.merge()
        return ret

    def check_version_in_expression(self, lj_expression):
        from lj_spider_core.version import get_base_version
        from lj_spider_core.version.version_base import Equal_Or_Compare_Type
        """
        检查版本是否属于棱镜表达式
        :param lj_expression:
        :return:
        """
        if isinstance(lj_expression, Item) or isinstance(lj_expression, ItemGroup):
            if lj_expression.get_value() == "*":
                return True
            ret = lj_expression
        elif isinstance(lj_expression, str):
            if lj_expression == "*":
                return True
            else:
                ret = self.get_lj_version_item(lj_expression)
        else:
            return "类型错误"
        if isinstance(ret, Item):
            return ret.is_in_version_item(self.version_str, self.package_type)
        elif isinstance(ret, ItemGroup):
            part_flag = False
            if ret.all_equal:
                if self.version_str in ret.all_equal:
                    part_flag = True
                else:
                    if self.package_type in Equal_Or_Compare_Type:
                        part_version = get_base_version(self.package_type, self.version_str)
                        if part_version.new_version:
                            part_com_version = part_version.new_version
                        else:
                            part_com_version = part_version.old_version
                        part_item = Item(left_open=True, right_open=True,
                                         left=part_com_version, right=part_com_version)
                        for i in ret.all_equal:
                            i_part_flag = part_item.is_in_version_item(i, self.package_type)
                            if i_part_flag:
                                part_flag = True
                                break
                    else:
                        part_item = Item(left_open=True, right_open=True,
                                         left=self.version_str, right=self.version_str)
                        if part_item.left in ret.all_equal:
                            part_flag = True
            if not part_flag and ret.all_other:
                for ret_item in ret.all_other:
                    part_flag = ret_item.is_in_version_item(self.version_str, self.package_type)
                    if part_flag:
                        break
            return part_flag

    def sort_versions2(self, versions, remove_not_final):
        from lj_spider_core.version import get_base_version
        not_version_objs = []
        final_version_objs = []
        fail_versions = []
        for version in versions:
            # new_version_obj = get_base_version(self.package_type, version, is_sort=True)
            new_version_obj = get_base_version(self.package_type, version)
            if new_version_obj.new_version:
                if remove_not_final:
                    if (
                            "a" not in new_version_obj.new_version
                            and "b" not in new_version_obj.new_version
                            and "rc" not in new_version_obj.new_version
                            and "pre" not in new_version_obj.new_version
                    ):
                        if new_version_obj.new_version:
                            not_version_objs.append(new_version_obj)
                        else:
                            fail_versions.append(new_version_obj)
                    else:
                        fail_versions.append(new_version_obj)
                else:
                    final_version_objs.append(new_version_obj)
            else:
                fail_versions.append(new_version_obj)
        if remove_not_final:
            version_objs = not_version_objs
        else:
            version_objs = final_version_objs
        last_sort_versions = sorted(version_objs)
        return list(map(str, last_sort_versions)), sorted(list(map(str, fail_versions)))

    # def merge_versions_expression(self, versions, is_or):
    #     from lj_spider_core.version import change_to_lj_expression
    #     if is_or:
    #         items = []
    #         for version in versions:
    #             part_item = change_to_lj_expression(package_type=self.package_type, version_expression=version)
    #             if isinstance(part_item, Item):
    #                 items.append(part_item)
    #             else:
    #                 items += part_item.items
    #         new_group = ItemGroup(*items, is_or=True)
    #     else:
    #         items = None
    #         for version in versions:
    #             part_item = change_to_lj_expression(package_type=self.package_type, version_expression=version)
    #             if items:
    #                 items = ItemGroup(items, part_item, is_or=is_or)
    #             else:
    #                 items = part_item
    #         new_group = items
    #     return new_group.merge()

    def merge_versions_expression(self, versions, is_or):
        from lj_spider_core.version import change_to_lj_expression
        if is_or:
            version = "||".join(versions)
            new_group = change_to_lj_expression(package_type=self.package_type, version_expression=version)
        else:
            items = []
            for version in versions:
                part_item = change_to_lj_expression(package_type=self.package_type, version_expression=version)
                items.append(part_item)
            new_group = ItemGroup(*items, is_or=is_or)
        return new_group.merge()
