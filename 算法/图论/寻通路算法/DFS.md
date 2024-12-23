# DFS 算法

## 算法描述
- DFS的核心是**分枝搜索，策略性回溯，递归性解决**
- DFS是路径算法的主干，另外还有一些常伴随出现的技巧
- 空间复杂度O(h)  
剪枝：在搜索过程中，如果发现当前路径不可能到达目标，则停止搜索，直接回溯

## 适用性
- 这个算法没有在搜索过程中进行剪枝，因此得到的路径只具有一般的特征
- 如需要得到最短路径等等特性路径，需要对搜索树进行剪枝，但效率不高
- 适合寻找全集联通路径
  
## 数据结构选择
- 图的邻接表  \( 稀疏图\)、的邻接矩阵 \(稠密图\)
- 栈
- 路径vector

## 容器算法模板
* 可达性
```C++
#include <stack>
#include <set>
#include <iostream>
#include <vector>
using namespace std;

const int RowMax = 1e3 + 5; // 行最大值
const int ColumnMax = 1e3 + 5; // 列最大值
#define INIT 0 // 初始值

// 地图
int Map[RowMax][ColumnMax] = { INIT };
set<pair<int, int>> directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

// 深度优先搜索函数
int DFS(int Map[RowMax][ColumnDMax], int sx, int sy, int ex, int ey, int rows, int columns) {
    stack<pair<int, int>> s; // 用于存储待处理的位置
    set<pair<int, int>> visited; // 记录已访问的位置

    pair<int, int> start = { sx, sy };
    s.push(start);
    visited.insert(start);

    while (!s.empty()) {
        pair<int, int> current = s.top();
        s.pop();

        // 检查是否到达目标位置
        if (current.first == ex && current.second == ey) {
            cout << "YES" << endl;
            return 1;
        }

        // 扩展相邻位置
        for (const auto& dir : directions) {
            int newX = current.first + dir.first;
            int newY = current.second + dir.second;

            // 检查位置是否合法
            if (newX >= 0 && newX < rows && newY >= 0 && newY < columns) {
                pair<int, int> newPos = { newX, newY };
                if (visited.find(newPos) == visited.end() && Map[newX][newY] == 0) {
                    s.push(newPos);
                    visited.insert(newPos); // 标记为已访问
                }
            }
        }
    }

    cout << "NO" << endl; // 如果没有找到路径
    return 0;
}

int main() {
    int r, c;
    int sx, sy, ex, ey;
    cin >> r >> c;
    cin >> sx >> sy >> ex >> ey;

    // 输入地图
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> Map[i][j];
        }
    }

    // 执行 DFS
    DFS(Map, sx, sy, ex, ey, r, c);
    return 0;
}

```
- 求所有路径
  - 分治-结果存储：对可以到达终点的每一条路径都进行存储
  
```C++
#include <stack>
#include <set>
#include <iostream>
#include <vector>

using namespace std;

const int RowMax = 1e3 + 5; // 行最大值
const int ColumnMax = 1e3 + 5; // 列最大值
#define INIT 0 // 初始值

// 地图
int Map[RowMax][ColumnMax] = { INIT };
set<pair<int, int>> directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

// 深度优先搜索函数
void DFS(int x, int y, int ex, int ey, int rows, int columns, vector<pair<int, int>>& path, vector<vector<pair<int, int>>>& allPaths, set<pair<int, int>>& visited) {
    // 如果到达目标位置，存储当前路径
    if (x == ex && y == ey) {
        allPaths.push_back(path);
        return;
    }

    // 扩展相邻位置
    for (const auto& dir : directions) {
        int newX = x + dir.first;
        int newY = y + dir.second;

        // 检查位置是否合法
        if (newX >= 0 && newX < rows && newY >= 0 && newY < columns && Map[newX][newY] == 0) {
            pair<int, int> newPos = { newX, newY };
            if (visited.find(newPos) == visited.end()) {
                // 记录当前路径
                path.push_back(newPos);
                visited.insert(newPos); // 标记为已访问
                // 递归调用 DFS
                DFS(newX, newY, ex, ey, rows, columns, path, allPaths, visited);
                // 回溯
                path.pop_back();
                visited.erase(newPos); // 解除访问标记
            }
        }
    }
}

int main() {
    int r, c;
    int sx, sy, ex, ey;
    cin >> r >> c;
    cin >> sx >> sy >> ex >> ey;

    // 输入地图
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> Map[i][j];
        }
    }

    vector<pair<int, int>> path; // 当前路径
    vector<vector<pair<int, int>>> allPaths; // 所有路径
    set<pair<int, int>> visited; // 记录已访问的位置

    // 将起点加入路径
    path.push_back({sx, sy});
    visited.insert({sx, sy});

    // 执行 DFS
    DFS(sx, sy, ex, ey, r, c, path, allPaths, visited);

    // 输出所有路径
    cout << "All paths from (" << sx << ", " << sy << ") to (" << ex << ", " << ey << "):" << endl;
    for (const auto& p : allPaths) {
        for (const auto& coord : p) {
            cout << "(" << coord.first << ", " << coord.second << ") ";
        }
        cout << endl;
    }

    return 0;
}

```

## 数组算法模板
- **普式DFS,一般用于生成全排列**
```C++
int n;
int path[N]; 
bool st[N];
void dfs(int u)
{
    if(u==n)
    {
        for(int i=0;i<n;i++)printf("%d",path[i]);
        return;
    }
    for(int i=1;i<=n;i++)
    {
        if(!st[i])
        {
            path[u]=i;
            st[i]=true;
            dfs(u+1);
            st[i]=false;
        }
    }
}
```

## 例题

皇后问题
