
 > **Floyd-Warshall 算法本身就能判断负权回路，只需要在算法执行完后检查对角线上的值是否小于 0。如果小于 0，说明存在负权回路。**
```cpp
const int N  =450;
int dp[N][N];
int n;
void init(){
	memset(dp,0x3f,sizeof dp);
	for(int i = 1;i<=n;i++)
	{
		dp[i][i] = min(dp[i][i],0);
	}
}
void add(int a,int b,int c)
{
	dp[a][b] = min(dp[a][b],c);
}

void Floyd(){
	for(int k =1;k<=n;k++){
		for (int i =1;i<=n;i++){
			for(int j = 1;j<=n;j++){
				dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]);			
			}
		}
	}	
}
```