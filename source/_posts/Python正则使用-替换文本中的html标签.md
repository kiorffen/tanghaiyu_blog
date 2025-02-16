---
title: Python正则使用-替换文本中的html标签
date: 2017-03-20 21:00:11
tags: python
categories: python
---


最近因为需要把字符串中的html标签替换掉，想到的是使用正则来做，因为原来模块是用C++码的，所以就用的glibc的regex来做的。后来查资料发现用python来做这件事，简单方便，而且一次性可以完成所有替换，不想用C还需要自己写程序移动指针完成替换。不多说了上代码，很简单。

<!--more-->   

```python
#! /usr/bin/env python
# -*- coding:gbk -*-

"""
Notes:
    A python script that use regex to replace all the label of a html file
"""

import os
import sys
import re

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r') as fp:
        for line in fp:
            line = line.rstrip()
            pattern = re.compile(r'<([^>]*)>')
            match_list = pattern.findall(line)
            for i in range(0, len(match_list)):
                print "matched:%s" %match_list[i]
            line = pattern.sub('', line)
                print line
```

输入文件 

```
 helle<p>world</p><br/>
```

输出结果

```
matched:p
matched:/p
matched:br/
helleworld
```

这里说一下，Python的re模块的findall函数返回的是正则模式里面组所匹配的内容，可以方便进一步使用。

