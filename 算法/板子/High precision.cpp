// This code is used to implement high precision arithmetic.
class HP {
private:
    string intPart, decPart;

    void norm() {
        if (decPart.empty() || all_of(decPart.begin(), decPart.end(), [](char c) { return c == '0'; }))
            decPart.clear();
    }

public:
    HP() : intPart("0"), decPart("") {}

    HP(string val) {
        size_t p = val.find('.');
        if (p != string::npos) {
            intPart = val.substr(0, p);
            decPart = val.substr(p + 1);
        } else {
            intPart = val;
            decPart.clear();
        }
        norm();
    }

    HP(int val) {
        intPart = to_string(val);
        decPart.clear();
    }

    HP(long long val) {
        intPart = to_string(val);
        decPart.clear();
    }

    HP(size_t val) {
        intPart = to_string(val);
        decPart.clear();
    }

    HP(double val) {
        stringstream ss;
        ss << val;
        string s = ss.str();
        size_t p = s.find('.');
        if (p != string::npos) {
            intPart = s.substr(0, p);
            decPart = s.substr(p + 1);
        } else {
            intPart = s;
            decPart.clear();
        }
        norm();
    }

    operator string() const {
        return intPart + (decPart.empty() ? "" : "." + decPart);
    }

    operator double() const {
        return stod(intPart) + (decPart.empty() ? 0.0 : stod("0." + decPart));
    }

    HP operator+(const HP& o) const {
        string resInt = intPart, resDec = decPart;
        int maxDec = max(decPart.size(), o.decPart.size());
        if (decPart.size() < maxDec) resDec.append(maxDec - decPart.size(), '0');
        if (o.decPart.size() < maxDec) resDec.append(maxDec - o.decPart.size(), '0');
        
        int carry = 0, i = resDec.size() - 1;
        while (i >= 0) {
            int sum = resDec[i] - '0' + o.decPart[i] - '0' + carry;
            carry = sum / 10;
            resDec[i] = sum % 10 + '0';
            --i;
        }
        return HP(resInt + "." + resDec);
    }

    HP operator+(int o) const {
        return *this + HP(o);
    }

    HP operator+(long long o) const {
        return *this + HP(o);
    }

    HP operator+(size_t o) const {
        return *this + HP(o);
    }

    HP operator+(double o) const {
        return *this + HP(o);
    }

    HP operator-(const HP& o) const {
        string resInt = intPart, resDec = decPart;
        int maxDec = max(decPart.size(), o.decPart.size());
        if (decPart.size() < maxDec) resDec.append(maxDec - decPart.size(), '0');
        if (o.decPart.size() < maxDec) resDec.append(maxDec - o.decPart.size(), '0');
        
        int borrow = 0, i = resDec.size() - 1;
        while (i >= 0) {
            int diff = resDec[i] - '0' - o.decPart[i] + '0' - borrow;
            if (diff < 0) { diff += 10; borrow = 1; } else borrow = 0;
            resDec[i] = diff + '0';
            --i;
        }
        return HP(resInt + "." + resDec);
    }

    HP operator-(int o) const {
        return *this - HP(o);
    }

    HP operator-(long long o) const {
        return *this - HP(o);
    }

    HP operator-(size_t o) const {
        return *this - HP(o);
    }

    HP operator-(double o) const {
        return *this - HP(o);
    }

    HP operator*(const HP& o) const {
        string resInt = intPart + decPart, oInt = o.intPart + o.decPart;
        vector<int> prod(resInt.size() + oInt.size(), 0);
        
        for (int i = resInt.size() - 1; i >= 0; --i) 
            for (int j = oInt.size() - 1; j >= 0; --j) {
                int mul = (resInt[i] - '0') * (oInt[j] - '0');
                prod[i + j + 1] += mul;
            }
        
        for (int i = prod.size() - 1; i > 0; --i) {
            prod[i - 1] += prod[i] / 10;
            prod[i] %= 10;
        }
        
        string result;
        bool leadingZero = true;
        for (int i = 0; i < prod.size(); ++i) {
            if (leadingZero && prod[i] == 0) continue;
            leadingZero = false;
            result.push_back(prod[i] + '0');
        }
        
        int decLen = decPart.size() + o.decPart.size();
        if (decLen > 0) result.insert(result.size() - decLen, ".");
        
        return HP(result);
    }

    HP operator*(int o) const {
        return *this * HP(o);
    }

    HP operator*(long long o) const {
        return *this * HP(o);
    }

    HP operator*(size_t o) const {
        return *this * HP(o);
    }

    HP operator*(double o) const {
        return *this * HP(o);
    }

    HP operator/(const HP& o) const {
        if (o.intPart == "0" && o.decPart == "0") throw invalid_argument("0不能作除数");
        return *this;  
    }

    HP operator/(int o) const {
        return *this / HP(o);
    }

    HP operator/(long long o) const {
        return *this / HP(o);
    }

    HP operator/(size_t o) const {
        return *this / HP(o);
    }

    HP operator/(double o) const {
        return *this / HP(o);
    }


    HP powIntPart(int exp) const {
        if (exp < 0) throw invalid_argument("指数不能为负数");
        

        string result = "1";  
        string base = intPart;
        while (exp > 0) {
            if (exp % 2 == 1) { 
                result = multiplyStrings(result, base);
            }
            base = multiplyStrings(base, base); 
            exp /= 2; 
        }
        return HP(result);
    }

private:
 
    string multiplyStrings(const string& num1, const string& num2) const {
        int len1 = num1.size(), len2 = num2.size();
        vector<int> result(len1 + len2, 0);
        
     
        for (int i = len1 - 1; i >= 0; --i) {
            for (int j = len2 - 1; j >= 0; --j) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = mul + result[i + j + 1];
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }
        
       
        string res;
        for (int i = 0; i < result.size(); ++i) {
            if (!(res.empty() && result[i] == 0)) {
                res.push_back(result[i] + '0');
            }
        }
        
        return res.empty() ? "0" : res;
    }
	friend istream& operator>>(istream& is, HP& h) {
	    string val;
	    is >> val; 

	    size_t p = val.find('.');
	    if (p != string::npos) {
	        h.intPart = val.substr(0, p); 
	        h.decPart = val.substr(p + 1);
	    } else {
	        h.intPart = val;
	        h.decPart.clear();
	    }
	    h.norm();
	
	    return is;
	}
	
	friend ostream& operator<<(ostream& os, const HP& h) {
	    string str = h.intPart;  
	
	    if (!h.decPart.empty()) {
	        str += "." + h.decPart;
	    }
	
	    if (os.flags() & ios::fixed) {
	        size_t dPos = str.find('.');
	        if (dPos != string::npos) {
	        
	            while (str.back() == '0') str.pop_back();
	
	            if (str.back() == '.') str.pop_back();
	        }
	
	        if (os.precision() > 0) {
	            size_t reqDec = os.precision() - (str.size() - dPos - 1);
	            str.append(reqDec, '0');
	        }
	    }
	
	    os << str;
	    return os;
	}

};



vector <int>  add (vector <int> & A,vector<int> & B){
	int tem = 0 ;
	vector <int> res;
	if(A.size()>B.size())return add(B,A);
	for(int i =0 ; i <B.size();i++){
		tem += B[i];
		if(i<A.size()) tem+=A[i];
		res.push_back(tem%10);
		tem = tem/10; 
	}
	if(tem)res.push_back(tem);
	return res;
}
//A>B
vector<int> sub(vector<int>& A,vector<int > & B){
	int tem = 0;
	vector<int> res;
	for(int i = 0; i < A.size();i++){
		tem =A[i] - tem;
		if(i< B.size()) tem = tem - B[i];
		res.push_back((10+tem)%10);
		if(tem<0)tem =1;
		else tem =0;
	}
	while (res.size()>1 &&res.back() == 0)res.pop_back();
	return res;
}
vector<int> mul (vector<int> & A ,int b){
	vector<int> res ;
	int tem = 0 ;
	 for(int i =0 ;i <A.size()||tem;i++){
	 	if(i<A.size())tem += (A[i]*b);
	 	res.push_back(tem%10);
		tem /=10;
	 }
	return res;
}
vector<int> div(vector<int> A ,int b,int & mod){
	vector<int> res;
	mod= 0 ;
	for(int i = A.size()-1;i>=0;i--){
		mod = 10*mod +A[i];
		res.push_back(mod/b);
		mod%=b;
	}
	reverse(res.begin(),res.end());
	while(res.size()>1&&res.back()==0)res.pop_back();
	return res;
}
#include <iostream>
using namespace std;

/*
example:
    // 1. 创建与初始化测试
    HP h1("123.456"); // 字符串输入，带小数部分
    HP h2(123);       // 整数输入
    HP h3(123456789012345); // 长整型输入
    HP h4(123.456);   // 双精度浮点数输入
    
    cout << "通过字符串 '123.456' 创建的 HP: " << h1 << endl;
    cout << "通过整数 123 创建的 HP: " << h2 << endl;
    cout << "通过长整型创建的 HP: " << h3 << endl;
    cout << "通过双精度浮点数 123.456 创建的 HP: " << h4 << endl;

    // 2. 算术运算测试
    HP h5 = h1 + h2;  // HP + int
    cout << "h1 + h2: " << h5 << endl;

    HP h6 = h1 - h2;  // HP - int
    cout << "h1 - h2: " << h6 << endl;

    HP h7 = h1 * h2;  // HP * int
    cout << "h1 * h2: " << h7 << endl;

    HP h8 = h1 / h2;  // HP / int
    cout << "h1 / h2: " << h8 << endl;

    // 3. 整数部分的指数运算测试
    HP h9 = h1.powIntPart(2);  // 整数部分的指数运算
    cout << "h1 ^ 2: " << h9 << endl;

    // 4. 输入输出流测试
    HP h10;
    cout << "请输入一个数给 HP: ";
    cin >> h10;  // 用户输入
    cout << "您输入的是: " << h10 << endl;

    // 5. 边界情况: 除以零
    try {
        HP h11("0");
        HP h12 = h1 / h11;  // 应该抛出异常
    } catch (const invalid_argument& e) {
        cout << "捕获到异常: " << e.what() << endl;
    }

/*

