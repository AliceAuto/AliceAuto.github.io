
# Bellman-Ford
### SPFA的原型
**适合处理稠密图**

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
