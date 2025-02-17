// 多重背包
int multiple_knapsack(int n, const vector<int>& w, const vector<int>& v, const vector<int>& c, int V) {
    /*
    w : 物品的重量
    v : 物品的价值
    c : 每种物品的最大数量
    V : 背包容量
    */
    vector<int> dp(V + 1, 0); // dp[i] 表示容量为 i 时的最大价值
    for (int i = 0; i < n; ++i) {
        for (int k = 1; k <= c[i]; k <<= 1) { // 二进制拆分
            int count = min(c[i] - (k - 1), V / (k * w[i]));
            for (int j = V; j >= k * w[i]; --j) {
                dp[j] = max(dp[j], dp[j - k * w[i]] + k * v[i]);
            }
        }
    }
    return dp[V]; // 返回最大价值
}
