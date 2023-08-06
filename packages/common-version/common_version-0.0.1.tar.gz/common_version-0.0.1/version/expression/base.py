# -*- coding: utf-8 -*-
class VersionExpression:
    def func(self, data):
        return data.group().strip()

    def change_to_lj_expression(self, package_type, version_expression):
        """
        将表达式改变为棱镜表达式
        :param pacage_type: 组件类型
        :param version_expression: 各组件版本表达式
        :return:
        """
        raise NotImplementedError
