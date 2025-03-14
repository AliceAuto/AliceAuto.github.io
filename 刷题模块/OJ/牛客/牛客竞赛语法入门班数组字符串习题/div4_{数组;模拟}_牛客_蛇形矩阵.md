---
layout: post
title: "蛇形矩阵"
permalink: /刷题模块/OJ/牛客/牛客竞赛语法入门班数组字符串习题/div4_{数组;模拟}_牛客_蛇形矩阵.md/
date: 2025-03-14
author: "JNMC孙国庆"
oj_url: "https://ac.nowcoder.com/acm/contest/19306/1027"
---

#### [备用返回通道](../../README.md)
#### [转到题目](https://ac.nowcoder.com/acm/contest/19306/1027)
---
### [前备知识](../../../../竞赛技巧/数组遍历.md)

**这个题目实际上就是个模拟题，几乎是只要会语法就可以做出来**
但是有一个问题就是
#### <span style="color:red"> 大家都会，你怎么样轻松的做出，优雅的做出来?</span>
**我的经验是:`先思后动`**
如果你看到题目就开始码，但凡过程中出现一点点坑位，你也就崩了。
>
> **因此，就算是简单的题，一定是要在大脑有了大致的逻辑闭环后再进行码**
> **如果发现很难维护，这个方式大概率不会成功**


### 思路




| 1 | 2 | 6 | 7 |
|---|---|---|---|
| 3 | 5 | 8 | 13 |
| 4 | 9 | 12 | 14 |
| 10 | 11 | 15 | 16 |

**与负对角线平行的满足i+j为定值**
根据i是奇数函数偶数，判定遍历方向
枚举i确定j
因此根据奇偶性确定j的枚举顺序就好

```cpp
#include <iostream>
using namespace std;
int a[1000][1000];
int main()
{
	int n,i,j,sum=0;
	cin>>n;
	for(i=0;i<2*n-1;i++)
		for(j=i;j>=0;j--)
		{
			if(j<n&&i-j<n) sum++;
			if(i%2!=0) a[i-j][j]=sum;
			else a[j][i-j]=sum;
		}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++) cout<<a[i][j]<<" ";
		cout<<"\n";
	}
}
```