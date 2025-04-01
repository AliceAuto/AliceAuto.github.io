**下面是一个点稀疏的BFS:**
- **图的存储方式:邻接矩阵**
- **基本数据结构:STL**
- **参数解释:**
  - g: 图的邻接矩阵
  - s: 起点
  - e: 终点

```cpp
#define all(x) x.begin(),x.end()
#define x first
#define y second


void bfs(const vector<vector<int>>& g,pair<int,int> s,pair<int,int> e){
    int n = g.size();
    int m = g[0].size();
    
    auto checker = [&] (pair<int,int> p){
        if(p.x<0||p.x>=n||p.y<0||p.y>=m)return false;
        else return true;
    };
    vector<vector<bool>>vis(n,vector<bool>(m,0));
    vector<vector<pair<int,int>>>pre(n,vector<pair<int,int>>(m,{-1,-1}));
    queue<pair<int,int>>q;
    q.push(s);
    vis[s.x][s.y] = 1;
    vector<int>dx = {1,0,-1,0};
    vector<int>dy = {0,1,0,-1};
    
    while(!q.empty()){
        auto p = q.front();
        q.pop();
        if(p==e){
            vector<pair<int,int>>path;
            while(p!=s){
                path.push_back(p);
                p = pre[p.x][p.y];
            }
            path.push_back(s);
            reverse(all(path));
            for(auto p:path){
                cout<<p.x<<" "<<p.y<<endl;
            }
            return;
        } 
        for(int i = 0;i<4;i++){
            auto np = make_pair(p.x+dx[i],p.y+dy[i]);
            if(checker(np)&&!vis[np.x][np.y]&&!g[np.x][np.y]){
                q.push(np);
                vis[np.x][np.y] = 1;
                pre[np.x][np.y] = p;
            } 
        }
    }

}
```

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