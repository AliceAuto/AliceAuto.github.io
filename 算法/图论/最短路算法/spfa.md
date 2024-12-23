
## 模板

```C++
#include<bits/stdc++.h>
using namespace std;

const int N=1e5+10;

int h[N],w[N],e[N],ne[N],idx,n,m;

bool st[N];
int dist[N];

void add(int a,int b,int c)
{
 e[idx]=b,w[idx]=c,ne[idx]=h[a],h[a]=idx++;   
}

void spfa()
{
    memset(dist,0x3f,sizeof dist);
    dist[1]=0;
    queue<int> q;
    q.push(1);
    st[1]=true;
    while(q.size())
    {
        int t=q.front();
        q.pop();
        //将队列中弹出的元素更新
        st[t]=false;
        for(int i=h[t];i!=-1;i=ne[i])
        {
            int j=e[i];
            if(dist[j]>dist[t]+w[i])
            {
                dist[j]=dist[t]+w[i];
                if(!st[j])
                {
                    st[j]=true;
                    q.push(j);
                }
            }
        }
    }
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
    spfa();
    if(dist[n]==0x3f3f3f3f) puts("impossible");
    else cout<<dist[n]<<endl;
    return 0;
}
```


## 如何判断是否存在负环

```C++
#include<bits/stdc++.h>
using namespace std;

const int N=2100,M=1e4+10;

int h[N],w[M],e[M],ne[M],idx,n,m;

bool st[N];
int dist[N];
int sz[N];

void add(int a,int b,int c)
{
 e[idx]=b,w[idx]=c,ne[idx]=h[a],h[a]=idx++;   
}

void spfa()
{
    //可以不将dist初始化为无穷大，因为dt数组的意义就是为了寻找负权边用的
   // memset(dist,0x3f,sizeof dist);
   // dist[1]=0;
    queue<int> q;
    //将所有的点都入队，因为负环不知道在那个点的后面，所以要全部入队
    for(int i=1;i<=n;i++)
    {
        st[i]=true;
        q.push(i);
    }
    while(q.size())
    {
      
        int t=q.front();
        q.pop();
        //将队列中弹出的元素更新
        st[t]=false;
        
        for(int i=h[t];i!=-1;i=ne[i])
        {
            int j=e[i];
            if(dist[j]>dist[t]+w[i])
            {
                dist[j]=dist[t]+w[i];
                /*只有距离变小的时候才会更新，也就是负环
                */
                sz[j]=sz[t]+1;
        //当1-j的点数大于等于n也就是有n+1条边，根据抽屉原理，一定会有一个环
                if(sz[j]>=n)
                {
                    cout<<"Yes"<<endl;
                    return ;
                }
                if(!st[j])
                {
                    st[j]=true;
                    q.push(j);
                }
            }
        }
    }
    cout<<"No"<<endl;
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
    spfa();
    return 0;
}
```