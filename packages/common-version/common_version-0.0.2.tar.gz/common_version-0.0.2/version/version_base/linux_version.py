# -*- coding: UTF-8 -*-
"""
@Project:lj_spider_core
@File:linux_lj_version.py
@IDE: PyCharm
@Author : hsc
@Date:2022/10/25 15:17
@function：
"""
import re

from version.version_base.snyk_version import SnykVersion


class LinuxVersion(SnykVersion):
    def __init__(self, version, package_type="linux", is_sort=False):
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
            version = version.replace("[", '.')
            version = version.replace("(", '.')
            version = version.replace("]", '.')
            version = version.replace(")", '.')
            version = version.replace(" ", "")
            version = version.replace("/", "")
            version = version.replace("、", ".")
            version = version.replace("+", "")

            version = version.replace("-", ".")
            version = version.replace("~", ".")
            version = self.del_zero(version)
            identification = self.get_identification(version)
            if identification:
                version = version[len(identification):]
            pattern = r"((>|<|=)*)\d*:"
            version_group = re.match(pattern, version)
            if version_group:
                version_mao = version_group.group()
                version = version[len(version_mao):]
            else:
                version_mao = ""
                version = version.replace(":", "_")
            version = identification + version
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
                elif new_version:
                    new_version = self.base_format(new_version)
                    canonical_version = arrangement_version(new_version,
                                                            self.package_type,
                                                            is_del_identifier=True,
                                                            is_format=False,
                                                            is_del_brackets=True, )
                    new_version = canonical_version
            if version_mao:
                new_version = version_mao + new_version
            if identification not in new_version:
                new_version = identification + new_version
        return new_version

    def format_cmp_version(self, other=None):
        final_cmp_version = []
        if self.new_version or self.old_version:
            if self.new_version:
                del_version = self.del_replace(self.new_version)
            else:
                del_version = self.del_replace(self.old_version)
            if other.new_version:
                other_del_version = other.del_replace(other.new_version)
            else:
                other_del_version = other.del_replace(other.old_version)
            if ":" not in other_del_version or ":" not in del_version:
                pattern = r"^\d*:"
                del_version = re.sub(pattern, "", del_version)
            else:
                del_version = del_version.replace(":", ".")
            final_cmp_version = self.get_final_cmp_version(del_version, other_del_version)
        return final_cmp_version
