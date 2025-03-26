
# 日期迭代

```cpp

#include <bits/stdc++.h>
using namespace std;


bool leap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
}

int dim(int y, int m) {
    int days[] = {31, (leap(y) ? 29 : 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    return days[m - 1];
}


void nxt(int &y, int &m, int &d) {
    d++;
    if (d > dim(y, m)) {
        d = 1;
        m++;
        if (m > 12) {
            m = 1;
            y++;
        }
    }
}


void prt(int y, int m, int d) {
    printf("%04d-%02d-%02d\n", y, m, d);
}

```