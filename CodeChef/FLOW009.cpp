#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
	int T, k = 0;
	cin>>T;
	while(T--)
	{
		float a, b;
		double ans;
		cin>>a>>b;
		ans = a*b;
		if(a>1000)
			ans -= 0.1*ans;
		cout<<fixed<<setw(11)<<setprecision(6)<<ans<<"\n";
	}
	return 0;
}