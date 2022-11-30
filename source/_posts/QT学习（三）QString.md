---
title: QT学习（三）QString操作
date: 2022-11-15 15:09:47
tags: 
- QT
- C++
categories: 学习笔记
---
>QString存储16位QChar（Unicode）字符串。
>QString使用隐式共享（copy-on-write）来提高性能。

**初始化方式**
>由于QString是Qchar类型，如果从C++ String转换为QString时，需要先通过c_str()转化为C风格字符串。
```cpp
int main(void){ 
  QString str1 = "The night train"; 	
  qDebug()  << str1; QString str2("A yellow rose"); 		
  qDebug()  << str2; QString str3 {"An old falcon"}; 		
  qDebug()  << str3; std::string s1 = "A blue sky"; 
  QString str4 = s1.c_str(); 		
  qDebug()  << str4; std::string s2 = "A thick fog"; 
  QString str5 = QString::fromLatin1(s2.data(), s2.size()); 
  qDebug()  << str5; char s3[] = "A deep forest"; 
  QString str6(s3); 			
  qDebug()  << str6;
}
```

**访问字符串元素：**
可以通过`[]`索引和at方式访问字符串元素。
>operator[]返回的是可以修改的QChar&。
>at返回为const QChar,为只读，更高效。

**构建字符串**
```cpp
QString s3 = "We have %1 lemons and %2 oranges"; 
int ln = 12; 
int on = 4; qDebug() << s3.arg(ln).arg(on) ; 
```

**截取字串的方式**
```cpp
str.right(5); 
str.left(9); 
str.mid(4, 5); 
```


**遍历字符串的几种方式**
```cpp
for (QChar qc: str) 
	out << qc << " "; out << endl; 
for (QChar *it=str.begin(); it!=str.end(); ++it) 
	out << *it << " " ; out << endl; 
for (int i = 0; i < str.size(); ++i) 
	out << str.at(i) << " "; 
```

**字符串比较**
QString::compare返回整型：
0表示相等
负数表示小于
正数表示大于

**字符类型判断**
```cpp
for (QChar s : str) { 
  if (s.isDigit()) {digits++;}          //判断数字
  else if (s.isLetter()) {letters++;}   //判断字母
  else if (s.isSpace()) {spaces++;}     //判断空白字符
  else if (s.isPunct()) {puncts++;}     //判断标点符号
}
```
**字符串类型转换**
转为int型 s1.toInt() 
转为字符串 setNum(n1) 

**字符串修改操作**
`str.append(" season")`：追加字符串
`str.remove(10, 3)`：移除index =10 后的三个字符
`str.replace(7, 3, "girl")`：替换 index = 7 后的三个字符为新字符串
`str.clear(); `：清空字符串

**对齐字符串**
可以使用leftJustified和rightJustified来对齐字符串
```cpp
QString field3 { "Residence: " }; 
QString field4 { "Marital status: " }; 
int width = field4.size(); 
qDebug() << field3.rightJustified(width, ' ') << "New York"; 
qDebug() << field4.rightJustified(width, ' ') << "single"; 
```
>     Residence: New York
>Marital status: single


**转码为html格式**
```cpp
QString allText = "<\"hello the world!\">"; 
qDebug() << allText.toHtmlEscaped(); 
```
>&lt;&quot;hello the world!&quot;&gt;






