
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
