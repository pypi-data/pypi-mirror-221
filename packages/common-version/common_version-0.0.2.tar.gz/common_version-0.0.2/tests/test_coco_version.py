# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[1.1.1,1.2.0)" == change_to_expression("cocoapods", "~> 1.1.1").get_value()
    assert "[1.1.1,]" == change_to_expression("cocoapods", ">= 1.1.1").get_value()
    assert "1.1.1" == change_to_expression("cocoapods", "1.1.1").get_value()
    assert "*" == change_to_expression("cocoapods", "").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("cocoapods", "1.1.2", "[1.1.1,1.2.0)")
    assert check_version_in_expression("cocoapods", "1.1.0", "1.1")
    assert check_version_in_expression("cocoapods", "1.1.0", "*")
