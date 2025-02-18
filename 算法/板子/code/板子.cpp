#ifndef CODE_H
#define CODE_H
#include <bits/stdc++.h>
using namespace std;


#define I_ERROR 0x3f3f3f3f
#define FastIOS {ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
#define REP(a, b, c, d) for(int a = b; a != c; a += d)
namespace Debug {
    template<typename T>
    void debug(const T& container) {
        for (const auto& e : container) {
            cout << e << " ";
        }
        cout << endl;
    }


    template<typename K, typename V>
    void debug(const std::map<K, V>& mp) {
        for (const auto& e : mp) {
            cout << e.first << ": " << e.second << " ";
        }
        cout << endl;
    }

    template<typename K, typename V>
    void debug(const std::unordered_map<K, V>& umap) {
        for (const auto& e : umap) {
            cout << e.first << ": " << e.second << " ";
        }
        cout << endl;
    }

    template<typename T1, typename T2>
    void debug(const std::pair<T1, T2>& p) {
        cout << "(" << p.first << ", " << p.second << ")" << endl;
    }


    template<typename T1, typename T2, typename T3>
    void debug(const std::tuple<T1, T2, T3>& t) {
        cout << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ")" << endl;
    }

    template <typename T, typename N>
    void debug(T* arr, N n) {
        for (N i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
}


namespace IO {

    std::vector<int> buildLPS(const std::string& pat) {
        int m = pat.length();
        std::vector<int> lps(m, 0);
        int len = 0, i = 1;

        while (i < m) {
            if (pat[i] == pat[len]) {
                len++;
                lps[i] = len;
                i++;
            }
            else {
                if (len) {
                    len = lps[len - 1];
                }
                else {
                    i++;
                }
            }
        }
        return lps;
    }

    size_t kmpSearch(const std::string& text, const std::string& pat, size_t start) {
        int n = text.length(), m = pat.length();
        if (start >= n) return std::string::npos;

        std::vector<int> lps = buildLPS(pat);
        int i = start, j = 0;

        while (i < n) {
            if (text[i] == pat[j]) {
                i++, j++;
            }

            if (j == m) {
                return i - m;
            }
            else if (i < n && text[i] != pat[j]) {
                if (j) {
                    j = lps[j - 1];
                }
                else {
                    i++;
                }
            }
        }
        return std::string::npos;
    }

    template <typename T>
    T stringTo(const std::string& str);

    template <>
    int stringTo<int>(const std::string& str) {
        return std::stoi(str);
    }

    template <>
    float stringTo<float>(const std::string& str) {
        return std::stof(str);
    }

    template <>
    double stringTo<double>(const std::string& str) {
        return std::stod(str);
    }

    template <>
    std::string stringTo<std::string>(const std::string& str) {
        return str;
    }

    template <typename T>
    std::vector<T> split(const std::string& str, const std::string& delim = " ") {
        std::vector<T> res;
        size_t start = 0, end = kmpSearch(str, delim, start);

        while (end != std::string::npos) {
            if (start != end) {
                std::string token = str.substr(start, end - start);
                res.push_back(stringTo<T>(token));
            }
            start = end + delim.length();
            end = kmpSearch(str, delim, start);
        }

        if (start != str.length()) {
            std::string token = str.substr(start);
            res.push_back(stringTo<T>(token));
        }

        return res;
    }

    std::string input() {
        std::string line;
        std::getline(std::cin, line);
        return line;
    }
}

namespace OtherType {

    class BigInt {
    private:
        std::string num;
        bool neg;

    public:
        BigInt() : neg(false), num("0") {}
        BigInt(long long val) {
            if (val < 0) { neg = true; val = -val; }
            else neg = false;
            num = std::to_string(val);
        }
        BigInt(const std::string& str) {
            if (str[0] == '-') { neg = true; num = str.substr(1); }
            else { neg = false; num = str; }
        }

        BigInt abs() const {
            return BigInt(neg ? num.substr(1) : num);
        }

        void normalize() {
            while (num.length() > 1 && num[0] == '0') num = num.substr(1);
            if (num == "0") neg = false;
        }

        void print() const {
            if (neg && num != "0") std::cout << "-";
            std::cout << num;
        }

        BigInt operator+(const BigInt& other) const {
            if (neg == other.neg) {
                std::string res = add(num, other.num);
                return BigInt(neg ? "-" + res : res);
            }
            else if (abs() >= other.abs()) {
                std::string res = sub(num, other.num);
                return BigInt(neg ? "-" + res : res);
            }
            else {
                std::string res = sub(other.num, num);
                return BigInt(other.neg ? "-" + res : res);
            }
        }

        BigInt operator-(const BigInt& other) const {
            if (neg == other.neg) {
                if (abs() >= other.abs()) {
                    std::string res = sub(num, other.num);
                    return BigInt(neg ? "-" + res : res);
                }
                else {
                    std::string res = sub(other.num, num);
                    return BigInt(other.neg ? "-" + res : res);
                }
            }
            else {
                std::string res = add(num, other.num);
                return BigInt(neg ? "-" + res : res);
            }
        }

        BigInt operator*(const BigInt& other) const {
            std::string res = mul(num, other.num);
            bool result_neg = neg != other.neg;
            return BigInt(result_neg ? "-" + res : res);
        }

        BigInt operator/(const BigInt& other) const {
            if (other.num == "0") throw std::invalid_argument("Division by zero.");
            std::string res = div(num, other.num);
            bool result_neg = neg != other.neg;
            return BigInt(result_neg ? "-" + res : res);
        }

        bool operator>=(const BigInt& other) const {
            if (neg && !other.neg) return false;
            if (!neg && other.neg) return true;
            if (neg && other.neg) return abs() <= other.abs();
            return abs() >= other.abs();
        }

        bool operator==(const BigInt& other) const {
            return neg == other.neg && num == other.num;
        }

        bool operator<(const BigInt& other) const {
            if (neg != other.neg) return neg;
            if (num.size() != other.num.size()) return num.size() < other.num.size();
            return num < other.num;
        }

        bool operator<=(const BigInt& other) const {
            return *this < other || *this == other;
        }

    private:
        static std::string add(const std::string& a, const std::string& b) {
            int carry = 0;
            std::string res;
            int i = a.size() - 1, j = b.size() - 1;
            while (i >= 0 || j >= 0 || carry) {
                int sum = carry;
                if (i >= 0) sum += a[i--] - '0';
                if (j >= 0) sum += b[j--] - '0';
                carry = sum / 10;
                res += (sum % 10) + '0';
            }
            std::reverse(res.begin(), res.end());
            return res;
        }

        static std::string sub(const std::string& a, const std::string& b) {
            int borrow = 0;
            std::string res;
            int i = a.size() - 1, j = b.size() - 1;
            while (i >= 0 || j >= 0 || borrow) {
                int diff = (a[i] - '0') - (j >= 0 ? b[j--] - '0' : 0) - borrow;
                if (diff < 0) {
                    diff += 10;
                    borrow = 1;
                }
                else {
                    borrow = 0;
                }
                res += diff + '0';
                i--;
            }
            while (res.size() > 1 && res.back() == '0') {
                res.pop_back();
            }
            std::reverse(res.begin(), res.end());
            return res;
        }

        static std::string mul(const std::string& a, const std::string& b) {
            int n = a.size(), m = b.size();
            std::vector<int> res(n + m, 0);
            for (int i = n - 1; i >= 0; --i) {
                for (int j = m - 1; j >= 0; --j) {
                    int mul = (a[i] - '0') * (b[j] - '0');
                    int sum = mul + res[i + j + 1];
                    res[i + j + 1] = sum % 10;
                    res[i + j] += sum / 10;
                }
            }
            std::string result;
            for (int i : res) {
                if (!(result.empty() && i == 0)) {
                    result += i + '0';
                }
            }
            return result.empty() ? "0" : result;
        }

        static std::string div(const std::string& a, const std::string& b) {
            std::string result;
            std::string temp = a.substr(0, b.size());
            int n = a.size();
            for (int i = b.size(); i <= n; ++i) {
                int quotient = 0;
                while (temp >= b) {
                    temp = sub(temp, b);
                    quotient++;
                }
                result += (quotient + '0');
                if (i < n) temp += a[i];
            }
            return result;
        }
    };

    template <typename T>
    class Fraction {
    private:
        T num;
        T denom;

        T gcd(T a, T b) const {
            while (b != T(0)) {
                T temp = a;
                a = b;
                b = temp % b;
            }
            return a;
        }

        void simplify() {
            if (denom == T(0)) throw std::invalid_argument("Denominator cannot be zero.");
            T gcd_value = gcd(num, denom);
            num /= gcd_value;
            denom /= gcd_value;
            if (denom < T(0)) {
                num = -num;
                denom = -denom;
            }
        }

    public:
        Fraction(T n = 0, T d = 1) : num(n), denom(d) { simplify(); }

        T getNum() const { return num; }
        T getDenom() const { return denom; }

        Fraction operator+(const Fraction& other) const {
            T n = num * other.denom + denom * other.num;
            T d = denom * other.denom;
            return Fraction(n, d);
        }

        Fraction operator-(const Fraction& other) const {
            T n = num * other.denom - denom * other.num;
            T d = denom * other.denom;
            return Fraction(n, d);
        }

        Fraction operator*(const Fraction& other) const {
            T n = num * other.num;
            T d = denom * other.denom;
            return Fraction(n, d);
        }

        Fraction operator/(const Fraction& other) const {
            if (other.num == T(0)) throw std::invalid_argument("Division by zero.");
            T n = num * other.denom;
            T d = denom * other.num;
            return Fraction(n, d);
        }

        void print() const {
            std::cout << num << "/" << denom << std::endl;
        }
    };

}

#endif

using namespace Debug;
using namespace IO;
using namespace OtherType;
int n;
vector<int> vec;

void solve() {
    
    debug(vec);
}
int main() {
    FastIOS;
    
    solve();
    return 0;
}
