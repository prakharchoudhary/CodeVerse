#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T)
	{
		int a,b;
		cin>>a>>b;
		int max = a>b?a:b;
		int sum = a+b;
		cout<<max<<" "<<sum<<"\n";
		--T;
	}
	return 0;
}