from ..operation.execute import execute


def __get_version():
    """
    获取版本信息
    :return: 版本信息
    """
    out, err = execute("-v")
    return out.strip()


version = __get_version()  # 版本信息
