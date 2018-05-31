#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int dolls[100000], count[100000]={0}, N, i, odd;
		cin>>N;
		for(i=0; i<N; i++)
		{
			cin>>dolls[i];
			count[dolls[i]] += 1;
		}

		int max = dolls[0];
		for(i=1; i<N; i++)
		{
			if(max<dolls[i])
				max=dolls[i];
		}
		for(i=0; i<max; i++)
		{
			if(count[i+1]%2!=0)
				odd = i+1;
		}
		cout<<odd<<"\n";
	}
}