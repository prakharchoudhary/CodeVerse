#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		char s1[200], s2[200];
		int i, min=0, max=0;
		cin>>s1;
		cin>>s2;
		for(i=0; s1[i]!='\0'; i++)
		{
			if(s1[i]=='?' || s2[i]=='?')
			{
				++max;
			}
			else{
				if(s1[i] != s2[i])
				{
					++min;
					++max;
				}
			}
		}
		cout<<min<<" "<<max<<"\n";
	}
}