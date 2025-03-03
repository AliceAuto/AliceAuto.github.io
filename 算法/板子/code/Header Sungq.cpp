#ifndef Preproccess
#define Preproccess
#include<bits/stdc++.h>
using namespace std;
#define GET_MACRO(_1, _2, _3, _4, NAME, ...) NAME
#define REP1(d) for (int i = 0; i != (d); ++i)
#define REP2(s,e) for (int i = (s); i != (e); ++i)
#define REP3(s,e,d) for (int i = (s); i != (e); i += (d))
#define REP4(i,s,e,d) for ((i) = (s); (i) != (e); (i) += (d))
#define REP(...) GET_MACRO(__VA_ARGS__, REP4, REP3, REP2, REP1)(__VA_ARGS__)
#define FastIOS {ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
using i64 = long long;
using i128 = __int128;
using pii = pair<int, int>;
using mat = vector<vector<int>>;
using u64 = unsigned long long;
using u128 = __uint128_t;
using ll = i64;
#define f32 float
#define f64 double
#define endl "\n"
#define pi acos(-1)
#define all(v) v.begin(),v.end()
#define pb push_back
#define x first
#define y second
#define inf 0x3f3f3f3f3f3f3f3f
#define INF 
namespace std{
template <>
struct hash<pair<int, int>> {
    u64 operator()(const pair<int, int>& p) const {
        u64 h1 = hash<int>()(p.first);
        u64 h2 = hash<int>()(p.second);
        return (h1 +h2)*(h1+h2+1)/2+h2;
    }
};
}
#define debug(_x) cout << #_x << '=' << _x << endl
#endif


void solve(){
    
}
int main(){
    FastIOS;
    solve();
    return 0;
}