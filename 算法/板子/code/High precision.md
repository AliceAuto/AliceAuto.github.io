
---

# 高精度计算实现（C++）

## A + B，要求 A >= 0, B >= 0

```cpp
vector<int> add(const vector<int>& A, const vector<int>& B) {
    vector<int> C;
    int t = 0;
    for (size_t i = 0; i < A.size() || i < B.size(); ++i) {
        if (i < A.size()) t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }
    if (t) C.push_back(t);
    return C;
}
```

---

## A - B，要求 A >= B, A >= 0, B >= 0

```cpp
vector<int> sub(const vector<int>& A, const vector<int>& B) {
    vector<int> C;
    int t = 0;
    for (size_t i = 0; i < A.size(); ++i) {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        t = t < 0 ? 1 : 0;
    }

    // 去除前导0
    while (C.size() > 1 && C.back() == 0)
        C.pop_back();
    return C;
}
```

---

## A * b，要求 A >= 0, b >= 0

```cpp
vector<int> mul(const vector<int>& A, int b) {
    vector<int> C;
    long long t = 0;
    for (size_t i = 0; i < A.size() || t; ++i) {
        if (i < A.size()) t += (long long)A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0)
        C.pop_back();
    return C;
}
```

---

## A * B，高精度乘法

```cpp
vector<int> mul(const vector<int>& A, const vector<int>& B) {
    vector<int> C(A.size() + B.size(), 0);
    for (size_t i = 0; i < A.size(); ++i)
        for (size_t j = 0; j < B.size(); ++j)
            C[i + j] += A[i] * B[j];

    // 处理进位
    for (size_t i = 0; i < C.size(); ++i) {
        if (C[i] >= 10) {
            if (i + 1 >= C.size()) C.push_back(0);
            C[i + 1] += C[i] / 10;
            C[i] %= 10;
        }
    }

    while (C.size() > 1 && C.back() == 0)
        C.pop_back();
    return C;
}
```

---

## A / b = C ... r，要求 A >= 0, b > 0

```cpp
vector<int> div(const vector<int>& A, int b, int& r) {
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; --i) {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }

    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0)
        C.pop_back();
    return C;
}
```

---

## 快速幂：base ^ exp

```cpp
vector<int> quickPow(vector<int> base, int exp) {
    vector<int> res = {1}; // 初始化为1
    while (exp) {
        if (exp & 1)
            res = mul(res, base);
        base = mul(base, base);
        exp >>= 1;
    }
    return res;
}
```

---

