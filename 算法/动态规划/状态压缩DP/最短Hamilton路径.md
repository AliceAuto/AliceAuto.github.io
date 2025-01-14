
---

# 题目：最短 Hamilton 路径

## 题意

给定一张 $n$ 个点的带权无向图，点从 $0 \sim n-1$ 标号，求起点 $0$ 到终点 $n-1$ 的最短 Hamilton 路径。

Hamilton 路径的定义是从 $0$ 到 $n-1$ 不重不漏地经过每个点恰好一次。

## 输入格式

- 第一行输入整数 $n$。
- 接下来 $n$ 行每行 $n$ 个整数，其中第 $i$ 行第 $j$ 个整数表示点 $i$ 到 $j$ 的距离（记为 $a[i][j]$）。

对于任意的 $x, y, z$，数据保证 $a[x][x] = 0$，$a[x][y] = a[y][x]$ 并且 $a[x][y] + a[y][z] \geq a[x][z]$。

## 输出格式

输出一个整数，表示最短 Hamilton 路径的长度。

## 数据范围

- $1 \leq n \leq 20$
- $0 \leq a[i][j] \leq 10^7$

## 输入样例：

```
5
0 2 4 5 1
2 0 6 5 3
4 6 0 8 3
5 5 8 0 5
1 3 3 5 0
```

## 输出样例：

```
18
```

---

```C++
#include<bits/stdc++.h>
using namespace std;

const int N = 20,M = 1<<N;

// f[i][j] i代表用路径代表的二进制数 j代表从0-j走过的路径
int g[N][N],f[M][N];
int n;

int main() {
    cin>>n;
    
    for(int i = 0; i < n; i ++ ) 
     for(int j = 0; j < n; j ++)
        cin>>g[i][j];
    
    memset(f,0x3f,sizeof f);
    f[1][0] = 0;
    // 枚举所有路径
    for(int i = 0; i < 1<<n; i ++)
    // 走到那个点
        for(int j = 0; j < n; j++)
    // 如果当前路径中有这个点
          if(i >> j & 1)
    // 枚举从这个点到其他点的路径是否有最短路
            for(int k = 0; k < n; k ++)
                if(i>>k & 1)
                f[i][j] = min(f[i][j],f[i - (1 << j)][k] + g[k][j]);
                
    // 表示为所有点都走过了，终点为n-1的最短路
    cout<<f[(1 << n) - 1][n-1]<<endl;
    return 0;
}
```