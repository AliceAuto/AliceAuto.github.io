#include <bits/stdc++.h>
using namespace std;


void shove(int x ,int n) {
    int IntBits[3];
    IntBits[0] = (x /100)%10;
    IntBits[1] = (x/10)%10;
    IntBits[2] = x%10;
    for (int i =0;i<3;i++){
        putchar((IntBits[i]+n)%3+'0');
    }
    cout<<endl;
}
int main() {
    int N;
    cin>>N;
    shove(N,1),shove(N,2);



    return 0;
}