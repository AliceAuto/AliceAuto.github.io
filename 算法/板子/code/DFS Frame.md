

## 非递归DFS
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 3;  // 候选总数，例如 0, 1, 2 表示候选
    vector<int> sol;           // 当前解（路径）
    vector<bool> used(n, false); // 标记候选是否被使用
    vector<int> nextIndex(n + 1, 0); // 各层候选起始位置，n+1保证层数足够
    int level = 0;             // 当前处在第几层

    while (level >= 0) {
        if (level == n) {  // 当前路径已满，找到一个完整解
            for (int x : sol) 
                cout << x << " ";
            cout << "\n";
            // 回溯：退回上一层，并准备尝试其它候选
            level--;
            if (level >= 0) {
                used[sol.back()] = false;
                sol.pop_back();
                nextIndex[level]++; // 上一层继续尝试下一个候选
            }
        }
        else if (nextIndex[level] >= n) { 
            // 当前层候选全部尝试完毕，回溯
            nextIndex[level] = 0; // 重置本层候选指针
            level--;
            if (level >= 0) {
                used[sol.back()] = false;
                sol.pop_back();
                nextIndex[level]++; // 上一层继续尝试下一个候选
            }
        }
        else {  // 当前层还有候选可选
            int candidate = nextIndex[level];
            if (used[candidate]) { 
                // 如果 candidate 已经使用，跳过（候选指针后移）
                nextIndex[level]++;
            } else {
                // 选择 candidate
                used[candidate] = true;
                sol.push_back(candidate);
                level++;
                if (level < n)
                    nextIndex[level] = 0;  // 初始化新层候选指针
            }
        }
    }
    return 0;
}

```