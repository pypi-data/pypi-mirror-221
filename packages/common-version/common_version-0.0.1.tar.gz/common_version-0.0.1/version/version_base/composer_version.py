# -*- coding: UTF-8 -*-
"""
@Project:lj_spider_core
@File:composer_version.py
@IDE: PyCharm
@Author : hsc
@Date:2022/9/21 16:01
@function：
"""
from lj_spider_core.version.version_base.base_version import Version


class ComposerVersion(Version):

    def __init__(self, version, package_type="composer", is_sort=False):
        super().__init__(version, package_type, is_sort)

    def format_version(self):
        from lj_spider_core.version.expression import arrangement_version
        """
        格式化版本
        :param version:
        :return:
        """
        new_version = ""
        if self.old_version:
            version = self.old_version
            version = version.lower()
            version = version.replace(" ", "")
            version = version.replace("/", "")
            version = version.replace("+", "")
            version = version.replace("、", ".")
            version = version.replace("-", ".")
            version = version.replace("_", ".")
            if version and version[0] == '.':
                version = "0" + version
            version = self.del_zero(version)
            new_version = self.base_format(version)
            canonical_version = arrangement_version(new_version,
                                                    self.package_type,
                                                    is_del_identifier=True,
                                                    is_format=False,
                                                    is_del_brackets=True, )
            if not self.is_canonical(canonical_version):
                if not self.is_sort:
                    new_version = self.del_str(new_version)
                if new_version and new_version[0] == '.':
                    new_version = new_version[1:]
        return new_version
