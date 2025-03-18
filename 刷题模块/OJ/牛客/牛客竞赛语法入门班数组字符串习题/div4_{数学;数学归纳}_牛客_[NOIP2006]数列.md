---
layout: post
title: "[NOIP2006]数列"
permalink: /刷题模块/OJ/牛客/牛客竞赛语法入门班数组字符串习题/div4_{数学;数学归纳}_牛客_[NOIP2006]数列.md/
date: 2025-03-18
author: "JNMC孙国庆"
oj_url: "https://ac.nowcoder.com/acm/contest/19305/1019"
---

#### [备用返回通道](../../README.md)
#### [转到题目](https://ac.nowcoder.com/acm/contest/19305/1019)
**核心切入点**  
所有序列中的数都可以表示成  
\[
a_0 k^0 + a_1 k^1 + a_2 k^2 + \dots
\]  
其中每个 \(a_i\) 只能取 0 或 1。这与二进制数的表示完全对应，只不过这里的“权值”从 \(2^i\)变成了 \(k^i\)。

**推导过程**  
1. **二进制对应**  
   - 设二进制数 \(b_nb_{n-1}\dots b_0\) 表示一个数，则其在二进制下的值为  
     \[
     \sum_{i=0}^{n} b_i \times 2^i.
     \]
   - 而题中要求的序列，其每个数正好对应  
     \[
     \sum_{i=0}^{n} b_i \times k^i.
     \]

2. **第 \(N\) 项求法**  
   - 将 \(N\) 写成二进制字符串，得到每一位 \(b_i\)。
   - 将该二进制串视作 \(k\) 进制数，计算  
     \[
     \text{ans} = \sum_{i=0}^{n} b_i \times k^{(n-i)}.
     \]
   - 得到的 \(\text{ans}\) 即为序列的第 \(N\) 项。

这种思路利用了二进制数仅由0和1构成的特点,也可以抽象成 **"存在与否"** 的问题，将二进制表示直接“映射”到 \(k\) 进制上，从而快速得到答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int k, N;
    cin >> k >> N;
    long long ans = 0, power = 1;
    while(N){
        if(N & 1)
            ans += power;
        power *= k;
        N >>= 1;
    }
    cout << ans;
    return 0;
}

```