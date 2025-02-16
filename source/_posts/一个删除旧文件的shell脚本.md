---
title: 一个删除旧文件的shell脚本（非常好用）
date: 2018-12-07 11:19:29
tags: shell
categories: linux
---

 一个删除旧文件的shell脚本（非常好用）

对于后端开发同学来说，一些服务会不可避免的产生一些输出文件，这些文件随着时间积累会越来越多，我们常常需要按照某个时间定期的清理掉之前的文件，比如5天之前的旧文件。这里的脚本就是为了解决这个问题，非常好用。

<!-- more -->

```bash
#!/bin/bash

days=5 #配置时间

dt=$(date -d "- $days day" "+%Y%m%d%H%M%S")

if [[ ! -d old-file ]]; then
    mkdir old-file
fi

ls > temp.${dt}
while read line; do
    file=$line
    if [[ "$file"x == "old-file"x || "$file"x == "old_file.sh"x ]]; then
        continue
    fi
    ftime=$(stat "$file"|grep -i Modify | awk -F. '{print $1}' | awk '{print $2$3}'| awk -F- '{print $1$2$3}' | awk -F: '{print $1$2$3}')
    
    if [[ "$ftime" < "$dt" ]]; then
        echo "file:"$file" time:$ftime has moved to old-file"
        mv "$file" old-file/
    fi
done < temp.${dt}

rm temp.${dt}

```

**注意**
上面的脚本会把要删除的文件，移动到一个old-file的文件夹，不会真正的删除，如果需要彻底删除的话，请在脚本执行完之后执行rm -rf old-file即可。
