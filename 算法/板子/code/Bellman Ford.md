
# Bellman-Ford
### SPFA的原型
**适合处理稠密图**

### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;

const int inf = 0x3f3f3f3f;
const int N = 510, M = 11000;
int dist[N], tmp[N];
int n, m, k;

struct Edge {
    int u, v, w;
} edges[M];

void bellman_ford() {
    memset(dist, inf, sizeof dist);
    dist[1] = 0;

    for (int i = 0; i < k; i++) {
        memcpy(tmp, dist, sizeof dist);
        for (int j = 0; j < m; j++) {
            auto e = edges[j];
            dist[e.v] = min(dist[e.v], tmp[e.u] + e.w);
        }
    }
}

bool nc_check() {
    for (int j = 0; j < m; j++) {
        auto e = edges[j];
        if (dist[e.u] != inf && dist[e.u] + e.w < dist[e.v]) {
            return true;
        }
    }
    return false;
}

```

### 分析

**bellman_ford算法在每一次遍历的时候，只允许更新一条边**
因此我们需要用last数组来存储上一次更新的边，  
每次更新一条边，如果一个点有多个出度边，在内循环中遍历所有边的时候，在这个点的所有出度边都会被更新。

**怎么判断是否有负权回路？**  
1.**在BF遍历n条边后dist[n]>0x3f3f3f3f/2的话 那么存在负权回路**
2.**在进行n-1次迭代后看是否还可以迭代**
