---
title: 安装配置VsCode_Online踩坑记录
date: 2022-08-26 21:12:37
tags: 
- Ubuntu
- Linux
- WebIDE
categories:
- 配置教程
---
本来使用腾讯云的theia IDE轻量应用服务器当作云端IDE的，但是无奈太难用了，launch.json的语法支持貌似和VSC也不一样。然后偶然发现VSC已经有Web版本了，折腾了一下终于安装成功，这里记录一下踩坑经历。
## 安装方式选择
配置VSCode Online有几种方法：
- 微软官方提供一个收费版本（含azure的服务器费用，捆绑销售），不推荐
- 下载 VSCode 源代码，编译以后通过yarn web启动。配置难度大，不推荐
- 通过 Code-Server 安装: https://coder.com
- 使用/修改现成的 docker 镜像：linuxserver/docker-code-server

我选择的是通过Code-Server安装,这里要注意第一个坑。**通过上边这个coder网站首页下载的并非是我们所需要的Code-Server**。
我们需要点进去文档界面，再左上角产品选择位置选择Code-Server（默认为Coder-OSS）。
在文档中提供了多种安装方式说明。这里推荐两种：
1. 通过脚本一键安装
   ```shell
   curl -fsSL https://code-server.dev/install.sh | sh
   ```
   如果要查看安装过程中的输出可以采用如下指令
   ```shell
   curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run
   ```
   需要注意的是通过脚本安装方式，由于国内服务器访问github较慢，耗费时间很长。
2. 下载安装包进行安装
   进入Code-server的github发布页下载最新版本的deb安装包
   `https://github.com/coder/code-server/releases/`
   这里下载安装包也有两种方式;
   - 直接下载到本地再上传到服务器
   - `curl -fOL ` 后加下载链接直接下载到服务器。下载链接可以通过转换工具转换为CDN加速后的链接，下载速度更快。
   然后就可以安装程序了(XXX替换为自己的安装包名)
   `sudo dpkg -i code-server_XXXX.deb`
   然后再执行指令添加到系统服务执行($USER换为自己的用户名)
   `sudo systemctl enable --now code-server@$USER`

# 配置Code-server
安装完成后Code-server默认是在 http://127.0.0.1:8080 访问的且只能本地访问. 
登入的密码可以在 `~/.config/code-server/config.yaml`查看，同时该文件也包含了其他必要的配置内容。
该文件默认格式如下
```xml
bind-addr: 127.0.0.1:8080
auth: password
password: afiaoskjfiojaoa468546
cert: false
```
只需要简单修改`bind-addr`和`password`即可外网通过`IP:8080`访问
```xml
bind-addr: 0.0.0.0:8080
auth: password
password: （你的密码）
cert: false
```
接下来就可以安装插件使用你的WebIDE编程了

