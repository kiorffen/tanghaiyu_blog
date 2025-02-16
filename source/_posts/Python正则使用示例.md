---
title: Python正则使用示例
date: 2017-06-30 15:34:01
tags: python
categories: python
---

使用python从一段文本中使用正则匹配自己需要的文本，如果使用search，只会进行一次匹配，group(0)里面的内容是全匹配，group(1)里面的内容是括号里面的子正则。如果需要全部匹配就使用findall，我这里的就是全匹配，返回的是一个列表，每一项内容就是括号里的字正则匹配内容。

<!--more-->

```python
#!/usr/bin/env python

import re
import sys
import json

class RegexImg(object):
    def __init__(self):
        self.pattern = re.compile(r'{\"img_src\":\"(.*?)",\"rcv_url\"')

    def process(self, str):
        return self.pattern.findall(str)

def main():
    dict = sys.argv[1]
    input = sys.argv[2]
    output = sys.argv[3]

    regex_img = RegexImg()
    dt = {}

    with open(dict, 'r') as fd, open(input, 'r') as fin, open(output, 'w') as fout:
        for line in fd:
            parts = line.rstrip().split('\t')
            if len(parts) != 2:
                print "wrong format line:%s" % line
                continue
            dt[parts[0]] = parts[1]
        for line in fin:
            parts = line.rstrip().split('\t')
            if len(parts) != 3:
                print "wrong format line:%s" % line
                continue
            ideaid = parts[0]
            material = parts[2]
            matchs = regex_img.process(material)
            if len(matchs) != 3:
                print "wrong img num:%d" % len(matchs)
                print matchs
                continue
            if ideaid not in dt:
                print "ideaid:%s has not its planid" % (ideaid)
                continue
            tmp_dt = {}
            tmp_dt["planid"] = dt[ideaid]
            tmp_dt["img_src"] = matchs
            json_str = json.dumps(tmp_dt)
            fout.write("%s\n" % json_str)

if __name__ == "__main__":
    main()
```
