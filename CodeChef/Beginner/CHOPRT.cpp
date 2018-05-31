#include<iostream>
using namespace std;

int main()
{
	unsigned int T;
	cin>>T;
	while(T--)
	{
		int a,b;
		cin>>a>>b;
		if(a!=b)
		{
			if(a>b)
				cout<<">\n";
			else
				cout<<"<\n";
		}
		else
			cout<<"=\n";
	}
	return 0;
}