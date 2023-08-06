# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[0.4,1.0)||[2.0,3.0)" == change_to_expression("hex", "~> 0.4 or ~> 2.0").get_value()
    assert "[3.0.0,3.5.0)" == change_to_expression("hex", ">= 3.0.0 and < 3.5.0").get_value()
    assert "[,3.0.0]||(3.5.0,]" == change_to_expression("hex", "<= 3.0.0 or > 3.5.0").get_value()


def test_version_in_lj_expression():
    assert not check_version_in_expression("hex", "0.3", "[0.4,1.0)||[1.0,2.0)")
    assert check_version_in_expression("hex", "0.5", "[0.4,1.0)||[1.0,2.0)")
    assert check_version_in_expression("hex", "3.1.1", "[3.0.0,3.5.0)")
