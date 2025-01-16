[程家贺]
# [转到题目](https://ac.nowcoder.com/acm/problem/283479)_
#### 思路: 分解495的质因数, 3 3 5 11, 发现至少需2个3, 1个5和1个7
#### 分解n个数, 得到一个关于3, 5, 9, 11 每种因子存在状态的数组(共12种), 进行前缀和
#### dp[i][0] 表示1-i个数的12种状态的前缀和
#### tp数组用于映射, 将12个下标对应到12个状态三元组
#### 这里称每种状态为一个状态三元组
#### 没有太大意义, 实战很难打出来
```C++

#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define endl '\n'
typedef long long ll;
#define MAX_INT ll(2e64 - 1)
#define REP(i, s, e) for (int i = (s); i < (e); ++i)
#define OUT(v) for (int k = 0; k < v.size(); ++k) cout << v[k] << ' '; cout << endl;
const int N = 1e5 + 10;

int dp[400010][12]; // 第i个元素的12种状态的前缀和
bool ck(int x, int j, const vector<vector<int>> &tp) { // 检查x分解完和tp[j] 是否相同
    int cc[] = {0, 0, 0}; // 3 9 5 11
    if (x % 3 == 0 && x % 9 != 0) cc[0] = 3;
    else if(x % 9 == 0) cc[0] = 9;
    if (x % 5 == 0) cc[1] = 5;
    if (x % 11 == 0) cc[2] = 11;
    for (int i = 0; i < 3; i++) {
        if (tp[j][i] != cc[i]) return false;
    }
    return true;
}
// contribution 用于计算每个元素对于其他所有数的贡献
int contribution(int x, int n, int idx, bool status, bool status2, vector<vector<int>> &tp) {
    // status 控制是累加前缀还是计算对全部元素的贡献
    // status2 true: 当前是x + 1, false : 当前是 x
    int sum = 0;
    int cc[] = {0, 0, 0}; // 3 9 5 11 // 存储x的状态三元组
    if (x % 3 == 0 && x % 9 != 0) cc[0] = 3;
    else if(x % 9 == 0) cc[0] = 9;
    if (x % 5 == 0) cc[1] = 5;
    if (x % 11 == 0) cc[2] = 11;
    int cc2[]= {0, 0, 0}; // 存储x - 1的状态三元组
    int b = x - 1; // b = x(main中的), 此时contribution的x相当于main中的x + 1
    if (b % 3 == 0 && b % 9 != 0) cc2[0] = 3;
    else if(b % 9 == 0) cc2[0] = 9;
    if (b % 5 == 0) cc2[1] = 5;
    if (b % 11 == 0) cc2[2] = 11;
    bool st = false, st2 = false;
    for (int i = 0; i < 12; i++) {
        if (tp[i][0] + cc[0] > 3 && tp[i][1] + cc[1] > 0 && tp[i][2] + cc[2] > 0) {
            if (tp[i][0] == cc2[0] && tp[i][1] == cc2[1] && tp[i][2] == cc2[2]) st = true; // 表示加到了x的状态的前缀
            if (tp[i][0] == cc[0] && tp[i][1] == cc[1] && tp[i][2] == cc[2]) st2 = true; // 表示加到了x的状态的前缀
            
            if(status) sum += dp[n][i];
            else sum += dp[idx-1][i]; // idx - 1才是之前出现的全部的和
            // 如果是x + 1的情况, 要把sum -1,因为x变成x + 1的过程中, x对应的状态三元组在dp中要-1, 而x+1对应的状态三元组+1, 但是x+1对应的状态三元组不用+1因为这样正好可以避免把自身这个重复元素算上去
            if (status2 && st) sum--, st = false; //
            if (!status2 && st2 && status) sum--, st2 = false;
        }
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> a (n + 1);
    vector<vector<int>> tp {{0, 0, 0}, {3, 0, 0}, {9, 0, 0}, {0, 5, 0}, {0, 0, 11}, 
    {3, 5, 0}, {3, 0, 11}, {9, 5, 0}, {9, 0, 11}, {0, 5, 11}, {3, 5, 11}, {9, 5, 11} };
    REP(i, 1, n + 1) cin >> a[i];
    REP(i, 1, n + 1) REP(j, 0, 12) { // 更新i个前缀
        int x = a[i];
        dp[i][j] += dp[i - 1][j];
        if (ck(x, j, tp)) dp[i][j]++; // 检查自己属于哪种状态, 属于就递增
    }
    int mx = 0; // 算出来的结果是+1后能让结果增加的最大的值
    ll sum = 0;
    REP(i, 1, n + 1) {
        int x = a[i];
        // 计算x对于其他所有数的贡献
        // 同时要将x的那个状态的前缀-1
        int res = contribution(x, n, i, true, false, tp);
        int res2 = contribution(x + 1, n, i, true, true, tp);
        cout << res << ' ' << res2 << endl;
        if (res2 > res) mx = max(mx, res2 - res);
        sum += contribution(x, n, i, false, false, tp); // 这里直接累加前缀, 表示不进行任何+1操作的结果
    }
    cout << sum + mx;
    return 0;
}
```