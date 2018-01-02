#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n, i, Y_flag=0, I_flag=0;
		cin>>n;
		char a[n];
		cin>>a;
		for(i=0; i<n; i++)
		{
			if(a[i]=='Y')
				Y_flag += 1;
			else if(a[i]=='I')
				I_flag += 1;
		}

		if(Y_flag>0)
			cout<<"NOT INDIAN\n";
		else if(I_flag>0)
			cout<<"INDIAN\n";
		else
			cout<<"NOT SURE\n"; 
	}
	return 0;
}