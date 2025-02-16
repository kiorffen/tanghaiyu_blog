---
title: Python模版引擎Jinja2
date: 2017-03-24 21:14:17
tags: python
categories: python
---

## 导语 
最近在调研开发一个BS服务框架，需要能够根据protobuf文件以及配置文件能够自动生成相关的代码，代码注册之后可以直接编译得到一个直接支持一种数据流的BS服务模块。即实现一个可以根据数据格式定制化的BS服务框架。因为要自动生成的代码有很多，如果使用python直接把这些代码打印出来，那工作将完全无法开展，并且生成代码的格式不好控制。

根据之前模板渲染的开发经验，完全可以像开发html模板一样，使用相同的方式开发一个C/C++代码模板，最后使用模板引擎进行渲染出来完整的代码。因为计划使用python进行模板渲染，所以就调研了python的模板引擎，比较之后发现jinja2的使用文档较全面而且也比较轻量级，所以就使用它进行代码的模板渲染。
 
 
<!--more-->

## Jinja2的介绍和使用
主要参考Jinja2的[中文使用文档](http://docs.jinkan.org/docs/jinja2/)。
安装
```
pip install jinja2
```

模板，我主要使用的一个是变量替换，一个是for循环（这个自己定义占位符完全搞不定）。
```
#include <iostream>

int main() {
{%for item in items%}
    {{item.type}} {{item.name}};
{%endfor%}
    return 0;
}
```

python使用代码，我用的最简单的使用方式
```python
#!/usr/bin/env python
# -*- coding:gbk -*-

import sys
from jinja2 import Template

class Item(object):
    pass

def main():
    input = sys.argv[1]
    with open(input, 'r') as fin:
        template = Template(fin.read())
        items = []
        item1 = Item()
        item1.name="name1"
        item1.type="int"
        items.append(item1)
        item2 = Item()
        item2.name="name2"
        item2.type="float"
        items.append(item2)
        content = template.render(items=items)
        print content

if __name__ == "__main__":
    main()
```

替换之后的效果，就是一个可以编译的C++的代码。
```cpp
#include <iostream>

int main() {

    int name1;

    float name2;

    return 0;
}
```
