# [树的dfs](https://www.acwing.com/problem/content/4313/)

### 题目描述

给定一棵 n个节点的树。

节点的编号为 1∼n，其中 1号节点为根节点，**每个节点的编号都大于其父节点的编号。**

我们规定，当遍历（或回溯）到某一节点时，**下一个遍历的目标应该是它的未经遍历的子节点中编号最小的那一个子节点。**

### 分析
因为题目要求，我们每次遍历的目标都应该是子节点中编号最小的，也就是说我们需要提前找到最小编号。  
如果使用数组存储节点
```
int h[N], e[M], w[M], ne[M], idx;

void add(int a, int b, int c)  // 添加一条边a->b，边权为c
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}
```
没有办法进行排序，因此我们可以用
```
vector<int> h[N];
```
来存储图，这样只需要进行sort排序就可以得到升序
```
for(int i=0;i<h.size();i++) sort(h[i].begin(),h[i].end())
```
**本题关键在于从dfs序不会改变，从1开始的dfs序列是最全的**，因此我们可以预处理。
此外 我们还需两个数组来存储dfs序列和关于dfs序列的映射
```
int dfs(int x)
{
    //将dps到的元素推入
    q.push_back(x);
    sz[x]=1;
    for(auto t : g[x])
    {
        sz[x]+=dfs(t);
    }
    return sz[x];
    
}
    //a[i]映射dfs序
     for(int i = 0; i < q.size(); i ++) a[q[i]] = i;

```
代码中的sz数组是存放对于x根节点的节点数，如果sz[x]>k则不存在


----------

#### C++ 代码
```
#include<bits/stdc++.h>
using namespace std;

const int N=2e5+10;

vector<int>g[N];
vector<int> q;//dfs顺序
int n,m,u,k;
int a[N];
int sz[N];

int dfs(int x)
{
    //将dps到的元素推入
    q.push_back(x);
    sz[x]=1;
    for(auto t : g[x])
    {
        sz[x]+=dfs(t);
    }
    return sz[x];
    
}
int main()
{
    cin>>n>>m;
    for(int i=2;i<=n;i++)
    {
        int t;
        cin>>t;
        g[t].push_back(i);
    }
    dfs(1);
    //a[i]映射dfs序
     for(int i = 0; i < q.size(); i ++) a[q[i]] = i;



    while(m--)
    {
        cin>>u>>k;
        
        if(k>sz[u]) puts("-1");
        else 
        {
            cout<<q[a[u]+k-1]<<endl;
        }
    }
    return 0;
}
```