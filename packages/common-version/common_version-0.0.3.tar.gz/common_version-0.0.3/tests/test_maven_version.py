# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[,1.2.0)||(1.3.0,]" == change_to_expression("maven", "[,1.2.0),(1.3.0,]").get_value()
    assert "[3.5,3.16b1]" == change_to_expression("maven", "[3.5,)(,3.16-beta1]").get_value()
    assert "1.0" == change_to_expression("maven", "1.0").get_value()
    assert "1.0" == change_to_expression("maven", "[1.0]").get_value()
    assert "1.0b2" == change_to_expression("maven", "[1.0-beta2]").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("maven", "1.1.1", "1.1.1")
    assert check_version_in_expression("maven", "1.1.1", "[,1.2.0)||(1.3.0,]")
    assert not check_version_in_expression("maven", "1.2.1", "[,1.2.0)||(1.3.0,]")
