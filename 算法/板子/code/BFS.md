**下面是一个点稀疏的BFS:**
- **图的存储方式:邻接矩阵**
- **基本数据结构:STL**
- **参数解释:**
  - g: 图的邻接矩阵
  - s: 起点
  - e: 终点

```cpp
#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define x first
#define y second
#define PII pair<int, int>
template<typename T> using mat = vector<vector<T>>;

mat<int> g;

void bfs(PII s, PII e) {
    int n = g.size();
    int m = g[0].size();
    
    auto checker = [&] (PII p) {
        return p.x >= 0 && p.x < n && p.y >= 0 && p.y < m;
    };

    mat<bool> vis(n, vector<bool>(m, 0));
    mat<PII> pre(n, vector<PII>(m, {-1, -1}));
    queue<PII> q;
    q.push(s);
    vis[s.x][s.y] = 1;

    vector<int> dx = {1, 0, -1, 0};
    vector<int> dy = {0, 1, 0, -1};

    while (!q.empty()) {
        auto p = q.front();
        q.pop();
        if (p == e) {
            vector<PII> path;
            while (p != s) {
                path.push_back(p);
                p = pre[p.x][p.y];
            }
            path.push_back(s);
            reverse(all(path));
            for (auto p : path) {
                cout << p.x << " " << p.y << endl;
            }
            return;
        } 
        for (int i = 0; i < 4; i++) {
            PII np = {p.x + dx[i], p.y + dy[i]};
            if (checker(np) && !vis[np.x][np.y] && !g[np.x][np.y]) {
                q.push(np);
                vis[np.x][np.y] = 1;
                pre[np.x][np.y] = p;
            }
        }
    }
}

```

**下面是一个边关系比较稀疏的BFS:**


```cpp
#include <bits/stdc++.h>
using namespace std;
#define all(x) (x).begin(), (x).end()
const int N = 1e5;
vector<int> adj[N];
int pre[N];
int n;


void add(int a, int b) {
    adj[a].push_back(b);
}

void BFS() {
    queue<int> q;
    q.push(1);
    bitset<N> st;
    st[1] = true;
    memset(pre, -1, sizeof pre);
    pre[1] = -1;

    while (!q.empty()) {
        int f = q.front();
        q.pop();

        if (f == n) {
            vector<int> path;
            for (int cur = n; cur != -1; cur = pre[cur]) {
                path.push_back(cur);
            }
            reverse(all(path));
            for (int x : path) {
                cout << x << " ";
            }
            return;
        }

        for (int j : adj[f]) {
            if (!st[j]) {
                st[j] = true;
                pre[j] = f;
                q.push(j);
            }
        }
    }
}

```