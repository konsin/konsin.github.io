---
title: NuXMV学习笔记
date: 2022-11-03 16:07:34
tags:
- NuXMV
categories:
- 学习笔记
---

# 快速入门
## smv文件示例
```js
MODULE main                                 -- 新建一个模型，名为main
VAR                                         -- 变量声明
    bit0 : counter_cell(TRUE);              -- bit0是模型counter_cell的实例
    bit1 : counter_cell(bit0.carry_out);
    bit2 : counter_cell(bit1.carry_out);
SPEC                                        -- CTL说明
    AG AF bit2.carry_out                    -- AG(forall globally),AF(forall finally),检测bit2.carry_out的结果

MODULE counter_cell(carry_in)               -- 新建一个模型，名为counter_cell
VAR                                         -- 变量声明
    value : boolean;                        -- 定义变量value,类型为boolean
ASSIGN                                      -- 指定约束
    init(value) := FALSE;                   -- 初始化value为FALSE
    next(value) := value xor carry_in;      -- value下一状态为value和carry_in的异或值
DEFINE                                      -- 定义声明
    carry_out := value & carry_in;          -- carry_out是value和carry_in的与值
```

## 验证CTL
> nuxmv -int
进入nuxmv交互shell。 
> read_model -i xx.smv
读取smv文件
> go
初始化验证后端
> check_ctlspec
验证文件中的ctl范式


# 详细内容
## 语法
### 基本规则
>- 等宽字体：表示语法类别（非终结符）、
>- **粗体字符** 令牌和字符集成员（终结符）
>- `[]`表示可选的语法结果
>- `|`用于分割语法规则中的备选项
>如果是加粗的符号`[]`和`|`就是正常字符。
>标识符以字母开头且标识符中只能包含 {A-Za-z0-9 $#-}中的字符
>任何以两个破折号(`——`)开头并以换行符结尾的字符串都是注释，解析器会忽略它。多行注释以`/——`开始，以`——/`结束。

### NuXMV保留关键字
>@F~, @O~, A, ABF, ABG, abs, AF, AG, array, ASSIGN, at next, at last, AX, bool, boolean, BU, case, Clock, clock, COMPASSION, COMPID, COMPUTE, COMPWFF, CONSTANTS, CONSTARRAY,CONSTRAINT, cos, count, CTLSPEC, CTLWFF, DEFINE, E, EBF, EBG, EF, EG, esac, EX, exp, extend, F, FAIRNESS, FALSE, floor, FROZENVAR, FUN, G, H, IN, in, INIT, init, Integer, integer, INVAR, INVARSPEC, ISA, ITYPE, IVAR, JUSTICE, ln, LTLSPEC, LTLWFF, MAX, max, MDEFINE, MIN, min, MIRROR, mod, MODULE, NAME, next, NEXTWFF, noncontinuous, O, of, PRED, PREDICATES, pi, pow, PSLSPEC, PARSYNTH, READ, Real, real, resize, S, SAT, self, signed, SIMPWFF, sin, sizeof, SPEC, swconst, T, tan, time, time since, time until, toint, TRANS, TRUE, typeof, U, union, unsigned, URGENT, uwconst, V, VALID, VAR, Word, word, word1, WRITE, X, xnor, xor, X~ Y, Y~, Z

### 类型
1. Boolean
   布尔类型由符号值FALSE和TRUE组成。
2. 枚举类型 Enumeration Types
   enum类型。
   我们实际上只处理两种枚举类型:符号枚举和整数符号枚举。这些类型是可区分的，并且允许对它们进行不同的操作。
   纯整数枚举没有必要，布尔类型枚举不被允许。
3. 字类型 Word
   unsigned word 无符号单词[•]和 signed word 有符号单词[•]类型用于建模位向量(布尔值)，允许按位进行逻辑和算术操作(分别为无符号和有符号)。这些类型可以通过宽度来区分。例如，类型无符号单词[3]表示3位的向量，允许无符号操作，类型有符号单词[7]表示7位的向量，允许有符号操作。
   当无符号字[N]的值被解释为整数时，所使用的位表示是最受欢迎的，即每个位表示0(位号0)到$2^N−1$(位号N−1)之间的连续2次幂。因此无符号字[N]能够表示0到$2^N−1$的值。
   有符号词[N]类型的位表示是"二进制补码"，即它与无符号词[N]相同，只是最高位(数字N−1)的值为$−2^{N−1}$。因此，符号词[N]可能的值从$−2^{N−1}$到$2^N−1$。
4. 整型 Integer
   首先，在某些模型检查引擎和算法中不允许使用整数。其次，目前，整型枚举类型有实现相关的约束，因为整型数只能在$−2^{32}  +1$到$2^{32}−1$的范围内(更准确地说，这些值等价于C/ c++宏INT MIN +1和INT MAX)。
5. 实数 Real
    类似于float型
6. 时钟类型Clock
   时钟类型仅在TTS(2.4)中支持。该类型的域取决于模块的时间域:
   - continuous时间域:时钟类型域等价于实类型域;
   - none 时间域:不能表示时钟类型。
7. 数组类型 Array
   数组声明时使用索引的下限和上限，以及数组中元素的类型。例如
   `array 0..3 of boolean`
   `array 1..8 of array -1..2 of unsigned word[5]`
   数组类型与set类型不兼容，即数组元素不能为set类型。
8. 字类型数组 WordArray
   字数组类型用于为数组建模，数组的大小是有限制的，并使用无符号单词[•]类型指定。数组的元素可以是某种类型的。例如,
   `array word[5] of unsigned word[3];`
9. 整型数组 IntArray
   `array integer of integer;`
10. 集合类型 Set
    集合类型用于标识表示一组值的表达式。集合有四种类型:boolean set,integer set, symbolic set, integers-and-symbolic set.。set类型的使用方式非常有限。特别是，变量不能为set类型。只有范围常量和联合运算符可以用来创建set类型的表达式，并且只有在、case、(•?•:•)，而assignment1表达式可以具有set类型的立即操作数。
11. 类型顺序
    integer小于integer -symbolic enum且小于real;符号枚举小于整数和符号枚举，等等。无符号词[•]和有符号词[•]类型不能与任何其他类型比较，也不能相互比较。任何类型都等于它本身。
    注意，只包含整数的枚举类型为integer。
12. 表达式
    1. 隐式类型转换
        在某些表达式中，操作数可以从一种类型转换为与其对应的set类型
        在NUXMV中也不再支持隐式整数<->布尔类型转换，必须使用显式强制转换操作符。
    2. 常数表达式
       常量可以是布尔值、整数、实数、符号、字或范围常量。
    3. 基本表达式
       ```cpp
       basic_expr ::
          constant -- a constant
          | variable_identifier -- a variable identifier
          | define_identifier -- a define identifier
          | function_call -- a call to a function
          | ( basic_expr )
          | pi -- the pi constant
          | abs ( basic expr ) -- absolute value
          | max ( basic expr , basic expr ) -- max
          | min ( basic expr , basic expr ) -- min
          | sin ( basic expr ) -- sin
          | cos ( basic expr ) -- cos
          | exp ( basic expr ) -- exp
          | tan ( basic expr ) -- tan
          | ln ( basic expr ) -- ln
          | ! basic_expr -- logical or bitwise NOT
          | basic_expr & basic_expr -- logical or bitwise AND
          | basic_expr | basic_expr -- logical or bitwise OR
          | basic_expr xor basic_expr -- logical or bitwise exclusive OR
          | basic_expr xnor basic_expr -- logical or bitwise NOT exclusive OR
          | basic_expr -> basic_expr -- logical or bitwise implication
          | basic_expr <-> basic_expr -- logical or bitwise equivalence
          | basic_expr = basic_expr -- equality
          | basic_expr != basic_expr -- inequality
          | basic_expr < basic_expr -- less than
          | basic_expr > basic_expr -- greater than
          | basic_expr <= basic_expr -- less than or equal
          | basic_expr >= basic_expr -- greater than or equal
          | - basic_expr -- integer or real or word unary minus
          | basic_expr + basic_expr -- integer or real or word addition
          | basic_expr - basic_expr -- integer or real or word subtraction
          | basic_expr * basic_expr -- integer or real or word multiplication
          | basic_expr / basic_expr -- integer or real or word division
          | basic_expr mod basic_expr -- integer or word remainder
          | basic_expr >> basic_expr -- bit shift right
          | basic_expr << basic_expr -- bit shift left
          | basic_expr [ index ] -- index subscript
          | basic_expr [ basic_expr : basic_expr ]
          -- word bits selection
          | basic_expr :: basic_expr -- word concatenation
          | word1 ( basic_expr ) -- boolean to unsigned word[1] conversion
          | bool ( basic_expr ) -- unsigned word[1] and int to boolean conversion
          | toint ( basic_expr ) -- word and boolean to integer constant conversion
          | count ( basic_expr_list ) -- count of true boolean expressions
          | swconst ( basic_expr , basic_expr )
          -- integer to signed word constant conversion
          | uwconst ( basic_expr, basic_expr )
          -- integer to unsigned word constant conversion
          | signed ( basic_expr ) -- unsigned word to signed word conversion
          | unsigned ( basic_expr ) -- signed word to unsigned word conversion
          | sizeof ( basic_expr ) -- word size as an integer
          | floor ( basic_expr ) -- from a real to an integer
          | extend ( basic_expr , basic_expr)
          -- word width extension
          | resize ( basic_expr , basic_expr)
          -- word width resize
          | signed word[N] ( basic_expr ) -- integer to signed word conversion
          | unsigned word[N] ( basic_expr ) -- integer to unsigned word conversion
          | basic_expr union basic_expr -- union of set expressions
          | { set_body_expr } -- set expression
          | basic_expr in basic_expr -- inclusion in a set expression
          | basic_expr ? basic_expr : basic_expr
          -- if-then-else expression
          | READ ( basic_expr , basic_expr ) -- read function with first argument
          -- an array and second index
          | WRITE ( basic_expr, basic_expr, basic_expr ) -- write function with first
          -- argument an array, second index, and third value to be stored
          | CONSTARRAY ( typeof ( variable_identifer ), basic_expr ) -- constant array
          -- constructor function that takes the type of the array variable indentifier
          | CONSTARRAY ( array word[n] of subtype, basic_expr ) -- constant array
          -- constructor function for word-array that takes the array type explicitly
          | CONSTARRAY ( array integer of subtype, basic_expr ) -- constant array
          -- constructor function for int-array that takes the array type explicitly
          | case_expr -- case expression
          | basic_next_expr -- next expression
          basic_expr_list ::
             basic_expr
             | basic_expr_list , basic_expr
       ```
    4. 操作符及顺序
       ```
       [ ]  下标索引, [ : ] 位选择运算[high : low]
       ! 非运算
       ::  连接操作符
       - (unary minus)
       * / mod
       + -
       << >>
       union
       in
       = != < > <= >=   
       &
       | xor xnor
       (• ? • : •)
       <->
       ->
       ```
    5. 变量和定义
       ```
       define_identifier :: complex_identifier
       variable_identifier :: complex_identifier
       ```
    6. 函数调用
        ```cpp
        function call :: function identifier ( fun args list )
        function identifier :: complex identifier
        fun args list :: next expr | fun args list next expr
        ```
    7. 其他操作
       - 连接字（:）
         w1 := 0ub4 1101 and w2 := 0sb2 00, the result of w1::w2 is 0ub6 110100.
       - 字扩展（extend） 
         扩展操作符通过在左侧附加额外的位来增加单词的宽度。可以理解为扩展后右移，填充字节规则同C
       - 调整字大小（resize）
         
       - set表达式
         在NUXMV中不能有集合的集合。集合只能包含单例值，而不能包含其他集合。
       - 包含运算符 in ： 判断左操作数是否是右操作数的子集。
       - read表达式
         读取操作符' read '提取数组中特定下标处的一个元素。操作符的第一个实参必须是word-array或int-array类型的表达式，第二个实参表达式的类型必须与第一个实参中的数组表达式的索引类型相同。
       - write表达式
         写操作符' write '更新数组特定下标处的一个元素，并将更新后的数组作为新数组返回。操作符的第一个参数必须是word-array或int-array类型的表达式。
         第二个和第三个参数表达式的类型必须与第一个参数中的数组表达式的索引类型和元素类型相同
       - CONSTARRAY表达式
         常量数组' CONSTARRAY '是一个特殊的构造函数，用于创建给定类型的数组，其中的元素设置为统一的给定值。
         `CONSTARRAY(typeof(a), 0)`
       - typeof表达式。它主要用于获取数组变量的类型。
       - case表达式
         ```
         case
           left_expression_1 : right_expression_1 ;
           left_expression_2 : right_expression_2 ;
           ...
           left_expression_N : right_expression_N ;
         esac
         ```
       - `if then else` 表达式 或`(• ? • : •)`即 
         cond_expr ? basic_expr1 : basic_expr2
       - next表达式
         Next表达式指的是处于下一个状态的变量的值。例如，如果一个变量v是一个状态变量，那么next(v)指的是下一个时间步中的变量v。应用于复杂表达式的next是递归应用于表达式中所有变量的next的一种速记方法。例如:next((1 + a) + b)等价于(1 + next(a)) + next(b)。
         注意，next操作符不能应用两次，即不允许next(next(a))。
       - count表达式 count运算符计算为真表达式的个数。
    8. 类型转换操作符
       - 整数转换操作符（toint）
       - floor转换操作符 将一个实数映射到之前最大的整数。
       - bool转换操作符
         将无符号单词和任何整数类型的表达式(例如1 + 2)转换为布尔值。
       - 整型到字常量的转换
         swconst、uwconst分别将整数常量转换为给定大小的有符号单词[•]常量或无符号单词[•]常量。
       - Word1显式转换 bool转换为unsigned word[1]
       - 无符号和有符号字显式转换
       - 一般整数到字的转换
         ```
         unsigned word[N](x) = −(unsigned word[N](−x))
         signed word[N](x) = signed(unsigned word[N](x))
         ```
### 变量声明 p27

