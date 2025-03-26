# 链式前向星 /Forward Star
**一种表示图的,邻接表代码框架**


```cpp
const int N = 1e5+10;
const int M = 2*N;
int h[N] ,e[M],ne[M],idx;
void init(){
    memset(h,-1,sizeof h);
    idx= 0;
}
void add(int a,int b){
    e[idx] = b;
    ne[idx] =h[a],h[a] =idx;
    idx++;
}

```


