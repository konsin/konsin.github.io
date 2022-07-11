---

title: Ubuntu使用deb包安装JDK
date: 2019-09-14 17:42:07
categories: 配置教程
tags:

- Linux

- Ubuntu

- Java

---

# Ubuntu使用deb包安装JDK

## 1.在oracle下载所需版本的jdk的deb包

### 2. 安装jdk包

```
sudo dpkg -i jdk-12.0.2_linux-x64_bin.deb (替换成自己的包的名称)
```

出现依赖问题,使用 `sudo apt install -f`修复

### 3. 环境配置

1. 首先导入安装路径,`/jdk12.0.2/`这里替换成自己的版本的.
   
   ```
   sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk12.0.2/bin/java 1
   sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk12.0.2/bin/javac 1
   ```

2. 环境配置
   
   ```
   sudo update-alternatives --config java
   sudo update-alternatives --config javac
   ```

### 4.验证安装

​        `java -version`
