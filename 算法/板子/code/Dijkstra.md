> #### Dijkstra算法
> 是和BFS一样是贪心思想，不同的是，这个为**有权图**的最短路径算法。
### 思路

## 堆优化的dijkstra算法

```cpp
#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> PII;
const int N=151000;

int h[N],e[N],w[N],ne[N],idx;

int n,m;

bool st[N];
int dis[N];
void add(int a,int b,int c)
{
    e[idx]=b,w[idx]=c,ne[idx]=h[a],h[a]=idx++;
}

int dijkstra()
{
    memset(dis,0x3f,sizeof dis);
    dis[1]=0;

    priority_queue<PII,vector<PII>,greater<PII>> heap;
    heap.emplace(0,1);

    while(heap.size())
    {
        auto t=heap.top();
        heap.pop();
        int ver=t.second;
        if(st[ver])continue;
        st[ver]=true;
        for(int i=h[ver];i!=-1;i=ne[i])
        {
            int j=e[i];
            if(dis[j]>dis[ver]+w[i])
            {
                dis[j]=dis[ver]+w[i];
                heap.emplace(dis[j],j);
            }
        }

    }
    if(dis[n]==0x3f3f3f3f)return -1;
    return dis[n];
}

int main()
{
    memset(h,-1,sizeof h);
    cin>>n>>m;
    for(int i=0;i<m;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        add(a,b,c);
    }
    cout<<dijkstra()<<endl;
    return 0;
}

```
## 讨论
**你们有没有发现dijkstra算法和dfs与bfs实际上很相似，他们的区别是在`维护容器`与出入维护的不同上，dijkstra算法维护的是`优先队列`，而dfs与bfs维护的是`栈`或者`队列`。而且他在'入'时贪心地维护了dist,区别也就是如此**