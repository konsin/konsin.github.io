---
title: Git强制上传本地分支
date: 2022-07-11 17:47:46
categories: 配置教程
tags:
- Git
---

采用这个方法可以让一个仓库存储不同的软件代码。如主分支存Hexo的网页代码，一个存Hexo的源代码。

现在git上建立分支新source。

如果还未建立本地git仓库。先执行如下指令

```shell
git init
git remote add origin https://github.com/XXXX/XXXXX.git 
git add .
git commit -m 'XXXX'
```

创建好本地仓库并关联远程仓库后执行如下指令.其中master替换为本地分支名，source替换为远程分支名。` -f`表示清空远程分支。如果不加` -f` 则会提示`error: failed to push some refs to`

```shell
git push origin master:source -f
```

