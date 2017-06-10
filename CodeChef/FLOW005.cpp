#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n, i, notes, q=0, rem;
		cin>>n;
		int a[] = {100, 50, 10, 5, 2, 1};
		for(i=0; i<6; i++)
		{
			q += n/a[i];
			rem = n%a[i];
			if(rem == 0)
				break;
			n = rem;
		}
		cout<<q<<"\n";
	}
	return 0;
}