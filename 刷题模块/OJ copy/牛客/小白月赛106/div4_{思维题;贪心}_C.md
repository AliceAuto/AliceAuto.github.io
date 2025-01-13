[JNMC孙国庆]
# [点击转到题目](https://ac.nowcoder.com/acm/contest/97439/C)

## 题目思路:
**首先我们根据题意，可以很容易的想到，边界为0的特殊性。这直接导致了最后的均值都一定是0，因为边界是没有办法变化的。**
**所以我们接下来就是要讨论什么情况下不能让均值为0就可以了**
- **怎么样才能让均值为0呢？**
  - 贪心的想一下，我们就至少要让每一步逐渐 **`逼近`** 0。
    - 那真实情况是怎么样的呢？一个数想逐渐趋近于0，要有一个指向'0'的方向。
      - **也就是如果一个数x大于0，那么它就应该减小，就要有一个数y<x,来引导x趋近0。**
      - 反之亦然。
      - **`极限情况下，的通解是:x相邻的y正负性不能相同 。即(x>0,y<=0) 或 (x<0,y>=0)。`**
      - 针对于单个位置，满足上述条件，就可以保证能将值逐渐趋近0。
      - 所以，我们只需要检查每个位置都符合条件就可以了


## 代码实现:
```c++

#include <bits/stdc++.h>
using namespace std;

#define I_ERROR 0x3f3f3f3f
#define FastIOS {ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}

const int N = 505;
int M[N][N];
int n;
int d[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };

bool notSame(int x, int y) {
    return (x > 0 && y <= 0) || (x < 0 && y >= 0);
}
bool check(int ii, int jj) {
    bool t = true;
    for (int _ = 0; _ < 4; _++) {
        auto [dx, dy] = d[_];
        t &= (notSame(M[ii][jj], M[ii + dx][jj + dy]));
 
    }
    return t;
}
void solve() {
    cin >> n;
    n += 2;
    bool tar = true;
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            cin >> M[i][j];
        }
    }

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (M[i][j] != 0)
                    tar &= check(i, j);
            }
        }
    if (tar)cout << "YES" << endl;
    else cout << "NO" << endl;

}
int main() {
    FastIOS;

    solve();
    return 0;
}
```