# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[1.0.0,2.9999.9999]" == change_to_expression(
        "npm", "1.0.0 - 2.9999.9999"
    ).get_value()
    assert "[1.1.0,1.2.0)" == change_to_expression("npm", "1.1.x").get_value()
    assert "[1.0,2.0)" == change_to_expression("npm", "1.x").get_value()
    assert "[6.0.0rc2,7]" == change_to_expression("npm", "6.0.0-rc.2 - 7").get_value()
    assert "[1.1.1,1.2.0)" == change_to_expression("npm", "~1.1.1").get_value()
    assert "[1.0.2,2.1.2)" == change_to_expression("npm", ">=1.0.2 <2.1.2").get_value()
    assert "[1.0.2,]" == change_to_expression("npm", ">=1.0.2").get_value()
    assert "[1.1.12,2.0)" == change_to_expression("npm", "^1.1.12").get_value()
    assert "[,1.0.2]||[1.1.0,1.3.0)||(1.5.0,]" == change_to_expression(
        "npm", "<=1.0.2 || >=1.1.0 <1.3.0 || >1.5.0"
    ).get_value()
    assert "http://asdf.com/asdf.tar.gz" == change_to_expression(
        "npm", "http://asdf.com/asdf.tar.gz"
    ).get_value()


def test_version_in_lj_expression():
    assert not check_version_in_expression(
        "npm", "1.1.1", "http://asdf.com/asdf.tar.gz"
    )
    assert check_version_in_expression(
        "npm", "http://asdf.com/asdf.tar.gz", "http://asdf.com/asdf.tar.gz"
    )
    assert check_version_in_expression("npm", "1.1.1", "[1.0.2,2.1.2)")
    assert check_version_in_expression(
        "npm", "1.0.2", "[,1.0.2]||[1.1.0,1.3.0)||(1.5.0,]"
    )
    assert not check_version_in_expression(
        "npm", "1.0.3", "[,1.0.2]||[1.1.0,1.3.0)||(1.5.0,]"
    )
