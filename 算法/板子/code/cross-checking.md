# 对拍器


### **对拍器需要的文件夹架构**
- 数据生成器: **data.cpp**
- 验证做法: **std.cpp**
- 测试做法: **solve.cpp**
- 对拍器: **cross_checker.cpp**


### 对拍器框架 checker.cpp

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    int t = 0;
    while(true){
        //cout<<"test: "<<t++<<endl;
        system("data.exe > data.in");
        system("std.exe < data.in > std.out");
        system("solve.exe <data.in >solve.out");
        if(system("fc std.out solve.out > diff.log"))
        {
            cout<<"WA\n";
            break;
        }
        //cout<<"AC\n";
    }
}
```

### 数据生成器 data.cpp

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
	srand(time(0));
	int x;
	x =rand()%100000000;
	cout<<x<<endl; 
	
}
```

### 验证者(例) std.cpp
```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int sum;
	for(int i = 1;i<=n;i++){
		sum+=1 ;
	}
	cout<<sum<<endl;

}
```

### 待验证(例) solve.cpp

```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	cout<<n<<endl;

}
```