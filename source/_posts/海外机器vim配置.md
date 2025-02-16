---
title: 海外机器vim配置，支持C++和golang的代码补全和跳转
date: 2018-10-20 19:34:11
tags: vim
categories: vim
---

想要配置一套支持golang和c++代码提示和自动补全的vim环境，一直以来都有一点问题，不是youcompleteme安装有问题，就是vim-go安装的不够完整。最近买了一台国外的vps，安装这些工具遇到的问题相对就比较好解决。注意：系统环境使用centos7以上。
简单列一下需要安装的工具：
- vim8.0以上，需要完美支持vim-go
- vundle，管理vim插件
- youcompleteme，这个不需要多说，自动补全的神器
- vim-go，支持vim写golang的代码提示，语法高亮，代码跳转等

下面开始安装过程：

1.vim8.0安装
删除系统自带的vim
```
yum remove -y vim-enhanced
```

安装必须lib
```
sudo yum install python-devel
sudo yum install ncurses-devel -y
```

<!--more-->

安装vim
```
wget https://github.com/vim/vim/archive/master.zip
unzip master.zip
cd vim-master
cd src/
./configure --with-features=huge --enable-pythoninterp=yes --with-python-config-dir=/usr/lib/python2.7/config
sudo make
sudo make install
```


2.安装vundle插件
```
mkdir -p ~/.vim/bundle 
cd bundle
git clone https://github.com/gmarik/vundle.git
```

编辑~/.vimrc,内容如下：
```
set expandtab
set ts=4
set sw=4
set sts=4
set tw=100
set cindent
set autoindent
set nu

set noai nosi

set nocompatible               " be iMproved
set backspace=indent,eol,start
syntax on

filetype off                   " required!
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
" let Vundle manage Vundle
" required!
Bundle 'gmarik/vundle'
" My Bundles here:
Bundle 'fatih/vim-go'
Bundle 'Valloric/YouCompleteMe'

filetype plugin indent on     " required!
"
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install(update) bundles
" :BundleSearch(!) foo - search(or refresh cache first) for foo
" :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle command are not allowed..

let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
set tags+=./tags,/usr/include/tags
```

执行BundleInstall,安装vim-go和youcomleteme

3.安装youcompleteme，先支持C/C++代码补全
上一步是先将youcomplete下载到本地，需要编译一下才能YcmServer，编译过程如下：
```
cd ./vim/bundle/YouCompleteMe
./install.py --clang-complete
```
到这youcompleteme基本安装完成，可以支持基本文本提示功能，如果需要支持C/C++的补全，需要进行如下操作
```
cd /home/work/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm
cp /home/work/.vim/bundle/YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py .
```

编辑ycm_extra_conf.py，在flag下面加入下面配置：
```
'/usr/include/c++/4.8.2/',
'/usr/include/c++/4.8.5/',
'/usr/include',
```

vimrc加入如下配置
```
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
set tags+=./tags,/usr/include/tags
```
生成tags使用ctags，一般除了在自己工程根目录下生成一个tags文件，还可以在/usr/include/目录下也生成一下，并加入tags路径，生成tags的命令如下。
```
ctags --c-kinds=+px --c++-kinds=+px --fields=+iafksS --extra=+qf -R .
```

4.支持golang代码补全
vim-go安装好之后，执行GoInstallBinaries，会自动安装go-def，gofmt，gocode等工具，这些工具支持go代码跳转，代码格式化，代码高亮等功能，详细可以参考github上的介绍。

到这一步，基本安装好了一个完整的支持c/c++，golang代码补全，代码跳转等功能的vim环境。在此过程中可能还需要安装一些必要的工作包，比如git，ctags，gcc, gcc-c++, cmake,ctags等工具，我这边都是使用系统工具yum自动安装，centos7.0以上支持这些软件版本基本都能满足需求。
