# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
    check_versions_in_expression
)


def test_change_to_expression():
    assert "[,1.20.14)||[21.0.0,21.1.2)" == change_to_expression(
        "linux", "[,1.20.14)||[21.0.0,21.1.2)"
    ).get_value()
    assert "0.1.0.2" == change_to_expression(
        "linux", "0.1.0~2"
    ).get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "linux", ">=1.0.319, <1.0.474||>=1.1.0, <1.1.11"
    ).get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "linux", ">=1.0.319, <1.0.474||>=1.1.0, <1.1.11||[1.1.0,1.1.11)"
    ).get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "linux", ">=1.0.319 <1.0.474||>=1.1.0 <1.1.11||[1.1.0,1.1.11)"
    ).get_value()

    assert "[,0:5.14.0.162.22.2)" == change_to_expression("linux", "<0:5.14.0-162.22.2.el9_1").get_value()
    assert ['1.1', '2.2'] == check_versions_in_expression(package_type="linux",
                                                          versions=['1.1', "2.2", "6.5", "0:5.15.0"],
                                                          version_expression="[,0:5.14.0.162.22.2)")


def test_version_in_lj_expression():
    assert check_version_in_expression(
        "linux", "1.0.320", "[1.0.319,1.0.474)||[1.1.0,1.1.11)"
    )
