# 括号匹配

**因涉及string的改动,防止右侧失效,需要匹配处理之后回退i**

```cpp
    void match(string & s){
        stack <int> lstk;
        int l ,r;
        for(int i = 0 ;i<s.size();i++){
            if(s[i] =='[')lstk.push(i);
            else if(s[i] == ']'){
                l = lstk.top();
                r = i;
                lstk.pop();
                //pross
                
                i =l-1;
            }
        }
        cout<<s<<endl;
    }
```