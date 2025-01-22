#include<bits/stdc++.h>

int main()
{
	std::vector<int> vec;

	std::string inp;
	getline (std::cin,inp);
	std::istringstream Is (inp);
	int tem;
	while(Is>>tem)vec.push_back(tem);
	std::vector<double> vvec;
	std::transform(vec.begin(),vec.end(),std::back_inserter(vvec),[](int x){return static_cast<double> (x*0.1) ;});
	
	for(auto x: vvec){
		std::cout<<std::fixed<<std::setprecision(2)<<x<<" ";
	}
	return 0;
}