
## 稀疏图的存储 -Adj 
**`vector<vector<int>>`实现的adj**

```cpp
#include <bits/stdc++.h>
using namespace std;
#define w first
#define to second
vector<vector<pair<int,int>>> adj;

void add(int a,int b,int c){
    adj[a].push_back({b,c});
}

bool del(int a,int b){
    bool flg =false;
    for(auto  e = adj[a].begin();e!=adj[a].end();){
        if(e->to ==b){
            e = adj[a].erase(e);
            flg =true;
            break;
        }
        else{
            ++e;
        }
    }
    return flg;
}
/*
  for(auto e:adj[cur])
  {
        
    }
*/
```
