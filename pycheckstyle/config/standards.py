from .base import __join_path, base_path

standard_path = __join_path(base_path, "standards")  # 内置检查标准路径
google_standard = __join_path(standard_path, "google_checks.xml")  # 内置Google检查标准文件路径
sun_standard = __join_path(standard_path, "sun_checks.xml")  # 内置Sun检查标准文件路径
