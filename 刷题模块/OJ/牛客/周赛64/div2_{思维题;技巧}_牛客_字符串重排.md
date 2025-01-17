---
layout: post
title: "字符串重排"
permalink: /刷题模块/OJ/牛客/周赛64/div2_{思维题;技巧}_牛客_字符串重排.md/
date: 2025-01-17
author: "JNMC孙国庆"
---

# [返回](https://aliceauto.github.io/%E5%88%B7%E9%A2%98%E6%A8%A1%E5%9D%97/OJ/)
# [转到题目](https://ac.nowcoder.com/acm/contest/92662/E)

## 思路
- 首先,题目让我们求的是，所有字符不在原来位置的排列.
- 那我们想,怎么样才能让所有字符不在原来位置呢?
- 如果，我们考虑单个字符，很显然，我们需要保证移动的到的位置对应的的字符，不能和自己一样的。那我应该怎么选呢?
  - 到此为止，至少你是知道你能暴力出来这个过程的. 
    - 那有没有可能某个字符没有可以移动的位置呢? 
      - 一个有n个字符的s字符串,当为其中一个字符选位置的时候可能的是
        - s.size()-n，
        - 第二个是s.size()-n-1
        - s.size()-2
        - s.size()-3
        - ...
        - 剩余为0
      - 也就说，当某个相同字符数量大于size()/2的时候,就一定没有办法完全移动到其他位置.
      - 所以，我们可以通过这种模拟的方法做出来，但是这种方式总归太麻烦了
      - 这里，我介绍一种针对于，这种问题的技巧
      - 核心是字符"集"偏移。
      - 让每个同类字符都有相同的偏移后都与自己排斥。那能符合条件的情况就是，让相同字符最多的字符偏移后也保持与自己排斥

```C++
#include<bits/stdc++.h>
using namespace std;
string s;

int main()
{
    ios::sync_with_stdio(0),cin.tie(); 
    cin>>s;
    vector<pair<char,int>> a(s.size());
    string ans(s.size(), ' ');
    int cnt[500];
    memset(cnt,0,sizeof(cnt));
    int mx=0;
    for(int i=0;i<s.size();i++)
    {
        a[i].first=s[i],a[i].second=i;
        cnt[s[i]-'a']++;
        mx=max(mx,cnt[s[i]-'a']);
    }
    if(mx>s.size()/2)
    {
        cout<<-1<<endl;
        return 0;
    }
    sort(a.begin(),a.end(),[](const pair<char,int>&a1,const pair<char , int >&a2)
         {return a1.first<a2.first;});
    for(int i=0;i<s.size();i++)
    {
        ans[a[i].second]=a[(i+mx)%s.size()].first;
        
    }
     cout << ans << endl;
    return 0;
}

```



