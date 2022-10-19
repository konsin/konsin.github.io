---
title: C++与正则表达式
date: 2022-10-19 15:46:17
tags:
    - C++
    - 正则表达式
categories:
    - 学习笔记
---
## 引入方式
   C++中正则表达式的API基本上都位于`<regex>`头文件中。`#include <regex>`
   引入正则后，定义正则表达式：`regex ex(string)`

## 基本的正则文法（regex syntaxes）
std::regex默认使用是ECMAScript文法，这种文法比较好用，且威力强大，常用符号的意义如下：

|符号|	意义|
|:--|:--|
|`^`|	匹配行的开头|
|`$`|	匹配行的结尾|
|`.`|	匹配任意单个字符|
|`[…]`|	匹配[]中的任意一个字符|
|`(…)`|	设定分组|
|`\`|	转义字符|
|`\d`|	匹配数字[0-9]|
|`\D`|	\d 取反|
|`\w`|	匹配字母[a-z]，数字，下划线|
|`\W`|	\w 取反|
|`\s`|	匹配空格|
|`\S`|	\s 取反|
|`+`|	前面的元素重复1次或多次|
|`*`|	前面的元素重复任意次|
|`?`|	前面的元素重复0次或1次|
|`{n}`|	前面的元素重复n次|
|`{n,}`|	前面的元素重复至少n次|
|`{n,m}`|	前面的元素重复至少n次，至多m次|
|`\|`|	逻辑或|

## 正则匹配
匹配是判断给定的字符串是否符合某个正则表达式。使用`regex_match`函数，匹配成功返回`true`。
`bool ret = std::regex_match(string_given, ex);`
如果要获得匹配结果可以使用`regex_match`的重载形式。
```cpp
std::cmatch cm; //C风格字符串。
std::smatch sm; //string字符串，sm.str()获取值
auto ret = std::regex_match(string_given, m, ex));
```
## 正则搜索
搜索是在一大段文本中搜索匹配的目标,并非完全匹配。。使用`regex_search`
使用方式：
```cpp
regex_search(string_given, ex);
regex_search(string_given, match, ex); //match保存搜索结果
```
## 正则分割（Tokenize）
C++没有提供很快捷的字符串分割算法，可以用正则。
```cpp
std::string mail("123@qq.vip.com,456@gmail.com,789@163.com,abcd@my.com");
std::regex reg(",");
std::sregex_token_iterator pos(mail.begin(), mail.end(), reg, -1); //-1表示获取正则匹配序列之前的字符串。0表示匹配的子串
std::sregex_token_iterator end;
for (; pos != end; ++pos)   //遍历分割后的数组
{
	std::cout << pos->str() << std::endl;
}
```
## 正则替换
正则表达式内容替换为指定内容，使用`regex_replace`方法。
`string r = regex_replace(pre_str, ex, need_str);`




