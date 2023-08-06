# -*- coding: UTF-8 -*-
"""
@Project:lj_spider_core
@File:snyk_version.py
@IDE: PyCharm
@Author : hsc
@Date:2022/9/21 14:26
@function：
"""
from version.version_base.base_version import Version


class NpmVersion(Version):
    def __init__(self, version, package_type="npm", is_sort=False):
        super().__init__(version, package_type, is_sort)

    def format_version(self):
        from version.expression import arrangement_version
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
            version = version.replace("、", ".")
            version = version.replace("+", "")
            version = version.replace("-", ".")
            version = self.del_zero(version)
            new_version = self.base_format(version)
            canonical_version = arrangement_version(new_version,
                                                    self.package_type,
                                                    is_del_identifier=True,
                                                    is_format=False,
                                                    is_del_brackets=True, )
            if not self.is_canonical(canonical_version):
                new_version = ""
        return new_version
