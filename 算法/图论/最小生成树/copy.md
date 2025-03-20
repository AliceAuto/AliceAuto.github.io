
---

## ✅ Prim 模板（邻接矩阵）

```cpp
#include <iostream>
#include <cstring>
using namespace std;

const int N = 510, INF = 0x3f3f3f3f;
int n, m, g[N][N], dist[N];
bool vis[N];

int prim() {
    memset(dist, 0x3f, sizeof dist);
    int res = 0;
    dist[1] = 0;
    for (int i = 1; i <= n; i++) {
        int t = -1;
        for (int j = 1; j <= n; j++)
            if (!vis[j] && (t == -1 || dist[j] < dist[t])) t = j;

        if (dist[t] == INF) return -1;
        vis[t] = true;
        res += dist[t];

        for (int j = 1; j <= n; j++)
            dist[j] = min(dist[j], g[t][j]);
    }
    return res;
}

int main() {
    cin >> n >> m;
    memset(g, 0x3f, sizeof g);
    while (m--) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u][v] = g[v][u] = min(g[u][v], w);
    }
    int ans = prim();
    cout << (ans == -1 ? "impossible" : to_string(ans)) << endl;
}
```

---

## ✅ Kruskal 模板（并查集）

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10;
int n, m, p[N];

struct Edge {
    int u, v, w;
    bool operator < (const Edge &e) const { return w < e.w; }
} e[N];

int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }

int kruskal() {
    sort(e, e + m);
    for (int i = 1; i <= n; i++) p[i] = i;

    int res = 0, cnt = 0;
    for (int i = 0; i < m; i++) {
        int a = find(e[i].u), b = find(e[i].v);
        if (a != b) {
            p[a] = b;
            res += e[i].w;
            if (++cnt == n - 1) break;
        }
    }
    return cnt < n - 1 ? -1 : res;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++)
        cin >> e[i].u >> e[i].v >> e[i].w;
    int ans = kruskal();
    cout << (ans == -1 ? "impossible" : to_string(ans)) << endl;
}
```

---

### ✅ 特点
- 简洁，去除注释，方便竞赛抄写。
- `Prim`：适合稠密图，邻接矩阵 \(O(n^2)\)。
- `Kruskal`：适合稀疏图，排序 + 并查集 \(O(mlogm)\)。

---
