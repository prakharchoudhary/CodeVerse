#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int i, n, a[100000];
		cin>>n;
		for(i = 0; i<n; i++){
			cin>>a[i];
		}

		int min = 32468543;
		for(i = 0; i<n; i++)
		{
			if(min>a[i])
				min = a[i];
		}

		int min2 = 32468543;	
		for(i = 0; i<n; i++)
		{
			if(min2>a[i] && a[i]>min)
				min2 = a[i];
		}

		cout<<min + min2<<"\n"; 
	}
	return 0;
}