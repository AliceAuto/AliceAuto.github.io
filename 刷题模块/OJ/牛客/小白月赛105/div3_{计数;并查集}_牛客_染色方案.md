---
layout: post
title: "染色方案"
permalink: /刷题模块/OJ/牛客/小白月赛105/div3_{计数;并查集}_牛客_染色方案.md/
date: 2025-01-17
author: "JNMC孙国庆"
---

# [返回](https://aliceauto.github.io/%E5%88%B7%E9%A2%98%E6%A8%A1%E5%9D%97/OJ/)
# [转到题目](https://ac.nowcoder.com/acm/contest/95937/D)
## 思路
- 根据题目要求,我们需要求出来最少的染色次数，保证，每次访问颜色都是相同的。
- 那我们要思考，什么时候染色次数最少呢？
  - 难道每次查询前都要染色吗?不是吧
  - 那我们让染色尽可能少,是不是要让每次查询尽可能相同,但这不是我们能决定的
    - 查询元素不相同时，我们至少要保证，染色方案是最优的，某种决策集导致染色次数最少。
      - 而这种枚举连通图拓展决策的方式，可以用并查集来实现。
      - 我们只需计数每个连通图的节点数，就可以找到最小的那个连通图，并染色。
    - 查询元素相同时,我们可以让染色次数尽可能少。这种方式也是符合并查集的操作，它对连通图的增益是0，这是最好的。
- 因此我们只需要将每个查询用并查集处理，并且计数找最小只就可以了。

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
unordered_map<int, int> p;

int find(int x) {
    if(p.find(x)==p.end()) p[x] =x;
	if (x != p[x]) {
		p[x] = find(p[x]);
	}
	return p[x];
}
void merge(int x, int y) {
	int rootX = find(x);
	int rootY = find(y);
	p[rootX] = rootY;
}
int n, m;
int main() {
	cin >> n >> m;
	vector<int> f(n + 1);
	for (int i = 1; i <= n; i++) {
		cin >> f[i];
	}
	unordered_map<int, unordered_map<int, int>>tc;
	int x, y;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		merge(x, y);
	}
	for (int i = 1; i <= n; i++) {
		int root = find(i);
		if (p.find(i) != p.end())tc[root][f[i]]++;
	}
	int res = 0;
	for (auto ma : tc) {
		int tmax = 0;
		int total = 0;
		for (auto e : ma.second) {
			tmax = max(tmax, e.second);
			total += e.second;
		}
		res += (total - tmax);
	}
	cout << res << endl;
	return 0;
}
```