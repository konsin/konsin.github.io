---
title: QT学习（四）常用容器
date: 2022-12-01 16:30:16
tags: 
- QT
- C++
categories: 学习笔记
---
相对于C++ STL里的容器，QT也提供了容器，且与STL模板兼容。
## 顺序容器
### QList
> QList、QVector(在qt6中，QVector是QList别名)
1. 引入容器：`#include <QList> `
2. 定义：`QList<int> vals = {1, 2, 3, 4, 5}; `
3. 容器大小：` vals.size();`
4. 首元素：` vals.first();`
5. 尾元素：` vals.last();`
6. 尾插：`vals.append()`
7. 头插：`vals.prepend()`
8. 一种遍历方式：
```cpp
for (int val : vals) 
      qDebug() << val ; 
```

>**tips:** QCollator类

QCollator使用QLocale和可选的排序策略进行初始化。它尝试用指定的值初始化collator。然后，可以使用collator以依赖于语言环境的方式对字符串进行比较和排序。
```cpp
QLocale cn(QLocale::Chinese); 
QCollator collator(cn); 
std::sort(authors.begin(), authors.end(), collator); 
```
> QStringList

QStringList仍包含于QList中。
```cpp
QString string = "coin, book, cup, pencil, clock, bookmark"; 
QStringList items = string.split(",");
```
使用Java风格的const迭代器遍历QStringList
- hasNext()判断是否有下一项
- next()：返回下一项并将迭代器前进一个位置。
```cpp
QStringListIterator it(items); 
while (it.hasNext()) 
    qDebug() << it.next(); 
```
使用C++风格的iterator迭代器遍历：
```cpp
QStringList::Iterator it=items.begin(); 
while (it!=items.end()) 
    qDebug() << (*it++).trimmed() ;
```

## 关联容器
### QSet
- 提供具有快速查找功能的单值集。
- 不支持排序。values方法返回一个QList，其中包含QSet中的元素。
- unite方法执行两个集合的并集。

1. 引入：`#include <QSet> `
2. 定义：`QSet<QString> cols1 = {"yellow", "red", "blue"};`
3. 求并集：`cols1.unite(cols2); `
4. 大小：`cols1.size()`
5. 插入元素：`cols1.insert("brown"); `
6. 遍历方式：
   ```cpp
   for (const QString &val : cols1) 
        out << val << endl; 
   ```
### QMap
1. 引入：`#include <QMap> `
2. 定义：`QMap<QString, int> items = { {"coins", 5}, {"books", 3} }; `
3. 插入：`items.insert("bottles", 7);  `
4. 大小：`items.size()`
5. 获取所有值：`QList<int> values(items.cbegin(),items.cend());`
    使用了cbegin()，cend()迭代器
7. 获取所有键：`QList<QString> keys(items.keyBegin(),items.keyEnd());`
   使用了keyBegin()，keyEnd()迭代器
8. 