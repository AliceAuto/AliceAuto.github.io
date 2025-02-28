#ifndef Preproccess
#define Preproccess
#include<bits/stdc++.h>
using namespace std;
#define REP(a,b,c,d) for (a = b;a!=c;a+=d)
#define FastIOS {ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
#define i32 int
#define i64 long long
#define i128 __int128
#define f32 float
#define f64 double
#define int long long
#define endl "\n"
#define pi acos(-1)
#define all(v) v.begin(),v.end()
#define pb push_back
#define pii pair<int,int>
#define x first
#define y second
template <>
struct std::hash<pair<int, int>> {
    unsigned i64 operator()(const pair<int, int>& p) const {
        unsigned i64 h1 = hash<int>()(p.first);
        unsigned i64 h2 = hash<int>()(p.second);
        return (h1 +h2)*(h1+h2+1)/2+h2;
    }
};
#endif