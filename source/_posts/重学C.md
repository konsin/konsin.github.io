---
title: 重学C++
date: 2022-08-18 15:08:28
categories: 学习笔记
tags: C++
---

## 第一章 

- C++语言的优点，缺点，和主要用途？
  - 优点：
    - 强大的封装抽象能力，强大的开发工程的能力
    - 高性能，运行快，占用资源少
    - 低功耗，特别适合微型嵌入式
  - 缺点
    - 语法相对复杂、细节较多
    - 需要一些好的规范和范式，否则代码难以维护
  - 主要用途
    - 大型桌面应用程序
    - 大型网站后台
    - 游戏和游戏引擎
    - 视觉库和AI引擎
    - 数据库
    - 自动驾驶系统、嵌入式设备等

- 面向对象和面向过程的优缺点

  面向过程

  - 优点：性能比面向对象高，因为类调用时需要实例化，开销比较大，比较消耗资源;比如单片机、嵌入式开发、Linux/Unix等一般采用面向过程开发，性能是最重要的因素。 
  - 缺点：没有面向对象易维护、易复用、易扩展 

  面向对象

  - 优点：易维护、易复用、易扩展，由于面向对象有封装、继承、多态性的特性，可以设计出低耦合的系统，使系统更加灵活、更加易于维护 
  - 缺点：性能比面向过程低 

## 第二章 C++基础语法

### 数据类型

   | 类型               | 位            | 范围                                                         |
   | :----------------- | :------------ | :----------------------------------------------------------- |
   | char               | 1 个字节      | -128 到 127 或者 0 到 255                                    |
   | unsigned char      | 1 个字节      | 0 到 255                                                     |
   | signed char        | 1 个字节      | -128 到 127                                                  |
   | int                | 4 个字节      | -2147483648 到 2147483647                                    |
   | unsigned int       | 4 个字节      | 0 到 4294967295                                              |
   | signed int         | 4 个字节      | -2147483648 到 2147483647                                    |
   | short int          | 2 个字节      | -32768 到 32767                                              |
   | unsigned short int | 2 个字节      | 0 到 65,535                                                  |
   | signed short int   | 2 个字节      | -32768 到 32767                                              |
   | long int           | 8 个字节      | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807      |
   | signed long int    | 8 个字节      | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807      |
   | unsigned long int  | 8 个字节      | 0 到 18,446,744,073,709,551,615                              |
   | float              | 4 个字节      | 精度型占4个字节（32位）内存空间，+/- 3.4e +/- 38 (~7 个数字) |
   | double             | 8 个字节      | 双精度型占8 个字节（64位）内存空间，+/- 1.7e +/- 308 (~15 个数字) |
   | long double        | 16 个字节     | 长双精度型 16 个字节（128位）内存空间，可提供18-19位有效数字。 |
   | wchar_t            | 2 或 4 个字节 | 1 个宽字符                                                   |

### 关键字

   | asm          | else      | new              | this     |
   | ------------ | --------- | ---------------- | -------- |
   | auto         | enum      | operator         | throw    |
   | bool         | explicit  | private          | true     |
   | break        | export    | protected        | try      |
   | case         | extern    | public           | typedef  |
   | catch        | false     | register         | typeid   |
   | char         | float     | reinterpret_cast | typename |
   | class        | for       | return           | union    |
   | const        | friend    | short            | unsigned |
   | const_cast   | goto      | signed           | using    |
   | continue     | if        | sizeof           | virtual  |
   | default      | inline    | static           | void     |
   | delete       | int       | static_cast      | volatile |
   | do           | long      | struct           | wchar_t  |
   | double       | mutable   | switch           | while    |
   | dynamic_cast | namespace | template         |          |

### 命名建议：变量名尽量使用“名词”或“形容词+名词”；函数名用“动词+名词”。原则上长度不超过32位

### 常用命名规则

   1. 匈牙利命名法：开头字母用变量类型缩写后面用变量的英文或缩写
   2. Camel命名法：首单词小写，后面单词首字母大写
   3. Pascal命名法：每个单词第一个字母都大写

### 常量与变量

   1. 常量：在程序运行过程中，值一直保持不变的量

      - 定义方法

        - 使用`#define `方式 `#define PI 3.1415`
        - 使用` const`方式 `const double PI = 3.1415`

        使用const定义常量可以在编译时检查出错误。而define只是宏定义，难以排错

      - 常量类型

        - 整数常量：可以是十进制、八进制或十六进制的常量。

        **前缀**指定基数：0x 或 0X 表示十六进制，0 表示八进制，不带前缀则默认表示十进制。

        **后缀**是 U 和 L 的组合，U 表示无符号整数（unsigned），L 表示长整数（long）。

        - 浮点常量

        小数形式表示时，必须包含整数部分、小数部分，或同时包含两者。

        指数形式表示时， 必须包含小数点、指数，或同时包含两者。e后面指定指数

        - 布尔常量
        - 字符常量

        如果常量以 L（仅当大写时）开头，则表示它是一个宽字符常量（例如 L'x'），此时它必须存储在 **wchar_t** 类型的变量中。

## 第三章 C++运算符与表达式
 
**运算符**：告诉编译器执行特定数学或逻辑操作的符号。（算术运算符、关系运算符、逻辑运算符、位运算符、赋值运算符、杂项运算符）

**表达式**：使用运算符将操作数连接而成的式子，每一个表达式都有自己的值，表达式都有运算结果

**注释的建议**：
  1. 好的命名和代码本身就是最好的注释；如果代码本身很清楚，不需要额外加注释。
  2. 在重要代码段、或复杂代码处先写注释再写代码，这样思路更清晰，同时可以保证代码和注释的一致性。
  3. 注释不是越多越好，它是对代码的提示，如果要写就写清楚，并且保证和代码一致。如果更新的代码，清更新相应的注释。

**补码**：
  有符号数另一种计算方式：![image](https://git.poker/konsin/images/blob/main/image.7ka0cc9pftg0.jpg?raw=true)
  常用计算方式：正数不变；复数 符号位不变，其余位取反，最后加1

**大端方式** 数字高位在低地址
**小段方式** 数字低位在低地址

## 第四章 C++基础容器
### 数组
概念：代表内存里一组连续的同类型存储区；可以用来把多个存储区合并成一个整体
C语言中数组下标：从0开始，使用非对称区间`[,)`，下届可以取到值，上界取不到值。
   好处：
      1. 取值范围的大小：上界 - 下届；
      2. 如果这个取值范围为空， 上界值 == 下界值
      3. 即使取值范围为空，上界值永远不可能小于下界值。
使用：
  1. 通过下下标可以直接访问任意一个元素
  2. 下标从0开始到元素个数减一为止
  3. 超过范围的下标不可以使用
  4. 数组名称和下标可以表示数组里的元素

优点：
  1. 可以编写循环依次处理数组里的所有元素
  2. 循环变量依次代表所有有效下标

**差一错误**：high - low + 1

### vector数组
`#include <vector>`
引入原因：使用最简单的数组，无法实现动态扩容插入元素，因为容量有限。
- 查询大小：`s.size()`
- 查询容量：`s.capacity()`
- 使用sort对vector排序
  `sort(num.begin(), num.end());`
- 插入数据的方式
  尾插 `push_back(val)`
  尾删 `pop_back()`
  插入 `insert()`
  删除 `erase()`
  清空 `clear()`

### 字符串
**定义方式**：
  `char str[] = {"hello"}`
  `char str[6] = {'h','e','l','l','o'}`
**字符串变量**：
  - 字符串是以空字符('\0')结束的字符数组
  - 空字符 '\0'自动添加到字符串的内部表示中
**字符串常量**：
  - 字符串常量是一对双引号括起来的字符串数组
  - 字符串中每个字符作为一个数组元素存储


**Unicode编码**：目的->把世界上的文字都映射到一套字符空间中
  1. UTF-8：1byte表示字符，可以兼容ASCII码；特点是存储效率高，变长（不方便内部随机访问），无字节序问题（可作为外部编码）
  2. UTF-16：分为UTF-16BE（big endian）、UTF-16LE(little endian)。特点是定长（方便内部随机访问），有字节序问题（不可作为外部编码）
  3. UTF-32：分为UTF-32BE、UTF-32LE。特点是定长（方便内部随机访问），有字节序问题（不可作为外部编码）

**字符串指针**：
  - 指针表示方法： `char* pStr = "hello";`
  - char[] 和 char* 的区别：
    - 地址和地址存储的信息
    - 可变与不可变。
    如果数组指针初始化指向字符串常量，那么这个指针所指内容不可发生改变。
    ``` cpp
    char *ps = "hello";  //字符串常量指针
    char s[] = {"hello"};
    char *ps2 = s;       //字符串变量指针
    ```
    s不可变，s[i]的值可变；
    ps可变，ps[i]的值可不可变取决于所指区间的存储区域是否可变。

**常见操作**：
  `strlen(s)`：返回s的长度
  `strcmp(s1, s2)`: 自左到右按ASCII值大小比较 s1 == s2 返回 0； s1 < s2 返回 -； s1 > s2 返回+；
  `strcpy(s1, s2)`: 复制s2到s1；
  `strncpy(s1, s2, n)` 将字符串s2中前n个字符拷贝到s1中
  `strcat(s1, s2)` 将字符串s2接到s1后面
  `strchr(s1,ch)` 查找ch在s1中第一次出现位置
  `strstr(s1, s2)` 查找s2在s1中第一次出现位置。

### string字符串
`#include <string>`
使用string可以更为方便和安全的管理字符串。
定义：`string s`; `string s = "hello"`; `string s("hello")`; `string s = string("hello")`;
**常用操作**
  - 获取长度：
    - `s.length()` 
    - `s.size()`
    - `s.capacity()` 容量 != 长度
  - 字符串比较：`==` `!=` `>` `>=` `<` `<=`
  - 转换为C风格字符串 char*
    `const char *c_s = s.c_str(); `
  - 可通过下标进行随机访问。
  - 可通过`=`进行字符串拷贝
  - 可通过`+`、`+=`连接字符串

## 第五章 指针
指针的缺点：使用指针是非常危险的行为，可能存在空指针，野指针的问题，并可能造成内存泄漏问题。
优点：指针非常的高效
**C++中内存单元内容与地址**
指针的本质：内存划分内存单元用来存放各种类型的数据。计算机对内存单元进行编号，称为内存地址，决定内存单元在内存中的位置。C++编译器让我们通过名字来访问这些内存位置。
指针定义的基本形式： 指针本身就是一个变量，其符合变量定义的基本形式，存储的是值的地址。对类型T，T*是‘到T的指针’类型。通过一个指针访问所指向地址的过程称为间接访问或引用指针。
  小结：
  1. 一个变量有三个重要信息：
     1. 变量的地址位置
     2. 变量所存的信息
     3. 变量的类型
  2. 指针变量是一个专门用来记录变量的地址的变量，通过指针变量可以间接的访问改变另一个变量的值
### C++中原始指针
1. 一般类型指针T*
2. 指针的数组与数组的指针
   指针的数组 T* t[]
   数组的指针 T (*t)[]
3. const pointer 和 pointer to const
   `char const` 和 `const char` 是等价的。
   看const修饰部分：
   - 看左侧最近的部分
   - 如果左侧没有则看右侧
4. 指向指针的指针 
   `*`操作符具有从右向左的结合性 
   `**`表达式相当于`*(*c)`，必须从里向外逐层求值
5. 未初始化和非法的指针
   如果定义到了一个非法地址，程序会出错，从而终止。
   如果定位到一个可以访问的地址，无意修改了它，这种错误难以捕捉，引发的错误可能与原先用于操作的代码完全不相干。
6. NULL指针
   一个特殊的指针，表示不指向任何东西。这种方法来表示特定的指针目前未指向任何东西
   注意事项：
   对应于一个指针如果已经知道被初始化为什么地址，如果不赋值就设置为NULL
   引用指针前先判断是否为NULL

**杜绝野指针**
if等判断对野指针不起作用，因为没有置NULL
一般有三种情况：
  1. 指针变量没有初始化
  2. 已经释放不用的指针没有置NULL，如delete和free之后的指针
  3. 指针操作超越了变量的作用范围。

没有初始化的，不用的或者超出范围的指针把值置为NULL

### 指针的基本运算
1. `&`与`*`操作符
   `&ch`取出来的是地址
   `*cp`为右值时是指向地址的内容，为左值时为指针。
        `*CP+1`左值非法，`*(cp+1)`为下一位指针对应的
2. `++`与`--`操作符
3. 关于`++++`与`----`等运算符
   编译程序分解成符号的方法是：一个字符一个字符的读入，如果该字符可能组成一个符号，那么读入下一个字符，一直到读入的字符不能再组成一个有意义的符号。 a+++b 相当于 a++ +b

### CPP程序存储区域划分
全局变量、常量在常量区，变量在栈区，动态申请变量在堆区。
![5-11-CPP程序的存储区域划分总结-00_05_34-2022_09_20_14_23_02-(2)](https://cdn.staticaly.com/gh/konsin/images@main/5-11-CPP程序的存储区域划分总结-00_05_34-2022_09_20_14_23_02-(2).6mgazj6rwp00.jpg)
1. 栈和队列
   栈：先进后出
   队列：先进先出
2. 动态分配资源-堆（heap）
   程序通常需要牵涉到三个内存管理器的操作：
   1. 分配某个大小的内存块；
   2. 释放一个之前分配的内存块；
   3. 垃圾收集操作，寻找不再使用的内存块并予以释放。（这个回收策略需要实现性能、实时性、额外开销等各方面的平衡，很难有统一和高效的做法）
   C++做了1、2，Java做了1、3。

### 资源管理方案--RAII(Resource Acquisition Is Initialization)
1. 主流的编程语言中，C++是唯一一个依赖RAII做资源管理的。
2. RAII依托**栈**和**析构函数**，来对所有的资源——包括堆内存在内进行管理。对RAII的使用，使得C++不需要类似Java那样的垃圾收集方法也能有效地对内存进行管理。
3. RAII有些比较成熟的智能指针代表：`std::auto_ptr`、`boost::shared_ptr`

### C++中几种变量对比
栈和堆中的变量对比
| | 栈区| 堆区|
|:------------|:------------|:--------------|
|作用域|函数体内，语句块{}作用域|整个程序范围内，由`new`,`malloc`开始，`delete`、`free`结束|
|编译间大小确定|变量大小范围确定|变量大小不确定，需要运行期确定|
|大小范围|Windows默认栈大小1M，linux默认栈大小8M或10M|所有系统的堆空间上限是接近内存（虚拟内存）的总大小的|
|内存分配方式|地址由高到低减少|地址由低到高增加|
|内容是否可变|可变|可变|
全局静态存储区和常量存储区的变量对比
||全局静态存储区|常量存储区|
|:-|:-|:-|
|存储内容|全局变量，静态变量|常量|
|编译期间大小是否确定|确定|确定|
|内容是否可变|可变|不可变|

### 内存泄漏（Memory Leak）问题
1. 什么是内存泄漏问题：
   指程序中已动态分配的**堆内存由于某种原因程序未释放或无法释放**，造成系统内存的浪费，导致**程序运行速度减慢甚至系统崩溃等严重后果**。
2. 内存泄漏发生原因和排查方式：
   1. 内存泄漏主要发生在**堆内存分配方式**中，即“配置了内存后，所有指向该内存的指针都遗失了”。若缺乏语言这样的垃圾回收机制，这样的内存片就无法归还系统。
   2. 因为内存泄漏属于程序运行中的问题，无法通过编译识别，**所以只能在程序运行过程中来判别和诊断**。
比指针更安全的解决方案
1. 使用更安全的指针-智能指针
2. 不使用指针，使用更安全的方式-引用

### 智能指针
C++中四种常用智能指针: unique_ptr、shared_ptr、weak_ptr、在C++17中已经废弃的auto_ptr
1. `auto_ptr`
   由`new expression`获取对象，在`auto_ptr`对象销毁时，其所管理的对象也会自动被`delete`掉。
   所有权转移：不小心把它传递给另外的智能指针，原来的指针就不再拥有这个对象了。在拷贝/赋值过程中，会直接剥夺指针对原对象内存的控制权，转交给新对象，然后再将**原对象指针置为`nullptr`**。
   `auto_ptr<int> pl(new int(10))`
2. `unique_ptr`
   `unique_ptr`是**专属所有权**，所以`unique_ptr`管理的内存，只能被一个对象持有，不支持复制和赋值。
   移动语义：`unique_ptr`禁止了拷贝语义，但是可以使用 `std::move()`进行控制所有权的转移。
3. `shared_ptr`
   `shared_ptr`**通过一个引用计数共享一个对象**，`shared_ptr`是为了解决`auto_ptr`在对象所有权上的局限性，在使用引用计数的机制上提供了可以共享所有权的智能指针。因为引入了引用计数，所以造成了额外的资源浪费，不如`unique_ptr`轻量。
   当引用计数为0时，说明对象没有被使用，可以析构。
   问题：
   循环引用：引用计数会带来循环引用的问题，循环引用会导致堆里的内存无法正常回收，造成内存泄漏。
4. `weak_ptr`
   **`weak_ptr`被设计为与`shared_ptr`共同工作**，用一种观察者模式工作。
   意味着`weak_ptr`只对`shared_ptr`进行引用而不改变其引用计数。

### C++的引用
引用是一种特殊的指针，不允许修改的指针。
：1. 不存在空引用；2. 必须初始化； 3. 一个引用永远指向它初始化的那个对象。
1. 引用的基本使用：可以认为值指定变量的别名，使用时可以认为是变量本身。
   `int& rx = x`, `cout << rx; `等同于`cout << x;`
2. 有了指针为什么还需要引用？ 为了支持函数运算符重载。
3. 有了引用为什么还需要指针？ 为了兼容C语言。

对内置基础类型（int、double等)而言，在函数中传值（pass by value）更高效。
对OO面向对象中自定义类型而言，在函数中传引用(pass by reference to const)更高效。

## 第六章 C++基础句法
单一语句： 在任何一个表达式后面加上分号`;`
复合语句：用一对花括号`{}`括起来的语句块，在语法上等效于一个单一的语句。
### 分支语句
1. `if`语句
if语句是最常用的一种分支语句，也称为条件语句。
（比较好的编程规范是if的花括号不允许不写，即使只是一个单一语句）
```cpp
if(...)
{
  ...
}
else
{
  ...
}
```

2. `switch`语句
```cpp
switch(表达式)
{
  case 常数1: 语句1;  break;
  case 常数2: 语句2;  break;
  ...
  case 常数n: 语句n;  break;
  default: 语句n+1;
}
```
### 枚举结构
1. 使用`#define`和const创建符号常量，而使用enum不仅能够创建符号常量，还能**定义新的数据类型**。
2. 枚举类型enum(enumeration)的声明和定义：
   ```cpp
   enum wT {
    Monday, Tuesday, Wednesday, Tursday, Friday, Saturday, Sunday
   }; //声明枚举类型
   wT weekday; //定义枚举变量
   ```
### 结构体和联合体
1. `struct`定义结构体
   各成员各自拥有自己的内存，各自使用互不干涉，同时存在的，遵循内存对齐原则。一个struct变量的总长度等于所有成员的长度之和。
   ```cpp
   struct Student 
   {
      char name[6];
      int age;
      Score s;
   };
   ```
2. `union`定义联合体
   各成员共用一块内存空间，并且同时只有一个成员可以得到这块内存的使用权(对该内存的读写)，各变量共用一个内存首地址。
   联合体的内存大小：1、至少要容纳最大的成员变量 2、必须是所有成员变量类型大小的整数倍
   ```cpp
   union Score
   {
    double sc;
    char level;
   }
   ```
**结构体中内存对齐问题**：综合考虑内存对数据的处理及最大的数据类型所占字节
   缺省对齐原则：
   32位cpu：
   - char: 任何地址
   - short: 偶数地址
   - int: 4的整数倍地址
   - double： 4的整数倍地址
  可以修改默认编译选项,设置内存按n字节寻址
  ```cpp
  //Visual C++：
  #pragma pack(n)

  //g++:
  __attribute__(aligned(n))
  __attribute__(__packed__)
  ```
### 循环语句
1. while循环
2. do while循环
3. for循环

### 函数
函数将一段逻辑封装起来便于复用。一个C++程序是由若干个源程序文件构成，而一个源程序是由若干函数构成。
1. 函数组成部分：
   - 返回类型：一个函数可以返回一个值。
   - 函数名称：是函数的实际名称，函数名和参数列表一起构成了函数签名。(SDK提供的`undname.exe`程序的作用就是为我们还原函数签名。)
   - 参数
   - 函数主体：函数主题包含一组定义函数执行任务的语句。
2. 函数重载overload 与C++ Name Mangling：相同函数名称然后不同参数则是不同的函数。
   `int test(int a);`、`int test(double a);`
3. 指向函数的指针与返回指针的函数
  每一个函数都占用一段内存单元，它们有一个起始地址，指向函数入口地址的指针称为函数指针。
  - 一般形式：数据类型(*指针变量名)(参数表)； 如`int(*p)(int);`
  - 与返回指针的函数之间的区别：
    ```cpp
    int(*p)(int); //是指针，指向一个函数入口地址
    int* p(int);  //是函数，返回的值是一个指针
    ```
### 命名空间
命名空间这个概念可作为附加信息来区分不同库中相同名称的函数、类、变量等，命名空间即定义了上下文。
本质上，命名空间就是定义了一个范围。
- 定义命名空间
  ```cpp
  namespace konsin
  {
    int test(int a);
  }
  ```
- 使用命名空间，可以再函数内声明这个函数使用的命名空间，也可以全局
  ```CPP
  using namespace konsin; //使用命名空间内所有的函数

  using konsin::test; //使用命名空间内的test函数

  konsin::test(a);  //直接调用命名空间内的test函数
  ```
### 内联函数（inline）
如果一个函数是内联的，那么在编译时，编译器会把该函数的代码副本放置在每个调用该函数的地方。
目的是为了解决程序中函数调用的效率问题。（空间换时间）
注意：内联函数内部不能有太复杂的逻辑，编译器有事会有自己的优化策略，内联不一定起作用。
```cpp
inline int test(){};
```
### 递归
递归背后的数学逻辑是数学归纳法。

递归四个基本准则：
1. 基准情形：无需递归就能解出；
2. 不断推进：每一次递归调用都必须使求解状况朝接近基准情形的方向推进；
3. 设计法则：假设所有的递归调用都能运行；
4. 合成效益法则：求解一个问题的同一个实例时，切勿在不同递归调用中做重复性工作。

递归的缺陷:
1. 空间上需要开辟大量的栈空间。
2. 时间上可能需要有大量的重复运算。
  
递归的优化：
1. 尾递归：所有递归形式的调用都出现在函数的末尾；
2. 使用循环代替
3. 使用动态规划，空间换时间。
  
## 第七章 C++高级语法
### 面向对象
面向对象是软件工程发展到一定阶段为了管理代码和数据提出的一种方法，没有解决以前解决不了的问题，不是万能的。

**面向对象三大特性**：封装，继承，多态。
1. 封装性：数据和代码捆绑在一起，避免外界干扰和不确定性访问，封装可以使得代码模块化。
2. 继承性：让某种类型对象获得另一个类型对象的属性和方法，继承可以扩展已存在的代码。
3. 多态性：同一事物表现出不同事物的能力，即面向不同对象会产生不同的行为，多态的目的则是为了接口重用。

**面向对象的误区**
1. 对象是对现实世界中具体物体的反映，继承是对物体分类的反映？
   错，类只是一个概念的抽象，而不是对现实世界的反映。
2. 面对变化，尽可能少修改原有的逻辑，要扩充逻辑。

### 类
C++使用struct、class来定义一个类，struct的默认成员权限是public，class的默认成员权限是private。
成员权限有：public、protected、private。
1. 构造类Complex `class Complex{}`
2. 构造函数：定义方法`Complex();`,不需要指定返回值类型。在实例化类对象时会自动调用构造函数创建类对象。系统会自动生成一个无参数的默认构造函数，而手动创建有参数的构造函数之后，则系统不会再去创建默认构造函数，会引起部分情况下错误。因此如果手动创建了构造函数，则也需要手动定义无参数的构造函数。
3. 析构函数：定义方法`virtual ~Complex();`，不需要指定返回值类型。在销毁对象时自动调用。
   `virtual`关键字用于实现多态，子类可以重写父类的函数。
4. 运算符重载：
   如果不需要改变变量的值则需要加`const`，具体区分看`+`号重载和`=`号重载
   - 加、减、乘、除符号重载声明：
   ```cpp 
    Complex operator+ (const Complex& x) const {
      return Complex(ref + x.ref);
    }
    ```
   - 等号重载声明
    ```cpp
    Complex& operator= (const Complex& c) {
	    if (this != &c) {
        ref = c.ref;
	    }
	    return *this;
    };
    ```
     - ++、--重载
     ```cpp
    Complex& Complex::operator++ () {
     	ref++;
     	return *this;
    }

    Complex Complex::operator++ (int) {
     	return Complex(ref++);
    }
     ``` 
    - <<、>>流运算符重载。
    标准流无法直接访问类的private属性，此时可以采用友元来解决。
      - 友元函数：在定义一个类的时候，可以把一些函数（包括全局函数和其他类的成员函数）声明为“友元”，这样那些函数就成为该类的友元函数，在友元函数内部就可以访问该类对象的私有成员了。
      - 友元类：一个类 A 可以将另一个类 B 声明为自己的友元，类 B 的所有成员函数就都可以访问类 A 对象的私有成员。

    ```cpp
    friend ostream& operator<<(ostream& os, const Complex &x) {
     	os << "value is  " << x.ref;
     	return os;
    }

    friend istream& operator >> (istream& is, Complex &x) {
     	is >> x.ref;
     	return is;
     }
    ```
   
### IO流
1. C和C++中I/O流对比：
   传统的C中I/O有printf、scanf等函数：
   1. 不可编程，仅仅能识别固有的数据类型
   2. 代码可移植性差，有很多的坑。
   C++中I/O流istream和ostream等：
   1. 可编程，对于类库的设计者来说很有用。
   2. 简化编程，能使得I/O的风格一致。

2. C++中I/O流类层次结构图
|类名|作用|在哪个头文件中声明|
|:-|:-|:-|
|ios|抽象基类|iostream|
||||
|istream|通用输入流和其他输入流的基类|iostream|
|ostream|通用输出流和其他输出流的基类|iostream|
 ||通用输入||
|iostream |输出流和其他输入输出流的基类|iostream|
||||
|ifstream|输入文件流类|fstream|              
|ofstream|输出文件流类|fstream| 
|fstream|输入输出文件流类|fstream|
||||
|istrstream|输入字符串流类|strstream|
|ostrstream|输出字符串流类|strstream|
|strstream|输入输出字符串流类|strstream|
3. IO缓存区
   标准IO提供三种类型的缓存模式：
      1. 按块缓存：如文件系统
      2. 按行缓存：\n
      3. 不缓存。
4. IO流的奇技淫巧
   使用IO流可以灵活的转换字符串为数或数转为字符串。
   ```cpp
   #include <string>       // std::string
   #include <iostream>     // std::cout
   #include <sstream>      // std::stringstream
    
   int main () {
     std::stringstream ss;
     ss << 100;
     int foo,bar;
     ss >> foo;
     std::cout << "foo: " << foo << '\n';   
     return 0;
   ```
### 文件操作
1. 文件操作步骤
   1. 打开文件用于读和写 open；
      文件打开方式：
      - ios::in 打开文件进行读操作（ifstream默认模式）
      - ios::out 打开文件进行写操作（ofstream默认模式）
      - ios::ate 打开一个已有输入或输出文件并查找到文件尾
      - ios::app 打开文件以便再文件尾部添加数据
      - ios::nocreate 如果文件不存在则打开失败
      - ios::trunc 如果文件存在，清除文件原有内容
      - ios::binary 以二进制方式打开  
      `fstrream f;`、 `f.open("x.text", ios::app | ios::binary);`。
   2. 检查打开是否成功 fail；
      `if(!f)` 或者 `if(f.fail)`
   3. 读或者写 read，write；
      `streamsize count = f.gcount();`获取读取到数据大小 。
   4. 检查是否读完 EOF (end of file)；
      `while (!f.eof())`
   5. 使用完文件后关闭文件 close;
      `f.close();`

### 头文件重复包含问题
避免同一个文件被include多次的方式：
1. 使用宏来防止同一文件被多次包含
   ```cpp
   #ifndef __SOMEFILE_H__
   #define __SOMEFILE_H__
   ···
   #endif
   ```
   优点：可移植性好；
   缺点：无法防止宏名重复，难以排错。
2. 使用编译器来防止同一文件被多次包含
   `#pragma once`
   优点：可以防止宏名重复，易排错。
   缺点：可移植性不好。

### 深拷贝和浅拷贝
浅拷贝：只拷贝指针地址，C++默认拷贝构造函数与赋值运算符重载都是浅拷贝。节省空间，但容易引发多次释放。
深拷贝：**重新分配堆内存**，拷贝指针指向内容。浪费空间，但不会导致多次释放。

## 第八章 C++编程思想9
### 软件的设计模式
一个模式描述了一个不断发生的问题及这个问题的解决方案；模式是前人的设计经验上总结出来的对于一些普遍存在的问题提供的通用解决方案。
23种面向对象可复用设计模式。
1. **单例模式**
整个程序中有且只有一个实例。便于访问控制和维护。

实现思路：
      1. Singleton拥有一个私有构造函数，确保用户无法通过new直接实例它；
      2. 包含一个静态私有成员变量`instance`与静态公有方法`instance()`；
   
实现样例：
```cpp
class Singleton
{
public:
	static const Singleton* getInstance()
   {
   	if (!This)
   	{
   		This = new Singleton;
   	}
   	return This;
   };
	static void DoSomething()
	{
		cout << "Do Something" << endl;
	}
// 将构造和析构函数私有化，防止外部访问
private:
	Singleton();
	~Singleton();

	static Singleton* This; // 使用静态变量帮助解决资源的分配和释放
};
```
调用方法其中的DoSomething()方法：`Singleton::getInstance()->DoSomething();`
不能实例化后再调用，而是通过提供的getInstance方法获取实例。

2. **观察者模式**
观察者模式中，观察者需要直接订阅目标事件；在目标发出内容改变事件后，直接接收事件并作出响应，对象常是一对多的关系。 常用于各种MVC框架中，Model的变化通知View。

实现思路：将问题的职责解耦合，将Observable和Observer抽象开，分清抽象和实体。
![image](https://cdn.staticaly.com/gh/konsin/images@main/image.619ssrb6vm80.webp)

在设计观察者模式时要注意以下几点：
- 要明确谁是观察者，谁是被观察者。明白了关注对象，问题也就清楚了；
- Observable在发送广播通知时，无须指定具体的Observer，观察者可以自己决定是否要订阅Observable的通知；
- 被观察者至少有三个方法： 添加监听者、删除监听者和通知监听者；观察者至少有一个方法：更新方法。
观察者模式的应用场景如下：
- 一个对象的数据或状态更新需要其它对象同步更新时；
- 系统存在事件多级触发时；
- 一个对象仅需要将自己的更新通知给其它对象而不需要知道其它对象细节时，如消息推送；
- 跨系统的消息交换场景，如通信过程中的消息队列处理机制。

Observer抽象类定义，具体实现由其继承子类实现：
```cpp
#pragma once

# ifndef OBSEVER_H_1
# define OBSEVER_H_1
class Observer
{
public:
	Observer() { ; }
	virtual ~Observer() { ; }

	// 当被观察对象发生变化时，通知被观察者调用这个方法
	virtual void Update(void* pArg) = 0;
};
# endif
```
Observable类定义：
```cpp
#pragma once

class Observer;

#include <string>
#include <list>
using namespace std;
class Observerable
{
public:
	Observerable();
	virtual ~Observerable();

	// 注册观察者
	void Attach(Observer* pOb);
	// 反注册观察者
	void Detach(Observer* pOb);

	virtual void GetSomeNews(string str)
	{
		SetChange(str);
	}
protected:
	void  SetChange(string news);   // 有变化，需要通知

private:
	void Notify(void* pArg);

private:
	bool _bChange;
	list<Observer*> _Obs;
};
```
Obseverable类实现
```cpp
#include "Observerable.h"


Observerable::Observerable():_bChange(false)
{
}


Observerable::~Observerable()
{
}


// 注册观察者
void Observerable::Attach(Observer* pOb)
{
	if (pOb == NULL)
	{
		return;
	}
	// 看看当前列表中是否有这个观察者
	auto it = _Obs.begin();
	for (; it != _Obs.end(); it++)
	{
		if (*it == pOb)
		{
			return;
		}
	}

	_Obs.push_back(pOb);
}
// 反注册观察者
void Observerable::Detach(Observer* pOb)
{
	if ((pOb == NULL) || (_Obs.empty() == true))
	{
		return;
	}

	_Obs.remove(pOb);
}

void Observerable::SetChange(string news)
{
	_bChange = true;

	Notify( ( (void*)news.c_str() ));
}


void Observerable::Notify(void* pArg)
{
	if (_bChange == false)
	{
		return;
	}

	// 看看当前列表中是否有这个观察者
	auto it = _Obs.begin();
	for (; it != _Obs.end(); it++)
	{
		(*it)->Update(pArg);
	}

	_bChange = false;
}
```
3. 适配器模式（Adapter）
适配器将类接口转换为客户端期望的另一个接口。使用适配器可防止类由于接口不兼容而一起工作。适配器模式的动机是，如果可以更改接口，则可以重用现有软件。
- 第一种适配的方式：**使用多重继承**。
```cpp
class LegacyRectangle
{
public:
	LegacyRectangle(double x1, double y1, double x2, double y2) { ... }

	void LegacyDraw() { ... }

private:
	...
};

class Rectangle
{
public:
	virtual void Draw(string str) = 0;
};

class RectangleAdapter: public Rectangle, public LegacyRectangle
{
public:
	RectangleAdapter(double x, double y, double w, double h) :
		LegacyRectangle(x, y, x + w, y + h)
	{
		...
	}

	virtual void Draw(string str)
	{
		LegacyDraw();
	}
};
```
- 第二种方式：组合方式的Adapter
```cpp

class RectangleAdapter :public Rectangle
{
public:
	RectangleAdapter2(double x, double y, double w, double h) :
		_lRect(x, y, x + w, y + h)
	{
		...
	}

	virtual void Draw(string str)
	{
		_lRect.LegacyDraw();
	}
private:
	LegacyRectangle _lRect;
};
```


### 类型转换
**`void*`,NULL 和 nullptr**
   在C语言中 `#define NULL((void*) 0)`，`void*` 可以转换为任意类型的指针进行传递。
   在C++11中，nullptr用来代替`(void*) 0`，NULL则只表示0。当然如果创建指针时使用NULL，此时NULL则代表空指针。

   C类型转换：
   1. 隐式类型转换: 存在丢失精度的问题。
   2. 显式类型转换：(类型)(表达式)
   
   C++类型转换：
   1. const_cast：用于转换指针或引用，去掉const属性。int a = const_cast<int>(b);
   2. reinterpret_cast: 重新解释类型，既不检查指向内容，也不检查指针类型本身。但要求转换前后的类型所占用内存大小一致，否则引发编译时的错误。**不安全的**
   3. static_cast: 用于基本类型转换，有继承关系类对象和类指针之间转换。可以替换C的显式类型转换。不会产生动态转换的类型安全检查开销。`static_cast<double>(i);`
   4. dynamic_cast：只能用于含有虚函数的类，必须用在多态体系中，用于类层次间的向上和向下转化；向下转化时，如果是非法的，对于指针返回NULL。（防止向下转换）

### 泛型编程（模板）
不同于面向对象的动态期多态，泛型编程是一种静态期多态，通过编译器生成最直接的代码；
泛型编程可以将算法与特定类型、结构剥离，尽可能复用代码。
使用模板类，模板函数实现，`template`关键字。
1. 模板函数示例
   ```cpp
   template<class T>
   T max(T a, T b)
   {
   	return a > b ? a:b;
   }
   ```
   对于某一数据类型的特例，可以采用特化的方法。
   ```cpp
   template<>
   char* max(char* a, char* b)
   {
   	return (strcmp(a, b) > 0 ?  (a) : (b));
   }
   ```
   对于模板函数参数不一致的情况，或者固定的返回值情况。
   ```cpp
   template<class T1, class T2>
   int max(T1 a, T2 b)
   {
   	return static_cast<int>(a > b ? a : b);
   }
   ```
2. 模板类示例
   在函数后面加 `:_a(a)`代表赋值操作，等同于在函数内`_a = a;`
   ```cpp
   template <class T>
   class TC
   {
   public:
   	TC(T a, T b,  T c);

   	T Min()
   	{
   	T minab = _a < _b ? _a : _b;
   	return minab < _c ? minab : _c;
   	};

   private:
   	T _a, _b, _c;
   };

   template<class T>
   TC<T>::TC(T a, T b, T c):
   	_a(a), _b(b), _c(c)
   {
       ;
   }
   ```
## 第九章 C++进阶
### STL算法
STL算法是泛型的，不与任何特定的数据结构和对象绑定，不必在环境类似的情况下重写代码。
STL算法可以量身定做，并具有很高的效率。
STL可以进行扩充，你可以编写自己的组件，并能与STL标准的组件进行很好的配合。
#### STL容器
序列式容器（Sequence Containers）：其中的元素都是可排序的(ordered),STL提供了`vector`, `list`,`deque`等序列式容器,而`stack`, `queue`, `priority_queue`则是容器适配器;
关联式容器(Associative Containers)：每个数据元素都是由一个键(key)和值(Value)组成，当元素被插入到容器时，按其键以某种特定规则放入适当位置;常见的STL关联容器如: `set`, `multiset`, `map`, `multimap`;

- STL函数 `for_each`：具有三个参数，（迭代起始位置，迭代终止位置，函数）
  STL源码：
  ```cpp
  template <class _InIt, class _Fn>
  _CONSTEXPR20 _Fn for_each(_InIt _First, _InIt _Last, _Fn _Func) { // perform function for each element [_First, _Last)
      _Adl_verify_range(_First, _Last);
      auto _UFirst      = _Get_unwrapped(_First);
      const auto _ULast = _Get_unwrapped(_Last);
      for (; _UFirst != _ULast; ++_UFirst) {
          _Func(*_UFirst);
      }

      return _Func;
  }
   ```
   使用方式：
   ```cpp
   struct Display //定义仿函数,可以通过构造函数的方法传入参数。
  {
  	void operator()(int i) //重载了括号运算符，等同于直接定义Display函数
  	{
  		cout << i << " ";
  	}
  };
  for_each( iVector.begin(), iVector.end(), Display() ); //调用方式
   ```
- map使用
  - 定义及插入方式
  ```cpp
   #include<map>
   map<string, double> studentSocres;
   studentSocres["LiMing"] = 95.0;
   studentSocres.insert( pair<string, double>("zhangsan", 100.0) );
   studentSocres.insert(map<string, double>::value_type("zhaoliu", 95.5) );
  ```
  - 遍历方式，查询方式
  ```cpp
   map<string, double>::iterator iter;
   iter = studentSocres.find("zhaoliu");
   iter->first;   iter->second;
   for_each(studentSocres.begin(), studentSocres.end(), Display());
   for (iter = studentSocres.begin(); iter != studentSocres.end(); iter++);
  ```
### 仿函数（functor）
STL仿函数在\<functional\>头文件内。
仿函数主要是为了搭配STL算法使用。
函数指针不能满足STL对抽象性的要求，不能满足软件积木的要求，无法和STL其他组件搭配。
本质是类重载了一个operator()，创建了一个行为类似函数的对象。看上文`Display`结构体.
```cpp
// C++仿函数模板
template<class T>
struct SortTF
{
	bool operator() (T const& a, T const& b) const
	{
		return a < b;
	}
};
```
### STL算法和lambda表达式
常见算法包括：查找、排序和通用算法、排列组合算法、数值算法、集合算法等。STL算法包含于\<algorithm\>、\<numeric\>、\<functional\>。分为：
1. 非可变序列算法:指不直接修改其所操作的容器内容的算法;
2. 可变序列算法:指可以修改它们所操作的容器内容的算法;
3. 排序算法:包括对序列进行排序和合并的算法、搜索算法以及有序序列上的集合操作;
4. 数值算法:对容器内容进行数值计算;

**transform()** 可以将函数应用到序列的元素上，并将这个函数返回的值保存到另一个序列中，它返回的迭代器指向输出序列所保存的最后一个元素的下一个位置。
1. 版本一和 for_each() 相似，可以将一个一元函数应用到元素序列上来改变它们的值
2. 第二个版本的 transform() 允许将二元函数应用到两个序列相应的元素上。
   1. 一元函数使用方式
      共有四个参数：它的前两个参数是定义输入序列的输入迭代器，第 3 个参数是目的位置的第一个元素的输出迭代器，第 4 个参数是一个二元函数。
      
      例： `transform(begin(deg_C), end(deg_C), rbegin(deg_F),[](double temp){ return 32.0 + 9.0*temp/5.0; });` 
      将函数处理后的deg_C数值保存在deg_F中

   2. 二元函数使用方式
      应用二元函数的这个版本的 transform() 含有 5 个参数：
      前两个参数是第一个输入序列的输入迭代器。
      第3个参数是第二个输入序列的开始迭代器，显然，这个序列必须至少包含和第一个输入序列同样多的元素。
      第4个参数是一个序列的输出迭代器，它所指向的是用来保存应用函数后得到的结果的序列的开始迭代器。
      第5个参数是一个函数对象，它定义了一个接受两个参数的函数，这个函数接受来自两个输入序列中的元素作为参数，返回一个可以保存在输出序列中的值。
     
      例：`transform(ones, ones + 5, twos, results, std::plus<int>());` 将one和tow的值相加保存在results中。

**lambda表达式**：定义了一个匿名函数，并且可以捕获一定范围内的变量。
格式为`[ capture ] ( params ) opt -> ret { body; };`，示例：
```cpp
[ ](int a)->void {
		cout << a << endl; }
```
**bind方法绑定参数**
在C++14中lambda支持多态，完全可以不用bind方法了。
`#include <functional>`
`bind1st()`和`bind2nd()`都是把二元函数转化为一元函数，方法是绑定其中一个参数。
`bind1st()`是绑定第一个参数。`bind2nd()`是绑定第二个参数。

`bind()`方法：可以绑定任意个参数`bind (Fn&& fn, Args&&... args);`具体使用见下文`count_if`
`std::placeholders::_1` 占位符位于std命名空间的placeholders命名空间中。其中_1, _2, _3是未指定的数字对象，用于function的bind中。 _1用于代替回调函数中的第一个参数， _2用于代替回调函数中的第二个参数。
```cpp
int TestFunc(int a, char c, float f)
auto bindFunc3 = bind(TestFunc, std::placeholders::_2, std::placeholders::_3, std::placeholders::_1);
bindFunc3(100.1, 30, 'C');
```
在bind的时候，第一个位置是TestFunc，除了这个，参数的第一个位置为占位符std::placeholders::_2，这就表示，调用bindFunc3的时候，它的第二个参数和TestFunc的第一个参数匹配，以此类推。

**查找函数**
`count`函数查找元素并返回个数。`count(begin, end, num)`
`count_if`:可加条件判断。 `count_if(numbers, numbers + 6, bind(less<int>(), std::placeholders::_1, 40));`
`binary_search`二分查找：查找元素是否存在。`binary_search(arr, arr + len, 9)`
`search`查找子序列：`*search(arr, arr + len, iA.begin(), iA.end())` 前两个参数指定序列，后两个参数指定子序列。返回一个地址，间接引用得到下标。

### 迭代器（iterator）
迭代器本质上是一种smater pointer，用于访问顺序容器和关联容器中的元素，相当于容器和操作容器算法之间的中介。
按定义方式分类：1. 正向迭代器(iterator); 2. 常量正向迭代器(const_iterator); 3. 反向迭代器(reverse_iterator); 4. 常量反向迭代器(const_reverse_iterator)
|容器|迭代器功能|
| -- | -- |
|vector|随机访问|
|deque|随机访问|
|list|双向访问|
|set/multiset|双向访问|
|map/multimap|双向访问|
|stack|不支持迭代器|
|queue|不支持迭代器|
|priority_queue|不支持迭代器|
使用示例：`for (vector<int>:: iteratorit = v.begin(); it != v.end(); it++)`。迭代器不支持`<`、`>`

### 适配器(adapter)
1. stack 堆栈：一种”先进后出”的容器，底层数据结构是使用的deque;
2. queue 队列：一种”先进先出”的容器，底层数据结构是使用的deque;
3. priority_queue 优先队列：一种特殊的队列，它能够在队列中进行排序(堆排序)，底层实现结构是vector或者deque;
```cpp
priority_queue<int> pq;  // 默认是最大值优先
priority_queue<int, vector<int>, greater<int> > pq3; // 最小值优先
```

### 空间配置器(allocator)
allocator隐藏在其他组件中默默工作，不需要关心。allocator的分析可以体现C++在性能和资源管理上优化思想。是理解STL最先分析的组件。
要学很底层再看。。。

### Boost库
早期C++使用Boost库可以避免重复造轮子，现在？
https://www.boost.org/
https://www.boost.org/users/download/

### 多线程





