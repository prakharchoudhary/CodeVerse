#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int a, i, flag=1;
		cin>>a;
		for(i = 2; i<=a/2; i++)
		{
			if(a%i == 0)
			{
				flag = 0;
				break;
			}
		}
			if(flag == 0)
				cout<<"no\n";
			else
				cout<<"yes\n";
	}
	return 0;
}