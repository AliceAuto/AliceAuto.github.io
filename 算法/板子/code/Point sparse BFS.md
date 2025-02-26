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