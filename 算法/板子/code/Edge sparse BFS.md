**下面是一个边关系比较稀疏的BFS:**
- **图的存储方式:邻接表**
- **基本数据结构:STL**
- **参数解释:**
  - g: 图的邻接表
  - s: 起点
  - e: 终点


```cpp
/*
    this is the standard BFS algorithm for solving the problem .
    also is a simple model.
*/
void bfs(const unordered_map<int ,vector<int>>& g ,int s,int e){
    queue<int>que;
    unordered_map<int ,bool> vis;
    unordered_map<int,int> pre;   
    vis[s] =true;
    que.push(s);
    while (que.size()){
        auto cur = que.front();
        que.pop();
        if(cur == e){
            for (int i = e; i != s; i = pre[i]){
                cout<<i<<" "; 
            }
            return;
        }
        for(auto nxt:g.at(cur)){
            if(vis[nxt]) continue;
            vis[nxt] = true;
            pre[nxt] = cur;
            que.push(nxt);
        }

    }
    
}
```