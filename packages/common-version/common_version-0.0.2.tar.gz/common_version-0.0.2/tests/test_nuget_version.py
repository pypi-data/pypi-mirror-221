# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    # -1格式无效
    # assert '[1.0.0,2.9999.9999]' == change_to_expression('nuget', '-1')
    assert "1.1.4" == change_to_expression("nuget", "1.1.4").get_value()
    assert "[1.1.0,1.2.0)" == change_to_expression("nuget", "1.1.*").get_value()
    assert "[1.1.0,1.1.9]" == change_to_expression("nuget", "[1.1.0,1.1.9]").get_value()
    assert "1.1.2" == change_to_expression("nuget", "[1.1.2]").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("nuget", "1.1.4", "1.1.4")
    assert check_version_in_expression("nuget", "1.1.4", "[1.1.0,1.1.9]")
