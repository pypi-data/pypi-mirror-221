# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "1.0.2" == change_to_expression("go", "1.0.2").get_value()
    assert "1.1.1" == change_to_expression("go", "1.1.1").get_value()
    assert "http://asdf.com/asdf.tar.gz" == change_to_expression(
        "go", "http://asdf.com/asdf.tar.gz"
    ).get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("go", "1.1.1", "1.1.1")
    assert not check_version_in_expression("go", "1.1.1", "http://asdf.com/asdf.tar.gz")
    assert check_version_in_expression(
        "go", "http://asdf.com/asdf.tar.gz", "http://asdf.com/asdf.tar.gz"
    )
