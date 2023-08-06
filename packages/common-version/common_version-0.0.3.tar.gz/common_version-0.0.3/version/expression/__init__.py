# -*- coding: utf-8 -*-
# flake8:noqa
from version.expression.base_method import arrangement_version, \
    handle_version_change_source, handle_version_compatible, dest_change_source, \
    handle_version_comma, find_str_index, handle_version_or
from version.expression.c_version_expression import VersionCExpression
from version.expression.cargo_version_expression import VersionCargoExpression
from version.expression.cocoapods_version_expression import VersionCocoExpression
from version.expression.composer_version_expression import VersionComposerExpression
from version.expression.go_version_expression import VersionGoExpression
from version.expression.hex_version_expression import VersionHexExpression
from version.expression.linux_version_expression import VersionLinuxExpression
from version.expression.maven_version_expression import VersionMavenExpression
from version.expression.npm_version_expression import VersionNpmExpression
from version.expression.nuget_version_expression import VersionNugetExpression
from version.expression.nvd_version_expression import VersionNvdExpression
from version.expression.other_version_expression import VersionOtherExpression
from version.expression.pip_version_expression import VersionPipExpression
from version.expression.ruby_version_expression import VersionRubyExpression
from version.expression.snyk_version_expression import VersionSnykExpression

__all__ = {
    "arrangement_version",
    "handle_version_change_source",
    "handle_version_compatible",
    "dest_change_source",
    "handle_version_comma",
    "find_str_index",
    "handle_version_or",
    "VersionSnykExpression",
    "VersionRubyExpression",
    "VersionPipExpression",
    "VersionNvdExpression",
    "VersionNugetExpression",
    "VersionNpmExpression",
    "VersionMavenExpression",
    "VersionHexExpression",
    "VersionGoExpression",
    "VersionComposerExpression",
    "VersionCargoExpression",
    "VersionCocoExpression",
    "VersionCExpression",
    "VersionLinuxExpression",
    "VersionOtherExpression",
}
