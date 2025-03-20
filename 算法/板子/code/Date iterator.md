
2024-11-16日xx贺被蓝桥杯模拟赛的某道日期题目恶心坏了,
于是连夜手搓了这个遍历日期的板子, (纯代码15行), 毕竟咱和python还是比不了
更新:
update on 2024/11/17
封装成了类
##### OS:
我觉得罪魁祸首是每个月的天数不同, 真该死啊, 要是每个月都是30天就好了
##### 代码功能:
给定起始日期和结束日期, 能够遍历得到区间内每一天的日期


```cpp
class Date {
public:
    const int rq[13] = {29, 31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31};  // r[2]平年, rq[0] 是闰年
    bool check(int yy) {
        return ((yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0));
    }
    int yy, mm, dd;
    Date(int year, int month, int day) {  // 不带默认值的构造函数
        yy = year, mm = month, dd = day;
    }
    void nextDay() {
        if ((!check(yy) && dd == rq[mm]) || (check(yy) && mm == 2 ? dd == rq[0] : dd == rq[mm])) {
            dd = 1, mm++;
            if (mm > 12) mm = 1, yy++;
        } else dd++;
    }
    bool isSame(Date d) {
        return d.getDay() == dd && d.getMonth() == mm && d.getYear() == yy;
    }
    void print() const { printf("%d-%02d-%02d\n", yy, mm, dd); }
    int getYear() const { return yy; }
    int getMonth() const { return mm; }
    int getDay() const { return dd; }
};
```


example :
int main() {
    int yy = 2023, mm = 12, dd = 1;   // 起始日期
    int YY = 2024, MM = 12, DD = 31;  // 结束日期
    Date start(yy, mm, dd);
    Date end(YY, MM, DD);
    while (true) {
        start.print();
        if (start.isSame(end)) break;
        start.nextDay();
    }
    return 0;
}
