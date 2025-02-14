template <typename T> 
class Pattern {
private:
	T patt;
	std::vector<int> next;
	void get_next_array() {
		int m = patt.size();
		next.resize(m);
		next[0] = 0;
		for (int i = 1, j = 0; i < m; i++) {
			while (j>0&&patt[i] != patt[j]) j = next[j - 1];
			if (j>0&&patt[i] == patt[j] )j++;
			next[i] = j;
		}
	}
public:
	Pattern(const T&pat):patt(pat) {
		get_next_array();
	}
	std::vector<int> KMP(const T &text) {
		std::vector<int> res;
		int t = text.size();
		int m = patt.size();
		for (int i = 0, j = 0; i < t; i++) {
			while (j>0&& patt[j] != text[i])j = next[j - 1];
			if (j<m&&patt[j] ==text[i])j++;
			if (j == m)
			{
				res.push_back(i-j+1);
			
				j = next[j - 1];
			}
		}
		return res;
	}
};
/*
example:

	std::string text;
	std::string pattern;
    
    # Input:
	std::cin >> text;
	std::cin >> pattern;

	Pattern<std::string> patt (pattern);
	std::vector<int> a = patt.KMP(text);

	for (auto i : a) {
		std:: cout << i << " ";
	}
    
    # Output:
	std::cout << std::endl;

	return 0;

*/