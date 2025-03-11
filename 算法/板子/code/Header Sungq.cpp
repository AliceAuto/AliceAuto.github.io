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
#define int long long
using i64 = long long;
using i128 = __int128;
using pii = pair<int, int>;
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
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
#define inf 0x3f3f3f3f3f3f3f3f
#define INF inf
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

template <typename T>
struct has_iter {
private:
    template <typename U>
    static constexpr decltype(std::declval<U>().begin(), std::true_type{}) test(int);
    template <typename>
    static constexpr std::false_type test(...);
public:
    static constexpr bool value = decltype(test<T>(0))::value;
};

void indent(int d) {
    for (int i = 0; i < d; ++i) std::cout << "    ";
}

template <typename T, typename std::enable_if<!has_iter<T>::value, int>::type = 0>
void dbg(const T& x, int d = 0) {
    std::cout << x;
}
template <typename T, typename std::enable_if<has_iter<T>::value && !has_iter<typename T::value_type>::value, int>::type = 0>
void dbg(const T& x, int d = 0) {
    std::cout << "{";
    bool f = true;
    for (const auto& e : x) {
        if (!f) std::cout << ", ";
        f = false;
        dbg(e, d);
    }
    std::cout << "}";
}
template <typename T, typename std::enable_if<has_iter<T>::value && has_iter<typename T::value_type>::value, int>::type = 0>
void dbg(const T& x, int d = 0) {
    std::cout << "{\n";
    for (const auto& r : x) {
        indent(d + 1);
        dbg(r, d + 1);
        std::cout << "\n";
    }
    indent(d);
    std::cout << "}";
}

#define debug(_x) { \
    std::cout << #_x << " = \n"; \
    dbg(_x); \
    std::cout << "\n"; \
}
#endif
/*

    This Header is written by Guoqing Sun. which is a template for algorithm contest.

*/
void solve()
{
 
}
signed main(){
    FastIOS;
    solve();
    return 0;
}