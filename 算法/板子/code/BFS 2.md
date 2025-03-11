**下面是一个边关系比较稀疏的BFS:**


```cpp
const int N  = 1e5;
int e[N],ne[N],h[N],pre[N],idx;
int n ;
void init (){
    memset(h,-1,sizeof h);
}
void add(int a,int b){
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++; 
}
void BFS(){
    queue<int> q;
    q.push(1);
    bitset<N> st;
    st[1] = true;
    memset(pre, -1, sizeof pre);  
    pre[1] = -1; 
    while (q.size())
    {
        auto f = q.front();
        q.pop(); 

        if(f == n){
            vector<int> path;
            for(int cur = n; cur != -1; cur = pre[cur]) {
                path.push_back(cur);
            }
            reverse(path.begin(), path.end());
            for(int x : path) {
                cout << x << " ";
            }
            return;  
        }
        for(int i = h[f]; i!=-1; i= ne[i]){
            int j = e[i];
            if(!st[j]){
                st[j] = true;
                pre[j] = f;  
                q.push(j);
            }
        }
    }

}
```