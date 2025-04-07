
2024-11-16日xx贺被蓝桥杯模拟赛的某道日期题目恶心坏了,
于是连夜手搓了这个遍历日期的板子, (纯代码15行), 毕竟咱和python还是比不了
更新:
update on 2024/11/17
:封装成了类
update one 2025/04/07
:精简模板, 更容易理解, 去掉不常用成员函数, 仅保留核心日期迭代函数nextDay

##### OS:
我觉得罪魁祸首是每个月的天数不同, 真该死啊, 要是每个月都是30天就好了
##### 代码功能:
给定起始日期和结束日期, 能够遍历得到区间内每一天的日期


```cpp
#include <bits/stdc++.h>
using namespace std;

class Date {
public:
    const int days[13] = {0, 31, (leap(yy) ? 29 : 28), 31, 30, 31, 30,31, 31, 30, 31, 30, 31};
    bool leap(int y) {
        return ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0));
    }
    Date(int y, int m, int d) {  // 不带默认值的构造函数
        yy = y, mm = m, dd = d;
    }
    int yy, mm, dd;
    void nextDay() {
        dd ++ ;
        if (dd > days[mm]) {
            dd = 1;
            mm ++ ;
            if (mm > 12) mm = 1, yy ++ ;
        }
    }
};

int main() {
    int yy = 2023, mm = 12, dd = 1;   // 起始日期
    Date start(yy, mm, dd);
    cout << start.dd << endl;
    start.nextDay();
    cout << start.dd << endl;
    return 0;
}
```

