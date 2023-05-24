---
title: 使用PySide为树莓派创建应用
date: 2023-05-24 15:19:43
tags:
    - QT
    - Linux
    - Raspberry Pi
categories:
    - 学习笔记
    - 配置教程
---

# 树莓派设置QT程序自启动
修改rc.local或者systemcmd注册服务的方式启动`PySide`编写的窗口应用会出现错误
>qt.qpa.xcb: could not connect to display

因此这并不是一个很好的方式，而树莓派的系统中提供了另一种应用自启动的方式：
在`/home/XXX/.config/autostart`目录下创建`.desktop`文件可以实现桌面应用程序的自动执行。如下为文件书写格式
```bash
[Desktop Entry]
Name=app_name
Comment=app_comment
Exec=正常的执行程序的shell指令
Icon=图标文件（非必须）
Terminal=false
MultipleArgs=false
Type=Application
Categories=Application;Development;
StartupNotify=true
```
# pyqt或者pyside实现将SVG显示在Label的方法。
如果不需要对SVG进行修改可以直接使用修改styleSheet的方式，添加属性为`image:url()`。
如果需要调整SVG尺寸或者颜色，可以参考如下方式。
```python
def convertSVGtoImg(self, src, size:QSize) ->QPixmap:
    """
    :param src: SVG路径
    :type src: _type_
    :param size: 生成图片大小
    :type size: QSize
    :return: 返回处理后的SVG图片
    :rtype: QPixmap
    """
    svg_remder = QSvgRenderer(src)

    image = QImage(size, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(Qt.transparent)
    painter = QPainter(image)
    painter.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing| QPainter.SmoothPixmapTransform)
    svg_remder.render(painter)
    pix = QPixmap() 
    painter.end()    
    pix=pix.fromImage(image) 
    return pix

def convertSVGtoImg(self, src, size:QSize, color:QColor) ->QPixmap:
    """
    :param src: SVG路径
    :type src: _type_
    :param size: 生成图片大小
    :type size: QSize
    :param color: 要更改的颜色
    :type color: QColor
    :return: 返回处理后的SVG图片
    :rtype: QPixmap
    """
    svg_remder = QSvgRenderer(src)

    image = QImage(size, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(Qt.transparent)
    painter = QPainter(image)
    painter.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing| QPainter.SmoothPixmapTransform)
    svg_remder.render(painter)
    pix = QPixmap() 
    painter.end()   
    for i in range(image.width()):
            for j in range(image.height()): 
                    if(image.pixelColor(i,j) != Qt.transparent ):
                            image.setPixelColor(i,j,color)   
    pix=pix.fromImage(image) 
    return pix  
```

# pyqt|pyside中定时器的使用
```python
#定义一个计时器
self.timeRefresh = QTimer()
#连接处理函数
self.timeRefresh.timeout.connect(self.refreshTime) 
#开启循环计时
self.timeRefresh.start(1000) 
"""
如果只需要单次计时
self.weatherRefresh.setSingleShot(True)
"""
```


# 树莓派中pyside的安装
树莓派中目前只有pyside2，并且在官方的 Ubuntu 和 Debian 存储库中。每个Pyside模块都是一个单独的包。所以安装时也需要一个个安装这些组件。一行命令搞定全部组件：
`sudo apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns
`


