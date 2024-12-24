[程家贺]
#### https://ac.nowcoder.com/acm/contest/95016/E



### 我也不知道什么算法, 思路就是这么个思路
```C++

#include <bits/stdc++.h>
using namespace std;
#define fast ios ::sync_with_stdio(false), cin.tie(0), cout.tie(0)
typedef long long ll;
#define MAX_INT int(2e31 - 1)
const int N = 1e5 + 10;

void out(vector<int> v) {
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << ' ';
    cout << endl;
}

ll num(ll x) {
    ll res = 0;
    while(x > 0) {
        res += x % 10;
        x /= 10;
    }
    return res;
}

void solve() {
    ll t;
    cin >> t;
    while(t--) {
        ll res = 0;
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        ll l = a + c, r = b + d;
        ll lf = r - l;
        ll cr = 0; // 当前位数-1能增加的值
        ll rs = 0; // 每次变更增加的
        while(l || lf) {
            if (lf % 10 == 0) {
                cr += 9 - (l % 10);
                l /= 10, lf /= 10;
                continue;
            }
            if (lf % 10 + l % 10 > 9) {
                rs += cr + 9 - (l % 10);
                cr = 0; 
            }
            else {
                if (cr - 1 >= 0) {
                    rs += cr - 1 + lf % 10;
                    cr = 9 - (l % 10 + lf % 10 - 1);
                }
                else {
                    rs += lf % 10;
                    cr += 9 - (l % 10 + lf % 10);
                }
            }
            l /= 10, lf /= 10;
        }
        cout << num(a + c) + rs << endl;
    }
}


int main() {
    fast;
    solve();
    return 0;
}

```

**JNMC孙国庆 的思路:`贪心`**
```python

def slove (a,b,c,d):
    sl = a+c
    sr = b+d
   #维护高位和上界

    res = 0

    for _  in range(19):
        if(sr==0):
            break

        bit = sr%10
        sl//=10
        sr//=10

        if (sr<=sl):
            res +=bit
            continue
        res+=9
        sr-=(bit<9)

    return res



t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    print(slove(a,b,c,d))
```