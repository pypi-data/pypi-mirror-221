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


class MavenVersion(Version):

    def __init__(self, version, package_type="composer", is_sort=False):
        super().__init__(version, package_type, is_sort)

    def format_release(self, version):
        """
        预发行版分别允许alpha、beta、c、 pre和previewfor a、b、rc、rc和的附加拼写rc 。
        这允许诸如1.1alpha1、1.1beta2或 1.1c3规范化为1.1a1、1.1b2和的版本1.1rc3。
        在每种情况下，附加拼写应被视为等同于它们的正常形式。
        :param version:
        :return:
        """
        version = super().format_release(version)
        if "m" in version:
            version = version.replace("m", "b")
        return version

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
