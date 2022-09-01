---
title: 为code-server配置https解决Markdown无法预览的问题
date: 2022-08-27 14:00:51
tags:
- Ubuntu
- Linux
- code-server
- Nginx
categories:
- 配置教程
---
1. 首先为IDE安装`Markdown All in One`插件启用Markdown编辑预览支持。
   但是此时右键选择预览时发现预览栏空白，没有渲染。查看浏览器控制台发现浏览器拒绝了预览显示的请求。
   为网站配置SSL证书可以解决这个问题。
2. 申请SSL证书，如果没有为服务器绑定域名可以通过[ZeroSSL](https://zerossl.com/)为服务器IP申请SSL证书，证书有效期3个月。当然该网站也支持为域名下发证书。申请证书流程不做赘述。
3. 为Nginx配置HTTPS。
   - 首先需要将证书文件上传至服务器，包括两个`.crt`文件和一个`.key`文件。
   - 接着配置证书。进入nginx安装目录，执行`sudo vim conf/nginx.conf`编辑配置文件
     https最基本配置内容如下,`# #`内要修改为自己的实际环境
     ```shell
        server {
    	    listen               443 ssl;
            
    	    ssl                  on;
    	    ssl_certificate      # certificate.crt路径 #; 
    	    ssl_certificate_key  # private.key 路径 #;

    	    server_name  # 你的ip地址或者域名 #;

    	    location / {
                root   html;
                index  index.html index.htm;
            }
        }
     ```
     配置完成后重启nginx，之后就可以在浏览器通过https访问了。
4. 配置code-server通过https访问。
   由于https默认不允许`ip:port`的方式访问网站，所以需要通过Nginx进行反代设置。
   - 继续修改上文的nginx配置文件，主要是将`location /`中内容替换
     ```shell
        server {
        	listen               443 ssl;
            
    	    ssl                  on;
    	    ssl_certificate      # certificate.crt路径 #; 
    	    ssl_certificate_key  # private.key 路径 #;

    	    server_name  # 你的ip地址或者域名 #;

        	location / {
                proxy_pass http://localhost:8080;
                proxy_set_header Host $host;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection upgrade;
                proxy_set_header Accept-Encoding gzip;
            }
        }
     ```
   - 修改code-server的配置文件
     `sudo vim /home/ubuntu/.config/code-server/config.yaml`
     将最后一行修改为如下内容，`# #`中的内容要替换
     ``` yaml
     cert: # certificate.crt路径 #
     cert-key: # private.key 路径 #
     ```
此时重启服务就可以通过访问`https://ip:8080`在https下打开IDE了。


