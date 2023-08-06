# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "1.1.1||1.3.4||6.2.0rc1" == change_to_expression(
        "nvd", "=1.1.1||=1.3.4||=release/6.2.0-rc"
    ).get_value()
    assert "5.0.4rc2||5.0.5||5.0.7||5.0.8" == change_to_expression(
        "nvd", "=5.0.4_pre2||=5.0.7||=5.0.8||=5.0.5"
    ).get_value()
    assert "6.2.0" == change_to_expression("nvd", "=6.2.0").get_value()
    assert not "6.2.0rc1" == change_to_expression("nvd", "release/6.2.0-rc").get_value()


def test_version_in_lj_expression():
    assert not check_version_in_expression(
        "nvd", "release/2.0.5", "5.0.4rc2||5.0.7||5.0.8||5.0.5"
    )
    assert check_version_in_expression("nvd", "v5.0.7", "5.0.4rc2||v5.0.7||5.0.8||5.0.5")
    assert not check_version_in_expression("nvd", "v5.0.7", "5.0.7||5.0.8")
