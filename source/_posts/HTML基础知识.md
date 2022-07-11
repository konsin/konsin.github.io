---
title: HTML基础知识
date: 2020-06-30 10:58:53
categories: 学习笔记
tags: 

- Html
- 前端
---

# HTML学习

[TOC]

## HTML基础知识

### HTML标签

标签不区分大小写,推荐小写

#### 标签种类

1. **双标签**(体标记)  :格式如`<标记名></标记名>  `.由开始和结束两个标记符组成的标记.
   
   ```html
   例子:<a href="https://www.shiyanlou.com">实验楼</a> (第一个尖括号内科对属性进行设置)
   <html></html>        //html是根标记
   <head></head>        //头部标记;定义文档头部信息,一个 HTML 文档只能含有一对 <head>标记
   <title></title>        //<title>标记用于定义 HTML 页面的标题，必须位于<head>标记之内。只能有一对
   <body></body>        //<body>标记用于定义 HTML 文档所要显示的内容.在<head>之后.是用户所看到的.
   <h1></h1>            //用于对齐文字
   <h2></h2>
   <p></p>                //<p> 标签定义段落。
   <div></div>
   <span></span>
   <a></a>                //<a> 标签定义超链接，用于从一张页面链接到另一张页面。
                       //<a> 元素最重要的属性是 href 属性，它指示链接的目标(指向标签)。
                           例子:<a href="https://www.shiyanlou.com">实验楼</a>
                       //另一个属性是name属性,创建文档内的书签
                           <a href="#winter">查看冬天。</a>
                           <h2><a name="winter">冬</a></h2>
                           点击查看冬天则跳转到冬所在行
                       //target 属性：用于指定链接页面的打开方式，其取值有 _self(默认)                         和_blank(新开一个页面)
   <ul></ul>
   <ol></ol>
   <dt></dt>
   <dd></dd>
   <mark></mark>
   <iframe></iframe>
   ```

2. **单标签**(空标记) :格式如:`<标记名/>  ` ;
   
   ```html
   <br/>     <!--换行-->
   <hr />    <!--水平分隔线-->
   <meta />
   <img />
   ```

#### 标签关系

1. 嵌套关系
   
   ```
   <head>  
       <title>  
       </title>  
   </head>
   ```

2. 并列关系
   
   ```
   <head></head>
   <body></body>
   ```

### HTML 列表

有序列表（ol），无序列表（ul）以及自定义列表（dl）。

1. 有序列表(ol)
   
   ```html
   语法格式:
   <ol type=value1 start=value2>
       <li></li>        
   </ol>
   ```
   
   1. 属性有 type start两种.type默认为数字列表(可设为"1","a","A","i","I");

2. 无序列表(ul)
   
   ul 的 type 属性：默认值(实心圆): disc，方块: square，空心圆: circle。

3. 自定义列表（dl）
   
   ```html
   <dl>                        自定义列表以<dl> 标签开始。
       <dt>名词1</dt>            每个自定义列表项以 <dt> 开始。
       <dd>名词1解释1</dd>            每个自定义列表项的定义以 <dd> 开始。
   </dl>
   ```

### HTML 元数据

```
<meta>标签提供关于 HTML 文档的元数据：描述（description）、关键词（keywords）、文档的作者（author）等其他元数据。在<head>标签中
```

### HTML 块

1. 块级元素
   1. 总是独占一行，表现为另起一行开始，而且其后的元素也必须另起一行显示。宽度(width)、高度(height)、内边距(padding)和外边距(margin)都可控制。
   2. 常见块级元素： <h1>,<p>, <ul>, <table>。
2. 内联元素
   1. 常见内联元素：<b>, <td>, <a>, <img>。
   2. 内联元素在显示时通常不会以新行开始。

### HTML 布局（div，span）

table 元素布局：

- 优点：
1. 理解比较简单。
2. 不同的浏览器看到的效果一般相同。
3. table 在显示数据时更加方便
- 缺点：
1. 显示样式和数据绑定在一起。
2. 布局的时候灵活度不高。
3. 一个页面可能会有大量的 table 元素，代码冗余度高。
4. 增加带宽。
5. 搜索引擎不喜欢这样的布局。

div 元素布局：

- 优点：
1. 符合 W3C 标准。
2. 搜索引擎更加友好。
3. 样式的调整更加方便，内容和样式的分离，使页面和样式的调整变得更加方便。
4. 节省代宽，代码冗余度低。
5. 表现和结构分离，在团队开发中更容易分工合作而减少相互关联性。

### 一些其他的属性

1. lang 属性:规定元素内容的语言。在以下标签中无效：`<base>, <br>, <frame>, <frameset>, <hr>, <iframe>, <param> 以及 <script>。`
2. style属性也比较常见

### 文本格式

| 标签       | 描述                                                                                       |
| -------- | ---------------------------------------------------------------------------------------- |
| <b>      | 定义粗体文本   `<b>新华网</b>`         <b>新华网</b>                                                 |
| <big>    | 定义大号字      `<big>新华网</big>  `    <big>新华网</big>                                          |
| <em>     | 定义着重文字   `<em>新华网</em>`     <em>新华网</em>                                                 |
| <i>      | 定义斜体字       `<i>新华网</i>`         <i>新华网</i>                                              |
| <small>  | 定义小号字       `<small>新华网</small>`       <small>新华网</small>                                |
| <strong> | 定义加重语气   `<strong>新华网</strong>`   <strong>新华网</strong>                                   |
| <sub>    | 定义下标字        `<sub>新华网</sub>`     <sub>新华网</sub>                                         |
| <sup>    | 定义上标字        `<sup>新华网</sup>`      <sup>新华网</sup>                                        |
| <ins>    | 定义插入字     `<ins>新华网</ins>`     <ins>新华网</ins>                                            |
| <del>    | 定义删除字     `<del>新华网</del>`     <del>新华网</del>                                            |
| <font>   | 定义字体属性   `<font color="red" size="4">新华网</font>`   <font color="red" size="4">新华网</font> |

### 文档和网站架构

专用标签:

- 标题：<header>
- 导航栏：<nav>
- 主要内容：<main>具有代表性的内容段落主题可以使用 <article>, <section>，<div>元素。
- 侧栏：<aside>经常嵌套在<main>中
- 页脚：<footer>

## HTML表格

### 表格基本标签

1. `<table>标签` :用于在 HTML 文档中创建表格。它包含表名和表格本身内容的代码。
   1. 语法：`<table>... </table>`；
   2. 属性: 
      1. border 边框厚度
      2. cellspacing:单元格与单元格间距离
      3. cellpadding:文字与单元格之间距离
      4. width;height 宽度,高度
      5. bgcolor:颜色
2. `<tr>标签`          用于定义每一行。
3. `<td>标签`    用于定义每一列。
4. `<th>标签`    用于定义标题;
   1. colspan（合并行）和 rowspan（合并列）属性

## 多媒体与嵌入概述

### 图片

1. 图像标签    `<img> `标签(单标签)    语法为：`<img src="url" alt="" />，
   1. src 的值是图像文件路径。
   2. alt 规定图像的替代文本即当图片未成功显示的时候显示的文本信息。
   3. title 设置鼠标悬停时显示的内容（一般不用设置）
   4. 设置 width 和 height 的值来设置图片的宽和高
2. 相对路径:位于上一级目录就用"../"
3. 绝对路径:
4. **自适应图片**:width和height设置值为auto

### 视频和音频

1. `<video>标签`和`<audio>标签`
   
   | 属性                                                                   | 值        | 说明                                                  |
   | -------------------------------------------------------------------- | -------- | --------------------------------------------------- |
   | [autoplay](https://www.w3school.com.cn/html5/att_video_autoplay.asp) | autoplay | 如果出现该属性，则视频在就绪后马上播放。                                |
   | [controls](https://www.w3school.com.cn/html5/att_video_controls.asp) | controls | 如果出现该属性，则向用户显示控件，比如播放按钮。                            |
   | [height](https://www.w3school.com.cn/html5/att_video_height.asp)     | *pixels* | 设置视频播放器的高度。                                         |
   | [loop](https://www.w3school.com.cn/html5/att_video_loop.asp)         | loop     | 如果出现该属性，则当媒介文件完成播放后再次开始播放。                          |
   | [preload](https://www.w3school.com.cn/html5/att_video_preload.asp)   | preload  | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
   | [src](https://www.w3school.com.cn/html5/att_video_src.asp)           | *url*    | 要播放的视频的 URL。                                        |
   | [width](https://www.w3school.com.cn/html5/att_video_width.asp)       | *pixels* | 设置视频播放器的宽度。                                         |

2. `<source> 标签`:
   
   1. `<source>` 标签为媒介元素（比如` <video> `和` <audio>`）定义媒介资源。

### 矢量图

1.图库

- 阿里巴巴矢量图标库 http://iconfont.cn/
- 谷歌浏览器里的矢量图库 https://icomoon.io/

### iframe嵌入技术

iframe 元素会创建包含另外一个文档的内联框架（即行内框架）。

属性:

| 属性                                                                           | 值                                                               | 说明                               |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------- |
| [align](https://www.w3school.com.cn/tags/att_iframe_align.asp)               | leftrighttopmiddlebottom                                        | 不赞成使用。请使用样式代替。规定如何根据周围的元素来对齐此框架。 |
| [frameborder](https://www.w3school.com.cn/tags/att_iframe_frameborder.asp)   | 10                                                              | 规定是否显示框架周围的边框。                   |
| [height](https://www.w3school.com.cn/tags/att_iframe_height.asp)             | *pixels**%*                                                     | 规定 iframe 的高度。                   |
| [longdesc](https://www.w3school.com.cn/tags/att_iframe_longdesc.asp)         | *URL*                                                           | 规定一个页面，该页面包含了有关 iframe 的较长描述。    |
| [marginheight](https://www.w3school.com.cn/tags/att_iframe_marginheight.asp) | *pixels*                                                        | 定义 iframe 的顶部和底部的边距。             |
| [marginwidth](https://www.w3school.com.cn/tags/att_iframe_marginwidth.asp)   | *pixels*                                                        | 定义 iframe 的左侧和右侧的边距。             |
| [name](https://www.w3school.com.cn/tags/att_iframe_name.asp)                 | *frame_name*                                                    | 规定 iframe 的名称。                   |
| [sandbox](https://www.w3school.com.cn/tags/att_iframe_sandbox.asp)           | ""allow-formsallow-same-originallow-scriptsallow-top-navigation | 启用一系列对 <iframe> 中内容的额外限制。        |
| [scrolling](https://www.w3school.com.cn/tags/att_iframe_scrolling.asp)       | yesnoauto                                                       | 规定是否在 iframe 中显示滚动条。             |
| [seamless](https://www.w3school.com.cn/tags/att_iframe_seamless.asp)         | seamless                                                        | 规定 <iframe> 看上去像是包含文档的一部分。       |
| [src](https://www.w3school.com.cn/tags/att_iframe_src.asp)                   | *URL*                                                           | 规定在 iframe 中显示的文档的 URL。          |
| [srcdoc](https://www.w3school.com.cn/tags/att_iframe_srcdoc.asp)             | *HTML_code*                                                     | 规定在 <iframe> 中显示的页面的 HTML 内容。    |
| [width](https://www.w3school.com.cn/tags/att_iframe_width.asp)               | *pixels**%*                                                     | 定义 iframe 的宽度。                   |

## HTML 表单

#### `<form>` 标签

​    定义html表单

1. 组成部分:
   
   1. 表单标签：这里面包含了处理表单数据所用 CGI 程序的 URL 以及数据提交到服务器的方法。
   2. 表单域：包含了文本框、密码框、隐藏域、多行文本框、复选框、单选框、下拉选择框和文件上传框等。
   3. 表单按钮：包括提交按钮、复位按钮和一般按钮；用于将数据传送到服务器上的 CGI 脚本或者取消输入，还可以用表单按钮来控制其他定义了处理脚本的处理工作。

2. 语法:
   
   ```
   <form name="form_name" method="get/post" action="url"> </form>
   ```
   
   1. name：定义表单的名字。
   
   2. method：定义表单结果从浏览器传送到服务器的方式，默认参数为：get 。post 安全性更高，因此常用作传输密码等，而 get 安全性较低，一般用于查询数据。**使用 get 请求用户将在他们的 URL 栏中看到数据，但是使用 post 请求用户将不会看到。**
   
   3. action：用来指定表单处理程序的位置(服务器端脚本处理程序）。
      
      ```
      <form action="https:.com/">
      <!--数据发送到一个绝对URL：https:.com/-->
      <form action="/somewhere_else">
      <!-- 数据发送到一个相对URL -->
      <form action="#">
      <!-- 数据被发送到表单出现的相同页面上 -->
      ```

#### 表单元素

##### `<input />`元素

1. `<input> `标签规定了用户可以在其中输入数据的输入字段。单标签用法
   
   ```
   <input type="text" name="fname">
   ```

2. type属性
   
   type的值有
   
   | 类型     | 描述                 |
   |:------ |:------------------ |
   | text   | 定义常规文本输入。          |
   | radio  | 定义单选按钮输入（选择多个选择之一） |
   | submit | 定义提交按钮（提交表单）       |

3. required:输入值不能为空,如果输入值为空，将会提示错误信息。

##### `<select> `元素和`<option>`元素

 `<select>`元素定义下拉列表;`option`元素定义待选择选项

```html
<select name="cars">
<option value="volvo" selected >Volvo</option> //selected属性定义默认项
<option value="saab">Saab</option>
</select>
```

##### `<textarea> `元素

```html
元素定义多行输入字段（文本域）：
<textarea name="message" rows="10" cols="30">
The cat was playing.
in the garden.
</textarea>
```
