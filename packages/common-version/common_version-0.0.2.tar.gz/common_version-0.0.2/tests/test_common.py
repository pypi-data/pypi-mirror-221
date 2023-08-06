# -*- coding: utf-8 -*-
from version import get_base_version, is_canonical, sort_versions


def test_version_format_version():
    assert "1.2.4" == get_base_version("c", "1.2.4").new_version
    assert "1.2.1a1" == get_base_version("c", "1.2.1.a").new_version
    assert "1.2.1b1" == get_base_version("c", "1.2.1.b").new_version
    assert "1.2.1rc1" == get_base_version("c", "1.2.1.rc").new_version
    assert "1.2.1.dev1" == get_base_version("c", "1.2.1.dev").new_version
    assert "1.2.1.post1" == get_base_version("c", "1.2.1.post").new_version
    assert "1.2.4" == get_base_version("c", "1.2.4").new_version


def test_version_is_canonical():
    assert is_canonical("c", "1.2.4")
    assert is_canonical("c", "1.2.4a1")
    assert is_canonical("c", "1.2.4.post1")


def test_version_sort_versions():
    s, _ = sort_versions(
        ["1.2.3", "1.1.2", "1.2.a", "1.2.3.post"], True
    )
    f, _ = sort_versions(
        ["1.2.3", "1.1.2", "1.2.a", "1.2.3.post"], False
    )
    assert ['1.1.2', '1.2.3', '1.2.3.post'] == s
    assert ['1.1.2', '1.2.a', '1.2.3', '1.2.3.post'] == f
