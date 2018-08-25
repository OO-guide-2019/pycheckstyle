from ..config.execute import command_line_base as __command_line_base
from ..models.exception import try_raise_execute
import subprocess


def execute(*args, ignore_return_code=False, ignore_stderr=False):
    """
    底层执行接口
    当返回值非零的时候将抛出异常
    :param args: 命令行参数
    :param ignore_return_code: 忽略返回值异常
    :param ignore_stderr: 忽略异常输出
    :return: 标准输出信息
    """
    command_line_args = __command_line_base + list(args)
    program = subprocess.Popen(command_line_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = program.communicate()

    try_return_code = program.returncode
    try_stderr = err.decode()
    if ignore_return_code:
        try_return_code = None
    if ignore_stderr:
        try_stderr = None
    try_raise_execute(try_return_code, try_stderr)

    return out.decode(), err.decode()
