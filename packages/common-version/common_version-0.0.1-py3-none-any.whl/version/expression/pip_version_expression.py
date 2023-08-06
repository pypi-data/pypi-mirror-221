# -*- coding: utf-8 -*-
# flake8: noqa
from abc import ABC

from lj_spider_core.version.exceptions import VersionDestError
from lj_spider_core.version.expression.base import VersionExpression
from lj_spider_core.version.expression.base_method import (
    arrangement_version,
    handle_version_change_source,
    handle_version_compatible, get_equal_item, chinese_to_english_version, handle_version_or,
)
from lj_spider_core.version.version_base import Item, ItemGroup
from lj_spider_core.version.version_base.base_version import Version


class VersionPipExpression(VersionExpression, ABC):
    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param package_type: 包类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        version_expression = chinese_to_english_version(version_expression)
        if version_expression:
            version_expression = version_expression.replace(" ", "")
        if "," in version_expression:
            version_dest_list = version_expression.split(",")
            items = []
            for version in version_dest_list:
                part_version_item = self.handle_pip_compare(package_type, version)
                items.append(part_version_item)
            version_item = ItemGroup(*items, is_or=False)
        else:
            version_item = self.handle_pip_compare(package_type, version_expression)
        if isinstance(version_item, ItemGroup):
            version_item = version_item.merge()
        return version_item

    def handle_pip_compare(self, package_type, version_dest):
        """
        开始比较函数
        :param package_type:包类型
        :param version_dest:版本表达式
        :return:
        """
        if "~=" in version_dest:
            version_item = handle_version_compatible(version_dest, package_type)
        elif "!=" in version_dest or "==" in version_dest:
            if "*" not in version_dest:
                if "===" not in version_dest:
                    version_item = self.handle_pip_matching(package_type, version_dest)
                else:
                    version_item = get_equal_item(version_dest, package_type, is_del_brackets=True)
            else:
                version_item = self.handle_pip_star(package_type, version_dest)
        elif ">" in version_dest or "<" in version_dest:
            version_item = handle_version_or(version_dest, package_type)
        else:
            format_version_dest = arrangement_version(
                version_dest, package_type, is_del_identifier=True
            )
            if isinstance(format_version_dest,Version):
                version_item = Item(
                    left_open=True,
                    right_open=True,
                    left=format_version_dest.new_version,
                    right=format_version_dest.new_version,
                )
            else:
                version_item = Item(
                    left_open=True,
                    right_open=True,
                    left=format_version_dest,
                    right=format_version_dest,
                )
        return version_item

    def handle_pip_star(self, package_type, version_dest):
        """
        带有*的 != 和==逻辑
        :param package_type:
        :param version_dest:
        :return:
        """
        version_dest = version_dest.replace("*", "0")
        version_obj = arrangement_version(
            version_dest, package_type, is_del_identifier=True
        )
        if isinstance(version_obj, Version):
            if version_obj.new_version:
                format_version = version_obj.new_version
            else:
                raise VersionDestError(version_obj.old_version + "version_expression格式化失败")
        else:
            format_version = version_obj
        if "!=" in version_dest:
            max_version = Version.max_version_calculation(format_version)
            left_item = Item(
                left_open=True, right_open=False, left="", right=format_version
            )
            right_item = Item(
                left_open=True, right_open=True, left=max_version, right=""
            )
            group = ItemGroup(left_item, right_item, is_or=True)
            return group
        else:
            max_version = Version.max_version_calculation(format_version)
            return Item(
                left_open=True,
                right_open=False,
                left=format_version,
                right=max_version,
            )

    def handle_pip_matching(self, package_type, version_dest):
        from lj_spider_core.version.version_base import Version

        """
        不带有*的 != 和==逻辑
        处理==
            例1：==1.1.1  版本号必须与1.1.1完全相等才算作匹配
            例2：==1.1     版本号为1.1.0或1.1都算作与之匹配
            例3：==1.1.*   匹配前缀与1.1.相等的版本号，包括：1.1.post1
        :param package_type:
        :param version_dest:
        :return:
        """

        new_version_dest = arrangement_version(
            version_dest, package_type, is_del_identifier=True
        )
        if isinstance(new_version_dest, Version):
            if new_version_dest.new_version:
                format_version = new_version_dest.new_version
            else:
                raise VersionDestError(new_version_dest.old_version + "version_expression格式化失败")
        else:
            format_version = new_version_dest
        if "!=" in version_dest:
            left_item = Item(
                left_open=True, right_open=False, left="", right=format_version
            )
            right_item = Item(
                left_open=False, right_open=True, left=format_version, right=""
            )
            group = ItemGroup(left_item, right_item, is_or=True)
            return group

        else:
            return Item(
                left_open=True,
                right_open=True,
                left=format_version,
                right=format_version,
            )

    def handle_pip_minimum_match(self, version_dest):
        """
        todo 处理>===
            可以使用的最小版本
        :param version_dest:
        :return:
        """
        pass
