# 毕业设计

为了更好的维护代码，本项目采用前后端分离，前端使用vue脚手架搭建应用，后端使用django框架搭建各类应用服务。

python 版本 Python 3.10.13 

backend后端部分采用的是django

frontend前端部分采用vue框架

项目所需环境在environment.yml里，可以使用conda直接导入

下面是使用conda的导入教程

1. **确保你有一个`environment.yml`文件**：这个文件包含了环境的名称、包含的包以及可能的其他依赖信息。它通常看起来像这样：

```
yamlCopy codename: myenv
dependencies:
  - numpy
  - pandas
  - scipy
  - pip:
    - somepippackage==1.0.0
```

1. **打开终端或命令提示符**：在你的计算机上打开终端（Linux或macOS）或命令提示符/PowerShell（Windows）。
2. **导入环境**：导航到包含`environment.yml`文件的目录，然后运行以下命令：

```shell
conda env create -f environment.yml
```

这个命令会读取`environment.yml`文件，并创建一个新的Conda环境，环境的名称和包依赖都是基于文件内容。如果`environment.yml`文件中指定了环境的名称，那么Conda会使用这个名称创建环境。如果你想为环境指定一个不同的名称，可以在创建时不使用`-f`选项直接指定名称，但这样做会忽略`environment.yml`文件中指定的环境名称。

1. **激活新环境**：环境创建完成后，你可以通过以下命令来激活这个环境：

```shell
conda activate myenv
```

请将`myenv`替换为你的环境名称，如果你在`environment.yml`文件中使用了不同的名称，或者你在创建环境时指定了一个不同的名称。