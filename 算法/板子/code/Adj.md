
## 稀疏图的存储 -Adj 
**`vector<vector<int>>`实现的adj**

```cpp
#include <bits/stdc++.h>
using namespace std;

#define w first
#define to second 

vector<vector<pair<int, int>>> adj;

void add(int a, int b, int c) {
    if (a >= (int)adj.size()) adj.resize(a + 1);
    adj[a].emplace_back(c, b); 
}

bool del(int a, int b) {
    if (a >= (int)adj.size()) return false;
    auto& v = adj[a];

    auto it = find_if(v.begin(), v.end(), [b](const pair<int, int>& edge) {
        return edge.to == b;
    });

    if (it != v.end()) {
        v.erase(it);
        return true;
    }
    return false;
}

/*
  for(auto e:adj[cur])
  {
        
    }
*/
```
