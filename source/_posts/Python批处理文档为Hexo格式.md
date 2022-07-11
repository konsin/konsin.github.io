---
title: Python批处理文档为Hexo格式
date: 2022-07-11 17:41:35
categories: 配置教程
tags:
- Python
- Hexo 
---

需要将要处理的文件放到同一个文件夹，并在该文件夹下创建python文件。

```python
import os, time

path = r"./"	#采用相对路径读取当前目录md文件

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if not ".md" in name: continue
        print(name)
        _path = os.path.join(root, name)
        #editTime = time.strptime(os.path.getmtime(_path), "%Y-%m-%d %H:%M:%S")
        editTime = time.localtime(os.path.getmtime(_path)) #获取文档最后修改时间
        editTime = time.strftime("%Y-%m-%d %H:%M:%S", editTime) #格式化时间戳
        _name = name[:len(name)-3]
        with open(_path, "r+", encoding="utf-8") as f:
            old = f.read()
            f.seek(0)
            f.write("---\n")
            f.write("title: %s\n" %_name)
            f.write("date: %s\n" %editTime)
            f.write("categories:\n")
            f.write("tags:\n")
            f.write("---\n")
            f.write(old) #将文件原内容追加到前缀后面
```

