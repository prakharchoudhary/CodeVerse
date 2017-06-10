#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--){
		int dis, a[5][5], i,j;
		float d[3];
		//input of distance
		cin>>dis;
		//input of the coordinates
		for(i=0; i<3; i++)
		{
			cin>>a[i][0]>>a[i][1];
		}
		int k = 0;
		for(i=0; i<2; i++)
		{
			for(j =i+1; j<=2; j++)
			{
				d[k] = pow((a[j][0] - a[i][0]),2) + pow((a[j][1] - a[i][1]),2);
				d[k] = sqrt(d[k]);
				k++;
			}
		}

		int count = 0;
		for(i=0; i<3; i++)
		{
			if(d[i]>dis)
				count++;
		}

		if(count>=2)
			cout<<"\nno";
		else
			cout<<"\nyes";

		cout<<"\n";
	}
	return 0;
}