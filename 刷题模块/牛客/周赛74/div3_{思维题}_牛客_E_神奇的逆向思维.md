[JNMC张富涵]
# [转到题目](https://ac.nowcoder.com/acm/contest/99458/E)

# 题目思路:
**题目说明，把数组转化为严格递增或者严格递减的数组，其中有一部分是不需要排序的。**
此时我们只需要找到不需要排序的那些数组的最大长度是否大于题目要求的长度即可，就是（排序前后顺序没有变化的那些数字）比如 12 3 8 7 6 5  中8 7 6 5 排序前后 8 7 6 5是的顺序是不变的（8一定在7的左边 7一定在6的左边）也就是说排序前和排序后两个的顺序差都是1
  -先是输入，在输入的时候判断是否有重复的数字，有重复的数字的话就直接输出no
  for (int i = 1; i <= n; i++)
    {
        cin >> b[i];
        r.insert(b[i]);   //把输入的数字存到set里面，利用set排序
        if(e[b[i]])bq=1;    
        e[b[i]]++;
        
    } 
     if(bq)
    {
        cout<<"NO"<<endl;
        return ;
    }
  - 再就是获取数字排序之后在第几位
    int index=1;
    for (auto i:r) j[i] = index++;
  -然后我们就可以暴力枚举获取最长的严格递增或者递减的数组有多少
   for (int i = 2; i <= n; i++)
    {
        if (j[b[i]] == j[b[i - 1]]+1)z++;  
        else
        {
            ma1 = max(ma1, z);
            z = 1;
        }
        if (j[b[i]] + 1 == j[b[i - 1]])j1++;
        else
        {
            mi1 = max(mi1, j1);
            j1 = 1;
        }
    }
    mi1 = max(mi1, j1);
    ma1 = max(ma1, z);
  - 最后再判断即可
   if (mi1 >= m || ma1 >= m)cout << "YES" << endl;
    else cout << "NO" << endl;
  
**完整代码如下**
#include<iostream>
#include<cmath>
#include<set>
#include<map>
#include<cstring>
#include<algorithm>
using namespace std;
void solve()
{
  
    map<long long, int>j;
    map<long long, int>e;
    set<long long>r;
    int n, m;
    cin >> n >> m;
    int mi1 = 0;
    int ma1 = 0;
    int bq=0;
    int z = 1;
    int j1 = 1;
    int b[200005] = { 0 };
    for (int i = 1; i <= n; i++)
    {
        cin >> b[i];
        r.insert(b[i]);
        if(e[b[i]])bq=1;
        e[b[i]]++;
        
    }
    int index=1;
    if(bq)
    {
        cout<<"NO"<<endl;
        return ;
    }
    for (auto i:r) j[i] = index++;
    
    for (int i = 2; i <= n; i++)
    {
        
        if (j[b[i]] == j[b[i - 1]]+1)z++;
        else
        {
            ma1 = max(ma1, z);
            z = 1;
        }
        if (j[b[i]] + 1 == j[b[i - 1]])j1++;
        else
        {
            mi1 = max(mi1, j1);
            j1 = 1;
        }
    }
    
    mi1 = max(mi1, j1);
    ma1 = max(ma1, z);
    //cout << mi1 << " " << ma1 << endl;
    if (mi1 >= m || ma1 >= m)cout << "YES" << endl;
    else cout << "NO" << endl;



}
int main()
{
    int t;
    cin >> t;
    while (t--)solve();
    return 0;


}






