// https://kamacoder.com/problempage.php?pid=1053

#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
typedef long long ll;
#define REP(i, s, e) for (int i = (s); i < (e); ++i)
#define OUT(v) for (int k = 0; k < v.size(); ++k) cout << v[k] << ' '; cout << endl;
const int N = 1e5 + 10;


int h[N], e[2 * N], ne[2 * N];
int w[2 * N]; // 第i条边的权值
int idx;

void add(int a, int b) { // a b 之间插入一条边
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> minDist(n + 1, INT_MAX);

    for (int i = 1; i <= m; i++) {
        int a, b, value;
        cin >> a >> b >> value;
        w[idx] = value;
        add(a, b);
        w[idx] = value;
        add(b, a);
    }
    vector<int> tree, us(n + 1, 0);
    tree.push_back(1), us[1] = 1;
    while(tree.size() < n) {
        int x = tree[tree.size() - 1];
        // 更新相邻节点的minDist
        for (int i = h[x]; i != -1; i = ne[i]) {
            if (!us[e[i]]) {
                minDist[e[i]] = min(w[i], minDist[e[i]]);
            }
        }
        // 寻找距离生成树最短距离的节点
        int mi = INT_MAX, idxx = -1;
        for (int j = 1; j <= n; j++) {
            if (!us[j]) {
                if (minDist[j] < mi) {
                    mi = minDist[j];
                    idxx = j;
                }
            }
        }
        tree.push_back(idxx);
        us[idxx] = 1;
    }
    int res = 0;
    for (int j = 2; j <= n; j++) {
        res += minDist[j];
    }
    cout << res;
}

int main() {
    fast;
    fill(begin(h), end(h), -1);
    solve();
    return 0;
}


