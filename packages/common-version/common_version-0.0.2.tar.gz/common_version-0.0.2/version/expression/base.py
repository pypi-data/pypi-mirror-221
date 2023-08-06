# -*- coding: utf-8 -*-
class VersionExpression:
    @staticmethod
    def func(data):
        return data.group().strip()

    def change_to_expression(self, package_type, version_expression):
        """
        将表达式改变为通用版本表达式
        :param package_type: 组件类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        raise NotImplementedError
