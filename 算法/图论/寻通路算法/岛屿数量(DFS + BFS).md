https://kamacoder.com/problempage.php?pid=1171

"""
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，你需要计算岛屿的数量。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。

后续 N 行，每行包含 M 个数字，数字为 1 或者 0。

输出描述  
输出一个整数，表示岛屿的数量。如果不存在岛屿，则输出 0。  
输入示例  
4 5  
1 1 0 0 0  
1 1 0 0 0  
0 0 1 0 0  
0 0 0 1 1  
输出示例  
3

"""

``` C++
#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;

void bfs(vector<vector<int>> &g, vector<vector<bool>> &us, int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y}), us[x][y] = true;
    int dx[] = {0, -1, 0, 1}, dy[] = {-1, 0, 1, 0}; // 顺时针
    while(!q.empty()) {
        int a = q.front().first, b = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int xx = a + dx[i], yy = b + dy[i];
            if (g[xx][yy] == 1 && !us[xx][yy]) {
                us[xx][yy] = true;
                q.push({xx, yy});
            }
        }
    }
}

void dfs (vector<vector<int>> &g, vector<vector<bool>> &us, int x, int y) {
    int dx[] = {0, -1, 0, 1}, dy[] = {-1, 0, 1, 0};
    for (int i = 0; i < 4; i++) {
        int xx = x + dx[i], yy = y + dy[i];
        if (g[xx][yy] == 1 && !us[xx][yy]) {
            us[xx][yy] = 1;
            dfs(g, us, xx, yy);
        }
    }
}

int main() {
    int res = 0;
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 2, vector<int> (m + 2, 0));
    vector<vector<bool>> us(n + 2, vector<bool> (m + 2, false));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> g[i][j];
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (g[i][j] == 1 && !us[i][j]) {
                dfs(g, us, i, j);
                //bfs(g, us, i, j);           
                res++;
            }
        }
    }
    cout << res << endl;
    return 0;
}

```