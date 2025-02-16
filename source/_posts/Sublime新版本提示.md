---
title: Sublime新版本提示
date: 2017-04-07 14:36:27
tags: 编辑器
categories: 编辑器
---

使用Sublime已经有一段时间了，从st2到st3用下来感觉非常不错，应该是除了vim之外我最喜欢的编辑器了。

使用了st3一段时间之后，每次打开软件，总是会遇到如下提示，感觉很烦

```
"a new version of sublime text is available, download now?"
```

<!--more-->

去除这个提示的办法如下，在Sublime的Preferences->Settings->User里面添加如下一行即可。

```
{
    ......
    "update_check": false,
    ......
}
```
