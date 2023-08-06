# -*- coding: utf-8 -*-
class VersionBase:
    def check_version_expression(self, version_expression):
        """
        检查版本表达式是否合法
        :param version_expression: 版本表达式
        :return: bool
        """
        raise NotImplementedError

    def check_version_in_expression(self, version_name, version_expression):
        """
        检查版本号是否属于版本表达式
        :param version_name: 版本号
        :param version_expression: 版本表达式
        :return: bool
        """
        raise NotImplementedError
