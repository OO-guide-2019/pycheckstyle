from .message import CheckMessage
from ..config.standards import google_standard, sun_standard
from ..operation import execute


class CheckStandard:
    """
    检查标准类
    """

    def __init__(self, standard_file, ignore_return_code=False, ignore_stderr=False):
        """
        构造函数
        :param standard_file: 检查规范标准文件
        :param ignore_return_code: 忽略非零返回值
        :param ignore_stderr: 忽略异常输出
        """
        self.__standard_file = standard_file
        self.__ignore_return_code = ignore_return_code
        self.__ignore_stderr = ignore_stderr

    @property
    def standard_file(self):
        """
        获取检查规范标准文件
        :return: 检查规范标准文件
        """
        return self.__standard_file

    def check(self, check_dir, abs_path=False):
        """
        检查对应的路径（文件）
        :param check_dir: 检查的路径（文件）
        :param abs_path: 使用绝对路径（默认为False）
        :return: 检查结果（list格式，内部包含CheckMessage对象）
        """
        out, err = execute(
            "-c", self.standard_file, check_dir,
            ignore_return_code=self.__ignore_return_code,
            ignore_stderr=self.__ignore_stderr
        )
        messages = []
        for line in out.splitlines():
            if abs_path:
                work_dir = None
            else:
                work_dir = check_dir
            message = CheckMessage.parse(line, work_dir)
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
        super().__init__(sun_standard, ignore_return_code=True)
