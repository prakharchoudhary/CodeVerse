#include<iostream>
#include<cstring>
using namespace std;

int minimum(int x, int y)
{
	int m = x;
	if(m>=y)
	{
		m=y;
	}
	return m;
}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int a=0, b=0;
		char s[100];
		cin>>s;
		int len = strlen(s);
		for(int i=0; i<len; i++)
		{
			if(s[i]=='a')
				a++;
			else if(s[i]=='b')
				b++;
		}
		cout<<minimum(a,b)<<endl;
	}
}
