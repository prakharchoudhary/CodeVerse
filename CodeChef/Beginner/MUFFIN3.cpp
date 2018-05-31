#include<iostream>
using namespace std;

int main()
{
	int T, N, max_package;
	cin>>T;
	while(T)
	{
		cin>>N;
		max_package = N/2 + 1;
		cout<<max_package<<"\n";
		T--;		 
	}
	return 0;
} 