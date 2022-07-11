---

title: python学习笔记
date: 2020-03-27 17:14:58
categories: 学习笔记
tags: Python

---

1. 每调用一次 `print()` 就会换一次行，你可以通过 `print()` 的另一个参数 `end` 来替换这个换行符
   
   ```
   print("my name is %s.I am %d years old" % ('Shixiaolou',4))
   ```

2. `print("{:5d}".format(a)) ` 格式化输出语句.{:5d} 输出长度5的整型,str.format()传递参数

3. ```
   print("-" * 50)
   ```
   
   字符串若是乘上整数 n，将返回由 n 个此字符串拼接起来的新字符串。

4. **while** 
   
   ```python
   while n <= 100:
       term *= x / n
       result += term
       n += 1
       if term < 0.0001: 
           break            
   ```

5. for语句
   
   ```
   for x in a:
   for x in a[:]:
   for i in range(5):  range(i,j,k) 以间隔K访问第i到第j个的数据.i和 k可省略
   ```
   
   1. 可以在循环后面使用可选的 `else` 语句。它将会在循环完毕后执行，除非有 `break` 语句终止了循环。

6. **列表/序列(有点像数组?)  竟然还可以当作栈和队列使用**
   
   1. ```
      a[0],访问第一个.
      a[-1],访问末尾第一个
      切片: 切片并不会改变正在操作的列表，切片操作返回其子列表
          省略的第一个索引默认为零，省略的第二个索引默认为切片的字符串的大小：a[:]
          a[i:j],访问第i到第j个的.
          a[i:j:k]:以间隔K访问第i到第j个的数据.
      ```
   
   2. ```
      列表也支持连接这样的操作，它返回一个新的列表：
       a + [36, 49, 64, 81, 100]
      ```
   
   3. 切片赋值，此操作可以改变列表的尺寸，或清空它
      
      ```python
      >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
      >>> # 替换某些值
      >>> letters[2:5] = ['C', 'D', 'E']
      >>> letters
      ['a', 'b', 'C', 'D', 'E', 'f', 'g']
      >>> # 现在移除他们
      >>> letters[2:5] = []
      >>> letters
      ['a', 'b', 'f', 'g']
      >>> # 通过替换所有元素为空列表来清空这个列表
      >>> letters[:] = []
      ```
   
   4. `len()` 可查看长度 ; `type()` 可查看类型
   
   5. 检查某值是否在列表中.
      
      ```
      >>> a = ['ShiYanLou', 'is', 'cool']
      >>> 'cool' in a
      True
      ```
   
   6. 检查列表是否为空 `if list_name:`
   
   7. 列表允许嵌套
   
   8. ```
      a.append(45) 在列表末尾添加数字45
      ```
   
   9. ```
      a.insert(1, 2) 在索引1处插入数字2
      ```
   
   10. ```
       a.count(45)  统计 45 这个元素在列表中出现了多少次。
       ```
   
   11. ```
       a.remove(234) 移除列表中 值为234的数据
       ```
   
   12. ```
       a.reverse()  反转列表
       ```
   
   13. ```
       a.extend(b) # 添加 b 的元素而不是 b 本身  类似于a + b
       ```
   
   14. ```
       del a[-1]   删除a[-1]位置的元素
       ```
   
   15. ```
       遍历两个序列类型，你可以使用 zip() 函数。
       for x, y in zip(a, b):
       ...     print("{} uses {}".format(x, y))
       ```
   
   16. ```
       遍历列表（或任何序列类型）的同时获得元素索引值，你可以使用 enumerate()。
       for i, j in enumerate(['a', 'b', 'c']):
       ...     print(i, j)
       ```
   
   17. ```
       当作栈或队列时
       a.append() 类似于push
       a.pop()   栈的pop
       a.pop(0)   队列的pop
       ```

7. **列表推导式**
   
   1. ```
      for x in range(10):
           squares.append(x**2)
      ```
   
   2. ```
      squares = list(map(lambda x: x**2, range(10)))
      ```
   
   3. ```
      squares = list(map(lambda x: x**2, range(10)))
      ```

8. **元组**
   
   1. 元组是由数个逗号分割的值组成。
   2. 元组是不可变类型
   3. divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

9. **集合**  集合是一个**无序不重复元素**的集。
   
   1. 集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算
   
   2. 大括号或 set() 函数可以用来创建集合。
      
      **注意**：想要创建空集合，你必须使用 set() 而不是 {}。后者用于创建空字典，
   
   ```
   >>> a.pop()  # pop 方法随机删除一个元素并打印
   'h'
   >>> a.add('c')    #插入一个元素 字符c
   ```

10. **字典**(dict)  是无序的键值对（`key:value`）集合
    
    1. ```
       创建字典: data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
       ```
    
    2. 创建新的键值对：
       
       ```
       data['parthan'] = 'Ubuntu'
       ```
    
    3. `del` 关键字删除任意指定的键值对
       
       ```
       del 关键字删除任意指定的键值对
       ```
    
    4. 使用 `in` 关键字查询指定的键是否存在于字典中
       
       ```
       'ShiYanLou' in data
       ```
    
    5. `dict()` 可以从包含键值对的元组中创建字典。
       
       ```
       dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
       {'Indian': 'Delhi', 'Bangladesh': 'Dhaka'}
       ```
    
    6. 遍历字典用`items()`方法
       
       ```
       for x, y in data.items():
       ```
    
    7. 往字典中的元素添加数据
       
       ```
       data.setdefault('names', []).append('Ruby')
       ```
    
    8. 使用 `dict.get(key, default)` 来索引键，如果键不存在，那么返回指定的 default 值。

11. **字符串**
    
    1. 字符串标识 "..."和'...'都能表示,**区别?**
    
    2. 如果你想要分几行输入字符串，并且希望行尾的换行符自动包含到字符串当中，可以使用三对引号：`"""..."""` 或 `'''...'''` 。
       
       ```
       print("""\
        Usage: thingy [OPTIONS]
             -h                        Display this usage message
             -H hostname               Hostname to connect to
        """)
       ```
    
    3. 方法 `title()` 返回字符串的标题版本，即单词首字母大写其余字母小写。
    
    4. 方法 `upper()` 返回字符串全部大写的版本，反之 `lower()` 返回字符串的全部小写
    
    5. 方法 `swapcase()` 返回字符串大小写交换后的版本 :
    
    6. 方法 `isalnum()` 检查所有字符是否只有字母和数字
    
    7. 方法 `isalpha()` 检查字符串之中是否只有字母。
    
    8. 使用 `split()` 分割任意字符串，`split()` 允许有一个参数，用来指定字符串以什么字符分隔（默认为 `" "`）
    
    9. 方法 `join()` 使用指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入然后连接列表内的字符串元素。
       
       ```
       >>> "-".join("GNU/Linux is great".split())
       'GNU/Linux-is-great'
       ```
    
    10. `strip(chars)`，用来剥离字符串首尾中指定的字符,不指定参数则默认剥离掉首尾的空格和换行符
    
    11. 使用 `lstrip(chars)` 或 `rstrip(chars)` 只对字符串左或右剥离。
        
        ```
        s.lstrip("cwsd.") #删除在字符串左边出现的'c','w','s','d','.'字符
        ```
    
    12. 文本搜索
        
        ```
        s.find("fora")   #find() 找到第一个匹配的子字符串，没有找到则返回 -1。
        -1
        >>> s.startswith("fa") # 检查字符串是否以 fa 开头
        True
        >>> s.endswith("reason") # 检查字符串是否以 reason 结尾
        True
        ```
    
    13. z = s[::-1]  #把输入的字符串s 进行倒序处理形成新的字符串z

12. **函数**
    
    1. 定义
       
       ```
       def 函数名(参数):
           语句1
           语句2
       ```
    
    2. 函数可以通过关键字参数的形式来调用，形如 keyword = value。如下：
       
       ```
       >>> def func(a, b=5, c=10):
       ...     print('a is', a, 'and b is', b, 'and c is', c)
       ...
       >>> func(12, 24)
       a is 12 and b is 24 and c is 10
       >>> func(12, c = 24)
       a is 12 and b is 5 and c is 24
       >>> func(b=12, c = 24, a = -1)
       a is -1 and b is 12 and c is 24
       在上面的例子中你能看见调用函数时使用了变量名，比如 func(12,c = 24)，这样我们将 24 赋给 c 且 b 具有默认值。
       ```
    
    3. 强制关键字参数
       
       函数的参数标记为只允许使用关键字参数.
       
       ```
        def hello(*, name='User')
        输入hello('shiyanlou')报错
        hello('shiyanlou') 正确
       ```
    
    4. **文档字符串**????不太懂,继续看
       
       ```
       __doc__ 属性表示函数中中的注释部分
       ```

    5. 高阶函数（*Higher-order function*）或仿函数（*functor*）是可以接受函数作为参数的函数：
    
       ```
       # 创建一个函数，将参数列表中每个元素都变成全大写
       >>> def high(l):
       ...     return [i.upper() for i in l]
       ...
       # 创建高阶函数，接受一个函数和一个列表作为参数
       >>> def test(h, l):
       ...     return h(l)
       ...
       >>> l = ['python', 'Linux', 'Git']
       # 运行高阶函数，返回预期的结果
       >>> test(high, l)
       ['PYTHON', 'LINUX', 'GIT']
       ```
    
    6. **`map`函数**
    
       接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器）
    
     `if __name__ == '__main__':` 这条语句，它的作用是，只有在当前模块名为 `__main__` 的时候（即作为脚本执行的时候）才会执行此 `if` 块内的语句。

13. **文件**
    
    1. 打开文件
       
       ```
       fobj = open("sample.txt")
       或者
       with open('sample.txt') as fobj:使用 with 语句处理文件对象，它会在文件用完后会自动关闭
       ```
    
    2. 关闭文件 `fobj.close()`
    
    3. 读取文件
       
       ```
       使用 read() 方法一次性读取整个文件。 可是传入参数size
       readline() 能帮助你每次读取文件的一行。
       使用 readlines() 方法读取所有行到一个列表中。
       循环遍历文件对象来读取文件中的每一行。    for x in fobj:
                                       ...     print(x, end = '')
       ```
    
    4. 文件写入 ` write() `添加到文末
       
       ```
       fobj.write('powerpork\n')
       ```
    
    5. 拷贝文件
       
       1. sys模块
          
          ```
          sys.argv包含所有命令行参数.
          sys.argv[0]是命令自身的名字
          ```
       
       2. ```
          enumerate(iterableobject)索引位置和对应值可以使用它同时得到
          ```
    
    6. 文本统计
       
       ```
       count()函数 str.count("char", start,end),统计在start-end中字符char的次数
       ```
    
    7. with语句
       
       它会在文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写

14. **异常处理**
    
    1. `try...except`块处理异常
       
       `except  SyntaxError`语法异常
       
       `except NameError`未定义变量异常
       
       `except TypeError` 类型异常
       
       一个空的 except 语句能捕获任何异常
    
    2. raise抛出异常
       
       ```
       try:
       ...     raise ValueError("A value error happened.")
       ... except ValueError:
       ...     print("ValueError in our code.")
       ```
    
    3. finally清理行为
       
       ```
       不管有没有发生异常，finally 子句 在程序离开 try 后都一定会被执行。
       在真实场景的应用程序中，finally 子句用于释放外部资源
       ```

15. **类**
    
    1. 定义简单的类
       
       ```
       class nameoftheclass(parent_class):
           statement1
           statement2
           statement3
       ```
    
    2. `__init__ `方法
       
       ```
       def __init__(self):
           self.data = []
       类定义了 __init__() 方法的话，类的实例化操作会自动为新创建的类实例调用 __init__() 方法。
       ```
    
    3. Python 中的继承
       
       ```
       class Student(Person): Student类继承Person
       ```
    
    4. 多继承
       
       ```
       class MyClass(Parentclass1, Parentclass2,...):
       ```
    
    5. 删除对象
       
       ```
       关键字 del 
       ```
    
    6. 属性读取方法
    
    7. `@property` 装饰器
       
       ```
       @property 装饰器就是负责把一个方法变成属性调用的。
       ```

16. **模块**
    
    1. 模块的导入
       
       1. 可以由全局变量 `__name__` 得到模块的模块名
       2. 从模块中导入指定的函数。`from bars import simplebar, starbar`
    
    2. 包
       
       1. 含有 `__init__.py` 文件的目录可以用来作为一个包
    
    3. 默认/第三方模块介绍
       
       1. os 模块    
          
          ```
          getuid() 函数返回当前进程的有效用户 id。
          getpid() 函数返回当前进程的 id。getppid() 返回父进程的 id。
          uname() 函数返回识别操作系统的不同信息
          getcwd() 函数返回当前工作目录
          ```
       
       2. Requests 模块  http库
          
          ```
          可以使用 get() 方法获取任意一个网页
          ```
       
       3. argparse 命令行参数处理模块
    
    4. 命令行参数

17. **Collections 模块**
    
    1. `Counter` 是一个有助于 *hashable* 对象计数的 dict 子类
       
       ```
       elements() 的方法，其返回的序列中，依照计数重复元素相同次数
       most_common() 方法返回最常见的元素及其计数，顺序为最常见到最少。
       ```
    
    2. `defaultdict` 是内建 `dict` 类的子类，它覆写了一个方法并添加了一个可写的实例变量。
       
       defaultdict() 第一个参数提供了 default_factory 属性的初始值，默认值为 None，default_factory
    
    3. `namedtuple`    命名元组有助于对元组每个位置赋予意义，并且让我们的代码有更好的可读性和自文档性。

18. 
