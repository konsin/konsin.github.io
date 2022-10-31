---
layout: qt学习（一）基本模块
date: 2022-10-24 18:56:29
tags: 
- QT
- C++
categories: 学习笔记
---

## 基本模块：

|模块|描述|
|:-|:-|
|Qt Core|其他模块都用到的核心非图形类|
|Qt GUI|设计GUI的基础类，包括OpenGL|
|Qt Multimedia|音频、视频、摄像头及广播功能的类|
|Qt Multimedia Widgets|实现多媒体功能的界面组件类|
|Qt Network|使网络编程更简单和轻便的类|
|Qt QML|用于QML和JavaScript的类|
|Qt Quick|用于构建具有定制用户界面的动态应用程序的声明框架|
|Qt Quick Controls|创建桌面样式用户界面|
|Qt Quick Dialogs|通过Qt Quick创建系统对话框并与之交互的类型|
|Qt Quick Layouts|用于Qt Quick2界面元素的布局项|
|Qt SQL|使用SQL用于数据库操作的类|
|Qt Test|用于应用程序和库进行单元测试的类|
|Qt Widgets|用于构建GUI的C++图形组件类|

## 常用控件：
### QlineEdit 单行文本框控件
QLineEdit类是一个单行文本框控件，可以输入单行字符串。
常用方法

|方法|功能|
|:-|:-|
|setText()|设置文本框的内容|
|setPlaceholderText()|设置文本框显示的文字|
|setAlignment()|按固定值方式对齐文本|

### QGridLayout 网格布局控件
QGridLayout可将窗口分割成行和列的网格来进行排列，类似于控件的容器。
用户可使用`addWidget()`函数将被管理的控件添加到窗口中。
或使用`addLayout()`函数将布局添加到窗口中。
1. `addWidget()`函数：
   给网格布局添加部件，设置指定的行数和列数，起始位置默认值为(0,0)
   ```cpp
    addWidget(Qwdget Widget, int row, int col, int alignment = 0)
    ```
    - widget：表示所添加的控件
    - row：表示控件的行数，默认从0开始
    - col：标示空间的列数，默认从0开始
    - alignment：表示对其方式


