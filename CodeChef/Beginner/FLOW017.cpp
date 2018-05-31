#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int max1, max2, a, b, c;
		cin>>a>>b>>c;
		if(c>a)
			swap(a,c);
		if(c>b)
			swap(b,c);
		if(b>a)
			swap(a,b);
		cout<<b<<"\n";		
	}
	return 0;
}