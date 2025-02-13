---
layout: post
title: "举手赢棋easy"
permalink: /刷题模块/OJ/牛客/周赛80/div4_{思维题}_牛客_举手赢棋easy.md/
date: 2025-02-10
author: "JNMC孙国庆"
---

#### [备用返回通道](../../README.md)
# [转到题目](https://ac.nowcoder.com/acm/contest/101196/C)
# 思路:
本题要求1的插入方案，使得每个前缀中1都不比0少，并且就有一个`插入1`
而为了优先保障可以赢，我们应该尽早插入一个有效1，以为更多的前缀贡献
这样我们就能得到一个线性关系:
- **插入的有效1越靠后，对应的贡献越小，直到贡献不足，让某个前缀中1的数量小于0**

同时我们只要保证不输就可以，因此，反而就没有必要选第一个`0`了，只要保证能赢就行
也就是我们直到快输的时候强制转变为`1`，这样就是极限的情况了，再晚就不行了。
我们只需要知道，包括极限情况时，之前有多少个可以变为1的0就可以了。
**以上是对使用一次`举手1`就可以获胜的情况(一般情况)，还有其他情况**

- (最期待情况)如果整局(极限情况)都没有用上 `举手1`也可以获胜,那么就可以在任意时间举手
- (最不期待情况)如果在保守情况下，尽快用了一次`举手1`，之后还有不合规的前缀，那么就意味着不会赢了，结果就是0
# 代码:

```cpp

#include <bits/stdc++.h>
using namespace std;
const int N = 1e5;

void solve() {
    int n;
    cin >> n; // 读取 n
    char in;
    int cnt1 = 0, cnt0 = 0;
    int cnt = 0, res1 = 0, res_case = 0;
    
    for (int i = 0; i < n; i++) {
        cin >> in;
        if (in == '1') cnt1++;
        else cnt0++;
        
        if (cnt1 < cnt0) { // 触发极限情况
            if (cnt == 0) { // 第一次触发
                res1 = cnt0;
                cnt1++;
                cnt0--;
                cnt++;
            } else { // 说明已经处于无法翻盘的情况
                res_case = 3;
                break;
            }
        }
    }

    if (res_case != 3) { 
        if (cnt == 1) { // 需要调整一次才能赢
            //res_case = 2;
            cout << res1 << endl;
        } else { // 直接就赢
            //res_case = 1;
            cout << n << endl;
        }
    } else { // 无法取胜
        cout << 0 << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    solve();    
    return 0;
}

```
