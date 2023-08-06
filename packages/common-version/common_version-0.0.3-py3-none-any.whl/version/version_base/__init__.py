# -*- coding: utf-8 -*-
from .base_item import Item, ItemGroup
from .base_version import Version, VersionSort
from .composer_version import ComposerVersion
from .go_version import GoVersion
from .lj_version import LjVersion
from .npm_version import NpmVersion
from .snyk_version import SnykVersion
from .maven_version import MavenVersion

__all__ = ["Item", "ItemGroup", "LjVersion", "VersionSort", "Version", "ComposerVersion", "GoVersion", "NpmVersion",
           "SnykVersion", "MavenVersion"]

Equal_Not_Compare_Type = ["nvd", "npm", "go"]
Equal_Or_Compare_Type = ["cargo", "snyk", "cocoapods", "other", "maven"]
