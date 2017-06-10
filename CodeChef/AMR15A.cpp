#include<iostream>
using namespace std;

int main()
{
	int T, a[100], lucky=0, unlucky=0;
	cin>>T;
	for(int i = 0; i<T; i++)
	{
		cin>>a[i];
	}

	for(int i = 0; i<T; i++)
	{
		if(a[i]%2 == 0)
			a[i] = 1;
		else
			a[i] = 0;
	}

	for(int i = 0; i<T; i++)
	{
		if(a[i] == 1)
			lucky += 1;
		else
			unlucky += 1;
	}

	if(lucky>unlucky)
		cout<<"READY FOR BATTLE\n";
	else
		cout<<"NOT READY\n";
}