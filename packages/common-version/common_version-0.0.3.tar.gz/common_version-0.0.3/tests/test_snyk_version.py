# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression
)


def test_change_to_expression():
    assert "[,1.20.14)||[21.0.0,21.1.2)" == change_to_expression(
        "snyk", "[,1.20.14)||[21.0.0,21.1.2)"
    ).get_value()
    assert "[2.5.0,2.5.17)||[2.6.0,2.6.10)||[2.7.0,2.7.1)" == \
           change_to_expression("snyk", ">= 2.5.0, < 2.5.17 ||>= 2.6.0, < 2.6.10 ||>= 2.7.0, < 2.7.1").get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "snyk", ">=1.0.319, <1.0.474||>=1.1.0, <1.1.11"
    ).get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "snyk", ">=1.0.319, <1.0.474||>=1.1.0, <1.1.11||[1.1.0,1.1.11)"
    ).get_value()
    assert "[1.0.319,1.0.474)||[1.1.0,1.1.11)" == change_to_expression(
        "snyk", ">=1.0.319 <1.0.474||>=1.1.0 <1.1.11||[1.1.0,1.1.11)"
    ).get_value()
    assert "[10.1.1.20.3,]" == change_to_expression("Snyk", "[10.1(1.20.3),]").get_value()
    assert "[,0.7.6_1)" == change_to_expression("snyk", '[0,0.7.5-1+deb8u2)||[0,0.7.6-1+deb9u1)').get_value()
    assert "[8.0_0,8.0_2020_7_1)||[8.1_0,8.1_2020_7_1)||[9_0,9_2020_7_1)||[10_0,10_2020_7_1)" \
           == change_to_expression("snyk",
                                   '[8.0:0,8.0:2020-07-01)||[8.1:0,8.1:2020-07-01)||[9:0,9:2020-07-01)||[10:0,'
                                   '10:2020-07-01)').get_value()
    assert "[,0_5.14.0_162.22.2)" == change_to_expression("snyk", "<0:5.14.0-162.22.2.el9_1").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression(
        "snyk", "1.0.320", "[1.0.319,1.0.474)||[1.1.0,1.1.11)"
    )
