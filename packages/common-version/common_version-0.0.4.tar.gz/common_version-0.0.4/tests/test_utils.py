# -*- coding: utf-8 -*-
from version.core import utils


def test_hash_key():
    assert utils.gen_hash_key('aa') == 0x371091a9
    assert utils.gen_hash_key('aa', 123) == 0x42f366b7
    assert utils.gen_hash_key('a测试a') == 0x9ba6cdf9


def test_pre_path():
    assert utils.gen_pre_path('aa') == '/mnt/disk/01'
    assert utils.gen_pre_path('-a') == '/mnt/disk/00'
