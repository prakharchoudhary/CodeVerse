#include<iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int i, r;
		float inc_price, discounted_price;
		float loss=0.0000, recipes[100000][3];
		cin>>r;
		for(i=0; i<r; i++)
		{
			cin>>recipes[i][0]>>recipes[i][1]>>recipes[i][2];
			inc_price = recipes[i][0] + (recipes[i][2]*recipes[i][0]/100);
			discounted_price = inc_price - (inc_price)*(recipes[i][2]/100);
			loss += (recipes[i][0] - discounted_price) * recipes[i][1];
		}
		cout<<loss<<endl;
	}
}