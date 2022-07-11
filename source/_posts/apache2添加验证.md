---
title: apache2添加验证
date: 2019-11-24 22:35:09
categories: 配置教程
tags: Apache

---

如果希望将某些或所有网站限制仅允许特定用户或组访问，使用HTTP Auth（基于apache2）方式很容易实现。
 一、在CentOS上，httpd的配置文件默认在/etc/httpd/conf/httpd.conf文件，

```csharp
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
# 下面这3行是默认的，可以直接改，或者注释掉
#    AllowOverride ALL
#    Order allow,deny
#    Allow from all
# 改成下面这样
    AllowOverride authconfig
    Order allow,deny
    Allow from all
    AuthName "Web Access"
#名字随意
    AuthType Basic
    AuthUserFile /var/www/html/.htpasswd
#认证文件名字和位置和下面生成的要一致
    Require valid-user
</Directory>
```

这里存放用户密码的文件就是.htpasswd， 位置和名称可以改。
 生成用户密码文件：

```swift
htpasswd -c /var/www/html/.htpasswd <username>
#创建第一个认证用户的时候用-c，其他用户要把-c去掉，否则会被覆盖掉
重启httpd服务即可
systemctl restart httpd
```

也可使用用户组来控制，也是编辑httpd配置文件，这里不写了。
 二、Ubuntu的apache配置文件编辑/etc/apache2/sites-enabled/目录下的文件，根据虚拟站点有不同的名称，比如我的nagios配置文件就叫nagios.conf，看起来是这样子的：

```php
Alias /nagios "/usr/local/nagios/share"
<Directory "/usr/local/nagios/share">
#  SSLRequireSSL
   Options None
   AllowOverride None
   <IfVersion >= 2.3>
      <RequireAll>
         Require all granted
#        Require host 127.0.0.1
         AuthName "Nagios Access"
         AuthType Basic
         AuthUserFile /usr/local/nagios/etc/htpasswd.users
         Require valid-user
      </RequireAll>
   </IfVersion>
 <IfVersion < 2.3>
      Order allow,deny
      Allow from all
     Order deny,allow
     Deny from all
      AuthName "Nagios Access"
      AuthType Basic
      AuthUserFile /usr/local/nagios/etc/htpasswd.users
      Require valid-user
   </IfVersion>
</Directory>
```

Ubuntu如果默认没有安装htpasswd工具的话，要先安装apache2-utils包：
 sudo apt install apache2-utils
 生成用户密码的用法和CentOS是一样的。