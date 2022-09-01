---
title: openwrt折腾笔记
date: 2022-09-01 09:08:45
tags:
-linux
-openwrt
categories: 配置教程
---
本文记录使用Winserver环境下使用Hyper-V安装OpenWRT的过程。
## 下载OpenWRT固件
推荐下载别人已经编译好的OpenWRT固件。我这里使用的是由[Kiddin](https://op.supes.top/firmware/x86_64/)二次编译过的LuCI的固件。
## 转为虚拟磁盘文件
下载安装`StarWind V2V Converter`软件。然后点击Local File转换镜像文件
![image](https://git.poker/konsin/images/blob/main/image.3o033mqvamo0.jpg?raw=true)
然后继续选择Local File，在之后的界面选择VHD/VHDX，最后再选择磁盘镜像的具体格式即可选择导出路径进行转换。
![image](https://git.poker/konsin/images/blob/main/image.oyaxaxxqs28.jpg?raw=true)
## 导入Hyper-V
正常创建虚拟机，但是再连接虚拟硬盘这一步要选择使用现有虚拟硬盘。
![image](https://git.poker/konsin/images/blob/main/image.4vu9ma90l5k0.jpg?raw=true)
## 配置OpenWRT的IP
打开虚拟机，在终端输入`vim /etc/config/network`使用vim手动编辑IP设置。
修改lan口设置为固定ip
![image](https://git.poker/konsin/images/blob/main/image.5ihqux07rhs0.jpg?raw=true)
## 进入OpenWRT网页管理界面继续设置
在浏览器输入刚才修改的IP即可进入管理界面。默认密码为空。
![image](https://git.poker/konsin/images/blob/main/image.jsw8wd2cop8.jpg?raw=true)
