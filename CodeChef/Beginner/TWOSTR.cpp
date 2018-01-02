#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int flag=1;
		string s1, s2;
		cin>>s1>>s2;
		for(int i=0; s1[i]!='\0'; i++)
		{
			if(s1[i] != '?' && s2[i] != '?')
			{
				if(s1[i] != s2[i])
				{
					flag=0;
					break;
				}
			}
		}
		if(flag)
			cout<<"Yes\n";
		else
			cout<<"No\n";
	}
	return 0;
}