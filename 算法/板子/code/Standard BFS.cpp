/*
    this is the standard BFS algorithm for solving the problem .
    also is a simple model.
*/
#include <bits/stdc++.h>
using namespace std;
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
int main(){
   unordered_map<int,vector<int>> g={
        {1,{2,3}},
        {2,{4,5}},
        {3,{6,7}},
   } ;
   bfs(g,1,7);
}