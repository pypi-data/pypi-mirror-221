# -*- coding: utf-8 -*-
import re

from version.version_base import VersionSort

sort_values = []
for i in VersionSort.__members__.values():
    sort_values.append(i.values[0])


def fun(mat):
    groups = mat.groups()
    final_list = [i.replace(" ", "") for i in groups]
    return "".join(final_list)


def chinese_to_english_version(version):
    version = version.replace("＝", '=')
    version = version.replace("～", '~')
    version = version.replace("ˆ", '^')
    version = version.replace("⁰", '0')
    version = version.replace("¹", '1')
    version = version.replace("²", '2')
    version = version.replace("³", '3')
    version = version.replace("⁴", '4')
    version = version.replace("⁵", '5')
    version = version.replace("⁶", '6')
    version = version.replace("⁷", '7')
    version = version.replace("⁸", '8')
    version = version.replace("⁹", '9')
    version = version.replace("（", '(')
    version = version.replace("）", ')')
    version = version.replace("【", '[')
    version = version.replace("】", ']')
    version = version.replace("｜", "|")
    return version


def arrangement_version(
        version,
        package_type,
        is_del_identifier=False,
        is_format=True,
        is_del_brackets=False,
):
    from version import get_base_version
    """
    版本号格式化
    is_del_identifier 是否删除其他标识符  例如：> < = !
    :param is_format:
    :param package_type: 包类型
    :param version:
    :param is_del_identifier:
    :return:
    """
    if is_del_identifier:
        version = version.replace(" ", "")
        version = version.replace("=", "")
        version = version.replace(">", "")
        version = version.replace("<", "")
        version = version.replace("!", "")
    if is_del_brackets:
        version = version.replace("[", "")
        version = version.replace("(", "")
        version = version.replace("]", "")
        version = version.replace(")", "")
    # if package_type == PackageType.Npm.value:
    #     version = version.replace("-", ".")

    if is_format:
        version = get_base_version(package_type, version)
    return version


def compare_str_by_dict_val(source_str, dest_str):
    """
    带有字母部分进行比较
    :param source_str:
    :param dest_str:
    :return:
    """
    flag = 0
    dest_val_tup = VersionSort("other").values
    source_val_tup = VersionSort("other").values
    try:
        if dest_str in sort_values and source_str in sort_values:
            source_val_tup = VersionSort(source_str).values
            source_val = source_val_tup[1]
            dest_val_tup = VersionSort(dest_str).values
            dest_val = dest_val_tup[1]
            if source_val > dest_val:
                flag = 1
            elif source_val < dest_val:
                flag = -1
        elif dest_str not in sort_values and source_str in sort_values:
            dest_val = dest_val_tup[1]
            source_val_tup = VersionSort(source_str).values
            source_val = source_val_tup[1]
            if source_val > dest_val:
                flag = 1
            elif source_val < dest_val:
                flag = -1
        elif dest_str not in sort_values and source_str not in sort_values:
            compare_source = source_val_tup
            compare_dest = dest_val_tup
            try:
                source_int = int(source_str)
                compare_source = source_int
            except Exception:
                pass
            try:
                dest_int = int(dest_str)
                compare_dest = dest_int
            except Exception:
                pass
            if compare_source == compare_dest and compare_dest == VersionSort("other").values:
                compare_source = source_str
                compare_dest = dest_str
            if compare_source == compare_dest:
                flag = 0
            elif compare_source > compare_dest:
                flag = 1
            elif compare_source < compare_dest:
                flag = -1
        else:
            source_val = source_val_tup[1]
            dest_val_tup = VersionSort(dest_str).values
            dest_val = dest_val_tup[1]
            if source_val > dest_val:
                flag = 1
            elif source_val < dest_val:
                flag = -1
    except Exception:
        flag = -1
    return flag


def compare_str(version_source_str_list, version_dest_str_list):
    """
    带有字符串的比较的大小判断逻辑
    1  大于
    0  等于
    -1 小于
    :param version_source_str_list:
    :param version_dest_str_list:
    :return:
    """
    flag = 0
    min_len = min(len(version_source_str_list), len(version_dest_str_list))
    if len(version_source_str_list) == min_len:
        version_source_str_list = version_source_str_list + [
            0 for i in range(len(version_dest_str_list) - min_len)
        ]
    if len(version_dest_str_list) == min_len:
        version_dest_str_list = version_dest_str_list + [
            0 for i in range(len(version_source_str_list) - min_len)
        ]
    for i in range(len(version_dest_str_list)):
        try:
            int_source = int(version_source_str_list[i])
            int_dest = int(version_dest_str_list[i])
            if int_source > int_dest:
                flag = 1
            elif int_source < int_dest:
                flag = -1
        except Exception:
            flag = compare_str_by_dict_val(
                version_source_str_list[i], version_dest_str_list[i]
            )
        finally:
            if flag == 1 or flag == -1:
                break
    return flag


def version_str_change_list(version_dest):
    """
    切割字母
    :param version_source:
    :param version_dest:
    :return:
    """
    pattern = re.compile(r"([a-z]+)")
    if isinstance(version_dest, str):
        dest_res = re.findall(pattern, version_dest)
        if dest_res:
            version_dest_list = version_dest.split(dest_res[0])
            if version_dest_list[0] and version_dest_list[-1]:
                return [version_dest_list[0], dest_res[0]] + version_str_change_list(
                    version_dest[len(version_dest_list[0]) + len(dest_res[0]):]
                )
            elif version_dest_list[0] and not version_dest_list[-1]:
                return [version_dest_list[0], dest_res[0]]
            else:
                return [dest_res[0]] + version_str_change_list(
                    version_dest[len(version_dest_list[0]) + len(dest_res[0]):]
                )
        else:
            version_dest_str_list = [version_dest]
            return version_dest_str_list
    else:
        return [version_dest]


def compare_str_change_list(version_source, version_dest):
    """
    带字母的比较入口函数
    :param version_source:
    :param version_dest:
    :return:
    """
    version_source_str_list = version_str_change_list(version_source)
    version_dest_str_list = version_str_change_list(version_dest)
    flag = compare_str(version_source_str_list, version_dest_str_list)
    return flag


def supplement_zero(version_source_list, version_dest_list):
    """
    等于、不等于时的补零操作
    :param version_source_list:
    :param version_dest_list:
    :return:
    """
    if len(version_source_list) < len(version_dest_list):
        for i in range(len(version_dest_list) - len(version_source_list)):
            version_source_list.append("0")
    else:
        for i in range(len(version_source_list) - len(version_dest_list)):
            version_dest_list.append("0")
    return version_source_list, version_dest_list


def base_greater(version_source_list, version_dest_list):
    """
    大于、大于等于逻辑比较部分
    :param version_source_list:
    :param version_dest_list:
    :return:
    """
    flag = True
    equal_num = 0
    min_len = min(len(version_source_list), len(version_dest_list))
    version_source_list, version_dest_list = supplement_zero(
        version_source_list, version_dest_list
    )
    for i in range(0, len(version_source_list)):
        # 验证
        pattern = re.compile(r"([a-z]+)")
        dest_res = re.findall(pattern, version_dest_list[i])
        source_res = re.findall(pattern, version_source_list[i])
        if not dest_res and not source_res:
            if not version_source_list[i]:
                version_source_list[i] = "0"
            version_source_i = int(version_source_list[i])
            if not version_dest_list[i]:
                version_dest_list[i] = '0'
            version_dest_i = int(version_dest_list[i])
            if version_source_i > version_dest_i:
                for j in range(0, i):
                    j_dest_res = re.findall(pattern, version_dest_list[j])
                    j_source_res = re.findall(pattern, version_source_list[j])
                    if not j_source_res and not j_dest_res:
                        version_source_j = int(version_source_list[j])
                        version_dest_j = int(version_dest_list[j])
                        if version_source_j < version_dest_j:
                            flag = False
                            break
                    else:
                        new_flag = compare_str_change_list(
                            version_source_list[j], version_dest_list[j]
                        )
                        if new_flag == -1:
                            flag = False
                            break
                if flag:
                    break
            elif version_source_i < version_dest_i:
                flag = False
                break
            elif version_source_i == version_dest_i:
                equal_num += 1
        else:
            new_flag = compare_str_change_list(
                version_source_list[i], version_dest_list[i]
            )
            if new_flag == 1:
                flag = True
            elif new_flag == -1:
                flag = False
            else:
                equal_num += 1
    return equal_num, min_len, flag


def base_less(version_source_list, version_dest_list):
    """
    小于、小于等于逻辑代码
    :param version_source_list:
    :param version_dest_list:
    :return:
    """
    flag = True
    equal_num = 0
    min_len = min(len(version_source_list), len(version_dest_list))
    version_source_list, version_dest_list = supplement_zero(
        version_source_list, version_dest_list
    )
    for i in range(0, len(version_source_list)):
        # 验证
        pattern = re.compile(r"([a-z]+)")
        dest_res = re.findall(pattern, version_dest_list[i])
        source_res = re.findall(pattern, version_source_list[i])
        if not dest_res and not source_res:
            version_source_i = int(version_source_list[i])
            version_dest_i = int(version_dest_list[i])
            if version_source_i < version_dest_i:
                for j in range(0, i):
                    j_dest_res = re.findall(pattern, version_dest_list[j])
                    j_source_res = re.findall(pattern, version_source_list[j])
                    if not j_dest_res and not j_source_res:
                        version_source_j = int(version_source_list[j])
                        version_dest_j = int(version_dest_list[j])
                        if version_source_j > version_dest_j:
                            flag = False
                            break
                    else:
                        new_flag = compare_str_change_list(
                            version_source_list[i], version_dest_list[i]
                        )
                        if new_flag == 1:
                            flag = False
                            break
                if flag:
                    break
            elif version_source_i > version_dest_i:
                flag = False
                break
            elif version_source_i == version_dest_i:
                equal_num += 1
        else:
            new_flag = compare_str_change_list(
                version_source_list[i], version_dest_list[i]
            )
            if new_flag == -1:
                flag = True
            elif new_flag == 1:
                flag = False
            else:
                equal_num += 1
    return equal_num, min_len, flag


def cut_version_with_comma(version_dest):
    """
    以,切割版本 例如 [,1.2.3),(1.2.3,],[1.3.0,]
                    返回 ['[,1.2.3)', '(1.2.3,]', '[1.3.0,]']
    :param version_dest:
    :return:
    """
    pos = version_dest.find(",")
    previous_pos = 0
    count = 0
    version_dest_list = []
    while pos != -1:
        count = count + 1
        if count % 2 == 0:
            if previous_pos == 0:
                version_dest_list.append(version_dest[previous_pos:pos])
            else:
                version_dest_list.append(version_dest[previous_pos + 1: pos])
            previous_pos = pos
        pos = version_dest.find(",", pos + 1)
        if pos == -1 and previous_pos != 0:
            if version_dest[previous_pos + 1:]:
                version_dest_list.append(version_dest[previous_pos + 1:])
        elif pos == -1 and previous_pos == 0:
            if version_dest[previous_pos:]:
                version_dest_list.append(version_dest[previous_pos:])
    return version_dest_list


# def compare_version_size(left_version, right_version, package_type=None):
#     from version.version_base import Version
#     """
#     比较两个版本的大小
#         1 大于
#         0 等于
#         -1 小于
#     :param left_version:左边版本
#     :param right_version:右边版本
#     :return:
#     """
#     flag_num = 0
#     left_version_list = []
#     right_version_list = []
#     if package_type is not None:
#         left_version = arrangement_version(left_version, package_type)
#         right_version = arrangement_version(right_version, package_type)
#     if isinstance(left_version, Version):
#         left_version = left_version.new_version
#     if isinstance(right_version, Version):
#         right_version = right_version.new_version
#     if left_version:
#         left_version_list = left_version.split(".")
#     if right_version:
#         right_version_list = right_version.split(".")
#     if left_version_list:
#         _, _, greater_flag = base_greater(left_version_list, right_version_list)
#     else:
#         greater_flag = True
#     if right_version_list:
#         _, _, less_flag = base_less(left_version_list, right_version_list)
#     else:
#         less_flag = True
#     if greater_flag and not less_flag:
#         flag_num = 1
#     if less_flag and not greater_flag:
#         flag_num = -1
#     return flag_num


def handle_version_compatible(version_dest, package_type):
    from version.version_base import Item, Version
    from version import PackageType
    """
    此函数用于处理   获取大于当前版本的最小版本
    :param package_type:包类型
    :param version_dest: 版本表达式
    :return:Item()
    """
    if package_type == PackageType.Npm.value:
        if "~" in version_dest:
            version_dest = version_dest.split("~")[1]
        else:
            version_dest = version_dest.replace("x", "0")
    elif package_type == PackageType.C.value:
        version_dest = version_dest.replace(" ", "")
        if "~=" in version_dest:
            version_dest = version_dest.split("~=")[1]
    elif package_type == PackageType.Cargo.value:
        version_dest = version_dest.replace(" ", "")
        if "~" in version_dest:
            version_dest = version_dest.split("~")[1]
        if "*" in version_dest:
            version_dest = version_dest.replace("*", "0")
        if "^" in version_dest:
            version_dest = version_dest.split("^")[1]
    elif package_type == PackageType.Other.value:
        version_dest = version_dest.replace(" ", "")
        if "~" in version_dest and "~>" not in version_dest:
            version_dest = version_dest.split("~")[1]
        if "~>" in version_dest:
            version_dest = version_dest.split("~>")[1]
        if "*" in version_dest:
            version_dest = version_dest.replace("*", "0")
        if "^" in version_dest:
            version_dest = version_dest.split("^")[1]
    elif package_type == PackageType.Nuget.value:
        version_dest = version_dest.replace("*", "0")
    elif package_type == PackageType.Snyk.value:
        if "~" in version_dest:
            version_dest = version_dest.split("~")[1]
    elif package_type == PackageType.Cocoapods.value:
        version_dest = version_dest.replace(" ", "")
        if "~>" in version_dest:
            version_dest = version_dest.split("~>")[1]
    elif package_type == PackageType.Composer.value:
        if "^" in version_dest:
            version_dest = version_dest.split("^")[1]
        elif "~" in version_dest:
            version_dest = version_dest.split("~")[1]
        version_dest = version_dest.replace("x", "0")
    elif package_type == PackageType.Hex.value:
        version_dest = version_dest.replace(" ", "")
        if "~>" in version_dest:
            version_dest = version_dest.split("~>")[1]
    elif package_type == PackageType.Pip.value:
        version_dest = version_dest.replace(" ", "")
        version_dest = version_dest.split("~=")[1]
    elif package_type == PackageType.Ruby.value:
        version_dest = version_dest.replace(" ", "")
        if "~>" in version_dest:
            version_dest = version_dest.split("~>")[1]
    version_dest = arrangement_version(
        version_dest, package_type, is_del_identifier=True
    )
    if isinstance(version_dest, Version):
        max_version = version_dest.max_version_calculation(version_dest.new_version)
        version_item = Item(
            left_open=True, left=version_dest.new_version, right_open=False, right=max_version
        )
    else:
        max_version = Version.max_version_calculation(version_dest)
        version_item = Item(
            left_open=True, left=version_dest, right_open=False, right=max_version
        )
    return version_item


def dest_change_source(version_dest):
    from version.version_base import Item

    """
    大于、大于等于、小于、小于等于逻辑范围
    :param package_type:
    :param version_dest:
    :return:
    """
    version_dest = version_dest.replace(" ", "")
    new_item = Item(valid=False)
    if ">" in version_dest:
        if ">=" in version_dest:
            version_dest = version_dest.split(">=")[1]
            new_item = Item(
                left_open=True, left=version_dest, right_open=True, right=""
            )
        else:
            version_dest = version_dest.split(">")[1]
            new_item = Item(
                left_open=False, left=version_dest, right_open=True, right=""
            )
    if "<" in version_dest:
        if "<=" in version_dest:
            version_dest = version_dest.split("<=")[1]
            new_item = Item(
                left_open=False, left="", right_open=True, right=version_dest
            )
        else:
            version_dest = version_dest.split("<")[1]
            new_item = Item(
                left_open=True, left="", right_open=False, right=version_dest
            )
    return new_item


def find_str_index(version, msg):
    """
    主要作用  递归删除 npm表达式中 >= 4.1.1之后的空格
    :param version:
    :param msg:
    :return:
    """
    msg_index = version.find(msg)
    pattern = re.compile(r"^\d.*")
    if msg_index != -1:
        res_count = re.match(pattern, version[msg_index + len(msg):])
        if res_count:
            return version[:msg_index] + find_str_index(
                version[msg_index + len(msg):], msg
            )
        else:
            return version[: msg_index + len(msg)] + find_str_index(
                version[msg_index + len(msg):], msg
            )
    else:
        return version


def handle_version_change_source(version_dest, package_type):
    from version.version_base import Version

    """
    小于等于逻辑、大于等于逻辑、大于逻辑、小于逻辑
    :param package_type:
    :param version_dest:
    :return:
    """
    version_dest = arrangement_version(version_dest, package_type, is_del_identifier=False)
    if isinstance(version_dest, Version):
        version_item = dest_change_source(version_dest.new_version)
    else:
        version_item = dest_change_source(version_dest)
    return version_item


def find_left_or_right_identifier(version):
    """
    判断左右开闭区间
    例如：
        >= ---> True
        > ---> False
        <= ---> True
        < ---> Falsee
    :param version:
    :return:
    """
    left_open = None
    right_open = None
    if ">" in version:
        if "=" in version:
            left_open = True
        else:
            left_open = False
    if "<" in version:
        if "=" in version:
            right_open = True
        else:
            right_open = False
    if "[" in version:
        left_open = True
    elif "(" in version:
        left_open = False
    if "]" in version:
        right_open = True
    elif ")" in version:
        right_open = False
    return left_open, right_open


def get_cut_version_item(left_open, right_open, format_version, is_left=True):
    from version.version_base import Item, Version

    if left_open is None:
        if isinstance(format_version, Version):
            right = format_version.new_version
        else:
            right = format_version
        final_item = Item(
            left_open=True,
            left="",
            right_open=right_open,
            right=right,
        )
    else:
        if isinstance(format_version, Version):
            left = format_version.new_version
        else:
            left = format_version
        if is_left:
            final_item = Item(
                left_open=left_open, left=left, right_open=right_open, right=""
            )
        else:
            final_item = Item(
                left_open=left_open, left="", right_open=right_open, right=left
            )
    return final_item


def cut_not_in(left_version, right_version, package_type):
    from version.version_base import Item
    from version import get_base_version
    left_item = Item(valid=False)
    right_item = Item(valid=False)
    if len(left_version) > 1:
        format_left_version = get_base_version(package_type, left_version[1:])
        if len(right_version) == 1:
            final_version = left_version + "," + right_version
        elif len(right_version) > 1:
            final_version = left_version + ",]"
        else:
            final_version = left_version
        left_open, right_open = find_left_or_right_identifier(final_version)
        left_item = get_cut_version_item(left_open, right_open, format_left_version)
    if len(right_version) > 1:
        # format_right_version = change_to_expression(package_type, right_version[:-1]).get_value()
        format_right_version = get_base_version(package_type, right_version[:-1])
        if len(left_version) == 1:
            final_version = left_version + "," + right_version
        elif len(left_version) > 1:
            final_version = "[," + right_version
        else:
            final_version = right_version
        other_left_open, other_right_open = find_left_or_right_identifier(final_version)
        right_item = get_cut_version_item(other_left_open, other_right_open, format_right_version,
                                          is_left=False)
    if len(left_version) == 1 and len(right_version) == 1:
        new_item = Item(left_open=True, left="", right_open=True, right="")
    else:
        if left_item.valid and right_item.valid:
            new_item = Item(
                left_open=left_item.left_open,
                right_open=right_item.right_open,
                left=left_item.left,
                right=right_item.right
            )
            # new_item = ItemGroup(right_item, left_item, is_or=False).merge()
            # new_item = right_item.is_intersect2(left_item, is_or=False)
        elif left_item.valid and not right_item.valid:
            new_item = left_item
        else:
            new_item = right_item
    return new_item


def cut_left_and_right_dest(version_dest_list, package_type):
    from version.version_base import ItemGroup
    """
    比较大小取交集
    仅适用与 ['>1','<2]此种情况
    :param version_dest_list:
    :return:
    """
    left_version = version_dest_list[0].replace(" ", "")
    right_version = version_dest_list[1].replace(" ", "")

    if (">" and "<" and "=") not in left_version and (">" and "<" and "=") not in right_version:
        new_item = cut_not_in(left_version, right_version, package_type)
    else:
        left_item = handle_version_change_source(left_version, package_type)
        right_item = handle_version_change_source(right_version, package_type)
        new_item = ItemGroup(left_item, right_item, is_or=False).merge()
    return new_item


def handle_version_or(version_dest, package_type):
    from version.version_base import Item, Version

    """
    :param version_dest:
    :return:
    """
    left_open, right_open = find_left_or_right_identifier(version_dest)
    new_version_dest = arrangement_version(
        version_dest, package_type, is_del_identifier=True
    )
    if isinstance(new_version_dest, Version):
        new_version_dest = new_version_dest.new_version
    if left_open is not None:
        version_item = Item(
            left_open=left_open, right_open=True, left=new_version_dest, right=""
        )
    else:
        version_item = Item(
            left_open=True, right_open=right_open, right=new_version_dest, left=""
        )
    return version_item


def handle_version_comma(version_dest, package_type):
    from version.version_base import Item
    from version import PackageType
    """
    比较左右大小 取交集
    :param package_type:
    :param version_dest:
    :return:
    """
    version_dest = version_dest.strip(" ")
    new_item = Item(valid=False)
    versions = []
    if package_type == PackageType.Composer.value or package_type == PackageType.Npm.value:
        versions = version_dest.split(" ")
    elif package_type == PackageType.Nuget.value:
        versions = version_dest.split(",")
    if versions:
        new_item = cut_left_and_right_dest(versions, package_type)
    return new_item


def get_equal_item(version_expression, package_type, is_del_brackets=False):
    from version.version_base import Version, Item

    format_version_dest = arrangement_version(
        version_expression, package_type, is_del_identifier=True, is_del_brackets=is_del_brackets
    )
    if isinstance(format_version_dest, Version):
        if format_version_dest.new_version:
            format_version = format_version_dest.new_version
        else:
            format_version = format_version_dest.old_version
    else:
        format_version = format_version_dest
    version_item = Item(
        left_open=True,
        left=format_version,
        right_open=True,
        right=format_version,
    )
    return version_item
