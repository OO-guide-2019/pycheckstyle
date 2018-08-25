# pycheckstyle

基于checkstyle的python封装包

checkstyle原文档地址：[http://checkstyle.sourceforge.net/cmdline.html](http://checkstyle.sourceforge.net/cmdline.html)

## 安装
### 准备工作

在正式安装之前，首先需要进行一些准备：

* 完整的java环境（推荐使用`Oracle Java 8`）
* 完整的python环境（推荐使用`python 3.5+`）
* 相关系统依赖

### 安装jar包

首先将`checkstyle.jar`安装至系统内部。

```bash
sudo ./install.sh
```

注意：需要`sudo`权限

### 安装pycheckstyle

接下来安装`pycheckstyle`包

```bash
sudo python3 setup.py install
```

注意：同样的，这步操作依然需要`sudo`权限

## 开始使用

在本包中，目前只内置了版本信息和基本的`-c`查询功能。后续还将根据需要进一步完善

### 获取使用的checkstyle版本信息

```python
from pycheckstyle import *

if __name__ == "__main__":
    print(checkstyle_version)

```

输出：

```
Checkstyle version: 8.12
```

### 使用内置的模板进行代码风格检查

```python
from pycheckstyle import *

if __name__ == "__main__":
    for message in SunStandard().check("/vagrant_data/java_projects/ips-project"):
        print(message.level, message.type, message.message)
        print(message.position)

```

此处程序使用了`pycheckstyle`内置的`SunStandard`模板，实际上包内还内置了一个名为`GoogleStandard`的模板，使用方法基本一样。

此外，check的对象可以是路径，也可以是单个文件。

### 使用自定义模板进行代码风格检查

方法和上面的例子基本类似，使用`CheckStandard`可以在构造函数中自定义模板位置

```python
from pycheckstyle import *

if __name__ == "__main__":
    for message in CheckStandard("standards/google_checks.xml").check("/vagrant_data/java_projects/ips-project"):
        print(message.level, message.type, message.message)
        print(message.position)

```

更多技术细节，以及相关对象的方法可以自行阅读源代码。