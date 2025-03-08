
---

## 1. 弗罗贝努斯问题

- **定义：**  
  给定一对互质正整数，求它们的线性组合中**最小未达值**（也称硬币问题中的“不可表示金额”）。
- **应用：**  
  - 资源最优化配置  
  - 有限资金下的收益最大化  
  - 寻找最优因子组合

---

## 2. 快速幂算法（Exponentiation by Squaring）

- **目的：**  
  在 \(O(\log n)\) 时间内计算 \(a^n\)，常用于模运算和大数幂运算。
- **核心思想：**  
  利用指数的二进制表示，将幂运算拆分为若干次平方与乘积。
- **示例代码（C++）：**

```cpp
typedef long long LL;
int qmi(int a, int k, int p) {
    LL res = 1;
    while(k) {
        if(k & 1) res = (LL)res * a % p;
        k >>= 1;
        a = (LL)a * a % p;
    }
    return res;
}
```

---

## 3. 快速幂求逆元

- **背景：**  
  用于求模运算中的乘法逆元（当模数为质数且与底数互质时）。
- **原理：**  
  根据费马小定理，\( b^{p-1} \equiv 1 \pmod{p} \) 可推出 \( b^{p-2} \equiv b^{-1} \pmod{p} \)。
- **示例代码（C++）：**

```cpp
typedef long long ll;
ll qmi(int a, int p) {
    int k = p - 2;
    ll res = 1;
    while(k) {
        if(k & 1) res = (ll)res * a % p;
        k >>= 1;
        a = (ll)a * a % p;
    }
    return res;
}
```

---

## 4. 裴蜀定理（扩展欧几里得算法）

- **定义：**  
  对任意整数 \(a\) 和 \(b\)，存在整数 \(x\) 和 \(y\) 使得  
  \[
  ax + by = \gcd(a, b)
  \]
- **用途：**  
  - 求解线性同余方程  
  - 计算模逆元（当模数不为质数时）
- **示例代码（C++）：**

```cpp
void exgcd(int a, int b, int &x, int &y) {
    if(!b) {
        x = 1, y = 0;
        return;
    }
    exgcd(b, a % b, y, x);
    y -= a / b * x;
}
```

---

## 5. 欧拉函数及其应用

### (1) 欧拉函数 \(\varphi(n)\)

- **定义：**  
  表示 \(1\) 到 \(n\) 中与 \(n\) 互质的正整数个数。
- **计算方法：**  
  对 \(n\) 进行质因数分解后，利用公式  
  \[
  \varphi(n) = n \times \prod_{p|n}\left(1 - \frac{1}{p}\right)
  \]
- **示例代码（C++）：**

```cpp
int phi(int x) {
    int res = x;
    for (int i = 2; i <= x / i; i++) {
        if (x % i == 0) {
            res = res / i * (i - 1);
            while(x % i == 0) x /= i;
        }
    }
    if(x > 1) res = res / x * (x - 1);
    return res;
}
```

### (2) 欧拉定理与费马小定理

- **欧拉定理：**  
  若 \(a\) 与 \(n\) 互质，则  
  \[
  a^{\varphi(n)} \equiv 1 \pmod{n}
  \]
- **费马小定理：**  
  当 \(n\) 为质数时，有  
  \[
  a^{n-1} \equiv 1 \pmod{n}
  \]

### (3) 欧拉函数求和

- **思路：**  
  通过筛法预处理质数与欧拉函数值，可快速计算区间内各数的 \(\varphi\) 值之和。

---

## 6. 约数相关算法

### (1) 求一个数的所有约数

- **方法：**  
  枚举 \(1\) 到 \(\sqrt{n}\) 的整数，若 \(i\) 整除 \(n\)，则 \(i\) 与 \(n/i\) 均为约数（注意去重）。
- **示例代码（C++）：**

```cpp
void divisors(int n) {
    for(int i = 1; i <= n / i; i++) {
        if(n % i == 0) {
            cout << i << endl;
            if(i != n / i) cout << n / i << endl;
        }
    }
}
```

### (2) 约数个数与约数之和

- **原理：**  
  若 \( n = p_1^{c_1} \times p_2^{c_2} \times \ldots \times p_k^{c_k} \)  
  - **约数个数：** \((c_1 + 1) \times (c_2 + 1) \times \cdots \times (c_k + 1)\)  
  - **约数之和：** 每个质因数的幂次和相乘得到

---

## 7. 欧几里得算法（辗转相除法）

- **目的：**  
  计算两个数的最大公约数（gcd）。
- **核心公式：**  
  \[
  \gcd(a, b) = \gcd(b, a \bmod b)
  \]
- **示例代码（C++）：**

```cpp
int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}
```

---

## 8. 最小公倍数（LCM）

- **定义：**  
  两个正整数 \(a\) 和 \(b\) 的最小公倍数是能被它们整除的最小正整数。
- **性质：**  
  \[
  \operatorname{lcm}(a, b) \times \gcd(a, b) = a \times b
  \]
- **示例代码（C++）：**

```cpp
int lcm(int a, int b) {
    return a / gcd(a, b) * b; // 先除后乘，防止溢出
}
```

---

## 9. 质数检测与质因数分解

### (1) 质数检测

- **方法：**  
  通过试除法检查 \(x\) 是否存在 \(2\) 到 \(\sqrt{x}\) 的除数。
- **示例代码（C++）：**

```cpp
bool Is_prime(int x) {
    if(x < 2) return false;
    for(int i = 2; i <= x / i; i++)
        if(x % i == 0) return false;
    return true;
}
```

### (2) 质因数分解

- **方法：**  
  利用试除法逐步分解 \(x\)，处理大于 \(\sqrt{x}\) 的质因数（只出现一次）。
- **示例代码（C++）：**

```cpp
void divided(int x) {
    for(int i = 2; i <= x / i; i++) {
        if(x % i == 0) {
            int s = 0;
            while(x % i == 0) {
                x /= i;
                s++;
            }
            printf("%d %d\n", i, s);
        }
    }
    if(x > 1) printf("%d 1\n", x);
    puts(" ");
}
```

---

## 10. 筛质数算法

### (1) 埃氏筛法（Sieve of Eratosthenes）

- **特点：**  
  时间复杂度 \(O(n \log \log n)\)，适合较大范围质数筛选。
- **示例代码（C++）：**

```cpp
void get_primes(int n) {
    for(int i = 2; i <= n; i++) {
        if(!st[i]) {
            primes[cnt++] = i;
            for(int j = i + i; j <= n; j += i)
                st[j] = true;
        }
    }
}
```

### (2) 线性筛法

- **特点：**  
  时间复杂度 \(O(n)\)，每个合数仅被标记一次，同时获得所有质数。
- **示例代码（C++）：**

```cpp
void get_primes_linear(int n) {
    for (int i = 2; i <= n; i++) {
        if(!st[i]) primes[cnt++] = i;
        for (int j = 0; primes[j] <= n / i; j++) {
            st[primes[j] * i] = true;
            if(i % primes[j] == 0) break;
        }
    }
}
```

### (3) 质数定理

- **说明：**  
  在 \(1\) 到 \(n\) 中，质数的数量大致为 \( \frac{n}{\ln n} \)。

---
