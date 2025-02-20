#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
using ll = long long;
#define int long long
#define OUT(v)                         \
    for (int k = 0; k < v.size(); ++k) \
        cout << v[k] << ' ';           \
    cout << endl;
const int N = 1e5 + 10;
int h[N], e[2 * N], ne[N];
const int MOD = 1e9 + 7;
int mul(int x, int y) {return 1LL * x * y % MOD; }
int fact[N], ifact[N];