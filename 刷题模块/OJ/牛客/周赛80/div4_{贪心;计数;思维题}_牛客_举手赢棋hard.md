---
layout: post
title: "举手赢棋hard"
permalink: /刷题模块/OJ/牛客/周赛80/div4_{贪心;计数;思维题}_牛客_举手赢棋hard.md/
date: 2025-02-10
author: "JNMC孙国庆"
---

#### [备用返回通道](../../README.md)
# [转到题目](https://ac.nowcoder.com/acm/contest/101196/D)
# 思路
和easy版本的区别在于我有两个`举手1`的机会，只要清晰地模拟这个过程就可以
# 代码
```cpp
#define ll long long
#include<bits/stdc++.h>
using namespace std;
int main(){
    ll n;
    cin>>n;
    string s;
    cin>>s;
    int p,p2,t=0;
    int cnt[2]={0};
    for(int i=0;i<n;i++){
        cnt[s[i]-'0']++;
        if(cnt[0]>cnt[1]){
            if(t>=2)
                //已经举过2次手
            {
                cout<<0;
                return 0;
            }
            else{
                t++;
                cnt[1]++;
                cnt[0]--;
                if(t==1)
                    //第一次举手后
                {
                    p=cnt[0]+1;//回溯记录
                }
                else    
                    //第二次举手后
                {
                    p2=cnt[0]+2;//回溯记录
                }
            }
        }
    }
    ll ans;
    if(t==0)
        //最希望情况
    {
        ans=n*(n-1)/2;
    }
    
    else
    {
        ll c=p;
        if(t==1)
            //举了一次手
        {
            ans=c*(c-1)/2+c*(n-c);
        }
        
        else   
            //举了一次手
        {
            ll c2=p2-p;
            ans=c*(c-1)/2+c*c2;
        }
    }
    cout<<ans;
    return 0;
}
```