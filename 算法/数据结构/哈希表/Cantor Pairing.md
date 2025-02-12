Cantor配对函数是一种将两个非负整数 \(a\) 和 \(b\) 唯一地配对成一个单一整数的方法。它是一个双射（bijection），意味着它在整数对和单一整数之间创建了一个一一对应的关系。

Cantor配对函数的公式是：

\[
\pi(a, b) = \frac{(a + b)(a + b + 1)}{2} + b
\]

### 工作原理：
- \(a + b\) 用来确定整数对所在的“对角线”位置。
- \(\frac{(a + b)(a + b + 1)}{2}\) 是一个三角数，它表示从 (0, 0) 到当前对角线上的所有点的总数。
- 然后加上 \(b\)，得到该对角线上的具体位置。

#### 例子：
比如我们要配对整数 2 和 3：

1. 计算 \(a + b = 2 + 3 = 5\)。
2. 计算 5 对应的三角数：
   \[
   \frac{5(5 + 1)}{2} = \frac{5 \times 6}{2} = 15。
   \]
3. 然后加上 \(b = 3\)：
   \[
   \pi(2, 3) = 15 + 3 = 18。
   \]

所以，\(\pi(2, 3) = 18\)，意味着整数对 (2, 3) 对应的单一整数是 18。

Cantor配对函数在数学中有广泛的应用，特别是在研究可数性和高维空间时。
```cpp
namespace std {
    template <>
    struct hash<pair<int, int>> {
        size_t operator()(const pair<int, int>& p) const {
            size_t h1 = hash<int>()(p.first);
            size_t h2 = hash<int>()(p.second);
            return (h1 +h2)*(h1+h2+1)/2+h2;
        }
    };
}
```