---
title: Flask-scoketio_API
date: 2020-06-10 10:58:31
categories: 学习笔记
tags:
- 计算机网络
- Python
- Flask
---

## API Reference

1. ***class*** flask_socketio.`SocketIO(*app=None*, ***kwargs*)`
   
   创建一个Flask-ScoketIO服务
   
   参数:
   
   ​        **app** = flask应用程序实例。如果在实例化此类时不知道应用程序实例，则在应用程序实例可用后调用。`socketio.init_app(app)`
   
   ​        **manage_session** = 如果设置为 True，则此扩展将管理Socket.IO事件的用户会话。如果设置为False ，则使用 Flask 自己的会话管理。使用基于 Flask 的 Cookie 会话时，建议您将此集保留为 默认值True 。使用服务器端会话时，设置False 允许在 HTTP 路由和Socket.IO事件之间共享用户会话。
   
   ​        **message_queue** = 服务器可用于多进程通信的消息队列服务的连接 URL。使用单个服务器进程时不需要消息队列。
   
   ​        **channel**= 使用消息队列时通道名称。如果未指定通道，将使用默认通道。如果多个 SocketIO 进程群集需要使用相同的消息队列而不相互干扰，则每个群集应使用不同的通道。
   
   ​        **path**= Socket.IO服务器公开的路径。默认值为`'socket.io'` 。除非你知道你在做什么，否则请保持默认。
   
   ​        **resource** = 同 `path`.
   
   ​        **kwargs** = Socket.IO和Engine.IO服务器选项。

2. 下面详细介绍了Socket.IO服务器选项：
   
   参数:
   
   ​        **client_manager** = 将管理客户端列表的客户端管理器实例。省略此选项后，客户端列表存储在内存结构中，因此无法使用多连接的服务器。在大多数情况下，不需要显式设置此参数。
   
   ​        **logger** = True启用日志记录集或传递记录器对象才能使用。Fasle禁用日志记录集 。默认值为False 。请注意，即使设置为False，也会记录致命错误。
   
   ​        **binary**= 支持二进制有效负载，将所有有效负载视为文本。在 Python 2 上，如果设置为True，则值将被视为文本，并且值将字符串`str`和字节`bytes`视为二进制值。此选项对 Python 3 没有影响.
   
   ​        **json** = 用于编码和解码数据包的替代 json 模块。自定义 json 模块必须具有与标准库版本兼容的 `dumps`和`loads`功能。要使用与 Flask 应用程序相同的 json 编码器和解码器，请使用flask.json 。
   
   ​        **async_handlers** = 如果设置为True ，则客户端的事件处理程序在单独的线程中执行。要同步运行客户端的处理程序，应设置为False 。默认值为 True。
   
   ​        **always_connect** = 设置为False时，新连接是证明的，直到连接处理程序返回其他连接False，此时它们被接受。当设置为True时，将立即接受连接，然后如果连接处理程序返回False断开连接。如果需要从连接处理程序发出事件，并且客户端在连接接受之前接收事件时，设置为True。在任何其他情况下使用默认值Fasle 。

3. Engine.IO服务器配置支持以下设置：
   
   参数: 
   
   ​        **async_mode** = 使用异步模型。有关可用选项的说明，请参阅文档中的"部署"部分。有效的异步模式为`threading`, `eventlet`, `gevent`和`gevent_uwsgi`。如果未给出此参数，则首先尝试`eventlet`，然后`gevent_uwsgi`，`gevent`,最后`threading`。安装了其所有依赖项的第一个异步模式是所选的。
   
   ​        **ping_timeout** = 客户端等待服务器在断开连接前响应的时间（以秒为单位）。默认值为 60 秒。
   
   ​        **ping_interval** = 客户端 ping 服务器的时间间隔（以秒为单位）。默认值为 25 秒。
   
   ​        **max_http_buffer_size** = 使用轮询传输时消息的最大大小。默认值为 100，000，000 字节。
   
   ​        **allow_upgrades** – 是否允许上传。默认值为 `True`
   
   ​        **http_compression** = 使用轮询传输时是否压缩packages。默认值为 `True`
   
   ​        **compression_threshold** = 仅当消息的字节大小大于此值时，才压缩消息。默认值为 1024 字节。
   
   ​        **cookie** = 包含客户端会话 ID 的 HTTP Cookie 的名称。如果设置为 None，则 Cookie 不会发送到客户端。默认值为 `'io'`
   
   ​        **cors_allowed_origins** = 允许连接到此服务器的原点或源列表。默认情况下只允许相同的原点。将此参数设置为`'*'`允许所有源，或`[]`禁用 CORS 处理。
   
   ​        **cors_credentials** = 是否允许凭据（cookie、身份验证）用于此服务器的请求。默认值为 True
   
   ​        **monitor_clients** = 如果设置为True ，后台任务将确保关闭非活动客户端。设置为False禁用监视任务（不推荐）。默认值为 True
   
   ​        **engineio_logger** = 若要启用Engine.IO日志记录，请将其设置为True或传递要使用的记录器对象。要禁用日志记录，请设置为False。默认值为False。请注意，即使engineio_logger为False，也会记录致命错误。

4. **`on`(*message*, *namespace=None*)**
   
   用于注册 SocketIO 事件处理程序的修饰器。
   
   此修饰器必须应用于 SocketIO 事件处理程序。例：
   
   ```python
   @socketio.on('my event', namespace='/chat')
   def handle_my_custom_event(json):
       print('received json: ' + str(json))
   ```
   
   参数: 
   
   ​        **message**–事件的名称。这通常是用户定义的字符串，但已经定义了一些事件名。使用`'message'`定义接受字符串负载的处理程序，`'json'`定义接受json blob负载的处理程序，`'connect'`或`'disconnect'`为连接和断开连接事件创建处理程序。
   
   ​        **namespace**= 要注册处理程序的命名空间。默认值为全局命名空间

5. **`on_error`(*namespace=None*)**
   
   用于为 SocketIO 事件定义自定义错误处理程序。
   
   此修饰器可以应用于充当命名空间的错误处理程序的函数。当 SocketIO 事件处理程序引发异常时，将调用此处理程序。处理程序函数必须接受一个参数，这是引发的异常。例：
   
   ```python
   @socketio.on_error(namespace='/chat')
   def chat_error_handler(e):
       print('An error has occurred: ' + str(e))
   ```
   
   参数: 
   
   ​        **namespace**= 要为其注册错误处理程序的命名空间。默认值为全局命名空间。

6. **`on_error_default`(*exception_handler*)**
   
   用于定义 SocketIO 事件的默认错误处理程序。
   
   此修饰器可以应用于充当没有特定处理程序的任何命名空间的默认错误处理程序的函数。例：
   
   ```python
   @socketio.on_error_default
   def error_handler(e):
       print('An error has occurred: ' + str(e))
   ```

7. **`on_event`(*message*, *handler*, *namespace=None*)**
   
   注册 SocketIO 事件处理程序。
   
   `on_event`不需要修饰器,例:
   
   ```python
   def on_foo_event(json):
       print('received json: ' + str(json))
   
   socketio.on_event('my event', on_foo_event, namespace='/chat')
   ```
   
   参数:
   
   ​        **message**= 事件的名称。这通常是用户定义的字符串，但几个事件名称已定义。`'message'`用于定义采用字符串有效负载的处理程序、`'json'`定义获取 JSON Blob 负载的处理程序， `'connect'`  或`'disconnect'`为连接和断开连接事件创建处理程序。
   
   ​        **handler**= 处理事件的函数。
   
   ​        **namespace**= 要注册处理程序的命名空间。默认值为全局命名空间

8. **`emit`(*event*, args*, *kwargs*)**
   
   发出服务器生成的 SocketIO 事件。
   
   此函数向一个或多个连接的客户端发出 SocketIO 事件。JSON blob 可以作为有效负载附加到事件。此功能可以在 SocketIO 事件上下文之外使用，因此，当服务器是事件的发起者时，在任何客户端上下文之外（如常规 HTTP 请求处理程序或后台任务中）都可以使用。例子：
   
   ```python
   @app.route('/ping')
   def ping():
       socketio.emit('ping event', {'data': 42}, namespace='/chat')
   ```
   
   参数:
   
   ​        **event** = 要发出的用户事件的名称。
   ​        **args**= 包含 JSON 数据作为有效负载发送的字典。
   ​        **namespace**= 要发送消息的命名空间。默认值为全局命名空间。
   ​        **room**= 将消息发送给给定房间中的所有用户。如果未包含此参数，则事件将发送给所有已连接的用户。
   ​        **include_self** - 设置为True在广播或寻址房间时包括发件人，设置为False发送给（除发件人）所有人
   ​        **skip_sid** = 在广播或寻址房间时要忽略的客户端的会话 ID。这通常设置为消息的发起者，以便除客户端外的每个人都收到消息。要跳过多个 sids 传递列表。
   ​        **callback** - 如果给定，将调用此函数以确认客户端已收到消息。将传递给函数的参数是客户端提供的参数。回调函数只能在寻址单个客户端时使用。

9. **`send`(*data*, *json=False*, *namespace=None*, *room=None*, *callback=None*, *include_self=True*, *skip_sid=None*, *\*\*kwargs*)**
   
   发送服务器生成的 SocketIO 消息。
   
   此函数向一个或多个连接的客户端发送一个简单的 SocketIO 消息。消息可以是字符串或 JSON blob。这是比`emit()`更简单的版本，应该首选。此功能可以在 SocketIO 事件上下文之外使用，因此当服务器是事件的发起者时，它才适合使用。
   
   参数:
   
   ​        **data**= 要发送的消息，字符串或 JSON blob。
   
   ​        **json** = 如果`massage`是 JSON blob为True，否则 False
   
   ​        **namespace**= 要发送消息的命名空间。默认值为全局命名空间。
   
   ​        **room**= 仅向给定房间中的用户发送消息。如果未包含此参数，则会将消息发送给所有已连接的用户。
   
   ​        **include_self** - 设置为`True`在广播或寻址房间时包括发件人，设置为`False`发送给（除发件人）所有人
   
   ​        **skip_sid** = 在广播或寻址房间时要忽略的客户端的会话 ID。这通常设置为消息的发起者，以便除客户端外的每个人都收到消息。要跳过多个 sids 传递列表。
   
   ​        **callback** - 如果给定，将调用此函数以确认客户端已收到消息。将传递给函数的参数是客户端提供的参数。回调函数只能在寻址单个客户端时使用。

10. **`close_room`(*room*, *namespace=None*)**
    
    关闭房间。
    
    此功能删除给定聊天室中的任何用户，然后从服务器中删除该文件室。此功能可以在 SocketIO 事件上下文之外使用。
    
    参数：    
    
            **room**= 要关闭的房间的名称。
            **namespace**= 存在房间的命名空间。默认值为全局命名空间。

11. **`run`(*app*, *host=None*, *port=None*, \**kwargs)**
    
    运行 SocketIO Web 服务器。
    
    参数:
    
    ​        **app**= Flask应用程序实例。
    ​        **host**= 要侦听的主机名或 IP 地址。默认值为 127.0.0.1。
    ​        **port**= 服务器要侦听的端口号。默认值为 5000。
    ​        **debug**= `True`在调试模式下启动服务器，`False`在正常模式下启动。
    ​        **use_reloader** – `True`启用 Flask 重装程序，`False`以禁用它。
    ​        **extra_files** = Flask 重新加载程序应监视的其他文件的列表。默认值为None
    ​        **log_output** = 如果`True`，服务器将记录所有连接。如果`False`禁用日志记录。默认为`True`在调试模式下，在正常模式下`False`。使用线程异步模式时不使用。
    ​        **kwargs** = 其他 Web 服务器选项。Web 服务器选项特定于每个受支持异步模式中使用的服务器。请注意，在使用外部 Web 服务器（如 gunicorn）时，不会看到此处提供的选项，因为在这种情况下不会调用此方法。

12. **stop()**
    
    停止正在运行的 SocketIO Web 服务器。
    
    必须从 HTTP 或 SocketIO 处理程序函数调用此方法。

13. **`sleep`(*seconds=0*)**
    
    使用适当的异步模型休眠请求的时间量。
    
    这是一个实用程序函数，应用程序可以使用该函数将任务置于睡眠状态，而不必担心对所选异步模式使用正确的调用。

14. 
