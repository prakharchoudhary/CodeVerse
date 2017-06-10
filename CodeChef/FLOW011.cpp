#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		float n, da, hra, total;
		cin>>n;
		if(n>=1500)
		{
			da = 0.98*n;
			hra = 500;
		}
		else
		{
			da = 0.9*n;
			hra = 0.1*n;
		}
		cout<<n + hra + da<<"\n";
	}
	return 0;
}