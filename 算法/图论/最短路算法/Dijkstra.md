## 朴素版dijkstra算法

### 思路

1. 初始化距离

```c++
dist[1]=0,dist[i]=0x3f
s[]//当前已经确定最短距离的点
```

2. for循环 每次迭代找到不在s中的距离最近的点，把这个点加入s中，用这个点更新其他点的距离  

3. 每次循环都确定一个最短路径的点

```C++
#include<bits/stdc++.h>
using namespace std;

const int N=510,M=1e5+10;

int g[N][N],dist[N];
bool st[N];
int n,m;

int dijkstra()
{
    memset(dist,0x3f,sizeof dist);
    dist[1]=0;
    
    for(int i=0;i<n;i++)
    {
        
    
    //找到当前最短路的末节点
    int t=0;
        for(int j=1;j<=n;j++)
        {
            if(!st[j]&&dist[t]>dist[j])
            t=j;
        }
    //t->j 不管能不能走因为n很小所以可以暴力搜索
    for(int j=1;j<=n;j++)
    {
        dist[j]=min(dist[j],dist[t]+g[t][j]);
    }
    
    st[t]=true;
    }
    if(dist[n]==0x3f3f3f3f) return -1;
    else return dist[n];
}

int main()
{
    memset(g,0x3f,sizeof g);
    cin>>n>>m;
    for(int i=0;i<m;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        //处理重边的情况，取最小的一条边
        g[a][b]=min(g[a][b],c);
    }
    int d=dijkstra();
    cout<<d<<endl;
    return 0;
}

```

## 堆优化的dijkstra算法

```c++
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
    //因为小根堆自动排序 将距离最近的放在top上面
    priority_queue<PII,vector<PII>,greater<PII>> heap;
    heap.emplace(0,1);

    while(heap.size())
    {
        auto t=heap.top();
        heap.pop();
        //拿到下标
        int ver=t.second;
        //已经遍历过的下标不需要再遍历
        if(st[ver])continue;
        st[ver]=true;
        //遍历下标 拿到最小的下一个最小
        for(int i=h[ver];i!=-1;i=ne[i])
        {
            int j=e[i];
            //如果1-j的距离大于1-ver+ver-这个j的距离
            //即有更小的距离 则更新
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