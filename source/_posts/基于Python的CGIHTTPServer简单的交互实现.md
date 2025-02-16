---
title: 基于Python的CGIHTTPServer简单的交互实现
date: 2017-07-04 13:06:41
tags: python
categories: python
---

# 基于Python的CGIHTTPServer简单的交互实现

## 介绍
对于服务器后端开发者而言，有时候需要把自己的一些服务直接暴露给PM或者其他RD使用，这个时候需要搭建一套web服务可以和前端用户做简单交互，按照最常规的做法，一般是用Apache或者Nginx作为webserver后端使用cgi或者fcgi程序或者脚本进行处理，当然这种做法安全且正规。

但是我个人更喜欢一个更简单的做法：就是利用python自带的CGIHTTPServer作为服务器，然后通过一个简单的html页面进行交互，通过post请求直接调用总控脚本，与用户进行交互。

![http://cdn.tanghaiyu.com/python-cgi.jpg](http://cdn.tanghaiyu.com/python-cgi.jpg)

<!--more-->

## 使用方法和示例

### 启动服务
Python的CGIHTTPServer一般是与python一起安装的，使用如下命令既可以启动，为了便于组织目录，建议先建立一个目录，比如web，然后再运行下面的命令。
```shell
nohup python -m CGIHTTPServer 8088 &
```
上面的命令使CGIHTTPServer在非中断后台运行，运行log可以通过当前目录下的nohup.out查看。

### 编写交互页面
在启动server的当前目录下，建立一个index.html文件，编写内容如下。

```html
<!DOCTYPE html>
<html>
   <head>
       <meta http-equiv="Content-Type" content="text/html; charset=gbk">
       <title> Python-CGIHTTPServer使用示例 </title>
       <meta name="author" content="Haiyu">
       <center><h1> Python-CGIHTTPServer使用示例 </h1></center>
   </head>
   <hr style="height:5px;border:none;border-top:5px ridge green;" />
   <body>
       <br/>
       <center><h2>计算圆的周长</h2></center>
       <center>
       <p>请输入圆的半径长度.</p>
       <br/>
       <form action="cgi-bin/c_length.sh" method="post" enctype="text/plain" target="_blank">
           radius:<input type="text" id="radius" name="radius" value=""/>
           <input type="submit" id="c_length" name="c_length" value="计算周长">
       </form>
       </center>
       <br/>
       <br/>
       <br/>
   </body>
   <hr style="height:5px;border:none;border-top:5px ridge green;" />
   <br/>
   <br/>
</html>
```

这个界面的功能非常简单，使用一个form表单接收用户的提交的半径参数，然后计算完周长之后进行返回，使用post请求。

### CGI脚本
这个才是我们后端开发同学最关心的内容，这个脚本就是用来完成主要的逻辑操作进行返回，因为我们后端同学关注更多的不是交互界面的华丽而是逻辑处理的正确性和严谨性，根据我的经验，后端不管多么复杂的处理流程，最终都可以用一个脚本包起来，根据输入得到输出，这里面的输入就是我们用户提交的参数，输出就是我们经过层层处理之后需要返回的内容。
这个脚本建议放在server运行目录下新建立的cgi-bin目录中。

```bash
#!/bin/bash

mysql_bin=/home/work/mysql/bin/mysql

echo "Content-Type:text/html; Charset=gbk"
echo ""

echo "<br/>"
radius=0
c_length=0
if [[ "$REQUEST_METHOD" == "POST" ]];then
    read vars
    echo "$vars" | awk -F "=" '{print $2}' > temp
    dos2unix temp
    radius=`cat temp`
    c_length=$(echo "scale=2;2*3.14*$radius" | bc)

    echo "<br/>"
    echo "<table border="5" cellpadding="10">"
    echo "Userid Info:"
    echo "<tr>"
    echo "<td>半径</td><td>周长</td>"
    echo "</tr>"
    echo "<tr>"
    echo "<td>"$radius"</td><td>"$c_length"</td>"
    echo "</tr>"
    echo "</table>"
fi
```

## 总结
以上就是使用Python的CGIHTTPServer进行用户交互的主要内容，其优点就是开发使用方便，让后端同学能更加专注于业务逻辑处理相关的内容。不足之处可能就是不够正规，使用有风险，因为使用的是纯CGI协议交互，记得之前排查过一个bash的cgi漏洞，使用起来可能会有风险，因此这种方式更适合开发一套对内使用的简易工具，不建议对外部用户暴露。
