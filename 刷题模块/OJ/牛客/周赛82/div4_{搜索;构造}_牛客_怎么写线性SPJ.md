---
layout: post
title: "怎么写线性SPJ"
permalink: /刷题模块/OJ/牛客/周赛82/div4_{搜索;构造;贪心}_牛客_怎么写线性SPJ.md/
date: 2025-02-24
author: "JNMC张富涵"
---

#### [备用返回通道](../../README.md)
# [转到题目](https://ac.nowcoder.com/acm/contest/102303/F)

## 题目描述

第一次，碰到这么简单的 f 题，补牛客周赛的时候感觉比赛有点水

要求如题目：（接下来是链接）

当 n=3 的时候，可以 `1 2 1`，那么当 `1 2 1` 可以的话，我后面再用是不是也可以，`1 2 1 ... 1 2 1` 显然中间再放一个 `3`，前后就能完美链接，`12 1 3 1 2 1` 同理，`121312141213121` 也可以的，直接这么构造很简单直接，不过不知道为什么输出 `int` 才 60，输出 `char` 才能 AC。

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
string s;
int w;
void bfs(int len, int n, int r)   // 当前长度（可以增加的长度） 需要的长度 当前数字大小
{
    if (len >= n) return;
    string h = s;
    char e = r + '0';
    s = h + e + h;
    r++;
    w = r;
    bfs(len * 2 + 1, n, r);
}

int main() {
    int n;
    cin >> n;
    bfs(0, n, 1);
    cout << w - 1 << endl;
    for (int i = 0; i < n; i++) cout << s[i] - '0' << " ";
    return 0;
}
```