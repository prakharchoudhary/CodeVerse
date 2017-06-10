#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int i, n, fact = 1;
		cin>>n;
		for(i=1; i<=n; i++)
		{
			fact *= i;
		}
		cout<<fact<<"\n";
	}
	return 0;
}