## Kruskal算法 O(mlogm)

### 流程

1. 将所有边按权值从小到大排序(快排)O(mlogm)
2. 枚举每条边a-b 权重c O(m)  
- 如果a-b不在同一个集合中，则将a-b加入集合，并累加权重c
- 可以用并查集维护集合

    ```C++
    const int N = 1e5 + 10;
    int n, m, fa[N];

    struct Edge {
        int u, v, w;
        bool operator<(const Edge &e) const { return w < e.w; }
    };
    vector<Edge> edges;

    int find(int x) { return x == fa[x] ? x : fa[x] = find(fa[x]); }

    int kruskal() {
        iota(fa, fa + n + 1, 0);
        sort(edges.begin(), edges.end());
        int res = 0, cnt = 0;

        for (auto [u, v, w] : edges) {
            int fu = find(u), fv = find(v);
            if (fu != fv) {
                fa[fu] = fv;
                res += w;   
                if (++cnt == n - 1) break;
            }
        }
        return cnt == n - 1 ? res : -1;
    }

```