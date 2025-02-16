---
title: 阿里云机器安装Tensorflow和Paddlepaddle
date: 2017-11-03 16:47:11
tags: ML
categories: ML
---


### 阿里云机器安装tensorflow和paddlepaddle
准备用自己1核1G的阿里云机器学习一下深度学习知识，工欲善其事，必先利其器，话不多说，下面开始安装。

#### 安装anaconda2
anaconda2是什么请自行百度，其实我也只知道他是一个python发行版，包含了很多计算工具包。
买的是最低版本的配置，直接wget官网的anaconda，居然只有100k左右的速度，于是我先下载到自己mac上，然后scp到阿里云机器上，mac可以直接scp到阿里云机器，一般人我不告诉他，这个速度可以达到5m左右，也超出了我的认识，怎么会这么快？不会是bug吧。。。
下载好的anaconda直接 bash xxx.sh 就可以完成安装。

<!--more-->

#### 安装tensorflow
tensorflow是google的jeff dean开发的，深度学习平台应该是大哥。

- 创建虚拟环境

```
conda create -n tensorflow python=2.7
```

- 进入环境安装tensorflow

```
source activate tensorflow

pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl

soource deactivate //退出虚拟环境
```

我安装的是cpu版本

- 验证

进入python命令行环境

```
import tensorflow as tf
```

不报错就是ok了。


#### 安装paddlepaddle

ddlepaddle是国内的百度开发，网上说入门比tensorflow要简单一些。paddlepaddle的安装和tensorflow类似，都是使用anaconda创建虚拟环境进行安装。

- 创建虚拟环境

```
conda create -n paddlepaddle python=2.7
```

- 进入虚拟环境安装

```
source activate paddlepaddle

pip install --upgrade paddlepaddle // cpu版本

soource deactivate //退出虚拟环境
```

- 验证

进入python命令行模式执行下面语句，没有出错应该就安装成功了。

```
import paddle.v2 as paddle
```


### 最后

其实我对机器学习和深度学习基本不了解，但是公司内部现在非常流行用AI的思维解决问题，个人感觉还是很有必要学习一下，主要是能多一些解决问题的思路，这个也有可能就是以后的趋势。
