import re


class CheckMessage(object):
    """
    格式检查结果信息类
    """
    __parse_pattern = "^\[([A-Za-z]+)\]\s+([\s\S]+?):(\d+)(:(\d+)|):\s+([\s\S]+?)\s+\[([A-Za-z0-9]+)\]\s*$"

    def __init__(self, level, msg_type, position, message):
        """
        构造函数
        :param level: 信息级别
        :param msg_type: 信息类型
        :param position: 位置
        :param message: 信息文本
        """
        self.__level = level
        self.__type = msg_type
        self.__position = position
        self.__message = message

    @property
    def level(self):
        """
        获取信息级别
        :return: 信息级别
        """
        return self.__level

    @property
    def type(self):
        """
        获取信息类别
        :return: 信息类别
        """
        return self.__type

    @property
    def position(self):
        """
        获取信息位置
        :return: 信息位置
        """
        return self.__position

    @property
    def message(self):
        """
        获取信息文本
        :return: 信息文本
        """
        return self.__message

    @classmethod
    def parse(cls, string):
        """
        信息解析
        :param string: 原字符串
        :return: 解析后的对象，解析失败返回None
        """
        groups = re.findall(cls.__parse_pattern, string)
        if groups:
            group = groups[0]

            file = group[1]
            line = int(group[2])
            column = int(group[4] or group[2])
            position = MessagePosition(file, line, column)

            level = group[0]
            message = group[5]
            msg_type = group[6]
            return cls(level, msg_type, position, message)
        else:
            return None

    def __repr__(self):
        """
        获取表达式形式
        :return: 表达式形式
        """
        return r'<CheckMessage %s, %s, message: "%s">' % (self.level, self.type, self.message)

    @property
    def origin(self):
        """
        获取原字符串
        :return: 原字符串
        """
        return "[%s] %s: %s [%s]" % (self.level, self.position.origin, self.message, self.type)

    def __str__(self):
        """
        获取字符串格式
        :return: 字符串格式
        """
        return self.origin


class MessagePosition(object):
    """
    信息位置类
    """

    def __init__(self, file, line, column=None):
        """
        构造函数
        :param file: 文件路径
        :param line: 起始行
        :param column: 结束行
        """
        self.__file = file
        self.__line = line
        self.__column = column

    @property
    def line(self):
        """
        获取起始行
        :return: 起始行
        """
        return self.__line

    @property
    def column(self):
        """
        获取结束行
        :return: 结束行
        """
        return self.__column

    @property
    def file(self):
        """
        获取文件路径
        :return: 文件路径
        """
        return self.__file

    @property
    def position(self):
        """
        获取格式化位置
        :return: 格式化位置
        """
        if self.column:
            return "%s:%s" % (self.line, self.column)
        else:
            return "%s" % self.line

    @property
    def origin(self):
        """
        还原成原字符串
        :return: 原字符串
        """
        return "%s:%s" % (self.file, self.position)

    def __str__(self):
        """
        获取字符串格式信息
        :return: 字符串格式信息
        """
        return self.origin

    @property
    def __full_position(self):
        """
        获取完整位置信息
        :return 完整位置信息
        """
        if self.column:
            return "line %s, column: %s" % (self.line, self.column)
        else:
            return "line %s" % self.line

    def __repr__(self):
        """
        获取输出表达格式信息
        :return: 输出表达格式信息
        """
        return "<MessagePosition %s, file: %s>" % (self.__full_position, self.file)
