---
layout: post
title: "怎么写线性SPJ"
permalink: /刷题模块/OJ/牛客/周赛82/div4_{搜索;构造;贪心}_牛客_怎么写线性SPJ.md/
date: 2025-02-24
author: "JNMC张富涵;JNMC孙国庆"
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
## 思路2

```cpp

//有单数组的定义决定了相邻两个元素一定是不能相同的，
//长度为3，4...的子数组至少要有一个种类数为1
//    而贪心为了让种类数尽可能少应该尽可能对已经出现的数进行贡献
//    我们思考拓展:
//    1->2 任意元素都可以让他符合
//    2->3 显然如果我对称拓展一个 x y x ,那能保证轴是唯一的,种类数也没变多,也是符合的，同理
//    3->5 也是
//    5->9
//    9->19
// 这显然是一个迭代问题
#include<bits/stdc++.h>
using namespace std;
int n;
int main(){
    cin>>n;
    vector<int> vec;

    int cnt =1;
    while(vec.size()<n){
        auto tem  = vec;
        vec.push_back(cnt++);
        for(auto x: tem){
            vec.push_back(x);
        }
    }
    cout<<cnt-1<<endl;
    for(int  i =0 ; i <n ;i ++ ) cout<<vec[i]<<" ";
    
    return 0;
}
```