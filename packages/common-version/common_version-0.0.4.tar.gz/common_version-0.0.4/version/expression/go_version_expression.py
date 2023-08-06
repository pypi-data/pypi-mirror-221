# -*- coding: utf-8 -*-
from abc import ABC

from version.expression.base import VersionExpression
from version.version_base import Item


class VersionGoExpression(VersionExpression, ABC):
    def change_to_expression(self, package_type, version_expression):
        # version_expression = chinese_to_english_version(version_expression)
        if version_expression:
            version_item = Item(left_open=True, right_open=True, left=version_expression, right=version_expression)
        else:
            version_item = Item(left_open=True, right_open=True, left="", right="")
        return version_item
