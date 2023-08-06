# -*- coding: utf-8 -*-
__version__ = "0.0.3"

import enum

__all__ = [
    "check_version_in_expression",
    "PackageType",
    "get_base_version",
    "is_canonical",
    "change_to_expression",
    "check_versions_in_expression",
]

from version.expression import VersionPipExpression, VersionMavenExpression, VersionNpmExpression, \
    VersionNugetExpression, VersionCargoExpression, VersionGoExpression, VersionCocoExpression, VersionCExpression, \
    VersionRubyExpression, VersionComposerExpression, VersionHexExpression, VersionNvdExpression, \
    VersionSnykExpression, VersionLinuxExpression, VersionOtherExpression
from version.version_base import LjVersion, Version, NpmVersion, GoVersion, ComposerVersion, SnykVersion
from version.version_base.linux_version import LinuxVersion
from version.version_base.maven_version import MavenVersion


class PackageType(enum.Enum):
    Base = "base"
    Pip = "pip"
    Maven = "maven"
    Npm = "npm"
    Nuget = "nuget"
    Cargo = "cargo"
    Go = "go"
    Cocoapods = "cocoapods"
    C = "c"
    Ruby = "ruby"
    Composer = "composer"
    Hex = "hex"
    Nvd = "nvd"
    Snyk = "snyk"
    Linux = "linux"
    Other = "other"

    @classmethod
    def values(cls):
        return [item.value for item in cls]


class MapPackageType(enum.Enum):
    Base = "base"
    Maven = "maven"
    Gradle = "maven"
    Ivy = "maven"
    Sbt = "maven"
    Grape = "maven"
    Composer = "composer"
    Ruby = "ruby"
    Cocoapods = "cocoapods"
    Nuget = "nuget"
    Cargo = "cargo"
    Wordpress = "other"
    Go = "go"
    Govendor = "go"
    Vendor = "go"
    Gomoudles = "go"
    Godep = "go"
    Pip = "pip"
    Conda = "pip"
    Python = "pip"
    Poetry = "pip"
    Npm = "npm"
    Yarn = "npm"
    Jspm = "npm"
    Bower = "npm"
    Linux = "linux"
    C = "c"
    Conan = "c"
    Hex = "hex"
    Other = "other"
    Pub = "other"
    Cran = "other"
    Pear = "other"
    Clojars = "other"
    Nvd = "nvd"
    Snyk = "snyk"

    @classmethod
    def values(cls):
        return [item.value for item in cls]

    @classmethod
    def get_value_by_key(cls, key: str):
        try:
            val = MapPackageType[key.capitalize()].value
        except Exception:
            val = MapPackageType["Other"].value
        return val


Expression_CLASSES = {
    PackageType.Pip: VersionPipExpression(),
    PackageType.Maven: VersionMavenExpression(),
    PackageType.Npm: VersionNpmExpression(),
    PackageType.Nuget: VersionNugetExpression(),
    PackageType.Cargo: VersionCargoExpression(),
    PackageType.Go: VersionGoExpression(),
    PackageType.Cocoapods: VersionCocoExpression(),
    PackageType.C: VersionCExpression(),
    PackageType.Ruby: VersionRubyExpression(),
    PackageType.Composer: VersionComposerExpression(),
    PackageType.Hex: VersionHexExpression(),
    PackageType.Nvd: VersionNvdExpression(),
    PackageType.Snyk: VersionSnykExpression(),
    PackageType.Linux: VersionLinuxExpression(),
    PackageType.Other: VersionOtherExpression(),
}

Package_CLASSES = {
    PackageType.Base: Version,
    PackageType.Pip: Version,
    PackageType.Maven: MavenVersion,
    PackageType.Npm: NpmVersion,
    PackageType.Nuget: Version,
    PackageType.Cargo: Version,
    PackageType.Go: GoVersion,
    PackageType.Cocoapods: Version,
    PackageType.C: Version,
    PackageType.Ruby: Version,
    PackageType.Composer: ComposerVersion,
    PackageType.Hex: Version,
    PackageType.Nvd: Version,
    PackageType.Snyk: SnykVersion,
    PackageType.Linux: LinuxVersion,
    PackageType.Other: Version,

}
LJ_VERSION_CLASS = {
    PackageType.Base: LjVersion,
    PackageType.Pip: LjVersion,
    PackageType.Maven: LjVersion,
    PackageType.Npm: LjVersion,
    PackageType.Nuget: LjVersion,
    PackageType.Cargo: LjVersion,
    PackageType.Go: LjVersion,
    PackageType.Cocoapods: LjVersion,
    PackageType.C: LjVersion,
    PackageType.Ruby: LjVersion,
    PackageType.Composer: LjVersion,
    PackageType.Hex: LjVersion,
    PackageType.Nvd: LjVersion,
    PackageType.Snyk: LjVersion,
    PackageType.Linux: LjVersion,
    PackageType.Other: LjVersion,
}


def check_version_in_expression(package_type: str, version_name, version_expression):
    """
    检查版本号是否属于版本表达式
    :param package_type: 包管理器类型
    :param version_name: 版本号
    :param version_expression: 版本表达式
    :return: bool
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    return LJ_VERSION_CLASS[class_package_type](package_type=package_type.lower(),
                                                version_str=version_name).check_version_in_expression(
        version_expression)


def version_compare(package_type: str, version1, version2):
    """
    版本大小比较
    :param package_type: 包管理器类型
    :param version1:
    :param version2:
    :return: 0 相等，1：version1 > version2, -1: version1 < version2, None: 有不符合标准的版本号
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    return LJ_VERSION_CLASS[class_package_type](package_type=package_type.lower()).version_compare(version1, version2)


def get_base_version(package_type=None, version_name=None, is_sort=False):
    """
    格式化版本
    :param package_type: 包管理器类型
    :param version_name: 版本号
    :return: bool
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        class_package_type = PackageType(package_type.lower())
    elif not package_type:
        package_type = "base"
        class_package_type = PackageType(package_type.lower())
    assert class_package_type in Package_CLASSES
    return Package_CLASSES[class_package_type](version_name, package_type.lower(), is_sort)


def is_canonical(package_type: str, version):
    """
    格式化版本
    :param package_type: 包管理器类型
    :param version: 版本号
    :return: bool
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in Package_CLASSES
    if isinstance(version, Version):
        return version.is_canonical(version)
    else:
        return Package_CLASSES[class_package_type](version, package_type.lower()).is_canonical(version)


def change_to_expression(package_type: str, version_expression):
    """
    组件版本表达式转换为版本表达式
    :param package_type: 包管理器类型
    :param version_expression: 组件版本表达式
    :return: 版本表达式
    """
    expression_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            expression_type = PackageType(package_type.lower())
        else:
            expression_type = PackageType.Other
            package_type = "other"
    assert expression_type in Expression_CLASSES
    return Expression_CLASSES[expression_type].change_to_expression(
        package_type.lower(), version_expression
    )


def sort_versions(versions, remove_not_final, package_type="snyk"):
    """
    版本大小比较
    :param package_type: 包管理器类型
    :param versions: 版本列表
    :param remove_not_final: 是否删除列表中的非正式版本
    :return: 从小到大排序的版本列表,version_objs列表
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    return LJ_VERSION_CLASS[class_package_type](package_type=package_type.lower()).sort_versions2(
        versions, remove_not_final
    )


def merge_version_expression(versions_list, is_or, package_type=PackageType.Snyk.value):
    """
    多个表达式合并
    :param versions_list:表达式列表
    :param is_or:是否是或
    :param package_type:包类型
    :return:
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    return LJ_VERSION_CLASS[class_package_type](package_type=package_type).merge_versions_expression(versions_list,
                                                                                                     is_or)


def check_and_sort_versions(package_type: str, versions, version_expression):
    """
    检查版本号是否属于版本表达式
    :param package_type: 包管理器类型
    :param versions: 版本列表
    :param version_expression: 版本表达式
    :return: bool
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    assert isinstance(versions, list)
    final_item = change_to_expression(package_type, version_expression)
    final_list = []
    not_in_list = []
    for i in versions:
        part_bool = LJ_VERSION_CLASS[class_package_type](package_type=package_type.lower(),
                                                         version_str=i).check_version_in_expression(
            final_item)
        if part_bool:
            final_list.append(i)
        else:
            not_in_list.append(i)
    fail_list = []
    if len(final_list) > 1:
        final_list, fail_list = sort_versions(final_list, remove_not_final=False, package_type=package_type)
    fail_list += not_in_list
    return final_list, fail_list, final_item.get_value()


def check_versions_in_expression(package_type: str, versions, version_expression):
    """
    检查版本号是否属于版本表达式
    :param package_type: 包管理器类型
    :param versions: 版本列表
    :param version_expression: 版本表达式
    :return: bool
    """
    class_package_type = None
    if isinstance(package_type, str):
        package_type = MapPackageType.get_value_by_key(package_type)
        if package_type.lower() in PackageType.values():
            class_package_type = PackageType(package_type.lower())
        else:
            class_package_type = PackageType.Other
            package_type = "other"
    assert class_package_type in LJ_VERSION_CLASS
    assert isinstance(versions, list)
    final_item = change_to_expression(package_type, version_expression)
    final_list = []
    for i in versions:
        part_bool = LJ_VERSION_CLASS[class_package_type](package_type=package_type.lower(),
                                                         version_str=i).check_version_in_expression(
            final_item)
        if part_bool:
            final_list.append(i)
    return final_list
