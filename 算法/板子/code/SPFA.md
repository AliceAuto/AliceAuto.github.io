
## 模板
# 负环检测
**如果还需要检测是否存在负环**
- 方式1 :
  - 检测节点被更新的次数,不能超过n-1
- 方式2 :
  - 检测某个最短长度被更新次数,不能超过n-1


```cpp
const int N = 10010;
const int M = 2*N;
int h[N],ne[M],e[M],w[M],idx;

bitset<N> st;
int dist[N];
void init(){
	memset(h,-1,sizeof h);
	idx= 0;
}
void add(int a , int b, int c){
	e[idx] =b;
	w[idx] = c;
	ne[idx] =h[a],h[a] = idx;
	idx++;
}


void spfa(int S,int E){
	memset(dist,0x3f,sizeof dist);
	dist[S] = 0;
	queue<int> q;
	q.push(S);
	st[S] = true;
	while(q.size()){
		auto f = q.front();
		q.pop();
		st[f] = false;
		for(int i = h[f];~i;i = ne[i]){
			int j = e[i];
			if(dist[j]> dist[f] + w[i]){
				if(!st[j])
				{
					dist[j]= dist[f] + w[i];
					q.push(j);
					st[j] = true;
				}
			}
		}
	}
}

```
