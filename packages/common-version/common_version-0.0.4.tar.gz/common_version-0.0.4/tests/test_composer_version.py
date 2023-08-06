# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[1.1.1,]" == change_to_expression("composer", ">=1.1.1").get_value()
    assert "1.1.1" == change_to_expression("composer", "1.1.1").get_value()
    assert "[10.4,11.0)||[11.5,12.0)" == change_to_expression(
        "composer", "^10.4 || ^11.5"
    ).get_value()
    assert "[1.0,2.0)" == change_to_expression("composer", "^1.0").get_value()
    assert "4.0.0.dev1" == change_to_expression("composer", "4.0.x-dev").get_value()
    assert "dev-develop||dev-master||[1.0.0,1.1.0)" == \
           change_to_expression("composer", "^1.0.0 || dev-master || dev-develop").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("composer", "1.1.2", "[1.1.1,1.2.0)")
    assert check_version_in_expression("composer", "1.1", "1.1")
    assert check_version_in_expression("composer", "10.5", "[10.4,11.0)||[11.5,12.0)")
    assert check_version_in_expression("composer", "11.6", "[10.4,11.0)||[11.5,12.0)")
