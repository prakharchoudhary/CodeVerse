#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T){
		int n, sum=0;
		cin>>n;
		while(n){
			sum += n%10;
			n = n/10;
		}
		cout<<sum<<"\n";
		T--;
	}
	return 0;
}