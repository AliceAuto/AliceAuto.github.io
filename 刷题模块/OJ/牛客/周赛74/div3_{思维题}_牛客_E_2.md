[JNMC张富涵]  
# [转到题目](https://ac.nowcoder.com/acm/contest/99458/E)

## 题目思路:
**题目说明**：把数组转化为严格递增或者严格递减的数组，其中有一部分是不需要排序的。

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
