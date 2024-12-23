#include<bits/stdc++.h>
using namespace std;
int x;
bool check(int n) {

    string s = "";
    while (n > 0) {
        s = char(n % 10 + '0') + s;
        n /= 10;
    }
    if (s.empty()) s = "0";

    stack<string> stk;
    stk.push(s);

    while (!stk.empty()) {
        string t = stk.top();
        stk.pop();

        size_t p = t.find("33");
        if (p != string::npos) {
            t.erase(p, 2);
            stk.push(t);
        } else {
            if (t.empty()) t = "0";
            int num = 0;
      
            for (int i = 0; i < t.size(); ++i) {
                num = num * 10 + (t[i] - '0');
            }
            if (num % 33 == 0) return true;
        }
    }

    return false;
}



void solve() {
	if (x < 33) cout << "NO" << endl;
	else {
		if (x % 33 == 0) cout << "YES" << endl;
		else {
            if (check(x))cout << "YES" << endl;
            else cout << "NO" << endl;
		}
	}


}

int t;
int main() {
	cin >> t;
	while (t--) {
		cin >> x;
		solve();
	}


	return 0;
}