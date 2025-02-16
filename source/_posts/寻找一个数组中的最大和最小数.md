---
title: 寻找一个数组中的最大和最小数
date: 2017-03-18 12:19:47
tags: Algorithm
categories: Algorithm
---

工作一段快两年了，感觉之前学的数据结构和算法基本忘得差不多了，最近一段时间准备复习一下相关知识。

有一个求数组中最大和最小数的题目，基本的思路是遍历一遍数组，然后每个一个元素都和最大值和最小值比较，时间复杂度是2(N-1)或2N。

比较简单的一种减少复杂度的方法是把数组的元素两两分组比较，然后较大的数和max比较，较小的数和min比较，这种实现方法的时间复杂度是1.5N。

还有一种是采用分治法，比较次数也是1.5N，思路是将数组一分为二，分别获取两个子数组的最大和最小值，然后进行取两个子数组中较小的最小值和较大的最大值。

O(N) = (N/2 + N/4 + ... + N/2^(log2(N))) = 3N/2 (收敛?)

<!--more--> 

```cpp

#include <cstdio>
 
void max_min(int a[], int begin, int end, int *max, int *min) {
    if (end == begin) {
        *max = a[begin];
        *min = a[end];

        return;
    }
    int l_max, r_max;
    int l_min, r_min;
    max_min(a, begin, begin + (end - begin) / 2, &l_max, &l_min);
    max_min(a, begin + (end - begin) / 2 + 1, end, &r_max, &r_min);
    *max = l_max > r_max ? l_max : r_max;
    *min = l_min < r_min ? l_min : r_min;
}

int main() {
    int array[] = {5,7,8,9,11,13,45,8,9,23,45,97,3,2,7,14,64};
    int len = sizeof(array) / sizeof(int);
    int max = array[0];
    int min = array[0];
    for (int i = 1; i < len; ++i) {
        if (array[i] > max) {
            max = array[i];
        } else if (array[i] < min){
            min = array[i];
        }
    }
    printf("max:%d min:%d\", max, min);
    int start = -1;
    if (len & 0x1) {
        start = 1;
    } else {
        start = 0;
    }
    for (int i = start; i < len; i+=2) {
        if (array[i] > array[i + 1]) {
            if (array[i] > max) max = array[i];
            if (array[i + 1] < min) min = array[i + 1];
        } else if (array[i] < array[i + 1]) {
            if (array[i] < min) min = array[i];
            if (array[i + 1] > max) max = array[i + 1];
        }
    }
    printf("max:%d min:%d\", max, min);

    max_min(array, 0, len - 1, &max, &min);
    printf("max:%d min:%d\", max, min);

    return 0;
}

```


