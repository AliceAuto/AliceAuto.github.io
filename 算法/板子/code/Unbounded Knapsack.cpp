//完全背包

int complate_bp(int n,const vector<int> & w,const vector<int>&v, int V){
    /*
    w :weight
    v :value
    V :Capacity
    */
    vector<int> dp(V + 1, 0); // dp[i]表示容量为i时的最大价值
    for (int i = 0; i < n; ++i) {
        for (int j = w[i]; j <= V; ++j) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }
    return /*res */;
}
