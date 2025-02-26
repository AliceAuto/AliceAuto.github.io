```cpp
#define sequence vector<char>
#define dict vector<int> 
sequence text;
sequence pat;

int kmp(sequence &text,sequence &pat){
	dict next(pat.size(),0);
	auto getNext = [&](){
		for (int i = 1, j = 0; i < pat.size(); i++) {
			while (j > 0 && pat[i] != pat[j]) j = next[j - 1];
			if (pat[i] == pat[j]) j++;
			next[i] = j;
		}
	};
	getNext();
	for (int i = 0, j = 0; i < text.size(); i++) {
		while (j > 0 && text[i] != pat[j]) j = next[j - 1];
		if (text[i] == pat[j]) j++;
		if (j == pat.size()) return i - pat.size() + 1;
	}
	
}
/*

int main(){
	string t;
	string p;
	cin>>t>>p;
	for(auto c:t) text.push_back(c);
	for(auto c:p) pat.push_back(c);
	cout<<kmp(text,pat)<<endl;


	return 0;
}

*/
```
