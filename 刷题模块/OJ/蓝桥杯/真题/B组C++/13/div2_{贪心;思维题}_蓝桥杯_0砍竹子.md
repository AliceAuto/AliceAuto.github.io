---
layout: post
title: "0砍竹子"
permalink: /刷题模块/OJ/蓝桥杯/真题/B组C++/13/div2_{贪心;思维题}_蓝桥杯_0砍竹子.md/
date: 2025-03-27
author: "JNMC孙国庆"
oj_url: "https://www.lanqiao.cn/problems/2117/learning/"
---

#### [备用返回通道](../../README.md)
#### [转到题目](https://www.lanqiao.cn/problems/2117/learning/)

## 思路
**我们想用最少的次数，那怎么样减少使用魔法是次数呢?**
**答案是对于连续元素越多越好，这样我们就尽可能大的正贡献**
**怎么样保证对足够多的连续元素施法过？**
- 每个竹子只能被砍，不能增长
- 可能让竹子尽可能一块被砍

**因此：对于每一步，我们可以让竹子都先砍到他们的"最高共同高度"**
**应该怎么实现呢？**
**子区间都是连续元素组成的，因此**
**如果我们保证每一个最小的子区间，连续元素之间都要保证"最高共同高度"的性质**
**这样后：**
- 任意子区间
- 更小的子区间 ：两个连续元素

都会遵循这个
**因此我们只要维护每两个连续元素之间的`"最高共同高度"`准则就可以"**

## 代码

```cpp

#include <bits/stdc++.h>
using namespace std;
#define int long long
int res =0;
int n;

signed main(){
  cin>>n;
  unordered_set<long long>pre;
  for(int i =0;i<n;i++){
    int tmp;
    cin>>tmp;
    unordered_set<long long>st;
    while(tmp!=1){
      st.insert(tmp);
      if(!pre.count(tmp))res++;
      tmp = sqrtl(tmp/2+1);
    }
    pre = st;
  }
  cout<<res<<endl;
  return 0;
}
```