#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n, m, count=0, flag=0,i, j=0;
		cin>>n;
		int seq[n];
		for(i=0; i<n; i++)
		{
			cin>>seq[i];
		} 
		cin>>m;
		int subseq[m];
		for(i=0; i<m; i++)
		{
			cin>>subseq[i];
		}

		for(i=0; i<n; i++)
		{
			if(seq[i]==subseq[j]){
				count++;
				j++;
			}

			if(count>=m)
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
			cout<<"Yes"<<endl;
		else
			cout<<"No"<<endl;
	}
}