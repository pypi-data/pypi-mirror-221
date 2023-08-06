# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[2.0.0,3.0.0)||(3.0.0,3.0.1)||(3.0.1,3.1.0)" == \
           change_to_expression("Other", "!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0").get_value()
    assert "[0.1.0,0.2.0)" == change_to_expression("Other", "0.1.*").get_value()
    assert "[0.1,1.0)" == change_to_expression("Other", "^0.1").get_value()
    assert "[0.1,1.0)" == change_to_expression("Other", "~0.1").get_value()
    assert "(0.1,]" == change_to_expression("Other", "~>0.1").get_value()
    assert '[,3.0.0)||(3.0.0,3.0.1)||(3.0.1,]' == change_to_expression("Other", "!=3.0.0,!=3.0.1").get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("c", "1.1.2", "[1.1.1,]")
    assert not check_version_in_expression("c", "1.1.1.a", "[1.1.1,)")
    assert check_version_in_expression("c", "1.1.1.post1", "[1.1.1,)")
    assert check_version_in_expression("c", "1.1.1", "1.1.1")
