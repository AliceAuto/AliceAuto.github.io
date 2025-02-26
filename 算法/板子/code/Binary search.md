
# 二分搜索
> **主要调整在于修改check内的偏序关系**
> **mid 的更新模式决定优先保留左/右边界，而对应要求怎么样的cheak**
```cpp
// 找左边界
int find_left(int l, int r) {
    auto check = [&](int x) {  
        return tar <= x;
    };
    while(l < r) {
        int mid = (l + r) >> 1;
        check(mid) ? r = mid : l = mid + 1;
    }
    return (l <= r && check(l)) ? l : -1;  
}

// 找右边界
int find_right(int l, int r) {
    auto check = [&](int x) {  
        return x<= tar; 
    };
    while(l < r) {
        int mid = (l + r + 1) >> 1;
        check(mid) ? l = mid : r = mid - 1;
    }
    return (l <= r && check(l)) ? l : -1;  
}

```