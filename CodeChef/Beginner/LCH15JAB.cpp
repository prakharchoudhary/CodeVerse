#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		char s[52];
		int ascii, i;
		int alpha[256] = {0};
		cin>>s;
		if(strlen(s)%2 !=0)
		{
			cout<<"NO";
		}
		else
		{
			for(i=0; s[i]!='\0'; i++)
			{
				ascii = int(s[i]);
				alpha[ascii-1]++; 
			}

			int max = alpha[0];
			for(i=1; i<256; i++)
			{	
				if(alpha[i]>max)
					max = alpha[i];
			}

			if(max == strlen(s)/2)
				cout<<"YES";
			else
				cout<<"NO";
		}
		cout<<"\n";
	}
}