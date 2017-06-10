#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T,i;
	cin>>T;
	while(T)
	{
		int num,r,rev = 0;
		cin>>num;
		while(num){
			r = num%10;
			rev = 10*rev + r;
			num = num/10;
		}
		cout<<rev<<"\n";
		T--;
	}
	return 0;
}