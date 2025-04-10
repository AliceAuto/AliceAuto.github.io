```cpp
#include <vector>
using namespace std;

template<typename T, typename seq = vector<T>>
void cnxt(const seq& pat, vector<int>& nxt) {
    int m = pat.size();
    int j = 0;
    nxt[0] = 0;

    for (int i = 1; i < m; i++) {
        while (j > 0 && pat[i] != pat[j]) {
            j = nxt[j - 1];
        }

        if (pat[i] == pat[j]) {
            j++;
        }

        nxt[i] = j;
    }
}

template<typename T, typename seq = vector<T>>
int kmp(const seq& txt, const seq& pat) {
    vector<int> nxt(pat.size(), 0);
    cnxt(pat, nxt);

    for (int i = 0, j = 0; i < txt.size(); i++) {
        while (j > 0 && txt[i] != pat[j]) {
            j = nxt[j - 1];
        }
        if (txt[i] == pat[j]) {
            j++;
        }
        if (j == pat.size()) {
            return i - pat.size() + 1;
        }
    }
    return -1;
}


```
