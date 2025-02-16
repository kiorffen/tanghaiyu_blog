---
title: 多机同步hexo博客
date: 2017-03-21 10:48:57
tags: 建站相关
categories: 建站相关
---

## 多机同步hexo博客

在阿里云开发机上借助Github-Pages和hexo搭建了个人blog，现在想在Mac和Win7下面继续更新博客的文章，如果每次都登陆开发机也可能会比较麻烦，所以干脆在多台机器上把环境都配置一下。

<!--more-->

### 把源代码上传到github
在github上申请一个仓库，将blog的源代码提交到仓库，这是多机同步第一步。

### 安装必要的依赖
- 需要安装git和nodejs
- 与github建立新机器的ssh信任关系，windows借助git-bash
- clone源代码
- 使用npm安装hexo等依赖，这个不需要每一个依赖都单独安装了，可以在clone源代码之后，进入目录直接执行npm-install。它会根据package.json的依赖关系自动安装所有依赖。

## 注意
以后使用npm安装依赖时，都建议使用本地安装，加上--save参数，这样就会把依赖关系同步到package.json，方便多机同步环境。
