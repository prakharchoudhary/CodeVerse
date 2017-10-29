#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n,m,k,diff;
		cin>>n>>m>>k;
		diff = abs(n-m);
		if(diff<=k)
		{
			diff = 0;
		}
		else{
			diff = diff-k;
		}
		cout<<diff<<"\n";
	}
}