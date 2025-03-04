## Kruskal算法 O(mlogm)

### 流程

1. 将所有边按权值从小到大排序(快排)O(mlogm)
2. 枚举每条边a-b 权重c O(m)  
- 如果a-b不在同一个集合中，则将a-b加入集合，并累加权重c
- 可以用并查集维护集合

```C++
#include<bits/stdc++.h>
using namespace std;

const int N=1e5+10,M=2e5+10,INF=0x3f3f3f3f;

struct Edge
{
    int a,b,w;
    bool operator<(const Edge&A)
    {
        return w<A.w;
    }
} e[M];

int p[N];
int n,m;
//因为考虑到集合问题，所以可以用并查集 查询是否在一个集合里面
int find(int x)
{
    if(p[x]!=x)p[x]=find(p[x]);
    return p[x];
}

int kruskal()
{
    //初始化每个集合
    for(int i=1;i<=n;i++)p[i]=i;
    //res代表总距离，cnt代表节点个数
    int res=0,cnt=0;
    //枚举m次边
    for(int i=0;i<m;i++)
    {
        //对于每个节点从a-b的边
        int a=e[i].a,b=e[i].b;
        //找到他的点的集合
        a=find(a),b=find(b);
        //这两个点如果不在一个集合里面
        if(a!=b)
        {
            //加入集合，并且节点数加1
            cnt++;
            p[a]=b;
            //因为w排序了，此时的w就是最小值，直接加就可以了
            res+=e[i].w;
        }
    }
    //如果节点数少于n-1个 也就是说没法构成连通图
    if(cnt<n-1)return INF;
    return res;
}
int main()
{
    cin>>n>>m;
    for(int i=0;i<m;i++)
    {
        int a,b,w;
        cin>>a>>b>>w;
        e[i]={a,b,w};
    }
    sort(e,e+m);
    int t=kruskal();
    if(t==INF)puts("impossible");
    else cout<<t<<endl;
    return 0;
}

```