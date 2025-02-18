#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<int> vec ={2,31,41,51,1,1,81,1};
    ranges::sort(vec);
    for(auto x:vec){
        cout<<x<<" ";
    }
    cout<<endl;

    return 0;


}
