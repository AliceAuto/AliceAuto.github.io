// 分组背包
int group_knapsack(int n, const vector<vector<int>>& w, const vector<vector<int>>& v, int V) {
    /*
    w : 每组物品的重量
    v : 每组物品的价值
    V : 背包容量
    */
    vector<int> dp(V + 1, 0); // dp[i] 表示容量为 i 时的最大价值
    for (int i = 0; i < n; ++i) {
        vector<int> temp = dp; // 临时保存上一次的状态
        for (int j = 0; j < w[i].size(); ++j) {
            for (int k = V; k >= w[i][j]; --k) {
                temp[k] = max(temp[k], dp[k - w[i][j]] + v[i][j]);
            }
        }
        dp = temp; // 更新 dp 数组
    }
    return dp[V]; // 返回最大价值
}
