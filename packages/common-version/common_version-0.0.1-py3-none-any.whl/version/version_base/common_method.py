# -*- coding: utf-8 -*-
import re


# def sort_version(version_list, package_type=None):
#     from lj_spider_core.version import Version
#     """
#     快速排序
#     version_list  版本列表   排序  从小到大
#     :param version_list:
#     :param package_type:
#     :return:
#     """
#     if len(version_list) <= 1:
#         return version_list
#     pivot = version_list[0]
#     left = [version_list[i] for i in range(1, len(version_list)) if
#             Version(version_list[i], package_type).__cmp__(pivot) == -1]
#     right = [version_list[i] for i in range(1, len(version_list)) if
#              Version(version_list[i], package_type).__cmp__(pivot) > -1]
#     return sort_version(left) + [pivot] + sort_version(right)


def is_match(version_str, regex):
    """
    处理re表达式
    :param version_str:
    :param regex: re表达式
    :return:
    """
    pattern = re.compile(regex)
    match_obj = re.match(pattern, version_str)
    if match_obj:
        re_version = match_obj.group(1)
        return True, re_version
    return False, ""


def get_alpha_index(version):
    """
    得到字母所在下标
    :param version:
    :return:
    """
    pattern = re.compile("[a-zA-Z\\-]")
    match_obj = re.search(pattern, version)
    if match_obj:
        return match_obj.start()
    return -1


def has_alpha(version_str):
    """
    判断是否含有字母
    :param version_str:
    :return:
    """
    flag, _ = is_match(version_str, "[a-zA-Z]")
    return flag


def handle_alpha_num(version):
    """
    删除字母
    :param version:
    :return:
    """
    index = get_alpha_index(version)
    version_num = version[:index]
    return version_num


def remove_char(version):
    pattern = re.compile("[a-zA-Z]")
    new_version = re.sub(pattern, ".", version)
    return new_version
