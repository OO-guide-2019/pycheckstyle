import os


def __join_path(path, *paths):
    """
    路径拼接
    :param path: 基路径
    :param paths: 拼接路径
    :return:
    """
    return os.path.normpath(os.path.join(path, *paths))


# 系统运行基础路径
base_path = "/usr/lib/checkstyle"
