#include<iostream>
using namespace std;

int main()
{
	int T,i;
	cin>>T;
	while(T)
	{
		int num, sum, first, last;
		cin>>num;
		if(num<10)
			cout<<num<<"\n";
		else
			last = num%10;
			while(num){
				first = num%10;
				num = num/10;
			}
			cout<<first + last<<"\n";
		T--;
	}
	return 0;
}