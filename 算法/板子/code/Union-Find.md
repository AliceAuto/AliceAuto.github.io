
# 并查集
**下面是并查集的原理原型**
- **如果还需要维护一些 `根属性` 、`叶子属性` 还需要对模版进行改进**
  - 叶子属性：专注于 **find( )** 的修改
  - 根属性: 专注于 **merge( )** 的修改

```cpp
const int N = 10010;
int p[N];

void init(int n) {
    for (int i = 1; i <= n; i++) p[i] = i;
}

int find(int x) {
    return p[x] == x ? x : p[x] = find(p[x]);
}

void merge(int a, int b) {
    p[find(a)] = find(b);
}

bool same(int a, int b) {
    return find(a) == find(b);
}

```