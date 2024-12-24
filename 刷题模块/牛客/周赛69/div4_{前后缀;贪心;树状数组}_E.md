[程家贺]
// https://ac.nowcoder.com/acm/contest/96115/E
#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
typedef long long ll;
#define REP(i, s, e) for (int i = (s); i < (e); ++i)
#define OUT(v) for (int k = 1; k < v.size(); ++k) cout << v[k] << ' '; cout << endl;
const int N = 1e5 + 10;
int h[N], e[2 * N], ne[N];


void solve() {
    int n;
    cin >> n;
    vector<ll> qz(n + 1, 0), a(n + 1, 0);
    vector<ll> sum(n + 1, 0);  // 正数的个数, 单调不减函数
    REP(i, 1, n + 1) cin >> a[i];
    REP(i, 1, n + 1) {
        qz[i] = qz[i-1] + a[i];
        sum[i] = sum[i-1] + (a[i] > 0 ? 1 : 0);
    }
    if (qz[n] % 3) {cout << 0; return;}
    int t1 = qz[n] / 3, pre = 0, pos = 0, res = 0;
    vector<ll> nw; //维护出现的 1/3 点的sum
    for (int i = 1; i <= n; i++) {
        if (qz[i] == t1) nw.push_back(sum[i]);
        if (qz[i] == 2 * t1) {
            while(pos < nw.size()) { // 找到第一个小于当前2/3点的sum的位置, 第二段正数判断
                if (nw[pos] >= sum[i]) break;
                else pos++;
            }
            if (sum[n] - sum[i] > 0) res += pos; // 第三段的正数判断
        }
    }
    cout << res << endl;
}

int main() {
    fast;
    solve();
    return 0;
}
