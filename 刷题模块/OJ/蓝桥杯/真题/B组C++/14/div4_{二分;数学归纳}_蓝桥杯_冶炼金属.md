---
layout: post
title: "冶炼金属"
permalink: /刷题模块/OJ/蓝桥杯/真题/B组C++/14/div4_{二分;数学归纳}_蓝桥杯_冶炼金属.md/
date: 2025-03-27
author: "JNMC孙国庆"
oj_url: "https://www.lanqiao.cn/problems/3510/learning/"
---

#### [备用返回通道](../../README.md)
#### [转到题目](https://www.lanqiao.cn/problems/3510/learning/)
# 思路1:二分
**首先我们先用数学公式表述关系**
$$
    B =  \lfloor A/V \rfloor \tag{1}
$$
$$ 
   A  = B*V + k  (0<=k < V)  \tag{2} 
$$
$$
根据(2)发现为线性函数，具有全局单调性   \Longrightarrow  二分答案\\ 
根据(1)发现V 越大 B越大 \\ 
\Longrightarrow MIN根据每条记录找f(V) ==B的最小V \Longrightarrow收缩左边界 \\
同理 \Longrightarrow MAX找每条记录f(V) ==B的最大V \Longrightarrow收缩有边界
$$



```cpp
#include<bits/stdc++.h>
using namespace std;
int A,B;
bool check1(int V)//V没到最小时
{
	return B >= A/V;
}
bool check2(int V)//V没到最大时
{
	return B<=A/V;
}
int mi= 0;
int ma= 1e9;
int l,r;
int main(){
	int T;
	cin>>T;
	
	while(T--){
		cin>>A>>B;
		l = mi;
		r = ma;
		while(l<r){
			
			int mid = (l+r)>>1;

			if(check1(mid))r =mid;
			else l = mid+1;
		}			
		mi = max(mi,r);
		l = mi;
		r = ma;
		while(l<r){
			int mid =(l+r+1)>>1;
			if(check2(mid))l = mid;
			else r = mid-1;
		}
		ma = min(ma,l);
	}
	cout<<mi<<" "<<ma<<endl;
	
	
	return 0;
}
```
# 思路2:数学推导
```cpp
#include<bits/stdc++.h>
using namespace std;
/*
X: V O/X
每一条记录要保证
A = B*V +k (0<=k<V)
mi: V= (A-k)/B  <=> V = (A-V+1)/B => V = vB = A -v+1 => V(B+1) =A+1 => V =(A+1)/(B+1) 
向上取整=>保证合法 V = (A+B+1)/(B+1) 
ma = V = A/B
向下取整保证合法 => V =A/B (没变)
B = floor(A/V)  ==> V:[(A+B+1)/(B+1),A/B]
维护交集
*/
#define int long long
const int INF=0x3f3f3f3f3f3f3f3f;
#define inf INF
signed main(){
  int mi = -inf;
  int ma = inf;
  int T ;
  cin>>T;
  int l,r;
  int A,B;
  while(T--){
    cin>>A>>B;
    l = (A+B+1)/(B+1);
    r =A/B;
    mi = max(l,mi);
    ma = min(r,ma); 

  }
  cout<<mi<<" "<<ma<<endl;


  return 0;
}
```