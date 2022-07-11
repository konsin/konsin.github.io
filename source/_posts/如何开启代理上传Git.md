---
title: 如何开启代理上传Git
date: 2022-07-11 17:48:18
categories: 配置教程
tags:
- Git
- Clash
---

如果Git上传时出现`Failed to connect to github.com port 443: Timed out`，则说明当前网络环境连不上Github，需要开启代理。

以代理工具Clash为例。

先开启Clash的系统代理`System Proxy`

![image-20220711180300486](https://cdn.jsdelivr.net/gh/konsin/images@main/202207111803521.png)

然后再终端执行如下代码开启代理

```shell
git config --global https.proxy https://127.0.0.1:7890
```

等上传结束后再执行指令关闭代理

```shell
git config --global --unset https.proxy
```

