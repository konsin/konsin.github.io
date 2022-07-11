---
title: MySQL ERROR 1698 (28000) 解决方案
date: 2022-06-30 10:59:09
categories: 异常处理
tags:

- MySQL

---

# MySQL ERROR 1698 (28000) 解决方案

解决步骤：
1、停止MySQL服务

~$ sudo service mysql stop

2、以安全模式启动MySQL

~$ sudo mysqld_safe --skip-grant-tables &

3、然后无需密码直接进入MySQL

~$ mysql -u root

4、查看user表，发现错误原因user表被修改了

命令：mysql> select user ,plugin from mysql.user

错误：

5、root的plugin应该和剩下的三种一样为 mysql_native_password

即正确为：

6、所以我们只需要修改过来就可以了

mysql> update mysql.user set authentication_string=PASSWORD('newPwd'), plugin='mysql_native_password' where user='root';

mysql> flush privileges;

mysql> quit；
