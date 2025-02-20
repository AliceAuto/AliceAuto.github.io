int C(int n, int m) {
    if (m == 0 || m == n) return 1;
    m = min(m, n - m);
    int result = 1;
    for (int i = 1; i <= m; ++i) {
        result = result * (n - i + 1) / i;
    }
    return result;
}