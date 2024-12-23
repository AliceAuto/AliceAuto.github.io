// https://kamacoder.com/problempage.php?pid=1053
// Kruskal 
#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
typedef long long ll;
#define REP(i, s, e) for (int i = (s); i < (e); ++i)
#define OUT(v) for (int k = 0; k < v.size(); ++k) cout << v[k] << ' '; cout << endl;
const int N = 1e5 + 10;

struct Edge { // 左右节点, 权值
    int l, r, val;
};

// 并查集
vector<int> father;
void init(int size) {
    father.resize(size + 1);
    for (int i = 0; i <= size; i++) father[i] = i;
}

int find(int u) {
    return u == father[u] ? u : father[u] = find(father[u]);
}
bool same(int a, int b) {
    a = find(a);
    b = find(b);
    return a == b;
}
void add(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    father[b] = a;
}

void solve() {
    int n, m;
    cin >> n >> m;
    init(n);
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].l >> edges[i].r >> edges[i].val;
    }
    sort(edges.begin(), edges.end(), [](const Edge&a, const Edge&b) {return a.val < b.val; });
    int res = 0, cur = 0;
    for (auto it: edges) {
        if (!same(it.l, it.r)) {
            res += it.val;
            cur++;
            add(it.l, it.r);
        }
        if (cur >= n - 1) break;
    }
    cout << res;
}

int main() {
    fast;
    solve();
    return 0;
}


