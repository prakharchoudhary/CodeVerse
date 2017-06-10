#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n;
		cin>>n;
		if(n<10)
			cout<<"What an obedient servant you are!\n";
		else
			cout<<-1<<"\n";
	}
	return 0;
}