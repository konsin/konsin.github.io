---
title: 使用Hexo及Gitee搭建博客
date: 2022-07-09 21:09:06
categories: 配置教程
tags: 
    - Hexo
    - Git
---

 Hexo官方文档地址：[文档 | Hexo](https://hexo.io/zh-cn/docs/)

# Step1：安装Node.Js

前往[NPM官网]([nodejs.org](https://nodejs.org/))下载适合自己系统的Node.Js。

更换为国内镜像源：

```shell
npm config set registry http://registry.npm.taobao.org
```

查看当前镜像是否修改成功：

```shell
npm get registry
```

# Step2: 安装Git

可以在安装git后设置SSH公钥。

Gitee生成/添加SSH公钥教程：[生成/添加SSH公钥 - Gitee.com](https://gitee.com/help/articles/4181#article-header0)

# Step3：安装Hexo

使用 npm 安装 Hexo。

```shell
npm install -g hexo-cli
```

同时为了推送到Gitee需要安装如下插件

```shell
npm install hexo-deployer-git --save
```

# Step4：Hexo生成blog目录

使用如下指令在指定文件夹中新建所需要的文件，`<folder>`为指定的空文件夹名

如果是Window操作系统，需要设置PoweShell允许脚本运行。

```shell
hexo init <folder>
```

# Step5：修改网站配置信息

进入网站文件目录下，目录结构如下：

```textile
.
├── _config.yml
├── package.json
├── scaffolds
├── source
|   ├── _drafts
|   └── _posts
└── themes
```

对` _config.yml`进行修改。

在配置文件最后进行如下修改以推送到gitee仓库,github同理。

```xml
deploy:
  type: 'git'
  repo: git@gitee.com:XXXXXX.git
  branch: master
```

如果需要同时添加多个仓库则如下配置

```xml-doc
deploy:
- type: 'git'
  repo: git@gitee.com:xxxx.git
  branch: xxx

- type: 'git'
  repo: git@github.com:xxxx.git
  branch: xxx
```

# 配置结束

之后要对网站进行修改都需要进入博客所在目录进行终端操作。

# 创建新文档

使用如下指令创建文档，而后在`source/_posts`文件下生成md文件。`[layout]`可省略使用默认布局.

```shell
hexo new [layout] <title>
```

# 生成并部署

使用如下命令使，Hexo 在生成完毕后自动部署网站

```shell
hexo generate --deploy
```

该命令也可简写为`hexo g -d`

如未安装`hexo-deployer-git`插件则会出现`# ERROR Deployer not found`错误。

# 创建标签

在博客目录下打开终端输入如下指令

```shell
hexo new page tags
```

创建成功打开`source/tags`目录下的`index.md`文件添加type属性。

```bash
---
title: XXX
date: XXX-XXXX
type: "tags"
---
```

在文章中使用分类只需要在抬头中添加`tags`属性即可，Hexo会自动创建分类索引。

一篇文章只能设置多个标签。

```css
---
title: 使用Hexo及Gitee搭建博客
date: 2022-07-09 21:09:06
tags: 
    - Hexo
    - Git
---
```

# 创建分类

在博客目录下打开终端输入如下指令

```shell
hexo new page categories
```

创建成功打开`source/categories`目录下的`index.md`文件添加type属性。

```bash
---
title: XXXX
date: XXX-XXXX
type: "categories"
---
```

在文章中使用分类只需要在抬头中添加`categories: XXX`即可，Hexo会自动创建分类索引。

一篇文章只能设置一个分类。

```css
---
title: 使用Hexo及Gitee搭建博客
date: 2022-07-09 21:09:06
categories: 配置教程
---
```
# 图床问题
可以自建Github仓库作为图床，使用[PicX](https://picx.xpoet.cn)方便快速的管理。
