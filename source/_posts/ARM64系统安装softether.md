---
title: ARM64系统安装softether
date: 2019-06-30 10:58:21
categories: 配置教程
tags: 

---

# ARM64系统安装softether

官方文档 https://github.com/SoftEtherVPN/SoftEtherVPN/blob/master/src/BUILD_UNIX.md 

安装依赖包

```
apt -y install cmake gcc g ++ libncurses5-dev libreadline-dev libssl-dev make zlib1g-dev
```

git下载源码包

```
./configure
```

编辑makefile文件去掉 所有的`-m64`

然后

```
make
make install
```

安装完成

启动/停止服务

```
vpnserver start
vpnserver stop
```

配置服务

```
vpncmd
1 
```

输入` ServerPasswordSet `配置管理员密码.