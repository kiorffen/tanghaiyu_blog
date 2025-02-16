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
