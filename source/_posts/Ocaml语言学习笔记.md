---

title: Ocaml语言学习笔记
date: 2019-11-07 20:55:10
categories:
tags:

---

# Ocaml语言学习笔记

## unit类型和简单的输入输出

1. unit类型只有一个值();

2. 从标准输入上读取整数: read_int    浮点数,字符串类似 (没有单独读取一个字符的),read_line

3. 打印函数为 print_int ; 浮点数,字符,字符串类似.还有print_newline() 打印新行
   
   print_endline 也可以打印字符串,并换行

4. 合并字符串 操作符 str1 ^ str2

5. 字符串换    int_of_string   /float_of_string