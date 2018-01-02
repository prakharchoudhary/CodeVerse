#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		float H, cc, ts;
		cin>>H>>cc>>ts;
		if((H > 50) && (cc < 0.7) && (ts > 5600))
			cout<<10<<"\n";
		else if((H > 50) && (cc < 0.7))
			cout<<9<<"\n";
		else if((cc < 0.7) && (ts > 5600))
			cout<<8<<"\n";
		else if((H > 50) && (ts > 5600))
			cout<<7<<"\n";
		else if((H > 50) || (cc < 0.7) || (ts > 5600))
			cout<<6<<"\n";
		else
			cout<<5<<"\n";
	}
}