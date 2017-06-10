#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int a, b, c, i, sum = 0;
		cin>>a>>b>>c;
		sum = a+b+c;
		if(a && b && c)
			if(sum == 180)
				cout<<"YES\n";
			else
				cout<<"NO\n";
		else
			cout<<"NO\n";
	}
	return 0;
}