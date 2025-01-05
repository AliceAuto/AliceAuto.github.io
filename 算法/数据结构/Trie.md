# Trie(字典树)

## 定义：高效地存储和查找字符串集合的数据结构

## 模板

```C++
int son[N][26], cnt[N], idx;

// 0号点既是根节点，又是空节点
// son[][]存储树中每个节点的子节点
// cnt[]存储以当前节点结尾的单词数量
// idx是节点编号

// 插入一个字符串
void insert(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a';
        if (!son[p][u])
            son[p][u] = ++idx;
        p = son[p][u];
    }
    cnt[p]++; // 当前节点单词数量加一
}
// 查询字符串出现的次数
int query(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a';
        if (!son[p][u])
            return 0;
        p = son[p][u];
    }
    return cnt[p];
}
```

## 分析

idx是节点编号,从0开始,在创建新节点时递增。


## 例题

### 最大异或和  

在给定的整数数组中，找到两个数，使得它们的异或值最大，并输出这个最大值。  
输入格式:第一行输入一个整数N:第二行输入N个整数。  
输出格式：输出一个整数，表示答案。

```C++
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 100010, M = 3100010;

int n;
int a[N], son[M][2], idx;

void insert(int x)
{
    int p = 0;
    for (int i = 30; i >= 0; i -- )
    {
        //&:一个取地址符作用，另一个是引用
        int &s = son[p][x >> i & 1];
        if (!s) s = ++ idx;
        p = s;
    }
}

int search(int x)
{
    int p = 0, res = 0;
    for (int i = 30; i >= 0; i -- )
    {
        int s = x >> i & 1;
        if (son[p][!s])
        {
            res += 1 << i;
            p = son[p][!s];
        }
        //只有与x的当前位不同 res才+=1<<i 因为相同的时候异或为0也就是不加不减，所以跳过
        else p = son[p][s];
    }
    return res;
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ )
    {
        scanf("%d", &a[i]);
        insert(a[i]);
    }

    int res = 0;
    for (int i = 0; i < n; i ++ ) res = max(res, search(a[i]));

    printf("%d\n", res);

    return 0;
}
```
