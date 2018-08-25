from .base import CheckStyleException


class CheckStyleErrorException(CheckStyleException):
    """
    异常输出异常
    """

    def __init__(self, stderr):
        """
        异常输出
        :param stderr: 异常输出
        """
        self.__stderr = stderr
        self.__title = None
        for line in stderr.splitlines():
            if line.strip():
                self.__title = line.strip()
                break

    @property
    def title(self):
        """
        获取异常标题
        :return: 异常标题
        """
        return self.__title

    @property
    def stderr(self):
        """
        获取异常输出
        :return: 获取异常输出
        """
        return self.__stderr

    def __str__(self):
        """
        获取字符串格式
        :return: 字符串格式
        """
        return self.__repr__()

    def __repr__(self):
        """
        获取表达式格式
        :return: 表达式格式
        """
        return r'<%s "%s">' % (type(self).__name__, self.title)


class CheckStyleReturnCodeException(CheckStyleException):
    """
    异常返回值异常
    """

    def __init__(self, return_code):
        """
        构造函数
        :param return_code: 返回值
        """
        self.__return_code = return_code

    @property
    def return_code(self):
        """
        获取返回值
        :return: 返回值
        """
        return self.__return_code

    def __str__(self):
        """
        获取字符串格式
        :return: 字符串格式
        """
        return self.__repr__()

    def __repr__(self):
        """
        获取表达式格式
        :return: 表达式格式
        """
        return r'<%s code: %s>' % (type(self).__name__, self.return_code)


class CheckStyleCommonException(CheckStyleReturnCodeException, CheckStyleErrorException):
    def __init__(self, return_code, stderr):
        """
        构造函数
        :param return_code: 返回值
        :param stderr: 异常输出
        """
        CheckStyleErrorException.__init__(self, stderr)
        CheckStyleReturnCodeException.__init__(self, return_code)

    def __str__(self):
        """
        获取字符串格式
        :return: 字符串格式
        """
        return self.__repr__()

    def __repr__(self):
        """
        获取表达式格式
        :return: 表达式格式
        """
        return r'<%s return: %s, title: "%s">' % (type(self).__name__, self.return_code, self.title)


def try_raise(return_code, stderr):
    """
    根据返回值尝试抛出异常
    :param return_code: 返回值
    :param stderr: 异常输出信息
    :return: None
    """
    if return_code and stderr:
        raise CheckStyleCommonException(return_code, stderr)
    elif return_code:
        raise CheckStyleReturnCodeException(return_code)
    elif stderr:
        raise CheckStyleErrorException(stderr)
