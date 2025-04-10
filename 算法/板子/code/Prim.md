
```cpp

const int N = 510, INF = 0x3f3f3f3f;
int n, g[N][N], dist[N]; // g[i][j] = 边权
bool vis[N];

int prim() {
    memset(dist, 0x3f, sizeof dist);
    memset(vis, 0, sizeof vis);
    dist[1] = 0;
    int res = 0;

    for (int i = 1; i <= n; ++i) {
        int t = -1;
        for (int j = 1; j <= n; ++j)
            if (!vis[j] && (t == -1 || dist[j] < dist[t]))
                t = j;

        if (dist[t] == INF) return -1;
        vis[t] = true;
        res += dist[t];

        for (int j = 1; j <= n; ++j)
            if (!vis[j]) dist[j] = min(dist[j], g[t][j]);
    }
    return res;
}

```