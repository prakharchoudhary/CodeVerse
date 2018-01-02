#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T)
	{
		float b, ls, s_min, s_max;
		cin>>b>>ls;
		s_min = pow(ls, 2) - pow(b, 2);
		s_max = pow(b, 2) + pow(ls, 2);
		cout<<pow(s_min, 0.5)<<" "<<pow(s_max, 0.5)<<"\n";
		--T;
	}
	return 0;
}