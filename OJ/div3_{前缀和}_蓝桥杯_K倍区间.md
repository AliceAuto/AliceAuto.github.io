---
layout: post
title: "K倍区间"
permalink: v3_{前缀和}_蓝桥杯_K倍区间.md/
date: 2025-01-26
author: "JNMC李衍坤"
---

#### [备用返回通道](../../README.md)
#### 题目描述

给定一个长度为 $ N $ 的数列 $ A_1, A_2, \ldots, A_N $，如果其中一段连续的子序列 $ A_i, A_{i+1}, \ldots, A_j $ 之和是 $ K $ 的倍数，我们就称这个区间 $[i, j]$ 是 $ K $ 倍区间。

你能求出数列中总共有多少个 $ K $ 倍区间吗？

**输入格式**
- 第一行包含两个整数 $ N $ 和 $ K $。
- 以下 $ N $ 行每行包含一个整数 $ A_i $。

**输出格式**
- 输出一个整数，代表 $ K $ 倍区间的数目。

**数据范围**
- $ 1 \leq N, K \leq 100000 $
- $ 1 \leq A_i \leq 100000 $

**输入样例**：

**输入样例**：

```
5 2
1
2
3
4
5
```

**输出样例**：

```
6
```


#### 代码

```C++
#include<bits/stdc++.h>
using namespace std;

const int N = 1e5+10;

int sum[N],a[N],n,k;

long long res;

int main()
{
    cin>>n>>k;
    for(int i = 1; i <= n; i++)
    {
        cin>>a[i];
        a[i] += a[i - 1];
        a[i] %= k;
    }
    // 特判
    sum[0] = 1;
    
    for(int i = 1; i <= n; i ++)
    {
        res += sum[a[i]]++;   
        /*
            像哈希一样
            如果有相同的数 那么就会有一个区间
            依次枚举
        */
    }
    cout<<res<<endl;
    return 0;
}
```