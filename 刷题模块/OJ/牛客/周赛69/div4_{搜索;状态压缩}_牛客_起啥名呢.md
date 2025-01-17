---
layout: post
title: "起啥名呢"
permalink: /刷题模块/OJ/牛客/周赛69/div4_{搜索;状态压缩}_牛客_起啥名呢.md/
date: 2025-01-17
author: "JNMC程家贺"
---

# [返回](https://aliceauto.github.io/%E5%88%B7%E9%A2%98%E6%A8%A1%E5%9D%97/OJ/)

```cpp
#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
typedef long long ll;
#define REP(i, s, e) for (int i = (s); i < (e); ++i)
#define OUT(v) for (int k = 0; k < v.size(); ++k) cout << v[k] << ' '; cout << endl;
const int N = 1e5 + 10;
int h[N], e[2 * N], ne[N];

int n, m, q;
// int g[8];
// int jh[8][8];
vector<int> g;
vector<vector<int>> jh;
int sum = 0;
int sz = 0;  // m 个 1的大小

vector<int> path;
vector<int> rs(100);
int ten(string s) { // 压缩, 传入01字符串压缩为二进制的int
    int res = 0, len = s.size();
    for (int i = 0; i < len; i++) {
        if (s[i] == '1') {
            res += pow(2, len - i - 1);
        }
    }
    return res;
}

bool ck(vector<int> &tg) {
    for (int i = 1; i <= n; i++) {
        if ((tg[i] ^ g[i]) != sz) return false; // tg[i] ^ g[i]要加小括号的, 
    }
    return true;
}

void dfs(int u, vector<int> tg) {
    if (u == q) { // 选择了q次
        if (ck(tg) && path.size() < rs.size()) {
            rs = path;
        }
        return;
    }
    for (int i = 0; i <= 1; i++) { // 0-1的顺序, tg可以不回溯, 1-0就得回溯了
        if (i == 0) {
            dfs(u + 1, tg);
        }
        else {
            int k = u + 1;
            vector<int> ttg = tg;
            for (int j = 1; j <= n; j++) {
                tg[j] = (tg[j] | jh[k][j]);
            }
            path.push_back(k);
            dfs(u + 1, tg);
            tg = ttg;
            path.pop_back();
        }
    }
}

void solve() {
    cin >> n >> m >> q;
    g.resize(n + 1), jh.resize(q + 1, vector<int> (n + 1));
    sz = int(pow(2, m) - 1);
    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        g[i] = ten(s);
    }
    for(int k = 1; k <= q; k++) {
        for (int i = 1; i <= n; i++) {
            string s;
            cin >> s;
            jh[k][i] = ten(s);
        }
    }
    vector<int> tg(n + 1);
    dfs(0, tg);
    if (rs.size() == 100) {
        cout << -1;
    }
    else {
        cout << rs.size() << endl;
        OUT(rs);
    }
}

int main() {
    solve();
}

```