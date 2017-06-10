#include <iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int m,n,k, temp, no=0, both=0;
		int total[101]={0};
		cin>>n>>m>>k;
		for(int i=1; i<=m; i++)
		{
			cin>>temp;
			total[temp]++;
		}

		for(int i=1; i<=k; i++)
		{
			cin>>temp;
			total[temp]++;
		}  

		for(int i=1; i<=n; i++)
		{
			// cout<<total[i]<<" ";
			if(total[i]==0)
				no++;
			else if(total[i]==2)
				both++;
		}
		cout<<both<<" "<<no<<endl;
	}
	return 0;
}