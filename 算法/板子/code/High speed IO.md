## 高速IO
> **这个是为了进行高频的简单格式的输入输入**
> **如果是输入输出瓶颈可以尝试，大概会比cin块10倍**

```cpp
inline void fast_io() {
    ios::sync_with_stdio(false);  
    cin.tie(0);  
    cout.tie(0);  
}

template <typename T>
inline T read() {
    T x = 0;
    char c;
    bool neg = false;
    while ((c = getchar()) < '0' || c > '9') {
        if (c == '-') {
            neg = true;
        }
    }
    do {
        x = x * 10 + (c - '0');
    } while ((c = getchar()) >= '0' && c <= '9');
    return neg ? -x : x;
}

template <>
inline double read<double>() {
    double x = 0.0;
    char c;
    bool neg = false;
    while ((c = getchar()) < '0' || c > '9') {
        if (c == '-') {
            neg = true;
        }
    }
    do {
        x = x * 10 + (c - '0');
    } while ((c = getchar()) >= '0' && c <= '9');
    if (c == '.') {
        double frac = 1;
        while ((c = getchar()) >= '0' && c <= '9') {
            frac /= 10;
            x += (c - '0') * frac;
        }
    }
    return neg? -x : x;
}

template <typename T>
inline void write(const T &x) {
    if constexpr (is_integral<T>::value) {
        if (x < 0) {
            putchar('-');
            write(-x);
        } else {
            if (x >= 10) {
                write(x / 10);
            }
            putchar(x % 10 + '0');
        }
    } else if constexpr (is_floating_point<T>::value) {
        printf("%.6f", x);
    }
}
```
>
>example:
>int main() {
>    fast_io(); 
>
>    int t = read<int>();  // 读取数据组数
>
>    while (t--) {
>        double a = read<double>(), b = read<double>();  // 每组输入两个浮点数
>        write(a + b);  // 输出结果
>        putchar('\n');  // 换行
>  }

