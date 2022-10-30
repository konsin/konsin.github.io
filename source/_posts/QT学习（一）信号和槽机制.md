---
title: QT学习（一）信号和槽机制
date: 2022-10-24 18:56:29
tags: 
- QT
- C++
categories: 学习笔记
---
槽的本质是类的成员函数。参数任意，可以是虚函数。槽通常和信号连接在一起，当信号被发出时，与这个信号连接的槽函数就会被调用。
### **语法：**
    `connect(sender, SIGNAL(signal), reveiver, SLOT(slot));`
    参数如下：
    - sender：发出信号的对象，指向发送信号对象的指针。
    - signal：发送对象发出的信号。不带参数的函数名，SIGNAL()将函数名转为字符串并传入connect()中
    - receiver：接收信号的对象，指向包含槽函数的对象的指针。
    - slot：接收对象在接收到信号之后需要调用的函数。不带参数的函数名，SLOT()将函数名转为字符串并传入connect()中
**信号与槽的连接移除示例：**
1. 一个信号连接多个槽
   ```cpp
   connect(sender, SIGNAL(signal), reveiverA, SLOT(slotA));
   connect(sender, SIGNAL(signal), reveiverB, SLOT(slotB));
   ```
2. 多个信号连接同一个槽
   ```cpp
   connect(senderA, SIGNAL(signalA), reveiverA, SLOT(slotA));
   connect(senderB, SIGNAL(signalB), reveiverA, SLOT(slotA));
   ```
3. 一个信号连接另一个信号
   ```cpp
   connect(sender, SIGNAL(signalA), reveiver, SIGNAL(signalB));
   ```
4. 移除信号与槽的连接
   ```cpp
   disconnect(sender, SIGNAL(signal), reveiver, SLOT(slot));
   ```

### **QT信号槽机制的优缺点：**
- 可减少程序员编写的代码量。
- 信号可以对应多个槽，也可以多个槽映射一个信号。
- 信号和槽的建立与解除绑定十分自由。
- 信号和槽相对于回调函数时间损耗很大。
- 信号和槽参数限定很多，不能携带模板类参数，不能出现宏定义等。

示例代码文件解读：
```cpp
/*
 *widget.h 头文件
 */
#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPushButton> //引入按钮模块

QT_BEGIN_NAMESPACE //定义自己命名空间
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget //继承自基类QWidget
{
    Q_OBJECT //Q_OBJECT宏，只有继承了QOBJECT类的宏才具有信号和槽。该宏是任何实现信号、槽或属性的强制性要求。

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    Ui::Widget *ui;
    QPushButton button1; //声明一个按钮
};
#endif // WIDGET_H


#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    //ui->setupUi(this);
    button1.setParent(this); //绑定窗口和按钮
    button1.setText("关闭"); //按钮中文本
    button1.move(100, 100); //定义按钮的位置，以左上角为原点。
    connect(&button1, &QPushButton::pressed, this, &Widget::close);
}

Widget::~Widget()
{
    //delete ui;
}
```
> 代码中在类定义的第一行写上了`Q_OBJECT`来声明`Q_OBJECT`宏。这个宏为类提供了信号和槽机制、国际化机制、以及Qt提供的不基于C++ RTTI（Runtime Type Identification）的反射能力。其他很多操作都会依赖这个宏，即使类中不需要使用信号和槽也需要添加这个宏。

### **自定义槽函数和自定义信号**
要点：
- 发送者和接受者都需要QObject的派生类（槽函数是全局函数、Lambda表达式等无需接收者的时候除外）
- 使用`signals`标记信号，信号是一个函数声明，返回void，不需要实现函数代码。
- 使用`emit`在恰当位置发送信号。
- 可以在main.cpp中使用`QObject::connect()`函数连接信号和槽函数。
- 槽函数可以传入参数，但是没有返回值。
- 任何成员函数、静态成员函数、全局函数及Lambda表达式都可以作为参函数。与信号函数不同，槽函数必须自己完成实现代码。槽函数就是普通的成员函数。
```cpp
/**
 * newspaper.h文件
 **/
#ifndef NEWSPAPER_H
#define NEWSPAPER_H

#include <QMainWindow>


QT_BEGIN_NAMESPACE
namespace Ui { class NewsPaper; }
QT_END_NAMESPACE

class NewsPaper : public QMainWindow
{
    Q_OBJECT

public:
    NewsPaper(const QString name):m_name(name){};
    ~NewsPaper();
    void sent();    //定义发送自定义信号的函数
signals:
    void newPaper(const QString &name); //定义信号，无需实现，可以有参数，返回类型必须为void
private:
    Ui::NewsPaper *ui;
    QString m_name;
};
#endif // NEWSPAPER_H

/**
 * reader.h文件
 **/
#ifndef READER_H
#define READER_H

#include <QWidget>
class Reader : public QWidget
{
    Q_OBJECT
public:
    Reader();
    void receiveNews(const QString &name); //简单函数，负责输出接收到的参数name。

};

#endif // READER_H

/**
 * newspaper.cpp文件
 **/
#include "newspaper.h"
#include "./ui_newspaper.h"


NewsPaper::~NewsPaper()
{
    delete ui;
}

void NewsPaper::sent(){
    emit newPaper(m_name);
}

/**
 * reader.cpp文件
 **/

#include "reader.h"
#include "QDebug""
Reader::Reader()
{
}
void Reader::receiveNews(const QString &name){
    qDebug() << "reveive news: " << name;
}

/**
 * main.cpp文件
 **/
#include "newspaper.h"
#include "reader.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    NewsPaper newsPaper("NewsPaper:A ");
    Reader reader;
    QObject::connect(&newsPaper,&NewsPaper::newPaper, &reader, &Reader::receiveNews);
    newsPaper.sent();
    return a.exec();
}
```
>上文输出采用了qDebug，这是因为std::cout不支持QString字符串的输出，如果要用cout需要把字符串转为stdString

### **Lambda表达式**
基本语法:
>[函数对象参数] (操作符重载函数参数) mutable或exception ->返回值{函数体}
1. 函数对象参数：
   以`[]`标识一个Lambda表达式的开始。函数对象参数是传递给编译器自动生成桉树对象类的构造函数的。函数对象参数只能使用那些到定义Lambda表达式为止时Lambda所在作用范围内可见的局部变量（包括所在类的this）。参数形式：
   - 空，没有使用任何函数对象参数。
   - “=”，函数体内可以使用Lambda表达式所在作用范围内所有可见的局部变量（包括所在类的this）。是值传递方式
   - “&”，函数体内可以使用Lambda表达式所在作用范围内所有可见的局部变量（包括所在类的this）。是引用传递方式
2. 操作符重载函数参数、
   以`()`标识重载的操作符的参数，没有参数时，可以省略。参数可以通过按值和按引用两种方式进行传递。
3. 可修改标识符
   mutable声明，可省略。按值传递函数对象参数时，加上mutable后可以修改按值传递进来的副本。
4. 错误抛出标识符
   exception声明，这部分也可以声乐。exception声明用于指定函数抛出的异常，使用throw()方法
5. 函数返回值
   以`->`标识函数返回值类型。当返回值为void或者只有一处返回时可以省略，因为编译器可以自动推导类型。
6. 函数体
   不可省略，但可为空。
示例：
```cpp
connect(&button1, &QPushButton::pressed,this,
            [=]()-> void {
        button1.setText("Hello");
    });
```



