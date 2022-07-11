---
title: FLASK入门
date: 2020-06-10 10:58:43
categories: 学习笔记
tags: 

- Flask

- Python

---

# FLASK入门

1. 装饰器: 函数前使用`@app.*`
   
   `route('/')`设置url 路径,'/'为根目录

2. 变量规则
   
   ```
   @app.route('/user/<username>')
   def show_user_profile(username):
       # 显示用户名
       return 'User {}'.format(username)
   
   @app.route('/post/<int:post_id>')
   def show_post(post_id):
       # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
       return 'Post {}'.format(post_id)
   ```
   
   转换器类型:
   
   | 类型     | 含义                      |
   | ------ | ----------------------- |
   | string | 默认的数据类型，接受没有任何斜杠“/”的字符串 |
   | int    | 接受整型                    |
   | float  | 接受浮点类型                  |
   | path   | 和 string 类似，但是接受斜杠“/”   |
   | uuid   | 只接受 uuid 字符串            |

3. Urls
   
   **重定向**
   
   在代码的 URL 设置时斜线只可多写不可少写；
   
   `@app.route('/about')`
   
   当访问 `http://127.0.0.1:5000/about` 时，页面会显示 `The about page` ；但是当访问 `http://127.0.0.1:5000/about/` 时，页面就会报错 `Not Found` 。
   
   `@app.route('/about/')`都可以访问
   
   用 `redirect()` 函数重定向用户到其它地方。能够用 `abort()` 函数提前中断一个请求并带有一个错误代码。
   
   **URL构建**
   
   去构建一个 URL 来匹配一个特定的函数可以使用 `url_for()` 方法。
   
   `url_for('static', filename='style.css')`这个文件应该存储在文件系统上的 static/style.css 。

4. 渲染模板
   
    `render_template()` 来渲染模板,`render_template('hello.html', name=name)`

5. 请求对象
   
   `from flask import request`
   
   `@app.route('/login', methods=['POST', 'GET'])`装饰器声明方法
   
   `  if request.method == 'POST':`判断方法
   
    `log_the_user_in(request.form['username']) ` request请求表单属性

6. 文件上传
   
   HTML表单中需要设置属性`enctype="multipart/form-data"`
   
   ```python
   from flask import request
   from werkzeug import secure_filename
   
   @app.route('/upload', methods=['GET', 'POST'])
   def upload_file():
       if request.method == 'POST':
           f = request.files['the_file']
           f.save('/var/www/uploads/' + secure_filename(f.filename))
       ...
   ```

7. 
