#include<iostream>
using namespace std;

int calc(int n)
{	
	int i, k = 0;
	for(i = 1; i<=n; i++)
	{
		if(i%2 == 0)
		{
			k += (i-2)/2;
		} 
	}
	return k;	
}

int main()
{
	int T, k = 0;
	cin>>T;
	while(T--)
	{
		int n;
		cin>>n;
		cout<<calc(n)<<"\n";
	}
	return 0;
}