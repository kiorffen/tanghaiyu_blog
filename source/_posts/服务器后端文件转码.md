---
title: 服务器后端文件转码
date: 2017-03-20 20:09:41
tags: 服务器
categories: 服务器
---

## 文件转码

工作中经常遇到的问题之一，就是一个转码问题，这主要的坑爹原因是公司的前端都使用utf8编码，后端一般则是使用gbk编码。对于代码中的编码转化一般是使用公司现成的api，这里就不具体介绍了。下面要说的是在做数据分析时，对文件编码进行转换的解决方法。个人主要使用如下两种方法。

<!--more-->

### 方法1：linux的iconv转码命令
例如对于一个utf8编码的文件想要转化为gbk，通常的做法如下：

```bash
iconv -f UTF-8 -t GBK input_file(原编码文件) -o output_file(目标编码文件)
```

这个命令使用起来非常方便，但是也经常对一些特殊字符转化无能为力，导致文件转码失败。如果我们可以忽略那些特殊字符，只需要整个文件转码完成，则可以使用方法二。

### 方法2：使用一个简单python脚本

代码如下，核心代码就一行。

```python
#! /usr/bin/env python
# -*- coding:gbk -*-

import sys

def main():
    input = sys.argv[1]
    output = sys.argv[2]

    with open(input, 'r') as fin, open(output, 'w') as fout:
        for line in fin:
            line = line.decode('utf8', 'ignore').encode('gbk', 'ignore')
            fout.write(line)

if __name__ == "__main__":
    main()
```

脚本的使用方式很简单。

```bash
python iconv.py input output
```

这两个方法都不复杂，个人一般先使用方法1，如果失败的话再使用方法2。
