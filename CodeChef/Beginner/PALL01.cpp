#include<iostream>
#include<cstring>
#define SIZE 10000
using namespace std;

int main()
{
	int T, k = 0;
	cin>>T;
	while(T--)
	{
		char n[SIZE];
		int i, flag=1;
		cin>>n;
		int s = strlen(n);
		for(i=0; i<(s/2)+1; i++)
		{
			if(n[i] != n[s-i-1])
			{
				flag = 0;
				break;
			}
		}
		if(flag == 0)
			cout<<"losses\n";
		else
			cout<<"wins\n";
	}
	return 0;
}