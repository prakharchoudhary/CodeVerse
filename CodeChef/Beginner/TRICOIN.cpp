#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		long long int n, num=0,i=1, count=0;
		cin>>n;
		while(1)
		{
			num = num + i;
			if(num<=n)
			{
				count++;
			}
			else
				break;
			i++;
		}
		cout<<count<<endl;
	}
}