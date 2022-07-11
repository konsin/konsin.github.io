---
title: kodexplorer不修改版权改标签
date: 2019-07-10 11:02:09
categories: 配置教程
tags:

- KodExplorer

---

# kodexplorer不修改版权改标签

1. 自定义可道云名称和描述:
   
   这个很简单,在admin账号下,右上角下拉菜单选择系统设置就可以修改了

2. 隐藏 页面底部版权信息 
   
   admin账号->系统设置->其他->自定义css
   
   ```css
   .copyright-content{display:none}
   ```
   
   然后可以自定义在页面底部显示自己的信息,方法是` admin账号->系统设置->其他->自定义html
   
   ```
   <script>
   var html = document.getElementsByClassName("common-footer")[0].innerHTML;
   document.getElementsByClassName("common-footer")[0].innerHTML = html + "Copyright@ 1611253728@qq.com";
   </script>
   ```

3. 隐藏设置界面和下拉菜单中的`免费版`字样
   
   这里我通过添加自定义css没有效果所以是直接修改的css文件.请做好备份
   
   1. 右键选择`免费版`,在右键菜单中选择`检查`;
   
   2. 复制标签名(我的是` version-vip` ),鼠标移到下图位置会显示改页面的css位置.
   
   3. 找到这个文件进行编辑.
   
   4. ctrl+f 输入刚才复制的标签名进行搜索.
   
   5. 在属性中添加`visibility: hidden;`,并将`height`值改为0.
      
      ```css
      .version-vip{visibility: hidden;height:0px;
      ```
   
   6. 保存后就可以看到效果了