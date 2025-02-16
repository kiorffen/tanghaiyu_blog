---
title: C语言正则表达式使用及注意点
date: 2017-03-22 16:17:41
tags: C/C++
categories: C/C++
---

# C语言正则表达式使用及注意点

正则表达式作为程序员必备的高效率技能之一，程序开发中不可避免的就会用到，最近在开发中就需要使用C语言的正则表达式来解决一些问题。吐槽一句（gcc版本太低，用不了C++11的特性，也就用不了c++的regex）。

<!--more-->

## API和参数介绍

### 编译正则表达式
```C
int regcomp(regex_t* compiled, const char* pattern, int cflags)
```
- regex_t 是一个结构体数据类型，用来存放编译后的正则表达式，它的成员re_nsub 用来存储正则表达式中的子正则表达式的个数，子正则表达式就是用圆括号包起来的部分表达式。
- pattern 是指向我们写好的正则表达式的指针。
- cflags有以下四种取值。

>REG_EXTENDED 以功能更加强大的扩展正则表达式的方式进行匹配。
REG_ICASE 匹配字母时忽略大小写。
REG_NOSUB 不用存储匹配后的结果。
REG_NEWLINE 识别换行符，这样'$'就可以从行尾开始匹配，'^'就可以从行的开头开始匹配

### 匹配正则表达式
```C
int regexec (regex_t *compiled, char *string, size_t nmatch, regmatch_t matchptr [], int eflags)

regmatch_t //结构体数据类型，在regex.h中定义：             
typedef struct
{
   regoff_t rm_so;
   regoff_t rm_eo;
} regmatch_t;

// 成员rm_so 存放匹配文本串在目标串中的开始位置，rm_eo 存放结束位置。通常我们以数组的形式定义一组这样的结构。因为往往我们的正则表达式中还包含子正则表达式。数组0单元存放主正则表达式位置，后边的单元依次存放子正则表达式位置。
```
- compiled 是已经用regcomp函数编译好的正则表达式。
- string 是目标文本串。
- nmatch 是regmatch_t结构体数组的长度。
- matchptr regmatch_t类型的结构体数组，存放匹配文本串的位置信息。
- eflags 有两个值

>REG_NOTBOL 按我的理解是如果指定了这个值，那么'^'就不会从我们的目标串开始匹配。总之我到现在还不是很明白这个参数的意义；
REG_NOTEOL 和上边那个作用差不多，不过这个指定结束end of line。

### 释放正则表达式
```C
void regfree (regex_t *compiled)
```
当我们使用完编译好的正则表达式后，或者要重新编译其他正则表达式的时候，我们可以用这个函数清空compiled指向的regex_t结构体的内容，请记住，如果是重新编译的话，一定要先清空regex_t结构体。

### 获取错误信息
```C
size_t regerror (int errcode, regex_t *compiled, char *buffer, size_t length)
```
当执行regcomp 或者regexec 产生错误的时候，就可以调用这个函数而返回一个包含错误信息的字符串。
- errcode 是由regcomp 和 regexec 函数返回的错误代号。
- compiled 是已经用regcomp函数编译好的正则表达式，这个值可以为NULL。
- buffer 指向用来存放错误信息的字符串的内存空间。
- length 指明buffer的长度，如果这个错误信息的长度大于这个值，则regerror 函数会自动截断超出的字符串，但他仍然会返回完整的字符串的长度。所以我们可以用如下的方法先得到错误字符串的长度。


## 使用方式
主要从两个方面，一个是获取所有的匹配字串，一个是获取匹配字符串以及相关子正则字串。

### 获取所有匹配字串
这个比较恶心，需要自己移动指针，完成所有字符串的匹配
```cpp
#include <cstdio>
#include <regex.h>
#include <string.h>
#include <stdio.h>

int main(){
    regex_t re;
    regmatch_t subs[1024];
    char matched[1024];
    char src[1024]="beginworldendtestbeginworkendtest";
    char pattern[1024] = "begin(.*?)end";

    int err = regcomp(&re, pattern, REG_EXTENDED);
    if (err) {
        printf("regex error");
        return 1;
    }

    const char *ptr = src;
    // 匹配所有模式字串
    while (strlen(ptr) > 0) {
        memset(subs, 0, sizeof(subs));
        err = regexec(&re, ptr, (size_t)1024, subs, 0);
        if (err == REG_NOMATCH) {
            break;
        } else if (err) {
            char errbuf[1024];
            regerror(err, &re, errbuf, sizeof(errbuf));
            printf("errbuf:%s\n", errbuf);
            break;
        }
        int len = subs[0].rm_eo - subs[0].rm_so;
        memcpy(matched, ptr + subs[0].rm_so, len);
        matched[len] = '\0';
        printf("match:%s\n", matched);
        ptr = ptr + subs[0].rm_so + len;
    }

    regfree(&re);

    return 0;
}
```

### 获取模式字串以及子正则模式串
```cpp
#include <cstdio>
#include <regex.h>
#include <string.h>
#include <stdio.h>

int main(){
    regex_t re;
    regmatch_t subs[1024];
    char matched[1024];
    char src[1024]="beginworldendtestbeginworkendtest";
    char pattern[1024] = "begin(.*?)end";

    int err = regcomp(&re, pattern, REG_EXTENDED);
    if (err) {
        printf("regex error");
        return 1;
    }

    const char *ptr = src;
    // 匹配模式字串以及子正则
    err = regexec(&re, ptr, 1024, subs, 0); 
    for (int x = 0; x < 1024 && subs[x].rm_so != -1; ++x) {
        int len = subs[x].rm_eo - subs[x].rm_so;
        memcpy(matched, ptr + subs[x].rm_so, len);
        matched[len] = '\0';
        printf("matched:%s\n", matched);
    }

    regfree(&re);

    return 0;
}
```

>以上代码为测试demo，省去了很多参数检查

[参考地址1](http://blog.chinaunix.net/uid-479984-id-2114941.html)
[参考地址2](http://blog.csdn.net/ljp1919/article/details/47753559)
