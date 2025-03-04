
## 特点

1. 不管什么图的存储方式都可以只需要能遍历所有边即可
2. 可以指定走最多多少条边
3. 可以处理负权回路(不如spfa一根)

## 例题

### [有边数限制的最短路](https://www.acwing.com/problem/content/855/)

#### 题目介绍

给定一个 n个点 m条边的有向图，图中可能存在重边和自环，**边权可能为负数。**
请你求出从 1号点到 n号点的最多经过k条边的最短距离，如果无法从1号到n号点，输出 impossible。

注意：图中可能**存在负权回路** 。

**输入格式**   
第一行包含三个整数n,m,k。  
接下来m行，每行包含三个整数x,y,z,表示存在一条从点x到y的有向边，边权为z。  
点的编号为1-n。

**输出格式**
输出一个整数，表示从1号点到n号点的最多更新k条边的最短距离。  
如果不存在满足条件的路径，输出impossible。


### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;

const int N=510,M=11000;
int dist[N],last[N];
int n,m,k;
struct 
{
    int a,b,w;
}edges[M];

void bellman_ford()
{
    memset(dist,0x3f,sizeof dist);
    dist[1]=0;
    for(int i=0;i<k;i++)
    {
        memcpy(last,dist,sizeof dist);
        for(int j=0;j<m;j++)
        {
            auto e=edges[j];
            //松弛操作
            dist[e.b]=min(dist[e.b],last[e.a]+e.w);
        }
    }
     //三角不等式
     //dist[e.b]<=min(dist[e.b],last[e.a]+e.w);
}

int main()
{
    cin>>n>>m>>k;
    for(int i=0;i<m;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        edges[i]={a,b,c};
    }
    bellman_ford();
    if(dist[n]>0x3f3f3f3f/2) cout<<"impossible"<<endl;
    else cout<<dist[n]<<endl;
    return 0;
}


```

### 分析

**bellman_ford算法在每一次遍历的时候，只允许更新一条边**
因此我们需要用last数组来存储上一次更新的边，  
每次更新一条边，如果一个点有多个出度边，在内循环中遍历所有边的时候，在这个点的所有出度边都会被更新。

**怎么判断是否有负权回路？**  
**在BF遍历n条边后dist[n]>0x3f3f3f3f/2的话 那么存在负权回路**
