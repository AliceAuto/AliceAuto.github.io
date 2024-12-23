 # BFS算法
 

## 算法描述
- 算法原理可参考波的传递，圆在变大时第一个进入圆内的点一定距离圆心最近，因此可以用BFS算法来寻找最短路径。  
- 所需空间为O(2^h)，h为树的高度。
- 虽然BFS的空间复杂度高，但有最短性，因此可以用于寻找最短路径。



## 数据结构选择
- 队列


## 算法步骤
## 容器算法模板


```C++
#include <queue>
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

// 广度优先搜索函数
int BFS(int Map[RowMax][ColumnMax], int sx, int sy, int ex, int ey, int rows, int columns) {
    queue<pair<int, int>> q; // 队列用于存储待处理的位置
    set<pair<int, int>> visited; // 记录已访问的位置

    pair<int, int> start = { sx, sy };
    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();

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
                    q.push(newPos);
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

    // 执行 BFS
    BFS(Map, sx, sy, ex, ey, r, c);
    return 0;
}

```

- 求路径
  - 前导向量法：新增一个前导节点映射数组来实现路径回溯
```C++
#include <stack>
#include <set>
#include <iostream>
#include <vector>

const int RowMax = 1e3 + 5; // 行最大值
const int ColumnMax = 1e3 + 5; // 列最大值
#define INIT 0 // 初始值

// 地图
int Map[RowMax][ColumnMax] = { INIT };
std::set<std::pair<int, int>> directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

// 深度优先搜索函数
bool BFS(int Map[RowMax][ColumnMax], int sx, int sy, int ex, int ey, int rows, int columns, std::vector<std::pair<int, int>>& predecessors) {
    std::stack<std::pair<int, int>> s; // 用于存储待处理的位置
    std::set<std::pair<int, int>> visited; // 记录已访问的位置

    std::pair<int, int> start = { sx, sy };
    s.push(start);
    visited.insert(start);

    while (!s.empty()) {
        std::pair<int, int> current = s.top();
        s.pop();

        // 检查是否到达目标位置
        if (current.first == ex && current.second == ey) {
            return true; // 找到目标
        }

        // 扩展相邻位置
        for (const auto& dir : directions) {
            int newX = current.first + dir.first;
            int newY = current.second + dir.second;

            // 检查位置是否合法
            if (newX >= 0 && newX < rows && newY >= 0 && newY < columns) {
                std::pair<int, int> newPos = { newX, newY };
                if (visited.find(newPos) == visited.end() && Map[newX][newY] == 0) {
                    s.push(newPos);
                    visited.insert(newPos); // 标记为已访问
                    predecessors[newX * columns + newY] = current; // 记录前导节点
                }
            }
        }
    }

    return false; // 如果没有找到路径
}

// 打印路径
void printPath(int sx, int sy, int ex, int ey, const std::vector<std::pair<int, int>>& predecessors) {
    std::vector<std::pair<int, int>> path;
    std::pair<int, int> current = { ex, ey };

    while (current.first != sx || current.second != sy) {
        path.push_back(current);
        current = predecessors[current.first * ColumnMax + current.second];
    }
    path.push_back({ sx, sy });

    // 反向输出路径
    std::cout << "Path: ";
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        std::cout << "(" << it->first << ", " << it->second << ") ";
    }
    std::cout << std::endl;
}

int main() {
    int r, c;
    int sx, sy, ex, ey;
    std::cin >> r >> c;
    std::cin >> sx >> sy >> ex >> ey;

    // 输入地图
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            std::cin >> Map[i][j];
        }
    }

    // 前导节点数组
    std::vector<std::pair<int, int>> predecessors(RowMax * ColumnMax, {-1, -1});

    // 执行 BFS
    if (BFS(Map, sx, sy, ex, ey, r, c, predecessors)) {
        std::cout << "YES" << std::endl;
        printPath(sx, sy, ex, ey, predecessors);
    } else {
        std::cout << "NO" << std::endl; // 如果没有找到路径
    }

    return 0;
}
```






## 数组模板
```C++
queue<int> q;
st[1] = true; // 表示1号点已经被遍历过
q.push(1);

while (q.size())
{
    int t = q.front();
    q.pop();

    for (int i = h[t]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true; // 表示点j已经被遍历过
            q.push(j);
        }
    }
}
```

## 例题

走迷宫 https://www.acwing.com/problem/content/846/
```C++
#inlude <iostream>
#include <cstring>
#include<algorithm>

using namespace std;

const int N = 110;
typedef pair<int, int> PII;
int n, m;
int g[N][N];//地图
int d[N][N];//距离
int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
PII q[N * N];
int  bfs()
{
    q[0]={0,0};
    int hh=0,tt=-1;
    memset(d,-1,sizeof d);
    d[0][0]=0;
    while(hh<=tt)
    {
        auto t=q[hh++];
        for(int i=0;i<4;i++)
        {
            int x=t.first+dx[i],y=t.second+dy[i];
            if(x>=0 && x<n && y>=0 && y<m && g[x][y] == 0 && d[x][y] == -1)
            {
                q[++tt]={x,y};
                d[x][y]=d[t.first][t.second]+1;
            }
        }
    }
    return d[n-1][m-1];
}

int main()
{
    cin >> n >> m;
   for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)
        cin>>g[i][j];
    cout<<bfs()<<endl;
}

```