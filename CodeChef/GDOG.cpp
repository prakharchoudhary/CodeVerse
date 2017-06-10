#include<iostream>
using namespace std;

int main()
{
	int T, n, k, m, i;
	cin>>T;
	while(T--)
	{
		cin>>n>>k;
		m=0;
		i=1;
		while(i<=k)
		{
			m=(m>(n%i))?m:(n%i);
			i++;
		}
		cout<<m<<"\n";
	}
	return 0;
}