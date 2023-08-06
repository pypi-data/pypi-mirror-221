# -*- coding: UTF-8 -*-
"""
@Project:lj_spider_core
@File:snyk_version.py
@IDE: PyCharm
@Author : hsc
@Date:2022/9/21 14:26
@function：
"""
import re

from version.version_base.base_version import Version


class SnykVersion(Version):
    def __init__(self, version, package_type="snyk", is_sort=False):
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
            version = version.replace("~", ".")
            version = version.replace("-", "_")
            version = version.replace(":", "_")
            if version and version[0] == '.':
                version = "0" + version
            version = self.del_zero(version)
            identification = self.get_identification(version)
            if identification:
                version = version[len(identification):]
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
            final_cmp_version = self.get_final_cmp_version(del_version, other_del_version)
        return final_cmp_version

    def get_final_cmp_version(self, del_version, other_del_version):
        from version.expression.base_method import supplement_zero
        final_cmp_version = []
        cmp_versions = []
        if "_" in del_version:
            part_versions = del_version.split("_")
            other_part_versions = []
            if "_" in other_del_version:
                other_part_versions = other_del_version.split("_")
            for i in range(len(part_versions)):
                part_i_version = part_versions[i].split(".")
                if other_part_versions and len(other_part_versions) - 1 >= i:
                    other_part_i_versions = other_part_versions[i].split(".")
                    sup_cmp_versions, _ = supplement_zero(
                        part_i_version, other_part_i_versions
                    )
                    cmp_versions += sup_cmp_versions
                else:
                    cmp_versions += part_i_version
        else:
            cmp_versions += del_version.split(".")
        for cmp_version in cmp_versions:
            pattern = re.compile(r"([a-z]+)")
            dest_res = re.findall(pattern, cmp_version)
            if dest_res:
                final_cmp_version.append(cmp_version)
            else:
                if cmp_version:
                    try:
                        final_cmp_version.append(int(cmp_version))
                    except Exception:
                        shu_pattern = re.compile(r"([0-9]+)")
                        shu_dest_res = re.findall(pattern, cmp_version)
                        if shu_pattern:
                            for i in shu_dest_res:
                                final_cmp_version.append(i)
        return final_cmp_version

    def is_canonical(self, version):
        version_re = r"([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][" \
                     r"0-9]*))?(\.dev(0|[1-9][0-9]*))?"
        if version:
            return re.match(f"^{version_re}(_{version_re})*$", version, ) is not None
        return False
