---
layout: post
title: "狠狠地算吗"
permalink: /刷题模块/OJ/牛客/杂/div5_{贪心;数学;思维题}_牛客_狠狠地算吗.md/
date: 2025-01-17
author: "JNMC孙国庆"
---

# [返回](https://aliceauto.github.io/%E5%88%B7%E9%A2%98%E6%A8%A1%E5%9D%97/OJ/)
# [转到题目](https://ac.nowcoder.com/acm/contest/19304/N)

## 解题思路
**首先,题目要求的是3个是数的运算最大值**
**其中可以随意加括号的意思是没有了乘与加法的运算优先级，并且优先级是多种情况**
而要求最大值，我们可以贪心考虑
- 运算一定是两步完成,我们为了让最终结果最大。我们只需要保证每一步都是当前最大的就可以
   - 第一步，我们可以选择加法或乘法
     - 分析可知，当操作数没有1时，*对结果的增益一定是比+大的
     - 当两个操作数有1时选择加法是当前最优
   - 第二步和第一步一样，不同的是把第一步的结果当做一个操作数
- 由于运算优先级不是唯一的，因此，我们需要在 **`第1、2个先运算`** 与 **`第2、3个先运算`** 之间的贪心中取最大值
  
## 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int a,b,c;
int res1,res2;
int main(){
    cin>>a>>b>>c;
    if(a==1||b==1){
        res1 = a+b;
    }
    else{
        res1 = a*b;
    }
    if(c==1){res1+=c;}
    else {res1*=c;}
    
    if(b==1||c==1){
        res2 = c+b;
    }
    else{
        res2 = c*b;
    }
    if(a==1){res2+=a;}
    else {res2*=a;}
    cout<<max(res1,res2)<<endl;
    return 0;
}
```