# -*- coding: utf-8 -*-
import copy
import enum
import re

from aenum import MultiValueEnum

from lj_spider_core.version.version_base.common_method import is_match


class VersionSort(MultiValueEnum):
    DEV = "dev", 10
    X_DEV = "x-dev", 11
    A = "a", 20
    B = "b", 30
    M = "m", 35
    RC = "rc", 40
    OTHER = "other", 50
    POST = "post", 60


class CompareType(enum.Enum):
    COMPARE = "compare"
    EQUAL = "=="


def del_index(version, ver_type):
    """
    递归删除表达式中后边的.
    :param version:
    :param ver_type:
    :return:
    """
    pattern = re.compile(r"^\d.*")
    if ver_type in version:
        index_ver = version.index(ver_type)
        res = re.match(pattern, version[index_ver + len(ver_type):])
        if res:
            ver_num = res.group()
            if version[index_ver - 1] == ".":
                if ver_type == "dev" or ver_type == "post":
                    return version[
                           : index_ver + len(ver_type) + len(ver_num)
                           ] + del_index(
                        version[index_ver + len(ver_type) + len(ver_num):], ver_type
                    )
                else:
                    return (
                            version[: index_ver - 1]
                            + version[index_ver: index_ver + len(ver_type) + len(ver_num)]
                            + del_index(version[index_ver + len(ver_type) + len(ver_num):], ver_type)
                    )
            return version[: index_ver + len(ver_type) + len(ver_num)] + del_index(
                version[index_ver + len(ver_type) + len(ver_num):], ver_type
            )
        else:
            if index_ver + len(ver_type) < len(version):
                next_res = re.match(
                    pattern, version[index_ver + len(ver_type) + 1:]
                )
                if (ver_type == 'a' or ver_type == 'b' or ver_type == "rc") \
                        and index_ver > 0 and version[index_ver - 1] == '.':
                    return version[:index_ver - 1] + del_index(version[index_ver:], ver_type)
                if version[index_ver + len(ver_type)] == ".":
                    if index_ver + len(ver_type) + 1 == len(version):
                        if (
                                ver_type == "dev"
                                or ver_type == "post"
                                # or ver_type == "rc"
                        ):
                            return version[:index_ver + len(ver_type) - 1] + "1"
                        else:
                            return version[:index_ver + len(ver_type)] + "1"

                    else:
                        if (
                                ver_type == "dev"
                                or ver_type == "post"
                                # or ver_type == "rc"
                        ):
                            if next_res:
                                ver_num = next_res.group()
                                if index_ver + len(ver_type) + len(ver_num) + 1 == len(version):
                                    return version[:index_ver + len(ver_type)] + ver_num
                                else:
                                    return version[:index_ver + len(ver_type)] + ver_num + '.' + del_index(
                                        version[index_ver + len(ver_type) + len(ver_num):], ver_type)
                            else:
                                return version[:index_ver + len(ver_type)] + "1." + del_index(
                                    version[index_ver + len(ver_type) + 1:], ver_type)
                        else:
                            if next_res:
                                ver_num = next_res.group()
                                if index_ver + len(ver_type) + len(ver_num) + 1 == len(version):
                                    return version[:index_ver + len(ver_type)] + ver_num
                                else:
                                    return version[:index_ver + len(ver_type)] + ver_num + '.' + del_index(
                                        version[index_ver + len(ver_type) + len(ver_num) + 1:], ver_type)
                            else:
                                return version[:index_ver + len(ver_type)] + "1" + del_index(
                                    version[index_ver + len(ver_type) + 1:], ver_type)
                else:
                    return version[: index_ver + len(ver_type)] + del_index(
                        version[index_ver + len(ver_type):], ver_type
                    )
            elif index_ver + len(ver_type) == len(version):
                if (
                        version[index_ver - 1] == "."
                        and ver_type != "dev"
                        and ver_type != "post"
                ):
                    return version[: index_ver - 1] + ver_type + "1"
                else:
                    if version[index_ver] != '.' and (ver_type == "post" or ver_type == 'dev'):
                        if version[index_ver - 1] != '.':
                            return version[:index_ver] + "." + ver_type + "1"
                    return version[:index_ver] + ver_type + "1"
            else:
                if version[index_ver - 1] == ".":
                    return version[: index_ver - 1] + ver_type + "1"
                else:
                    return version
    return version


class Version:
    def __init__(self, version, package_type=None, is_sort=False):
        self.is_sort = is_sort
        self.old_version = version
        self.package_type = package_type
        self.new_version = self.format_version()
        self.cmp_versions = ""

    def __str__(self):
        return str(self.old_version)

    def __repr__(self):
        return str(self)

    def del_zero_func(self, data):
        iden = "."
        new_data = data.group()
        new_data = new_data.replace(".", "")
        if self.package_type == "snyk" and "_" in new_data:
            new_data = new_data.replace("_", "")
            iden = "_"
        new_data = int(new_data)
        return iden + str(new_data)

    def del_zero(self, data):
        if data:
            data = re.sub(r"\.0+([1-9]+)", self.del_zero_func, data)
            if self.package_type == "snyk" and "_" in data:
                data = re.sub(r"\_0+([1-9]+)", self.del_zero_func, data)
        return data

    def del_replace(self, version):
        cmp_versions = version.replace("<", "")
        cmp_versions = cmp_versions.replace(">", "")
        cmp_versions = cmp_versions.replace("=", "")
        cmp_versions = cmp_versions.replace("[", "")
        cmp_versions = cmp_versions.replace("(", "")
        cmp_versions = cmp_versions.replace("]", "")
        cmp_versions = cmp_versions.replace(")", "")
        return cmp_versions

    def format_cmp_version(self, other=None):
        final_cmp_version = []
        if self.new_version or self.old_version:
            if self.new_version:
                cmp_versions = self.del_replace(self.new_version).split(".")
            else:
                cmp_versions = self.del_replace(self.old_version).split(".")
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
                            pass
        return final_cmp_version

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __cmp__(self, other):
        from lj_spider_core.version import get_base_version
        if isinstance(other, str):
            other = get_base_version(self.package_type, other)
        other.cmp_versions = other.format_cmp_version(self)
        self.cmp_versions = self.format_cmp_version(other)
        flag = self.compare_to_versions(other)
        return flag if self.cmp_versions else 2

    def compare_to_versions(self, other):
        from lj_spider_core.version.expression.base_method import supplement_zero, compare_str_change_list
        equal_num = 0
        version_source_list, version_dest_list = supplement_zero(
            self.cmp_versions, other.cmp_versions
        )
        version_source_list = [i if i != '0' else 0 for i in version_source_list]
        version_dest_list = [i if i != '0' else 0 for i in version_dest_list]
        flag = 0
        for i in range(0, len(version_source_list)):
            if version_source_list[i] == "master" or version_dest_list[i] == "master":
                if version_dest_list[i] != "master":
                    flag = 1
                    break
                elif version_source_list[i] != "master":
                    flag = -1
                    break
            if isinstance(version_source_list[i], int) and isinstance(version_dest_list[i], int):
                if version_source_list[i] > version_dest_list[i]:
                    flag = 1
                    break
                elif version_source_list[i] < version_dest_list[i]:
                    flag = -1
                    break
                elif version_source_list[i] == version_dest_list[i]:
                    equal_num += 1
            else:
                if self.old_version != version_source_list[i] and other.old_version != version_dest_list[i]:
                    flag = compare_str_change_list(
                        version_source_list[i], version_dest_list[i]
                    )
                    if flag != 0:
                        break
                    else:
                        equal_num += 1
                else:
                    flag = -1
                    break
        return flag

    def del_str(self, version):
        pattern = r"((>|<|=)*)\d(\_|\.|\d|a|b|(rc)|(.post)|(_post)){0,}\d*"
        version_group = re.finditer(pattern, version)
        final_version = []
        for i in version_group:
            list_version = i.group().split(".")
            if len(list_version) > len(final_version):
                final_version = list_version
        new_version = ".".join(final_version)
        return new_version

    def base_format(self, version):
        version = version.replace("+", "")
        flag, re_version = is_match(version, r"^[a-zA-Z-_\/]*(\S+)$")
        if flag and re_version != version and len(re_version) > 1:
            version = re_version
        if (re_version == version and len(re_version) == 1) or len(re_version) > 1:
            part_version = copy.deepcopy(version)
            if part_version.replace(" ", "").replace(".", "") != 'master':
                version = self.format_release(version)
                version = self.format_post(version)
                version = self.format_dev(version)
                version = self.format_del(version)
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
            version = version.replace("-", ".")
            version = version.replace('"', "")
            version = version.replace("'", "")
            # version = version.replace("\\", "")
            version = version.replace("、", ".")
            version = version.replace(":", ".")
            version = version.replace("_", ".")
            version = self.del_zero(version)
            if version and version[0] == '.':
                version = "0" + version
            identification = self.get_identification(version)
            new_version = self.base_format(version)
            canonical_version = arrangement_version(new_version,
                                                    self.package_type,
                                                    is_del_identifier=True,
                                                    is_format=False,
                                                    is_del_brackets=True, )
            if not self.is_canonical(canonical_version):
                if not self.is_sort:
                    new_version = self.del_str(new_version)
            if identification not in new_version:
                new_version = identification + new_version
            if new_version:
                if new_version[-1] == '.':
                    new_version = new_version[:-1]
        return new_version

    def get_identification(self, version):
        new_version = ""
        pattern = r"(>|<|=)*"
        version2 = re.match(pattern, version)
        if version2:
            new_version = version[version2.start():version2.end()]
        return new_version

    def format_release(self, version):
        """
        预发行版分别允许alpha、beta、c、 pre和previewfor a、b、rc、rc和的附加拼写rc 。
        这允许诸如1.1alpha1、1.1beta2或 1.1c3规范化为1.1a1、1.1b2和的版本1.1rc3。
        在每种情况下，附加拼写应被视为等同于它们的正常形式。
        :param version:
        :return:
        """
        if "alpha" in version:
            version = version.replace("alpha", "a")
        if "beta" in version:
            version = version.replace("beta", "b")
        if "rc" in version:
            version = version.replace("rc", "rc")
        if "preview" in version:
            version = version.replace("preview", "rc")
        if "pre" in version:
            version = version.replace("pre", "rc")
        if "c" in version and "rc" not in version:
            version = version.replace("c", "rc")
        return version

    def format_post(self, version):
        """
        发布后允许 和 的附加rev拼写r。
        这允许诸如1.0-r4which normalizes to之类的版本1.0.post4。与预发行版一样，应将附加拼写视为等同于其正常形式。
        :param version:
        :return:
        """
        if "release" in version:
            version = version.replace("release", "post")
        if "rev" in version:
            version = version.replace("rev", "post")
        if "r" in version and "rc" not in version:
            version = version.replace("r", "post")
        return version

    def format_dev(self, version):
        """
        发布后允许 和 的附加rev拼写r。
        这允许诸如1.0-r4which normalizes to之类的版本1.0.post4。与预发行版一样，应将附加拼写视为等同于其正常形式。
        :param version:
        :return:
        """
        if "devel" in version:
            version = version.replace("devel", "dev")
        if "dev" in version:
            version = version.replace("dev", "dev")
        if "final" in version:
            version = version.replace("final", "dev")
        return version

    def format_del(self, version):
        version = del_index(version, "a")
        version = del_index(version, "b")
        version = del_index(version, "rc")
        version = del_index(version, "post")
        version = del_index(version, "dev")
        if version[-1] == ".":
            version = version[:-1]
        return version

    def is_canonical(self, version):
        """
        版本格式化之后的验证
        :return:
        """
        version_re = r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][" \
                     r"0-9]*))?(\.dev(0|[1-9][0-9]*))?$"
        if version:
            return re.match(f"{version_re}", version, ) is not None
        return False

    @staticmethod
    def max_version_str(version):
        """
        带有字母的最大版本
        :param version:
        :return:
        """
        pattern = re.compile(r"([a-z]+)")
        version_re = re.findall(pattern, version)
        version_dest_str_list = [
            int(i) if i else "0" for i in version.split(version_re[0])
        ]
        ver_enum = VersionSort("other").values
        try:
            ver_enum = VersionSort(version_re[0]).values
        except Exception:
            print("此处未找到对应的英文版本")
        finally:
            ver_arg = ver_enum[1]
            if ver_arg != 6:
                max_version_num = int(version_dest_str_list[0]) + 1
            else:
                max_version_num = int(version_dest_str_list[0]) + 2
            return str(max_version_num)

    @staticmethod
    def max_version_calculation(version):
        """
        带有字母的最大版本
        :param version:
        :return:
        """
        max_version = ""
        version_list = version.split(".")
        if len(version_list) >= 2:
            pattern = re.compile(r"([a-z]+)")
            version_re = re.findall(pattern, version)
            if version_re:
                for ver in range(0, len(version_list)):
                    pattern = re.compile(r"([a-z]+)")
                    version_re = re.findall(pattern, version_list[ver])
                    if version_re:
                        max_version = Version.max_version_calculation(max_version)
                        break
                    else:
                        max_version = max_version + version_list[ver] + "."
            else:
                for ver in range(0, len(version_list)):
                    if ver < len(version_list) - 2:
                        max_version = max_version + version_list[ver] + "."
                    elif ver == len(version_list) - 2:
                        max_version_count = int(version_list[-2]) + 1
                        max_version = max_version + str(max_version_count) + "."
                    else:
                        if ver != len(version_list) - 1:
                            max_version = max_version + str(0) + "."
                        else:
                            max_version = max_version + str(0)
        else:
            pattern = re.compile(r"([a-z]+)")
            version_re = re.findall(pattern, version_list[0])
            if not version_re:
                max_version = str(int(version_list[0]) + 1)
            else:
                max_version_num = Version.max_version_str(version_list[0])
                max_version = max_version + max_version_num
        if max_version[-1] == ".":
            max_version = max_version[:-1]
        return max_version
