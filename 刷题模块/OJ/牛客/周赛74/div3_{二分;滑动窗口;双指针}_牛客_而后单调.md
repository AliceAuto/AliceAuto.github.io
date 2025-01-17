---
layout: post
title: "而后单调"
permalink: /刷题模块/OJ/牛客/周赛74/div3_{二分;滑动窗口;双指针}_牛客_而后单调.md/
date: 2025-01-17
author: "JNMC张富涵"
---

# [返回](https://aliceauto.github.io/%E5%88%B7%E9%A2%98%E6%A8%A1%E5%9D%97/OJ/)
### 思路引导:

题目说，先选m个隔离，剩下的n-m个排序，问把有没有能让m插入后是严格单调的可能。
如果我们从正向分析，由于没有优质推论，我们可能需要暴力来获得答案，海底捞针。
### 思路1:`正难则反,逆向思维`
我们知道,如果题目存在解,那它一定是经过层层操作后，是单调的。
这可以推出:
- `m项`是单调的`(因为没变)`
- `n-m项`为m项留足"间隔"

这是答案的性质(必要性)
那充分性呢？是否充要?
我们发现，反过来也满足，因此条件是`充要条件`

既然已经知道了充要条件，我们怎么知道不存在这样的情况呢?
这里一个巧妙的思维就是，从"值域"上看,这里的"值域"是普通的排序序列
由于我们知道，如果有解，一定是在这个值域上，因此。
如果存在解，一定满足充要条件:
- `m项`一定是在原数组中也连续且有序
- `n-m项`一定为m项留足了空间
由于这个值域比较小，我们只需枚举check上面条件，如果没有满足的就是NO，否则YES

### 思路2:


此时我们只需要找到不需要排序的那些数组的最大长度是否大于题目要求的长度即可，举个例子，如 `12 3 8 7 6 5`，其中 `8 7 6 5` 排序前后顺序是不变的（8 一定在 7 的左边，7 一定在 6 的左边）。也就是说排序前和排序后两个的顺序差都是 1。

1. **输入处理**：在输入时检查是否有重复的数字，若有重复则直接输出 `NO`。
   
```cpp
for (int i = 1; i <= n; i++) {
    cin >> b[i];
    r.insert(b[i]);   // 把输入的数字存到 set 里面，利用 set 排序
    if (e[b[i]]) bq = 1;
    e[b[i]]++;
}
if (bq) {
    cout << "NO" << endl;
    return;
}
```

2. **获取排序后的位置**：排序后每个元素的位置。

```cpp
int index = 1;
for (auto i : r) j[i] = index++;
```

3. **暴力枚举获取最长的严格递增或严格递减子数组的长度**：

```cpp
for (int i = 2; i <= n; i++) {
    if (j[b[i]] == j[b[i - 1]] + 1) z++;  
    else {
        ma1 = max(ma1, z);
        z = 1;
    }
    if (j[b[i]] + 1 == j[b[i - 1]]) j1++;
    else {
        mi1 = max(mi1, j1);
        j1 = 1;
    }
}
mi1 = max(mi1, j1);
ma1 = max(ma1, z);
```

4. **最终判断**：根据子数组长度判断是否符合题目要求。

```cpp
if (mi1 >= m || ma1 >= m) cout << "YES" << endl;
else cout << "NO" << endl;
```

## 完整代码如下：

```cpp
#include<iostream>
#include<cmath>
#include<set>
#include<map>
#include<cstring>
#include<algorithm>
using namespace std;

void solve() {
    map<long long, int> j;
    map<long long, int> e;
    set<long long> r;
    int n, m;
    cin >> n >> m;
    
    int mi1 = 0;
    int ma1 = 0;
    int bq = 0;
    int z = 1;
    int j1 = 1;
    int b[200005] = {0};
    
    // 输入处理
    for (int i = 1; i <= n; i++) {
        cin >> b[i];
        r.insert(b[i]);
        if (e[b[i]]) bq = 1;
        e[b[i]]++;
    }

    int index = 1;
    if (bq) {
        cout << "NO" << endl;
        return;
    }

    // 获取排序后的元素位置
    for (auto i : r) j[i] = index++;

    // 计算最长的递增和递减子数组长度
    for (int i = 2; i <= n; i++) {
        if (j[b[i]] == j[b[i - 1]] + 1) z++;
        else {
            ma1 = max(ma1, z);
            z = 1;
        }
        if (j[b[i]] + 1 == j[b[i - 1]]) j1++;
        else {
            mi1 = max(mi1, j1);
            j1 = 1;
        }
    }
    
    mi1 = max(mi1, j1);
    ma1 = max(ma1, z);

    // 最终判断输出结果
    if (mi1 >= m || ma1 >= m) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
```

--- 
