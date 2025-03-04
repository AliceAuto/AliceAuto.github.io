
## 不允许存在负权回路

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N=210,INF=2e9;

int n,m,q;
int d[N][N];

void Floyd()
{
    for(int k=1;k<=n;k++)
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
}
int main()
{
    
    cin>>n>>m>>q;
    
    
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= n; j ++ )
            if (i == j) d[i][j] = 0;//将自环变成0，重边保留长度最小的边
            else d[i][j] = INF;//其他为正无穷
    
    for(int i=0;i<m;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        d[a][b] = min(d[a][b], c);
    }
    while(q--)
    {
        int a,b;
        cin>>a>>b;
        if(d[a][b]>INF/2)puts("impossible");
        else cout<<d[a][b]<<endl;
    }
    return 0;
}
```