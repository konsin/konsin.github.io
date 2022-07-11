---
title: Debian-Pi-arch64 安装nextcloud
date: 2019-11-25 20:18:27
categories: 配置教程
tags: 

- Debian
- Linux
- Nextcloud

---

# Debian-Pi-arch64 安装nextcloud

安装nextcloud过程中出现了,工具安装问题,u盘不能读取问题,NTFS格式U盘会提示0770权限问题的错误,下面详细说明下怎么解决的这些问题

## 安装依赖

### 服务器

这里我们使用apache2作为服务器，通过以下命令安装apache2.80端口被封的话自己改端口

```bash
apt-get install apache2
```

### 数据库

NextCloud可用的数据库有MySQL/MariaDB，PostgreSQL，Oracle。官方推荐MySQL/MariaDB，这里以mysql为例，执行以下指令安装mysql：

```bash
apt-get install mysql-server
mysql_secure_installation
```

期间会让你设置root密码和密码强度，请自行判断。

进入mysql命令界面：

```bash
mysql -u root -p
```

创建数据库

```sql
create database nextcloud;
```

再为NextCloud创建一个数据库用户:

```sql
create user 'your_username'@'localhost' identified by 'your_passwd'
```

其中`your_username`是用户名,`localhost`指明只能通过本地访问。要想通过远程访问可改为`remote`同时配置你的mysql访问策略。`your_passwd`即所对应的密码。
 如果遇到`Your password does not satisfy the current policy requirements` 问题，这是因为你的密码强度级别设置太高，通过`set global validate_password_policy=0`可以设置为最低级别，关于密码强度的说明请参考百度。

为所创建的用户授予权限:

```sql
grant all privileges on nextcloud.* to 'your_username'@'localhost' identified by 'your_passwd';
flush privileges;
quit
```

到此数据库的部分已经完成了。

### 运行环境要求

执行下面的命令安装php

```bash
apt-get install php
```

官方要求php5.0+，通过以下指令查看php版本

```bash
php -v
```

然后安装NextCloud所需的其它php依赖

```bash
apt-get install php-zip
apt-get install php-dompdf
apt-get install php-xml
apt-get install php-mbstring
apt-get install php-curl
apt-get install php-mysql
```

到此环境配置已经完成,

## 配置nextcloud

已经将从官网下载的安装包上传到服务器

下面进行解压缩

```
tar -xjf nextcloud-XX.XX.tar.bz2
```

更改文件权限

```
sudo chown -R root:root nextcloud
```

移动文件到`/var/www/html/`中

```
sudo mv nextcloud /var/www/html
```

这时已经可以在浏览器输入` http://localhost/nextcloud `访问了

但是还存在一堆问题.现在切换到root用户开始更改配置文件.

打开config.php文件

```
 nano /var/www/html/nextcloud/config
```

配置储存盘/数据目录.我是将NTFS格式的U盘挂载到了`/home/pi/mydisk/`并创建了nextcloud文件

```
'datadirectory' => '/home/pi/mydisk/nextcloud',
```

当提示数据目录要0770权限时:

在nextcloud目录下config/config.php文件中加入

```
'check_data_directory_permissions' => false
```

这一条语句是取消文件权限检测.

## 添加离线下载功能

安装ocDownload插件.

安装aria2

```shell
sudo apt-get install aria2 curl php-curl
```

配置aria2

```shell
mkdir /var/log/aria2c /var/local/aria2c
touch /var/log/aria2c/aria2c.log
touch /var/local/aria2c/aria2c.sess
chown www-data.www-data -R /var/log/aria2c /var/local/aria2c
chmod 770 -R /var/log/aria2c /var/local/aria2c
sudo -u www-data aria2c --enable-rpc --rpc-allow-origin-all -c -D --log=/var/log/aria2c/aria2c.log --check-certificate=false --save-session=/var/local/aria2c/aria2c.sess --save-session-interval=2 --continue=true --input-file=/var/local/aria2c/aria2c.sess --rpc-save-upload-metadata=true --force-save=true --log-level=warn --rpc-listen-all=false
```