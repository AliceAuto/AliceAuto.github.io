// 0-1背包
int zero_one_knapsack(int n, const vector<int>& w, const vector<int>& v, int V) {
    /*
    w : 物品的重量
    v : 物品的价值
    V : 背包容量
    */
    vector<int> dp(V + 1, 0); // dp[i] 表示容量为 i 时的最大价值
    for (int i = 0; i < n; ++i) {
        for (int j = V; j >= w[i]; --j) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }
    return dp[V]; // 返回最大价值
}

