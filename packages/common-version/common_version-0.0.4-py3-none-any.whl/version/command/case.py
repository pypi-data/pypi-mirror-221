# -*- coding: UTF-8 -*-
"""
@Project:cmdline_test
@File:case.py
@IDE: PyCharm
@Author : hsc
@Date:2022/11/4 16:52
@function：
"""
import json
import click
from version import version_compare, check_version_in_expression, get_base_version, \
    change_to_expression, merge_version_expression, sort_versions, check_versions_in_expression, \
    check_and_sort_versions


@click.group()
def cli():
    pass


@click.command()
@click.option('--package_type', prompt='包类型：', help='包类型')
@click.option('--version1', prompt='版本1：', help='版本1')
@click.option('--version2', prompt='版本2：', help='版本2')
@click.option('--file_path', help='文件路径', default="")
def compare(package_type, version1, version2, file_path):
    """版本大小比较: version_compare"""
    final_data = {
        "success": False
    }
    try:
        flag = version_compare(package_type, version1, version2)
        final_data = {
            "success": True,
            "flag": flag
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--package_type', help='包类型', default="snyk")
@click.option('--version', prompt='须校验版本号：', help='须校验版本号')
@click.option('--version_expression', prompt='版本表达式：', help='版本表达式')
@click.option('--file_path', help='文件路径', default="")
def check(package_type, version, version_expression, file_path):
    """检查版本号是否属于版本表达式:check_version_in_expression"""
    final_data = {
        "success": False
    }
    try:
        flag = check_version_in_expression(package_type=package_type, version_name=version,
                                           version_expression=version_expression)
        final_data = {
            "success": True,
            "flag": flag
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--version', prompt='须校验版本号列表：', help='须校验版本号列表')
@click.argument('version', nargs=-1, required=True)
@click.option('--version_expression', prompt='版本表达式：', help='版本表达式')
@click.option('--package_type', help='包类型', default="snyk")
@click.option('--file_path', help='文件路径', default="")
def checks(package_type, version, version_expression, file_path):
    """检查版本号是否属于版本表达式:check_versions_in_expression"""
    final_data = {
        "success": False
    }
    if isinstance(version, str):
        version = list(eval(version))
    elif isinstance(version, tuple):
        version = list(version)
    else:
        print(json.dumps(final_data))
        return
    try:
        final_list = check_versions_in_expression(package_type=package_type, versions=version,
                                                  version_expression=version_expression)
        final_data = {
            "success": True,
            "final_list": final_list
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--version', prompt='须校验版本号列表：', help='须校验版本号列表')
@click.argument('version', nargs=-1, required=True)
@click.option('--version_expression', prompt='版本表达式：', help='版本表达式')
@click.option('--package_type', help='包类型', default="snyk")
@click.option('--file_path', help='文件路径', default="")
def checks_and_sort(package_type, version, version_expression, file_path):
    """检查版本号是否属于版本表达式:check_and_sort_versions"""
    final_data = {
        "success": False
    }
    if isinstance(version, str):
        version = list(eval(version))
    elif isinstance(version, tuple):
        version = list(version)
    else:
        print(json.dumps(final_data))
        return
    try:
        sort_list, fail_list = check_and_sort_versions(package_type=package_type, versions=version,
                                                       version_expression=version_expression)
        final_data = {
            "sort_versions": sort_list,
            "fail_versions": fail_list,
            "success": True
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--package_type', prompt='包类型：', help='包类型')
@click.option('--version', prompt='需要格式化的版本：', help='需要格式化的版本')
@click.option('--file_path', help='文件路径', default="")
def to_format(package_type, version, file_path):
    """格式化版本: get_base_version"""
    final_data = {
        "success": False
    }
    try:
        version_obj = get_base_version(package_type, version)
        version_format = version_obj.new_version
        final_data = {
            "success": True,
            "version_format": version_format
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--package_type', prompt='包类型：', help='包类型')
@click.option('--version_exp', prompt='原始版本表达式：', help='原始版本表达式')
@click.option('--file_path', help='文件路径', default="")
def change(package_type, version_exp, file_path):
    """组件版本表达式转换为版本表达式: change_to_expression"""
    final_data = {
        "success": False
    }
    try:
        version_item = change_to_expression(package_type, version_exp)
        version = version_item.get_value()
        final_data = {
            "success": True,
            "version": version
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--package_type', prompt='包类型：', help='包类型')
@click.option('--version_list', prompt='版本表达式列表：', help='版本表达式列表')
@click.option('--is_or', prompt='或关系为1 ,且关系为其他：', help='或关系为1 ,且关系为其他')
@click.option('--file_path', help='文件路径', default="")
def merge(package_type, version_list, is_or, file_path):
    """合并多个版本表达式多个表达式合并: merge"""
    final_data = {
        "success": False
    }
    if is_or == "1":
        is_or = True
    else:
        is_or = False
    try:
        final_versions = merge_version_expression(version_list, is_or=is_or, package_type=package_type)
        version = final_versions.get_value()
        final_data = {
            "success": True,
            "version": version
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.option('--package_type', prompt='包类型：', help='包类型')
@click.option('--versions', prompt='版本列表：', help='版本列表')
@click.option('--file_path', help='文件路径', default="")
@click.option('--is_remove', prompt='是否删除列表中的非正式版本,删除为1，不删除为其他：', help='是否删除列表中的非正式版本,删除为1，不删除为其他')
def sort(package_type, versions, is_remove, file_path):
    """版本列表大小排序: sort_versions"""
    final_data = {
        "success": False
    }
    if is_remove == "1":
        is_remove = True
    else:
        is_remove = False
    try:
        success_versions, fail_versions = sort_versions(package_type=package_type, versions=versions,
                                                        remove_not_final=is_remove)
        final_data = {
            "success": True,
            "sort_versions": success_versions,
            "fail_versions": fail_versions
        }
    except Exception:
        pass
    finally:
        data = json.dumps(final_data)
        if not file_path:
            print(data)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)


@click.command()
@click.argument('open_file', type=click.File('rb'), default='-')
@click.option('--file_path', help='文件路径', default="")
def change_and_check_sort(open_file, file_path):
    final_data = []
    r_versions = open_file.read()
    versions = json.loads(r_versions)
    if not isinstance(versions, list):
        versions = [versions]
    for part_check in versions:
        part_dict = dict()
        part_dict['sort_versions'] = ""
        version = part_check.get("version", [])
        package_type = part_check.get("package_type", "")
        package_name = part_check.get("package_name", "")
        version_exp = part_check.get("version_exp", "")
        part_dict['package_type'] = package_type
        part_dict['package_name'] = package_name
        part_dict['version_exp'] = version_exp
        part_dict['lj_version_exp'] = ""
        try:
            try:
                sort_list, _, version_expression = check_and_sort_versions(package_type=package_type, versions=version,
                                                                           version_expression=version_exp)
                part_dict['lj_version_exp'] = version_expression
                part_dict['sort_versions'] = sort_list
            except Exception:
                pass
        except Exception:
            pass
        final_data.append(part_dict)
    if not isinstance(versions, list) and final_data:
        final_data = final_data[0]
    data = json.dumps(final_data)
    if not file_path:
        print(data)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)


cli.add_command(check)
cli.add_command(checks)
cli.add_command(change)
cli.add_command(compare)
cli.add_command(merge)
cli.add_command(sort)
cli.add_command(checks_and_sort)
cli.add_command(to_format)
cli.add_command(change_and_check_sort)

if __name__ == "__main__":
    cli()
