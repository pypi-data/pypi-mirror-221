# -*- coding: utf-8 -*-
class BaseError(Exception):
    """不要直接使用这个类，请继承然后抛出异常。"""

    code = 1
    message = "应用错误"

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __str__(self):
        return self.message

    def get_response_data(self):
        return {"errors": [{"code": self.code, "message": self.message}]}

    def __repr__(self):
        return "<%s>" % self.__class__.__name__


class VersionSourceError(BaseError):
    code = 1
    message = "version_source格式化失败"


class VersionDestError(BaseError):
    code = 2
    message = "version_expression格式化失败"


class MaxVersionError(BaseError):
    code = 2
    message = "最大版本获取失败"
