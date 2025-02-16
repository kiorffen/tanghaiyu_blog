---
title: Python发送http请求解析返回json小demo
date: 2017-03-18 11:48:33
tags:
---

python发起http请求，并解析返回的json字符串的小demo，方便以后用到。

<!--more-->

```python
#! /usr/bin/env python
# -*- coding:gbk -*-
    
import os
import sys
import json
import urllib
import urllib2

if __name__ == "__main__":
    query_file = sys.argv[1]
    query_index = 0
    with open(query_file, 'r') as fp:
        for line in fp:
            query = line.rstrip()
            query_index = query_index + 1
            query_gbk = query
            query = query.decode('gbk', 'ignore').encode('utf8', 'ignore')
            url = 'http://10.42.141.12:8089/adrender?query=%s&ad_num=3&srcid=101'\\
                  '&ip=172.22.182.55&baiduid=61ABB404320C72436EB6B8352DFBB388:FG=1' % (query)
            req = urllib2.urlopen(url)
            page = req.read()
            ddict = json.loads(page)
            expid = ddict['expid']
            sid = ddict['sid']
            ad_num = ddict['response_adnum']
            for i in range(0, ad_num):
                output_html = '%s-%d.html' % (query_gbk, i)
                output = open(output_html, 'w')
                ad = ddict['response_ads'][i].encode('utf8', 'ignore')
                output.write('<html>\')
                output.write('<head>\    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\<head>\')
                output.write("%s" % (ad))
                output.write('\</html>\')
                output.close()
```
