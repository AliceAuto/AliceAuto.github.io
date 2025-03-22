---
layout: post
title: "小紫的树上染色"
permalink: /刷题模块/OJ/牛客/周赛85/div2_{搜索;图论;二分;贪心}_牛客_小紫的树上染色.md/
date: 2025-03-21
author: "JNMC孙国庆"
oj_url: "https://ac.nowcoder.com/acm/contest/103948/F"
---

#### [备用返回通道](../../README.md)
#### [转到题目](https://ac.nowcoder.com/acm/contest/103948/F)


#### 思路：

**题意分析：**  
题目要求我们在 `k` 次染色机会下，最小化联通块的大小。  

普遍的想法可能是直接尝试每一个可能的方案来找到最优结果，但这显然不可行。
**我们需要将问题转化成一个我们能控制的形式：**

- 假设我们只有一次染色机会，那我们应该选取最优的染色位置。具体选哪个位置，虽然我们不容易直接确定。
- 如果我们假设有两次染色机会，我们可以知道结果一定是小于或等于一次染色机会时的最大值。  

**通过这种分析，我们可以发现 `k` 次染色机会与最小的联通块大小之间是负相关的**
**即 `k` 越多，最小联通块的MAX大小可能越小。** 
虽然我们无法直接计算出某次染色机会下的最大联通块大小，但 `k` 是有限的，并且随着 `k` 的增加，结果具有单调性。因此，我们可以通过二分法来确定最小的联通块大小 `MAX`。  

**具体步骤：**  
1. **二分查找：**  
   由于 `k` 是有限的，我们可以利用单调性来使用二分法找到合适的 `MAX` 值。  
   - **check 函数：** 对于每个 `MAX` 值，我们需要判断是否存在 `x` 次染色机会，使得所有的联通块大小都小于等于 `MAX`，并且染色的次数不大于 `k` 。(因为我们要收缩右边界）  

2. **保证每次染色都能最大化结果：**  
   我们希望通过染色使得联通块尽可能大，这样避免浪费染色机会。  

3. **从叶子节点开始考虑：**  
   我们可以从树的叶子节点开始，进行 DFS。如果某个节点被染色了，那么其子树就会被切除，不再考虑。如果未染色，就将该节点的影响累加。  

4. **优化染色策略：**  
   当某个节点不染色时，可能导致联通块的大小超过 `MAX`。因此，当这种情况出现时，我们就需要染色该节点。这样可以确保每次染色的效果最大化，从而接近我们目标的 `MAX`。

通过这样的策略，我们可以高效地找到最小的联通块大小 `MAX`，并确保在 `k` 次染色机会下，能够达到题目要求的目标。


```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
const int M = 2 * N;
int n, k;
int h[N], e[M], ne[M], idx;
int cnt;


void init() {
    memset(h, -1, sizeof h);
    idx = 0;
}

void add(int a, int b) {
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}


int dfs(int p, int parent, int lim) {
    int sum = 1; 
    for (int i = h[p]; i != -1; i = ne[i]) {
        int j = e[i];
        if(j == parent) continue;
        sum += dfs(j, p, lim);
    }
    if(sum > lim) {
        cnt++; 
        return 0; 
    }
    return sum;
}
bool check(int lim) {
    cnt = 0;
    dfs(1, 0, lim);
    return (cnt <= k);
}

void solve(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    init();
    cin >> n >> k;
    if(k >= n) {
        cout << 0;
        return;
    }
    
    for (int i = 1; i <= n - 1; i++){
        int a, b;
        cin >> a >> b;
        add(a, b);
        add(b, a);
    }
    
    int l = 1, r = n, ans = n;

    while(l < r) {
        int mid = (l + r) >> 1;
        if(check(mid)) { 
            ans = mid;
            r = mid;
        } else {      
            l = mid + 1;
        }
    }
    cout << ans;
}

int main(){
    solve();
    return 0;
}

```