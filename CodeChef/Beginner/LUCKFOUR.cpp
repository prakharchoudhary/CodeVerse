#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T,i;
	cin>>T;
	while(T--)
	{
		int count=0;
		char a[100000];
		cin>>a;
		for(i=0; i<strlen(a); i++){
			if(a[i] == '4')
				++count;
		}
		cout<<count<<"\n";		
	}
	return 0;
}