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
### 思路一 **`二分`**
#### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long 
const int N = 2e5;
int res;
typedef struct a_b {
	int a;
	int b;
} a_b;
a_b  ab[N];
int n ,m;
bool check (int x)//用来确定答案是否在mid右侧
{
	int sum =0 ; 
	for (int i= 0; i <n ; i++){
		if(x - ab[i].a >ab[i].b)return false;
		else{
			sum += max(0LL,x - ab[i].a);
		}
	}
	if (sum <=m)return true;
	else return false;
	
	
}
void solve(){
	cin>>n>>m;
	for (int i =0 ; i<n ;i++)cin>>ab[i].a;
	for (int i = 0LL;i<n;i++)cin>>ab[i].b;
	sort(ab,ab+n,[](a_b x ,a_b y){return x.a < y.a;});
	int l = 0 ; 
	int r = n*n +n;
	int mid;
	while ( l +1< r) {
	    mid  = (l+r)>>1;
		if(check(mid))
		{
			l = mid ;
		}
		else r=mid ;
	}
	res = l;
	
	
}



signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	solve();
	cout<<res<<endl;
	return 0;
}
```

### 思路二 **`贪心`**
#### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int  unsigned long long 
const int N =2e5;
class ab //a_i 与 b_i 绑定，方便排序
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
    //输入
    for(int i = 0 ;i < n;i++){
        cin>>da[i].a;
    }
    for (int i = 0 ; i < n;i++){
        cin>>da[i].b;
    }
    //a_i为主键排序
    sort(da,da+n,[](ab A, ab B){return A.a<B.a;});
    
    //求特殊用途前缀
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