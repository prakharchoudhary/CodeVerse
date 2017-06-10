#include<iostream>
using namespace std;

int min_house(int loc, int max)
{
	int diff;
	diff = loc-max;
	if(diff<0)
		return 0;
	return diff;
}

int max_house(int loc, int max)
{
	int sum;
	sum = loc+max;
	if(sum>100)
		return 100;
	return sum;
}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int M,x,y,houses[100]={0}, cops[10], i, j, count=0, max_houses,min_h, max_h;
		cin>>M>>x>>y;
		for(i=0; i<M; i++)
		{
			cin>>cops[i];
			cops[i]--;
		}
		max_houses = x*y;
		for(i=0; i<M; i++)
		{
			min_h = min_house(cops[i], max_houses);
			max_h = max_house(cops[i], max_houses);
			
			for(j=min_h; j<=max_h; j++)
			{
				houses[j]++;
			}
		}

		for(i=0; i<100; i++)
		{
			if(houses[i]==0)
				count++;
		}

		cout<<count<<"\n";
	}
}