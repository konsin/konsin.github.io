---
title: 为code-server配置c++环境
date: 2022-08-27 14:56:38
tags:
- C++
- Linux
- code-server
categories:
- 配置教程
---
code-server默认是不支持运行和调试C++的，并且在插件库中也找不到C++的环境插件。但是我们可以通过手动安装的方式来让IDE支持C++的调试运行。
### 环境依赖
gcc是一定要安装的，没安装的话执行`sudo apt install build-essential`安装
### 下载插件
由于插件库没有内置C/C++插件，所以我们需要去VSCode插件网站下载插件。
- 浏览器打开[插件页面](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- 进入插件页面后点击右下角的`Download Extension`选择对应平台进行下载。
- 将下载的插件上传到服务器。
### 安装插件
推荐使用IDE在线安装。具体流程如下
- IDE资源管理器打开插件上传目录
- 在插件条目上右键选择`从VSIX安装`即可安装插件。如果提示`Corrupt ZIP: end of central directory record signature not found`则说明插件安装包有错误，重新下载即可。
### 配置launch.json和task.json
这里推荐使用C/C++ Config插件。安装完插件后按下`Ctrl + Shift + P`组合键，在弹出输入框输入`Generate C++ Config Files`即可一键生成配置文件。

### 其他
如果安装C/C++插件后进行插件设置时提示
```
IntelliSense-related commands cannot be executed when `C_Cpp.intelliSenseEngine` is set to `Disabled`.
```
可以通过修改`/home/ubuntu/.local/share/code-server/User/settings.json`文件将`"C_Cpp.intelliSenseEngine": "Disable",`修改为`"C_Cpp.intelliSenseEngine": "Default",`解决。

同时如果打开cpp文件后右上角没有三角形的运行图标，此方法也是部分情况下的解决方式。