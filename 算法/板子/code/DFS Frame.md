

## 非递归DFS
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 3;                      // 元素数量
    vector<bool> vis(n);           // 是否被选过
    vector<int> path, idx(n + 1);  // 当前路径，每层候选起点
    int dep = 0;                   // 当前深度（path.size())

    while (dep >= 0) {
        if (dep == n) {            // 找到一个解
            for (int x : path) cout << x << " ";
            cout << "\n";
            dep--;                 // 回溯
            if (dep >= 0) {
                vis[path.back()] = false;
                path.pop_back();
                idx[dep]++;
            }
        } else if (idx[dep] >= n) {  // 本层选完了
            idx[dep] = 0;
            dep--;
            if (dep >= 0) {
                vis[path.back()] = false;
                path.pop_back();
                idx[dep]++;
            }
        } else {
            int x = idx[dep];
            if (vis[x]) {
                idx[dep]++;
            } else {
                vis[x] = true;
                path.push_back(x);
                dep++;
                if (dep < n) idx[dep] = 0;
            }
        }
    }
}
```