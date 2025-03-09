

```cpp

int n;
int d[1000000];


int binary_search_l(int x){
    auto check = [&](int mid_){
        return d[mid_]>=x;//开区间改成 >
    };
    int l = 0; int r = n-1;
    while(l<r){
       int mid = (l+r)/2;
       if(check(mid)){
            r = mid;
       } 
       else {
            l = mid+1;
       }
       cout<<l<<" "<<r<<endl;
    }
    return r;
}
int binary_search_r(int x){
    auto check = [&](int mid_){
        return d[mid_]<=x;//开区间改成 <
    };
    int l = 0; int r = n-1;
    while(l<r){
       int mid = (l+r+1)/2;
       if(check(mid)){
            l = mid;
       } 
       else {
            r = mid-1;
       }
       cout<<l<<" "<<r<<endl;
    }
    return l;
}
```