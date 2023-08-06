# -*- coding: utf-8 -*-
from version import (
    change_to_expression,
    check_version_in_expression,
)


def test_change_to_expression():
    assert "[1.2,2.0)" == change_to_expression("pip", "~=1.2").get_value()
    assert "1.2.0" == change_to_expression("pip", "===1.2.0").get_value()
    assert "[1.2.0,1.3.0)" == change_to_expression("pip", "==1.2.*").get_value()
    assert "[,1.9.0)||[1.10.0,]" == change_to_expression("pip", "!=1.9.*").get_value()
    assert "[,1.2.1.post1)" == change_to_expression("pip", "<1.2.1.post").get_value()
    assert "[,1.2.1a1)" == change_to_expression("pip", "<1.2.1.a").get_value()
    assert "[1.2.0,1.3.0)" == change_to_expression("pip", ">=1.2.0,<1.3.0").get_value()
    assert "[,1.2.3)||(1.2.3,]" == change_to_expression("pip", "!=1.2.3").get_value()
    assert "(1.2,1.2.3)||(1.2.3,]" == change_to_expression(
        "pip", ">1.1,!=1.2.3,>1.2"
    ).get_value()
    assert "(1.1,1.2.3)||(1.2.3,1.5)" == change_to_expression(
        "pip", ">1.1,!=1.2.3,<1.5"
    ).get_value()


def test_version_in_lj_expression():
    assert check_version_in_expression("pip", "1.1.4", "[,1.2.3)||(1.2.3,]")
    assert not check_version_in_expression("pip", "1.2.3", "(,1.2.1.post1)")
