from .base import base_path, __join_path

java = "java"  # java命令
jar_file = __join_path(base_path, "checkstyle.jar")  # checkstyle.jar路径
command_line_base = [java, "-jar", jar_file]  # 运行基础命令行
