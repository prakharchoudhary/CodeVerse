#include<iostream>
using namespace std;

int findMin(int a, int b)
{
	int min=a;
	if(min>b){
		min = b;
	}
	return min;
}

int findGCD(int a, int b)
{
	int hcf;
	int min = findMin(a,b);
	for(int i = 1; i<=min; i++)
	{
		if(a%i==0 && b%i==0)
			hcf = i;
	}
	return hcf;
}

int main()
{
	int T, n, k, m, i;
	cin>>T;
	while(T--)
	{
		int a, b, gcd, lcm;
		cin>>a>>b;
		gcd = findGCD(a,b);
		lcm = (a*b)/gcd;
		cout<<gcd<<" "<<lcm<<"\n";
	}
	return 0;
}