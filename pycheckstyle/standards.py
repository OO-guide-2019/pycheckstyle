from .execute import execute
from .config.standards import google_standard, sun_standard
from .message import CheckMessage


class CheckStandard:
    """
    检查标准类
    """

    def __init__(self, standard_file):
        """
        构造函数
        :param standard_file: 检查规范标准文件
        """
        self.__standard_file = standard_file

    @property
    def standard_file(self):
        """
        获取检查规范标准文件
        :return: 检查规范标准文件
        """
        return self.__standard_file

    def check(self, check_dir):
        """
        检查对应的路径（文件）
        :param check_dir: 检查的路径（文件）
        :return: 检查结果（list格式，内部包含CheckMessage对象）
        """
        out, err = execute("-c", self.standard_file, check_dir)
        messages = []
        for line in out.splitlines():
            message = CheckMessage.parse(line)
            if message:
                messages += [message]
        return messages


class GoogleStandard(CheckStandard):
    """
    内置的Google规范检查标注
    """

    def __init__(self):
        """
        构造函数
        """
        super().__init__(google_standard)


class SunStandard(CheckStandard):
    """
    内置的Sun规范检查标准
    """

    def __init__(self):
        """
        构造函数
        """
        super().__init__(sun_standard)
