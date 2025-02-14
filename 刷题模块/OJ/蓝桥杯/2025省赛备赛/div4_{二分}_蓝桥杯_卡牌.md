---
layout: post
title: "卡牌"
permalink: /刷题模块/OJ/蓝桥杯/2025省赛备赛/div4_{二分;贪心}_蓝桥杯_卡牌.md/
date: 2025-02-14
author: "JNMC孙国庆"
---

#### [备用返回通道](../../README.md)
# [转到题目](https://www.luogu.com.cn/problem/P8800)


## 思路
### 思路一 :) **`二分`**


### 思路二 **`贪心`**
#### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int  unsigned long long 
const int N =2e5;
class ab 
{
public:
	int a;
	int b;
};

ab da[N];
int c[N];
int n,m;
int tem;
int res;
void solve(){
    for(int i = 0 ;i < n;i++){
        cin>>da[i].a;
    }
    for (int i = 0 ; i < n;i++){
        cin>>da[i].b;
    }
    sort(da,da+n,[](ab A, ab B){return A.a<B.a;});
    
    for (int i = 1 ;i< n;i++){
        c[i] = c[i-1]+ i*(da[i].a - da[i-1].a);
    }
    int lim=  0x3f3f3f3f;
    
    int mod =-1;//标记
    for (int i= 0 ; i <n;i++){
        if(c[i]<=m){
            tem = max(tem,da[i].a);
            lim = min(lim,da[i].a+da[i].b);
            
        }
        else//处理某个决定后空牌有剩余
         {
            mod = (m - c[i-1])/i;
            break;
        }
    }
    //处理最终空牌仍有剩余
    if(mod ==-1){
        mod =(m - c[n-1] )/n;
    }
    res = min(lim,tem+mod);


    
}
signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin>>n>>m;
    solve();
    cout<<res<<endl;
    return 0;
    
}
```