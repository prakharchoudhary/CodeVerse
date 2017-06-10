#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int i,s, min, arr[100000],cost=0;
		cin>>s;
		for(i=0; i<s; i++)
		{
			cin>>arr[i];
		}

		min = arr[0];

		for(i=1; i<s-1; i++)
		{
			if(arr[i]<min)
				min = arr[i];
		}

		cost = min*(s-1);
		cout<<cost<<"\n";
	}
	return 0;
}